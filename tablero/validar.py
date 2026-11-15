#!/usr/bin/env python3
"""Valida busquedas/busquedas.json contra el modelo de datos de CLAUDE.md.

Lo llama tablero/sincronizar.sh. Solo usa la biblioteca estándar.

Uso: python validar.py <ruta al JSON>

Salida:
  0  todo bien
  1  el archivo no es JSON válido (sincronizar.sh no regenera datos.js)
  2  es JSON válido pero no respeta el modelo de datos (datos.js se regenera igual)
Los problemas se escriben en stderr, uno por línea, para que Claude los corrija.
"""
import json
import re
import sys

FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FECHA_HORA = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$")
ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
AREAS = {"producto", "atencion"}
ESTADOS = {"arranque", "abierta", "terna", "oferta", "pausada", "cerrada"}
RESULTADOS = {"cubierta", "cubierta-por-otro", "cancelada", "desierta"}
ETAPAS = {"identificado", "contactado", "screening", "entrevista-cliente", "terna",
          "oferta", "contratado", "descartado", "retirado"}
CON_MOTIVO = {"descartado", "retirado"}
DEVOLUCIONES = {"no-aplica", "pendiente", "enviada"}
PRIORIDADES = {"alta", "media", "baja"}
FUENTES = {"gmail", "calendar"}
CONTEO = ("cumple", "parcial", "noCumple", "falta")


def main(ruta):
    try:
        with open(ruta, encoding="utf-8") as f:
            datos = json.load(f)
    except json.JSONDecodeError as e:
        print(f"busquedas.json no es JSON válido: {e.msg} (línea {e.lineno}, columna {e.colno}). "
              "tablero/datos.js NO se actualizó.", file=sys.stderr)
        return 1

    problemas = []

    def fecha(valor, donde, nula=True, hora=False):
        if valor is None and nula:
            return
        patron = FECHA_HORA if hora else FECHA
        if not isinstance(valor, str) or not patron.match(valor):
            formato = "AAAA-MM-DDTHH:MM" if hora else "AAAA-MM-DD"
            problemas.append(f"{donde}: fecha {valor!r} no tiene el formato {formato}")

    def historial(lista, donde):
        if lista is None:
            return
        if not isinstance(lista, list):
            problemas.append(f"{donde}: historial tiene que ser una lista")
            return
        for j, h in enumerate(lista):
            if not isinstance(h, dict) or not h.get("texto"):
                problemas.append(f"{donde}: historial[{j}] sin texto")
                continue
            fecha(h.get("fecha"), f"{donde}, historial[{j}]", nula=False)
            fuente = h.get("fuente")
            if fuente is not None and fuente not in FUENTES:
                problemas.append(f"{donde}: historial[{j}] con fuente {fuente!r}")

    def ident(valor, donde):
        if not isinstance(valor, str) or not ID.match(valor):
            problemas.append(f"{donde}: id {valor!r} tiene que ir en minúsculas, sin tildes y con guiones")

    if not isinstance(datos, dict):
        print("busquedas.json tiene que ser un objeto con clientes, búsquedas y acciones.", file=sys.stderr)
        return 2

    if datos.get("actualizado"):
        fecha(datos["actualizado"], "actualizado", hora=True)

    listas = {}
    for clave in ("clientes", "busquedas", "acciones"):
        valor = datos.get(clave)
        if not isinstance(valor, list):
            problemas.append(f"falta la lista '{clave}'")
            valor = []
        listas[clave] = valor

    ids_clientes = set()
    for i, c in enumerate(listas["clientes"]):
        if not isinstance(c, dict):
            problemas.append(f"clientes[{i}] no es un objeto")
            continue
        cid = c.get("id")
        ident(cid, f"clientes[{i}]")
        if cid in ids_clientes:
            problemas.append(f"cliente {cid}: id repetido")
        ids_clientes.add(cid)
        if not c.get("nombre"):
            problemas.append(f"cliente {cid}: falta el nombre")

    ids_busquedas = set()
    candidatos_por_busqueda = {}
    for i, b in enumerate(listas["busquedas"]):
        if not isinstance(b, dict):
            problemas.append(f"busquedas[{i}] no es un objeto")
            continue
        bid = b.get("id")
        donde = f"búsqueda {bid or i}"
        ident(bid, f"busquedas[{i}]")
        if bid in ids_busquedas:
            problemas.append(f"{donde}: id repetido")
        ids_busquedas.add(bid)
        if b.get("cliente") not in ids_clientes:
            problemas.append(f"{donde}: el cliente {b.get('cliente')!r} no está en 'clientes'")
        if b.get("area") not in AREAS:
            problemas.append(f"{donde}: area {b.get('area')!r} no es una de {sorted(AREAS)}")
        estado = b.get("estado")
        if estado not in ESTADOS:
            problemas.append(f"{donde}: estado {estado!r} no es uno de {sorted(ESTADOS)}")
        resultado = b.get("resultado")
        if estado == "cerrada" and resultado not in RESULTADOS:
            problemas.append(f"{donde}: está cerrada y su resultado {json.dumps(resultado)} "
                             f"no es uno de {sorted(RESULTADOS)}")
        if estado != "cerrada" and resultado is not None:
            problemas.append(f"{donde}: tiene resultado {resultado!r} pero no está cerrada")
        fecha(b.get("abierta"), f"{donde}, abierta", nula=False)
        fecha(b.get("objetivoCierre"), f"{donde}, objetivoCierre")
        fecha(b.get("ultimaNovedad"), f"{donde}, ultimaNovedad")
        historial(b.get("historial"), donde)

        candidatos = b.get("candidatos")
        if candidatos is None:
            candidatos = []
        if not isinstance(candidatos, list):
            problemas.append(f"{donde}: 'candidatos' tiene que ser una lista")
            candidatos = []
        ids_cand = set()
        contratados = 0
        for k, c in enumerate(candidatos):
            if not isinstance(c, dict):
                problemas.append(f"{donde}: candidatos[{k}] no es un objeto")
                continue
            cid = c.get("id")
            dc = f"{donde}, candidato {cid or k}"
            ident(cid, f"{donde}, candidatos[{k}]")
            if cid in ids_cand:
                problemas.append(f"{dc}: id repetido en la búsqueda")
            ids_cand.add(cid)
            anonimo = isinstance(cid, str) and cid.startswith("anonimo-")
            if not c.get("nombre") and not anonimo:
                problemas.append(f"{dc}: falta el nombre")
            if anonimo and c.get("nombre"):
                problemas.append(f"{dc}: es anónimo y todavía tiene nombre")
            etapa = c.get("etapa")
            if etapa not in ETAPAS:
                problemas.append(f"{dc}: etapa {etapa!r} no es una de {sorted(ETAPAS)}")
            if etapa == "contratado":
                contratados += 1
            if etapa in CON_MOTIVO and not c.get("motivo"):
                problemas.append(f"{dc}: está {etapa} y no tiene motivo")
            if c.get("devolucion") not in DEVOLUCIONES:
                problemas.append(f"{dc}: devolucion {c.get('devolucion')!r} no es una de {sorted(DEVOLUCIONES)}")
            ev = c.get("evaluacion")
            if ev is not None:
                if not isinstance(ev, dict) or any(
                        not isinstance(ev.get(x), int) or isinstance(ev.get(x), bool) or ev.get(x) < 0
                        for x in CONTEO):
                    problemas.append(f"{dc}: evaluacion tiene que ser null o un objeto con "
                                     f"{', '.join(CONTEO)} (enteros)")
            fecha(c.get("ultimaNovedad"), f"{dc}, ultimaNovedad")
            fecha(c.get("consentimiento"), f"{dc}, consentimiento")
            if not anonimo:
                fecha(c.get("borrarEl"), f"{dc}, borrarEl", nula=False)
            historial(c.get("historial"), dc)
        if contratados > 1:
            problemas.append(f"{donde}: tiene {contratados} candidatos contratados; "
                             "¿es una búsqueda de varios puestos? Preguntá")
        if contratados and estado not in ("cerrada", "oferta"):
            problemas.append(f"{donde}: tiene un candidato contratado pero está {estado!r}")
        candidatos_por_busqueda[bid] = ids_cand

    ids_acciones = set()
    for i, a in enumerate(listas["acciones"]):
        if not isinstance(a, dict):
            problemas.append(f"acciones[{i}] no es un objeto")
            continue
        aid = a.get("id")
        donde = f"acción {aid or i}"
        if not aid:
            problemas.append(f"acciones[{i}] no tiene id")
        elif aid in ids_acciones:
            problemas.append(f"{donde}: id repetido")
        ids_acciones.add(aid)
        if not a.get("texto"):
            problemas.append(f"{donde}: falta el texto")
        bid = a.get("busqueda")
        if bid is not None and bid not in ids_busquedas:
            problemas.append(f"{donde}: apunta a la búsqueda {bid!r}, que no existe")
        cand = a.get("candidato")
        if cand is not None:
            if bid is None:
                problemas.append(f"{donde}: tiene candidato pero no búsqueda")
            elif bid in candidatos_por_busqueda and cand not in candidatos_por_busqueda[bid]:
                problemas.append(f"{donde}: el candidato {cand!r} no está en la búsqueda {bid!r}")
        if a.get("prioridad") not in PRIORIDADES:
            problemas.append(f"{donde}: prioridad {a.get('prioridad')!r} no es una de {sorted(PRIORIDADES)}")
        if not isinstance(a.get("hecha"), bool):
            problemas.append(f"{donde}: 'hecha' tiene que ser true o false")
        fecha(a.get("fecha"), f"{donde}, fecha")
        fecha(a.get("hechaEl"), f"{donde}, hechaEl")
        if a.get("hecha") is True and not a.get("hechaEl"):
            problemas.append(f"{donde}: está hecha y no tiene hechaEl")

    sync = datos.get("sync")
    if isinstance(sync, dict):
        fecha(sync.get("ultima"), "sync.ultima", hora=True)
        fecha(sync.get("ultimoIntento"), "sync.ultimoIntento", hora=True)
        for j, r in enumerate(sync.get("porRevisar") or []):
            if isinstance(r, dict) and r.get("fuente") not in FUENTES:
                problemas.append(f"sync.porRevisar[{j}]: fuente {r.get('fuente')!r} no es gmail ni calendar")
            if not isinstance(r, dict):
                continue
            rb, rc = r.get("busqueda"), r.get("candidato")
            if rb is not None and rb not in ids_busquedas:
                problemas.append(f"sync.porRevisar[{j}]: apunta a la búsqueda {rb!r}, que no existe")
            if rc is not None and rb in candidatos_por_busqueda and rc not in candidatos_por_busqueda[rb]:
                problemas.append(f"sync.porRevisar[{j}]: el candidato {rc!r} no está en la búsqueda {rb!r}")
            if not r.get("resumen"):
                problemas.append(f"sync.porRevisar[{j}]: falta el resumen")

    if problemas:
        print("busquedas.json no respeta el modelo de datos de CLAUDE.md:", file=sys.stderr)
        for p in problemas:
            print(f"- {p}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
