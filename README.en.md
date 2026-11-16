# Recruiting OS

**English** · [Español](README.md)

A system to run talent searches with **Claude Code**, with judgment: the kickoff with the hiring manager, a scorecard you can actually evaluate against, every candidate assessed against that scorecard, interviews, the shortlist, feedback to every candidate, and a dashboard that tells you what to do today. Everything stays in folders on the recruiter's own computer.

It is built for **boutique recruiting firms and independent recruiters in Latin America** who run **Product** and **Customer Support / CX** searches (leadership and specialist roles) at tech companies. It is not calibrated for high-volume hiring, or for Engineering or Design searches.

It is the other side of [busqueda-laboral-os](https://github.com/JuanLoredo6/busqueda-laboral-os), the system for people looking for a job.

> **Language:** the system works in Spanish (Rioplatense). Commands, skills, templates and the dashboard are in Spanish. This page explains what it does for English-speaking readers.

## How it works

- **AI prepares, people decide.** No score ever rules anyone out. Each candidate is assessed against the scorecard, criterion by criterion, with evidence: ✅ meets · 🟡 partial · ❌ doesn't meet · ❓ unknown.
- **Blind on protected attributes.** Age, gender, origin, photo, marital status or health never enter an evaluation. If a client asks for something like that, the system flags it and proposes a behavior-based requirement instead.
- **Third-party data, handled properly.** Every candidate has their consent recorded and the date their data will be deleted. `/privacidad` reviews what has expired.
- **Nothing is sent automatically.** Claude drafts messages, job posts, feedback and reports; a person sends them. It does not automate LinkedIn.
- **Every candidate gets feedback.** The dashboard flags the ones running late.

---

## Guided installation

You need a Claude plan that includes Claude Code, and the **Claude desktop app** ([claude.com/download](https://claude.com/download)). For a firm with more than one person, a **Team** or **Enterprise** plan is recommended. No coding required.

1. Open the app, go to the **Code** tab, and choose your **Documents** folder as the working folder.
2. Paste this request:

```
Instalá el Recruiting OS siguiendo, etapa por etapa, la guía https://raw.githubusercontent.com/JuanLoredo6/recruiting-os/main/INSTALACION.md
```

If Claude can't download from GitHub on your network, download the [ZIP](https://github.com/JuanLoredo6/recruiting-os/archive/refs/heads/main.zip) with your browser, leave it in Documents and ask: «Instalá el Recruiting OS desde el ZIP que dejé en Documentos». The full guide is in **[INSTALACION.md](INSTALACION.md)** (Spanish).

When it's done, in the system's folder, type:

```
/empezar
```

### Common issues

| What happens | What to do |
|---|---|
| I type `/empezar` and nothing shows up | Claude Code is open in a different folder. Start a new session **in the system's folder** (the one with `CLAUDE.md` inside) |
| The dashboard says «Todavía no hay datos» (no data yet) | Run `/empezar` first. If you already did, ask Claude: «regenerá el tablero» |
| The dashboard doesn't update | Reload the page (F5). If it stays the same, ask Claude: «corré tablero/sincronizar.sh» |
| `/sincronizar-correo` says a connector is missing | Click the **+** next to the message box → connectors → Gmail or Google Calendar → Connect. Then start a new session |
| `/vista-cliente` says a connector is missing | Same, with **Google Drive** (and **Google Sheets** if listed separately), using the firm's account |
| I don't know what to do next | Ask Claude «¿qué hago ahora?» or type `/mapa-de-skills` |

---

## How to use it

| When | What you tell Claude |
|---|---|
| The first time | `/empezar` |
| Before accepting a search | `/mapeo-de-mercado` |
| Before the kickoff with the hiring manager | `/nueva-busqueda` (prepares the guide) |
| After the kickoff, with the notes or transcript | `/nueva-busqueda` (role profile and scorecard) |
| To start sourcing | `/pitch-del-rol`, `/redactar-aviso`, `/plan-de-sourcing` |
| Each CV or profile | `/evaluar-candidato` |
| Before an interview | `/guia-de-entrevista` |
| After an interview | `/registrar-entrevista` |
| When something happens ("X replied", "the client passed on Y") | Just tell it, or `/actualizar` |
| To bring in what arrived by email or on the calendar | 🔄 SYNC on the dashboard, or `/sincronizar-correo` |
| To write to a candidate or the client | `/redactar-mensaje` |
| When there are finalists | `/armar-terna` |
| If you share progress with the client in Google Sheets and Drive | `/vista-cliente` |
| On Fridays | `/reporte-semanal` |
| When a search gets stuck | `/diagnostico-proceso` |
| To see everything available | `/mapa-de-skills` |

You don't need to remember the names: if you ask in your own words, Claude picks the right skill.

### The dashboard

Open `tablero/tablero.html` with a double click and keep it open in a tab. It shows:

- **Today:** what needs to be done today.
- **To review:** what the sync brought in from Gmail, Calendar and the client's Sheet that needs a decision.
- **Alerts:** late feedback, searches with no movement or past their date, candidate data that is due for deletion, changes the client can't see yet, and closed searches still being shared.
- **Numbers:** open searches, active candidates, feedback on time, and overdue actions.
- **Portfolio:** every search with its status and next step.
- **Pipeline:** the candidates of the selected search, by stage, with their evaluation against the scorecard.

It updates by itself every time Claude changes something. If you move a candidate or check off an action on the dashboard, click **Copiar pedido para Claude** (copy request for Claude) and paste it into Claude Code so it gets saved.

To see it with sample data before loading your own, click **Ver el tablero con datos de ejemplo** (see the dashboard with sample data).

---

## What's inside

```
recruiting-os/
├── INSTALACION.md     The guided installation guide
├── CLAUDE.md          Instructions for Claude: scope, rules, folders, data model
├── contexto/          The firm: who they are, how they work, their voice and their data policy
├── clientes/          One folder per client
├── busquedas/         busquedas.json (dashboard data) + one folder per search with its candidates
├── investigacion/     Dated reports: market, diagnoses, metrics, learnings
├── tablero/           tablero.html (open it with a double click)
├── plantillas/        What /empezar and /nueva-busqueda copy
├── pruebas/           Fictional material to try the system
└── .claude/skills/    The 22 skills
```

### The skills

**Day to day**

| Skill | What it's for |
|---|---|
| `empezar` | Setup: the firm, its method, its voice, its data policy, clients and searches in progress |
| `nueva-busqueda` | Kickoff with the hiring manager: role profile, requirements put to the test, and scorecard |
| `redactar-aviso` | The job post, built from the scorecard, per channel |
| `evaluar-candidato` | Each profile against the scorecard, with evidence and no scores |
| `actualizar` | Takes every update to the dashboard and creates the next actions |
| `sincronizar-correo` | Brings in what arrived by Gmail and Calendar, read-only |
| `guia-de-entrevista` | Interview guide for the search, for each candidate and for the hiring manager, with Product and Customer Support criteria |
| `registrar-entrevista` | What the candidate said, kept apart from impressions, against the scorecard |
| `armar-terna` | Compares finalists and builds the shortlist presentation for the client. Claude never picks |
| `redactar-mensaje` | Outreach, follow-ups, feedback and client messages, in the firm's voice |
| `reporte-semanal` | Portfolio review, client report and closing retro |
| `vista-cliente` | Optional: the search shared with the client in a protected Google Sheet and a Drive folder. The client doesn't need Claude |

**Search strategy**

| Skill | What it's for |
|---|---|
| `mapeo-de-mercado` | How much talent there is and how hard the search is, with sources |
| `pitch-del-rol` | Why someone good would move to this role |
| `plan-de-sourcing` | Who to look for based on what they've done, where and how |
| `diagnostico-proceso` | Why a search isn't moving, and what to measure |
| `aprendizajes` | Patterns across several searches, with literal quotes |

**Judgment and care**

| Skill | What it's for |
|---|---|
| `poner-a-prueba` | Pushes back on requirements, evaluations, rejections and decisions until there is evidence |
| `candidatos-sinteticos` | Tests job posts, messages and the pitch against simulated candidates |
| `privacidad` | Consent, deletions and sensitive data |
| `disenador-visual` | Shortlists, reports and proposals with proper design |
| `mapa-de-skills` | The index of everything above |

---

## The data

- The firm's, its clients' and its candidates' data stay **only on each person's computer**. The `.gitignore` prevents them from being pushed to GitHub by mistake.
- This repository is public and contains **only the system**: skills, templates and the dashboard, with nobody's data.
- **Your copy, on the other hand, holds candidate data: don't push it to a public repository.** Don't use a public fork to store your searches either. If you want a backup, use a company cloud or a **private** repository.
- `contexto/privacidad.md` is a starting point, not legal advice: review it with whoever advises the firm in the countries where it operates.
- Each team member has their own folder: the current version doesn't share searches across computers.
- **With the client view (optional),** part of the data leaves the computer on purpose: candidates who agreed to be presented, with their evaluation and a CV without personal data, go to a Drive folder owned by the firm and shared with specific client emails. Nothing is published or shared without your OK, and when the search closes the folder goes to the trash. Whatever the client downloaded while they had access is outside the firm's control.

## Updating the system

When there are improvements, ask Claude «actualizá el sistema» or run `git pull`. Your data is not touched: it lives outside what is versioned. What changed in each version is in [CHANGELOG.md](CHANGELOG.md) and in the [releases](https://github.com/JuanLoredo6/recruiting-os/releases).

## Credits

- System built by Juan Rodríguez Loredo. MIT License: see [LICENSE](LICENSE).
- Several pieces are adaptations of the product skills by **Pedro Romero Luna** ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills)) and **Paweł Huryn** ([pm-skills](https://github.com/phuryn/pm-skills), [product-engineering](https://github.com/phuryn/product-engineering) and [pm-brain](https://github.com/phuryn/pm-brain)), both under the MIT License. Details in [CREDITOS.md](CREDITOS.md).
