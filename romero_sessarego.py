import streamlit as st
from streamlit_monaco import st_monaco
import pandas as pd
import graphviz
import folium
from streamlit_folium import st_folium

st.sidebar.title("Interfaces Lingüísticas en Judeo-Español en Estambul y Español Afro-Ecuatoriano")
opciones = st.sidebar.selectbox("Selecciona la sección:",["Introducción", "Similaridades sociolingüísticas", "Datos"] )

if opciones == "Introducción":
    st.markdown(f'<h1 style="font-size: 38px; text-align: center; ">Difícil de conseguir, fácil de perder: Interfaces Lingüísticas en Judeo-Español en Estambul y Español Afro-Ecuatoriano</h1>', unsafe_allow_html=True)
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; ">Romero y Sessarego (2018)</h2>', unsafe_allow_html=True)
    text_1 = """

    """
    st.markdown(text_1)

elif opciones == "Similaridades sociolingüísticas":
    # st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Similitudes sociolingüísticas entre AES y IJS</h2>', unsafe_allow_html=True)

    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Español Afro-Ecuatoriano (AES)</h3>', unsafe_allow_html=True)

    text_2 = """
    📜 Origen histórico:
    
    El EAS es hablado por descendientes de esclavos africanos traídos a las tierras altas de Ecuador durante la época colonial para trabajar en haciendas jesuitas.
    
    🌱 Cambio sociopolítico en 1964:
    
    La reforma agraria liberó a los afroecuatorianos de la servidumbre por deudas, otorgándoles tierras y acceso a la educación.

    🎓 Impacto en la movilidad social:
    
    Se establecieron escuelas en zonas rurales afroecuatorianas y se facilitó el acceso a trabajos en ciudades, promoviendo la movilidad social.

    🔄 Cambio lingüístico:
    
    Estas transformaciones sociales llevaron a una disminución sistemática en el uso del AES en favor del español ecuatoriano de las tierras altas (HES), una variedad con mayor prestigio social.
    
    ⚠️ Situación actual:
    
    Solo unos pocos cientos de afroecuatorianos mayores siguen hablando variantes del AES con rasgos afrohispánicos tradicionales.

    🧒🏽 Generaciones jóvenes:
    
    Los jóvenes afroecuatorianos usan variedades de español altamente influenciadas o prácticamente indistinguibles del HES.
    
    """
    st.markdown(text_2)

    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Judeo-Español en Estambul (IJS)</h3>', unsafe_allow_html=True)
    text_3 = """
        🗺️ Origen histórico:

        Tras la expulsión de los judíos sefardíes de España en 1492, muchos se asentaron en el Imperio Otomano, donde su español evolucionó en varios dialectos, incluido el IJS.
       

        🕌 Protección bajo el sistema zimmi:

        El IJS se mantuvo durante siglos gracias al estatus de zimmi, que permitía autonomía comunitaria en aspectos religiosos, educativos y legales a cambio de un impuesto.
       

        🏛️ Cambio sociolingüístico en el siglo XX:

        Con la fundación de la República Turca en 1929, se impusieron políticas nacionalistas que promovían exclusivamente el uso del turco, incluyendo educación obligatoria en turco y la prohibición de escuelas en otros idiomas.
       

        ✈️ Migración y pérdida de dominios lingüísticos:

        La emigración de sefardíes a países de Europa, América y otros destinos debilitó aún más el uso del IJS en Estambul.

        ⚠️ Lengua en peligro:

        Hoy, el IJS se encuentra en peligro de extinción, con un número de hablantes considerablemente reducido.
        

        👶🏽 Cambio generacional:

        Las generaciones jóvenes de judíos en Estambul muestran una clara preferencia por el turco, y menor competencia en IJS que sus mayores.

        🌍 Influencias modernas:

        Incluso quienes conservan el IJS tienden a acomodarse fonética y léxicamente al español peninsular o latinoamericano por razones comerciales y educativas.
    
        """
    st.markdown(text_3)

    # Crear la tabla de comparación
    data = {
        "Aspecto": [
            "Origen histórico",
            "Ubicación geográfica",
            "Grupo hablante",
            "Situación sociolingüística",
            "Dominio de uso",
            "Actitudes externas",
            "Transmisión lingüística",
            "Vínculo con identidad",
            "Presión del idioma dominante",
            "Cambio generacional",
            "Resultado del contacto lingüístico",
            "Fenómenos paralelos"
        ],
        "AES tradicional": [
            "Descendientes de esclavos africanos en plantaciones jesuitas del norte de Ecuador (Sessarego 2013a)",
            "Valle del Chota, tierras altas del norte de Ecuador",
            "Afroecuatorianos mayores",
            "Lengua minoritaria con funciones de identidad comunitaria",
            "Ámbitos familiares, canciones folclóricas, oralidad local",
            "Frecuentemente negativas; bajo valor en el mercado lingüístico",
            "Transmisión doméstica, en declive entre jóvenes",
            "Asociado a identidad afrodescendiente y prácticas culturales",
            "Presión del español estándar (HES) en educación y empleo",
            "Cambio hacia el español regional y estándar",
            "Convergencia hacia variedades dominantes (HES)",
            "Rasgos tradicionales del AES coinciden con fenómenos del IJS joven"
        ],
        "IJS contemporáneo": [
            "Descendientes de judíos sefardíes expulsados de España en 1492 (Romero 2012)",
            "Estambul, Turquía",
            "Judíos sefardíes jóvenes",
            "Lengua minoritaria con funciones de solidaridad grupal",
            "Ámbitos religiosos, canciones tradicionales, memoria cultural",
            "Frecuentemente negativas; desplazada por el turco",
            "Transmisión limitada; pérdida en generaciones jóvenes",
            "Lengua ligada a identidad sefardí y religiosa",
            "Imposición del turco en contextos educativos y públicos",
            "Cambio hacia el turco dominante",
            "Divergencia progresiva del judeoespañol tradicional",
            "Rasgos innovadores del IJS coinciden con estructuras del AES antiguo"
        ]
    }

    df = pd.DataFrame(data)

    # Mostrar la tabla en Streamlit
    st.table(df)

elif opciones == "Datos":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Recolección de datos</h2>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Datos del AES</h3>', unsafe_allow_html=True)
    text_4 = """
       - Se realizó durante el invierno de 2011-2012.

       - Participaron 50 hablantes nativos del AES.

       - Los participantes residían en 9 pueblos del Valle del Chota (Imbabura y Carchi): Tumbabiro, Carpuela, Chota, Santiago, Chalguayacu, Chamanal, Concepción, Caldera y Cuajara.

       - Ninguno de los informantes hablaba otras lenguas regionales como el quichua.
    """
    st.markdown(text_4)

    # Coordenadas aproximadas de los pueblos del Valle del Chota
    locations = {
        "Tumbabiro": (-0.3693, -78.2325),
        "Carpuela": (0.3783, -78.1133),
        "Chota": (0.3958, -78.1178),
        "Santiago": (0.3894, -78.1281),
        "Chalguayacu": (0.4155, -78.1228),
        "Chamanal": (0.6296, -77.7404),
        "Concepción": (0.8441, -77.9432),
        "Caldera": (0.3900, -78.1160),
        "Cuajara": (0.3974, -78.1206)
    }

    # Crear mapa centrado en el Valle del Chota
    m = folium.Map(location=[0.5, -78.0], zoom_start=9, tiles='CartoDB positron')

    # Añadir los marcadores al mapa
    for name, coords in locations.items():
        folium.Marker(location=coords, popup=name).add_to(m)

    # Mostrar el mapa en Streamlit
    st.title("Mapa del Valle del Chota (Imbabura y Carchi)")
    st_folium(m, width=700, height=500)

    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Datos del IJS</h3>', unsafe_allow_html=True)
    text_5 = """
       - Se realizó en 2007.

       - Participaron más de 60 hablantes.

       - Todos los informantes residían en Estambul.

       - Todos los participantes eran bilingües: hablaban turco local e IJS, aprendido en casa.
    """
    st.markdown(text_5)

    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Metodología común en ambas comunidades</h3>', unsafe_allow_html=True)
    text_6 = """
       - Se usaron entrevistas sociolingüísticas como principal técnica de recolección.

       - Las entrevistas se desarrollaron en tono libre, permitiendo a los hablantes hablar de temas de su interés.

       - Se aplicó el principio de desplazamiento tangencial para fomentar narrativas espontáneas.

       - Se buscó minimizar la paradoja del observador y capturar datos naturalistas del habla vernácula.
    """
    st.markdown(text_6)



