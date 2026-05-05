# Componente: WhatsApp CTA Avanzado

## Objetivo

Convertir visitas en conversaciones prellenadas, segmentando la intención del usuario.

## Cuándo usarlo

- Landings comerciales.
- Catálogos.
- Ferias.
- Eventos.
- Gimnasios.
- Hoteles.
- Páginas de servicios.

## Tipos de CTA

1. CTA general.
2. CTA por producto.
3. CTA por plan.
4. CTA por servicio.
5. CTA para visitante.
6. CTA para expositor.
7. CTA para reunión.

## Reglas

- El mensaje debe venir prellenado.
- No usar teléfono fijo como WhatsApp sin verificar.
- En Chile, priorizar móviles +56 9.
- Cada CTA debe indicar origen o intención.
- El botón flotante móvil debe ser persistente.

## Snippet base

```js
const PHONE = '56900000000';
const messages = {
  general: 'Hola, vi la página y quiero más información.',
  expositor: 'Hola, quiero consultar por cupos para participar como expositor.',
  visitante: 'Hola, quiero consultar horarios y ubicación para visitar.'
};
function openWa(type){
  const msg = messages[type] || messages.general;
  window.open(`https://wa.me/${PHONE}?text=${encodeURIComponent(msg)}`,'_blank','noopener');
}
```

## Checklist

- Número validado.
- Mensaje natural.
- CTA por intención.
- Botón visible en móvil.
- Sin mensajes excesivamente largos.
