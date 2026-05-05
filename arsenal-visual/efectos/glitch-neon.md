# Efecto Glitch Neon

## Cuándo usarlo

- Gimnasios, música, urbano, tecnología, gaming, marcas con actitud fuerte.
- Títulos hero, nombres de marca o palabras de alto impacto.

## Cuándo no usarlo

- Hoteles de lujo sobrios.
- Documentos institucionales.
- Páginas con tono médico, legal o financiero serio.

## Reglas UX

- Usar solo en 1 o 2 elementos por pantalla.
- Mantener legibilidad.
- No animar párrafos largos.
- Evitar parpadeos excesivos.

## Snippet base

```css
.glitch {
  position: relative;
  color: var(--accent);
  animation: blinkPulse 1.6s steps(2,end) infinite;
}
.glitch::before,
.glitch::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: .7;
}
.glitch::before {
  color: var(--accent-2);
  transform: translate(2px,-1px);
  clip-path: inset(0 0 50% 0);
}
.glitch::after {
  color: var(--danger);
  transform: translate(-2px,1px);
  clip-path: inset(50% 0 0 0);
}
@keyframes blinkPulse {
  0%, 70%, 100% { filter: brightness(1); }
  72%, 80% { filter: brightness(1.9); }
  84% { filter: brightness(.75); }
}
```

## Checklist

- Texto legible.
- No marea.
- Refuerza identidad.
- No compite con CTA.
