#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Juan Rodríguez Loredo. Ver LICENSE en la raíz del repo.
# Límites L3, L4, L10 y L14 de CLAUDE.md: nada sale en nombre de la consultora sin confirmación,
# Gmail y Calendar son de solo lectura y lo que se publica en Drive o Sheets lo ve el cliente.
#
# Lo corre un hook PreToolUse de Claude Code (.claude/settings.json) antes de cualquier herramienta
# que envía o modifica mails, etiquetas o eventos, o que crea, escribe, comparte o manda a la papelera
# algo en Google Drive o Sheets. El filtro por nombre de herramienta está en settings.json y no depende
# del ID del conector, así que funciona en cualquier instalación.
#
# No bloquea: le pide a la persona que confirme esa llamada, aunque la sesión esté en modo automático.
# En una corrida sin nadie que confirme (por ejemplo, una tarea programada), la llamada no se hace.
# Adaptado del hook de busqueda-laboral-os.

entrada="$(cat)"
herramienta="$(printf '%s' "$entrada" | sed -n 's/.*"tool_name"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n 1)"
herramienta="${herramienta##*__}"
[ -n "$herramienta" ] || herramienta="una herramienta que envía, publica o modifica"

case "$herramienta" in
  *_file|request_access|*spreadsheet*|*_values|insert_dimension|update_formulas|copy_sheet_*)
    motivo="Límite L14 (CLAUDE.md): $herramienta escribe o comparte algo en Google Drive o Sheets, y eso lo puede ver el cliente. Confirmá solo si revisaste qué cambia y lo pediste para este caso." ;;
  *)
    motivo="Límites L3 y L4 (CLAUDE.md): $herramienta envía o modifica algo en Gmail o Calendar en nombre de la consultora. Confirmá solo si lo pediste vos para este caso." ;;
esac

printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"%s"}}\n' "$motivo"
exit 0
