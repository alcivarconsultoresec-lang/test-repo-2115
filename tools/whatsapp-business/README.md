# NOX FORGE WhatsApp Business Tool

## Objetivo

Herramienta base para conectar NOX FORGE con WhatsApp Business Cloud API y, posteriormente, exponer acciones vía MCP.

## Requisitos

- Meta Business Manager.
- App en Meta Developers.
- Producto WhatsApp agregado.
- Número de WhatsApp Business.
- Access token.
- Phone Number ID.
- Webhook HTTPS público.

## Instalación

```bash
cd tools/whatsapp-business
npm install
cp .env.example .env
```

Completar `.env` con credenciales reales. No subir `.env` al repositorio.

## Enviar texto

```bash
npm run send:text -- 56912345678 "Hola, este es un mensaje de prueba"
```

## Enviar plantilla

```bash
npm run send:template -- 56912345678 nombre_plantilla es
```

## Levantar webhook

```bash
npm run webhook
```

URL de verificación Meta:

```txt
https://tu-dominio.com/webhook
```

## Limitaciones importantes

- Mensajes fuera de ventana requieren plantillas aprobadas.
- No usar para spam.
- Usar contactos con consentimiento o relación comercial válida.
- Registrar fuente y opt-in cuando sea posible.

## Próximos pasos

- Conectar con Supabase.
- Conectar con Matriz_Entregas.
- Agregar MCP server completo.
- Registrar respuestas y estados.
- Crear plantillas por nicho NOX FORGE.
