import { sendTextMessage } from './meta-client.js';

const [, , to, ...messageParts] = process.argv;
const text = messageParts.join(' ');

if (!to || !text) {
  console.error('Uso: npm run send:text -- 56912345678 "Hola, mensaje de prueba"');
  process.exit(1);
}

try {
  const result = await sendTextMessage({ to, text });
  console.log(JSON.stringify(result, null, 2));
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
