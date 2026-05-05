# Componente: Lead Form

## Objetivo

Capturar datos mínimos para continuar la venta sin frenar la conversión.

## Cuándo usarlo

- Eventos.
- Hoteles.
- Ferias.
- Servicios B2B.
- Catálogos mayoristas.

## Campos recomendados por nicho

### Eventos

- Nombre.
- Tipo de evento.
- Fecha tentativa.
- Cantidad de personas.
- Servicios requeridos.

### Feria

- Nombre.
- Rubro.
- Producto/servicio.
- Interés: visitar o postular.
- WhatsApp.

### Hotel anfitrión

- Nombre.
- Cargo.
- Empresa.
- Fecha sugerida.
- Motivo de reunión.

### Catálogo mayorista

- Nombre negocio.
- Categoría de interés.
- Volumen aproximado.
- Comuna.
- WhatsApp.

## Reglas UX

- Pedir lo mínimo.
- No más de 5 campos en mobile.
- Permitir derivar a WhatsApp.
- Validación visual simple.

## Snippet conceptual

```html
<form class="lead-form">
  <label>Nombre<input required></label>
  <label>Interés<select></select></label>
  <label>Mensaje<textarea></textarea></label>
  <button>Enviar consulta</button>
</form>
```

## Checklist

- Campos mínimos.
- Mensaje claro.
- CTA visible.
- Funciona en móvil.
- No pide datos innecesarios.
