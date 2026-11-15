---
name: armar-terna
description: "Compara a los finalistas de una búsqueda contra el scorecard, criterio por criterio y con la evidencia de sus evaluaciones y entrevistas, para que la consultora decida quiénes van a la terna sin depender de la intuición, y arma la presentación de la terna al cliente (por candidato: trayectoria, evidencia por criterio, lo que falta validar, condiciones y riesgos). También ayuda al cliente a decidir entre dos finalistas. Claude nunca elige: muestra en qué se diferencian. Usala cuando digan 'armá la terna', 'quiénes presento', 'compará a X y a Y', 'el cliente no puede decidir entre dos', 'prepará la presentación de los finalistas', o desde una acción del tablero."
license: "MIT. Ver LICENSE en la raíz del repo."
---

# armar-terna — decidir con el scorecard a la vista

Al final de una búsqueda, la decisión suele tomarse con lo que se recuerda de la última entrevista. Este skill pone a todos los finalistas contra los mismos criterios, con la misma evidencia, para que la decisión de la consultora y la del cliente se puedan explicar.

Hablá en rioplatense, con voseo. Corto y concreto.

## Regla número uno

**Claude no elige.** Ni la terna ni el ganador. Muestra en qué criterios se diferencian los candidatos y con qué evidencia. Si le piden "¿a quién presentarías?", devuelve el empate sin romperlo y dice qué falta saber para desempatar.

## Modos

| Pedido | Modo |
|---|---|
| `/armar-terna <cliente-rol>`, "quiénes presento" | **Comparar** a los candidatos en `screening` o más |
| "Armá la presentación", después de que la consultora eligió | **Presentar** la terna al cliente |
| "El cliente duda entre X e Y" | **Desempatar** entre dos finalistas |

## Antes de empezar

Leé `perfil-del-rol.md` (scorecard y proceso del cliente: cuántos quiere en la terna), `clientes/<cliente>/cliente.md` (qué valoró y qué rechazó antes) y, por cada candidato, su `evaluacion.md`, sus registros de entrevista y su historial en `busquedas/busquedas.json`.

Si a un candidato le falta registrar una entrevista, decilo antes de comparar: una comparación con un candidato a medio registrar favorece al que se recuerda mejor. Ofrecé `/registrar-entrevista` primero.

## Comparar

1. **La tabla**, criterio por criterio, una columna por candidato, **en el orden en que llegaron a la búsqueda**:

| # | Criterio | Tipo | Martina | Joaquín | Sofía |
|---|---|---|---|---|---|
| 1 | Llevó un producto con métricas propias | Excluyente | ✅ 📌 entrevista 11/11, min 8 | ✅ 📌 CV | 🟡 📌 entrevista 12/11 |

   Cada celda con su estado y la fuente más fuerte (conducta en entrevista > dato del CV > afirmación).

2. **Dónde se diferencian:** solo los criterios donde los estados no son iguales, con la evidencia lado a lado. Lo que es igual para todos no ayuda a decidir.
3. **Lo que falta para decidir:** los ❓ que quedan en criterios excluyentes y quién los puede cerrar (la consultora en una llamada, el cliente en su entrevista, una referencia).
4. **Riesgos de cada uno**, con su fuente: otros procesos en curso, expectativa salarial fuera del rango, disponibilidad, una señal de la entrevista. Ningún atributo protegido.
5. **Revisión de sesgos**, en una línea por cada uno que aparezca: un candidato que "se recuerda mejor" porque fue el último, uno que se parece al hiring manager, uno con menos evidencia porque se lo entrevistó menos.

Después preguntá: ¿quiénes van a la terna? La decisión es de la consultora. Si quieren poner a prueba la decisión, `poner-a-prueba` sobre el motivo de cada uno que queda afuera.

## Presentar

Con la terna elegida, armá `busquedas/<cliente-rol>/terna-<AAAA-MM-DD>.md`:

1. **Resumen de la búsqueda:** cuántos perfiles se revisaron, se contactaron y se entrevistaron, en una línea. Sin nombres de los que no avanzaron.
2. **Por candidato**, en el orden que decidió la consultora:
   - Trayectoria en tres líneas.
   - Contra el scorecard: lo que cumple, con la evidencia más fuerte.
   - Lo que falta validar y quién lo valida (casi siempre, el cliente en su entrevista).
   - Condiciones que el candidato autorizó compartir: disponibilidad, expectativa, modalidad.
   - Por qué lo presenta la consultora, en una frase.
3. **Lo que les recomendamos preguntar** en sus entrevistas, atado a los ❓ de cada uno. Ofrecé la guía para el hiring manager (`/guia-de-entrevista <cliente-rol> hiring-manager`).
4. **Próximos pasos con fecha:** cuándo quieren entrevistar y cuándo esperan dar feedback.

Reglas de la presentación:

- **Sin puntajes ni rankings numéricos.** El orden es el de la consultora y se puede explicar.
- Nada que el candidato no autorizó compartir (salario actual, otros procesos con nombre).
- Ningún atributo protegido, ni foto.
- Pasala por `.claude/skills/redactar-mensaje/SKILL.md#revisión-de-voz`.

Si quieren una versión con diseño (PDF o presentación), ofrecé `/disenador-visual`.

Después, en `busquedas/busquedas.json`: los candidatos de la terna pasan a `terna`, la búsqueda a `terna`, historial y una acción "Pedir a <hiring manager> fechas para las entrevistas" con pedido `/redactar-mensaje cliente <cliente-rol>`. Los que no entraron siguen activos hasta que la consultora decida; si se descartan, va con `actualizar` (motivo y devolución pendiente).

## Desempatar

Cuando el cliente duda entre dos:

1. La tabla de comparar, solo con esos dos y solo los criterios donde se diferencian.
2. **La pregunta que desempata:** qué criterio le pesa más al cliente para este rol hoy, a la luz de lo que tiene que lograr a 90 días (`perfil-del-rol.md`). Recomendá hacer esa pregunta, no responderla.
3. Lo que se puede averiguar antes de decidir: una referencia, una segunda charla corta enfocada en el criterio que desempata, un caso.

Guardalo en `busquedas/<cliente-rol>/desempate-<AAAA-MM-DD>.md` y ofrecé el mensaje al cliente.

## Cierre

Ejemplo ilustrativo, con datos ficticios:

```text
Comparé a 4 candidatos en screening o más. Se diferencian en 2 criterios:
- Criterio 2 (excluyente, priorizar ante negocio): Martina ✅ con caso concreto; Sofía ❓, no se le preguntó.
- Criterio 3 (deseable, pagos): Joaquín ✅; Martina 🟡.
Falta: registrar la entrevista de Tomás antes de comparar.
¿Quiénes van a la terna?
```

## Reglas

- Claude no elige ni ordena por conteo.
- Cada estado sale de la evaluación o de un registro, con su fuente. Lo que no está, es ❓.
- El JSON tiene que quedar válido. Si el hook devuelve errores, corregilos antes de cerrar.
