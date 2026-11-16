# Cómo se publica una versión

Para quien mantiene el Recruiting OS. Una versión está publicada cuando tiene las tres cosas en GitHub: el cambio en `main`, el tag `vX.Y.Z` y la release con sus notas. La release la crea sola el workflow `Release` al subir el tag, así que un tag nunca queda sin release.

## Pasos

1. **CHANGELOG, dentro del PR.** Antes de mergear, pasá lo de `## [Sin publicar]` a una sección nueva y sumá su link al final:

   ```markdown
   ## [Sin publicar]

   ## [0.5.0] - 2026-12-01

   Una línea que resuma la versión.

   ### Agregado
   ...

   [Sin publicar]: https://github.com/JuanLoredo6/recruiting-os/compare/v0.5.0...HEAD
   [0.5.0]: https://github.com/JuanLoredo6/recruiting-os/compare/v0.4.0...v0.5.0
   ```

   Versión menor (`0.5.0`) si cambia el modelo de datos del tablero o suma algo nuevo; parche (`0.4.1`) si solo corrige.

2. **Mergeá el PR a `main`** y actualizá tu copia: `git checkout main && git pull`.

3. **Creá el tag anotado y subilo.** El mensaje es el título de la release:

   ```bash
   git tag -a v0.5.0 -m "v0.5.0: vista del cliente en Google Sheets y Drive"
   git push origin v0.5.0
   ```

4. **Comprobá que quedó publicada.** El workflow tarda menos de un minuto:

   ```bash
   gh run list --workflow release.yml --limit 1
   gh release view v0.5.0
   ```

   Si el workflow falló, el error dice qué falta (la sección del CHANGELOG, el link, un tag sin anotar o fuera de `main`). Corregilo y volvé a correrlo desde Actions → Release → Run workflow, con el mismo tag.

## Lo que revisa el workflow

- El tag tiene la forma `vX.Y.Z`, es anotado y apunta a un commit que está en `main`.
- El CHANGELOG tiene `## [X.Y.Z] - AAAA-MM-DD` con contenido y el link `[X.Y.Z]: ...`.
- Crea la release con esas notas, el título del tag y el link a los cambios desde la versión anterior. Solo la marca como la última si es la versión más alta.
- Si la release ya existe, no la toca.
- Al final, falla si queda **algún** tag sin release, aunque sea de otra versión.

Para ver qué publicaría sin crear nada: `SOLO_REVISAR=1 bash .github/scripts/release-desde-changelog.sh v0.5.0`.
