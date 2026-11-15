---
name: guia-de-entrevista
description: "Arma la guía de una entrevista con criterio, no un cuestionario genérico: la guía base de la búsqueda (qué etapa evalúa qué criterio del scorecard, preguntas de comportamiento y de caso, qué es una buena respuesta y qué es una señal de alerta), la guía para un candidato concreto (cruza su CV con los desafíos del rol y ataca primero los criterios en ❓ o 🟡) y la guía para que el hiring manager entreviste mejor (entrevista estructurada, cómo plantear un caso de Producto o de Atención al cliente, cómo registrar lo observado). Trae el criterio de un líder de Producto y el de un líder de Atención al cliente. Usala cuando digan 'tengo un screening con X', 'armá la guía de entrevista', 'qué le pregunto', 'preparame la entrevista de Y', 'el hiring manager no sabe qué preguntar', 'armá un caso para la entrevista', o desde una acción del tablero."
license: "MIT. Adapta material de Pedro Romero Luna (MIT); ver CREDITOS.md y .claude/skills/LICENSE-ai-first-product-skills.txt."
---

# guia-de-entrevista — preguntar lo que el scorecard necesita saber

> El criterio de Producto (`criterio-producto.md`) está adaptado de `cpo`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT), a través de `busqueda-laboral-os`.

Una entrevista sin guía mide simpatía. Una guía armada contra el scorecard mide lo que el cliente dijo que importa, igual para todos los candidatos, y deja espacio para repreguntar lo que cada trayectoria no muestra.

Hablá en rioplatense, con voseo, frases cortas. Si la entrevista es en inglés o en portugués, las preguntas van en ese idioma y las indicaciones en español.

## Modos

| Pedido | Modo | Dónde se guarda |
|---|---|---|
| `/guia-de-entrevista <cliente-rol>` | **Guía base** de la búsqueda | `busquedas/<cliente-rol>/guia-entrevista.md` |
| `/guia-de-entrevista <cliente-rol> <candidato>` | **Guía para un candidato** | `busquedas/<cliente-rol>/candidatos/<candidato>/guia-<AAAA-MM-DD>.md` |
| `/guia-de-entrevista <cliente-rol> hiring-manager` | **Guía para el hiring manager** | `busquedas/<cliente-rol>/guia-hiring-manager.md` |

## Antes de empezar

Leé siempre `busquedas/<cliente-rol>/perfil-del-rol.md`. **Sin scorecard no hay guía:** ofrecé `/nueva-busqueda` primero.

Según el área de la búsqueda, leé y seguí el criterio que corresponde:

- Producto → `.claude/skills/guia-de-entrevista/criterio-producto.md`
- Atención al cliente → `.claude/skills/guia-de-entrevista/criterio-atencion.md`

Para la guía de un candidato, leé además su `evaluacion.md`, su CV y las notas de entrevistas anteriores en su carpeta.

Si no se sabe qué etapa es (screening de la consultora, entrevista con el hiring manager, caso, panel), la duración o el idioma, preguntalo en una línea.

## Lo que vale para las tres guías

- **Cada pregunta está atada a un criterio del scorecard.** Una pregunta que no mide ningún criterio se saca o se justifica.
- **Comportamiento antes que hipótesis.** "Contame de una vez que..." mide mejor que "¿qué harías si...?". Los casos se usan para lo que no se puede ver en el pasado.
- **Repreguntas preparadas.** Por cada pregunta, dos repreguntas para llegar al hecho: "¿qué hiciste vos, no el equipo?", "¿cómo lo mediste?", "¿qué pasó después?". Es el ingrediente 1 de `.claude/skills/poner-a-prueba/SKILL.md#método`, aplicado al candidato.
- **Qué es una buena respuesta y qué es una señal de alerta**, para cada pregunta, escrito antes de la entrevista. Así se compara a todos con la misma vara.
- **Preguntas prohibidas.** Nada sobre edad, planes familiares, hijos, estado civil, religión, salud, origen, orientación sexual ni afiliación política o sindical, aunque sea "para romper el hielo". Si el hiring manager suele hacerlas, la guía para el hiring manager lo dice.
- **Tiempo.** La guía entra en la duración real, con 5 minutos para las preguntas del candidato.

## Modo guía base

1. **Qué evalúa cada etapa.** Una tabla: etapa, quién entrevista, qué criterios del scorecard mide y cuánto dura. Ningún criterio queda sin etapa; ninguno se mide tres veces sin motivo.
2. **Por cada criterio**, de 1 a 3 preguntas:
   - La pregunta, traducida al rol y al cliente.
   - Las dos repreguntas.
   - Buena respuesta (qué tiene que aparecer) y señal de alerta.
   - Cuánto tiempo darle.
3. **El caso**, si el proceso lo tiene: el planteo, los datos que se le dan al candidato si pregunta, qué se evalúa y cómo se ve una respuesta floja, una correcta y una muy buena. Seguí la sección «El caso» del criterio del área.
4. **Cómo contar el rol** en el screening: el pitch del rol del perfil, el proceso y los tiempos, y qué se puede decir del cliente según `contexto/consultora.md`.

## Modo guía para un candidato

1. **Primero lo que falta saber.** Los criterios en ❓ y 🟡 de su `evaluacion.md` van al principio, con las preguntas de la guía base adaptadas a su trayectoria ("en Nimbo llevaste el checkout: ¿qué decisión de priorización te tocó defender ante negocio?").
2. **Lo que su CV dice y hay que comprobar:** los logros más fuertes, con la repregunta que lleva al hecho.
3. **Lo que hay que preguntar sin juzgar:** huecos, cambios cortos, saltos de alcance. Con una formulación neutra ("contame qué pasó entre 2023 y 2024") y nunca como sospecha.
4. **Lo que el candidato va a querer saber:** del rol, del equipo, del proceso. Lo que la consultora no puede contestar, anotado para no improvisar.
5. **Repaso de 3 minutos:** una lista corta para leer antes de entrar.

## Modo guía para el hiring manager

Para que el hiring manager entreviste con el mismo criterio que la consultora:

1. **Qué criterios le toca medir** a él y por qué a él.
2. **Sus preguntas**, con repreguntas, buena respuesta y señal de alerta, y cómo plantear el caso.
3. **Cómo registrar lo observado:** una línea por criterio con lo que el candidato dijo o hizo, separado de la impresión. El formato es el de `registrar-entrevista`, para que la consultora lo pueda cargar tal cual.
4. **Errores comunes a evitar:** decidir en los primeros 5 minutos, hablar más que el candidato, preguntar por hipótesis lo que se puede preguntar por hechos, comparar con el último candidato en vez de con el scorecard, preguntas prohibidas.
5. **Cómo dar su feedback a la consultora:** en 24 horas, por criterio, con el ✅ 🟡 ❌ ❓.

Escribila para que la pueda leer en 5 minutos. Ofrecé el mensaje para mandársela (`/redactar-mensaje cliente <cliente-rol>`).

## Cierre

Decí dónde quedó la guía, qué criterios cubre cada etapa y, para un candidato, las dos preguntas más importantes. Ofrecé registrar la entrevista después con `/registrar-entrevista <cliente-rol> <candidato>` y sumá esa acción para el día de la entrevista si hay fecha.

Ejemplo de una pregunta preparada, ilustrativo y con datos ficticios:

```text
Criterio 2 (excluyente): priorizó con datos y lo defendió ante negocio.
Pregunta: "Contame de una vez que le dijiste que no a un pedido de negocio. ¿Qué pidieron y qué hiciste?"
Repreguntas: "¿Qué dato usaste para decidir?" · "¿Qué pasó con la relación con esa persona después?"
Buena respuesta: un pedido concreto, el dato que usó, la alternativa que ofreció y cómo terminó.
Señal de alerta: "en general negocio entiende", sin un caso; o un no sin alternativa.
Tiempo: 6 minutos.
```

## Reglas

- No inventes datos del cliente, del rol ni del candidato. Lo que falta se marca ❓.
- Ninguna pregunta prohibida, ni en la guía ni en las repreguntas.
- Las respuestas modelo describen qué tiene que aparecer, no un texto que el candidato deba decir.
