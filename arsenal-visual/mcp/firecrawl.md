# Firecrawl MCP para NOX FORGE

## Objetivo

Agregar una capa de extracción de contenido web para analizar prospectos antes de diseñar o programar.

Firecrawl permite convertir una URL pública en contenido estructurado útil para:

- Diagnóstico comercial.
- Auditoría de sitio existente.
- Extracción de servicios.
- Detección de propuesta de valor.
- Levantamiento de textos base.
- Preparación de Design Canvas.
- Investigación de competidores.

---

# Variables necesarias

```txt
FIRECRAWL_API_KEY=
```

Nunca guardar la API key dentro del repositorio.

Usar:

```txt
.env local
Vercel Environment Variables
GitHub Secrets
Panel seguro MCP
```

---

# Endpoints base

## Scrape

Uso: extraer una página específica.

```txt
POST https://api.firecrawl.dev/v2/scrape
```

## Search

Uso: buscar en la web y opcionalmente extraer contenido.

```txt
POST https://api.firecrawl.dev/v2/search
```

## Crawl

Uso: rastrear múltiples páginas de un sitio.

```txt
POST https://api.firecrawl.dev/v2/crawl
```

---

# Flujo NOX FORGE

```txt
1. Recibir URL del prospecto.
2. Ejecutar scrape.
3. Guardar markdown y JSON.
4. Detectar rubro, servicios, tono y CTA actuales.
5. Identificar oportunidades.
6. Crear Design Canvas.
7. Solo después diseñar o programar.
```

---

# Casos de uso por nicho

## Feria

Extraer:

- nombre de feria
- rubros
- horarios
- ubicación
- requisitos de postulación
- redes sociales

## Eventos

Extraer:

- capacidades
- tipos de eventos
- ubicación
- paquetes
- condiciones
- galería

## Hotel

Extraer:

- habitaciones
- experiencias
- restaurante
- ubicación
- tono institucional
- CTA de reserva

## Gimnasio

Extraer:

- planes
- precios
- horarios
- ubicación
- servicios
- promociones

## Mayorista

Extraer:

- categorías
- productos
- lista de precios
- condiciones de despacho
- canales de pedido

---

# Checklist de salida

Después de usar Firecrawl, producir:

```txt
[ ] Resumen del negocio.
[ ] Servicios detectados.
[ ] Oferta actual.
[ ] CTA actual.
[ ] Problemas de comunicación.
[ ] Oportunidades visuales.
[ ] Oportunidades comerciales.
[ ] Recomendación de nicho NOX FORGE.
[ ] Próximo paso.
```

---

# Regla

No usar Firecrawl para extraer contenido privado, restringido o con acceso no autorizado.
Solo usar sobre páginas públicas o URLs proporcionadas por el usuario.
