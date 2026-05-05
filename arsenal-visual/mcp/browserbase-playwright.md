# Browserbase / Playwright para NOX FORGE

## Objetivo

Agregar una capa de QA visual y funcional antes de enviar cualquier página al cliente.

Esta conexión permite:

- Abrir URLs publicadas en Vercel.
- Tomar screenshots.
- Probar versión móvil.
- Validar botones de WhatsApp.
- Detectar errores visuales básicos.
- Revisar que imágenes/assets carguen.
- Generar evidencia antes de entregar.

---

# Estado de uso

## Modo local / GitHub

Se puede usar Playwright desde el repositorio para pruebas simples.

## Modo Browserbase MCP

Cuando Browserbase esté conectado como MCP, se usará para navegación remota, capturas y QA asistido.

---

# Variables necesarias

Para Browserbase:

```txt
BROWSERBASE_API_KEY=
BROWSERBASE_PROJECT_ID=
```

Para ejecución local Playwright no se requiere API key.

---

# Flujo NOX FORGE

```txt
1. Publicar en Vercel.
2. Obtener URL final.
3. Ejecutar QA Playwright.
4. Revisar screenshot desktop.
5. Revisar screenshot mobile.
6. Validar CTA WhatsApp.
7. Validar ausencia de placeholders.
8. Corregir si falla.
9. Entregar al cliente.
```

---

# Checklist visual automático

El QA debe revisar:

```txt
[ ] La página carga con status 200.
[ ] El hero existe.
[ ] Hay CTA visible arriba del fold.
[ ] Existe al menos un link wa.me o botón WhatsApp.
[ ] No aparece texto placeholder.
[ ] No aparece texto interno como “imagen aquí”, “lorem ipsum” o “cargando foto” permanente.
[ ] Las imágenes principales cargan.
[ ] Mobile no rompe layout.
[ ] Se genera screenshot desktop.
[ ] Se genera screenshot mobile.
```

---

# Uso sugerido

```bash
npm install
npm run qa -- https://url-del-proyecto.vercel.app
```

---

# Regla NOX FORGE

Ningún enlace debe enviarse a cliente sin pasar por esta revisión o una revisión manual equivalente.
