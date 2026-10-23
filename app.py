
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Mano Vuelta", page_icon="🤝", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1.4rem; padding-bottom: 3rem;}
div[data-testid="stMetric"] {
    background: #F4F8F2; border: 1px solid #D7E5D1; padding: 14px;
    border-radius: 14px;
}
.mv-card {
    border:1px solid #D9E4D5; border-radius:16px; padding:18px;
    margin-bottom:14px; background:#FBFDF9;
}
.mv-badge {display:inline-block; padding:4px 9px; border-radius:10px;
    background:#E8F3E3; margin-right:5px; font-size:0.86rem;}
.small {color:#5f6b61; font-size:.92rem;}
</style>
""", unsafe_allow_html=True)

if "applications" not in st.session_state:
    st.session_state.applications = []
if "hours" not in st.session_state:
    st.session_state.hours = 126
if "new_challenges" not in st.session_state:
    st.session_state.new_challenges = []

BASE_CHALLENGES = [
    {"Código":"MV-01","Reto":"Optimizar la separación y registro de residuos","Organización":"EcoBrunca",
     "Área":"Gestión ambiental","Duración":"4 semanas","Cupos":3,"Competencias":"Excel · residuos · análisis de datos",
     "Mentor":"Laura M.","Estado":"Disponible","Progreso":0},
    {"Código":"MV-02","Reto":"Digitalizar el control de inventario de una pyme","Organización":"CoopeValle",
     "Área":"Transformación digital","Duración":"4 semanas","Cupos":2,"Competencias":"Excel · procesos · organización",
     "Mentor":"Carlos R.","Estado":"Disponible","Progreso":0},
    {"Código":"MV-03","Reto":"Diseñar una campaña para atraer clientes jóvenes","Organización":"Mercado Brunca",
     "Área":"Comunicación","Duración":"4 semanas","Cupos":1,"Competencias":"Canva · redes · comunicación",
     "Mentor":"Andrea S.","Estado":"Disponible","Progreso":0},
    {"Código":"MV-04","Reto":"Mapear oportunidades de turismo rural local","Organización":"Ruta PZ",
     "Área":"Turismo","Duración":"4 semanas","Cupos":4,"Competencias":"Investigación · GIS · comunicación",
     "Mentor":"Daniel V.","Estado":"Disponible","Progreso":0},
    {"Código":"MV-05","Reto":"Mejorar el seguimiento de pedidos y entregas","Organización":"AgroSur",
     "Área":"Operaciones","Duración":"4 semanas","Cupos":0,"Competencias":"Procesos · Excel · logística",
     "Mentor":"María J.","Estado":"En ejecución","Progreso":65},
]

PORTFOLIO = [
    {"Reto":"Diagnóstico de residuos","Organización":"EcoBrunca","Estado":"Verificado","Horas":32,"Competencias":"Análisis · Excel · sostenibilidad"},
    {"Reto":"Inventario digital","Organización":"CoopeValle","Estado":"Verificado","Horas":28,"Competencias":"Procesos · Excel"},
    {"Reto":"Mapeo turístico","Organización":"Ruta PZ","Estado":"En ejecución","Horas":18,"Competencias":"GIS · investigación"},
]

def challenges_df():
    return pd.DataFrame(BASE_CHALLENGES + st.session_state.new_challenges)

st.sidebar.title("🤝 Mano Vuelta")
st.sidebar.caption("Talento que se demuestra haciendo")
page = st.sidebar.radio("Navegación", [
    "🏠 Inicio","📌 Mural de Retos","👥 Mi Cuadrilla","📁 Mi Mano",
    "🤝 Banco de Horas","🏢 Portal Empresa","📊 Impacto","🧭 Coordinación"
])
st.sidebar.divider()
st.sidebar.caption("Prototipo UINNOVA · Piloto Pérez Zeledón")

df = challenges_df()

if page == "🏠 Inicio":
    st.title("Mano Vuelta")
    st.subheader("Conectamos retos reales con talento joven.")
    st.write("Las organizaciones publican problemas concretos; cuadrillas de jóvenes los resuelven con mentoría, formación breve y evidencia verificable.")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Jóvenes", "24", "Meta piloto")
    c2.metric("Retos", "18", "Meta piloto")
    c3.metric("Organizaciones", "10", "Meta piloto")
    c4.metric("Horas devueltas", f"{st.session_state.hours}", "de 300")
    st.info("Demo interactiva: entra al Mural, postúlate a un reto, revisa Mi Mano y luego cambia al Portal Empresa.")
    st.markdown("### ¿Cómo funciona?")
    st.write("**Reto publicado → Cuadrilla → Cápsula y práctica → Evidencia firmada → Portafolio Mi Mano → Oportunidad → Banco de Horas**")
    st.progress(0.42, text="Avance ilustrativo del piloto: 42 %")

elif page == "📌 Mural de Retos":
    st.title("📌 Mural de Retos")
    st.write("Explora problemas reales de organizaciones de Pérez Zeledón.")
    areas = ["Todas"] + sorted(df["Área"].unique().tolist())
    area = st.selectbox("Filtrar por área", areas)
    view = df if area == "Todas" else df[df["Área"] == area]
    for _, r in view.iterrows():
        st.markdown(f"""<div class="mv-card">
        <b>{r['Código']} · {r['Reto']}</b><br>
        <span class="small">{r['Organización']} · {r['Duración']} · Mentoría: {r['Mentor']}</span><br><br>
        <span class="mv-badge">{r['Área']}</span>
        <span class="mv-badge">{r['Cupos']} cupos</span>
        <p><b>Competencias:</b> {r['Competencias']}</p>
        </div>""", unsafe_allow_html=True)
        if r["Cupos"] > 0:
            if st.button("Quiero participar", key=f"apply_{r['Código']}"):
                if r["Código"] not in st.session_state.applications:
                    st.session_state.applications.append(r["Código"])
                st.success(f"Postulación registrada para {r['Código']} (demo).")
        else:
            st.caption("Cuadrilla completa / reto en ejecución.")

elif page == "👥 Mi Cuadrilla":
    st.title("👥 Mi Cuadrilla")
    st.caption("Reto activo: MV-04 · Mapeo de oportunidades de turismo rural")
    c1,c2 = st.columns([1,2])
    with c1:
        st.metric("Integrantes", "4/4")
        st.metric("Semana", "3 de 4")
        st.metric("Avance", "72 %")
    with c2:
        st.write("**Integrantes:** Sofía · Andrés · Valeria · Diego")
        st.write("**Mentor:** Daniel V. · Ruta PZ")
        st.write("**Cápsula asociada:** levantamiento de información y visualización territorial")
        st.progress(0.72)
        st.text_area("Bitácora de avance", "Se completó el levantamiento inicial y se están validando los puntos con la organización.")
        if st.button("Guardar avance"):
            st.success("Avance guardado en el prototipo.")

elif page == "📁 Mi Mano":
    st.title("📁 Portafolio Mi Mano")
    st.write("**Sofía Rodríguez** · Pérez Zeledón")
    a,b,c = st.columns(3)
    a.metric("Retos", "3")
    b.metric("Experiencia demostrada", "78 h")
    c.metric("Evidencias verificadas", "2")
    st.dataframe(pd.DataFrame(PORTFOLIO), use_container_width=True, hide_index=True)
    st.success("Las evidencias verificadas pueden mostrarse como experiencia práctica ante futuras organizaciones.")

elif page == "🤝 Banco de Horas":
    st.title("🤝 Banco de Horas")
    a,b,c = st.columns(3)
    a.metric("Horas recibidas", "78")
    b.metric("Horas devueltas", "18")
    c.metric("Balance solidario", "60")
    st.write("Devuelve parte del apoyo recibido mediante mentoría, visitas, apoyo a otra cuadrilla u otras contribuciones validadas.")
    with st.form("hours"):
        qty = st.number_input("Horas a devolver", min_value=1, max_value=40, value=2)
        kind = st.selectbox("Tipo de aporte", ["Mentoría","Apoyo técnico","Visita","Cápsula entre pares"])
        if st.form_submit_button("Registrar aporte"):
            st.session_state.hours += int(qty)
            st.success(f"Se registraron {qty} horas de {kind.lower()}.")

elif page == "🏢 Portal Empresa":
    st.title("🏢 Portal de Organización")
    tab1, tab2 = st.tabs(["Publicar reto","Seguimiento"])
    with tab1:
        with st.form("new_challenge"):
            org = st.text_input("Organización", "Organización Demo")
            challenge = st.text_input("Problema / reto")
            area = st.selectbox("Área", ["Gestión ambiental","Transformación digital","Comunicación","Operaciones","Turismo","Otro"])
            skills = st.text_input("Competencias requeridas")
            mentor = st.text_input("Persona mentora")
            slots = st.number_input("Cupos", 1, 4, 4)
            result = st.text_area("Resultado verificable esperado")
            if st.form_submit_button("Publicar reto"):
                code = f"MV-{len(df)+1:02d}"
                st.session_state.new_challenges.append({
                    "Código":code,"Reto":challenge or "Reto de demostración","Organización":org,
                    "Área":area,"Duración":"4 semanas","Cupos":slots,
                    "Competencias":skills or "Por definir","Mentor":mentor or "Por asignar",
                    "Estado":"Disponible","Progreso":0
                })
                st.success(f"{code} publicado correctamente.")
    with tab2:
        st.dataframe(df[["Código","Reto","Estado","Progreso","Mentor"]], use_container_width=True, hide_index=True)
        st.write("**Validación de evidencia final**")
        code = st.selectbox("Reto", df["Código"].tolist())
        verdict = st.selectbox("Resultado", ["Pendiente","Aprobada","Requiere ajustes"])
        if st.button("Registrar validación"):
            st.success(f"Evidencia de {code}: {verdict}.")

elif page == "📊 Impacto":
    st.title("📊 Dashboard de Impacto")
    st.caption("Meta propuesta vs. avance ilustrativo de la demo")
    metrics = pd.DataFrame({
        "Indicador":["Organizaciones","Retos","Jóvenes","Portafolios","Ofertas","Permanencias","Horas devueltas"],
        "Meta":[10,18,24,20,15,12,300],
        "Avance demo":[6,11,18,9,5,2,st.session_state.hours]
    })
    metrics["Cumplimiento %"] = (metrics["Avance demo"]/metrics["Meta"]*100).clip(upper=100).round(1)
    st.dataframe(metrics, use_container_width=True, hide_index=True)
    st.bar_chart(metrics.set_index("Indicador")[["Meta","Avance demo"]])
    st.markdown("### Lectura ejecutiva")
    avg = metrics["Cumplimiento %"].mean()
    st.metric("Cumplimiento promedio de metas", f"{avg:.1f} %")
    st.warning("Los valores de avance son datos ficticios para demostrar el funcionamiento del prototipo; no representan resultados reales del piloto.")

elif page == "🧭 Coordinación":
    st.title("🧭 Centro de Coordinación")
    st.write("Seguimiento de condiciones críticas para decidir si el piloto continúa, ajusta o reprograma.")
    controls = pd.DataFrame([
        ["Retos verificables suficientes","Parcial","Alta","Coordinación","Validar 7 retos adicionales"],
        ["Mentores disponibles","Cumple","Media","Organizaciones","Mantener confirmaciones"],
        ["Capacidad formativa INA/MEP","Pendiente","Alta","Enlace formación","Confirmar oferta y modalidad"],
        ["Barreras de acceso","Parcial","Alta","Coordinación","Validar transporte y conectividad"],
        ["Recursos del piloto","Pendiente","Crítica","Mesa técnica","Confirmar aportes antes de iniciar"],
        ["Protección de datos","Cumple","Alta","Responsable de datos","Mantener acceso restringido"],
    ], columns=["Condición","Estado","Prioridad","Responsable","Próxima acción"])
    st.dataframe(controls, use_container_width=True, hide_index=True)
    st.error("DECISIÓN DEMO: AJUSTAR / VALIDAR antes de escalar.")
    st.write("**Regla:** si faltan retos, mentores, capacidad formativa o recursos esenciales, el inicio debe reprogramarse o redimensionarse.")

st.divider()
st.caption("Mano Vuelta · Prototipo demostrativo UINNOVA CONARE · Los datos de avance mostrados son ficticios para fines de demostración.")
