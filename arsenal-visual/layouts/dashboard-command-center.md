# Layout: Dashboard Command Center

## Cuándo usarlo

- CRM.
- Embudos.
- Ferias con panel de gestión.
- Reportes comerciales.
- Herramientas internas.

## Estructura visual

```txt
[Topbar / identidad / estado]
[KPI strip]
[Panel principal + panel lateral]
[Tabla / board / cards]
[Acciones recomendadas]
[CTA persistente]
```

## Componentes

- Topbar con nombre del sistema.
- Estado del día.
- Cards KPI.
- Filtros.
- Panel de prioridad.
- Tabla o grid.
- CTA principal.

## Reglas UX

- Los datos importantes deben estar arriba.
- Cada métrica debe tener una acción asociada.
- No saturar con más de 5 colores.
- Mantener contraste alto.
- En móvil, convertir paneles a cards apiladas.

## Snippet conceptual

```html
<section class="command-center">
  <header class="topbar"></header>
  <div class="kpi-grid"></div>
  <main class="workbench">
    <section class="primary-panel"></section>
    <aside class="action-panel"></aside>
  </main>
</section>
```

## Checklist

- Se entiende qué está pasando.
- Se entiende qué hacer ahora.
- Hay filtros o segmentación.
- Mobile no se rompe.
- Parece software, no folleto.