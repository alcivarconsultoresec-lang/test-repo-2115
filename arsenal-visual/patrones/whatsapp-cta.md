# Patrón: WhatsApp CTA Comercial

## Objetivo

Convertir visitas en conversaciones comerciales por WhatsApp, evitando botones genéricos como “Contáctanos”.

## Cuándo usarlo

- Todas las páginas de prospectos.
- Catálogos.
- Landings de eventos.
- Restaurantes.
- Gimnasios.
- Tiendas pequeñas.
- Servicios profesionales.

## Principio central

El botón no debe enviar al usuario a escribir desde cero. Debe abrir WhatsApp con un mensaje prellenado, específico para la oferta y la sección desde donde hizo clic.

## Fórmula de mensaje

```txt
Hola, vi la página de [negocio].
Me interesa [producto/servicio/oferta].
Quisiera saber disponibilidad, precio y próximos pasos.
Origen: [sección o botón].
```

## Estructura técnica

```html
<a href="https://wa.me/569XXXXXXXX?text=MENSAJE_CODIFICADO" target="_blank" rel="noopener">
  Consultar por WhatsApp
</a>
```

## Variante con JavaScript

```js
const phone = '569XXXXXXXX';
const baseMessage = 'Hola, vi la página y quiero consultar.';
function openWhatsApp(source){
  const text = `${baseMessage}\nOrigen: ${source}`;
  window.open(`https://wa.me/${phone}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
}
```

## Botones recomendados por tipo de negocio

### Gimnasio

```txt
Quiero entrenar esta semana
Consultar plan mensual
Agendar visita
Probar una clase
```

### Cuarzos

```txt
Quiero este cuarzo
Ayúdame a elegir mi cuarzo
Consultar disponibilidad
Armar un pack energético
```

### Eventos / Club Montt

```txt
Cotizar mi evento
Ver disponibilidad de fecha
Consultar cumpleaños
Consultar evento empresa
```

### Restaurante

```txt
Ver menú de hoy
Reservar mesa
Pedir por WhatsApp
Consultar evento privado
```

## Reglas importantes

1. Verificar si el número es móvil y compatible con WhatsApp.
2. En Chile, priorizar formato +56 9.
3. No usar teléfonos fijos para wa.me sin advertencia.
4. El CTA debe estar arriba, en medio y al final de la página.
5. En móvil, usar botón flotante o dock inferior.
6. Cada CTA debe tener intención comercial distinta.

## Ubicaciones recomendadas

```txt
Hero: CTA principal
Cards de producto: CTA específico
Galería: CTA de visita/consulta
FAQ: CTA para dudas
Footer: CTA final
Dock móvil: CTA siempre visible
```

## Prompt base para Codex

```txt
Integra botones de WhatsApp en esta landing.
Cada botón debe abrir un mensaje prellenado y específico según la sección.
Usa formato móvil chileno +56 9 cuando corresponda.
Incluye botón flotante en escritorio y dock inferior en móvil.
No uses textos genéricos; cada CTA debe vender una acción concreta.
```
