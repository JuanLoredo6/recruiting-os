#!/usr/bin/env bash
# Crea la release de GitHub de un tag con las notas de su sección del CHANGELOG.
# Lo corre el workflow .github/workflows/release.yml cada vez que se sube un tag vX.Y.Z.
# También se puede correr a mano desde la raíz del repo: bash .github/scripts/release-desde-changelog.sh v0.4.0
# Con SOLO_REVISAR=1 no crea nada: muestra el título y las notas que usaría.
# Recruiting OS · Licencia MIT (ver LICENSE en la raíz del repo).
#
# Falla (y la release no se crea) si:
# - el tag no existe, no es anotado o no está en la historia de main;
# - el CHANGELOG no tiene la sección «## [X.Y.Z] - AAAA-MM-DD» o el link «[X.Y.Z]: ...»;
# - después de crearla, queda algún tag vX.Y.Z sin release en GitHub.
# Si la release ya existe, no la toca y solo revisa que no falte ninguna.
set -euo pipefail

TAG="${1:?Uso: release-desde-changelog.sh vX.Y.Z}"
REPO_URL="https://github.com/JuanLoredo6/recruiting-os"
[[ "$TAG" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]] || { echo "::error::El tag $TAG no tiene la forma vX.Y.Z"; exit 1; }
VERSION="${TAG#v}"

error() { echo "::error::$1"; exit 1; }

# 1. El tag existe, es anotado y está en main.
git rev-parse -q --verify "refs/tags/$TAG" >/dev/null || error "No existe el tag $TAG. Crealo con: git tag -a $TAG -m \"$TAG: <título>\""
[ "$(git cat-file -t "refs/tags/$TAG")" = "tag" ] || error "El tag $TAG no es anotado. Borralo y crealo con: git tag -a $TAG -m \"$TAG: <título>\""
git fetch -q origin main
git merge-base --is-ancestor "$TAG" origin/main || error "El tag $TAG apunta a un commit que no está en main. Mergeá primero y después creá el tag."

# 2. La sección y el link del CHANGELOG.
NOTAS="$(mktemp)"
# Sin \r (copias de Windows) y sin líneas en blanco al principio ni al final.
tr -d '\r' < CHANGELOG.md | awk -v v="$VERSION" '
  index($0, "## [" v "] - ") == 1 { dentro = 1; next }
  dentro && /^## \[/ { exit }
  dentro && /^\[[^]]+\]: / { exit }
  dentro { lineas[++n] = $0 }
  END {
    i = 1; while (i <= n && lineas[i] == "") i++
    while (n >= i && lineas[n] == "") n--
    for (; i <= n; i++) print lineas[i]
  }
' > "$NOTAS"
[ -s "$NOTAS" ] || error "CHANGELOG.md no tiene la sección «## [$VERSION] - AAAA-MM-DD» con contenido."
grep -q "^\[$VERSION\]: " CHANGELOG.md || error "CHANGELOG.md no tiene el link «[$VERSION]: $REPO_URL/compare/...» al final."

ANTERIOR="$(git describe --tags --abbrev=0 --match 'v*.*.*' "$TAG^" 2>/dev/null || true)"
if [ -n "$ANTERIOR" ]; then
  printf '\n**Cambios completos:** %s/compare/%s...%s\n' "$REPO_URL" "$ANTERIOR" "$TAG" >> "$NOTAS"
fi

# 3. El título sale del mensaje del tag: «v0.4.0: vista del cliente…» → «v0.4.0 · Vista del cliente…».
ASUNTO="$(git for-each-ref "refs/tags/$TAG" --format='%(contents:subject)')"
DESCRIPCION="${ASUNTO#"$TAG: "}"
DESCRIPCION="${DESCRIPCION#"$TAG"}"
[ -n "$DESCRIPCION" ] || error "El mensaje del tag está vacío. Usá: git tag -a $TAG -m \"$TAG: <título>\""
TITULO="$TAG · ${DESCRIPCION^}"

# Es la última solo si es la versión más alta.
MAS_ALTA="$(git tag -l 'v*.*.*' | sort -V | tail -1)"
ULTIMA=false; [ "$MAS_ALTA" = "$TAG" ] && ULTIMA=true

if [ "${SOLO_REVISAR:-0}" = "1" ]; then
  echo "Título: $TITULO"
  echo "Última: $ULTIMA"
  echo "--- notas ---"
  cat "$NOTAS"
  exit 0
fi

# 4. Crear la release (si no existe).
if gh release view "$TAG" >/dev/null 2>&1; then
  echo "La release $TAG ya existe: no se toca."
else
  gh release create "$TAG" --verify-tag --title "$TITULO" --notes-file "$NOTAS" --latest="$ULTIMA"
  echo "Release creada: $REPO_URL/releases/tag/$TAG"
fi

# 5. Ningún tag sin release.
FALTAN=""
for t in $(git tag -l 'v*.*.*'); do
  gh release view "$t" >/dev/null 2>&1 || FALTAN="$FALTAN $t"
done
[ -z "$FALTAN" ] || error "Estos tags no tienen release en GitHub:$FALTAN. Corré el workflow «Release» a mano con cada uno."
echo "Todos los tags tienen su release."
