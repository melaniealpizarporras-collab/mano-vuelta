import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Mano Vuelta", page_icon="🤝", layout="wide")
BASE=Path(__file__).parent

st.markdown("""
<style>
.stApp{background:#FCFBF7}.block-container{padding-top:1.4rem;max-width:1450px}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#0C432F,#073524)}
[data-testid="stSidebar"] *{color:#F7FBF8}
h1,h2,h3{color:#163C2D}
.hero{background:linear-gradient(115deg,#123F2C,#1D6346 60%,#658866);padding:42px;border-radius:24px;color:white;margin-bottom:20px}
.hero h1{color:white;font-size:3rem;line-height:1.05}.hero p{font-size:1.08rem;max-width:760px;color:#EDF6EF}
.card,.challenge{background:white;border:1px solid #E7E6DF;border-radius:18px;padding:18px;margin-bottom:12px;box-shadow:0 4px 18px rgba(25,50,35,.045)}
.tag{display:inline-block;background:#EEF5EF;color:#245B3D;padding:5px 9px;border-radius:999px;font-size:.78rem;font-weight:600;margin-right:4px}
.orange{background:#FFF0E8;color:#A94F2C}.muted{color:#69756E;font-size:.92rem}
.axis1{border-top:5px solid #2F8F55}.axis2{border-top:5px solid #4779D8}.axis3{border-top:5px solid #D8753F}.axis4{border-top:5px solid #8157C7}.axis5{border-top:5px solid #D05A7A}
div[data-testid="stMetric"]{background:white;border:1px solid #E8E7E1;padding:14px;border-radius:16px}
.stButton>button{border-radius:10px;font-weight:650}
</style>""",unsafe_allow_html=True)

if "applications" not in st.session_state: st.session_state.applications=[]
if "hours_returned" not in st.session_state: st.session_state.hours_returned=126
if "new_challenges" not in st.session_state: st.session_state.new_challenges=[]
if "participants" not in st.session_state:
    st.session_state.participants=[
      {"Nombre":"Sofía Ramírez","Cantón":"Pérez Zeledón","Provincia":"San José","lat":9.3547,"lon":-83.6348,"Retos":3,"Horas":78},
      {"Nombre":"Andrés Mora","Cantón":"San Carlos","Provincia":"Alajuela","lat":10.3238,"lon":-84.4271,"Retos":2,"Horas":44},
      {"Nombre":"Valeria Solís","Cantón":"Cartago","Provincia":"Cartago","lat":9.8644,"lon":-83.9194,"Retos":2,"Horas":51},
      {"Nombre":"Diego Rojas","Cantón":"Liberia","Provincia":"Guanacaste","lat":10.6346,"lon":-85.4404,"Retos":1,"Horas":26},
      {"Nombre":"Mariana Vega","Cantón":"Limón","Provincia":"Limón","lat":9.9913,"lon":-83.0415,"Retos":2,"Horas":39},
      {"Nombre":"José Arias","Cantón":"Puntarenas","Provincia":"Puntarenas","lat":9.9763,"lon":-84.8384,"Retos":1,"Horas":20},
      {"Nombre":"Daniela Chaves","Cantón":"Heredia","Provincia":"Heredia","lat":10.0024,"lon":-84.1165,"Retos":2,"Horas":36},
    ]

BASE_CHALLENGES=[
 {"Código":"MV-01","Reto":"Optimizar la separación y registro de residuos","Organización":"EcoBrunca","Área":"Ambiente","Cantón":"Pérez Zeledón","Provincia":"San José","Cupos":4,"Ocupados":1,"Competencias":"Excel · residuos · análisis","Estado":"Disponible","Impacto":"Ambiental","Horas":40},
 {"Código":"MV-02","Reto":"Digitalizar el control de inventario","Organización":"CoopeValle","Área":"Tecnología","Cantón":"Pérez Zeledón","Provincia":"San José","Cupos":4,"Ocupados":2,"Competencias":"Excel · procesos · innovación","Estado":"Disponible","Impacto":"Económico","Horas":36},
 {"Código":"MV-03","Reto":"Estrategia de comunicación para mercado local","Organización":"Mercado Brunca","Área":"Comunicación","Cantón":"San Isidro","Provincia":"San José","Cupos":4,"Ocupados":2,"Competencias":"Canva · marketing · comunicación","Estado":"Disponible","Impacto":"Social","Horas":32},
 {"Código":"MV-04","Reto":"Mapear oportunidades de turismo rural","Organización":"Ruta PZ","Área":"Comunidad","Cantón":"Pérez Zeledón","Provincia":"San José","Cupos":4,"Ocupados":4,"Competencias":"GIS · investigación · territorio","Estado":"En ejecución","Impacto":"Territorial","Horas":48},
 {"Código":"MV-05","Reto":"Mejorar seguimiento de pedidos y entregas","Organización":"AgroSur","Área":"Administración","Cantón":"Buenos Aires","Provincia":"Puntarenas","Cupos":4,"Ocupados":4,"Competencias":"Procesos · Excel · logística","Estado":"En ejecución","Impacto":"Económico","Horas":44},
 {"Código":"MV-06","Reto":"Cápsula de alfabetización digital","Organización":"Red Joven","Área":"Formación","Cantón":"Pérez Zeledón","Provincia":"San José","Cupos":4,"Ocupados":3,"Competencias":"Facilitación · tecnología","Estado":"Disponible","Impacto":"Educativo","Horas":30},
]

def challenges():
    return pd.DataFrame(BASE_CHALLENGES+st.session_state.new_challenges)

with st.sidebar:
    st.image(str(BASE/"assets"/"logo.svg"),width=220)
    st.caption("Piloto territorial · Costa Rica")
    page=st.radio("",["🏠 Inicio","🧩 Mural de Retos","👥 Mi Cuadrilla","🪪 Mi Mano","🤝 Banco de Horas","🎓 Formación","🗺️ Mapa","📊 Impacto","🏢 Empresas","🧭 Coordinación"])
    st.divider(); st.markdown("**Sofía Ramírez**"); st.caption("Joven · Pérez Zeledón")

df=challenges(); people=pd.DataFrame(st.session_state.participants)

if page=="🏠 Inicio":
    st.markdown("""<div class="hero"><h1>Una oportunidad hoy,<br>un mejor territorio mañana.</h1><p>Conectamos jóvenes, empresas y comunidades a través de retos reales que generan experiencia comprobable, capacidades y desarrollo territorial.</p></div>""",unsafe_allow_html=True)
    a,b,c,d=st.columns(4); a.metric("Retos activos",len(df)); b.metric("Jóvenes",len(people)); c.metric("Organizaciones",df["Organización"].nunique()); d.metric("Horas movilizadas",int(df["Horas"].sum()))
    st.subheader("¿Cómo funciona?")
    for col,title,txt in zip(st.columns(4),["1 · Encuentra","2 · Aprende","3 · Demuestra","4 · Devuelve"],["Elegí un reto real.","Recibí mentoría y formación.","Generá evidencia verificable.","Ayudá a la siguiente cuadrilla."]):
        col.markdown('<div class="card"><h3>'+title+'</h3><p class="muted">'+txt+'</p></div>',unsafe_allow_html=True)

elif page=="🧩 Mural de Retos":
    st.title("Mural de Retos"); st.caption("Explorá oportunidades reales en tu territorio.")
    c1,c2,c3=st.columns([2,1,1])
    q=c1.text_input("Buscar",placeholder="Reto, organización o competencia...")
    area=c2.selectbox("Área",["Todas"]+sorted(df["Área"].unique().tolist()))
    prov=c3.selectbox("Provincia",["Toda Costa Rica"]+sorted(df["Provincia"].unique().tolist()))
    view=df.copy()
    if q: view=view[view.astype(str).apply(lambda r:r.str.contains(q,case=False).any(),axis=1)]
    if area!="Todas": view=view[view["Área"]==area]
    if prov!="Toda Costa Rica": view=view[view["Provincia"]==prov]
    for _,r in view.iterrows():
        left,right=st.columns([5,1])
        available=max(int(r["Cupos"]-r["Ocupados"]),0)
        left.markdown('<div class="challenge"><span class="tag">'+str(r["Área"])+'</span><span class="tag orange">'+str(r["Impacto"])+'</span><h3>'+str(r["Reto"])+'</h3><p class="muted">🏢 '+str(r["Organización"])+' · 📍 '+str(r["Cantón"])+', '+str(r["Provincia"])+' · 👥 '+str(available)+' cupos</p><b>Competencias:</b> '+str(r["Competencias"])+'</div>',unsafe_allow_html=True)
        with right:
            if available>0 and st.button("Postularme",key="p"+str(r["Código"]),type="primary"):
                if r["Código"] not in st.session_state.applications: st.session_state.applications.append(r["Código"])
                st.success("Registrada")

elif page=="👥 Mi Cuadrilla":
    st.title("Mi Cuadrilla"); st.caption("MV-04 · Mapeo de oportunidades de turismo rural")
    a,b,c=st.columns(3); a.metric("Integrantes","4/4"); b.metric("Semana","3 de 4"); c.metric("Avance","72%")
    st.progress(.72)
    st.markdown('<div class="card"><h3>Equipo</h3><p>Sofía · Andrés · Valeria · Diego</p><b>Mentor:</b> Daniel V. · Ruta PZ<br><br><b>Próximo hito:</b> validación territorial del mapa.</div>',unsafe_allow_html=True)
    st.text_area("Bitácora","Levantamiento inicial completado. Pendiente validación con la organización.")

elif page=="🪪 Mi Mano":
    st.title("Perfil del joven"); st.subheader("Sofía Ramírez"); st.caption("📍 Pérez Zeledón, San José")
    a,b,c,d=st.columns(4); a.metric("Retos",3); b.metric("Horas",78); c.metric("Evidencias",2); d.metric("Competencias",5)
    st.markdown('<div class="card"><h3>Sobre mí</h3><p>Interés en sostenibilidad, análisis de datos, trabajo en equipo y desarrollo territorial.</p></div>',unsafe_allow_html=True)
    port=pd.DataFrame([["Diagnóstico de residuos","EcoBrunca","Verificado",32],["Inventario digital","CoopeValle","Verificado",28],["Mapeo turístico","Ruta PZ","En ejecución",18]],columns=["Reto","Organización","Estado","Horas"])
    st.dataframe(port,use_container_width=True,hide_index=True)

elif page=="🤝 Banco de Horas":
    st.title("Banco de Horas"); st.caption("Hoy recibís, mañana devolvés.")
    a,b,c=st.columns(3); a.metric("Horas recibidas",78); b.metric("Horas devueltas",18); c.metric("Balance",60)
    st.progress(18/78,text="23% de las horas recibidas ya fueron devueltas")
    with st.form("hours"):
        typ=st.selectbox("Tipo",["Mentoría","Apoyo técnico","Visita","Cápsula entre pares"]); hrs=st.number_input("Horas",1,40,2)
        if st.form_submit_button("Registrar aporte"): st.session_state.hours_returned+=int(hrs); st.success("Aporte registrado")

elif page=="🎓 Formación":
    st.title("Formación"); st.caption("Cápsulas cortas vinculadas con retos reales.")
    for x in ["Excel para análisis y seguimiento","Comunicación efectiva","Introducción a GIS y levantamiento territorial"]:
        st.markdown('<div class="card"><span class="tag">Disponible</span><h3>'+x+'</h3><p class="muted">Formación asociada a necesidades detectadas en los retos.</p></div>',unsafe_allow_html=True)

elif page=="🗺️ Mapa":
    st.title("Mapa de participantes"); st.caption("Cada participante registrado alimenta automáticamente la visualización territorial.")
    t1,t2=st.tabs(["Mapa","Agregar participante"])
    with t1:
        st.map(people,latitude="lat",longitude="lon",size=90,zoom=6)
        st.dataframe(people[["Nombre","Cantón","Provincia","Retos","Horas"]],use_container_width=True,hide_index=True)
    with t2:
        st.info("En este prototipo las coordenadas se ingresan manualmente para evitar depender de servicios externos.")
        with st.form("person"):
            name=st.text_input("Nombre"); canton=st.text_input("Cantón")
            province=st.selectbox("Provincia",["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"])
            lat=st.number_input("Latitud",value=9.3547,format="%.5f"); lon=st.number_input("Longitud",value=-83.6348,format="%.5f")
            if st.form_submit_button("Agregar al mapa"):
                st.session_state.participants.append({"Nombre":name or "Participante","Cantón":canton or "Por definir","Provincia":province,"lat":lat,"lon":lon,"Retos":0,"Horas":0}); st.success("Agregado. Abrí la pestaña Mapa.")

elif page=="📊 Impacto":
    st.title("Dashboard de Impacto"); st.caption("Los indicadores se recalculan desde los registros de la plataforma.")
    orgs=df["Organización"].nunique(); youth=len(people)
    top=st.columns(7)
    vals=[(youth,"Jóvenes"),(len(df),"Retos"),(orgs,"Organizaciones"),(9,"Portafolios"),(5,"Ofertas"),(2,"Permanencias"),(st.session_state.hours_returned,"Horas devueltas")]
    for col,(v,l) in zip(top,vals): col.metric(l,v)
    st.subheader("Indicadores por eje temático")
    axes=[
      ("axis1","🌿 Ambiental",[(len(df[df.Impacto=="Ambiental"]),"Retos ambientales"),(int(df[df.Impacto=="Ambiental"]["Horas"].sum()),"Horas movilizadas"),(df[df.Impacto=="Ambiental"]["Organización"].nunique(),"Organizaciones")]),
      ("axis2","💼 Económico",[(len(df[df.Impacto=="Económico"]),"Retos productivos"),(5,"Ofertas registradas"),(2,"Permanencias")]),
      ("axis3","👥 Social",[(youth,"Jóvenes"),(people["Cantón"].nunique(),"Cantones de origen"),(st.session_state.hours_returned,"Horas devueltas")]),
      ("axis4","🎓 Educativo",[(len(df[df.Impacto=="Educativo"]),"Retos formativos"),(3,"Cápsulas"),(int(people["Retos"].sum()),"Experiencias")]),
      ("axis5","📍 Territorial",[(df["Cantón"].nunique(),"Cantones con retos"),(df["Provincia"].nunique(),"Provincias"),(orgs,"Organizaciones locales")])]
    for col,(css,title,items) in zip(st.columns(5),axes):
        h='<div class="card '+css+'"><h3>'+title+'</h3>'
        for v,l in items: h+='<p><b style="font-size:1.3rem">'+str(v)+'</b><br><span class="muted">'+l+'</span></p>'
        col.markdown(h+'</div>',unsafe_allow_html=True)
    st.subheader("Meta del piloto vs. registro")
    k=pd.DataFrame({"Indicador":["Organizaciones","Retos","Jóvenes","Portafolios","Ofertas","Permanencias","Horas devueltas"],"Meta":[10,18,24,20,15,12,300],"Registro":[orgs,len(df),youth,9,5,2,st.session_state.hours_returned]})
    k["Cumplimiento %"]=(k.Registro/k.Meta*100).clip(upper=100).round(1)
    st.dataframe(k,use_container_width=True,hide_index=True); st.bar_chart(k.set_index("Indicador")[["Meta","Registro"]])
    st.warning("Los registros precargados son ficticios para demostrar la plataforma; las metas corresponden al diseño del piloto.")

elif page=="🏢 Empresas":
    st.title("Portal de Organizaciones")
    tab1,tab2=st.tabs(["Publicar reto","Retos registrados"])
    with tab1:
        with st.form("new"):
            org=st.text_input("Organización"); reto=st.text_input("Problema / reto real")
            c1,c2=st.columns(2); area=c1.selectbox("Área",["Ambiente","Tecnología","Comunicación","Administración","Comunidad","Formación"]); impact=c2.selectbox("Eje de impacto",["Ambiental","Económico","Social","Educativo","Territorial"])
            canton=st.text_input("Cantón","Pérez Zeledón"); province=st.selectbox("Provincia",["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"])
            skills=st.text_input("Competencias"); mentor=st.text_input("Mentor/a")
            if st.form_submit_button("Publicar reto"):
                code="MV-"+str(len(df)+1).zfill(2)
                st.session_state.new_challenges.append({"Código":code,"Reto":reto or "Nuevo reto","Organización":org or "Organización demo","Área":area,"Cantón":canton,"Provincia":province,"Cupos":4,"Ocupados":0,"Competencias":skills or "Por definir","Estado":"Disponible","Impacto":impact,"Horas":32})
                st.success(code+" publicado: ya alimenta el Mural y el Dashboard.")
    with tab2: st.dataframe(df,use_container_width=True,hide_index=True)

elif page=="🧭 Coordinación":
    st.title("Centro de Coordinación")
    controls=pd.DataFrame([["Retos verificables","Parcial","Alta"],["Mentores","Cumple","Media"],["Capacidad formativa","Pendiente","Alta"],["Barreras de acceso","Parcial","Alta"],["Recursos","Pendiente","Crítica"],["Protección de datos","Cumple","Alta"]],columns=["Condición","Estado","Prioridad"])
    st.dataframe(controls,use_container_width=True,hide_index=True); st.error("Decisión demo: VALIDAR / AJUSTAR antes de escalar.")

st.divider(); st.caption("Mano Vuelta · Prototipo UINNOVA CONARE · Datos precargados ficticios para demostración.")
