# Plan de implementación MCP para NOX FORGE

## Objetivo

Implementar conexiones MCP en orden estratégico para ampliar NOX FORGE desde un sistema de creación de páginas hacia una máquina completa de investigación, diseño, publicación, medición y venta.

---

# Fase 0: Base actual

Conectores ya disponibles:

```txt
GitHub
Gmail
Google Drive / Docs / Sheets / Slides
Google Calendar
Canva
Vercel
```

Uso actual:

```txt
GitHub = código, patrones, repositorios, versiones.
Canva = diseño visual, maquetas, piezas comerciales.
Vercel = publicación, deployments, validación.
Sheets = CRM / embudo / entregas.
Gmail = comunicaciones comerciales.
Calendar = reuniones y seguimiento.
Drive = documentos y recursos.
```

---

# Fase 1: Diseño y QA visual

## 1. Figma MCP

### Propósito

Cerrar la brecha entre diseño aprobado y código.

### Requisitos

- Cuenta Figma.
- Acceso a archivos de diseño.
- Token o conexión OAuth según proveedor MCP.

### Variables comunes

```txt
FIGMA_API_KEY
FIGMA_ACCESS_TOKEN
FIGMA_TEAM_ID
```

### Flujo NOX FORGE

```txt
Diseño aprobado -> inspección Figma -> Design Canvas -> implementación HTML/React -> QA visual
```

---

## 2. Browserbase / Playwright MCP

### Propósito

Validar visualmente páginas publicadas.

### Requisitos

- Cuenta Browserbase o entorno Playwright.
- API key si se usa Browserbase.

### Variables comunes

```txt
BROWSERBASE_API_KEY
BROWSERBASE_PROJECT_ID
```

### Flujo NOX FORGE

```txt
Vercel URL -> abrir -> screenshot -> revisar mobile -> detectar errores -> corregir
```

---

# Fase 2: Investigación y prospección

## 3. Firecrawl MCP

### Propósito

Extraer contenido estructurado de páginas públicas.

### Requisitos

- Cuenta Firecrawl.
- API key.

### Variables comunes

```txt
FIRECRAWL_API_KEY
```

### Flujo NOX FORGE

```txt
URL prospecto -> scrape/map/crawl -> resumen comercial -> oportunidades -> design canvas
```

---

## 4. Google Maps / Places MCP

### Propósito

Completar datos de prospectos y encontrar negocios.

### Requisitos

- Google Cloud.
- Places API habilitada.
- API key restringida.

### Variables comunes

```txt
GOOGLE_MAPS_API_KEY
GOOGLE_PLACES_API_KEY
```

### Flujo NOX FORGE

```txt
Rubro + zona -> negocios -> teléfonos/web/horarios/reseñas -> CRM -> oferta personalizada
```

---

# Fase 3: Base de datos y automatización

## 5. Supabase MCP

### Propósito

Crear base operacional de NOX FORGE.

### Requisitos

- Proyecto Supabase.
- URL del proyecto.
- Service role key o anon key según permisos.

### Variables comunes

```txt
SUPABASE_URL
SUPABASE_ANON_KEY
SUPABASE_SERVICE_ROLE_KEY
```

### Tablas sugeridas

```txt
prospects
projects
deliveries
assets
messages
followups
vercel_links
canva_designs
```

### Flujo NOX FORGE

```txt
Sheets -> Supabase -> dashboard -> automatización -> analítica
```

---

## 6. n8n / Make MCP

### Propósito

Automatizar tareas comerciales y técnicas.

### Requisitos

- n8n cloud/self-hosted o Make.
- Webhooks.
- Credenciales de servicios.

### Variables comunes

```txt
N8N_API_KEY
N8N_BASE_URL
MAKE_API_KEY
```

### Automatizaciones iniciales

```txt
Nuevo prospecto -> crear registro -> generar tarea -> preparar mensaje
Página publicada -> actualizar Matriz_Entregas -> crear seguimiento
Respuesta de correo -> actualizar temperatura -> sugerir próxima acción
```

---

# Fase 4: Mensajería y ventas

## 7. WhatsApp Business Cloud API MCP

### Propósito

Pasar de links manuales a comunicación controlada y medible.

### Requisitos

- Meta Business.
- Número aprobado.
- App de Meta.
- Token.
- Plantillas si aplica.

### Variables comunes

```txt
META_ACCESS_TOKEN
WHATSAPP_PHONE_NUMBER_ID
WHATSAPP_BUSINESS_ACCOUNT_ID
META_APP_ID
META_APP_SECRET
```

### Flujo NOX FORGE

```txt
Prospecto caliente -> mensaje autorizado -> seguimiento -> registro en CRM
```

---

## 8. Meta Business MCP

### Propósito

Administrar presencia, campañas y análisis social.

### Requisitos

- Business Manager.
- Páginas conectadas.
- Permisos de anuncios o contenido.

### Variables comunes

```txt
META_ACCESS_TOKEN
META_BUSINESS_ID
META_PAGE_ID
INSTAGRAM_BUSINESS_ID
```

### Flujo NOX FORGE

```txt
Página cliente -> campaña local -> pieza Canva -> publicación -> métricas
```

---

# Fase 5: Assets, rendimiento y medición

## 9. Cloudinary MCP

### Propósito

Gestionar imágenes profesionalmente.

### Requisitos

- Cuenta Cloudinary.
- Cloud name.
- API key/secret.

### Variables comunes

```txt
CLOUDINARY_CLOUD_NAME
CLOUDINARY_API_KEY
CLOUDINARY_API_SECRET
```

### Flujo NOX FORGE

```txt
Fotos cliente -> optimizar -> URLs webp -> usar en landing -> mejor performance
```

---

## 10. Lighthouse / PageSpeed MCP

### Propósito

Auditoría técnica antes de entregar.

### Requisitos

- Puede ser local, API o integración externa.

### Variables comunes

```txt
PAGESPEED_API_KEY
```

### Flujo NOX FORGE

```txt
URL Vercel -> auditoría -> score -> correcciones -> entrega
```

---

## 11. PostHog / Google Analytics MCP

### Propósito

Medir comportamiento real.

### Variables comunes

```txt
POSTHOG_API_KEY
POSTHOG_PROJECT_ID
GA_PROPERTY_ID
GOOGLE_APPLICATION_CREDENTIALS
```

### Eventos sugeridos

```txt
page_view
cta_whatsapp_click
form_submit
package_click
filter_used
scroll_75
```

---

# Fase 6: Control avanzado

## 12. Sentry MCP

### Propósito

Monitorear errores en apps más complejas.

### Variables comunes

```txt
SENTRY_AUTH_TOKEN
SENTRY_ORG
SENTRY_PROJECT
```

---

## 13. Mercado Pago / Stripe MCP

### Propósito

Cobrar planes, demos, páginas y suscripciones.

### Variables comunes

```txt
MERCADOPAGO_ACCESS_TOKEN
STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET
```

---

# Orden operativo recomendado

```txt
1. Browserbase / Playwright
2. Firecrawl
3. Google Maps / Places
4. Supabase
5. Figma
6. n8n / Make
7. WhatsApp Business Cloud API
8. Cloudinary
9. Lighthouse / PageSpeed
10. PostHog / Analytics
11. Meta Business
12. Sentry
13. Mercado Pago / Stripe
```

## Motivo del orden

Primero se mejora la capacidad de ver, investigar y validar. Luego se estructura la base de datos. Después se automatiza y finalmente se mide/cobra.

---

# Checklist de conexión por MCP

Para cada MCP nuevo:

```txt
[ ] Definir objetivo.
[ ] Crear cuenta o confirmar acceso.
[ ] Obtener API key/token.
[ ] Configurar permisos mínimos.
[ ] Guardar variables en entorno seguro.
[ ] Probar una llamada simple.
[ ] Documentar uso en arsenal-visual/mcp/.
[ ] Agregar al flujo NOX FORGE.
```

---

# Regla de seguridad

Nunca guardar API keys reales dentro del repositorio.

Usar:

```txt
.env local
Vercel Environment Variables
GitHub Secrets
Panel seguro del proveedor MCP
```
