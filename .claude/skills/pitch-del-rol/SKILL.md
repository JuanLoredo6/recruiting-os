---
name: pitch-del-rol
description: "Arma la propuesta del rol para el candidato: por qué alguien bueno, que hoy está bien en su trabajo, dejaría todo por este. Explora ángulos verdaderos a partir del perfil del rol, del cliente y de lo que dijeron candidatos reales (con la consultora eligiendo, nunca Claude), y escribe el mapa de valor del rol, el pitch de 30 segundos para el primer contacto, el de 2 minutos para el screening y las respuestas a las objeciones típicas. Usala cuando digan 'cómo vendo este rol', 'nadie responde los mensajes', 'qué le digo a un candidato pasivo', 'por qué alguien se cambiaría a esta empresa', 'armá el pitch', o después de nueva-busqueda."
license: "MIT. Adapta material de Pedro Romero Luna (MIT); ver CREDITOS.md y .claude/skills/LICENSE-ai-first-product-skills.txt."
---

# pitch-del-rol — por qué alguien bueno se cambiaría

> Adaptado de `ideation-engine` y `prd`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT), a través de la fase de propuesta de valor de `posicionamiento` en `busqueda-laboral-os`.

Los mejores candidatos de Producto y de Atención al cliente casi nunca están buscando: hay que darles una razón para escuchar. "Excelente oportunidad en empresa líder" no es una razón. Este skill encuentra las razones verdaderas y las convierte en un pitch.

Hablá en rioplatense, con voseo.

## Regla número uno

**Claude propone, siembra y sintetiza; la consultora elige el ángulo.** Y nada entra al pitch si no es verdad: cada razón sale del perfil del rol, del cliente o de lo que dijeron candidatos reales, con su fuente. Un pitch que promete lo que el rol no tiene trae candidatos que se van a los seis meses.

## Antes de empezar

Leé `busquedas/<cliente-rol>/perfil-del-rol.md`, `clientes/<cliente>/cliente.md` y, si hay, los historiales y registros de candidatos de esta búsqueda o de búsquedas anteriores con el mismo cliente (qué les atrajo, qué los frenó, por qué se retiraron). **Sin perfil del rol no hay pitch:** ofrecé `/nueva-busqueda` primero.

## 1. Las razones verdaderas

Con el método de `.claude/skills/poner-a-prueba/SKILL.md#método`, armá la lista de lo que el rol ofrece de verdad, cada ítem con su fuente:

- **El problema:** qué va a resolver la persona y por qué es interesante (escala, impacto, novedad).
- **El alcance:** qué decide, qué construye o qué arma desde cero.
- **El equipo y quién lidera:** con quién va a aprender o a quién va a formar.
- **El momento de la empresa:** etapa, crecimiento, financiamiento, con fuente.
- **Las condiciones:** modalidad, rango, flexibilidad, lo que el cliente confirmó.
- **Lo que les importó a candidatos reales**, con su cita, de los historiales y registros.

Lo que no tiene fuente se marca ❓ y se le pregunta al cliente. Lo que el rol no tiene (por ejemplo, no hay equipo propio) se escribe también: es la objeción que va a venir.

## 2. Por qué se quedaría donde está

Para el candidato al que apunta la búsqueda (del perfil del rol), las cuatro fuerzas de un cambio:

| Fuerza | Pregunta |
|---|---|
| Empuje | ¿Qué le suele molestar en su trabajo actual a alguien así? |
| Atracción | ¿Qué de este rol resuelve eso? |
| Ansiedad | ¿Qué miedo tendría al cambiar? (estabilidad, empresa más chica, un líder que no conoce) |
| Hábito | ¿Qué lo retiene? (antigüedad, acciones, comodidad, un equipo que armó) |

Lo que sale de evidencia (candidatos reales, el perfil del rol) lleva su cita; lo que es lectura va con 🔍.

## 3. Ángulos

Proponé de 3 a 5 ángulos para presentar el rol, cada uno con la técnica que lo produjo, para que no salgan todos iguales:

- **[PROBLEMA]:** abrir por lo que va a resolver ("vas a armar desde cero el cobro a pymes en tres países").
- **[PERSONA]:** abrir por quién lidera o con quién trabaja.
- **[MOMENTO]:** abrir por la etapa de la empresa.
- **[INVERSIÓN]:** dar vuelta lo que parece una debilidad ("es una empresa chica: vas a decidir vos").
- **[CONTRASTE]:** contra el trabajo típico de alguien así ("si hoy ejecutás un roadmap que te dan, acá lo definís").

Cada ángulo con las razones verdaderas que lo sostienen. Un ángulo sin una razón con fuente no entra.

**Si la consultora quiere armar sus propios ángulos primero** (sola o con el equipo), los de Claude se muestran después, para no anclar.

La consultora elige uno o dos. Si piden que elija Claude, decí qué evidencia sostiene a cada uno y devolvé la decisión.

## 4. El pitch

Con el ángulo elegido, escribí `busquedas/<cliente-rol>/pitch.md`:

```
## Mapa de valor del rol
## Pitch de 30 segundos
## Pitch de 2 minutos
## Objeciones y respuestas
## Lo que no hay que prometer
```

- **Mapa de valor del rol:** las razones verdaderas ordenadas por lo que alivian (empuje) o lo que ganan (atracción), cada una con su fuente.
- **Pitch de 30 segundos:** para el primer contacto escrito o la primera frase de una llamada. Por qué esta persona, el rol en una línea y la razón más fuerte.
- **Pitch de 2 minutos:** para el screening: el problema, el alcance, el equipo, las condiciones y el proceso.
- **Objeciones y respuestas:** las de la fuerza de ansiedad y hábito, cada una con una respuesta verdadera. Si no hay respuesta verdadera, se dice ("es cierto, no hay equipo propio el primer año") y se ofrece lo que sí hay.
- **Lo que no hay que prometer:** lo que el rol no tiene o el cliente no confirmó.

Pasá los textos por `.claude/skills/redactar-mensaje/SKILL.md#revisión-de-voz`. Copiá con el visto bueno el pitch de 30 segundos a la sección «Pitch del rol» de `perfil-del-rol.md`, que es la versión viva que usan `redactar-mensaje` y `redactar-aviso`.

Si quieren probarlo antes de usarlo: `/candidatos-sinteticos` con el pitch.

## Reglas

- Ninguna razón sin fuente; ninguna promesa que el cliente no confirmó.
- Claude no elige el ángulo.
- No se ocultan las debilidades del rol: se responden.
