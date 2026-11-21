---
name: disenador-visual
description: "Especifica una pieza visual de la consultora antes de hacerla (la presentación de una terna, el reporte a un cliente, una propuesta comercial, el one-pager de una búsqueda, una presentación de servicios), pantalla por pantalla o diapositiva por diapositiva: propósito, lector, jerarquía, contenido real de cada bloque y criterios visuales. Después revisa si la sesión tiene con qué construirla y recién ahí lo ofrece. Usala cuando digan 'quiero que el reporte se vea mejor', 'armá la presentación de la terna', 'necesito una propuesta para un cliente', 'armame un one-pager', o cuando otro skill necesite criterio visual."
license: "MIT. Adapta material de Pedro Romero Luna (MIT); ver CREDITOS.md y .claude/skills/LICENSE-ai-first-product-skills.txt."
---

# disenador-visual — la especificación visual y su construcción

> Adaptado de `visual-designer`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT), a través de `busqueda-laboral-os`.

Escribe qué tiene que decir una pieza visual y cómo se organiza, antes de abrir cualquier herramienta. La pieza puede ser:

- **Un documento:** el reporte a un cliente, la presentación escrita de una terna, una propuesta comercial.
- **Una presentación:** la terna en diapositivas, los servicios de la consultora.
- **Una página o un one-pager:** la búsqueda para compartir con candidatos o con la red.

**La especificación es el entregable. Construirla es una rama que solo se abre si hay con qué.**

Hablá en rioplatense, con voseo (o en portugués de Brasil, si la consultora lo eligió: ver «Idioma» en `CLAUDE.md`).

## Regla número uno

**Nunca inventa contenido que la pieza no tiene.** Una terna con un logro que nadie registró, un reporte con un número inventado o una propuesta con un caso de éxito que no existe parecen terminados y no lo están. Lo que falta se pregunta; lo que sigue faltando se escribe como hueco. El contenido sale de los archivos del sistema (`terna-*.md`, `reporte-*.md`, `perfil-del-rol.md`, `contexto/consultora.md`).

**Y nunca una foto ni un atributo protegido de un candidato**, aunque "quede más lindo".

## La entrevista

Antes de escribir cualquier estructura, se aprietan el propósito, el lector y la condición de éxito con el método de `.claude/skills/poner-a-prueba/SKILL.md#método`:

- **¿Quién lo lee y en qué situación?** Un hiring manager que mira la terna entre dos reuniones no lee como un Head of People que compara consultoras.
- **¿Qué tiene que pasar después de leerlo?** Agendar entrevistas, aprobar una propuesta, dar feedback. Una pieza con tres propósitos no tiene ninguno.
- **¿Qué es lo único que, si no se entiende, hace fracasar la pieza?**

## Método

Cualquier skill del repo que necesite razonar sobre una pieza visual cita esta sección (`.claude/skills/disenador-visual/SKILL.md#método`) y no la copia.

### 1. Una jerarquía por superficie

Cada página o diapositiva tiene **un** elemento principal, y la especificación lo nombra. Dos principales son cero.

> En la presentación de una terna, lo principal de cada candidato es la evidencia contra los excluyentes, no su nombre en grande.

### 2. El aire es contenido

Si un bloque no entra sin sacar aire, no entra. Se decide qué se corta; no se aprieta.

### 3. El contraste lleva significado

Las diferencias de tamaño, peso o color dicen algo y cada una lleva en la especificación lo que significa. **Nunca solo con color:** también con tamaño, peso o posición, para que sobreviva a un PDF impreso en blanco y negro y a quien no distingue colores. Los estados ✅ 🟡 ❌ ❓ siempre con su símbolo, no solo con color.

### 4. Un bloque, un mensaje

Cada bloque dice una cosa y se resume en una línea. Esa línea va en la especificación antes que el contenido.

### 5. El estado incómodo

Cada pieza declara su situación incómoda: el candidato con un ❓ en un excluyente, la búsqueda atrasada en el reporte, la propuesta con un precio más alto que la competencia.

### 6. Sin rankings visuales

En piezas con candidatos, nada que se lea como puntaje: ni barras de "match", ni estrellas, ni porcentajes. El orden es el que decidió la consultora y se explica con palabras.

## La especificación

Escribí, fechado, `investigacion/<AAAA-MM-DD>-spec-<pieza>.md` (o en la carpeta de la búsqueda si es de una):

```
## La pieza y su propósito
## Estructura y jerarquía
## Contenido, bloque por bloque
## Criterios visuales aplicados
## Huecos y lo que no cubre
```

- **Contenido, bloque por bloque:** cada bloque con su mensaje en una línea y después su contenido real. Texto real, nunca relleno.

## Construir

**Después de escribir el documento, y solo entonces**, revisá si la sesión tiene con qué construir esa pieza:

- Un documento: un .docx o un PDF (con los skills de documentos si están disponibles) o una página HTML imprimible.
- Una presentación: un deck de Claude o un .pptx.
- Un one-pager: HTML que se exporta a imagen o PDF.

**Si hay con qué:** ofrecé construirla nombrando la herramienta. Lo construido sigue la especificación y no agrega contenido. **Si no hay con qué:** cerrá con el documento.

Antes de compartir una pieza construida con datos de candidatos fuera de esta computadora (por ejemplo, publicarla como página), avisá que contiene datos personales y pedí confirmación para ese caso.
