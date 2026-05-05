# Guía de configuración Meta + MCP para NOX FORGE

## Objetivo

Dejar una ruta práctica para configurar Meta WhatsApp Business Cloud API y los módulos MCP/programas creados en el repositorio.

---

# 1. Configurar Meta WhatsApp Business Cloud API

## 1.1 Crear o verificar activos Meta

Necesitas:

```txt
Meta Business Manager
Meta Developers App
Producto WhatsApp agregado
WhatsApp Business Account / WABA
Número de WhatsApp Business
Access Token
Phone Number ID
Business Account ID
Webhook HTTPS público
```

## 1.2 Datos que debes copiar de Meta

Guardar estos datos en un lugar seguro:

```txt
META_ACCESS_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WHATSAPP_BUSINESS_ACCOUNT_ID=
META_APP_SECRET=
WHATSAPP_VERIFY_TOKEN=
META_GRAPH_VERSION=v21.0
WEBHOOK_PUBLIC_URL=
```

No guardar claves reales en GitHub.

## 1.3 Permisos recomendados

```txt
whatsapp_business_messaging
whatsapp_business_management
business_management si se requiere gestionar activos del negocio
```

## 1.4 Webhook

Meta debe apuntar a:

```txt
https://TU_DOMINIO/webhook
```

El verify token debe coincidir con:

```txt
WHATSAPP_VERIFY_TOKEN
```

## 1.5 Regla de operación

```txt
Mensajes libres: solo dentro de la ventana permitida de conversación.
Mensajes fuera de ventana: usar plantillas aprobadas.
No usar para spam.
No usar como bot de propósito general.
Usar para atención, cotización, reservas, pedidos, seguimiento y soporte comercial.
```

---

# 2. Configurar herramienta WhatsApp del repo

Ruta:

```txt
tools/whatsapp-business/
```

## Instalación

```bash
cd tools/whatsapp-business
npm install
cp .env.example .env
```

Completar `.env`:

```txt
META_GRAPH_VERSION=v21.0
META_ACCESS_TOKEN=PEGAR_TOKEN
WHATSAPP_PHONE_NUMBER_ID=PEGAR_PHONE_NUMBER_ID
WHATSAPP_BUSINESS_ACCOUNT_ID=PEGAR_WABA_ID
WHATSAPP_VERIFY_TOKEN=nox_forge_verify_token
META_APP_SECRET=PEGAR_APP_SECRET
WEBHOOK_PUBLIC_URL=https://TU_DOMINIO/webhook
DEFAULT_COUNTRY_CODE=56
```

## Probar envío de texto

```bash
npm run send:text -- 56912345678 "Hola, este es un mensaje de prueba desde NOX FORGE"
```

## Probar plantilla

```bash
npm run send:template -- 56912345678 nombre_plantilla es
```

## Levantar webhook local

```bash
npm run webhook
```

Para pruebas públicas usar túnel HTTPS o desplegar en Vercel/Render/Railway.

---

# 3. Configurar QA Playwright

Ruta:

```txt
qa/
```

## Instalación

```bash
cd qa
npm install
npx playwright install chromium
```

## Ejecutar QA

```bash
npm run qa -- https://url-del-proyecto.vercel.app
```

## Salida

```txt
qa-output/report.json
qa-output/desktop.png
qa-output/mobile.png
```

Este QA revisa:

```txt
status de carga
hero
CTA
WhatsApp
placeholders
imágenes rotas
screenshots desktop/mobile
```

---

# 4. Configurar Firecrawl

Estado actual:

```txt
Documentado en arsenal-visual/mcp/firecrawl.md
Scripts operativos pendientes de crear
```

Variables futuras:

```txt
FIRECRAWL_API_KEY=
```

Uso esperado:

```txt
URL prospecto -> scrape -> markdown/json -> auditoría comercial -> Design Canvas
```

---

# 5. Configurar Browserbase / Playwright MCP

Estado actual:

```txt
Playwright local implementado en qa/
Browserbase MCP pendiente de conexión externa
```

Variables futuras:

```txt
BROWSERBASE_API_KEY=
BROWSERBASE_PROJECT_ID=
```

Uso esperado:

```txt
Vercel URL -> abrir navegador remoto -> capturas -> QA visual -> corrección -> entrega
```

---

# 6. Configurar Supabase MCP

Estado actual:

```txt
Planificado en arsenal-visual/mcp/plan-implementacion-mcp.md
Pendiente crear proyecto Supabase
```

Variables:

```txt
SUPABASE_URL=
SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
```

Tablas sugeridas:

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

---

# 7. Configurar Google Maps / Places MCP

Estado actual:

```txt
Planificado
Pendiente crear API key en Google Cloud y activar Places API
```

Variables:

```txt
GOOGLE_MAPS_API_KEY=
GOOGLE_PLACES_API_KEY=
```

Uso esperado:

```txt
rubro + zona -> negocios -> datos públicos -> CRM -> oferta personalizada
```

---

# 8. Configurar Cloudinary MCP

Estado actual:

```txt
Planificado
Pendiente crear cuenta Cloudinary
```

Variables:

```txt
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

Uso esperado:

```txt
fotos cliente -> optimización -> URLs webp -> landing rápida
```

---

# 9. Configurar analítica

## PostHog

Variables:

```txt
POSTHOG_API_KEY=
POSTHOG_PROJECT_ID=
```

Eventos sugeridos:

```txt
page_view
cta_whatsapp_click
form_submit
package_click
filter_used
scroll_75
```

## Google Analytics / Search Console

Variables:

```txt
GA_PROPERTY_ID=
GOOGLE_APPLICATION_CREDENTIALS=
```

---

# 10. Orden recomendado de configuración real

```txt
1. Meta WhatsApp Business Cloud API
2. QA Playwright local
3. Firecrawl
4. Browserbase MCP
5. Supabase
6. Google Maps / Places
7. Cloudinary
8. PostHog / Analytics
9. n8n / Make
10. Mercado Pago / Stripe
```

---

# 11. Regla de seguridad

Nunca guardar secretos reales en el repositorio.

Usar:

```txt
.env local
Vercel Environment Variables
GitHub Secrets
panel del proveedor MCP
```

---

# 12. Próximo archivo técnico pendiente

```txt
tools/whatsapp-business/src/mcp-server.js
```

Ese archivo debe exponer herramientas MCP:

```txt
send_text_message
send_template_message
receive_webhook_event
register_lead_message
schedule_followup
```
