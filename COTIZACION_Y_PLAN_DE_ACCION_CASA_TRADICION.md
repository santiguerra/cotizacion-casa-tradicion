# PROPUESTA TÉCNICA Y COMERCIAL
## DESARROLLO DE PLATAFORMA WEB INTERACTIVA Y CATÁLOGO DIGITAL DE VENTAS
### CASA TRADICIÓN — PRECOCIDOS Y SNACKS

---

| **DATOS GENERALES DE LA COTIZACIÓN** | **DETALLE** |
| :--- | :--- |
| **Cliente:** | Casa Tradición — Precocidos y Snacks |
| **Atención:** | Don Diego / Gerencia General (`gerencia.tradicion@gmail.com`) |
| **Líder de Proyecto & Desarrollo:** | Santiago Guerra — Desarrollador Web & Soluciones Digitales |
| **Fecha de Emisión:** | Octubre de 2026 |
| **Validez de la Oferta:** | 15 días calendario |
| **Inversión Total:** | **$2.500.000 COP** (Dos millones quinientos mil pesos colombianos) |
| **Tiempo Estimado de Ejecución:** | 3 a 4 semanas (Entregas semanales por fases) |

---

## 1. RESUMEN EJECUTIVO & VISIÓN DEL PROYECTO

**Casa Tradición** representa el valor del campo colombiano llevado a la máxima eficiencia gastronómica: productos precocidos, prelistos y snacks de plátano y yuca que estandarizan tiempos, eliminan mermas y garantizan calidad tanto para el canal institucional (**HORECA**: restaurantes, asaderos, hamburgueserías, casinos y eventos) como para el consumidor final.

En atención a la conversación sostenida con Don Diego, el objetivo principal es diseñar y desarrollar una **plataforma web moderna, fresca, interactiva y con alto concepto de marca**, que no sea una simple página estática o "folleto digital", sino un **canal comercial activo** enfocado en:

1. **Exhibir con impacto visual gourmet** las 25 referencias del portafolio en sus diferentes presentaciones (gramajes y unidades).
2. **Facilitar la compra y cotización ágil**: que restaurantes y clientes seleccionen productos y envíen su orden de compra directamente y estructurada al **WhatsApp comercial de Casa Tradición**.
3. **Cero costos ocultos ni comisiones bancarias abusivas**: Atendiendo a la directriz de Don Diego, la plataforma integrará **pagos directos vía código QR (Bancolombia / Nequi / Daviplata)** sin costos mensuales ni retenciones de pasarelas de pago externas.
4. **Arquitectura escalable "Gateway-Ready"**: Dejamos la plataforma completamente estructurada para que, cuando el volumen de venta crezca, se pueda activar una pasarela como Wompi o Bold con solo conectar las credenciales.
5. **Innovación e Interactividad ("Fresca y con concepto")**: Simulador dinámico de rendimientos y porciones para chefs/administradores, filtros inteligentes por tipo de negocio y micro-animaciones de alto nivel.

---

## 2. ESTRUCTURA Y ARQUITECTURA DE LA PLATAFORMA

La web estará construida bajo estándares internacionales de alto rendimiento, optimizada para carga ultrarrápida en dispositivos móviles (donde ocurre más del 85% del tráfico comercial en Colombia) y con la identidad visual corporativa de Casa Tradición: tonos dorados artesanales, verdes frescos del plátano, calidez rústica y tipografía premium.

```
                    ┌──────────────────────────────────────────────┐
                    │           PORTAL CASA TRADICIÓN              │
                    └──────────────────────┬───────────────────────┘
                                           │
         ┌──────────────────┬──────────────┴─────┬─────────────────┬──────────────────┐
         │                  │                    │                 │                  │
    ┌────▼─────┐       ┌────▼───────┐      ┌─────▼──────┐    ┌─────▼─────┐       ┌────▼────┐
    │  INICIO  │       │ CATÁLOGO   │      │ SIMULADOR  │    │  CARRITO  │       │ CONTACTO│
    │ HERO 360 │       │25 PRODUCTOS│      │  HORECA    │    │ & QR PAGO │       │ & SEDE  │
    └──────────┘       └────┬───────┘      └────────────┘    └─────┬─────┘       └─────────┘
                            │                                      │
            ┌───────────────┼───────────────┐              ┌───────┴────────┐
            │               │               │              │                │
      Línea Verde     Línea Maduro     Línea Yuca      Orden Directa   Pago QR Directo
      & Patacones     & Aborrajados    & Croquetas     a WhatsApp      (0% Comisiones)
            │               │               │
      Tostones G.     Snacks & Bases  Canastas/Conos
```

### Secciones y Componentes Principales:

* **Cabecera & Barra de Navegación Dinámica:** Logo oficial de Casa Tradición con acabado dorado, navegación fluida, selector de categorías y botón de acceso rápido al carrito/pedido con contador en tiempo real.
* **Hero Banner de Alto Impacto:** Video/imagen estilizada con estética de la tienda física (ladrillo cálido, maderas nobles y producto fresco), titular comercial contundente y llamada a la acción (*"Estandariza tu cocina con la mejor tradición"*).
* **Catálogo Digital de 25 Referencias (5 Categorías):**
  1. *Línea Plátano Verde:* Plátano Picado trozos (500g - 1kg), Plátano Entero Verde (3 unds), Plátano Timbal (500g - 1kg), Moneda Verde (500g - 2.5kg).
  2. *Línea Plátano Maduro:* Maduro Entero (3 unds), Tajadas de Maduro (500g - 2.5kg), Tronquitos para asaderos (500g - 2.5kg), Cubos de Maduro para arroces y wok (500g - 2kg), Aborrajado Premium con queso (9 unds).
  3. *Línea Yuca Seleccionada:* Yuca Astilla (500g a 5kg), Croquetas de Yuca 8cm (500g - 2kg).
  4. *Línea Tostones y Patacones Gourmet:* Patacón Verde (500g - 2.5kg), Patacón Pintón (500g - 2.5kg), Burguer Pintón para hamburguesas (10 unds), Tostón Pisao 10cm crocante (10 unds), Tostón Redondo 17cm (10 unds), Tostón Artesanal 18cm (10 unds), Tostón Ovalado 17x24cm para patacón con todo (10 unds), Tostón Jumbo 28cm (10 unds), Tostón Dúo 13cm estándar universal (20 unds), Totuma de Plátano para rellenar (12 unds).
  5. *Línea Snacks, Canastas & Eventos:* Mini Canasta Frita 8cm (30 unds), Canasta Estándar Frita 14cm (10 unds), Cono Estándar Frito 14cm (10 unds), Platanitos Snacks 8cm (paquete x 40 unds).
* **Fichas de Producto con Modales Interactivos:**
  * Fotografía del paquete al vacío + Fotografía del plato servido/preparado (para abrir el apetito y mostrar versatilidad culinaria).
  * Ficha técnica: sugerencias de cocción (freír, hornear, asar, hervir), rendimiento por porción y ventajas de estandarización.
  * Selector interactivo de gramaje / empaque.
* **Simulador Interactivo de Pedidos y Rendimiento HORECA ("Innovación e IA Ligera"):**
  * Herramienta donde el chef o dueño de restaurante selecciona su tipo de negocio (Asadero, Típico, Comidas Rápidas, Eventos) y la cantidad de comensales diarios.
  * La web le calcula automáticamente los kilos o unidades requeridas, proyectando el ahorro en mermas (cero desperdicio de cáscaras) y tiempo de preparación en cocina.
* **Carrito de Compra & Módulo de Órdenes a WhatsApp:**
  * El cliente agrega referencias, selecciona cantidades y hace clic en *"Generar Pedido"*.
  * La plataforma compila automáticamente un mensaje limpio, formateado y profesional con el desglose exacto del pedido, el total estimado y los datos de despacho.
  * Se abre WhatsApp comercial con el texto listo para enviar, cerrando la venta sin intermediarios.
* **Módulo de Pago Seguro Directo vía QR:**
  * Modal emergente que despliega el código QR oficial de Casa Tradición (Bancolombia, Nequi o Daviplata).
  * Instrucciones claras: *"Escanea, transfiere y adjunta tu comprobante en este mismo chat de WhatsApp"*.
  * Sin comisiones de 3.5% + $900 COP por transacción que cobran las pasarelas tradicionales.
* **Módulo Preparado para Pasarela (Fase 2):**
  * Sección en el checkout con un botón estilizado e inactivo temporalmente o marcado como *"Próximamente pago con tarjeta y PSE"*, con la arquitectura interna ya diseñada para conectar la API de Wompi, Bold o Mercado Pago en minutos tan pronto Don Diego lo solicite.
* **Ubicación & Contacto Institucional:**
  * Mapa interactivo de Google Maps vinculado a la dirección física compartida en WhatsApp.
  * Botón de llamada directa, enlaces a redes sociales y correo corporativo (`gerencia.tradicion@gmail.com`).

---

## 3. DESGLOSE PRESUPUESTAL DETALLADO ($2.500.000 COP)

Cada peso invertido está estrictamente justificado en horas profesionales de ingeniería de software, diseño gráfico, estructuración comercial y puesta en producción:

| Ítem | Componente / Entregable | Justificación Técnica & Comercial | Inversión (COP) |
| :---: | :--- | :--- | :---: |
| **01** | **Arquitectura de Información, UI/UX & Sistema de Diseño Corporativo** | • Conceptualización visual "Fresca y Tradicional" alineada con el render de la tienda y el brochure.<br>• Paleta de color corporativa (Dorado #D4AF37, Verde Plátano, Terracota cálido, Blanco pulcro).<br>• Diseño de interfaz 100% responsiva (Mobile First para smartphones, tablets y computadores).<br>• Tratamiento digital y optimización de logotipos e imágenes del brochure. | **$450.000** |
| **02** | **Desarrollo Frontend & Catálogo Digital Interactivo (25 Referencias)** | • Maquetación moderna con código limpio y de máxima velocidad de carga.<br>• Programación de 25 fichas técnicas interactivas clasificadas en 5 líneas de producto.<br>• Selectores dinámicos de cantidades, gramajes (500g a 5kg) y unidades (10 a 40 unds).<br>• Visualización dual: Producto en empaque al vacío vs. Presentación servida en plato. | **$750.000** |
| **03** | **Motor de Pedidos a WhatsApp, Carrito Inteligente & Integración QR** | • Carrito de compras reactivo en tiempo real con memoria local (no pierde productos al navegar).<br>• Generador de orden automatizada a WhatsApp con desglose de ítems, cantidades y datos de entrega.<br>• Integración de módulo de pago directo con imagen de código QR de Bancolombia / Nequi sin cobro de comisiones bancarias por transacción.<br>• Arquitectura modular "Ready-to-Gateway" para futura conexión inmediata de Wompi/Bold. | **$650.000** |
| **04** | **Innovación Interactiva (Simulador HORECA) & Optimización SEO** | • Programación del Simulador / Calculadora de Porciones y Mermas para restaurantes y eventos.<br>• Micro-animaciones fluidas e interactivas al hacer scroll y clic en productos.<br>• Optimización técnica SEO en buscadores (Google) para términos clave: *plátano precocido, patacones para restaurantes, yuca congelada por mayor*.<br>• Integración interactiva de ubicación de sede en Google Maps. | **$400.000** |
| **05** | **Infraestructura Cloud, Dominio, Seguridad SSL & Capacitación** | • Configuración y despliegue en servidor cloud de alta velocidad y 99.9% de disponibilidad.<br>• Configuración de certificado de seguridad SSL HTTPS (candado verde de navegación segura).<br>• Vinculación del dominio web y enlace con el correo `gerencia.tradicion@gmail.com`.<br>• Sesión de entrega y capacitación personalizada a Don Diego para atención de pedidos.<br>• **30 días de soporte técnico y garantía post-lanzamiento** incluidos. | **$250.000** |
| **TOTAL** | **INVERSIÓN TOTAL DEL PROYECTO** | **Desarrollo Integral Llave en Mano** | **$2.500.000 COP** |

---

## 4. PLAN DE ACCIÓN Y CRONOGRAMA DE ENTREGAS

El proyecto se ejecutará en **4 semanas (1 mes de desarrollo ágil)**, con revisiones y avances continuos para asegurar total satisfacción:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ CRONOGRAMA DE TRABAJO (4 SEMANAS)                                           │
├─────────────┬─────────────────────────────────────────────────┬─────────────┤
│ SEMANA      │ ACTIVIDADES PRINCIPALES                         │ ENTREGABLE  │
├─────────────┼─────────────────────────────────────────────────┼─────────────┤
│ Semana 1    │ • Recopilación final de insumos y textos.       │ Mockup UI   │
│ (Días 1-7)  │ • Definición de paleta cromática y wireframes.  │ aprobado en │
│             │ • Aprobación de la estructura visual con cliente│ Figma/Demo  │
├─────────────┼─────────────────────────────────────────────────┼─────────────┤
│ Semana 2    │ • Construcción frontend responsive.             │ Catálogo    │
│ (Días 8-14) │ • Carga de las 25 referencias en 5 categorías.  │ funcional y │
│             │ • Implementación de fichas y fotos duales.      │ navegable   │
├─────────────┼─────────────────────────────────────────────────┼─────────────┤
│ Semana 3    │ • Programación del carrito y pedidos WhatsApp.  │ Sistema de  │
│ (Días 15-21)│ • Integración de código QR para pagos directos. │ compras y   │
│             │ • Desarrollo del Simulador HORECA interactivo.  │ simulador OK│
├─────────────┼─────────────────────────────────────────────────┼─────────────┤
│ Semana 4    │ • Pruebas en smartphones (iOS / Android) y PC.  │ Lanzamiento │
│ (Días 22-28)│ • Configuración de dominio, DNS y hosting cloud.│ oficial y   │
│             │ • Capacitación a Don Diego y entrega formal.    │ entrega     │
└─────────────┴─────────────────────────────────────────────────┴─────────────┘
```

---

## 5. BENEFICIOS Y RETORNO DE INVERSIÓN (ROI) PARA CASA TRADICIÓN

1. **Ahorro permanente en comisiones bancarias:**
   Al implementar el flujo directo de WhatsApp con QR en lugar de una pasarela automática tradicional desde el primer día, Casa Tradición se ahorra entre un **2.9% y 3.5% + $900 COP + IVA** por cada transacción, además de costos de suscripción mensual. En un volumen de $15.000.000 COP en pedidos mensuales, esto representa un **ahorro de más de $600.000 COP cada mes**, pagando la web en menos de 4 meses solo por comisiones ahorradas.
2. **Cierre de ventas B2B personalizado:**
   Los clientes de restaurantes no compran un kilo como en un supermercado; compran bultos de 5kg, cajas de 20 paquetes o frecuencias semanales. El pedido formateado en WhatsApp permite a Don Diego y su equipo comercial entablar relación directa, negociar volumen, fidelizar y coordinar la logística de entrega de inmediato.
3. **Catálogo 24/7 sin enviar PDFs pesados:**
   En lugar de enviar un archivo PDF de 15 megas que satura la memoria del celular de los chefs o que queda obsoleto, Don Diego solo envía el enlace web: `casatradicion.com`. Los clientes ven las fotos en alta definición, las presentaciones y montan el pedido en segundos.
4. **Posicionamiento de Marca Premium:**
   La combinación de la tienda física moderna con una presencia web impecable transmite solidez, confianza y estándares industriales, facilitando negociaciones con cadenas de restaurantes y distribuidores grandes.

---

## 6. CONDICIONES COMERCIALES Y FORMA DE PAGO

* **Monto Total:** $2.500.000 COP.
* **Forma de Pago Escalonada:**
  * **50% de Anticipo ($1.250.000 COP):** Para dar inicio a las actividades de diseño, arquitectura y montaje del entorno de desarrollo.
  * **50% Saldo Final ($1.250.000 COP):** Contra entrega a satisfacción, una vez culminadas las pruebas, desplegada la plataforma en el dominio final y efectuada la capacitación.
* **Garantía:** 30 días calendario de garantía técnica posterior a la entrega para ajustes menores de texto, imágenes o correcciones sin costo adicional.
* **Exclusiones:** No incluye pauta publicitaria en redes sociales (Facebook/Instagram Ads o Google Ads) ni adquisición del nombre de dominio comercial si aún no se tiene comprado (aproximadamente $60.000 COP anuales en proveedores de dominios).

---

## 7. ACEPTACIÓN DE LA PROPUESTA

Para formalizar el inicio del proyecto, Don Diego puede dar su visto bueno respondiendo por WhatsApp o correo electrónico confirmando la aceptación de la presente cotización para coordinar la transferencia del anticipo y el inicio inmediato del Sprint 1.

**Santiago Guerra**  
*Desarrollo & Soluciones Digitales Web*  
Contacto Directo: WhatsApp / Celular  
Email: Enlace directo al proyecto  
Octubre de 2026
