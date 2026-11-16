# Cambios

Todos los cambios del Recruiting OS, de la versión más nueva a la más vieja. El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y las versiones, [versionado semántico](https://semver.org/lang/es/). Mientras el sistema esté en `0.x`, una versión menor puede cambiar el modelo de datos del tablero: cuando pase, se avisa acá en **Cambia**.

## [Sin publicar]

### Agregado

- **Vista del cliente en Google Sheets y Drive** (opcional), para las consultoras que le muestran el avance a su cliente en un Sheet compartido. El cliente no necesita Claude.
  - Skill `vista-cliente`: crea la carpeta y el Sheet protegido de cada búsqueda, comparte con mails puntuales, publica mostrando antes qué cambia, sube CVs limpios y la terna, lee la decisión del cliente hacia «Para revisar» y cierra el acceso. Trae un plan B sin conectores (`.xlsx` o `.csv`).
  - `plantillas/vista-cliente.md`: carpeta, pestañas, columnas, etapas en lenguaje del cliente y la configuración que el conector no hace.
  - `redactar-mensaje`: el pedido al candidato para presentarlo al cliente y el aviso de la vista del cliente.
  - Tablero: insignia «Compartida con el cliente», link al Sheet, novedades del «Sheet del cliente» y dos alertas (cambios sin publicar, búsqueda cerrada que sigue compartida).
  - `INSTALACION.md`: etapa opcional para conectar Google Drive y Sheets.

### Cambia

- **Modelo de datos del tablero:** la búsqueda suma `vistaCliente` y el candidato, `presentadoEl`, `cvCompartido` y `decisionCliente`. Los tres son opcionales: un `busquedas.json` anterior sigue siendo válido. «Para revisar» y el historial aceptan la fuente `sheets`.
- `armar-terna` pide el OK de cada candidato antes de presentarlo; `actualizar`, `sincronizar-correo`, `reporte-semanal`, `privacidad` y `empezar` conocen la vista del cliente.
- `plantillas/privacidad.md` suma qué se comparte con el cliente, dónde y hasta cuándo.

- `CLAUDE.md` nombra también a Paweł Huryn en los créditos y pide acreditar cualquier material nuevo de terceros.
- `README.md` y `CREDITOS.md` enlazan los tres repositorios de Paweł Huryn; `CREDITOS.md` abre con la licencia del sistema.
- `guia-de-entrevista` acredita en su encabezado el criterio de Producto adaptado de Pedro Romero Luna.
- Los archivos del tablero (`tablero.html`, `ejemplo.js`, `sincronizar.sh`, `validar.py`) declaran la licencia MIT.

## [0.3.2] - 2026-11-15

Licencia y créditos en cada skill.

### Cambia

- Cada `SKILL.md` declara su licencia en el encabezado (`license:`). Los skills adaptados nombran a Pedro Romero Luna, a Paweł Huryn o a los dos, y remiten a su texto de licencia.
- La nota del `LICENSE` raíz también nombra a Paweł Huryn y su licencia, `.claude/skills/LICENSE-phuryn.txt`.

## [0.3.1] - 2026-11-15

Instalación ajustada al repositorio público.

### Cambia

- La instalación ya no depende de pedir el ZIP: el repositorio es público. El ZIP queda solo para redes que bloquean GitHub y se baja con el navegador.
- `README.md` aclara que el repositorio público trae solo el sistema y que la copia con datos nunca va a un repositorio público. Suma el link al changelog y a las releases.

## [0.3.0] - 2026-11-14

Lista para el piloto de instalación con consultoras.

### Agregado

- `README.md`: qué es, para quién, principios, cómo se usa, el tablero y los skills.
- `INSTALACION.md`: instalación asistida por Claude, en etapas y con comprobación en cada una. Funciona con Git o con el ZIP del repositorio.
- `pruebas/`: material ficticio para probar el sistema de punta a punta. Dos arranques con hiring managers y cuatro CVs, con trampas a propósito, notas de una entrevista, el recorrido con lo esperado en cada paso, pedidos para comprobar qué skill se carga y el checklist del piloto.
- `CHANGELOG.md`, tags y notas de versión en GitHub. El repositorio pasa a ser público: se instala sin pedir el ZIP.

### Cambia

- Quien se postula a un aviso entra en la etapa `contactado`, no en `identificado`.
- Una sola regla de devolución: quien se postuló o aceptó una charla siempre recibe una respuesta (`devolucion: pendiente` al descartarlo). Ajustados `actualizar`, `evaluar-candidato` y `redactar-mensaje`.

### Corregido

- Plurales en las métricas del tablero («1 búsqueda abierta», «1 candidato activo»).

## [0.2.0] - 2026-11-14

Sistema completo: 21 skills y sincronización con Gmail y Google Calendar.

### Agregado

- `armar-terna`: compara finalistas contra el scorecard, arma la presentación de la terna y ayuda al cliente a desempatar. Claude nunca elige.
- `redactar-aviso`: aviso a partir del scorecard, sin requisitos inflados ni discriminatorios, con versiones para LinkedIn, portales de LATAM y la web del cliente.
- `pitch-del-rol`: razones verdaderas para cambiarse, pitch de 30 segundos y de 2 minutos, respuestas a las objeciones típicas.
- `plan-de-sourcing`: a quién buscar por lo que hizo, empresas fuente, búsquedas booleanas, referidos y mensajes por canal. No automatiza LinkedIn.
- `mapeo-de-mercado`: tamaño del talento disponible, empresas que lo concentran, dificultad de la búsqueda y rangos salariales, cada número con su fuente.
- `candidatos-sinteticos`: prueba avisos, mensajes, pitch y guías contra candidatos simulados antes de usarlos con personas reales.
- `diagnostico-proceso` (con `metricas.md`): por qué se traba una búsqueda, indicador principal, árbol de palancas y antimétricas.
- `aprendizajes`: patrones de varias búsquedas, cada uno con una cita literal.
- `disenador-visual`: especifica y construye ternas, reportes y propuestas.
- `sincronizar-correo`: trae de Gmail y Calendar las novedades de las búsquedas, solo lectura. Puede correr sola cada 2 horas en horario laboral.
- Tablero: botón 🔄 SYNC y la sección «Para revisar» con lo dudoso de la sincronización.

### Cambia

- Modelo de datos: `busquedas.json` suma el bloque `sync` (última sincronización, ids procesados, `porRevisar`). `validar.py` lo valida. Un JSON sin `sync` se completa con los valores vacíos de `plantillas/busquedas.json`.
- `mapa-de-skills`, `empezar`, `CLAUDE.md` y `CREDITOS.md` actualizados con los skills nuevos.

## [0.1.0] - 2026-11-14

Base del sistema y núcleo para los primeros pilotos (fases 0 y 1).

### Agregado

- `CLAUDE.md` con el alcance (Producto y Atención al cliente en empresas de tecnología), las reglas (sin puntajes que descarten, evaluación ciega en atributos protegidos, datos de terceros con consentimiento y fecha de borrado, nada se envía sin confirmación) y el modelo de datos de `busquedas.json`.
- Plantillas: consultora, voz, privacidad, cliente, perfil del rol con scorecard, evaluación y prompt para importar contexto de otra IA.
- 11 skills: `empezar`, `nueva-busqueda`, `evaluar-candidato`, `actualizar`, `guia-de-entrevista` (con criterio de Producto y de Atención al cliente), `registrar-entrevista`, `redactar-mensaje`, `reporte-semanal`, `poner-a-prueba`, `privacidad` y `mapa-de-skills`.
- Tablero local (`tablero.html`, se abre con doble clic): Hoy, Alertas (devoluciones pendientes, búsquedas quietas, borrados vencidos), cartera y pipeline por búsqueda.
- Hook de Claude Code que valida `busquedas.json` con `validar.py` y regenera `datos.js` después de cada edición.
- Licencia MIT y créditos a los skills de origen.

[Sin publicar]: https://github.com/JuanLoredo6/recruiting-os/compare/v0.3.2...HEAD
[0.3.2]: https://github.com/JuanLoredo6/recruiting-os/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/JuanLoredo6/recruiting-os/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/JuanLoredo6/recruiting-os/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/JuanLoredo6/recruiting-os/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/JuanLoredo6/recruiting-os/releases/tag/v0.1.0
