# PROTOCOLO NOX FORGE

## Nombre de activación

**NOX FORGE**

Comando de uso:

```txt
Activa NOX FORGE
```

Cuando el usuario indique `NOX FORGE`, todo proyecto web, landing, demo comercial, dashboard, página para prospecto o interfaz HTML debe construirse bajo este protocolo, salvo que el usuario ordene explícitamente lo contrario.

---

# 1. Objetivo del protocolo

NOX FORGE existe para evitar páginas genéricas, repetitivas o pobres visualmente. Su finalidad es convertir cada proyecto en una pieza digital de alto impacto, funcional, vendible y técnicamente ordenada.

Cada entrega debe sentirse como:

```txt
una interfaz comercial premium + una herramienta de conversión + una pieza visual diferenciada
```

No se permite entregar una página que parezca plantilla básica, ejercicio escolar o formulario plano.

---

# 2. Regla cero: consultar contexto antes de crear

Antes de programar, se debe revisar el contexto disponible del proyecto y del arsenal visual.

## Archivos base a consultar cuando existan

```txt
arsenal-visual/repos-mapeados.md
arsenal-visual/patrones/hero-premium.md
arsenal-visual/patrones/whatsapp-cta.md
arsenal-visual/patrones/catalogo-cuarzos.md
```

## Para proyectos ya existentes

Antes de modificar:

```txt
1. Leer el index.html actual.
2. Leer README.md si existe.
3. Buscar assets disponibles.
4. Revisar commits o versiones si el usuario habla de una versión anterior.
5. No reescribir desde cero si el usuario pidió solo cambios específicos.
```

---

# 3. Modo de trabajo obligatorio

Todo proyecto debe pasar por estas capas:

## Capa 1: Diagnóstico comercial

Definir:

```txt
- Quién es el cliente/prospecto.
- Qué vende.
- Qué dolor comercial tiene.
- Qué acción debe realizar el visitante.
- Qué oferta se va a presentar.
- Qué canal de cierre se usará: WhatsApp, formulario, llamada, visita, reserva, cotización.
```

## Capa 2: Concepto visual

Antes del código debe existir un concepto:

```txt
- concepto central
- metáfora visual
- paleta
- tipografía
- estructura de layout
- componentes clave
- efecto diferenciador
```

## Capa 3: Arquitectura UX

La página debe responder rápido:

```txt
- Qué es esto.
- Para quién es.
- Qué gana el visitante.
- Qué opciones tiene.
- Cómo cotiza o contacta.
```

## Capa 4: Interfaz premium

Debe sentirse como sistema, no como folleto.

Usar módulos tipo:

```txt
- paneles visuales
- cards con jerarquía
- métricas
- filtros
- mapas de rubros
- catálogos
- estados
- barras dinámicas
- dock móvil
- CTA persistente
```

## Capa 5: Movimiento y microinteracciones

Cada proyecto debe tener al menos 3 capas dinámicas:

```txt
- animación de entrada o scroll
- hover visible en botones/cards
- ticker, marquee, partículas, glow, glitch o transición contextual
```

No usar movimiento decorativo sin función. El movimiento debe guiar atención, mejorar percepción o aumentar conversión.

---

# 4. Bibliotecas y tecnologías permitidas

Seleccionar según necesidad del proyecto.

## Base

```txt
HTML5
CSS3 interno o modular
JavaScript vanilla
Responsive mobile-first
```

## Efectos y experiencia

```txt
GSAP + ScrollTrigger
Lenis smooth scroll
tsParticles
Swiper
SplitType
Typed.js
anime.js
Vanta.js
Granim.js
CSS custom properties
IntersectionObserver
```

## Visualización tipo dashboard

```txt
cards KPI
barras de progreso
tablas visuales
filtros por categoría
grids asimétricos
paneles tipo command center
```

## Formularios y conversión

```txt
formularios con validación visual
links wa.me prellenados
CTA por sección
CTA por producto/servicio
botón flotante móvil
```

---

# 5. Cláusulas anti-genéricas

Queda prohibido:

```txt
- usar una estructura repetida sin adaptación al nicho
- crear hero sin concepto
- usar textos internos como “imagen aquí” o “placeholder” en versión cliente
- botones sin microinteracción
- secciones sin propósito comercial
- cards idénticas sin jerarquía visual
- colores sin criterio de marca o rubro
- dejar links de GitHub Pages como entrega cliente si se pidió Vercel
- borrar efectos o arquitectura existente sin autorización
- reemplazar una página completa cuando el usuario pidió cambios puntuales
```

---

# 6. Protocolo de modificación de proyectos existentes

Cuando el proyecto ya existe:

## No destruir

```txt
Nunca reescribir completamente sin autorización explícita.
```

## Cambios quirúrgicos

Si el usuario pide cambios específicos:

```txt
1. Identificar el bloque exacto.
2. Modificar solo ese bloque.
3. Mantener diseño, estructura, efectos y assets.
4. Confirmar qué archivo se tocó.
5. Indicar commit y enlace de revisión.
```

## Restauración

Si algo se rompe:

```txt
1. Detener cambios.
2. Buscar versión correcta en commits.
3. Restaurar desde fuente exacta, no reconstruir de memoria.
4. Confirmar visualmente con versión/cache busting.
```

---

# 7. Estándar visual mínimo

Cada página debe tener:

```txt
- hero fuerte
- CTA principal arriba del fold
- navegación clara
- secciones con jerarquía visual
- estética única por cliente
- diseño responsive real
- dock o CTA móvil
- WhatsApp o formulario funcional
- microinteracciones en enlaces, botones y cards
- footer con información de contacto
```

---

# 8. Estándar comercial mínimo

Cada página debe convertir. Por eso debe incluir:

```txt
- propuesta de valor clara
- beneficios concretos
- oferta o paquetes
- prueba visual: fotos, catálogo, mockup, métricas o casos
- objeciones resueltas
- CTA por sección
- mensaje de WhatsApp prellenado
- siguiente paso inequívoco
```

---

# 9. Modo dashboard CRM

Usar este modo cuando el usuario pida algo similar al CRM o una interfaz tipo sistema.

Aplicar:

```txt
- estética command center
- dark premium
- gradientes controlados
- cards KPI
- paneles por módulos
- filtros visuales
- barra lateral o navegación superior segmentada
- sensación de software operativo
- datos simulados solo si son útiles y etiquetados como ejemplo interno
```

Nunca hacerlo como landing plana.

---

# 10. Modo feria / marketplace / catálogo comunitario

Para ferias, clubes, emprendimientos, catálogos, comunidades o vitrinas comerciales:

```txt
- catálogo por rubro
- filtros por categoría
- agenda/horarios
- mapa o zona de ubicación
- módulo para nuevos postulantes
- cards de emprendedores
- novedades semanales
- CTA para visitantes
- CTA para expositores
- WhatsApp con mensaje diferenciado por intención
```

---

# 11. Protocolo de entrega

Al finalizar cada intervención:

```txt
1. Qué se modificó.
2. Por qué se modificó.
3. Qué archivo se tocó.
4. Commit generado.
5. Enlace de revisión con parámetro ?v=commit.
6. Qué queda pendiente.
```

---

# 12. Frase de activación operativa

Cuando el usuario diga:

```txt
Activa NOX FORGE
```

se debe asumir automáticamente:

```txt
- consultar arsenal visual
- diseñar antes de programar
- evitar plantillas genéricas
- priorizar interfaz premium
- incluir microinteracciones
- cuidar conversión comercial
- no destruir versiones existentes
- entregar con commit y enlace
```

---

# 13. Extensiones futuras del protocolo

Este protocolo puede crecer con nuevas capas:

```txt
NOX FORGE / Dashboard
NOX FORGE / Marketplace
NOX FORGE / Hotel
NOX FORGE / Restaurante
NOX FORGE / Fitness
NOX FORGE / Feria
NOX FORGE / Catálogo mayorista
NOX FORGE / Pitch visual
```

Cada extensión debe tener su propio patrón en `arsenal-visual/protocolos/`.

---

# 14. Principio final

Cada proyecto debe poder hacer que el cliente piense:

```txt
“Esto ya parece una herramienta real para vender más, no una maqueta improvisada.”
```
