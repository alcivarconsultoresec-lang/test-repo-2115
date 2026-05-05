# Componente: Filter Pills

## Objetivo

Permitir segmentar contenido sin complejidad: rubros, estados, categorías, planes o tipos de evento.

## Cuándo usarlo

- Catálogos.
- Ferias.
- CRM.
- Productos.
- Eventos.
- Gimnasios con planes.

## Estructura

- Grupo de botones tipo pill.
- Estado activo visible.
- Conteo opcional.
- Cambio de contenido inmediato.

## Snippet conceptual

```html
<div class="filter-pills">
  <button class="active" data-filter="todos">Todos</button>
  <button data-filter="gastronomia">Gastronomía</button>
  <button data-filter="moda">Moda</button>
</div>
```

## Reglas UX

- No usar más de 8 filtros visibles sin scroll horizontal.
- En móvil, permitir desplazamiento horizontal.
- El estado activo debe ser evidente.
- Cada filtro debe afectar contenido real.

## Checklist

- Filtro activo visible.
- Scroll horizontal en móvil si hace falta.
- No hay filtros sin contenido.
- Funciona con teclado/click.
