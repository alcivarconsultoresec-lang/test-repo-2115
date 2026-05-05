const { chromium, devices } = require('playwright');
const fs = require('fs');
const path = require('path');

const url = process.argv[2];
if (!url) {
  console.error('Uso: npm run qa -- https://tu-url.vercel.app');
  process.exit(1);
}

const forbiddenTexts = [
  'lorem ipsum',
  'placeholder',
  'imagen aquí',
  'image here',
  'texto pendiente',
  'cargando foto'
];

async function runViewport(browser, name, viewport) {
  const page = await browser.newPage({ viewport });
  const result = {
    viewport: name,
    url,
    status: null,
    title: '',
    hasHero: false,
    hasCTA: false,
    hasWhatsApp: false,
    forbiddenTextFound: [],
    imagesTotal: 0,
    imagesBroken: 0,
    screenshot: '',
    errors: []
  };

  try {
    const response = await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 });
    result.status = response ? response.status() : null;
    result.title = await page.title();

    result.hasHero = await page.locator('h1, .hero, [class*="hero"]').first().count().then(Boolean);
    result.hasCTA = await page.locator('a, button').evaluateAll(items =>
      items.some(el => /whatsapp|cotizar|consultar|contactar|reservar|postular|agenda/i.test(el.innerText || el.getAttribute('aria-label') || ''))
    );
    result.hasWhatsApp = await page.locator('a[href*="wa.me"], a[href*="whatsapp"]').count().then(count => count > 0);

    const bodyText = (await page.locator('body').innerText()).toLowerCase();
    result.forbiddenTextFound = forbiddenTexts.filter(t => bodyText.includes(t));

    result.imagesTotal = await page.locator('img').count();
    result.imagesBroken = await page.locator('img').evaluateAll(imgs =>
      imgs.filter(img => !img.complete || img.naturalWidth === 0).length
    );

    const dir = path.join(process.cwd(), 'qa-output');
    fs.mkdirSync(dir, { recursive: true });
    result.screenshot = path.join('qa-output', `${name}.png`);
    await page.screenshot({ path: path.join(process.cwd(), result.screenshot), fullPage: true });
  } catch (error) {
    result.errors.push(error.message);
  } finally {
    await page.close();
  }

  return result;
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const results = [];

  results.push(await runViewport(browser, 'desktop', { width: 1440, height: 1100 }));
  results.push(await runViewport(browser, 'mobile', devices['Pixel 5'].viewport));

  await browser.close();

  const passed = results.every(r =>
    r.status && r.status < 400 &&
    r.hasHero &&
    r.hasCTA &&
    r.hasWhatsApp &&
    r.forbiddenTextFound.length === 0 &&
    r.imagesBroken === 0 &&
    r.errors.length === 0
  );

  const report = {
    generatedAt: new Date().toISOString(),
    passed,
    results
  };

  fs.mkdirSync(path.join(process.cwd(), 'qa-output'), { recursive: true });
  fs.writeFileSync(path.join(process.cwd(), 'qa-output', 'report.json'), JSON.stringify(report, null, 2));

  console.log(JSON.stringify(report, null, 2));
  process.exit(passed ? 0 : 2);
})();
