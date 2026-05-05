import 'dotenv/config';

const GRAPH_VERSION = process.env.META_GRAPH_VERSION || 'v21.0';
const ACCESS_TOKEN = process.env.META_ACCESS_TOKEN;
const PHONE_NUMBER_ID = process.env.WHATSAPP_PHONE_NUMBER_ID;

function assertConfig() {
  const missing = [];
  if (!ACCESS_TOKEN) missing.push('META_ACCESS_TOKEN');
  if (!PHONE_NUMBER_ID) missing.push('WHATSAPP_PHONE_NUMBER_ID');
  if (missing.length) {
    throw new Error(`Missing environment variables: ${missing.join(', ')}`);
  }
}

export function normalizePhone(phone) {
  return String(phone || '').replace(/[^0-9]/g, '');
}

async function metaRequest(endpoint, payload) {
  assertConfig();
  const url = `https://graph.facebook.com/${GRAPH_VERSION}/${endpoint}`;
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${ACCESS_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });

  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(JSON.stringify({ status: response.status, data }, null, 2));
  }
  return data;
}

export async function sendTextMessage({ to, text }) {
  const phone = normalizePhone(to);
  if (!phone) throw new Error('Recipient phone is required');
  if (!text || !text.trim()) throw new Error('Message text is required');

  return metaRequest(`${PHONE_NUMBER_ID}/messages`, {
    messaging_product: 'whatsapp',
    recipient_type: 'individual',
    to: phone,
    type: 'text',
    text: {
      preview_url: false,
      body: text.trim()
    }
  });
}

export async function sendTemplateMessage({ to, templateName, language = 'es', components = [] }) {
  const phone = normalizePhone(to);
  if (!phone) throw new Error('Recipient phone is required');
  if (!templateName) throw new Error('Template name is required');

  return metaRequest(`${PHONE_NUMBER_ID}/messages`, {
    messaging_product: 'whatsapp',
    recipient_type: 'individual',
    to: phone,
    type: 'template',
    template: {
      name: templateName,
      language: { code: language },
      components
    }
  });
}
