import streamlit as st
import pandas as pd
from datetime import date

# ─────────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Herramientas Financieras Chubut",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# ESTILOS GLOBALES
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600&family=Barlow+Condensed:wght@600;700&display=swap');

/* Reset y base */
html, body, [class*="css"] {
    font-family: 'Public Sans', sans-serif;
    color: #1B1C1D;
}

/* Header principal */
.header-bar {
    background-color: #1C2443;
    color: white;
    padding: 18px 32px;
    border-radius: 10px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.header-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 26px;
    font-weight: 700;
    color: white;
    margin: 0;
    line-height: 1.2;
}
.header-sub {
    font-size: 12px;
    color: #9DBCCF;
    margin-top: 2px;
}
.header-period {
    font-size: 13px;
    color: #5894A7;
    text-align: right;
}

/* Aviso de bienvenida */
.welcome-banner {
    background: linear-gradient(135deg, #1C2443 0%, #5894A7 100%);
    color: white;
    border-radius: 10px;
    padding: 16px 24px;
    margin-bottom: 20px;
    font-size: 14px;
}

/* Cards de actividades */
.actividad-card {
    background: white;
    border-left: 4px solid #FF682C;
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 14px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
}
.actividad-fecha {
    font-size: 11px;
    color: #5894A7;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.actividad-titulo {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #1C2443;
    margin: 4px 0;
}
.actividad-desc {
    font-size: 13px;
    color: #555;
    line-height: 1.5;
}

/* Cards de programas */
.programa-card {
    background: white;
    border-radius: 10px;
    padding: 24px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    border-top: 4px solid #FF682C;
}
.programa-titulo {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #1C2443;
    margin-bottom: 4px;
}
.programa-org {
    font-size: 12px;
    color: #5894A7;
    font-weight: 600;
    margin-bottom: 12px;
}
.programa-desc {
    font-size: 13px;
    color: #444;
    line-height: 1.6;
    margin-bottom: 14px;
}
.programa-badge {
    display: inline-block;
    background: #FFF0EA;
    color: #FF682C;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 12px;
    font-weight: 600;
    margin: 2px 4px 2px 0;
}

/* Tabla de créditos */
.seccion-titulo {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #1C2443;
    border-bottom: 3px solid #FF682C;
    padding-bottom: 6px;
    margin: 24px 0 14px 0;
}
.credito-card {
    background: white;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 10px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.07);
    border-left: 3px solid #5894A7;
}
.credito-nombre {
    font-weight: 700;
    font-size: 14px;
    color: #1C2443;
}
.credito-detalle {
    font-size: 12px;
    color: #666;
    margin-top: 4px;
}
.tag-monto {
    display: inline-block;
    background: #E8F4F8;
    color: #1C2443;
    border-radius: 4px;
    padding: 1px 8px;
    font-size: 11px;
    font-weight: 600;
    margin-right: 6px;
}
.tag-tasa {
    display: inline-block;
    background: #FFF0EA;
    color: #FF682C;
    border-radius: 4px;
    padding: 1px 8px;
    font-size: 11px;
    font-weight: 600;
    margin-right: 6px;
}
.tag-plazo {
    display: inline-block;
    background: #F0F2F5;
    color: #555;
    border-radius: 4px;
    padding: 1px 8px;
    font-size: 11px;
    margin-right: 6px;
}
.contacto-box {
    background: #1C2443;
    color: white;
    border-radius: 8px;
    padding: 12px 18px;
    font-size: 12px;
    margin-top: 8px;
    margin-bottom: 20px;
}
.contacto-box a { color: #5894A7; }

/* Calendario */
.evento-card {
    background: white;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 10px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.07);
    display: flex;
    gap: 16px;
    align-items: flex-start;
}
.evento-fecha-box {
    background: #1C2443;
    color: white;
    border-radius: 8px;
    min-width: 54px;
    text-align: center;
    padding: 6px 4px;
    flex-shrink: 0;
}
.evento-dia {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 26px;
    font-weight: 700;
    line-height: 1;
}
.evento-mes {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #9DBCCF;
}
.evento-nombre {
    font-weight: 700;
    font-size: 14px;
    color: #1C2443;
}
.evento-org {
    font-size: 11px;
    color: #5894A7;
}
.evento-lugar {
    font-size: 12px;
    color: #666;
    margin-top: 2px;
}
.badge-realizado {
    display: inline-block;
    background: #E8F5E9;
    color: #2E7D32;
    border-radius: 20px;
    padding: 1px 10px;
    font-size: 11px;
    font-weight: 600;
}
.badge-proximo {
    display: inline-block;
    background: #FFF3E0;
    color: #E65100;
    border-radius: 20px;
    padding: 1px 10px;
    font-size: 11px;
    font-weight: 600;
}

/* Footer */
.footer-bar {
    background: #1C2443;
    color: #9DBCCF;
    border-radius: 8px;
    padding: 14px 24px;
    text-align: center;
    font-size: 12px;
    margin-top: 32px;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="header-bar">
  <div>
    <div class="header-title">💼 Herramientas Financieras Chubut</div>
    <div class="header-sub">Dirección de Promoción de las Inversiones · Ministerio de Producción · Gobierno del Chubut</div>
  </div>
  <div class="header-period">📅 Edición Junio 2026</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "📢 Actividades",
    "🚀 Programas",
    "💰 Créditos",
    "📅 Calendario"
])

# ════════════════════════════════════════════
# TAB 1 – ACTIVIDADES
# ════════════════════════════════════════════
with tab1:
    st.markdown("""
    <div class="welcome-banner">
        📬 <strong>Bienvenidos a la edición de junio 2026.</strong> Este newsletter reúne las novedades de la Dirección de Promoción de las Inversiones, las líneas de financiamiento vigentes, los programas activos y los eventos del ecosistema productivo provincial y nacional.
    </div>
    """, unsafe_allow_html=True)

    actividades = [
        {
            "fecha": "Junio 2026",
            "titulo": "Guía de Financiamiento Junio 2026",
            "desc": "Se actualizó la Guía de Líneas de Financiamiento Vigentes con tasas al día. Banco del Chubut redujo sus tasas 4 puntos porcentuales en mayo. Disponible para consulta y descarga.",
        },
        {
            "fecha": "2 de junio 2026",
            "titulo": "BNA Conecta – Trelew",
            "desc": "El Banco de la Nación Argentina realizó su Marketplace en Trelew (MEF). Se presentaron las líneas de crédito disponibles para MiPyMEs y emprendedores de la región.",
        },
        {
            "fecha": "Mayo – Junio 2026",
            "titulo": "Concurso Emprendimiento Argentino 2026 — Inscripciones abiertas",
            "desc": "Desde el 2 de junio hasta el 31 de julio de 2026 están abiertas las inscripciones para el Concurso Emprendimiento Argentino 2026. Dos categorías: Emprendimientos Tradicionales con Modelo de Negocio Innovador y Emprendimientos Tecnológicos y de Innovación Científica. La instancia provincial se realizará entre agosto y octubre.",
        },
        {
            "fecha": "18 de mayo 2026",
            "titulo": "Apertura del Programa INNOVA – CFI",
            "desc": "Se abrió la inscripción al Programa INNOVA del CFI, orientado a capitalizar startups y PyMEs nacientes. El cierre de la primera ventana es el 26 de junio. Las ventanas se repiten cada 4 meses. Más info en innova.cfi.org.ar.",
        },
        {
            "fecha": "Abril 2026",
            "titulo": "IV Foro Provincial de Garantías",
            "desc": "Se realizó en Posadas, Misiones, con participación de más de diez fondos de garantía provinciales, incluyendo FOGAMI, FONRED, FoGaCh, FOGAER, FOGAFE y el CFI. Chubut estuvo representado.",
        },
        {
            "fecha": "24 de abril 2026",
            "titulo": "Encuentro Mujeres Líderes Empresariales – Trelew",
            "desc": "Se realizó el encuentro provincial que destacó el rol de la mujer empresaria en Chubut. Actividad organizada por CICECH y socios.",
        },
    ]

    for a in actividades:
        st.markdown(f"""
        <div class="actividad-card">
            <div class="actividad-fecha">{a['fecha']}</div>
            <div class="actividad-titulo">{a['titulo']}</div>
            <div class="actividad-desc">{a['desc']}</div>
        </div>
        """, unsafe_allow_html=True)


# ════════════════════════════════════════════
# TAB 2 – PROGRAMAS
# ════════════════════════════════════════════
with tab2:
    st.markdown("<div style='margin-bottom:16px;font-size:14px;color:#555;'>Programas nacionales y provinciales de apoyo al ecosistema productivo y emprendedor de Chubut.</div>", unsafe_allow_html=True)

    programas = [
        {
            "titulo": "Concurso Emprendimiento Argentino 2026",
            "org": "Secretaría de Industria, Comercio y de la Pequeña y Mediana Empresa · Ministerio de Economía",
            "desc": """Certamen federal que busca descubrir y dar visibilidad a emprendimientos destacados de las distintas regiones del país. Fomenta la competitividad y el crecimiento de proyectos innovadores con impacto local, nacional y global.

El concurso tiene <strong>etapas provinciales</strong> (agosto–octubre 2026) y una <strong>final nacional</strong> (noviembre 2026, CABA). Los ganadores acceden a reconocimientos, conexión estratégica con el ecosistema emprendedor y acceso a programas de apoyo.

<strong>Categorías 2026:</strong>
<br>• Emprendimientos Tradicionales con Modelo de Negocio Innovador
<br>• Emprendimientos Tecnológicos y de Innovación Científica
<br><em>(cada categoría se subdivide en: Despegue Emprendedor y Crecimiento y Expansión)</em>

<strong>Inscripciones:</strong> 2 de junio al 31 de julio de 2026.""",
            "badges": ["🗓 Inscripciones abiertas", "🏆 Premios provinciales y nacionales", "📍 Federal"],
            "link": "https://www.argentina.gob.ar/economia/pymes-emprendedores-y-economia-del-conocimiento/ecosistema-emprendedor/concurso-emprendimiento",
            "contacto": "emprendimientoargentino@produccion.gob.ar",
        },
        {
            "titulo": "Programa INNOVA – CFI",
            "org": "Consejo Federal de Inversiones (CFI)",
            "desc": """Programa del CFI orientado a impulsar el ecosistema de innovación argentino. Busca capitalizar startups y PyMEs nacientes y aumentar la inversión de riesgo en Argentina con impacto en las provincias.

<strong>Objetivo:</strong> financiamiento y apoyo a proyectos de innovación con potencial de escalabilidad y generación de empleo local.

<strong>Ventanas de inscripción:</strong> cada 4 meses. Próximo cierre: <strong>26 de junio 2026</strong>.""",
            "badges": ["⏰ Cierre 26/06/2026", "💡 Innovación y startups", "🌐 Federal con impacto provincial"],
            "link": "https://innova.cfi.org.ar/",
            "contacto": "chubut@uepcfi.org.ar | WA: 2804290300",
        },
        {
            "titulo": "CRECER – Ministerio de Producción Chubut",
            "org": "Ministerio de Producción · Gobierno del Chubut",
            "desc": """Línea de financiamiento provincial destinada a productores agrícolas, ganaderos e industriales de Chubut. Financia inversiones en plantas de frutos y fruta fina, maquinaria e infraestructura orientada al desarrollo productivo.

<strong>Monto:</strong> Hasta $20 millones (consultar cupo disponible)
<br><strong>Tasa:</strong> 20% fija anual (15% para asociados a cooperativas)
<br><strong>Plazo:</strong> Se ajusta a los ciclos productivos""",
            "badges": ["🌿 Agro e industria", "🏛 Provincial", "💬 Consultar cupo"],
            "link": None,
            "contacto": "Subsecretaría de Financiamiento · WA: 2804276775",
        },
    ]

    for p in programas:
        badges_html = " ".join([f'<span class="programa-badge">{b}</span>' for b in p["badges"]])
        link_html = f'<br><a href="{p["link"]}" target="_blank" style="color:#FF682C;font-size:13px;font-weight:600;">🔗 Más información</a>' if p["link"] else ""
        st.markdown(f"""
        <div class="programa-card">
            <div class="programa-titulo">{p['titulo']}</div>
            <div class="programa-org">{p['org']}</div>
            <div class="programa-desc">{p['desc']}</div>
            {badges_html}
            {link_html}
            <div class="contacto-box" style="margin-top:12px;">
                📞 <strong>Contacto:</strong> {p['contacto']}
            </div>
        </div>
        """, unsafe_allow_html=True)


# ════════════════════════════════════════════
# TAB 3 – CRÉDITOS
# ════════════════════════════════════════════
with tab3:
    st.markdown("<div style='margin-bottom:8px;font-size:13px;color:#666;'>Líneas vigentes al período Junio 2026. Los datos son de carácter orientativo. Consulte siempre a la entidad correspondiente.</div>", unsafe_allow_html=True)

    # Filtro
    instituciones = ["Todas", "Min. Producción Chubut", "Sec. de Trabajo Chubut", "CFI", "Banco del Chubut", "BNA", "BICE"]
    filtro = st.selectbox("🔍 Filtrar por institución:", instituciones)

    creditos = {
        "Min. Producción Chubut": {
            "color": "#4CAF50",
            "contacto": "Subsecretaría de Financiamiento · WA: 2804276775",
            "lineas": [
                {
                    "nombre": "CRECER",
                    "destinatarios": "Productores Agrícolas, Ganaderos e Industriales",
                    "destino": "Inversiones en plantas productivas, maquinaria e infraestructura",
                    "monto": "Hasta $20 M",
                    "tasa": "20% fija (15% cooperativas)",
                    "plazo": "Según ciclo productivo",
                    "gracia": "A consultar",
                },
            ]
        },
        "Sec. de Trabajo Chubut": {
            "color": "#2196F3",
            "contacto": "Rawson: (02965) 4483543 / 4484834 · secretaria.str@chubut.gov.ar",
            "lineas": [
                {
                    "nombre": "Chubut Emprende",
                    "destinatarios": "Emprendedores individuales o equipos ≤5 personas / PJ ≤10 empleados con residencia ≥2 años en Chubut",
                    "destino": "Equipamiento, insumos, producción de bienes o servicios. Subsidio de capital reintegrable.",
                    "monto": "Hasta $5 M",
                    "tasa": "Capital reintegrable",
                    "plazo": "A consultar",
                    "gracia": "—",
                },
                {
                    "nombre": "Incluir Trabajo",
                    "destinatarios": "Instituciones que promueven inserción laboral de personas con discapacidad",
                    "destino": "Pago de capacitadores, bienes e insumos",
                    "monto": "Hasta $1.050.000",
                    "tasa": "Subsidio (no reintegrable)",
                    "plazo": "—",
                    "gracia": "—",
                },
                {
                    "nombre": "Fomentar Empleo Verde",
                    "destinatarios": "Comunas rurales, municipios, empresas y emprendimientos productivos verdes",
                    "destino": "Asistencia técnica + capacitación + financiamiento no reintegrable (por concurso, hasta 10 proyectos/año)",
                    "monto": "Hasta $9 M",
                    "tasa": "No reintegrable (concurso)",
                    "plazo": "—",
                    "gracia": "—",
                },
            ]
        },
        "CFI": {
            "color": "#009688",
            "contacto": "UEP Chubut · Tel: (0280) 4481302 · chubut@uepcfi.org.ar · WA: 2804290300 · Lic. Romina Farías / Cdr. Diego Mundt",
            "lineas": [
                {
                    "nombre": "Competitividad PyME",
                    "destinatarios": "MiPyMEs (humanas y jurídicas) con actividades productivas",
                    "destino": "Obra civil, activo fijo y capital de trabajo",
                    "monto": "$4 M – $200 M",
                    "tasa": "Año 1: 28% fija · Año 2+: TAMAR+2pp",
                    "plazo": "Hasta 48 meses",
                    "gracia": "Hasta 6 meses semiplena",
                },
                {
                    "nombre": "Financiamiento Verde",
                    "destinatarios": "MiPyMEs que realicen inversiones verdes",
                    "destino": "Riego, energías renovables, eficiencia energética, economía circular",
                    "monto": "$4 M – $500 M",
                    "tasa": "Años 1-2: 21% fija · Año 3+: TAMAR+2pp",
                    "plazo": "Hasta 60 meses",
                    "gracia": "Hasta 12 meses semiplena",
                },
                {
                    "nombre": "Desarrollo Productivo y Financiero de Mujeres",
                    "destinatarios": "Emprendimientos liderados por mujeres (monotributistas/autónomas) o empresas con ≥51% capital femenino o directora",
                    "destino": "Obras civiles, bienes de capital, capital de trabajo asociado",
                    "monto": "$4 M – $200 M",
                    "tasa": "Años 1-2: 21% fija · Año 3+: TAMAR+2pp",
                    "plazo": "Hasta 48 meses",
                    "gracia": "Hasta 6 meses semiplena",
                },
                {
                    "nombre": "Abordaje Integral / Triple Impacto",
                    "destinatarios": "Empresas B o en proceso · vinculadas a Programas CFI de abordaje integral",
                    "destino": "Inversiones con impacto económico, ambiental y/o social",
                    "monto": "$4 M – $500 M",
                    "tasa": "A consultar (Sistema Alemán)",
                    "plazo": "Hasta 60 meses",
                    "gracia": "Hasta 6 meses semiplena",
                },
                {
                    "nombre": "Exportación – Prefinanciación CFI",
                    "destinatarios": "MiPyMEs proveedoras de bienes e insumos para exportación",
                    "destino": "Capital de trabajo para ciclo productivo y colocación en mercados externos",
                    "monto": "Hasta USD 200.000 (100% FOB)",
                    "tasa": "2,5% fija TNA en USD",
                    "plazo": "Hasta 12 meses",
                    "gracia": "—",
                },
            ]
        },
        "Banco del Chubut": {
            "color": "#FF682C",
            "contacto": "WA: +54 9 280 472-8375 · bancochubut.com.ar",
            "nota": "⚡ Las tasas bajaron 4 puntos porcentuales en mayo 2026.",
            "lineas": [
                {
                    "nombre": "Chubut Crece – Micro y Pequeñas Empresas",
                    "destinatarios": "Personas humanas y jurídicas con certificado MiPyME vigente",
                    "destino": "Capital de trabajo",
                    "monto": "Hasta $100 M (o 3 meses compras s/IVA)",
                    "tasa": "46% fija",
                    "plazo": "Hasta 36 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "Chubut Crece – PyMEs",
                    "destinatarios": "Personas humanas y jurídicas con certificado MiPyME vigente",
                    "destino": "Capital de trabajo",
                    "monto": "Hasta $300 M (o 3 meses compras s/IVA)",
                    "tasa": "50% fija",
                    "plazo": "Hasta 36 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "CRECER (Min. Producción)",
                    "destinatarios": "Productores agrícolas, ganaderos e industriales",
                    "destino": "Maquinaria, infraestructura productiva",
                    "monto": "Hasta $20 M",
                    "tasa": "20% fija (15% cooperativas)",
                    "plazo": "Según ciclo productivo",
                    "gracia": "A consultar",
                },
                {
                    "nombre": "Agropecuarios – Capital de Trabajo",
                    "destinatarios": "Productores agropecuarios",
                    "destino": "Compra de insumos agrícolas/ganaderos, adquisición/retención de hacienda",
                    "monto": "Hasta $200 M",
                    "tasa": "36%–38% fija",
                    "plazo": "Hasta 60 meses (destinos hasta 18 m)",
                    "gracia": "—",
                },
                {
                    "nombre": "Agropecuarios – Inversiones",
                    "destinatarios": "Productores agropecuarios",
                    "destino": "Financiación de inversiones y bienes de uso",
                    "monto": "Hasta $500 M",
                    "tasa": "38% fija",
                    "plazo": "Hasta 60 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "Inversión Productiva",
                    "destinatarios": "Empresas o grupos con actividad industrial o de servicios",
                    "destino": "Bienes de capital, construcción de instalaciones",
                    "monto": "Hasta $3.000 M",
                    "tasa": "37% fija",
                    "plazo": "Hasta 60 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "Inversión Productiva (Ampliación)",
                    "destinatarios": "Empresas MiPyME con actividad industrial o de servicios",
                    "destino": "Bienes de capital, tecnología, construcción",
                    "monto": "Hasta $8.000 M por grupo económico",
                    "tasa": "40,5%",
                    "plazo": "Hasta 60 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "Fortalecer Chubut",
                    "destinatarios": "MiPyMEs con certificado vigente y actividad productiva en la provincia",
                    "destino": "Inversión productiva",
                    "monto": "Hasta $1.500 M por PyME",
                    "tasa": "TNA fija 12 meses · luego Badlar+250pb",
                    "plazo": "Hasta 60 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "Sello Origen Chubut",
                    "destinatarios": "Adherentes al Sello vigentes",
                    "destino": "Capital de trabajo y bienes de capital",
                    "monto": "Hasta $60 M",
                    "tasa": "36%",
                    "plazo": "Hasta 36 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "Capital de Trabajo (Comercio y Servicios)",
                    "destinatarios": "MiPyMEs del segmento comercio y servicios",
                    "destino": "Recomposición de capital de trabajo",
                    "monto": "Hasta $25 M",
                    "tasa": "47% fija",
                    "plazo": "Hasta 24 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "Profesionales",
                    "destinatarios": "Profesionales con título universitario",
                    "destino": "Actividades profesionales en la provincia",
                    "monto": "Hasta $40 M",
                    "tasa": "46% fija",
                    "plazo": "Hasta 60 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "Línea Verde Empresas",
                    "destinatarios": "Personas con actividad comercial en Chubut",
                    "destino": "Adquisición de bienes eco-sustentables",
                    "monto": "Hasta $40 M",
                    "tasa": "41%",
                    "plazo": "Hasta 48 meses",
                    "gracia": "Hasta 6 meses semiplena",
                },
                {
                    "nombre": "Damnificados Emergencia Climática – Capital de Trabajo",
                    "destinatarios": "Clientes del banco con constancia de afectación municipal",
                    "destino": "Productores agropecuarios/ganaderos afectados por nevadas",
                    "monto": "Hasta $25 M",
                    "tasa": "33% fija",
                    "plazo": "Hasta 36 meses",
                    "gracia": "12 meses",
                },
                {
                    "nombre": "Damnificados Emergencia Climática – Bienes de Capital",
                    "destinatarios": "Clientes del banco con constancia de afectación municipal",
                    "destino": "Productores agropecuarios/ganaderos afectados por nevadas",
                    "monto": "Hasta $50 M",
                    "tasa": "30% fija",
                    "plazo": "Hasta 60 meses",
                    "gracia": "12 meses",
                },
                {
                    "nombre": "COMEX – Prefinanciación de Exportación",
                    "destinatarios": "Empresas o grupos exportadores",
                    "destino": "Financiar la producción de bienes de exportación",
                    "monto": "Hasta 70% FOB",
                    "tasa": "Fija (a consultar)",
                    "plazo": "Hasta 6 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "COMEX – Financiación de Exportación",
                    "destinatarios": "Empresas o grupos exportadores",
                    "destino": "Financiar la venta de bienes de exportación",
                    "monto": "Hasta 70% FOB",
                    "tasa": "Fija (a consultar)",
                    "plazo": "Hasta 6 meses",
                    "gracia": "—",
                },
            ]
        },
        "BNA": {
            "color": "#1565C0",
            "contacto": "Equipo de Relacionamiento Trelew · Tel: (0280) 4386328",
            "lineas": [
                {
                    "nombre": "MiPyMEs Inversión Productiva (Reg. 750)",
                    "destinatarios": "MiPyMEs de todos los sectores",
                    "destino": "Proyectos de inversión para producción/comercialización y capital de trabajo",
                    "monto": "Hasta 100% calificación crediticia",
                    "tasa": "32% fija (3 años) · luego TAMAR+5,5pp",
                    "plazo": "Hasta 72 meses",
                    "gracia": "Hasta 6 meses",
                },
                {
                    "nombre": "MiPyMEs y Grandes Empresas en Pesos (Reg. 700)",
                    "destinatarios": "Todas las empresas",
                    "destino": "Inversión y capital de trabajo",
                    "monto": "Según calificación crediticia",
                    "tasa": "Desde 37% fija (MiPyMEs) / 40% (Grandes)",
                    "plazo": "Inversión: hasta 10 años · K.T.: hasta 3 años",
                    "gracia": "—",
                },
                {
                    "nombre": "Maquinaria Nacional en Pesos",
                    "destinatarios": "MiPyMEs de todos los sectores",
                    "destino": "Maquinarias, equipos, bienes de capital y vehículos nuevos nacionales",
                    "monto": "Hasta 100% del valor (sin IVA)",
                    "tasa": "Desde 29% fija",
                    "plazo": "Hasta 48 meses",
                    "gracia": "Según equipo",
                },
                {
                    "nombre": "Maquinaria Nacional Usada",
                    "destinatarios": "MiPyMEs y grandes empresas",
                    "destino": "Maquinaria agrícola o industrial usada nacional (hasta 10 años)",
                    "monto": "Hasta 70% del valor",
                    "tasa": "34% fija (3 años) · luego TAMAR+4pp",
                    "plazo": "Hasta 48 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "Camiones, Utilitarios y Más",
                    "destinatarios": "Empresas de transporte y logística",
                    "destino": "Adquisición de camiones, remolques y semirremolques nacionales",
                    "monto": "Según calificación",
                    "tasa": "Desde 29% fija",
                    "plazo": "Hasta 60 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "Programa Reconversión y Eficiencia Energética",
                    "destinatarios": "Todas las empresas",
                    "destino": "Productos sustentables energéticamente eficientes y/o de baja emisión",
                    "monto": "Hasta 100% de lo solicitado",
                    "tasa": "Desde 31% fija · luego TAMAR+6pp",
                    "plazo": "Hasta 10 años",
                    "gracia": "Hasta 24 meses (proyectos especiales)",
                },
                {
                    "nombre": "Financiamiento en Parques Industriales",
                    "destinatarios": "Empresas radicadas o a radicarse en parques industriales",
                    "destino": "Energías renovables, bienes de capital, capital de trabajo (máx. 20%)",
                    "monto": "Hasta 100% de lo solicitado",
                    "tasa": "32% fija o TAMAR+4pp",
                    "plazo": "Hasta 10 años",
                    "gracia": "Hasta 24 meses",
                },
                {
                    "nombre": "Prefinanciación de Exportaciones",
                    "destinatarios": "Exportadores finales de todos los sectores",
                    "destino": "Financiar etapas de producción y comercialización para mercados externos",
                    "monto": "Hasta 90% del valor FOB",
                    "tasa": "Desde 3,25% TNA (USD)",
                    "plazo": "Hasta 365 días",
                    "gracia": "—",
                },
                {
                    "nombre": "Financiación de Exportaciones",
                    "destinatarios": "Exportadores finales de todos los sectores",
                    "destino": "Facilitar la colocación de bienes nacionales en el exterior",
                    "monto": "Hasta 100% de la factura",
                    "tasa": "Desde 3,25% TNA",
                    "plazo": "Hasta 360 días",
                    "gracia": "—",
                },
                {
                    "nombre": "Nación PyME Digital",
                    "destinatarios": "MiPyMEs",
                    "destino": "Capital de trabajo y otros destinos – 100% online",
                    "monto": "Hasta $599 M",
                    "tasa": "A consultar",
                    "plazo": "A consultar",
                    "gracia": "—",
                },
            ]
        },
        "BICE": {
            "color": "#6A1B9A",
            "contacto": "Rocío Vera Bertoldi · avera@bice.com.ar · regionsur@bice.com.ar",
            "lineas": [
                {
                    "nombre": "Inversión Productiva a Largo Plazo",
                    "destinatarios": "PyMEs y grandes empresas",
                    "destino": "Modernización productiva, tecnología, bienes de capital, plantas",
                    "monto": "PyMEs: hasta $3.500 M · Grandes: hasta $6.500 M (80% del bien)",
                    "tasa": "A consultar",
                    "plazo": "Hasta 84 meses",
                    "gracia": "12 meses",
                },
                {
                    "nombre": "Leasing Productivo – Bienes Nuevos",
                    "destinatarios": "PyMEs y grandes empresas",
                    "destino": "Utilitarios, pickups, camiones, tractores, excavadoras, maquinarias nuevas",
                    "monto": "PyMEs: hasta $3.500 M · Grandes: hasta $6.500 M (100% del bien)",
                    "tasa": "A consultar",
                    "plazo": "Hasta 60 meses",
                    "gracia": "—",
                },
                {
                    "nombre": "Capital de Trabajo",
                    "destinatarios": "PyMEs y Grandes empresas",
                    "destino": "Compra de insumos, materia prima, combustible",
                    "monto": "PyMEs: $700 M · Medianas: $1.100 M · Grandes: $1.800 M",
                    "tasa": "A consultar",
                    "plazo": "Hasta 36 meses",
                    "gracia": "6 meses",
                },
                {
                    "nombre": "COMEX – Exportaciones",
                    "destinatarios": "PyMEs y no PyMEs exportadoras",
                    "destino": "Exportación de manufacturas agropecuarias, industriales y servicios argentinos",
                    "monto": "Hasta 100% del valor FOB en USD",
                    "tasa": "A consultar",
                    "plazo": "Hasta 9 meses",
                    "gracia": "—",
                },
            ]
        },
    }

    for inst, data in creditos.items():
        if filtro != "Todas" and filtro != inst:
            continue

        nota = data.get("nota", "")
        nota_html = f'<div style="background:#FFF3E0;border-left:3px solid #FF682C;padding:8px 12px;border-radius:4px;font-size:12px;margin-bottom:8px;">⚡ {nota}</div>' if nota else ""

        st.markdown(f"""
        <div class="seccion-titulo" style="border-color:{data['color']};">
            {inst}
        </div>
        {nota_html}
        """, unsafe_allow_html=True)

        for linea in data["lineas"]:
            st.markdown(f"""
            <div class="credito-card" style="border-left-color:{data['color']};">
                <div class="credito-nombre">{linea['nombre']}</div>
                <div class="credito-detalle"><em>{linea['destinatarios']}</em></div>
                <div class="credito-detalle" style="margin-top:4px;">{linea['destino']}</div>
                <div style="margin-top:8px;">
                    <span class="tag-monto">💰 {linea['monto']}</span>
                    <span class="tag-tasa">📊 {linea['tasa']}</span>
                    <span class="tag-plazo">⏱ {linea['plazo']}</span>
                    {"<span class='tag-plazo'>⌛ Gracia: " + linea['gracia'] + "</span>" if linea['gracia'] and linea['gracia'] != "—" else ""}
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="contacto-box">
            📞 <strong>Contacto {inst}:</strong> {data['contacto']}
        </div>
        """, unsafe_allow_html=True)


# ════════════════════════════════════════════
# TAB 4 – CALENDARIO
# ════════════════════════════════════════════
with tab4:
    st.markdown("<div style='margin-bottom:12px;font-size:14px;color:#555;'>Eventos del ecosistema productivo, financiero y emprendedor 2026.</div>", unsafe_allow_html=True)

    eventos = [
        {
            "fecha": "10/03/2026", "nombre": "Certificación de Idoneidad – Sistema Nacional de Garantías (inicio)",
            "org": "CASFOG", "lugar": "Virtual / Intensivo",
            "enfoque": "Marco regulatorio SGR, Mercado de Capitales PyME, lavado de dinero",
            "link": "casfog.com.ar", "estado": "Realizado"
        },
        {
            "fecha": "15/04/2026", "nombre": "IV Foro Provincial de Garantías y II Foro de la Región Litoral",
            "org": "FOGAMI, FONRED, FoGaCh, FOGAER, FOGAFE y CFI", "lugar": "Posadas, Misiones",
            "enfoque": "Más de 10 fondos de garantía provinciales",
            "link": "", "estado": "Realizado"
        },
        {
            "fecha": "24/04/2026", "nombre": "Encuentro Mujeres Líderes Empresariales",
            "org": "CICECH y socios", "lugar": "Trelew",
            "enfoque": "Rol de la Mujer Empresaria en Chubut",
            "link": "", "estado": "Realizado"
        },
        {
            "fecha": "28/04/2026", "nombre": "EXPO EFI 2026 – Congreso de Economía, Finanzas e Inversiones",
            "org": "Invecq + CASFOG", "lugar": "CABA – Centro de Convenciones (CEC)",
            "enfoque": "Economía, finanzas, inversiones, PyMEs, mercado de capitales, emprendedores, Oil&Gas, Agro",
            "link": "expoefi.com", "estado": "Realizado"
        },
        {
            "fecha": "18/05/2026", "nombre": "Inicio de Inscripción Programa INNOVA CFI",
            "org": "CFI", "lugar": "Virtual",
            "enfoque": "Startups y PyMEs nacientes · Innovación · Inversión de riesgo en Argentina",
            "link": "https://innova.cfi.org.ar/", "estado": "Realizado"
        },
        {
            "fecha": "26/05/2026", "nombre": "Venture Capital World Summit",
            "org": "Regus / Global", "lugar": "Buenos Aires",
            "enfoque": "Inversión ángel y capital de riesgo. Clave para escalar proyectos con capital privado.",
            "link": "https://vcworldsummit.com/", "estado": "Realizado"
        },
        {
            "fecha": "02/06/2026", "nombre": "BNA Conecta",
            "org": "BNA", "lugar": "Trelew – MEF",
            "enfoque": "Marketplace del BNA – líneas de crédito para MiPyMEs",
            "link": "", "estado": "Realizado"
        },
        {
            "fecha": "03/06/2026", "nombre": "Argentina Carbon Forum",
            "org": "Varios", "lugar": "Bolsa de Comercio",
            "enfoque": "Activos digitales, Fintech y financiamiento sostenible para la descarbonización",
            "link": "https://www.argentinacarbon.com/", "estado": "Realizado"
        },
        {
            "fecha": "09/06/2026", "nombre": "Tercer Foro Federal de Garantías",
            "org": "FONRED", "lugar": "San Juan",
            "enfoque": "Garantías y acceso al financiamiento PyME",
            "link": "https://fonred.com.ar/", "estado": "Próximo"
        },
        {
            "fecha": "12/06/2026", "nombre": "Presentación del Sello – Cultura Chubut",
            "org": "Cultura Chubut", "lugar": "Rawson",
            "enfoque": "Divulgación del Sello",
            "link": "", "estado": "Próximo"
        },
        {
            "fecha": "26/06/2026", "nombre": "Cierre de Inscripción INNOVA CFI – Ventana 1",
            "org": "CFI", "lugar": "Virtual",
            "enfoque": "Startups y PyMEs · Ventanas cada 4 meses",
            "link": "https://innova.cfi.org.ar/", "estado": "Próximo"
        },
        {
            "fecha": "29/06/2026", "nombre": "Congreso Nacional PyME",
            "org": "CASFOG", "lugar": "Centro de Convenciones",
            "enfoque": "Acceso al financiamiento PyME",
            "link": "casfog.com.ar", "estado": "Próximo"
        },
        {
            "fecha": "31/07/2026", "nombre": "Cierre de Inscripción – Concurso Emprendimiento Argentino 2026",
            "org": "Ministerio de Economía – Ecosistema Emprendedor", "lugar": "Nacional (online)",
            "enfoque": "Concurso federal para emprendimientos. Inscripción desde el 2 de junio.",
            "link": "https://www.argentina.gob.ar/economia/industria-comercio-y-pyme/pymes/ecosistema-emprendedor/concurso-emprendimiento",
            "estado": "Próximo"
        },
        {
            "fecha": "27/08/2026", "nombre": "eCommerce Day Argentina 2026",
            "org": "CACE", "lugar": "CABA – Centro de Convenciones (CEC)",
            "enfoque": "IA como motor del comercio unificado y crecimiento escalable",
            "link": "https://ecommerceday.org.ar/2026/", "estado": "Próximo"
        },
        {
            "fecha": "17/09/2026", "nombre": "XXIX Foro Iberoamericano de Garantías – REGAR",
            "org": "REGAR", "lugar": "Arequipa, Perú",
            "enfoque": "Transformación de los sistemas de garantías en entorno global cambiante",
            "link": "https://redegarantias.com/foro-peru-inicio/", "estado": "Próximo"
        },
        {
            "fecha": "01/12/2026", "nombre": "Foro Argentino de Inversiones – ARCAP",
            "org": "ARCAP", "lugar": "Palacio Libertad (ex CCK), CABA",
            "enfoque": "Venture Capital, Private Equity, emprendimiento e innovación en Argentina con proyección global",
            "link": "https://arcap.org/", "estado": "Próximo"
        },
    ]

    filtro_estado = st.radio("Mostrar:", ["Todos", "Solo próximos", "Solo realizados"], horizontal=True)

    meses_es = {1:"Ene",2:"Feb",3:"Mar",4:"Abr",5:"May",6:"Jun",7:"Jul",8:"Ago",9:"Sep",10:"Oct",11:"Nov",12:"Dic"}

    for ev in eventos:
        if filtro_estado == "Solo próximos" and ev["estado"] != "Próximo":
            continue
        if filtro_estado == "Solo realizados" and ev["estado"] != "Realizado":
            continue

        partes = ev["fecha"].split("/")
        dia = partes[0].lstrip("0") or "1"
        mes = meses_es.get(int(partes[1]), "")
        badge = f'<span class="badge-realizado">✓ Realizado</span>' if ev["estado"] == "Realizado" else f'<span class="badge-proximo">● Próximo</span>'
        link_html = f' · <a href="{ev["link"]}" target="_blank" style="color:#5894A7;font-size:11px;">Más info</a>' if ev["link"] else ""

        st.markdown(f"""
        <div class="evento-card">
            <div class="evento-fecha-box">
                <div class="evento-dia">{dia}</div>
                <div class="evento-mes">{mes}</div>
            </div>
            <div style="flex:1;">
                <div class="evento-nombre">{ev['nombre']}</div>
                <div class="evento-org">{ev['org']}</div>
                <div class="evento-lugar">📍 {ev['lugar']}</div>
                <div style="font-size:12px;color:#666;margin-top:4px;">{ev['enfoque']}</div>
                <div style="margin-top:6px;">{badge}{link_html}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer-bar">
    <strong>Dirección de Promoción de las Inversiones</strong> · Dirección General de Comercio · Ministerio de Producción · Provincia del Chubut<br>
    📞 Tel: 2804482606 · ✉️ herramientasfinancieraschubut@gmail.com<br>
    <span style="font-size:11px;">Las líneas pueden modificarse; son de carácter orientativo. Consulte siempre a la entidad correspondiente.</span>
</div>
""", unsafe_allow_html=True)
