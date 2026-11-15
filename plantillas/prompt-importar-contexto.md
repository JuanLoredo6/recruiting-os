# Prompt para traer el contexto de la consultora desde otro chat

> Para la consultora que ya habló de sus búsquedas, sus clientes o su método con Claude en el chat, ChatGPT, Gemini u otra IA.
> `/empezar` lo ofrece en el paso 2, antes de crear nada. Copiá el bloque de abajo, pegalo en ese chat
> y pegá la respuesta en Claude Code.
>
> Lo que vuelve no entra solo al sistema: Claude lo muestra por partes y vos confirmás cada una.
> Antes de pegar la respuesta, borrá datos sensibles de candidatos (documentos, fechas de nacimiento, salud, datos bancarios).

```text
Estoy armando un sistema para ordenar las búsquedas de mi consultora y quiero llevarle lo que vos ya sabés
de cómo trabajamos: lo que hablamos en esta conversación, en otras, en tus memorias o en los archivos del proyecto.

Devolveme un único bloque en Markdown con exactamente estas secciones y en este orden. Reglas:

- Solo lo que yo te dije o te mostré. No completes huecos, no mejores redacciones, no infieras.
- Marcá cada línea con [DIJE] si lo dije o mostré yo, o con [INFERIDO] si es una conclusión tuya.
- Los números, fechas, nombres y cargos, copialos tal cual. Si no estás seguro, poné [DUDOSO].
- Si una sección no tiene nada, escribí "Sin datos". No la inventes.
- De los candidatos, solo nombre, rol al que aplican, etapa y la última novedad. Nada de documentos,
  edad, fecha de nacimiento, fotos, salud, estado civil ni datos bancarios.

## 1. La consultora
Nombre, equipo, países, idiomas, qué búsquedas toma y cuáles no.

## 2. Cómo trabajamos
Etapas de una búsqueda con sus tiempos, cómo es una terna, cada cuánto reportamos, garantía, herramientas.

## 3. Cómo tratamos a los candidatos
Plazos de devolución y qué incluye.

## 4. Clientes
Por cada cliente: qué hace, quiénes son los hiring managers, qué valoran y qué rechazaron antes.

## 5. Búsquedas en curso
Por cada búsqueda: cliente, rol, fecha de apertura, en qué estado está, próximo paso.

## 6. Candidatos en curso
Por cada búsqueda: nombre, etapa, fuente y la última novedad con fecha.

## 7. Nuestro tono
Cómo escribimos a candidatos y a clientes, palabras que usamos y que no usamos nunca.
Si tenés textos que escribimos nosotros (no vos), pegá hasta 3 tal cual.

## 8. Decisiones que ya tomamos
Por ejemplo: tipos de búsqueda que dejamos de tomar y por qué. Con fecha si la sabés.

## 9. Lo que todavía no resolvimos
Dudas abiertas o datos que faltaba confirmar.
```
