# Layout: Marketplace Grid

## Cuándo usarlo

- Ferias.
- Catálogos de emprendedores.
- Tiendas multiproducto.
- Distribuidoras.
- Comunidades con miembros o puestos.

## Objetivo

Mostrar variedad sin perder orden, facilitando exploración por categoría e intención.

## Estructura visual

```txt
[Hero / valor principal]
[Filtros por rubro]
[Grid de cards]
[Producto, puesto o emprendedor destacado]
[CTA WhatsApp]
```

## Card recomendada

Cada card debe incluir:

- Imagen o placeholder premium si no hay foto.
- Nombre.
- Rubro.
- Breve propuesta.
- Estado o disponibilidad.
- CTA.

## Reglas UX

- Filtros visibles arriba del grid.
- Cards no idénticas visualmente si hay categorías distintas.
- El CTA debe ser contextual.
- En móvil, cards en una columna o carrusel manual.

## Snippet conceptual

```html
<section class="marketplace">
  <div class="filters"></div>
  <div class="market-grid">
    <article class="vendor-card"></article>
  </div>
</section>
```

## Checklist

- Se puede explorar rápido.
- Se entiende cada categoría.
- Hay CTA por item.
- No se siente como lista aburrida.
- Funciona bien en móvil.