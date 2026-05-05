# Ticker / Marquee

## Cuándo usarlo

- Ferias, eventos, gimnasios, marketplaces, comunidades y páginas con lista de servicios o rubros.
- Para dar sensación de actividad, movimiento y amplitud de oferta.

## Cuándo no usarlo

- Cuando distrae del CTA principal.
- Cuando el contenido es largo o difícil de leer.

## Reglas

- Repetir el contenido para continuidad visual.
- Mantener velocidad lenta.
- Usar frases cortas.
- No poner información crítica solo en el ticker.

## Snippet base

```html
<div class="ticker">
  <div class="ticker-track">
    <span>Emprendedores locales</span>
    <span>Gastronomía</span>
    <span>Moda</span>
    <span>Artesanía</span>
    <span>Postulaciones abiertas</span>
    <span>Emprendedores locales</span>
    <span>Gastronomía</span>
    <span>Moda</span>
    <span>Artesanía</span>
    <span>Postulaciones abiertas</span>
  </div>
</div>
```

```css
.ticker {
  overflow: hidden;
  white-space: nowrap;
  border-block: 1px solid var(--line);
}
.ticker-track {
  display: inline-flex;
  gap: 2rem;
  animation: ticker 28s linear infinite;
}
@keyframes ticker {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}
```

## Checklist

- No tapa contenido.
- No es demasiado rápido.
- Refuerza servicios/rubros.
- Se ve bien en móvil.
