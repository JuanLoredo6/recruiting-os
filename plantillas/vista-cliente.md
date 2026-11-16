# Vista del cliente · plantilla

> La usa el skill `vista-cliente` para crear el Google Sheet y la carpeta de Drive de una búsqueda.
> Es el formato estándar (`formato: estandar`). Si la consultora ya usa un Sheet propio con su cliente, `empezar` o `vista-cliente` mapean sus columnas y se usa `formato: propio`.
> No se edita: si la consultora quiere otro formato, se copia a `contexto/vista-cliente.md` y se ajusta ahí.

## Carpeta de Drive

```
<Consultora> · <Cliente> · <Rol>/        sin herencia de permisos
├── Seguimiento · <Cliente> · <Rol>      Google Sheet
├── CVs/                                 un Doc o PDF por candidato presentado
└── Terna AAAA-MM-DD · <Cliente> · <Rol> Google Doc, desde terna-<fecha>.md
```

## Pestañas del Sheet

### Resumen (protegida)

| Fila | Contenido |
|---|---|
| Búsqueda | `rol` · nombre del cliente |
| Actualizado | fecha de la última publicación |
| Embudo | conteo por etapa: identificados · contactados · en screening · presentados. Solo números, sin nombres |
| Próximo paso | `proximo` de la búsqueda |
| Lo que necesito de vos | pedidos abiertos al cliente (de `perfil-del-rol.md`, el último reporte o la persona) |
| Cómo usar este Sheet | «En «Candidatos», completá solo las columnas amarillas: Decisión del cliente y Comentario.» |

### Candidatos (protegida salvo las dos columnas del cliente)

Una fila por candidato con `presentadoEl`. Columnas en este orden:

1. **Candidato:** nombre y la inicial del apellido.
2. **Etapa:** en lenguaje del cliente (tabla de abajo).
3. **Presentado el:** `presentadoEl`.
4. **Trayectoria:** dos líneas, sin atributos protegidos.
5. **Una columna por criterio del scorecard**, con el nombre corto del criterio: marca (✅ 🟡 ❌ ❓) y una línea de evidencia con su fuente.
6. **Qué falta validar.**
7. **Condiciones autorizadas:** solo lo que el candidato autorizó compartir (disponibilidad, expectativa, modalidad). Si no autorizó nada, «❓ A confirmar».
8. **CV:** link al archivo de `CVs/`.
9. **Decisión del cliente** (editable, fondo amarillo): desplegable Avanza / No avanza / Quiero hablar.
10. **Comentario del cliente** (editable, fondo amarillo).
11. **id** (oculta y protegida): el id del candidato en `busquedas.json`. Así `vista-cliente` reconoce cada fila al publicar y al leer, aunque cambie el nombre o el orden.

### Historial (protegida)

Fecha y una línea por cada cambio publicado. Nunca se borra una línea, salvo la de un candidato que pidió que lo borren.

## Etapas en lenguaje del cliente

| `etapa` | En el Sheet |
|---|---|
| `terna` | Presentado |
| `entrevista-cliente` | Entrevista con ustedes |
| `oferta` | Oferta |
| `contratado` | Ingresó |
| `descartado` | No sigue (con el motivo en términos del scorecard) |
| `retirado` | Se retiró |

`identificado`, `contactado` y `screening` no aparecen nunca.

## Configuración que no hace el conector (la confirma la persona)

Probado con los conectores de Google el 2026-11-16:

- **Protecciones con editores explícitos.** Se crean con la cuenta de la consultora como único editor. Las dos columnas del cliente quedan libres desde la fila 2 hasta el final de la grilla. Después de cada vez que se comparte, se vuelven a leer: Google suma a cualquier persona con quien se comparte si la lista no es explícita.
- **Carpeta como lector, Sheet como editor.** Los archivos de la carpeta heredan el permiso de lector.
- **«Los editores pueden cambiar permisos y compartir»:** se apaga a mano en el Sheet (Compartir → ⚙️). Sin esto, el cliente puede invitar a otras personas y cambiar el acceso general. Google no permite separar las dos cosas.
- **Descarga del CV:** opcional. A mano, archivo por archivo: Compartir → ⚙️ → «Los lectores pueden ver la opción para descargar, imprimir y copiar». No impide una captura de pantalla.
- **Aviso al cliente:** el conector no garantiza el mail de Google. Claude redacta el mensaje con los links (`redactar-mensaje`) y lo manda la persona.
- **Vencimiento del acceso:** solo con Google Workspace. Con Gmail personal, al cerrar la búsqueda la carpeta va a la papelera.
- **Valores del cliente:** el desplegable frena lo que escribe el cliente, pero no lo que se escribe por API. Al leer, lo que no sea Avanza, No avanza o Quiero hablar va a «Para revisar».
