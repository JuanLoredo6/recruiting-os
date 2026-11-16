---
name: privacidad
description: "Cuida los datos de los candidatos según contexto/privacidad.md: revisa qué venció (perfiles de sourcing sin contacto, búsquedas cerradas hace más del plazo), borra o anonimiza a un candidato cuando lo pide o cuando vence su plazo, registra un consentimiento o el permiso para la base de talento, y busca datos sensibles que no deberían estar en el sistema. Nunca borra sin mostrar antes qué y pedir confirmación. Usala cuando digan '/privacidad', 'qué datos tengo que borrar', 'X pidió que lo borremos', 'borrá a Y', 'Z aceptó quedar en la base', 'revisá si hay datos sensibles', o desde una alerta del tablero."
license: "MIT. Ver LICENSE en la raíz del repo."
---

# privacidad — los datos de los candidatos, en regla

Los candidatos no eligieron estar en esta computadora. Este skill hace que la política de la consultora se cumpla de verdad: lo vencido se borra, lo que se guarda tiene permiso y lo sensible no entra.

Hablá en rioplatense, con voseo, corto.

> ❓ Este skill aplica la política que escribió la consultora en `contexto/privacidad.md`. No es asesoramiento legal: si una situación no está cubierta por la política (un pedido formal de acceso a los datos, una autoridad que pregunta), decilo y recomendá consultarlo con quien asesore a la consultora.

## Modos

| Pedido | Modo |
|---|---|
| `/privacidad`, `/privacidad revisar`, "qué tengo que borrar" | **Revisar** |
| `/privacidad borrar <cliente-rol> <candidato>`, "X pidió que lo borremos" | **Borrar** |
| "X aceptó quedar en la base", "registrá el consentimiento de Y" | **Registrar permiso** |
| "revisá si hay datos sensibles" | **Buscar datos sensibles** |

Leé siempre `contexto/privacidad.md` primero. Si no existe, decí que hay que correr `/empezar` y terminá.

## Revisar

1. En `busquedas/busquedas.json`, listá:
   - **Vencidos:** candidatos con `borrarEl` anterior o igual a hoy.
   - **Por vencer en 7 días.**
   - **Sin fecha de borrado** (no debería pasar: corregilo calculándola con la política).
   - **Sin consentimiento** en etapas que lo suponen (`screening` o más): puede ser un dato que falta cargar.
   - **Compartidos con el cliente** después de lo previsto: búsquedas cerradas con `vistaCliente` sin `revocada`, y candidatos con `cvCompartido` que ya no están en ninguna etapa activa. Proponé `/vista-cliente cerrar`.
2. Mostrá la lista agrupada, con nombre, búsqueda, etapa y fecha. Para cada vencido, la recomendación es borrar; para los que tienen una razón para seguir (por ejemplo, están en una búsqueda abierta), proponé recalcular la fecha y decí por qué.
3. La persona decide cuáles se borran. Aplicá **Borrar** a esos, en un solo paso.

## Borrar

1. Mostrá exactamente qué se va a borrar: la carpeta `busquedas/<cliente-rol>/candidatos/<candidato>/` con su lista de archivos, y las menciones a su nombre en otros archivos del sistema (reportes, notas de la búsqueda, acciones). Buscalas por nombre y por id.
2. Pedí confirmación explícita: **se borra y no se puede recuperar.**
3. Con el sí:
   - Borrá la carpeta del candidato.
   - **Si tiene `cvCompartido`**, su CV de la carpeta del cliente va a la papelera de Drive (con el conector, o a mano si no está), y su fila sale del Sheet con `/vista-cliente publicar`. Avisá que el cliente pudo haberlo descargado mientras tuvo acceso: eso queda fuera del alcance de la consultora. Después, `cvCompartido: null` y `presentadoEl: null`.
   - En `busquedas/busquedas.json`, reemplazá su entrada por una anónima para que los números de la búsqueda sigan cerrando: `id` `anonimo-<n>` (el primer número libre en esa búsqueda), `nombre` vacío, la misma `etapa`, `fuente` y `motivo` (si el motivo nombra a la persona, generalizalo), `evaluacion: null`, `consentimiento: null`, `borrarEl: null`, `historial: []`, `devolucion` como estaba.
   - Borrá o anonimizá sus acciones pendientes (si había una devolución pendiente, avisá antes: quizás conviene mandarla primero).
   - En reportes y notas que lo nombran, reemplazá el nombre por "un candidato" o el id anónimo. No toques `contexto/importado/`: avisá si ahí aparece, para que la persona lo resuelva.
4. Confirmá en dos líneas qué se borró y qué quedó anónimo.

**Si el candidato pidió que lo borren**, se borra en el momento, aunque la búsqueda siga abierta, y se anota en el historial de la búsqueda una línea sin su nombre: "un candidato pidió la baja de sus datos". Ofrecé el mensaje para confirmarle que se hizo (`/redactar-mensaje`).

## Registrar permiso

- **Consentimiento para la búsqueda:** `consentimiento` con la fecha y una línea en el historial con cómo lo dio (se postuló, aceptó la charla, lo dijo por mail).
- **Base de talento:** solo con un permiso explícito del candidato. Línea en el historial ("aceptó quedar en la base de talento, 📌 mail del 2026-11-14") y `borrarEl` recalculado con el plazo de la base.

Nunca registres un permiso que el candidato no dio, aunque "seguro le interesa".

## Buscar datos sensibles

Revisá los archivos que escribe el sistema (`evaluacion.md`, `entrevista-*.md`, `guia-*.md`, `feedback-*.md`, `reporte-*.md`, `notas-*.md`, `cliente.md` y `busquedas.json`) buscando lo que `contexto/privacidad.md` dice que no se guarda nunca: documentos de identidad, fechas de nacimiento, edades, domicilios, datos bancarios, salud, estado civil, hijos, religión, menciones a atributos protegidos. Los CVs originales no se tocan: se informa si traen datos sensibles y que el original queda tal cual llegó.

Mostrá cada hallazgo con archivo y línea, y proponé la corrección. Aplicala solo con confirmación.

## Reglas

- Nunca borres nada sin mostrar antes la lista exacta y recibir un sí.
- Nunca registres un consentimiento que no se dio.
- El JSON tiene que quedar válido. Si el hook devuelve errores, corregilos antes de cerrar.
