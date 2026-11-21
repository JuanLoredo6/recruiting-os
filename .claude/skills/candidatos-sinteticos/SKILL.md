---
name: candidatos-sinteticos
description: "Prueba un aviso, un mensaje de sourcing, el pitch del rol o una guía de entrevista contra candidatos simulados antes de usarlos con personas reales: un candidato pasivo que está bien donde está, uno escéptico, uno sobrecalificado, uno que cumple pero duda por la modalidad. Cada rasgo marcado como evidencia, dato público o suposición, cada reacción con el rasgo en que se apoya, y siempre un escéptico. Encuentra defectos y escribe la versión 2 de la pieza. No valida nada. Usala cuando digan 'probá este aviso', 'esto lo respondería alguien?', 'cómo lo leería un candidato', 'nadie responde, ¿qué está mal en el mensaje?', o antes de publicar o mandar algo importante."
license: "MIT. Adapta material de Pedro Romero Luna (MIT); ver CREDITOS.md y .claude/skills/LICENSE-ai-first-product-skills.txt."
---

# candidatos-sinteticos — diagnóstico y versión 2 de la pieza

> Adaptado de `synthetic-users`, de Pedro Romero Luna ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licencia MIT), a través de `recruiters-sinteticos` en `busqueda-laboral-os`.

Prueba una pieza de la búsqueda (aviso, mensaje de sourcing, pitch del rol, guía de entrevista, devolución) contra personajes simulados con rasgos explícitos. Sirve para encontrar defectos antes de gastar el primer contacto con un candidato real.

Hablá en rioplatense, con voseo (o en portugués de Brasil, si la consultora lo eligió: ver «Idioma» en `CLAUDE.md`).

## Regla número uno

**Esto NO valida NADA.** Abrí la sesión con esa frase y repetila al cerrar. Ninguna reacción de un personaje simulado prueba que la pieza funciona con personas reales. Sirve para una sola cosa: encontrar defectos antes de usarla.

## Antes de armar los personajes

Preguntá en una línea, si no está claro: ¿qué pieza y para qué búsqueda? Leé `perfil-del-rol.md` (el perfil al que apunta la búsqueda es la mejor fuente de rasgos con evidencia), `pitch.md` si existe, y los historiales y registros de candidatos reales de esta búsqueda o del mismo cliente (qué respondieron, por qué se retiraron).

## Los personajes

Se arman con el método de `.claude/skills/poner-a-prueba/SKILL.md#método`: cada rasgo propuesto se aprieta por su origen antes de entrar.

Cada rasgo lleva su origen marcado:

| Marca | Origen |
|---|---|
| **(evidencia)** | Algo real: lo que dijo un candidato de esta búsqueda o de una anterior, el perfil del rol, un motivo de retiro registrado |
| **(dato público: <fuente>)** | Un estudio o encuesta pública sobre cómo deciden los candidatos, con nombre y link |
| **(suposición)** | Una construcción sin evidencia ni dato público detrás |

Un rasgo sin marca no entra. **Antes de marcar un rasgo como suposición, buscalo en fuentes públicas.** Un dato público nunca se marca como evidencia: describe a candidatos en general, no a quien va a leer este mensaje.

**Ningún personaje se arma sobre atributos protegidos** (edad, género, origen). Los rasgos son de situación y de conducta: está cómodo en su trabajo, tiene acciones por cobrar, viene de una empresa grande, ya lo contactaron diez consultoras este mes.

**Siempre al menos un escéptico**, con su motivo: alguien que recibe cinco mensajes de recruiters por semana, alguien a quien una consultora le hizo ghosting, alguien que desconfía de las startups. Personajes que solo se entusiasman no encuentran defectos.

Elenco típico, ajustado a la pieza:

- **Candidato pasivo que cumple el perfil:** está bien donde está.
- **El escéptico.**
- **Alguien que cumple casi todo y duda** (por la modalidad, el rango, la etapa de la empresa).
- Para un aviso, opcional: **alguien que no cumple los excluyentes y se postularía igual**, para ver si el aviso lo filtra.

**Cada reacción nombra el rasgo en que se apoya**, con su marca. La reacción siempre es inventada, sea cual sea la marca del rasgo.

**Ningún "me interesa" sin su costo al lado:** qué le preocupa, qué tendría que creer para responder.

## Defectos a buscar

Cada defecto encontrado se anota con su reescritura al lado:

| Defecto | Ejemplo | Reescritura |
|---|---|---|
| Genérico, podría ser de cualquier búsqueda | "Excelente oportunidad en empresa líder" | La razón verdadera del pitch del rol |
| No dice por qué a esta persona | "Vi tu perfil y me pareció interesante" | Qué de su trayectoria motiva el contacto |
| Esconde lo que el candidato quiere saber | Sin modalidad, sin rango, sin nombre del rol | Lo que el cliente autorizó decir |
| Requisitos que espantan | Lista de 12 herramientas | Los excluyentes del scorecard |
| Pedido difícil de responder | "Mandame tu CV actualizado y tu pretensión" | "¿Te sirven 15 minutos el jueves?" |
| Tono de plantilla | "Espero que estés muy bien" | Ver la revisión de voz |
| Demasiado largo para el canal | Mensaje de LinkedIn de 6 párrafos | Ajustar al canal |
| No filtra (en avisos) | Quien no cumple se postularía igual | Excluyentes más claros |

Revisá también contra las muletillas de `.claude/skills/redactar-mensaje/SKILL.md#revisión-de-voz`: un candidato que recibe diez mensajes iguales por semana las reconoce.

**Nunca se inventa un dato del rol para arreglar un defecto.** Si la reescritura necesita algo que no está en el perfil del rol, se marca ❓ y se pregunta.

## El entregable

Escribí, fechado, `busquedas/<cliente-rol>/<AAAA-MM-DD>-prueba-<pieza>.md`:

```
## Personajes
## Simulación
## Defectos y reescrituras
## Versión 2
```

La sección **Versión 2** abre y cierra con la regla número uno escrita: "esto NO valida NADA".

## Lo que este entregable no es

No reemplaza la respuesta de candidatos reales. Lo que pase con ellos (tasa de respuesta, motivos de retiro) lo procesa `aprendizajes`.
