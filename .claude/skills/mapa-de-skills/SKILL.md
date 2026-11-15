---
name: mapa-de-skills
description: "El índice de todos los skills del Recruiting OS: qué skill resuelve cada cosa, en qué orden conviene usarlos y qué no cubre ninguno todavía. Usala para elegir el skill correcto en vez de adivinar, cuando alguien pregunte 'qué puedo hacer con esto', 'qué skills hay', 'por dónde empiezo', 'cuál uso para...', o cuando un pedido no encaja claramente en un skill."
license: "MIT. Adapta material de Pedro Romero Luna (MIT); ver CREDITOS.md y .claude/skills/LICENSE-ai-first-product-skills.txt."
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
| Redactar o revisar el aviso para LinkedIn, portales o la web del cliente | `redactar-aviso` |
| Evaluar uno o varios CVs o perfiles contra el scorecard | `evaluar-candidato` |
| Contar una novedad (respondió, la entrevistaron, la descartaron, aceptó) y actualizar el tablero | `actualizar` |
| Traer al tablero lo que llegó por Gmail o Google Calendar (botón 🔄 SYNC, o sola cada 2 horas) | `sincronizar-correo` |
| Armar la guía de entrevista de la búsqueda, de un candidato o para el hiring manager | `guia-de-entrevista` |
| Armar un caso de Producto o de Atención al cliente para la entrevista | `guia-de-entrevista` (sus criterios de producto y de atención) |
| Registrar una entrevista o el feedback del cliente contra el scorecard | `registrar-entrevista` |
| Comparar finalistas, decidir la terna y armar su presentación al cliente | `armar-terna` |
| Ayudar al cliente a decidir entre dos finalistas | `armar-terna` (modo desempatar) |
| Escribir un primer contacto, follow-up, invitación, devolución o mensaje al cliente | `redactar-mensaje` |
| Repasar la semana de toda la cartera | `reporte-semanal` |
| Armar el reporte para el cliente de una búsqueda | `reporte-semanal <búsqueda>` |
| Cerrar una búsqueda y sacar aprendizajes | `actualizar` y después `reporte-semanal <búsqueda> cierre` |

## Estrategia de la búsqueda

| Necesidad | Skill |
|---|---|
| Saber si hay talento para el rol, qué tan difícil es y rangos con fuente | `mapeo-de-mercado` |
| Por qué alguien bueno dejaría su trabajo por este rol: pitch y objeciones | `pitch-del-rol` |
| A quién buscar, dónde, búsquedas booleanas y referidos | `plan-de-sourcing` |
| Entender por qué una búsqueda no avanza | `diagnostico-proceso` |
| Definir qué números mirar en la consultora o en una búsqueda | `diagnostico-proceso` (su modo métricas) |
| Sacar patrones de varias búsquedas: qué valoran los clientes, por qué se caen candidatos | `aprendizajes` |

## Criterio y cuidado

| Necesidad | Skill |
|---|---|
| Poner a prueba un requisito, un scorecard, una evaluación, un descarte o una decisión | `poner-a-prueba` |
| Probar un aviso, un mensaje o el pitch contra candidatos simulados antes de usarlo | `candidatos-sinteticos` |
| Revisar qué datos de candidatos vencieron, borrar a alguien, registrar un permiso | `privacidad` |
| Especificar y construir una terna, un reporte o una propuesta con diseño | `disenador-visual` |

## Recorridos típicos

- **Primera semana:** `empezar` → `nueva-busqueda` para cada búsqueda abierta sin scorecard → `sincronizar-correo configurar` (opcional).
- **Antes de aceptar una búsqueda:** `mapeo-de-mercado`.
- **Cada búsqueda nueva:** `nueva-busqueda` (preparar) → arranque con el hiring manager → `nueva-busqueda` (armar) → `pitch-del-rol` → `redactar-aviso` y `plan-de-sourcing` → `guia-de-entrevista` (base y para el hiring manager). Si el aviso o el mensaje son importantes, `candidatos-sinteticos` antes de usarlos.
- **Cada perfil:** `evaluar-candidato` → `redactar-mensaje` (contacto) → `guia-de-entrevista` (candidato) → `registrar-entrevista`.
- **Cada novedad:** `actualizar` (y `redactar-mensaje` si hay que responder). Lo que llega por mail o calendario lo trae `sincronizar-correo`.
- **Cuando hay finalistas:** `armar-terna` → `disenador-visual` si quieren una versión con diseño.
- **Cada descarte:** `actualizar` → `redactar-mensaje` (devolución) dentro del plazo.
- **Cada viernes:** `reporte-semanal` (cartera) y `reporte-semanal <búsqueda>` para cada cliente.
- **Cuando una búsqueda se traba:** `diagnostico-proceso` → `mapeo-de-mercado` o `nueva-busqueda` (ajustar) según la hipótesis.
- **Cada mes:** `privacidad revisar`. **Cada trimestre:** `aprendizajes`.

Un pedido que ninguna fila cubre no se resuelve improvisando con uno de estos skills: se dice qué falta. Si el pedido es de un área fuera de alcance (Tecnología, Diseño, contratación masiva), se dice en una línea (ver «Alcance» en `CLAUDE.md`).

## Ejemplo

```text
Pedido: "El cliente me rechazó los tres candidatos de la terna, ¿qué hago?"

Respuesta: Primero registrá el feedback de cada uno con registrar-entrevista, para tenerlo contra el scorecard.
Si los tres fallan en el mismo criterio, el problema puede estar en el scorecard o en el sourcing:
poner-a-prueba sobre ese criterio, y después nueva-busqueda en modo ajustar con el cliente.
¿Arrancamos por el feedback?
```
