---
name: poner-a-prueba
description: "Pone a prueba lo que se da por cierto antes de que quede escrito: cada requisito de un hiring manager, cada criterio del scorecard, cada afirmación de un candidato en su CV o en una entrevista, cada motivo de descarte y cada decisión de la consultora. Repregunta con un ejemplo concreto, con un tope de intentos y salidas claras, ordena la evidencia (conducta > dato > afirmación > suposición) y anota lo que queda abierto sin inventarlo. Usala cuando pidan 'esto se sostiene?', 'apretame', 'cuestioname este requisito', 'el cliente pide X, ¿tiene sentido?', 'estoy por descartar a Y, ¿está bien?', o cuando otro skill necesite entrevistar: es el método que todos los demás citan."
---

# poner-a-prueba — el método que hace sostenible cada decisión

> Adaptado de `grill`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT), a través de `busqueda-laboral-os`.

Un requisito inflado le cuesta semanas a una búsqueda. Un descarte por intuición le cuesta un buen candidato. Mejor repreguntar antes. Este skill tiene dos usos:

- **Solo:** pone a prueba un requisito, un scorecard, una evaluación, un motivo de descarte o una decisión de la consultora.
- **Como método:** cualquier skill del repo que entrevista cita la sección **Método** en vez de copiarla. Puede cambiar los ejemplos o a quién apunta; el método es uno solo.

Hablá en rioplatense, con voseo, frases cortas.

## Método

Citalo como `.claude/skills/poner-a-prueba/SKILL.md#método`. Son diez ingredientes. Del 1 al 5, cómo se aprieta un dato. Del 6 al 10, cómo corre la entrevista entera.

### 1. Repregunta con un ejemplo concreto

Ante una frase que no se puede comprobar ("tiene que ser muy estratégico", "lideré la transformación de la atención", "no me cerró"), no la aceptes ni la reformules: devolvé una repregunta que pida el hecho que hay detrás, con un ejemplo de qué sería una buena respuesta.

> Mal: "¿Podés dar más detalle?"
>
> Bien: "'Muy estratégico' ¿cómo se vería en su primer trimestre? ¿Que arme el roadmap del año, que diga que no a pedidos de ventas, que proponga un producto nuevo? Una buena respuesta nombra lo que tendría que hacer: 'que en 90 días presente qué dejar de hacer en el producto de cobros, con datos'."

### 2. Como mucho dos intentos

Hasta dos repreguntas sobre el mismo dato. La tercera ya no trae información: cansa y convierte la entrevista en un interrogatorio. Vale igual con un hiring manager que con un candidato.

### 3. Salidas

Hay dos salidas, y ninguna es seguir insistiendo:

- **Segunda resistencia:** la respuesta a la segunda repregunta sigue sin hecho. No lo descartes ni lo fuerces: anotá el hueco con quién lo cierra y seguí.
- **Evidencia fuerte de entrada:** si la primera respuesta ya trae el hecho (algo que pasó, un número medido), no hay nada que repreguntar. Se confirma y se sigue.

### 4. Jerarquía de evidencia

`conducta > dato > afirmación > suposición`. Si dos respuestas compiten por el mismo hecho, gana la que está más arriba.

- Sobre un candidato: "es un gran líder" (afirmación de una referencia) no pesa lo mismo que "su equipo pasó de 8 a 20 personas y retuvo a todos" (dato) ni que "en el caso, antes de proponer, preguntó cómo estaba el equipo" (conducta observada).
- Sobre un requisito: "siempre buscamos ingenieros" (afirmación) no pesa lo mismo que "los dos PMs que funcionaron venían de ingeniería y los dos que no, de negocio" (dato).

### 5. Los huecos se anotan, nunca se rellenan

Si un dato no se pudo cerrar, no lo completes con una inferencia para que el documento quede prolijo. Anotalo como abierto en `contexto/datos-pendientes.md` (o en la sección «Abierto» del perfil del rol o de la evaluación), con quién lo cierra: "preguntarle a Carla si el inglés es para leer documentación o para hablar con clientes".

### 6. Rondas según lo que depende de qué

Ordená las preguntas por lo que depende de cada una. Cada ronda junta, numeradas, todas las que ya se pueden responder. Una que depende de otra todavía abierta va a la ronda siguiente. Después de cada ronda, recalculá qué quedó respondible.

Formato de una ronda (texto plano, legible en la terminal):

```
Ronda 1

1. ¿El rol tiene métricas propias o ejecuta el roadmap de otro?
   Recomendado: métricas propias, la conversión del checkout.

2. ¿El inglés es excluyente?
   Recomendado: deseable; el equipo trabaja en español y los clientes son de LATAM.
```

Se responde "sí" para aceptar todas las recomendaciones, o por número para cambiar alguna. El número, la pregunta y la recomendación van siempre en líneas separadas.

### 7. Una recomendación que se acepta con "sí"

Cada pregunta trae la respuesta que Claude recomienda, escrita para que "sí" la acepte. Estar de acuerdo nunca obliga a decir "no".

> Mal: "Recomendado: ¿no pedir 8 años?" (para estar de acuerdo hay que decir "no")
>
> Bien: "Recomendado: reemplazar '8 años' por 'llevó un producto con métricas propias de punta a punta'."

### 8. Los hechos se buscan, las decisiones se preguntan

Lo que el repo ya sabe (el perfil del rol, la evaluación, el CV, las notas de la entrevista, el historial del cliente) lo busca Claude y no lo pregunta. Si lo que encuentra contradice lo que se dijo, muestra la contradicción. La repregunta del ingrediente 1 queda para lo que solo la persona sabe. Las decisiones son siempre de la persona.

Si hay subagentes disponibles, la búsqueda va a uno y la ronda sigue con lo que no depende de ese dato. Si no, se busca antes de la ronda que lo necesita.

> Mal: "¿Cuántos años estuvo en su último trabajo?" (está en el CV)
>
> Bien: "Su LinkedIn dice marzo 2021 a octubre 2026 y el CV dice 2020. Lo pregunto en el screening."

### 9. Las palabras vagas se precisan

Si alguien usa una palabra vaga o con dos sentidos ("senior", "estratégico", "hands-on", "cultura", "fit", "lideró"), se frena en ese momento: se propone el término preciso y un caso límite que lo pruebe.

> Mal: el hiring manager dice "que tenga buen fit cultural" y queda así en el scorecard.
>
> Bien: "'Fit cultural' puede ser cualquier cosa, y es donde más se cuelan los sesgos. ¿Qué hace alguien que funciona en tu equipo que otro no? Propongo: 'decide con información incompleta y lo comunica'. Caso límite: ¿alguien que pide más datos antes de decidir no encaja? Recomendado: 'decide con información incompleta y declara sus supuestos'."

**"Fit cultural" sin una conducta atrás no entra nunca a un scorecard.**

### 10. Se cierra cuando no queda nada abierto y lo confirmás

Termina cuando no queda ninguna pregunta respondible sin responder y la persona confirma que los dos entienden lo mismo. Antes de esa confirmación, lo único que se escribe son formulaciones precisas (ingrediente 9), huecos (5) y decisiones. No se arma ningún entregable ni se manda nada.

> Bien: "No queda nada respondible abierto. Anoté dos huecos para Carla. ¿Entendemos lo mismo: PM Sr con métricas propias, 2 excluyentes, inglés deseable? Sí para cerrar."

## Uso solo

Si no dijeron qué poner a prueba, preguntá en una línea: ¿un requisito, el scorecard, la evaluación de un candidato, un motivo de descarte o una decisión de la consultora?

1. Leé la fuente (perfil del rol, evaluación, registro de entrevista, `contexto/decisiones.md`).
2. Corré el método sobre cada afirmación que no se pueda comprobar.
3. **Si lo que se pone a prueba es un descarte:** comprobá que el motivo esté en el scorecard y tenga una cita. Si el motivo es una impresión ("no me cerró") o roza un atributo protegido, decilo claro y proponé qué validar antes de decidir.
4. Distribuí lo que sale. No inventes otros destinos:

| Lo que sale | Dónde va |
|---|---|
| Un criterio o requisito precisado | `busquedas/<cliente-rol>/perfil-del-rol.md` (y la tabla de cambios, con quién lo decidió) |
| Un estado del scorecard de un candidato | `busquedas/<cliente-rol>/candidatos/<candidato>/evaluacion.md` |
| Un hueco | `contexto/datos-pendientes.md`: una línea con el dato, la búsqueda o el candidato, quién lo cierra y la fecha |
| Una decisión de la consultora | `contexto/decisiones.md`: una línea con fecha y la decisión (las ⭐ llevan además lo de «Decisiones clave») |

Si para seguir haría falta escribir en un destino que no está en esta tabla, decilo y frená.

## Decisiones clave

Todas las decisiones se anotan. Una **decisión clave** se marca con ⭐ en `contexto/decisiones.md` para que quien abra el sistema la lea antes que el resto. **Es clave solo si se cumplen las tres condiciones. Dos de tres no alcanzan:**

1. **Difícil de deshacer:** volver atrás cuesta trabajo, plata o credibilidad.
2. **Sorprende sin contexto:** alguien que no estuvo en la conversación no la adivinaría.
3. **Sale de un trade-off real:** había una alternativa concreta y se descartó.

> Clave: "Dejamos de tomar búsquedas de agentes de atención masivas". Volver atrás implica rearmar el proceso y el equipo (1), alguien que ve la cartera esperaría lo contrario (2) y se evaluó seguir con volumen (3).
>
> No clave: "Mandamos el reporte los viernes". Se cambia fácil (falla la 1), no sorprende a nadie (falla la 2) y no se descartó nada (falla la 3).

**Claude propone la marca y la persona la confirma.** Antes de marcarla, mostrá la decisión con las tres condiciones al lado y cuál se cumple. Marcala solo si la acepta. Si falla una condición, no la propongas: decí cuál falla.

### Qué la haría cambiar

> Adaptado del esquema de decisiones de `pm-brain`, de Paweł Huryn ([pm-brain](https://github.com/phuryn/pm-brain), licencia MIT).

Toda decisión ⭐ se escribe con dos líneas más, debajo:

```
- 2026-11-14 ⭐ Dejamos de tomar búsquedas masivas de agentes de atención.
  Descarto: seguir con volumen para sostener la facturación.
  Cambio de idea si: en 3 meses las búsquedas de liderazgo no cubren el 70 % de la facturación de hoy.
```

- **Descarto:** la alternativa concreta que se dejó.
- **Cambio de idea si:** una condición **observable**: un número del tablero, una fecha, algo que diga una persona concreta. Si no quieren fijarla, queda `Cambio de idea si: ❓` y va a `contexto/datos-pendientes.md`.

`reporte-semanal` revisa cada semana si alguna de esas condiciones se cumplió.
