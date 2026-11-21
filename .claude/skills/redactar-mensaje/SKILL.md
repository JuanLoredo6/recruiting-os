---
name: redactar-mensaje
description: "Escribe los mensajes de una búsqueda con la voz de la consultora y nunca los envía: primer contacto de sourcing, invitación de conexión, follow-up, invitación a entrevista, devolución a un candidato descartado (con feedback útil y sin atributos protegidos), cierre con quienes no avanzaron, mensajes al hiring manager (preguntas del arranque, guía para entrevistar, pedido de feedback), oferta y bienvenida. Adapta el largo al canal (LinkedIn, mail, WhatsApp) y usa solo datos reales del rol y del candidato. Usala cuando digan 'escribile a X', 'armá la devolución para Y', 'cómo le digo que no avanza', 'mandale un follow-up', 'escribile al hiring manager', 'necesito un mensaje para', 'escreve para o candidato', o desde una acción del tablero."
license: "MIT. Adapta material de Paweł Huryn (MIT); ver CREDITOS.md y .claude/skills/LICENSE-phuryn.txt."
---

# redactar-mensaje — mensajes que suenan a la consultora

Los mensajes de una búsqueda son la cara de la consultora: el primer contacto decide si un candidato pasivo responde, y la devolución decide si vuelve a confiar en ustedes. Este skill los redacta; la persona los revisa y los manda.

Hablá en rioplatense, con voseo (o en portugués de Brasil, si la consultora lo eligió: ver «Idioma» en `CLAUDE.md`), para explicar. El mensaje va en el idioma y el registro que corresponda (si el destinatario escribe en portugués, en inglés o de usted, se responde igual). En portugués de Brasil, seguí `.claude/skills/redactar-aviso/portugues.md`.

## Antes de escribir

Leé `contexto/voz.md` (cómo escribe la consultora y qué palabras no usa nunca), `contexto/consultora.md` (qué se puede decir del proceso y qué no se menciona nunca) y, según el mensaje:

- De un candidato: `busquedas/<cliente-rol>/perfil-del-rol.md` (sobre todo el pitch del rol), su `evaluacion.md`, sus entrevistas y su historial.
- Del cliente: `clientes/<cliente>/cliente.md` y lo que haya pendiente en la búsqueda.

Si falta saber algo esencial, preguntá en una sola ronda: a quién, por qué canal, qué pasó antes y qué se quiere lograr.

**Confidencialidad:** si la búsqueda es confidencial o el cliente no quiere aparecer, no lo nombres. Ante la duda, preguntá.

## Tipos de mensaje y su forma

| Tipo | Largo | Lo que no puede faltar |
|---|---|---|
| **Invitación de conexión en LinkedIn** | Hasta 200 caracteres (300 en algunas cuentas) | Por qué esa persona, en una frase |
| **Primer contacto de sourcing** | 4 a 6 líneas | Por qué ella (algo concreto de su trayectoria), el rol en una línea, una razón verdadera del pitch del rol, modalidad y rango si se puede decir, un pedido fácil (15 minutos) y facilidad para decir que no |
| **Follow-up** | 2 a 3 líneas | Referencia al mensaje anterior, un dato nuevo si lo hay, pregunta concreta. Uno solo; después, se deja |
| **Invitación a entrevista** | Lo necesario | Quién entrevista, qué etapa es, duración, formato, qué conviene preparar (sin adelantar el caso), cómo reprogramar |
| **Devolución a un descartado** | 4 a 7 líneas | Ver «La devolución» abajo |
| **Cierre a quien no llegó a una entrevista** (se postuló o respondió un contacto) | 2 a 3 líneas | Agradecer el tiempo, decir que no sigue, si se puede guardar su perfil para otra búsqueda (con su permiso) |
| **Pedido para presentar al cliente** (`consentimiento-presentacion`) | 3 a 5 líneas | A qué cliente y para qué rol (si la búsqueda es confidencial, preguntá qué se puede decir), qué se le va a mostrar al cliente (trayectoria, evaluación contra el scorecard, CV sin datos personales) y dónde (una carpeta de Drive de la consultora compartida con el cliente, si la búsqueda usa `vista-cliente`), que el cliente puede descargar lo que ve, y un sí o no fácil. Si acepta, `presentadoEl` se registra con `actualizar` |
| **Aviso de la vista del cliente** (`aviso-vista-cliente`) | 4 a 6 líneas | El link del Sheet y el de la carpeta, que solo completa las dos columnas amarillas (decisión y comentario) y que el resto lo actualiza la consultora. Va al contacto confirmado en `vista-cliente compartir` |
| **Al hiring manager** | Corto | Un pedido claro (preguntas del arranque, feedback de una entrevista, decisión sobre la terna), con fecha |
| **Oferta** (en nombre del cliente) | Lo necesario | Solo los datos que el cliente confirmó por escrito. Nada de condiciones supuestas |
| **Bienvenida o felicitación** | Corto | Fecha de ingreso, próximo paso, quién lo contacta |

## La devolución

Es el mensaje que más se saltea y el que más dice de la consultora. Todo candidato que se postuló o aceptó una charla recibe una devolución dentro del plazo de `contexto/consultora.md`. Si no llegó a una entrevista, alcanza con el formato corto de «Cierre» (sin feedback detallado); si fue entrevistado, va la devolución completa de abajo.

- **Clara desde la primera línea:** no avanza. Sin vueltas ni falsas esperanzas.
- **Un motivo verdadero y útil**, en términos del scorecard, si la consultora decide darlo. Por ejemplo: "para este rol el cliente necesitaba a alguien que ya haya tenido métricas de producto a cargo, y en tu caso la experiencia es más de gestión de proyectos". Nunca la evaluación completa, nunca el feedback literal del cliente sin su permiso, nunca comparaciones con otros candidatos.
- **Nunca un atributo protegido**, ni explícito ni sugerido ("buscaban un perfil más joven", "con más disponibilidad"). Si el motivo real es ese, frená y avisale a la persona: es un tema para hablar con el cliente, no para escribir.
- **Algo que se lleve**, si es verdad: lo que se destacó en la entrevista.
- **Qué pasa con sus datos:** si se guarda en la base de talento (solo con su permiso) o se borra según `contexto/privacidad.md`.
- **Nada de plantilla vacía.** "Tu perfil no se ajusta a lo que buscamos en este momento" es lo que no hay que escribir.

Si la persona prefiere no dar motivo, se respeta: el mensaje igual es claro, humano y a tiempo.

## Reglas de escritura

- **Con la voz de la consultora.** Si `voz.md` está vacío, escribí simple y directo, y preguntá si suena a ellos.
- **Datos reales (límite L1):** todo lo que se dice del rol sale de `perfil-del-rol.md`; todo lo que se dice del candidato, de su perfil o de sus entrevistas. Lo que no está, no se dice.
- **La logística tampoco se inventa:** duración, formato (videollamada, presencial), quién entrevista, en qué idioma o qué se va a evaluar en la charla entran al mensaje solo si están en el pedido o en los archivos. Si faltan, el mensaje se escribe sin ellos o con `<duración>`, y afuera del bloque va la pregunta. Los ejemplos de `voz.md` muestran el tono, no son datos: un «20 minutos» de un ejemplo no vale para este mensaje. Aclararlo afuera no alcanza: lo que no está confirmado no entra al texto para copiar.
- **Sin frases de reclutamiento de plantilla:** nada de "oportunidad única", "excelente propuesta", "empresa líder", "rockstar", "ninja", "espero que este mensaje te encuentre bien", "tu perfil nos pareció muy interesante".
- **Un solo pedido por mensaje**, y fácil de responder.
- **El nombre del destinatario**, si se sabe. Si no, no inventes uno: dejá `<nombre>`.
- **Nada de presión** ni urgencia fingida ("quedan pocos lugares", "el cliente decide mañana" si no es así).

## Revisión de voz

> Adaptado de `work-humanizer`, de Paweł Huryn ([product-engineering](https://github.com/phuryn/product-engineering), licencia MIT), a través de `busqueda-laboral-os`.

Todo texto que sale en nombre de la consultora pasa por acá antes de entregarse. Los demás skills citan esta sección (`.claude/skills/redactar-mensaje/SKILL.md#revisión-de-voz`) y no la copian.

### ¿Lo podría haber escrito cualquiera?

Si el mismo pedido, hecho por otra consultora, daría un mensaje casi igual, al texto le falta lo concreto: qué de esta trayectoria hizo que le escribieran, qué tiene este rol de distinto. Ninguna corrección de estilo lo arregla. Volvé a la evaluación y al pitch del rol, o preguntá en una sola ronda de hasta 3 preguntas.

### Lo que no cambia nunca

- **La certeza de cada dato.** "Hasta" no se vuelve "de", "híbrido" no se vuelve "remoto", "posible" no se vuelve "seguro".
- **Lo que el cliente no confirmó** (salario, beneficios, modalidad): no se agrega.

### Muletillas a sacar

- **Contraste con algo que nadie dijo:** "no es solo un trabajo, es un desafío". Decí lo concreto.
- **Anuncio antes del punto:** "Te cuento:", "Voy al grano:". El punto va directo.
- **Cierres de fórmula:** "Quedo atento a tus comentarios", "No dudes en contactarme", "Sin más". Se termina en el pedido.
- **Vocabulario inflado:** apasionado, desafiante, sinergia, potenciar, robusto, "aportar valor". También lo que liste `contexto/voz.md` en "no usamos nunca".
- **Adjetivos sin dato atrás:** "increíble equipo", "gran cultura". Se pega el hecho o se corta.
- **Puntuación de IA:** rayas (—), negritas sueltas, emojis de viñeta, varios signos de exclamación.

### Control final

1. **Control de hechos, frase por frase**, contra la fuente: cada dato del rol y del candidato está, con el mismo valor, y no apareció ninguno nuevo.
2. **Barrido de muletillas** en el texto final.
3. **Leelo como lo recibiría el candidato:** ¿le dan ganas de responder?, ¿entiende qué pasó?
4. **Opción más corta** en mensajes de más de 100 palabras: si sobra un cuarto o más, ofrecé la versión corta en una línea sin aplicarla.

## Entrega

1. Pasalo por la **Revisión de voz**. Mostrá el mensaje listo para copiar, en un bloque de código, con el conteo de caracteres si el canal tiene límite.
2. Si hay dos enfoques razonables, ofrecé una alternativa corta.
3. Guardalo en la carpeta que corresponda con nombre `mensaje-<tipo>-<AAAA-MM-DD>.md`: la del candidato (`busquedas/<cliente-rol>/candidatos/<candidato>/`) o la de la búsqueda si es al cliente.
4. Preguntá si lo va a mandar. Cuando confirme que lo mandó, registralo con `actualizar`: historial, acción hecha, `devolucion: "enviada"` si era una devolución, y el próximo follow-up si corresponde.

Ejemplo de primer contacto por LinkedIn, ilustrativo y con datos ficticios (el rol, el pitch y el tono salen siempre de `perfil-del-rol.md` y `voz.md`):

```text
Hola Valentina, vi que en Billetera Sur llevaste el onboarding de comercios desde cero.
Estoy buscando una PM Sr para pagos en una fintech regional: el rol arma el producto de cobros para pymes, con un squad propio.
Es remoto desde LATAM. ¿Te sirve que lo charlemos 15 minutos esta semana? Si no es momento, decime y no te escribo más.

(368 caracteres)
```

**Claude nunca envía el mensaje**, aunque tenga una herramienta de correo o de mensajería conectada, salvo que la persona lo pida expresamente para ese mensaje. Aun así, mostrá el texto final y el destinatario y esperá un "sí" antes de enviarlo.
