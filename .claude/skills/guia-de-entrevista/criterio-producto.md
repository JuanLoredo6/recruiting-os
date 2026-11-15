# Criterio de producto — evaluar como un líder de Producto

> Es parte de `guia-de-entrevista` (`.claude/skills/guia-de-entrevista/SKILL.md`). También lo citan `nueva-busqueda` (para el arranque y el scorecard) y `evaluar-candidato` (para leer trayectorias). Sirve para Product Manager, Product Owner, Product Lead, Group PM, Head o VP de Producto, Product Ops y Product Analyst.

> Adaptado de `cpo`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT), a través de `busqueda-laboral-os`.

Es el criterio de quien contrata y lidera equipos de Producto, aplicado desde el lado de la evaluación. Los datos del negocio (qué hace el cliente, quién es su usuario, qué tiene que lograr el rol) nunca viven acá: salen de `perfil-del-rol.md` y de `clientes/<cliente>/cliente.md`.

## Para el arranque

Preguntas para sumar a la guía del arranque con el hiring manager:

- **Qué decide esta persona sola** y qué decide con alguien arriba. Separa un PM que define qué construir de uno que ejecuta un backlog que le dan.
- **Qué métricas va a tener a cargo** y cómo se miden hoy. Si no hay métricas, el rol es otro (o es el primer trabajo de la persona que entre).
- **Con quién negocia**: negocio, ventas, operaciones, regulación. Cuánto pesa cada uno.
- **El equipo:** cuántos desarrolladores, diseño, datos. ¿Hay tech lead? ¿Hay discovery o solo delivery?
- **Etapa del producto:** de cero a uno, crecimiento, optimización, reemplazo de un sistema viejo. Cambia todo el perfil.
- **Por qué no lo cubren adentro.**

## Criterios típicos

Punto de partida para el scorecard. Cada criterio que entra tiene que salir de lo que el rol tiene que lograr.

| Criterio | Cómo se ve en la trayectoria | Cómo se prueba en la entrevista |
|---|---|---|
| Llevó un producto o una parte con métricas propias | Logros con un número que se movió y que era suyo | "¿Qué métrica tenías vos? ¿Cómo la moviste?" |
| Prioriza con datos y defiende el no | Decisiones de alcance, recortes, cosas que no se hicieron | Comportamiento: un pedido al que dijo que no |
| Hace discovery, no solo delivery | Entrevistas, pruebas, hipótesis descartadas | "Contame algo que pensabas construir y descartaste antes. ¿Qué te hizo descartarlo?" |
| Trabaja con ingeniería como par | Trade-offs técnicos mencionados, deuda técnica gestionada | "Una vez que el equipo te dijo que algo no se podía en ese plazo: ¿qué hiciste?" |
| Comunica y alinea a stakeholders | Lanzamientos con varias áreas, cambios de rumbo explicados | "¿Cómo le contaste a negocio que algo se atrasaba?" |
| Conoce el dominio | Industria, regulación, tipo de usuario | Preguntas del dominio del cliente, sin trampas |
| Lidera PMs (para Lead, Head, VP) | Personas a cargo, contrataciones, gente que creció | "Contame de alguien de tu equipo que creció. ¿Qué hiciste vos?" |

## Cómo leer una trayectoria

- **Un cargo no prueba nada.** "Product Manager" puede ser alguien que define estrategia o alguien que escribe historias de usuario para un backlog ajeno. Mirá qué decidía.
- **El número tiene que ser suyo.** "Crecimos 3x" en una empresa de 500 personas no es un logro del PM. "La conversión del onboarding pasó de 40 % a 55 % después del rediseño que lideré" sí.
- **Producto vs. proyecto.** Fechas, entregables y cumplimiento de plazos describen gestión de proyectos. Puede ser lo que el rol necesita, o no: depende del scorecard.
- **Etapa del producto.** Alguien que solo optimizó productos maduros puede sufrir en un cero a uno, y al revés. Es una pregunta para la entrevista, no un descarte.
- **Saltos de alcance.** De PM de una feature a Head of Product en un año: preguntar qué cambió en sus decisiones.

## El caso

En la entrevista, un caso de producto se evalúa con la respuesta en cuatro pasos de un líder de Producto. Lo que hay que observar:

1. **¿Diagnosticó antes de resolver?** ¿Preguntó para quién, qué cambió, cómo se mide hoy? Un candidato que propone funcionalidades en el primer minuto es una señal de alerta.
2. **¿Dio al menos dos opciones con lo que cede cada una?** Sin lo que cede, una opción es una idea, no un análisis.
3. **¿Tomó postura y la sostuvo** con un criterio? Presentar el menú y no elegir es la respuesta más floja.
4. **¿Cerró con próximos pasos observables** y con cómo llega lo que propone al usuario?

Además: **¿pidió datos o los inventó?** Un buen candidato declara sus supuestos en voz alta ("asumo que la mayoría entra desde el celular; ¿es así?").

### Cómo armar un caso para un cliente

- Sale de un problema real del rol (de `perfil-del-rol.md`), simplificado y sin datos confidenciales del cliente.
- Tiene datos para darle al candidato **solo si los pide**: así se ve si diagnostica.
- Dura entre 20 y 30 minutos en vivo. Un take-home, como mucho 3 horas de trabajo, y se lo dice al candidato.

Ejemplo de planteo, ilustrativo y con una empresa ficticia:

```text
Caso: "La conversión del checkout de Nimbo cayó 15 % este mes. Sos la PM. ¿Qué hacés?"
Datos si pregunta: la caída es solo en Android; empezó el día de un release; el medio de pago más usado no cambió.
Respuesta floja: propone rediseñar el checkout sin preguntar nada.
Respuesta correcta: segmenta la caída, encuentra Android y el release, propone revertir o investigar con lo que cede cada opción.
Respuesta muy buena: además, avisa a Soporte, define cómo va a saber que se resolvió y qué haría para que no vuelva a pasar.
```
