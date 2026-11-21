---
name: diagnostico-proceso
description: "Entrevista socrática para entender por qué una búsqueda (o la forma de trabajar de la consultora) no avanza: separa el síntoma ('no hay candidatos', 'el cliente rechaza a todos', 'se nos caen en la oferta') de la causa, ubica el problema en una etapa del embudo, ordena la evidencia, exige un número que muestre si se resuelve y prioriza hasta tres hipótesis para probar. Escribe el Diagnóstico. Su modo métricas define qué medir: indicador principal, árbol de palancas, un número por hipótesis y antimétricas (velocidad a costa de calidad, candidatos sin devolución). Usala cuando una búsqueda se traba, cuando digan 'no sé qué pasa con esta búsqueda', 'el cliente no quiere a nadie', 'cómo medimos cómo trabajamos', 'qué número miramos', aunque no nombren el skill."
license: "MIT. Adapta material de Pedro Romero Luna y de Paweł Huryn (MIT); ver CREDITOS.md, .claude/skills/LICENSE-ai-first-product-skills.txt y .claude/skills/LICENSE-phuryn.txt."
---

# diagnostico-proceso — el Diagnóstico de una búsqueda

> Adaptado de `product-strategy`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT), a través de `diagnostico-busqueda` en `busqueda-laboral-os`.

Cuando una búsqueda se traba, la reacción típica es hacer más de lo mismo: más mensajes, más perfiles. Este skill frena antes, separa el síntoma de la causa y cierra con hasta tres hipótesis que se pueden probar esta semana.

Hablá en rioplatense, con voseo (o en portugués de Brasil, si la consultora lo eligió: ver «Idioma» en `CLAUDE.md`), frases cortas.

## Alcance

| Pedido | Qué se diagnostica |
|---|---|
| `/diagnostico-proceso <cliente-rol>` | Una búsqueda |
| `/diagnostico-proceso` sin búsqueda | La forma de trabajar de la consultora (varias búsquedas) |
| "Cómo medimos", "qué número miramos" | Directo al modo métricas: leé y seguí `.claude/skills/diagnostico-proceso/metricas.md` |

## Antes de empezar

Leé lo que el repo ya sabe, para no preguntarlo: `busquedas/busquedas.json` (candidatos por etapa, días en cada etapa, motivos de descarte y de retiro), `perfil-del-rol.md`, los registros de entrevista y el feedback del cliente de la búsqueda, `clientes/<cliente>/cliente.md` y `contexto/consultora.md` (tiempos objetivo). Calculá los números del embudo vos: llegá a la entrevista con datos, no con impresiones.

## La entrevista

Se corre con el método de `.claude/skills/poner-a-prueba/SKILL.md#método`.

### Socrática: no da la razón a la primera

Si el planteo llega como solución ("hay que subir el rango", "necesitamos LinkedIn Recruiter", "hay que contactar a más gente"), devolvé la repregunta que separa la solución del problema:

> Mal: "Buena idea, ¿cuánto lo subimos?"
>
> Bien: "Eso es una solución. ¿Qué problema resuelve? ¿Los candidatos se retiran por el rango, o es algo que suponés? En el tablero, de 4 retirados, 1 dijo rango y 3 aceptaron otra oferta antes de que el cliente respondiera."

**Primero la mejor versión, después la pregunta.** Antes de cuestionar una explicación, decí en una línea la versión más fuerte de por qué podría ser cierta, y cuestioná esa. Si una explicación ya viene con buena evidencia, decilo.

> Adaptado de `strategy-red-team`, de Paweł Huryn ([pm-skills](https://github.com/phuryn/pm-skills), licencia MIT).

### Las etapas del embudo

1. **Definir:** que el perfil del rol y el scorecard sean claros, realistas y compartidos con el cliente.
2. **Atraer:** que aparezcan perfiles que cumplan los excluyentes (aviso, sourcing, referidos).
3. **Interesar:** que los perfiles buenos respondan y acepten charlar.
4. **Evaluar:** que el screening de la consultora filtre bien (lo que pasa, el cliente también lo quiere).
5. **Convencer al cliente:** que el cliente avance con los presentados y responda a tiempo.
6. **Cerrar:** que la oferta llegue, sirva y se acepte.

Un problema en una etapa casi siempre se ve en la siguiente: "el cliente rechaza a todos" (5) puede venir de un scorecard que el cliente no comparte (1) o de un screening que deja pasar demasiado (4).

### Jerarquía de evidencia

`conducta > dato > afirmación > suposición`.

- "Creo que el rango es bajo" es una **suposición**.
- "Dos candidatos dijeron que el rango era bajo" es una **afirmación** (de ellos) con **dato** (dos de cuántos).
- "De 12 contactados que cumplen los excluyentes, respondieron 2" es un **dato**.
- "Carla rechazó a los tres de la terna por 'poca profundidad en métricas', y el scorecard no tiene ese criterio" es **conducta** del cliente contra un documento.

La evidencia de menor nivel también se anota, con su nivel.

### El filtro de la métrica

**Si no hay un número, el problema no está claro.** ¿Qué número se movería si esto se resolviera? Por ejemplo: tasa de respuesta de perfiles que cumplen, presentados que el cliente avanza, días de respuesta del cliente, ofertas aceptadas. Si no hay respuesta, o es de vanidad (perfiles revisados, mensajes enviados), el filtro no pasa: decilo y pasá al modo métricas antes de seguir.

### Hipótesis, con formato fijo

```
Creemos que [quién: candidatos de X perfil, el hiring manager, el cliente] [hace X] en [qué etapa] porque [causa]; si es cierto, vamos a ver [evidencia].
```

Ejemplo: "Creemos que el hiring manager rechaza a los presentados en la etapa de convencer al cliente porque evalúa un criterio (profundidad en métricas) que no está en el scorecard; si es cierto, vamos a ver que al sumarlo y re-evaluar, los próximos dos presentados que lo cumplan pasan su entrevista."

**Como mucho 3, priorizadas por riesgo × impacto × qué tan barato es probarla.** Cada hipótesis lleva su **criterio para abandonarla**. Una cuarta va a `contexto/datos-pendientes.md`.

## El Diagnóstico

Escribí, fechado, `investigacion/<AAAA-MM-DD>-diagnostico-<cliente-rol o consultora>.md`:

```
## Problema
## Evidencia
## Filtro de la métrica
## Hipótesis priorizadas
## Lo que sí se sostiene
```

- **Problema:** el síntoma separado de la causa, en qué etapa del embudo y por qué ahora.
- **Evidencia:** cada dato con su nivel al lado.
- **Filtro de la métrica:** si pasó o no; si no, el pase al modo métricas explícito.
- **Hipótesis priorizadas:** hasta 3, con el formato fijo, el motivo del orden y el criterio para abandonarla.
- **Lo que sí se sostiene:** lo que la evidencia muestra que funciona (un canal que trae buenos perfiles, una etapa que se pasa bien). Se escribe siempre: evita cambiar lo que anda.

Por cada hipótesis, proponé una acción concreta para probarla y, si la aceptan, sumala al tablero. Si la hipótesis toca al cliente, ofrecé el mensaje (`/redactar-mensaje cliente <cliente-rol>`) o el ajuste del scorecard (`/nueva-busqueda <cliente-rol>`, modo ajustar).

## Lo que este entregable no es

Una foto fechada, no la definición del rol (eso es `perfil-del-rol.md`). Los patrones de varias búsquedas cerradas son trabajo de `aprendizajes`.
