---
pdf_options:
  format: A4
  margin:
    top: 0
    right: 0
    bottom: 0
    left: 0
---
<style>

  @page {
    margin: 20mm;
  }
  @page :first {
    margin: 0;
  }

  @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800;900&family=Plus+Jakarta+Sans:wght@400;700;900&display=swap');
  
  :root {
    --navy-dark: #0A192F;
    --navy-main: #1E3A8A;
    --navy-light: #EFF6FF;
    --gold: #D4AF37;
    --text-dark: #1E293B;
    --text-muted: #64748B;
  }

  body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--text-dark);
    background-color: #FAFCFF; /* Very subtle navy tint */
    line-height: 1.6;
    margin: 0;
    padding: 0;
  }

  h1, h2, h3, h4 {
    color: var(--navy-dark);
    font-family: 'Cinzel', serif;
  }

  h2 {
    border-bottom: 2px solid var(--navy-main);
    padding-bottom: 8px;
    margin-top: 40px;
    font-weight: 900;
    letter-spacing: -0.02em;
    color: var(--navy-main);
  }

  strong {
    color: var(--navy-dark);
  }

  ul li {
    margin-bottom: 8px;
  }

  .cover-page {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    page-break-after: always;
    background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%);
    position: relative;
    padding: 40px;
    box-sizing: border-box;
  }
  
  .cover-decoration {
    position: absolute;
    top: 40px;
    left: 40px;
    right: 40px;
    bottom: 40px;
    border: 2px solid var(--navy-main);
    opacity: 0.2;
    pointer-events: none;
  }

  .cover-logo {
    width: 250px;
    margin-bottom: 50px;
    z-index: 10;
  }

  .cover-title {
    font-family: 'Cinzel', serif;
    font-size: 38px;
    font-weight: 900;
    color: var(--navy-dark);
    margin-bottom: 15px;
    text-transform: uppercase;
    line-height: 1.1;
    z-index: 10;
  }

  .cover-subtitle {
    font-size: 20px;
    font-weight: 700;
    color: var(--navy-main);
    margin-bottom: 60px;
    letter-spacing: 2px;
    text-transform: uppercase;
    z-index: 10;
  }

  .cover-info {
    font-size: 14px;
    color: var(--text-muted);
    background: white;
    padding: 20px 40px;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(30, 58, 138, 0.05);
    z-index: 10;
  }

  .highlight-box {
    background-color: var(--navy-light);
    border-left: 4px solid var(--navy-main);
    padding: 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
  }
  
  .highlight-box strong {
    color: var(--navy-main);
  }

  hr {
    border: 0;
    height: 1px;
    background: var(--navy-main);
    opacity: 0.2;
    margin: 40px 0;
  }
</style>

<div class="cover-page">
  <div class="cover-decoration"></div>
  <img src="logo_navy.png" class="cover-logo" />
  <div class="cover-title">Propuesta Comercial<br>Desarrollo Web B2B</div>
  <div class="cover-subtitle">CASA TRADICIÓN</div>
  <div class="cover-info">
    <strong>Agencia:</strong> Meta Level<br>
    <strong>Contacto:</strong> +57 301 7505981<br>
    <strong>Fecha:</strong> 08 de Octubre, 2026
  </div>
</div>

## 1. EL ALCANCE DEL PROYECTO
Esta propuesta no contempla el uso de plantillas genéricas. Se trata de una arquitectura web construida desde cero (Código Nativo) orientada a dominar el sector B2B (HORECA).

**I. Identidad Visual Inmersiva:**
Desarrollo de un entorno digital de alta gama utilizando animaciones avanzadas (GSAP) y diseño editorial. El objetivo es vender el estatus premium de Casa Tradición, demostrando que no solo venden plátanos, sino ingeniería gastronómica.

**II. Motor B2B y Catálogo 3D:**
Espacio interactivo donde los clientes HORECA pueden explorar el portafolio. Las tarjetas de producto tendrán tecnología 3D, mostrando el empaque al vacío y la sugerencia de servido.

**III. Pasarela de Pagos (Fase 1 - WhatsApp):**
Sistema e-commerce B2B sin comisiones bancarias iniciales. El cliente llenará su información de envío en la web y al presionar "Comprar", la orden será enviada directamente al WhatsApp de Casa Tradición con el mensaje: *"Adjunto pago de [Producto], con valor de [X]"*. El cliente podrá adjuntar su comprobante de pago en el chat. Esta estructura en base de datos deja la página lista (solo requerirá comprar la licencia futura) para integrar una pasarela bancaria directa en una Fase 2.

## 2. STACK TECNOLÓGICO Y ARQUITECTURA
Implementaremos el mismo motor robusto usado en plataformas PWA de élite:
*   **Next.js & React 19:** Framework ultra rápido y responsivo, estándar en la industria.
*   **Google Firebase:** Motor de Base de Datos en tiempo real (Firestore) donde se centralizarán los catálogos y órdenes.
*   **TypeScript & Zustand:** Arquitectura tipada libre de errores y gestión de estado altamente optimizada.
*   **Tailwind CSS v4 & GSAP:** Diseño paramétrico con interacciones físicas y animaciones cinemáticas fluidas.

## 3. PLAN DE TRABAJO DETALLADO (90 DÍAS)

<div class="highlight-box">
<strong>MES 1: Frontend & Dirección de Arte (Días 01 - 30)</strong>
<ul>
<li><strong>Día 01 - 05:</strong> Levantamiento de requerimientos B2B, Wireframing y Arquitectura de Datos.</li>
<li><strong>Día 06 - 15:</strong> Setup de la infraestructura Next.js/React 19 y maquetación de la cuadrícula Jigsaw.</li>
<li><strong>Día 16 - 25:</strong> Desarrollo de los Catálogos 3D interactivos y estructuración UI con Tailwind.</li>
<li><strong>Día 26 - 30:</strong> Implementación de físicas y animaciones inmersivas (GSAP).</li>
</ul>
</div>

<div class="highlight-box">
<strong>MES 2: Backend & Motor de Base de Datos (Días 31 - 60)</strong>
<ul>
<li><strong>Día 31 - 40:</strong> Integración profunda con <strong>Google Firebase</strong>, levantando la base de datos Firestore y las reglas de seguridad.</li>
<li><strong>Día 41 - 50:</strong> Programación lógica de la Pasarela de Compras (recolección de info) y el enlace directo con WhatsApp.</li>
<li><strong>Día 51 - 55:</strong> Pruebas internas de estado con Zustand y QA de la agencia.</li>
<li><strong>Día 56 - 60: ENTREGA OFICIAL DEL SOFTWARE.</strong></li>
</ul>
</div>

<div class="highlight-box">
<strong>MES 3: Pruebas Beta y Soporte en Vivo (Días 61 - 90)</strong>
<ul>
<li><strong>Día 61 - 90:</strong> Lanzamiento en vivo a los primeros clientes HORECA. Realizaremos monitoreo constante de los servidores en Firebase, soporte técnico y correcciones de usabilidad en vivo basándonos en cómo los clientes reales usan la plataforma.</li>
</ul>
</div>

## 4. INVERSIÓN Y CONDICIONES

**Valor Total del Proyecto:** $2.500.000 COP

**Mantenimiento Operativo Mensual (Requisito Obligatorio):** $150.000 COP
Al ser un software vivo y no una plantilla estática, este rubro es indispensable para mantener el sistema en el aire. Incluye:
*   **Gestión de Infraestructura:** Administración técnica, monitoreo y asesoría/acompañamiento para la configuración de pagos directos de dominios y servidores (Google Firebase).
*   **Blindaje de Seguridad:** Certificados SSL, encriptación de datos de clientes HORECA y copias de seguridad.
*   **Soporte Técnico 24/7:** Monitoreo activo para un 99.9% de uptime (la página nunca se cae) y resolución de bugs.
*Aplica sistema de referidos: si nos refieren un cliente que cierre contrato con la agencia, este costo operativo baja al 50% ($75.000 COP) y desbloquean módulos de código gratis.*

### Planes de Pago Flexibles:

*   **Opción A (De Contado - Fast-Track):** Pago único de $2.500.000 COP al iniciar. Prioridad máxima y equipo dedicado: <strong style='color: #1E3A8A;'>Reduce el tiempo de desarrollo de 2 meses a solo 40 días</strong> para entrega acelerada.
*   **Opción B (3 Cuotas):** Tres pagos de $833.333 COP. Una cuota al inicio del Mes 1, otra al inicio del Mes 2, y la final al terminar la fase de pruebas del Mes 3.
*   **Opción C (40% / 60%) - Recomendado:** 
    *   Cuota inicial del 40% ($1.000.000 COP) para iniciar el desarrollo.
    *   Pago final del 60% ($1.500.000 COP) al finalizar el Mes 2 (Entrega del proyecto, justo antes de entrar a la fase de Pruebas).
