# Componente: KPI Cards

## Objetivo

Mostrar métricas clave de forma visual, rápida y accionable.

## Cuándo usarlo

- CRM.
- Dashboards.
- Ferias.
- Hoteles.
- Campañas comerciales.
- Catálogos con métricas.

## Estructura de card

- Etiqueta.
- Valor principal.
- Variación o estado.
- Icono.
- Microtexto de acción.

## Ejemplos

- Prospectos activos.
- Reuniones agendadas.
- Emprendedores inscritos.
- Rubros disponibles.
- Cotizaciones pendientes.
- Ventas estimadas.

## Reglas UX

- Máximo 4 a 6 KPI arriba del fold.
- Usar color solo para estado o prioridad.
- Incluir acción sugerida si aplica.
- En móvil, usar grid de 2 columnas o cards apiladas.

## Snippet conceptual

```html
<article class="kpi-card">
  <span class="kpi-label">Prospectos activos</span>
  <strong class="kpi-value">24</strong>
  <small class="kpi-status positive">+6 esta semana</small>
</article>
```

## Checklist

- Métrica entendible.
- Color con sentido.
- No saturar.
- Valor y acción claros.
