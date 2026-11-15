// Recruiting OS · Licencia MIT (ver LICENSE en la raíz del repo).
// Datos de ejemplo de una consultora ficticia, para mostrar el tablero en demos e implementaciones.
// Todas las empresas y personas son inventadas. Las fechas se calculan desde hoy para que el ejemplo nunca quede viejo.
// Se ven abriendo tablero.html?ejemplo (o con el botón "Ver el tablero con datos de ejemplo").
window.DATOS_EJEMPLO = function () {
  function d(n) {
    var x = new Date();
    x.setDate(x.getDate() + n);
    return x.getFullYear() + "-" + String(x.getMonth() + 1).padStart(2, "0") + "-" + String(x.getDate()).padStart(2, "0");
  }
  var borrar = d(365);
  return {
    version: 1,
    consultora: "Puente Talento (ejemplo)",
    actualizado: d(0) + "T09:30",
    clientes: [
      { id: "nimbo", nombre: "Nimbo Pagos", contacto: "Carla Ruiz (Head of Product)" },
      { id: "tienda-sur", nombre: "Tienda Sur", contacto: "Diego Paz (Gerente de CX)" },
      { id: "rumbo", nombre: "Rumbo Logística", contacto: "Ana Sosa (People)" }
    ],
    busquedas: [
      {
        id: "nimbo-product-manager-sr", cliente: "nimbo", rol: "Product Manager Sr · Pagos · remoto LATAM", area: "producto",
        hiringManager: "Carla Ruiz (Head of Product)", estado: "abierta", resultado: null,
        abierta: d(-18), objetivoCierre: d(12), proximo: "Presentar la terna el " + d(2), ultimaNovedad: d(-1),
        historial: [{ fecha: d(-18), texto: "Arranque con Carla: scorecard de 6 criterios" }],
        candidatos: [
          { id: "martina-l", nombre: "Martina López", fuente: "Referido", etapa: "terna", motivo: null,
            evaluacion: { cumple: 5, parcial: 1, noCumple: 0, falta: 0 }, ultimaNovedad: d(-1), devolucion: "no-aplica",
            consentimiento: d(-14), borrarEl: borrar,
            historial: [{ fecha: d(-14), texto: "Screening: lideró el rediseño del checkout" }, { fecha: d(-1), texto: "Entrevista con Carla: avanza" }] },
          { id: "joaquin-r", nombre: "Joaquín Ríos", fuente: "LinkedIn", etapa: "entrevista-cliente", motivo: null,
            evaluacion: { cumple: 4, parcial: 1, noCumple: 0, falta: 1 }, ultimaNovedad: d(-3), devolucion: "no-aplica",
            consentimiento: d(-12), borrarEl: borrar,
            historial: [{ fecha: d(-3), texto: "Entrevista con Carla agendada para el " + d(1) }] },
          { id: "sofia-m", nombre: "Sofía Méndez", fuente: "Aviso", etapa: "screening", motivo: null,
            evaluacion: { cumple: 3, parcial: 1, noCumple: 0, falta: 2 }, ultimaNovedad: d(-2), devolucion: "no-aplica",
            consentimiento: d(-5), borrarEl: borrar, historial: [] },
          { id: "tomas-b", nombre: "Tomás Benítez", fuente: "LinkedIn", etapa: "contactado", motivo: null,
            evaluacion: null, ultimaNovedad: d(-4), devolucion: "no-aplica", consentimiento: null, borrarEl: d(26), historial: [] },
          { id: "valentina-c", nombre: "Valentina Correa", fuente: "LinkedIn", etapa: "identificado", motivo: null,
            evaluacion: { cumple: 3, parcial: 0, noCumple: 0, falta: 3 }, ultimaNovedad: d(-1), devolucion: "no-aplica",
            consentimiento: null, borrarEl: d(29), historial: [] },
          { id: "lucas-f", nombre: "Lucas Fernández", fuente: "Aviso", etapa: "descartado",
            motivo: "No cumple el criterio 1: nunca tuvo a cargo un producto con métricas propias",
            evaluacion: { cumple: 2, parcial: 1, noCumple: 1, falta: 2 }, ultimaNovedad: d(-7), devolucion: "pendiente",
            consentimiento: d(-10), borrarEl: borrar,
            historial: [{ fecha: d(-7), texto: "Screening: descartado por el criterio 1" }] }
        ]
      },
      {
        id: "tienda-sur-team-lead-soporte", cliente: "tienda-sur", rol: "Team Lead de Soporte · híbrido CABA", area: "atencion",
        hiringManager: "Diego Paz (Gerente de CX)", estado: "abierta", resultado: null,
        abierta: d(-25), objetivoCierre: d(-2), proximo: "Ajustar el scorecard con Diego: pidió experiencia en WFM", ultimaNovedad: d(-9),
        historial: [{ fecha: d(-25), texto: "Arranque con Diego" }],
        candidatos: [
          { id: "paula-g", nombre: "Paula Giménez", fuente: "Base propia", etapa: "entrevista-cliente", motivo: null,
            evaluacion: { cumple: 4, parcial: 2, noCumple: 0, falta: 0 }, ultimaNovedad: d(-9), devolucion: "no-aplica",
            consentimiento: d(-20), borrarEl: borrar, historial: [] },
          { id: "martin-a", nombre: "Martín Álvarez", fuente: "Referido", etapa: "screening", motivo: null,
            evaluacion: { cumple: 3, parcial: 2, noCumple: 0, falta: 1 }, ultimaNovedad: d(-10), devolucion: "no-aplica",
            consentimiento: d(-15), borrarEl: borrar, historial: [] },
          { id: "carolina-v", nombre: "Carolina Vega", fuente: "Aviso", etapa: "retirado", motivo: "Aceptó otra oferta",
            evaluacion: { cumple: 4, parcial: 1, noCumple: 0, falta: 1 }, ultimaNovedad: d(-12), devolucion: "no-aplica",
            consentimiento: d(-21), borrarEl: borrar, historial: [] }
        ]
      },
      {
        id: "rumbo-head-of-cx", cliente: "rumbo", rol: "Head of Customer Experience · remoto", area: "atencion",
        hiringManager: "Ana Sosa (People)", estado: "arranque", resultado: null,
        abierta: d(-1), objetivoCierre: null, proximo: "Arranque con el CEO el " + d(1), ultimaNovedad: d(-1),
        historial: [], candidatos: []
      },
      {
        id: "nimbo-product-owner", cliente: "nimbo", rol: "Product Owner · Onboarding", area: "producto",
        hiringManager: "Carla Ruiz (Head of Product)", estado: "cerrada", resultado: "cubierta",
        abierta: d(-90), objetivoCierre: d(-50), proximo: "", ultimaNovedad: d(-48),
        historial: [{ fecha: d(-48), texto: "Ingresó Federico" }],
        candidatos: [
          { id: "federico-n", nombre: "Federico Núñez", fuente: "LinkedIn", etapa: "contratado", motivo: null,
            evaluacion: { cumple: 5, parcial: 1, noCumple: 0, falta: 0 }, ultimaNovedad: d(-48), devolucion: "no-aplica",
            consentimiento: d(-80), borrarEl: d(317), historial: [] },
          { id: "anonimo-1", nombre: "", fuente: "Aviso", etapa: "descartado", motivo: "No cumple el criterio 2",
            evaluacion: null, ultimaNovedad: d(-60), devolucion: "enviada", consentimiento: null, borrarEl: null, historial: [] }
        ]
      }
    ],
    acciones: [
      { id: "a-1", texto: "Mandar devolución a Lucas", busqueda: "nimbo-product-manager-sr", candidato: "lucas-f", fecha: d(-2), prioridad: "alta", hecha: false, hechaEl: null, pedido: "/redactar-mensaje devolucion nimbo-product-manager-sr lucas-f" },
      { id: "a-2", texto: "Preparar la guía para la entrevista de Joaquín con Carla", busqueda: "nimbo-product-manager-sr", candidato: "joaquin-r", fecha: d(0), prioridad: "alta", hecha: false, hechaEl: null, pedido: "/guia-de-entrevista nimbo-product-manager-sr joaquin-r" },
      { id: "a-3", texto: "Follow-up a Tomás", busqueda: "nimbo-product-manager-sr", candidato: "tomas-b", fecha: d(1), condicion: "solo si no respondió", prioridad: "media", hecha: false, hechaEl: null, pedido: "/redactar-mensaje follow-up nimbo-product-manager-sr tomas-b" },
      { id: "a-4", texto: "Preparar el arranque con el CEO de Rumbo", busqueda: "rumbo-head-of-cx", candidato: null, fecha: d(1), prioridad: "media", hecha: false, hechaEl: null, pedido: "/nueva-busqueda rumbo-head-of-cx" },
      { id: "a-5", texto: "Reporte de la semana para Diego", busqueda: "tienda-sur-team-lead-soporte", candidato: null, fecha: d(3), prioridad: "media", hecha: false, hechaEl: null, pedido: "/reporte-semanal tienda-sur-team-lead-soporte" },
      { id: "a-6", texto: "Evaluar a Sofía contra el scorecard", busqueda: "nimbo-product-manager-sr", candidato: "sofia-m", fecha: d(-5), prioridad: "media", hecha: true, hechaEl: d(-5), pedido: "/evaluar-candidato nimbo-product-manager-sr sofia-m" }
    ],
    sync: {
      ultima: (function () { var x = new Date(Date.now() - 40 * 60000); return d(0) + "T" + String(x.getHours()).padStart(2, "0") + ":" + String(x.getMinutes()).padStart(2, "0"); })(),
      ultimoIntento: null, programada: true, horario: "cada 2 h, de 8 a 20, lunes a viernes", error: null, procesados: [],
      porRevisar: [
        { id: "r1", fecha: d(0), fuente: "gmail", ref: "ejemplo-1", resumen: "Carla mandó su feedback de la entrevista con Joaquín: «sólido en pagos, me quedan dudas de cómo prioriza».", busqueda: "nimbo-product-manager-sr", candidato: "joaquin-r", propuesta: "Registrarlo con /registrar-entrevista: toca el criterio 2.", alerta: false },
        { id: "r2", fecha: d(0), fuente: "gmail", ref: "ejemplo-2", resumen: "Paula Giménez pide que borren sus datos de la base.", busqueda: "tienda-sur-team-lead-soporte", candidato: "paula-g", propuesta: "Borrar hoy con /privacidad borrar y confirmarle por mail.", alerta: true }
      ]
    }
  };
};
