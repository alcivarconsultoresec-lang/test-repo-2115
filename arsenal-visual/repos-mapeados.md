# Arsenal Visual Lefer — Repositorios públicos mapeados

Fecha de creación: 2026-05-05

Objetivo: construir una biblioteca de patrones visuales, componentes, efectos y referencias para mejorar páginas profesionales, landings, catálogos, dashboards, CRM y demos comerciales.

## Regla de uso

No copiar páginas completas. Usar estos repositorios como:

- inspiración visual,
- referencia de arquitectura,
- fuente de componentes reutilizables cuando la licencia lo permita,
- guía para crear componentes propios,
- base para prompts de Codex, v0, Stitch o Canva.

Antes de reutilizar código, revisar siempre licencia, atribución requerida, compatibilidad técnica y si el componente encaja con el cliente.

---

## Tier 1 — Base profesional para productos web

### 1. shadcn/ui

URL: https://github.com/shadcn-ui/ui

Uso recomendado:

- dashboards,
- formularios,
- tablas,
- modales,
- navegación,
- componentes base para SaaS,
- CRM personal,
- cotizadores y paneles de gestión.

Aplicación directa:

- NØX CRM Command Center,
- Club Montt cotizador,
- futuros sistemas de inventario,
- dashboards comerciales.

Nota: excelente para migrar de HTML puro a React + Tailwind + Vite/Next.js.

### 2. Magic UI

URL: https://github.com/magicuidesign/magicui

Uso recomendado:

- efectos hero,
- beams,
- fondos animados,
- textos destacados,
- efectos premium copy-paste,
- secciones de impacto visual.

Aplicación directa:

- landing de cuarzos,
- Club Montt,
- portfolio Alcívar Consultores,
- demos premium para clientes calientes.

### 3. React Bits

URL: https://github.com/DavidHDev/react-bits

Uso recomendado:

- animaciones de texto,
- fondos interactivos,
- componentes visuales memorables,
- efectos para landings modernas,
- interacción visual diferenciadora.

Aplicación directa:

- páginas que deben impresionar al abrir,
- landing boutique de cuarzos,
- portfolio de casos,
- demos con alto impacto emocional.

### 4. Motion Primitives

URL: https://github.com/ibelick/motion-primitives

Uso recomendado:

- microinteracciones,
- transiciones,
- tabs animados,
- acordeones premium,
- cards con movimiento elegante.

Aplicación directa:

- páginas boutique,
- ecommerce ligero,
- catálogo de cuarzos,
- formularios y selectores visuales.

---

## Tier 2 — Movimiento, scroll, 3D y experiencia premium

### 5. Lenis

URL: https://github.com/darkroomengineering/lenis

Uso recomendado:

- scroll suave,
- navegación premium,
- parallax,
- experiencia de landing larga.

Aplicación directa:

- portfolio Alcívar Consultores,
- Club Montt,
- cuarzos,
- páginas de alto impacto.

### 6. GSAP

URL: https://github.com/greensock/gsap

Uso recomendado:

- animaciones avanzadas,
- scroll reveal,
- timelines,
- transiciones cinemáticas,
- hero sections con alto impacto.

Aplicación directa:

- Metalpunk,
- Club Montt,
- páginas que necesiten energía visual agresiva o muy premium.

### 7. React Three Fiber

URL: https://github.com/pmndrs/react-three-fiber

Uso recomendado:

- escenas 3D,
- objetos interactivos,
- fondos especiales,
- experiencias de marca inmersivas.

Aplicación directa:

- cuarzos con cristales 3D,
- portfolio futurista,
- demos premium de alto ticket.

### 8. Drei

URL: https://github.com/pmndrs/drei

Uso recomendado:

- helpers para React Three Fiber,
- cámaras,
- controles,
- texto 3D,
- utilidades listas para WebGL.

Aplicación directa:

- visualizaciones 3D para productos,
- cristales/cuarzos,
- experiencias inmersivas.

---

## Tier 3 — Dashboards, datos y CRM

### 9. Recharts

URL: https://github.com/recharts/recharts

Uso recomendado:

- gráficos para CRM,
- métricas comerciales,
- embudos,
- ventas por etapa,
- dashboards tipo Power BI ligero.

Aplicación directa:

- NØX CRM,
- dashboards de prospección,
- reportes para clientes.

### 10. kbar

URL: https://github.com/timc1/kbar

Uso recomendado:

- comando tipo Cmd+K,
- buscador central,
- acciones rápidas,
- navegación productiva.

Aplicación directa:

- CRM personal,
- tablero de fábrica de ventas,
- panel de administración de clientes.

### 11. React Color

URL: https://github.com/uiwjs/react-color

Uso recomendado:

- selector de color,
- edición visual de marca,
- personalización de demos,
- panel para cambiar paletas por cliente.

Aplicación directa:

- futuro editor visual de plantillas,
- personalizador de landings.

---

## Tier 4 — HTML/CSS y componentes rápidos

### 12. Uiverse / Galaxy

URL: https://github.com/uiverse-io/galaxy

Uso recomendado:

- botones,
- loaders,
- inputs,
- microcomponentes HTML/CSS,
- prototipos rápidos sin React.

Aplicación directa:

- páginas simples para prospectos,
- versiones HTML descargables,
- efectos rápidos para demos urgentes.

### 13. Shadcn Space

URL: https://github.com/shadcnspace/shadcnspace

Uso recomendado:

- bloques de shadcn,
- templates,
- layouts,
- dashboards,
- secciones listas para producción.

Aplicación directa:

- CRM,
- cotizadores,
- paneles SaaS,
- páginas de servicios.

### 14. Awesome shadcn/ui

URL: https://github.com/birobirobiro/awesome-shadcn-ui

Uso recomendado:

- catálogo curado de recursos shadcn,
- descubrimiento de bloques,
- inspiración para sistemas React modernos.

Aplicación directa:

- búsqueda recurrente de componentes para nuevos clientes.

---

## Combinaciones por tipo de cliente

### Metalpunk

Usar:

- GSAP,
- Lenis,
- Uiverse,
- React Bits,
- efectos glitch,
- reveal agresivo,
- galería visual de alto contraste.

### Club Montt

Usar:

- shadcn/ui,
- Magic UI,
- Motion Primitives,
- Recharts si se agrega panel de reservas,
- cotizador visual,
- cards por tipo de evento.

### Cuarzos

Usar:

- Magic UI,
- React Bits,
- Motion Primitives,
- React Three Fiber + Drei si se quiere 3D,
- cards tipo joyería boutique,
- filtros por intención.

### NØX CRM

Usar:

- shadcn/ui,
- Recharts,
- kbar,
- Motion Primitives,
- Lenis,
- tablas, modales, command palette y gráficos.

---

## Consultas útiles para seguir explorando GitHub

```txt
landing page react tailwind stars:>1000 pushed:>2025-01-01
```

```txt
dashboard shadcn tailwind nextjs stars:>500
```

```txt
animation components react tailwind framer-motion stars:>500
```

```txt
html css javascript landing page animation stars:>300
```

```txt
ecommerce product cards tailwind react license:MIT
```

```txt
repo:magicuidesign/magicui hero path:components
```

```txt
repo:shadcn-ui/ui dashboard language:tsx
```

---

## Próximo paso recomendado

Crear dentro del arsenal una segunda carpeta:

```txt
arsenal-visual/patrones/
```

Con archivos propios como:

```txt
hero-premium.md
cards-catalogo.md
cotizador-eventos.md
catalogo-cuarzos.md
crm-dashboard.md
whatsapp-cta.md
```

Cada archivo debe describir el patrón, cuándo usarlo, código base sugerido, riesgos, variantes visuales y ejemplos de clientes.
