# Protocolo de Producción Visual Diferenciada

Fecha: 2026-05-05

## Propósito

Evitar que las landings, catálogos y demos comerciales se vean iguales entre sí. Cada proyecto debe tener dirección de arte propia, tipografía diferenciada, composición visual específica y una experiencia mobile-first coherente con el rubro del cliente.

Este protocolo es obligatorio antes de producir o modificar cualquier landing de prospecto caliente.

---

## Regla principal

No escribir HTML final sin antes completar una capa de dirección visual.

Todo proyecto debe pasar por estas fases:

1. Lectura del contexto del cliente.
2. Consulta del arsenal visual.
3. Definición de dirección de arte.
4. Selección tipográfica diferenciada.
5. Maqueta visual en Canva o equivalente.
6. Aprobación o iteración del usuario.
7. Implementación en código.
8. Auditoría móvil con captura o checklist.
9. Publicación.
10. Registro de cambios y pendientes.

---

## Checklist obligatorio antes de escribir código

### 1. Identidad visual

Responder:

- ¿Qué rubro es?
- ¿Qué emoción debe provocar?
- ¿Debe sentirse premium, popular, técnico, artesanal, elegante, agresivo, espiritual, familiar o corporativo?
- ¿Qué NO debe parecer?

Ejemplo:

```txt
Carlos Queques no debe parecer un formulario genérico marrón.
Debe sentirse como boutique bakery cálida, apetecible, de confianza, con sabor casero pero presentación comercial moderna.
```

---

### 2. Tipografía

Cada proyecto debe tener una combinación tipográfica propia.

No usar siempre la misma fuente de sistema salvo que sea una decisión consciente.

Opciones recomendadas por rubro:

#### Repostería / bakery

- Display: Fraunces, Playfair Display, Cormorant Garamond, Libre Baskerville.
- Texto: Inter, Manrope, Nunito Sans, Source Sans 3.
- Sensación: cálida, editorial, apetecible, artesanal premium.

#### Eventos / clubes

- Display: Sora, Space Grotesk, Clash Display, Archivo Black.
- Texto: Inter, Manrope, DM Sans.
- Sensación: nocturna, energética, moderna.

#### Cuarzos / boutique espiritual

- Display: Cormorant Garamond, Playfair Display, Fraunces.
- Texto: Manrope, Inter, Nunito Sans.
- Sensación: delicada, boutique, ritual, perla/lavanda.

#### Mayoristas / distribuidoras

- Display: Sora, Barlow Condensed, Archivo.
- Texto: Inter, IBM Plex Sans, Manrope.
- Sensación: orden, precio, volumen, eficiencia.

#### Hoteles / corporativo

- Display: Playfair Display, Cormorant, Libre Baskerville.
- Texto: Inter, Source Sans 3, Manrope.
- Sensación: ejecutiva, elegante, sobria.

---

### 3. Composición visual

Cada landing debe elegir una de estas estructuras, no repetir siempre la misma:

#### A. Editorial premium

- Imagen grande respirada.
- Texto lateral o debajo, nunca tapando zonas importantes.
- Layout tipo revista.
- Ideal para hoteles, bakery, productos premium, cuarzos.

#### B. Catálogo comercial

- Hero breve.
- Filtros o categorías.
- Cards con producto, precio, intención y CTA.
- Ideal para cuarzos, queques, mayoristas.

#### C. Experiencia inmersiva

- Fondo animado o composición visual fuerte.
- Microinteracciones.
- Secciones con narrativa.
- Ideal para gimnasios, clubes, propuestas de alto impacto.

#### D. Dashboard/cotizador

- KPIs, filtros, formularios, cotizador o simulador.
- Ideal para CRM, reservas, distribuidoras, inventario.

---

### 4. Uso de Canva

Si el usuario pide Canva o maqueta visual:

1. Generar primera maqueta.
2. Esperar aprobación o pedir segunda variante solo si el usuario lo solicita.
3. Convertir el diseño aprobado en guía de implementación.
4. Respetar al pie de la letra:
   - tipografía sugerida,
   - jerarquía,
   - paleta,
   - imagen protagonista,
   - proporciones,
   - estilo de botones,
   - espacios blancos,
   - no tapar fotos con texto.

No basta con decir que se usó Canva; el código debe reflejar la maqueta.

---

## Checklist mobile-first

Antes de publicar, verificar:

- Header no debe ocupar más del 14% de la altura visible inicial en móvil.
- El CTA principal debe verse sin tapar la imagen principal.
- No debe existir dock flotante tapando fotos, cards o texto crítico.
- El hero no debe parecer desktop encogido.
- Las fotos deben tener `object-fit: cover` y recorte intencional.
- El texto no debe quedar encima de rostros, productos o comida.
- Los botones deben tener alto mínimo de 44 px.
- La primera pantalla debe explicar qué vende el negocio.

---

## Checklist de diferenciación visual

Antes de entregar, responder sí/no:

1. ¿La tipografía cambia respecto al proyecto anterior?
2. ¿La paleta responde al rubro real?
3. ¿El hero tiene composición propia?
4. ¿Las cards tienen un diseño acorde al producto?
5. ¿Los botones dicen acciones concretas y no textos genéricos?
6. ¿El formulario está integrado al diseño y no parece pegado al final?
7. ¿Hay una diferencia clara entre este proyecto y Club Montt/Cuarzos?
8. ¿La página se puede reconocer por su rubro aunque se quite el logo?

Si alguna respuesta clave es “no”, no publicar todavía.

---

## Protocolo para WhatsApp CTA

Usar siempre el patrón `arsenal-visual/patrones/whatsapp-cta.md`.

Cada CTA debe incluir intención específica:

- producto,
- sabor,
- pack,
- fecha,
- cantidad,
- origen del botón.

Evitar:

```txt
Contáctanos
Más información
Enviar
```

Preferir:

```txt
Pedir este sabor
Cotizar mi evento
Consultar disponibilidad
Armar mi pack
Ver menú de hoy
Reservar una visita
```

---

## Protocolo para repositorios mapeados

Antes de construir:

1. Revisar `arsenal-visual/repos-mapeados.md`.
2. Elegir 1 a 3 referencias/patrones.
3. Declarar qué se usará de cada una:
   - hero,
   - microinteracciones,
   - cards,
   - formularios,
   - navegación,
   - mobile layout.
4. No copiar una página completa.
5. Adaptar al cliente.

---

## Plantilla de brief visual obligatorio

```txt
Cliente:
Rubro:
Objetivo comercial:
Emoción principal:
Paleta:
Tipografía display:
Tipografía texto:
Composición elegida:
Inspiración del arsenal:
Elementos prohibidos:
CTA principal:
CTA secundarios:
Experiencia móvil esperada:
```

---

## Aplicación inmediata: Carlos Queques

### Diagnóstico

La primera versión cumple estructura comercial pero no cumple diferenciación visual suficiente.

Problemas detectados:

- tipografía genérica,
- header similar a otros proyectos,
- hero demasiado parecido a Club Montt,
- formulario funcional pero poco integrado a una experiencia bakery,
- faltan detalles editoriales de repostería,
- falta sensación de boutique bakery real.

### Nueva dirección obligatoria

```txt
Cliente: Carlos Queques
Rubro: repostería / queques caseros
Objetivo comercial: pedidos por WhatsApp
Emoción principal: apetito, confianza, hogar, antojo, regalo
Paleta: crema, mantequilla, caramelo, chocolate, café, dorado suave
Tipografía display: Fraunces o Playfair Display
Tipografía texto: Nunito Sans o Manrope
Composición: editorial bakery + catálogo comercial
Inspiración: hero-premium + whatsapp-cta + catálogo de producto
Elementos prohibidos: formularios genéricos, estética SaaS, cards idénticas a otros clientes
CTA principal: Pedir mi queque
CTA secundarios: Ver sabores, Cotizar pack oficina, Pedir para cumpleaños
Experiencia móvil: primera pantalla apetecible, header mínimo, imagen protagonista limpia
```

---

## Regla de cierre

Cada entrega debe incluir:

- qué patrón se usó,
- qué se cambió,
- qué archivo se tocó,
- qué queda pendiente,
- enlace público,
- commit.

