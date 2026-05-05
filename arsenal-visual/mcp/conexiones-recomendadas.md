# Conexiones MCP recomendadas para NOX FORGE

## Objetivo

Convertir NOX FORGE en una navaja suiza de creación, investigación, diseño, publicación, auditoría y seguimiento comercial.

Este documento lista conexiones MCP recomendadas que todavía no forman parte completa de la máquina actual.

---

# 1. Prioridad máxima

## 1. Figma MCP

### Función

Permite consultar diseños, layouts, componentes, tokens visuales y referencias aprobadas antes de programar.

### Uso dentro de NOX FORGE

- Revisar diseños aprobados.
- Extraer paletas, tipografías y estructura.
- Validar que el HTML respete el diseño.
- Convertir maquetas en especificaciones frontend.

### Estado deseado

```txt
Diseño aprobado en Figma/Canva -> extracción visual -> código fiel al diseño.
```

### Prioridad

Muy alta.

---

## 2. Browserbase / Playwright / Puppeteer MCP

### Función

Permite abrir páginas, navegar, tomar capturas, probar formularios y detectar problemas visuales.

### Uso dentro de NOX FORGE

- Revisar demos publicadas.
- Probar páginas en Vercel.
- Validar mobile.
- Detectar botones rotos.
- Comparar diseño esperado vs página real.
- Tomar screenshots para auditoría.

### Estado deseado

```txt
Publicar -> abrir URL -> revisar visualmente -> detectar errores -> corregir.
```

### Prioridad

Muy alta.

---

## 3. Firecrawl MCP

### Función

Extrae contenido estructurado desde sitios web públicos.

### Uso dentro de NOX FORGE

- Extraer textos de prospectos.
- Analizar páginas existentes.
- Levantar servicios, precios, dirección y contenido público.
- Preparar auditorías comerciales.
- Generar bases de contexto antes de diseñar.

### Estado deseado

```txt
URL de prospecto -> extracción limpia -> diagnóstico -> propuesta visual.
```

### Prioridad

Muy alta.

---

## 4. Google Maps / Places MCP

### Función

Permite investigar negocios, ubicación, teléfono público, horarios, rubro, reseñas y presencia digital.

### Uso dentro de NOX FORGE

- Prospectar negocios.
- Completar datos del CRM.
- Confirmar ubicación.
- Detectar si tiene sitio web.
- Analizar reseñas para encontrar dolores comerciales.

### Estado deseado

```txt
Prospecto -> datos públicos -> CRM -> oferta personalizada.
```

### Prioridad

Muy alta.

---

## 5. Supabase MCP

### Función

Base de datos real para guardar prospectos, proyectos, estados, entregas, assets, URLs, mensajes y plantillas.

### Uso dentro de NOX FORGE

- CRM propio.
- Catálogo de proyectos.
- Historial de entregas.
- Base de datos de páginas creadas.
- Leads y seguimiento.
- Registro de URLs Vercel.

### Estado deseado

```txt
Sheets inicial -> Supabase operativo -> dashboard real -> automatización.
```

### Prioridad

Muy alta.

---

# 2. Prioridad alta

## 6. n8n / Make MCP

### Función

Automatización entre CRM, WhatsApp, Gmail, Sheets, Vercel y tareas comerciales.

### Uso dentro de NOX FORGE

- Crear tareas automáticas.
- Mover prospectos de estado.
- Enviar alertas.
- Generar mensajes.
- Sincronizar datos entre Sheets y Supabase.

### Prioridad

Muy alta.

---

## 7. WhatsApp Business Cloud API MCP

### Función

Automatizar mensajería, plantillas, respuestas y seguimiento por WhatsApp.

### Uso dentro de NOX FORGE

- Enviar mensajes a prospectos.
- Hacer seguimiento.
- Registrar respuestas.
- Activar plantillas aprobadas.
- Conectar landing con CRM.

### Prioridad

Muy alta.

---

## 8. Meta Business / Instagram / Facebook MCP

### Función

Gestión de presencia social, campañas, publicaciones y prospección.

### Uso dentro de NOX FORGE

- Revisar páginas de prospectos.
- Publicar piezas de campaña.
- Analizar presencia social.
- Generar campañas locales.

### Prioridad

Alta.

---

## 9. Cloudinary MCP

### Función

Gestión, optimización y entrega de imágenes para páginas web.

### Uso dentro de NOX FORGE

- Subir fotos de clientes.
- Optimizar imágenes.
- Generar URLs rápidas.
- Mantener assets ordenados.

### Prioridad

Alta.

---

## 10. Lighthouse / PageSpeed MCP

### Función

Auditoría de rendimiento, accesibilidad, SEO y buenas prácticas.

### Uso dentro de NOX FORGE

- Revisar páginas antes de entregar.
- Detectar problemas de carga.
- Validar mobile.
- Corregir SEO técnico básico.

### Prioridad

Alta.

---

# 3. Prioridad media-alta

## 11. PostHog MCP

### Función

Analítica de producto, eventos, clicks y funnels.

### Uso dentro de NOX FORGE

- Medir clicks en WhatsApp.
- Medir visitas.
- Medir scroll.
- Medir conversión por página.

### Prioridad

Media-alta.

---

## 12. Google Analytics / Search Console MCP

### Función

Medición de tráfico, SEO e indexación.

### Uso dentro de NOX FORGE

- Validar tráfico real.
- Ver páginas con mayor interés.
- Detectar consultas orgánicas.
- Mejorar posicionamiento.

### Prioridad

Media-alta.

---

## 13. Sentry MCP

### Función

Monitoreo de errores técnicos.

### Uso dentro de NOX FORGE

- Detectar errores JS.
- Revisar fallas en producción.
- Monitorear apps más complejas.

### Prioridad

Media.

---

## 14. Airtable MCP

### Función

CRM visual flexible si no se quiere empezar directamente en Supabase.

### Uso dentro de NOX FORGE

- Base de prospectos.
- Estados de proyectos.
- Catálogo de clientes.
- Registro visual de entregas.

### Prioridad

Media-alta.

---

## 15. Stripe / Mercado Pago MCP

### Función

Pagos, suscripciones, links de cobro y checkout.

### Uso dentro de NOX FORGE

- Cobrar demos.
- Activar planes mensuales.
- Generar links de pago.
- Registrar pagos de clientes.

### Prioridad

Media-alta.

---

# 4. Prioridad media

## 16. Spline MCP / workflow 3D

### Función

Crear o integrar objetos 3D en páginas premium.

### Uso dentro de NOX FORGE

- Hero 3D.
- Objetos de marca.
- Experiencias visuales avanzadas.

### Prioridad

Media.

---

## 17. Framer / Webflow MCP

### Función

Prototipado visual, publicación alternativa o inspiración de diseño.

### Uso dentro de NOX FORGE

- Crear prototipos.
- Validar experiencias visuales.
- Migrar referencias a código propio.

### Prioridad

Media.

---

## 18. Wappalyzer / BuiltWith MCP

### Función

Detectar tecnologías usadas por prospectos o competidores.

### Uso dentro de NOX FORGE

- Saber si un cliente usa Shopify, WordPress, Wix, etc.
- Preparar propuestas técnicas más específicas.
- Auditar competencia.

### Prioridad

Media-alta.

---

# 5. Orden recomendado de activación

```txt
1. Figma
2. Browserbase / Playwright
3. Firecrawl
4. Google Maps / Places
5. Supabase
6. n8n / Make
7. WhatsApp Business Cloud API
8. Cloudinary
9. Lighthouse / PageSpeed
10. PostHog / Google Analytics
11. Meta Business
12. Airtable
13. Sentry
14. Mercado Pago / Stripe
15. Spline / 3D
```

---

# 6. Regla de uso

Una conexión MCP solo se incorpora si resuelve una fase concreta:

```txt
investigar -> diseñar -> programar -> publicar -> medir -> vender -> automatizar
```

Si no mejora una de esas fases, no entra en la navaja suiza.
