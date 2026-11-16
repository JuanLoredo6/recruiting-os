# Recruiting OS

Un sistema para llevar búsquedas de talento con **Claude Code** y con criterio: el arranque con el hiring manager, un scorecard que se puede evaluar, cada candidato contra ese scorecard, las entrevistas, la terna, las devoluciones y un tablero que dice qué hacer hoy. Todo queda en carpetas de la computadora de la consultora.

Está pensado para **consultoras boutique y recruiters independientes de LATAM** que hacen búsquedas de **Producto** y de **Atención al cliente** (liderazgo y especialistas) en empresas de tecnología. No está calibrado para contratación masiva ni para búsquedas de Tecnología o Diseño.

Es el otro lado de [busqueda-laboral-os](https://github.com/JuanLoredo6/busqueda-laboral-os), el sistema para personas en búsqueda laboral.

## Cómo trabaja

- **La IA prepara, las personas deciden.** Ningún puntaje descarta a nadie. Cada candidato se evalúa contra el scorecard, criterio por criterio, con evidencia: ✅ cumple · 🟡 parcial · ❌ no cumple · ❓ falta saber.
- **Evaluación ciega en lo protegido.** Edad, género, origen, foto, estado civil o salud no entran a ninguna evaluación. Si un cliente pide algo así, el sistema lo marca y propone un requisito basado en conducta.
- **Datos de terceros, en regla.** Cada candidato tiene registrado su consentimiento y la fecha en que se borran sus datos. `/privacidad` revisa lo vencido.
- **Nada se envía solo.** Claude redacta mensajes, avisos, devoluciones y reportes; los manda una persona. No automatiza LinkedIn.
- **Cada candidato recibe una devolución.** El tablero marca las que se atrasan.

---

## Instalación asistida

Necesitás un plan de Claude que incluya Claude Code y la **app de escritorio de Claude** ([claude.com/download](https://claude.com/download)). Para una consultora con más de una persona, recomendamos un plan **Team** o **Enterprise**. No hace falta saber programar.

1. Abrí la app, pestaña **Code**, y elegí tu carpeta **Documentos** como carpeta de trabajo.
2. Pegá este pedido:

```
Instalá el Recruiting OS siguiendo, etapa por etapa, la guía https://raw.githubusercontent.com/JuanLoredo6/recruiting-os/main/INSTALACION.md
```

Si en tu red Claude no puede descargar de GitHub, bajá el [ZIP](https://github.com/JuanLoredo6/recruiting-os/archive/refs/heads/main.zip) con el navegador, dejalo en Documentos y pedí: «Instalá el Recruiting OS desde el ZIP que dejé en Documentos». La guía completa está en **[INSTALACION.md](INSTALACION.md)**.

Al terminar, en la carpeta del sistema, escribí:

```
/empezar
```

### Problemas frecuentes

| Qué pasa | Qué hacer |
|---|---|
| Escribo `/empezar` y no aparece | Claude Code está abierto en otra carpeta. Abrí una sesión nueva **en la carpeta del sistema** (la que tiene `CLAUDE.md` adentro) |
| El tablero dice «Todavía no hay datos» | Corré `/empezar` primero. Si ya lo hiciste, pedile a Claude: «regenerá el tablero» |
| El tablero no se actualiza | Recargá la página (F5). Si sigue igual, pedile a Claude: «corré tablero/sincronizar.sh» |
| `/sincronizar-correo` dice que falta un conector | Tocá el **+** junto al cuadro de mensaje → conectores → Gmail o Google Calendar → Conectar. Después abrí una sesión nueva |
| `/vista-cliente` dice que falta un conector | Lo mismo, con **Google Drive** (y **Google Sheets** si aparece aparte), con la cuenta de la consultora |
| No sé qué hacer ahora | Preguntale a Claude «¿qué hago ahora?» o escribí `/mapa-de-skills` |

---

## Cómo se usa

| Cuándo | Qué le decís a Claude |
|---|---|
| La primera vez | `/empezar` |
| Antes de aceptar una búsqueda | `/mapeo-de-mercado` |
| Antes del arranque con el hiring manager | `/nueva-busqueda` (te arma la guía) |
| Después del arranque, con las notas o la transcripción | `/nueva-busqueda` (perfil del rol y scorecard) |
| Para salir a buscar | `/pitch-del-rol`, `/redactar-aviso`, `/plan-de-sourcing` |
| Cada CV o perfil | `/evaluar-candidato` |
| Antes de una entrevista | `/guia-de-entrevista` |
| Después de una entrevista | `/registrar-entrevista` |
| Cuando pasa algo ("respondió X", "el cliente descartó a Y") | Contáselo, o `/actualizar` |
| Para traer lo que llegó por mail o al calendario | 🔄 SYNC en el tablero, o `/sincronizar-correo` |
| Para escribirle a un candidato o al cliente | `/redactar-mensaje` |
| Cuando hay finalistas | `/armar-terna` |
| Si le compartís el avance al cliente en Google Sheets y Drive | `/vista-cliente` |
| Los viernes | `/reporte-semanal` |
| Cuando una búsqueda se traba | `/diagnostico-proceso` |
| Para ver todo lo que hay | `/mapa-de-skills` |

No hace falta acordarse de los nombres: si le pedís algo con tus palabras, Claude elige el skill que corresponde.

### El tablero

Abrí `tablero/tablero.html` con doble clic y dejalo abierto en una pestaña. Muestra:

- **Hoy:** qué hay que hacer hoy.
- **Para revisar:** lo que trajo la sincronización con Gmail, Calendar y el Sheet del cliente, y necesita una decisión.
- **Alertas:** devoluciones atrasadas, búsquedas sin movimiento o pasadas de fecha, datos de candidatos que ya hay que borrar, cambios que el cliente todavía no ve y búsquedas cerradas que siguen compartidas.
- **Números:** búsquedas abiertas, candidatos activos, devoluciones al día y acciones vencidas.
- **Cartera:** cada búsqueda con su estado y su próximo paso.
- **Pipeline:** los candidatos de la búsqueda elegida, por etapa, con su evaluación contra el scorecard.

Se actualiza solo cada vez que Claude cambia algo. Si movés un candidato o marcás una acción en el tablero, tocá **Copiar pedido para Claude** y pegalo en Claude Code para que quede guardado.

Para verlo con datos de ejemplo antes de cargar los tuyos, tocá **Ver el tablero con datos de ejemplo**.

---

## Qué hay adentro

```
recruiting-os/
├── INSTALACION.md     La guía de instalación asistida
├── CLAUDE.md          Instrucciones para Claude: alcance, reglas, carpetas, modelo de datos
├── contexto/          La consultora: quiénes son, cómo trabajan, su voz y su política de datos
├── clientes/          Una carpeta por cliente
├── busquedas/         busquedas.json (datos del tablero) + una carpeta por búsqueda con sus candidatos
├── investigacion/     Informes fechados: mercado, diagnósticos, métricas, aprendizajes
├── tablero/           tablero.html (abrilo con doble clic)
├── plantillas/        Lo que copian /empezar y /nueva-busqueda
├── pruebas/           Material ficticio para probar el sistema
└── .claude/skills/    Los 22 skills
```

### Los skills

**Día a día**

| Skill | Para qué |
|---|---|
| `empezar` | Puesta en marcha: la consultora, su método, su voz, su política de datos, clientes y búsquedas en curso |
| `nueva-busqueda` | Arranque con el hiring manager: perfil del rol, requisitos puestos a prueba y scorecard |
| `redactar-aviso` | El aviso desde el scorecard, por canal |
| `evaluar-candidato` | Cada perfil contra el scorecard, con evidencia y sin puntajes |
| `actualizar` | Lleva cada novedad al tablero y crea las acciones que siguen |
| `sincronizar-correo` | Trae lo que llegó por Gmail y Calendar, solo lectura |
| `guia-de-entrevista` | Guía de la búsqueda, de cada candidato y para el hiring manager, con criterios de Producto y de Atención al cliente |
| `registrar-entrevista` | Lo que el candidato dijo, separado de la impresión, contra el scorecard |
| `armar-terna` | Compara finalistas y arma la presentación al cliente. Claude nunca elige |
| `redactar-mensaje` | Contacto, follow-up, devolución, mensajes al cliente, con la voz de la consultora |
| `reporte-semanal` | Repaso de la cartera, reporte al cliente y retro de cierre |
| `vista-cliente` | Opcional: la búsqueda compartida con el cliente en un Google Sheet protegido y una carpeta de Drive. El cliente no necesita Claude |

**Estrategia de la búsqueda**

| Skill | Para qué |
|---|---|
| `mapeo-de-mercado` | Cuánto talento hay y qué tan difícil es la búsqueda, con fuentes |
| `pitch-del-rol` | Por qué alguien bueno se cambiaría a este rol |
| `plan-de-sourcing` | A quién buscar por lo que hizo, dónde y cómo |
| `diagnostico-proceso` | Por qué una búsqueda no avanza, y qué medir |
| `aprendizajes` | Patrones de varias búsquedas, con citas literales |

**Criterio y cuidado**

| Skill | Para qué |
|---|---|
| `poner-a-prueba` | Repregunta requisitos, evaluaciones, descartes y decisiones hasta que haya evidencia |
| `candidatos-sinteticos` | Prueba avisos, mensajes y pitch contra candidatos simulados |
| `privacidad` | Consentimientos, borrados y datos sensibles |
| `disenador-visual` | Ternas, reportes y propuestas con diseño |
| `mapa-de-skills` | El índice de todo lo anterior |

---

## Los datos

- Los datos de la consultora, sus clientes y sus candidatos quedan **solo en la computadora** de cada persona. El `.gitignore` evita que se suban a GitHub por error.
- Este repositorio es público y trae **solo el sistema**: skills, plantillas y tablero, sin datos de nadie.
- **Tu copia, en cambio, tiene datos de candidatos: no la subas a un repositorio público.** Tampoco uses un fork público para guardar tus búsquedas. Si querés respaldo, una nube de la empresa o un repositorio **privado**.
- `contexto/privacidad.md` es un punto de partida, no asesoramiento legal: revisalo con quien asesore a la consultora según los países donde trabaja.
- Cada persona del equipo tiene su propia carpeta: la versión actual no comparte las búsquedas entre computadoras.
- **Con la vista del cliente (opcional),** una parte sale de la computadora a propósito: los candidatos que aceptaron ser presentados, con su evaluación y un CV sin datos personales, van a una carpeta de Drive de la consultora compartida con mails puntuales del cliente. Nada se publica ni se comparte sin tu OK, y al cerrar la búsqueda la carpeta va a la papelera. Lo que el cliente descargó mientras tuvo acceso queda fuera del alcance de la consultora.

## Actualizar el sistema

Cuando haya mejoras, pedile a Claude "actualizá el sistema" o corré `git pull`. Tus datos no se tocan: están fuera de lo que se versiona. Qué cambió en cada versión está en [CHANGELOG.md](CHANGELOG.md) y en las [releases](https://github.com/JuanLoredo6/recruiting-os/releases).

## Créditos

- Sistema armado por Juan Rodríguez Loredo. Licencia MIT: ver [LICENSE](LICENSE).
- Varias piezas son adaptaciones de los skills de producto de **Pedro Romero Luna** ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills)) y de **Paweł Huryn** ([pm-skills](https://github.com/phuryn/pm-skills), [product-engineering](https://github.com/phuryn/product-engineering) y [pm-brain](https://github.com/phuryn/pm-brain)), ambos con licencia MIT. Detalle en [CREDITOS.md](CREDITOS.md).
