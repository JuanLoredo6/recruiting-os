---
name: plan-de-sourcing
description: "Diseña cómo encontrar candidatos para una búsqueda: a quién buscar según lo que hizo (no según el cargo), las empresas y equipos fuente, las búsquedas booleanas para LinkedIn y Google, los pedidos de referidos, la base propia de la consultora y las comunidades, con el mensaje de contacto para cada canal. No navega ni actúa en LinkedIn: arma todo para que la persona lo haga. Usala cuando digan 'dónde busco', 'armá las búsquedas booleanas', 'no encuentro candidatos', 'a quién le pido referidos', 'de qué empresas saco perfiles', o después de nueva-busqueda."
---

# plan-de-sourcing — buscar por lo que hicieron, no por el cargo

> Adaptado de `ux-research`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT), a través de `plan-de-networking` en `busqueda-laboral-os`.

Buscar "Product Manager" en LinkedIn trae miles de perfiles que no se parecen entre sí. Buscar a "quien llevó el checkout de una billetera en los últimos dos años" trae pocos y buenos. Este skill traduce el scorecard en dónde y cómo buscar.

Hablá en rioplatense, con voseo.

## Antes de empezar

Leé `busquedas/<cliente-rol>/perfil-del-rol.md` (scorecard y señales de alerta), `pitch.md` si existe, `clientes/<cliente>/cliente.md` (empresas de las que no se puede sacar gente, si hay acuerdos de no contratación) y el último `investigacion/*-mapeo-*.md` de este rol, si existe. **Sin scorecard no hay plan:** ofrecé `/nueva-busqueda`.

Preguntá en una línea si hay empresas vedadas: clientes de la consultora, el propio cliente, acuerdos de no contratación. Nunca se hace sourcing en un cliente activo de la consultora sin que la consultora lo decida.

## 1. A quién buscar: por conducta

Con el método de `.claude/skills/poner-a-prueba/SKILL.md#método`, convertí los excluyentes del scorecard en un criterio de búsqueda verificable en un perfil público:

> Mal: "PMs senior de fintech".
>
> Bien: "Personas que en los últimos 3 años tuvieron a cargo un flujo de pagos o cobros (checkout, onboarding de comercios, conciliación) en una billetera, un PSP o un banco digital".

Por cada criterio: qué palabras o señales lo muestran en un perfil (títulos, productos, verbos, logros) y qué lo descarta.

## 2. Dónde están

- **Empresas y equipos fuente:** dónde hay gente que hizo eso, con el motivo y su fuente (el producto que tienen, una nota de prensa, `mapeo-de-mercado`). Separá las vedadas.
- **Trayectorias adyacentes:** de dónde viene gente que podría hacerlo aunque nunca haya tenido ese cargo (por ejemplo, un analista de operaciones de pagos que pasó a producto, o un líder de calidad que podría ser gerente de atención). Cada una con lo que hay que validar.
- **Comunidades:** grupos, meetups, newsletters del rubro donde se puede publicar.
- **Base propia:** candidatos de búsquedas anteriores con consentimiento para la base de talento (en `busquedas/busquedas.json`, con su historial). Solo esos.
- **Referidos:** a quién de la red de la consultora o del cliente pedirle nombres, con el criterio de conducta en la mano.

## 3. Búsquedas booleanas

Para LinkedIn (búsqueda de personas o Recruiter, según lo que tenga la consultora) y para Google (`site:linkedin.com/in`):

- De 3 a 5 búsquedas, de la más precisa a la más amplia, cada una con qué criterio ataca.
- Sinónimos en español, inglés y portugués si la búsqueda es regional ("atención al cliente" OR "customer support" OR "CX" OR "atendimento").
- Exclusiones útiles (NOT para títulos que no aplican, como recruiters o ventas).
- Una línea con qué revisar a mano en cada resultado.

**Claude no corre las búsquedas en LinkedIn ni abre perfiles.** Las arma para que la persona las pegue. Si la persona pega resultados o perfiles, se evalúan con `evaluar-candidato`.

## 4. Mensajes por canal

Uno por canal (primer contacto a un perfil, pedido de referido, publicación en una comunidad), armados con `redactar-mensaje` y el pitch de 30 segundos. Cada uno cita qué de la trayectoria de esa persona motiva el contacto.

## 5. Metas y ritmo

- Cuántos perfiles identificar y contactar por semana para llegar a la terna en la fecha objetivo, con el supuesto de respuesta escrito (🔍 si no hay dato propio de la consultora). Si hay historial de búsquedas parecidas en el JSON, usá esa tasa.
- Cuándo revisar el plan: si en una semana no aparece nadie que cumpla los excluyentes, el problema puede ser el scorecard o el mercado, no el esfuerzo (ver `diagnostico-proceso`).

## El Plan

Escribí `busquedas/<cliente-rol>/sourcing.md`, con fecha:

```
## A quién buscar
## Dónde están
## Búsquedas
## Mensajes
## Metas y ritmo
```

Ofrecé sumar acciones al tablero: "Correr las búsquedas 1 a 3 y pasar perfiles a evaluar", "Pedir referidos a <nombre>", "Publicar en <comunidad>", con fecha y pedido.

## Reglas

- Solo perfiles públicos, la red propia y la base con consentimiento. Nada de listas compradas ni datos sacados de cualquier lado.
- Un perfil identificado por sourcing entra al sistema con `consentimiento: null` y la fecha de borrado corta de `contexto/privacidad.md`.
- Ningún criterio de búsqueda por atributo protegido (edad por años de egreso, género por nombre, universidad como filtro de clase).
- Claude no actúa en LinkedIn ni envía mensajes.
