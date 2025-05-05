import streamlit as st
from streamlit_monaco import st_monaco
import pandas as pd
import graphviz
import folium
from streamlit_folium import st_folium

st.sidebar.title("Interfaces Lingüísticas en Judeo-Español en Estambul y Español Afro-Ecuatoriano")
opciones = st.sidebar.selectbox("Selecciona la sección:",["Introducción", "Similaridades sociolingüísticas", "Datos", "Rasgos gramaticales compartidos", "Comentarios"] )

if opciones == "Introducción":
    st.markdown(f'<h1 style="font-size: 38px; text-align: center; ">Difícil de conseguir, fácil de perder: Interfaces Lingüísticas en judeo-español de Estambul y español Afro-Ecuatoriano</h1>', unsafe_allow_html=True)
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; ">Romero y Sessarego (2018)</h2>', unsafe_allow_html=True)
    st.markdown("""
        - Se analizan dos dialectos del español: **AES** y **IJS**.
        - Ambos son **L1s** en sus comunidades, pero muestran rasgos típicos de **L2** y español **heredado**.
        - Fenómenos compartidos:
        - a) Sujeto explícito no enfático/contrastivo.
        - b) Nominal empobrecido.
        - c) Concordancia verbal en persona, número y género (**rasgos phi**).
        """)

    st.markdown("### Enfoque teórico")
    st.markdown("""
        - Se propone un **modelo de transmisión por contacto** basado en la **arquitectura modular** de la facultad del lenguaje.
        - Articula teorías de:
        - **Adquisición de segunda lengua (SLA)**.
        - **Atrición de lengua materna (FLA)**.
        """)

    st.markdown("### Aportes del estudio")
    st.markdown("""
        - Estudia dos variedades en contacto **nunca antes comparadas directamente**.
        - Identifica patrones estructurales similares en ambos dialectos.
        - Relaciona fenómenos observados con presiones socioeconómicas y desplazamiento lingüístico.
        - Contribuye a teorías sobre el lenguaje desde una **perspectiva formal y generativa**.
        """)



elif opciones == "Similaridades sociolingüísticas":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Similitudes sociolingüísticas entre AES y IJS</h2>', unsafe_allow_html=True)

    # Crear la tabla de comparación
    data = {
        "Aspecto": [
            "Origen histórico",
            "Ubicación geográfica",
            "Situación sociolingüística",
            "Dominio de uso",
            "Actitudes externas",
            "Transmisión lingüística",
            "Presión del idioma dominante",
            "Cambio generacional",
            "Resultado del contacto lingüístico",
            "Fenómenos paralelos"
        ],
        "AES: español afro-ecuatoriano": [
            "Descendientes de esclavos africanos en plantaciones jesuitas del norte de Ecuador",
            "Variedad afro-hiapánica hablado en el norte de Ecuador",
            "Lengua minoritaria con funciones de identidad comunitaria",
            "Ámbitos familiares, canciones folclóricas",
            "Frecuentemente negativas; bajo valor en el mercado lingüístico",
            "Transmisión doméstica, en declive entre jóvenes",
            "Presión del español prestigioso de las tierras altas (HES) en la educación y el empleo",
            "Cambio hacia la variedad dominante (HES)",
            "Convergencia hacia la variedad dominante (HES)",
            "Rasgos tradicionales del AES coinciden con fenómenos del IJS joven"
        ],
        "IJS: judeo-español de Estambul": [
            "Descendientes de judíos sefardíes expulsados de España en 1492",
            "Hablado por la comunidad sefardí en Estambul (Turquía)",
            "Lengua minoritaria con funciones de identidad comunitaria",
            "Ámbitos religiosos y familiares",
            "Frecuentemente negativas; desplazada por el turco",
            "Transmisión limitada; pérdida en generaciones jóvenes",
            "Imposición del turco en contextos educativos y públicos",
            "Cambio hacia el turco dominante",
            "Divergencia progresiva del judeoespañol tradicional",
            "Rasgos innovadores del IJS coinciden con estructuras del AES tradicional"
        ]
    }

    df = pd.DataFrame(data)

    # Mostrar la tabla en Streamlit
    st.table(df)

elif opciones == "Datos":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Recolección de datos</h2>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Datos del AES</h3>', unsafe_allow_html=True)
    text_4 = """
       - Se realizó entrevistas sociolingüísticas durante el invierno de 2011-2012.

       - Participaron 50 hablantes nativos del AES.

       - Los participantes residían en 9 pueblos del Valle del Chota (Imbabura y Carchi): Tumbabiro, Carpuela, Chota, Santiago, Chalguayacu, Chamanal, Concepción, Caldera y Cuajara.

       - Ninguno de los informantes hablaba otras lenguas regionales como el quichua.
    """
    st.markdown(text_4)

    # Función para crear un mapa con marcadores sin descripción
    def crear_mapa(locations, center_coords, zoom_start=9, map_title="Mapa del Valle del Chota (Imbabura y Carchi)"):
        # Crear mapa centrado en las coordenadas especificadas
        m = folium.Map(location=center_coords, zoom_start=zoom_start, tiles='CartoDB positron')

        # Añadir los marcadores al mapa sin descripciones
        for name, coords in locations.items():
            folium.Marker(location=coords, popup=f"<b>{name}</b>").add_to(m)

        # Mostrar el mapa en Streamlit
        st.title(map_title)
        st_data = st_folium(m, width=700, height=500)

    # Coordenadas de los pueblos del Valle del Chota
    locations = {
        "Tumbabiro": (0.4613, -78.1922),
        "Carpuela": (0.4399, -77.9972),
        "Chota": (0.4551, -77.9958),
        "Santiago": (0.3894, -78.1281),
        "Chalguayacu": (0.4260, -77.9625),
        "Concepción": (0.6031, -78.1292),
        "Caldera": (0.3900, -78.1160),
        "Cuajara": (0.6333, -78.1628)
    }

    # Llamar a la función para crear y mostrar el mapa
    crear_mapa(locations, center_coords=[0.5, -78.0])
    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Datos del IJS</h3>', unsafe_allow_html=True)
    text_5 = """
       - Se realizó entrevistas sociolingüísticas en 2007.

       - Participaron más de 60 hablantes.

       - Todos los informantes residían en Estambul.

       - Todos los participantes eran bilingües: hablaban turco local e IJS, aprendido en casa.
    """
    st.markdown(text_5)

    st.markdown(f'<h3 style="font-size: 30px; text-align: center; ">Metodología común en ambas comunidades</h3>', unsafe_allow_html=True)
    text_6 = """

       - Las entrevistas se desarrollaron en tono libre, permitiendo a los hablantes hablar de temas de su interés.

       - Se aplicó el principio de desplazamiento tangencial para fomentar narrativas espontáneas.

       - Se buscó minimizar la paradoja del observador y capturar datos naturales del habla vernácula.
    """
    st.markdown(text_6)

elif opciones == "Rasgos gramaticales compartidos":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Rasgos gramaticales compartidos</h2>', unsafe_allow_html=True)

    st.markdown("## Hallazgos principales del análisis comparativo")
    st.markdown("""
    - El **AES tradicional** y el **IJS contemporáneo** presentan similitudes morfosintácticas notables.
    - Estas características **se apartan de las variedades nativas típicas del español**.

    **Fenómenos observados:**
    - Uso excesivo de **pronombres sujeto**.
    - **Reducción de la morfología flexiva** en:
    - El dominio **nominal**.
    - El dominio **verbal**.
    """)

    st.markdown("### Uso de pronombres sujeto explícitos, no enfáticos y no contrastivos")
    st.markdown("""
    - Ejemplo (1): AES
                
        a. **Nosotro** somos de acá porque **nosotro** vivimo acá desde chico.
                 
        b. **Yo** iba a la ciudad y **yo** vendía los producto. 
    - Ejemplo (2): IJS
                
        a. **Yo** digo ke **yo** la kiero a mi ermuera ke está ermoza. 
           (Yo digo que yo la quiero a mi nuera que está hermosa.)
                
        b. **Tú** merkas los gazetos ke **tú** meldas el día entero. 
           (Tú compras los periódicos que tú lees el día entero.)
    """)


elif opciones == "Comentarios":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Comentarios</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    - A lo largo de la lectura eventualmente meten en el mismo saco a las lenguas caribeñas, lo que me hace mucho sentido 
     (¿creo que esta construcción 'hacer sentido' es calco del inglés?), por lo mismo que también tienen un influjo fuerte 
      de lenguas africanas en el español. Asimismo, también se habla de lenguas de herencia, como el español en EEUU. 
      Entonces, una vez más, me deja preguntándome por qué insistir en la comparación entre estas dos variantes. 
      Además, otro detalle que me parece importante resaltar: la comparativa es entre el EAE tradicional y el JEE moderno. 
      No hay procesos paralelos, sino más bien opuestos... Pienso que le han dado una explicación de formación histórica al EAE, 
      que ya se está perdiendo en nuevas generaciones, pero que para el JEE está en un punto de aparición por el contacto con el turco. 
      Ese punto, en todo caso, queda abandonado y ambas variantes son presentadas realmente como sorprendentemente paralelas; 
      me parece a mí que el paralelismo se debe a un proceso, que ellos mismos defienden, no exclusivo de ambas —porque lo señalan 
      para explicar también procesos en lenguas de herencia y otras variedades de español caribeño— y llevado a cabo en distintos 
      momentos históricos. Sumémosle a esto el hecho de que es un estudio generativista, que apunta a comprender el funcionamiento 
      universal del lenguaje a nivel abstracto: ¿cuál es el punto de la insistencia en la comparación de estas dos variantes? 
                
    - ¿Cómo se manifiesta concretamente la transferencia de estructuras sintácticas? ¿Existen casos de calcos semánticos 
    sutiles que van más allá del simple préstamo léxico?
                
     """)
    
    

