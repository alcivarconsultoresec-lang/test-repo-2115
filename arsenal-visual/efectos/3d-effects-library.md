# Biblioteca de efectos 3D NOX FORGE

## Objetivo

Agregar profundidad visual premium sin convertir la página en un experimento pesado o lento.

## Tecnologías candidatas

### Three.js

Uso:

- Objetos 3D reales.
- Fondos WebGL.
- Partículas avanzadas.
- Escenas interactivas.

Cuándo usar:

- Tech.
- CRM futurista.
- Producto premium.
- Hero experimental.

Evitar si:

- Página debe cargar muy rápido en móviles básicos.
- No hay propósito visual claro.

### React Three Fiber

Uso:

- Three.js dentro de React.
- Componentes 3D reutilizables.
- Experiencias interactivas más complejas.

Usar con:

- Vite + React.
- Next.js.

### Spline

Uso:

- Escenas 3D diseñadas visualmente.
- Objetos interactivos integrados por iframe o embed.

Ideal para:

- Maquetas visuales rápidas.
- Hero premium.
- Presentaciones para cliente.

### Vanta.js

Uso:

- Fondos 3D/animados simples.
- Efectos tipo net, waves, birds, fog.

Ideal para:

- Landing rápida.
- Fondo visual sin construir escena desde cero.

### tsParticles 3D-like

Uso:

- Fondos de partículas.
- Movimiento dinámico ligero.
- Simulación de profundidad.

### CSS 3D

Uso:

- Cards con tilt.
- Perspectiva.
- Flip cards.
- Capas parallax.

## Patrones 3D recomendados

### Hero 3D controlado

- Fondo 3D sutil.
- Título por encima.
- CTA siempre legible.

### Card tilt premium

- Transform perspective.
- Hover suave.
- Sombra dinámica.

### Parallax por capas

- Fondo lento.
- Cards medio.
- CTA fijo.

### Objeto 3D de marca

- Solo si representa el producto o concepto.

## Reglas de rendimiento

- No cargar 3D pesado si el usuario está en móvil básico.
- Usar fallback CSS.
- Limitar FPS si es posible.
- No bloquear CTA.
- No tapar texto.
- Medir peso de librerías.

## Checklist

- El 3D aporta al concepto.
- CTA sigue visible.
- Hay fallback.
- No ralentiza mobile.
- No parece efecto gratuito.
