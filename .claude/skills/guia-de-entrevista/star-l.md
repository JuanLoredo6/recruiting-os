# STAR-L — pedir, repreguntar y registrar una historia de comportamiento

> Es parte de `guia-de-entrevista` (`.claude/skills/guia-de-entrevista/SKILL.md`). También la usan `registrar-entrevista` (para ordenar lo que contó el candidato) y `armar-terna` (para citar evidencia). Adaptado del formato STAR-L de `busqueda-laboral-os`, ahí desde el lado de quien se postula.

Una pregunta de comportamiento ("contame de una vez que…") mide mejor que una hipotética, pero solo si se llega al hecho. STAR-L es el orden que usa quien entrevista para no quedarse con la parte linda de la historia: **situación, tarea, acción, resultado y aprendizaje**. Es una herramienta de la consultora, no un examen de formato: el candidato no tiene por qué conocerla ni contar en ese orden. Quien guía es quien entrevista.

## Los cinco pasos y qué buscar en cada uno

| Paso | Qué tiene que aparecer | Repregunta para llegar | Tiempo de la respuesta |
|---|---|---|---|
| **S · Situación** | El contexto justo: producto u operación, tamaño del equipo, qué estaba en juego | "¿Dónde estabas y qué estaba pasando?" | 10 a 15 s |
| **T · Tarea** | Qué le tocaba a la persona: el objetivo o el problema que era suyo. Separa su parte de la del equipo | "¿Qué te tocaba a vos, puntualmente?" · "¿Quién había definido ese objetivo?" | 10 s |
| **A · Acción** | Qué hizo **la persona**, en primera persona: qué decidió, qué priorizó, qué cedió. Es el centro | "¿Qué hiciste vos, no el equipo?" · "¿Qué opciones tenías y por qué elegiste esa?" | 40 a 60 s |
| **R · Resultado** | Qué cambió, con número si lo hay, y si era suyo | "¿Cómo lo mediste?" · "¿Qué pasó después?" | 10 a 15 s |
| **L · Aprendizaje** | Qué entendió después, qué haría distinto o qué regla le quedó | "Si lo hicieras hoy, ¿qué cambiarías?" | 10 a 15 s |

Una pregunta de comportamiento en la guía lleva, como mínimo, la repregunta de **Tarea**, la de **Acción** y la de **Aprendizaje**: son las que más se saltean y las que separan ejecución de criterio.

## Qué es una buena respuesta

- **La acción es suya.** "Propuse", "decidí", "le dije que no" con un porqué. Un relato todo en "nosotros" no es una mala señal por sí solo (hay culturas y personas que hablan así): se repregunta hasta encontrar su parte.
- **El resultado no está inflado.** Un número que la persona puede explicar y que era suyo. "Crecimos 3x" en una empresa grande no es su resultado.
- **El aprendizaje es concreto y cambia una conducta** ("hoy pacto la métrica de éxito antes de arrancar"). Uno genérico ("aprendí la importancia de comunicar") cuenta como que falta.
- **La historia cierra:** la tarea, la acción y el resultado hablan del mismo problema.

Señales de alerta: no hay ningún caso concreto ("en general…"), la acción es de otra persona, el resultado cambia de número al repreguntar, o no aparece nada que la persona haría distinto en ninguna historia.

## Cómo se registra

En `registrar-entrevista`, cada historia de comportamiento se anota por paso, con las palabras del candidato:

```markdown
- **Historia:** <de qué se trata, en una línea> · min <aprox.>
  - S: "<cita>" 📌
  - T: "<cita>" 📌
  - A: "<cita>" 📌
  - R: "<cita>" 📌
  - L: - ❓ no se preguntó
```

- **Lo que no se contó, no existe.** Si falta un paso, va con "-" y ❓, y pasa a «Abierto para la próxima etapa». **Nunca se deduce ni se completa** (límite L1): la tarea no se infiere del cargo, ni el aprendizaje del resultado.
- **Un criterio pasa a ✅ solo con Acción y Resultado propios.** Con la acción del equipo o sin resultado, queda 🟡 y se anota qué falta.
- **El aprendizaje no es excluyente por sí solo:** suma evidencia para criterios como "aprende de sus errores" o "toma decisiones con criterio", pero un candidato nervioso que no lo dijo no queda ❌: queda ❓ para la próxima etapa.

## Para el hiring manager

La guía para el hiring manager explica STAR-L en tres líneas y le pide anotar cada historia por paso. Así el feedback que llega a la consultora trae citas, no "me gustó".

Ejemplo, ilustrativo y con datos ficticios:

```text
Criterio 2 (excluyente): prioriza con datos y defiende el no ante negocio.
Pregunta: "Contame de una vez que le dijiste que no a un pedido de negocio."
T: "¿Qué te tocaba decidir a vos ahí?"
A: "¿Qué dato usaste y qué alternativa ofreciste?"
R: "¿Qué pasó con el pedido y con la relación después?"
L: "¿Lo volverías a hacer igual?"
Buena respuesta: un pedido concreto, el dato, la alternativa, cómo terminó y algo que haría distinto.
Señal de alerta: "en general negocio entiende", sin un caso.
Tiempo: 7 minutos.
```
