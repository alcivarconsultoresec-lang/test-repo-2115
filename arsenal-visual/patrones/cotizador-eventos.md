# Patrón: Cotizador Visual para Eventos

## Objetivo

Crear una landing para salones, clubes, restaurantes o centros de eventos que convierta consultas dispersas en cotizaciones ordenadas por WhatsApp.

Este patrón debe resolver el problema típico:

```txt
El cliente pregunta por WhatsApp o Marketplace y el negocio tiene que explicar todo desde cero.
```

## Cuándo usarlo

- Club Montt.
- Centros de eventos.
- Restaurantes con salones privados.
- Quinchos.
- Locales para cumpleaños.
- Productoras o banquetería.

## Estructura recomendada

```txt
Hero con promesa de evento
Selector por tipo de evento
Cards de espacios/capacidades
Paquetes sugeridos
Cotizador rápido
Galería
Condiciones y abonos
FAQ
CTA WhatsApp
```

## Selector por tipo de evento

Opciones mínimas:

```txt
Cumpleaños
Evento empresa
Fiesta privada
Celebración familiar
Arriendo simple
Evento con DJ
Cena o cóctel
```

Cada opción debe cambiar:

```txt
mensaje de WhatsApp
paquete recomendado
preguntas del cotizador
texto comercial
```

## Cotizador rápido

Campos recomendados:

```txt
Tipo de evento
Fecha tentativa
Cantidad de personas
Horario aproximado
Necesita DJ / comida / barra / decoración
Nombre
WhatsApp
```

Al enviar, abrir WhatsApp con mensaje ordenado:

```txt
Hola, quiero cotizar un evento en Club Montt.
Tipo de evento: Cumpleaños
Fecha: sábado 20
Personas: 50
Horario: noche
Servicios: DJ + barra
```

## Cards de paquetes

```txt
Arriendo simple
Evento cumpleaños
Evento empresa
Fiesta completa
```

Cada card debe incluir:

```txt
Ideal para
Incluye
No incluye
Capacidad sugerida
Botón cotizar
```

## Estética visual

Para clubes/eventos:

```txt
Fondo oscuro elegante
Dorado, azul profundo, burdeos o negro
Fotos grandes
Cards tipo invitación premium
Luces suaves
CTA claros
```

## Componentes recomendados del arsenal

- shadcn/ui: formulario, tabs, cards, accordion.
- Magic UI: hero y efectos de luz.
- Motion Primitives: selector animado por evento.
- WhatsApp CTA: mensaje prellenado por tipo de evento.
- Lenis: scroll premium.

## Reglas comerciales

1. El cliente debe entender rápido qué puede hacer en el local.
2. No saturar con texto largo.
3. La cotización debe reducir preguntas repetitivas.
4. El botón debe enviar un mensaje ya ordenado.
5. Separar claramente arriendo simple de evento completo.
6. Mostrar condiciones y abonos para evitar fricción.

## Copy base

```txt
Cotiza tu evento sin explicar todo desde cero.
Elige el tipo de celebración, estima la cantidad de personas y envía una solicitud ordenada por WhatsApp.
```

## Prompt base para Codex

```txt
Construye una landing para un centro de eventos llamado [nombre].
Debe funcionar como máquina de cotización, no como página decorativa.
Incluye selector de tipo de evento, paquetes sugeridos, galería, condiciones, preguntas frecuentes y botón de WhatsApp con mensaje prellenado según los datos del cotizador.
Estética elegante, nocturna y comercial.
HTML/CSS/JS puro, responsive y listo para GitHub Pages.
```

## Aplicación directa

- Club Montt.
- Restaurantes con salones.
- Productoras de eventos.
- Locales de arriendo para fiestas.
