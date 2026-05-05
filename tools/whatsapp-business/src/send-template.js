import { sendTemplateMessage } from './meta-client.js';

const [, , to, templateName, language = 'es'] = process.argv;

if (!to || !templateName) {
  console.error('Uso: npm run send:template -- 56912345678 nombre_plantilla es');
  process.exit(1);
}

try {
  const result = await sendTemplateMessage({ to, templateName, language });
  console.log(JSON.stringify(result, null, 2));
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
