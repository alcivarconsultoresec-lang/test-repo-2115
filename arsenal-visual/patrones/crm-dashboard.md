# Patrón: CRM Dashboard / Command Center

## Objetivo

Construir una interfaz de control comercial para prospectos, oportunidades, embudos, propuestas y seguimiento.

Debe sentirse como:

```txt
centro de mando comercial + tablero ejecutivo + fábrica de ventas
```

## Cuándo usarlo

- NØX CRM.
- Sistema personal de prospección.
- Dashboard de oportunidades.
- Panel para seguimiento de demos.
- Herramientas internas de consultoría.

## Módulos mínimos

```txt
Dashboard ejecutivo
Pipeline Kanban
Base de prospectos
Actividad reciente
Matriz de prioridad IA
Generador de WhatsApp
Listado de demos enviadas
Próxima mejor acción
```

## Métricas recomendadas

```txt
Prospectos activos
Prospectos calientes
Valor estimado del pipeline
Demos enviadas
Tasa de respuesta
Citas agendadas
Cierres del mes
Seguimientos vencidos
```

## Vistas principales

### Dashboard

Debe mostrar:

```txt
KPIs
gráficos
radar de urgencia
alertas
acciones recomendadas
```

### Pipeline

Columnas sugeridas:

```txt
Capturado
Diagnóstico
Demo enviada
Propuesta
Negociación
Cierre
Perdido / Dormido
```

### Prospectos

Campos sugeridos:

```txt
Nombre
Rubro
WhatsApp
Fuente
Dolor detectado
Oferta recomendada
Estado
Última interacción
Próxima acción
Valor estimado
```

### Matriz IA

Criterios:

```txt
Dolor visible
Capacidad de pago
Velocidad de respuesta
Urgencia
Facilidad de demo
Probabilidad de cierre
```

## Estética visual

```txt
Fondo oscuro
Glassmorphism
Neones controlados
Cards ejecutivas
Tablas limpias
Gráficos sobrios
Panel lateral
Comando rápido
```

## Componentes recomendados del arsenal

- shadcn/ui: cards, tables, modals, tabs, form.
- Recharts: gráficos.
- kbar: command palette.
- Motion Primitives: transiciones.
- Magic UI: efectos de fondo.
- Lenis: scroll premium.

## Reglas de experiencia

1. Todo debe estar orientado a la siguiente acción comercial.
2. No crear dashboards bonitos pero inútiles.
3. Cada prospecto debe tener un CTA claro.
4. La prioridad debe calcularse o mostrarse visualmente.
5. El usuario debe poder filtrar rápido por caliente, pendiente, vencido y demo enviada.
6. La versión inicial puede ser simulada, pero la estructura debe anticipar datos reales.

## Prompt base para Codex

```txt
Construye un dashboard CRM tipo command center para una fábrica de ventas.
Debe incluir KPIs, pipeline Kanban, tabla de prospectos, actividad reciente, matriz de prioridad IA y botones de acción WhatsApp.
Estética oscura premium, glassmorphism, neón controlado, responsive.
HTML/CSS/JS puro para prototipo o React + Tailwind + shadcn/ui para versión producto.
```

## Evolución técnica recomendada

```txt
Fase 1: HTML/CSS/JS simulado
Fase 2: React + Vite
Fase 3: Supabase o Google Sheets
Fase 4: WhatsApp API / Gmail / Calendar
Fase 5: IA para scoring y generación de mensajes
```
