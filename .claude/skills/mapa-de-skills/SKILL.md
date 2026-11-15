---
name: mapa-de-skills
description: "El índice de todos los skills del Recruiting OS: qué skill resuelve cada cosa, en qué orden conviene usarlos y qué no cubre ninguno todavía. Usala para elegir el skill correcto en vez de adivinar, cuando alguien pregunte 'qué puedo hacer con esto', 'qué skills hay', 'por dónde empiezo', 'cuál uso para...', o cuando un pedido no encaja claramente en un skill."
---

# mapa-de-skills — qué skill usar para cada cosa

> Adaptado de `product-builder-resolver`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT), a través de `busqueda-laboral-os`.

Una fila por necesidad. La columna Skill dice cuál cargar; todos viven en `.claude/skills/<skill>/SKILL.md`. Hablá en rioplatense, con voseo.

## El día a día

| Necesidad | Skill |
|---|---|
| Arrancar el sistema por primera vez: la consultora, su método, su voz, su política de datos, clientes y búsquedas en curso | `empezar` |
| Preparar el arranque con un hiring manager | `nueva-busqueda` (modo preparar) |
| Abrir una búsqueda con las notas del arranque: perfil del rol y scorecard | `nueva-busqueda` |
| Ajustar el scorecard porque el cliente cambió lo que busca | `nueva-busqueda` (modo ajustar) |
| Evaluar uno o varios CVs o perfiles contra el scorecard | `evaluar-candidato` |
| Contar una novedad (respondió, la entrevistaron, la descartaron, aceptó) y actualizar el tablero | `actualizar` |
| Armar la guía de entrevista de la búsqueda, de un candidato o para el hiring manager | `guia-de-entrevista` |
| Armar un caso de Producto o de Atención al cliente para la entrevista | `guia-de-entrevista` (sus criterios de producto y de atención) |
| Registrar una entrevista o el feedback del cliente contra el scorecard | `registrar-entrevista` |
| Escribir un primer contacto, follow-up, invitación, devolución o mensaje al cliente | `redactar-mensaje` |
| Repasar la semana de toda la cartera | `reporte-semanal` |
| Armar el reporte para el cliente de una búsqueda | `reporte-semanal <búsqueda>` |
| Cerrar una búsqueda y sacar aprendizajes | `actualizar` y después `reporte-semanal <búsqueda> cierre` |

## Criterio y cuidado

| Necesidad | Skill |
|---|---|
| Poner a prueba un requisito, un scorecard, una evaluación, un descarte o una decisión | `poner-a-prueba` |
| Revisar qué datos de candidatos vencieron, borrar a alguien, registrar un permiso | `privacidad` |

## Recorridos típicos

- **Primera semana:** `empezar` → `nueva-busqueda` para cada búsqueda abierta sin scorecard.
- **Cada búsqueda nueva:** `nueva-busqueda` (preparar) → arranque con el hiring manager → `nueva-busqueda` (armar) → `guia-de-entrevista` (base y para el hiring manager).
- **Cada perfil:** `evaluar-candidato` → `redactar-mensaje` (contacto) → `guia-de-entrevista` (candidato) → `registrar-entrevista`.
- **Cada novedad:** `actualizar` (y `redactar-mensaje` si hay que responder).
- **Cada descarte:** `actualizar` → `redactar-mensaje` (devolución) dentro del plazo.
- **Cada viernes:** `reporte-semanal` (cartera) y `reporte-semanal <búsqueda>` para cada cliente.
- **Cada mes:** `privacidad revisar`.

## Lo que todavía no está

Estos skills están planeados para la próxima versión. Mientras tanto, un pedido de este tipo se responde con criterio general y se dice que el skill específico todavía no existe:

| Necesidad | Skill planeado |
|---|---|
| Redactar el aviso para LinkedIn y portales | `redactar-aviso` |
| Comparar finalistas y armar la presentación de la terna | `armar-terna` |
| Traer novedades desde Gmail y Google Calendar | `sincronizar-correo` |
| Búsquedas booleanas, referidos y a quién buscar | `plan-de-sourcing` |
| Por qué alguien bueno dejaría su trabajo por este rol | `pitch-del-rol` |
| Probar un aviso o un mensaje contra candidatos simulados | `candidatos-sinteticos` |
| Por qué una búsqueda no avanza y qué medir | `diagnostico-proceso` |
| Dónde está el talento y rangos del mercado, con fuentes | `mapeo-de-mercado` |
| Patrones de varias búsquedas cerradas | `aprendizajes` |
| Reporte o presentación con diseño | `disenador-visual` |

Un pedido que ninguna fila cubre no se resuelve improvisando con uno de estos skills: se dice qué falta. Si el pedido es de un área fuera de alcance (Tecnología, Diseño, contratación masiva), se dice en una línea (ver «Alcance» en `CLAUDE.md`).

## Ejemplo

```text
Pedido: "El cliente me rechazó los tres candidatos de la terna, ¿qué hago?"

Respuesta: Primero registrá el feedback de cada uno con registrar-entrevista, para tenerlo contra el scorecard.
Si los tres fallan en el mismo criterio, el problema puede estar en el scorecard o en el sourcing:
poner-a-prueba sobre ese criterio, y después nueva-busqueda en modo ajustar con el cliente.
¿Arrancamos por el feedback?
```
