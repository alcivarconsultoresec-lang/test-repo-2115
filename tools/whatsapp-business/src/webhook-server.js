import 'dotenv/config';
import express from 'express';
import crypto from 'crypto';

const app = express();
const PORT = process.env.PORT || 3000;
const VERIFY_TOKEN = process.env.WHATSAPP_VERIFY_TOKEN;
const APP_SECRET = process.env.META_APP_SECRET;

app.use(express.json({
  verify: (req, res, buf) => {
    req.rawBody = buf;
  }
}));

function verifySignature(req) {
  if (!APP_SECRET) return true;
  const signature = req.get('x-hub-signature-256');
  if (!signature) return false;
  const expected = 'sha256=' + crypto
    .createHmac('sha256', APP_SECRET)
    .update(req.rawBody)
    .digest('hex');
  return crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(expected));
}

app.get('/webhook', (req, res) => {
  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];

  if (mode === 'subscribe' && token === VERIFY_TOKEN) {
    return res.status(200).send(challenge);
  }
  return res.sendStatus(403);
});

app.post('/webhook', (req, res) => {
  if (!verifySignature(req)) return res.sendStatus(403);

  const body = req.body;
  console.log(JSON.stringify({ receivedAt: new Date().toISOString(), body }, null, 2));

  // TODO: registrar en CRM/Supabase/Sheets.
  return res.sendStatus(200);
});

app.get('/health', (req, res) => {
  res.json({ ok: true, service: 'nox-forge-whatsapp-business' });
});

app.listen(PORT, () => {
  console.log(`Webhook server running on port ${PORT}`);
});
