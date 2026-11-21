# Métricas de la consultora — el Informe de métricas

> Es el modo métricas de `diagnostico-proceso` (`.claude/skills/diagnostico-proceso/SKILL.md`). Se carga cuando el filtro de la métrica no pasa, cuando preguntan cómo medir su trabajo o una búsqueda, o desde `reporte-semanal` si todavía no hay indicador.

> Adaptado de `product-metrics`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT), a través de `busqueda-laboral-os`.

Define el indicador principal de la consultora (o de una búsqueda), el árbol de palancas que lo sostienen, un número por hipótesis activa y las antimétricas.

Hablá en rioplatense, con voseo (o en portugués de Brasil, si la consultora lo eligió: ver «Idioma» en `CLAUDE.md`).

## La entrevista

Se corre con el método de `.claude/skills/poner-a-prueba/SKILL.md#método`.

Antes de preguntar: si hay un Diagnóstico en `investigacion/`, las hipótesis activas salen de ahí. Leé `busquedas/busquedas.json`: es la fuente de casi todos los valores de hoy. Calculalos vos, no los preguntes.

### 1. Indicador principal

Uno solo, con el motivo en una línea: qué decisión mueve.

> Ejemplo: "Presentados que el cliente avanza a su entrevista, por búsqueda. Si baja del 50 % en dos búsquedas seguidas, revisamos el scorecard con el cliente antes de seguir buscando."

"Búsquedas cubiertas" sirve como resultado del negocio, pero llega tarde: no dice nada mientras la búsqueda corre.

### 2. Árbol de palancas

```
Presentados que el cliente avanza
├── Perfiles que cumplen los excluyentes, por semana   (tablero: candidatos con evaluación sin ❌ en excluyentes)
├── Tasa de respuesta de esos perfiles                  (tablero: identificado → contactado → screening)
├── Calidad del screening                               (tablero: screening → entrevista-cliente, y motivos de descarte del cliente)
└── Días de respuesta del cliente                       (tablero: historial, desde entrevista-cliente hasta su feedback)
```

Cada palanca con dónde se mide. Una palanca sin "dónde se mide" es un hueco.

### 3. Un número por hipótesis activa

Para cada hipótesis: qué número la confirma o la refuta, cómo se mide y cuánto vale hoy. **Sin valor con fuente, no hay dato:** se anota como hueco con quién lo cierra.

### 4. Antimétricas

Lo que no tiene que empeorar mientras el indicador mejora, con su umbral verificable:

- **Velocidad a costa de calidad:** más del 30 % de los presentados descartados por el cliente en un excluyente del scorecard.
- **Candidatos sin devolución:** alguna devolución pendiente fuera del plazo de `contexto/consultora.md`.
- **Embudo por volumen:** más de 40 contactados por búsqueda sin llegar a 3 en screening (señal de sourcing poco preciso).
- **Sesgo en la terna:** todas las ternas salen del mismo canal o del mismo tipo de empresa durante un trimestre (se revisa con datos del tablero, nunca con atributos protegidos).
- **Desgaste del equipo:** más búsquedas abiertas por persona que las que la consultora definió como sostenibles.

### La métrica de vanidad

Después de cada métrica propuesta: **¿qué decisión cambia este número, se mueva para donde se mueva?** Si no hay respuesta, es de vanidad: "perfiles revisados", "mensajes enviados", "conexiones nuevas". Se dice así y se pide la decisión antes de aceptarla.

## El Informe de métricas

Escribí, fechado, `investigacion/<AAAA-MM-DD>-metricas.md`:

```
## Indicador principal
## Árbol de palancas
## Número por hipótesis
## Antimétricas
```

Las de vanidad quedan escritas con la etiqueta "(vanidad: no cambia [la decisión que se pidió])".

Con el visto bueno, el indicador y las antimétricas se copian a `contexto/consultora.md`, sección nueva `## Cómo medimos`, que es la versión viva que usa `reporte-semanal`.
