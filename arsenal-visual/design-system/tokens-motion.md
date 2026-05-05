# Tokens de movimiento NOX FORGE

## Principio

El movimiento debe guiar atención, mejorar percepción o aumentar conversión. No se agregan efectos por decoración vacía.

## Duraciones

```css
--motion-fast: 160ms;
--motion-base: 280ms;
--motion-slow: 520ms;
--motion-hero: 900ms;
```

## Easings

```css
--ease-out: cubic-bezier(.22,1,.36,1);
--ease-in-out: cubic-bezier(.65,0,.35,1);
--ease-spring: cubic-bezier(.34,1.56,.64,1);
--ease-premium: cubic-bezier(.16,1,.3,1);
```

## Microinteracciones mínimas

- Botón: translateY(-2px), glow o cambio de borde.
- Card: elevación, borde activo o spotlight.
- Input: borde + glow suave al focus.
- CTA móvil: pulso lento o brillo controlado.
- Hero: entrada escalonada de título, subtítulo y CTA.

## Reglas

- Evitar animaciones que bloqueen lectura.
- Reducir movimiento en mobile si afecta rendimiento.
- No usar carruseles automáticos salvo que el usuario lo apruebe.
- Preferir animaciones por scroll solo cuando aporten narrativa.
