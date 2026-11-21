# Política de datos de candidatos

> Los candidatos no eligieron estar en esta computadora. Esta política dice qué se guarda, por cuánto tiempo y con qué permiso.
> Claude la aplica en todos los skills. `/privacidad` la revisa y borra lo vencido.
> ❓ Esta plantilla es un punto de partida, no asesoramiento legal: conviene revisarla con quien asesore a la consultora
> según los países donde trabaja (por ejemplo, Ley 25.326 en Argentina, LGPD en Brasil, LFPDPPP en México, Ley 21.719 en Chile).

## Qué guardamos

- El CV o perfil que el candidato compartió, o el perfil público que encontramos por sourcing.
- Notas de entrevistas y la evaluación contra el scorecard.
- Los mensajes que intercambiamos, resumidos en una línea en el historial.

## Qué no guardamos nunca

- Documento de identidad, CUIL, CPF, RG, CURP, RUT o similar, y la carteira de trabalho (CTPS) en Brasil.
- Fecha de nacimiento, edad, foto.
- Datos bancarios, domicilio exacto.
- Salud, discapacidad, religión, orientación sexual, afiliación política o sindical.
- Estado civil, hijos o planes de tenerlos.

Si un CV trae algo de esto, el archivo original queda tal cual llegó, pero nada de eso se copia a otro archivo ni al tablero.

## Consentimiento

- **Perfil identificado por sourcing (sin contacto):** se guarda solo lo público necesario para decidir si contactarlo. Si no hay contacto en **30 días**, se borra.
- **Candidato que se postula, acepta una charla o lo confirma por escrito:** queda registrada la fecha en `consentimiento`.
- **Base de talento (para búsquedas futuras):** solo si el candidato lo acepta de forma explícita. Se anota en su historial.

## Cuánto tiempo

- **Plazo de borrado por defecto:** 12 meses desde el cierre de la búsqueda.
- **Con consentimiento para la base de talento:** 24 meses desde el último contacto.
- **Si el candidato pide que lo borremos:** se borra en el momento, con `/privacidad borrar`.

<!-- Ajustá estos plazos si la consultora decide otros. Claude calcula `borrarEl` con estos números. -->

## Lo que se comparte con el cliente (vista del cliente, opcional)

Si la consultora comparte las búsquedas con el cliente en Google Sheets y Drive (skill `vista-cliente`):

- **Quién entra:** solo candidatos que aceptaron ser presentados a ese cliente. Se anota la fecha en `presentadoEl`. Nada de perfiles de sourcing ni de candidatos en screening.
- **Qué CV:** la versión limpia por defecto (sin documento, fecha de nacimiento, foto, estado civil, hijos, domicilio ni datos de contacto). El original, solo si el candidato lo acepta.
- **Dónde:** en el Drive de la consultora, una carpeta por búsqueda, compartida con mails puntuales del cliente. Nunca con «cualquiera con el link».
- **Hasta cuándo:** con Google Workspace, el acceso vence a los 30 días de la fecha objetivo de cierre (tope: un año). Con Gmail personal no se puede poner vencimiento: al cerrar la búsqueda la carpeta va a la papelera, y Drive la vacía a los 30 días.
- **Lo que no controlamos:** lo que el cliente descarga, imprime o copia mientras tiene acceso. Se le avisa al candidato cuando acepta ser presentado.
- **Al borrar a un candidato:** su CV en Drive va a la papelera y su fila sale del Sheet en la próxima publicación.

<!-- Ajustá el plazo del acceso si la consultora decide otro. -->

## Qué es borrar

Se elimina la carpeta del candidato y en `busquedas.json` queda solo una entrada anónima (`id` del tipo `anonimo-1`, etapa, fuente y motivo), para que las métricas de la búsqueda sigan cerrando. Ningún nombre, link ni texto que lo identifique.
