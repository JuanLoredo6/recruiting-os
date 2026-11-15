---
name: redactar-aviso
description: "Redacta el aviso de una búsqueda a partir del perfil del rol y su scorecard: un título que la gente busca, qué va a lograr la persona, el contexto real del equipo, excluyentes y deseables separados (pocos y observables), condiciones, proceso y tiempos, con lenguaje inclusivo y sin requisitos discriminatorios. Entrega versiones para LinkedIn, portales de LATAM y la web del cliente, con sus largos, y revisa un aviso que ya existe. Nunca lo publica. Usala cuando digan 'armá el aviso', 'necesito publicar la búsqueda', 'revisá este aviso', 'el aviso no trae a nadie', 'pasalo a LinkedIn', o desde una acción del tablero."
---

# redactar-aviso — un aviso que atrae a quien cumple

Un aviso con 15 requisitos espanta a buenos candidatos (muchos no se postulan si no cumplen todo) y atrae a los que se postulan a todo. Uno armado desde el scorecard dice qué va a lograr la persona y pide solo lo que de verdad importa.

Hablá en rioplatense, con voseo. El aviso va en el idioma y el registro que decida la consultora.

## Antes de escribir

Leé `busquedas/<cliente-rol>/perfil-del-rol.md`. **Sin perfil del rol no hay aviso:** ofrecé `/nueva-busqueda` primero. Leé también `contexto/voz.md`, `contexto/consultora.md` y, si existe, `busquedas/<cliente-rol>/pitch.md` (de `pitch-del-rol`).

Preguntá en una sola ronda lo que no esté:

- **¿Confidencial?** Si el cliente no quiere aparecer, el aviso describe la empresa sin nombrarla ni dar pistas que la identifiquen.
- **¿Se publica el rango salarial?** Recomendado: sí, si el cliente lo autoriza; los avisos con rango reciben postulaciones más ajustadas. Si no lo autoriza, no se pone ni se insinúa.
- **¿Dónde se publica?** LinkedIn, portales (Computrabajo, Bumeran, Get on Board, Indeed u otros), la web del cliente, comunidades.

## El aviso, por partes

1. **Título:** el nombre con el que el mercado busca el rol, más seniority y lo distintivo ("Product Manager Sr · Pagos · Remoto LATAM"). Sin títulos inventados ("Product Ninja").
2. **La empresa en dos líneas:** qué hace y para quién, con 📌 a la fuente. Si es confidencial, el rubro, la etapa y el tamaño.
3. **Qué vas a lograr:** los resultados a 90 días y a 12 meses del perfil del rol, como logros, no tareas.
4. **Con quién y cómo:** equipo, a quién reporta, producto u operación, modalidad, zona horaria, idiomas y para qué se usan.
5. **Lo que buscamos:**
   - **Excluyentes:** solo los del scorecard, escritos como conducta observable. Idealmente 2 o 3.
   - **Suma si:** los deseables. Con una línea que invite a postularse aunque no se cumplan todos.
6. **Lo que ofrecemos:** solo lo que el cliente confirmó: rango si se autorizó, contratación, beneficios concretos. Nada de "excelente clima laboral" sin un hecho atrás.
7. **El proceso:** etapas, quién entrevista, si hay caso, cuánto tarda y el compromiso de devolución de la consultora (de `contexto/consultora.md`).
8. **Datos:** una línea sobre cómo trata la consultora los datos de quien se postula, coherente con `contexto/privacidad.md`.

## Revisión antes de entregar

- **Requisitos que espantan:** años de experiencia sin motivo, títulos como filtro, listas de herramientas. Cada uno se cambia por el criterio del scorecard que hay detrás.
- **Lenguaje excluyente:** género gramatical que deja afuera ("el candidato ideal"), palabras que el mercado asocia a un solo perfil ("rockstar", "joven y dinámico", "agresivo", "ninja"). Proponé alternativas neutras sin volverlo ilegible: "la persona que se sume", "vas a liderar".
- ⚠️ **Discriminatorio:** edad, género, nacionalidad, foto, estado civil, "buena presencia", "sin hijos". No entra, aunque el cliente lo haya pedido. Si estaba en el pedido, ya debería estar marcado en el perfil del rol: si no, marcalo y avisá.
- **Inconsistencias con el perfil:** un excluyente del aviso que no está en el scorecard, o al revés.
- **Revisión de voz:** `.claude/skills/redactar-mensaje/SKILL.md#revisión-de-voz`.

## Versiones

| Canal | Largo y forma |
|---|---|
| **LinkedIn (aviso)** | Completo, con títulos cortos por parte. Las primeras 2 o 3 líneas tienen que funcionar solas (es lo que se ve antes de "ver más") |
| **Publicación en el perfil o en una comunidad** | Hasta 8 líneas: el rol, lo que va a lograr, 2 excluyentes, modalidad y cómo postularse |
| **Portales** | Completo, sin formato rico. Respetá los campos del portal (título, ubicación, modalidad, salario) |
| **Web del cliente** | Completo, con la voz del cliente si la pasó |

Si la consultora quiere, `candidatos-sinteticos` prueba el aviso contra candidatos simulados antes de publicarlo.

## Salida

Guardalo en `busquedas/<cliente-rol>/aviso.md`, con cada versión en su sección y la fecha. Si ya existía, la versión anterior queda abajo, fechada, no se pisa. Mostrá la versión principal lista para copiar.

**Claude no publica el aviso.** Cuando la persona confirme que lo publicó, registralo con `actualizar` (historial de la búsqueda con dónde y cuándo).

## Revisar un aviso existente

Si pegan un aviso ya publicado o el que mandó el cliente: compará contra el perfil del rol, marcá cada problema de la revisión con su reescritura al lado y entregá la versión corregida. Si "no trae a nadie", sumá en dos líneas qué revisar además del texto: el canal, el título, el rango y si el scorecard pide algo que el mercado casi no tiene (eso es `mapeo-de-mercado`).

## Reglas

- Nada que el perfil del rol o el cliente no confirmen: ni beneficios, ni rango, ni datos de la empresa.
- Ningún requisito discriminatorio, aunque lo pida el cliente.
- Claude nunca publica.
