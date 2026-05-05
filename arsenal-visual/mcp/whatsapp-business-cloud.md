# WhatsApp Business Cloud MCP para NOX FORGE

## Estado

Sí es posible conectar NOX FORGE con WhatsApp Business vía MCP, pero la vía correcta no es WhatsApp personal ni WhatsApp Web.

La arquitectura correcta es:

```txt
NOX FORGE -> MCP Server -> WhatsApp Business Cloud API -> cliente/prospecto
```

---

## Qué permite

- Enviar mensajes de texto dentro de la ventana permitida.
- Enviar plantillas aprobadas.
- Recibir respuestas por webhook.
- Registrar conversaciones en CRM.
- Activar seguimientos.
- Conectar landing -> WhatsApp -> CRM.

---

## Requisitos Meta

Para operar se necesita:

```txt
1. Meta Business Manager.
2. App en Meta Developers.
3. Producto WhatsApp agregado.
4. Número de WhatsApp Business.
5. WHATSAPP_PHONE_NUMBER_ID.
6. WHATSAPP_BUSINESS_ACCOUNT_ID.
7. Access token permanente o system user token.
8. Webhook público HTTPS.
9. Verify token para webhook.
10. App secret para validar firmas.
```

---

## Variables de entorno

Nunca guardar estos valores reales en GitHub.

```txt
META_GRAPH_VERSION=v21.0
META_ACCESS_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WHATSAPP_BUSINESS_ACCOUNT_ID=
WHATSAPP_VERIFY_TOKEN=
META_APP_SECRET=
WEBHOOK_PUBLIC_URL=
```

Guardar en:

```txt
.env local
Vercel Environment Variables
GitHub Secrets
Panel seguro MCP
```

---

## Reglas comerciales y de cumplimiento

```txt
- No enviar spam.
- Usar solo contactos con consentimiento o relación comercial válida.
- Mensajes fuera de la ventana de conversación requieren plantilla aprobada.
- Los mensajes deben tener intención clara: atención, reserva, pedido, cotización o seguimiento.
- No usar la API para un chatbot genérico de propósito general.
- Registrar opt-in y fuente cuando sea posible.
```

---

## Herramientas MCP sugeridas

El MCP debe exponer acciones como:

```txt
send_text_message
send_template_message
list_templates
verify_webhook
receive_webhook_event
register_lead_message
schedule_followup
```

---

## Flujo NOX FORGE

```txt
1. Prospecto en CRM.
2. Verificar teléfono móvil y consentimiento.
3. Seleccionar plantilla o mensaje permitido.
4. Enviar por WhatsApp Business Cloud API.
5. Recibir respuesta por webhook.
6. Guardar evento en CRM/Supabase/Sheets.
7. Sugerir próxima acción.
```

---

## Arquitectura mínima creada en este repo

```txt
tools/whatsapp-business/
  package.json
  .env.example
  README.md
  src/meta-client.js
  src/send-text.js
  src/send-template.js
  src/webhook-server.js
  src/mcp-server.js
```

---

## Regla NOX FORGE

Este conector debe usarse para comunicación comercial legítima, seguimiento y atención; no para envíos masivos indiscriminados ni automatización invasiva.