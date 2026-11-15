---
name: reporte-semanal
description: "Hace dos cosas con el tablero: el repaso interno de la cartera (qué se hizo, búsquedas trabadas, candidatos sin movimiento, devoluciones atrasadas, borrados vencidos, tres prioridades para la semana) y el reporte para el cliente de una búsqueda (embudo, candidatos en proceso con su evidencia, lo que se aprendió del mercado, lo que se necesita del cliente y el próximo paso), listo para revisar y mandar. Al cerrar una búsqueda arma la retro. Usala cuando digan /reporte-semanal, 'cómo vamos', 'repasemos la semana', 'armá el reporte para el cliente', 'qué le cuento a Carla', 'por qué está trabada esta búsqueda', 'cerramos la búsqueda, hagamos la retro', o los viernes."
---

# reporte-semanal — la cartera en 10 minutos y el cliente al día

Una consultora con varias búsquedas abiertas pierde el hilo sin un momento fijo para mirar el conjunto, y un cliente que no recibe noticias asume que no pasa nada. Este skill resuelve las dos cosas con los datos del tablero.

Hablá en rioplatense, con voseo. Reconocé lo hecho antes de marcar lo que falta.

## Modos

| Pedido | Modo |
|---|---|
| `/reporte-semanal`, "repasemos la semana", "cómo vamos" | **Repaso interno** de toda la cartera |
| `/reporte-semanal <cliente-rol>`, "armá el reporte para <cliente>" | **Reporte al cliente** de una búsqueda |
| `/reporte-semanal <cliente-rol> cierre` | **Retro de cierre** de una búsqueda |

La semana es de lunes a domingo de la fecha de hoy, salvo que la persona diga otra cosa.

## Repaso interno

Leé `busquedas/busquedas.json`, `contexto/consultora.md` (tiempos objetivo y plazo de devolución), `contexto/decisiones.md` y los dos repasos anteriores en `investigacion/*-repaso-semanal.md`, si existen.

### 1. Lo que se hizo

Contá desde el JSON (no lo preguntes): candidatos sumados, contactados, screenings, presentados al cliente, ternas enviadas, ofertas, ingresos, devoluciones enviadas, acciones completadas. Una frase de reconocimiento concreta, sin exagerar.

### 2. Los números por búsqueda

| Búsqueda | Días abierta | Identificados | Contactados | Screening | Con el cliente | Terna | Objetivo de cierre |
|---|---|---|---|---|---|---|---|

Contá cada candidato en la etapa más avanzada a la que llegó (los descartados y retirados cuentan en la etapa en la que salieron, según su historial). Con menos de 10 candidatos en una búsqueda, aclará que las tasas todavía no dicen mucho.

### 3. Lo que se está cayendo

- **Acciones vencidas:** por cada una, hacerla, reprogramarla o descartarla (lo decide la persona).
- **Devoluciones atrasadas:** candidatos con `devolucion: "pendiente"` fuera del plazo de `contexto/consultora.md`. Van primero: es lo que más daña a la consultora.
- **Búsquedas sin movimiento:** abiertas con 7 días o más sin novedad, o pasadas de su `objetivoCierre`.
- **Candidatos quietos:** activos con 7 días o más sin novedad. Proponé el próximo paso.
- **Clientes que no responden:** candidatos en `entrevista-cliente` o `terna` sin feedback del cliente hace más de lo que el cliente se comprometió (`perfil-del-rol.md`, «Proceso del cliente»).
- **Datos:** borrados vencidos (`borrarEl` anterior a hoy) y perfiles de sourcing sin contacto a punto de vencer. Proponé `/privacidad revisar`.
- **Decisiones que piden revisión:** las ⭐ de `contexto/decisiones.md` cuya condición de "Cambio de idea si" ya se cumplió.

Cuando algo deja de sostenerse, citá cada señal por separado, con su fecha y su fuente. No lo resuelvas en el repaso: queda escrito y la persona decide.

### 4. Una lectura (🔍)

Dos o tres líneas: qué está funcionando y qué no. Si hay un patrón (todas las ternas salen de referidos, el cliente rechaza todo en la misma etapa, el aviso no trae a nadie que cumpla los excluyentes), señalalo y sugerí el próximo paso: ajustar el scorecard con el cliente (`/nueva-busqueda <cliente-rol>`, modo ajustar), cambiar el canal de sourcing, o una charla con el hiring manager.

### 5. Tres prioridades para la semana que viene

Proponé tres, concretas y con día, en una ronda con el formato de `.claude/skills/poner-a-prueba/SKILL.md#método`. Las aceptadas se suman como acciones al tablero, con fecha, prioridad alta y su pedido.

**Salida:** `investigacion/<AAAA-MM-DD>-repaso-semanal.md` con las cinco partes. Aplicá en el JSON los cambios decididos. El cierre en el chat son tres líneas: lo mejor de la semana, lo que hay que cuidar y la primera acción del lunes.

## Reporte al cliente

Leé la búsqueda en el JSON, `perfil-del-rol.md`, la evaluación y las entrevistas de cada candidato activo, `clientes/<cliente>/cliente.md` (cómo prefiere que le reporten) y el reporte anterior en la carpeta de la búsqueda, si existe.

El reporte tiene estas partes, cortas:

1. **Dónde estamos:** una línea con el estado y si se llega al objetivo de cierre.
2. **El embudo de la semana:** cuántos perfiles se revisaron, se contactaron, pasaron screening y se presentan. Sin nombres de los que no avanzaron.
3. **Candidatos en proceso:** por cada uno que el cliente ya conoce o que se presenta ahora, tres o cuatro líneas contra el scorecard: lo que cumple, con evidencia, y lo que falta validar. **En el orden de la terna que decidió la consultora, sin puntajes.**
4. **Lo que aprendimos del mercado:** qué dicen los candidatos del rol (rango, modalidad, lo que les atrae o no), con cuántos y sin nombres. Solo lo que está en los historiales y registros.
5. **Lo que necesitamos de ustedes:** feedback pendiente, decisiones, fechas de entrevista. Con fecha.
6. **Próximo paso** con fecha.

Reglas del reporte:

- Nada que el cliente no deba saber según `contexto/consultora.md` (honorarios de otros, otros clientes, el salario actual de un candidato si no autorizó compartirlo).
- Ningún atributo protegido de ningún candidato.
- Si el cliente está demorando el proceso, se dice con el dato ("Martina espera feedback hace 6 días hábiles; tiene otro proceso avanzado"), sin dramatizar.

Pasalo por la revisión de voz de `.claude/skills/redactar-mensaje/SKILL.md#revisión-de-voz` y guardalo en `busquedas/<cliente-rol>/reporte-<AAAA-MM-DD>.md`. Mostralo listo para copiar. **No lo envíes:** cuando la persona confirme que lo mandó, registralo con `actualizar`.

## Retro de cierre

Cuando una búsqueda se cierra (cubierta, por otro, cancelada o desierta):

1. **Los números:** días desde la apertura hasta la terna y hasta el ingreso, candidatos por etapa, de dónde salió quien ingresó, cuántas devoluciones se dieron a tiempo.
2. **Qué funcionó y qué no**, con citas de los registros y del feedback del cliente.
3. **Qué aprendimos de este cliente:** lo que valoró y lo que rechazó, en términos del scorecard. Ofrecé sumarlo a `clientes/<cliente>/cliente.md`, sección «Qué valoran y qué rechazan».
4. **Pendientes de cierre:** devoluciones, fechas de borrado recalculadas, consentimientos para la base de talento.

Guardala en `investigacion/<AAAA-MM-DD>-retro-<cliente-rol>.md`.

## Sugerencia de rutina

Si la consultora quiere que el repaso le llegue solo, explicá que puede crear una tarea programada en Claude Code (por ejemplo, viernes a las 16) que corra `/reporte-semanal` en esta carpeta. No la crees sin que lo pida.

## Reglas

- Los números salen del JSON, nunca se estiman.
- No inventes feedback, motivos ni conclusiones que los registros no traen. Lo que es lectura va con 🔍.
- El JSON tiene que quedar válido. Si el hook devuelve errores, corregilos antes de cerrar.
