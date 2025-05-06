import streamlit as st
from streamlit_monaco import st_monaco
import pandas as pd
import graphviz
import folium
from streamlit_folium import st_folium

st.sidebar.title("Interfaces Lingüísticas en judeo-español en Estambul y español afro-Eecuatoriano")
opciones = st.sidebar.selectbox("Selecciona la sección:",["Introducción", "Similaridades sociolingüísticas", "Datos", "Rasgos gramaticales compartidos", "Análisis de datos", "La propuesta para las características de AES y IJS", "Comentarios"] )

if opciones == "Introducción":
    st.markdown(f'<h1 style="font-size: 38px; text-align: center; ">Difícil de conseguir, fácil de perder: Interfaces Lingüísticas en judeo-español de Estambul y español afro-ecuatoriano</h1>', unsafe_allow_html=True)
    st.markdown(f'<h2 style="font-size: 30px; text-align: center; ">Romero y Sessarego (2018)</h2>', unsafe_allow_html=True)
    st.markdown("""
        - Se analizan dos dialectos del español: **AES** y **IJS**.
        - Fenómenos compartidos:
        
            a) Sujeto explícito no enfático - no contrastivo.
            
            b) Concordancia nominal empobrecido.
            
            c) Concordancia verbal de persona, número y género (**rasgos phi**).
            
        - Se propone un **modelo de transmisión por contacto** basado en la **arquitectura modular** de la facultad del lenguaje.
            - **Adquisición de la segunda lengua (SLA)**.
            - **Atrición de la lengua materna (FLA)**.
        """)        
    st.markdown("### **Población afroecuatoriana en el 2022**")
    st.image("CENSO 2022.png", caption="Censo 2022 de Ecuador", use_container_width=True)

    st.markdown("### **Población serfadí en el 2021**")
    st.markdown("https://www.publico.es/sociedad/sefardies-largo-camino-vuelta-casa.html")
        


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
            "Cambio generacional"
        ],
        "AES: español afro-ecuatoriano": [
            "Descendientes de esclavos africanos en plantaciones jesuitas del norte de Ecuador",
            "Variedad afro-hiapánica hablado en el norte de Ecuador",
            "Lengua minoritaria con funciones de identidad comunitaria",
            "Ámbitos familiares, canciones folclóricas",
            "Frecuentemente negativas; bajo valor en el mercado lingüístico",
            "Transmisión doméstica, en declive entre jóvenes",
            "Presión del español prestigioso de las tierras altas (HES) en la educación y el empleo",
            "Cambio hacia la variedad dominante (HES)"
        ],
        "IJS: judeo-español de Estambul": [
            "Descendientes de judíos sefardíes expulsados de España en 1492",
            "Hablado por la comunidad sefardí en Estambul (Turquía)",
            "Lengua minoritaria con funciones de identidad comunitaria",
            "Ámbitos religiosos y familiares",
            "Frecuentemente negativas; desplazada por el turco",
            "Transmisión limitada; pérdida en generaciones jóvenes",
            "Imposición del turco en contextos educativos y públicos",
            "Cambio hacia el turco dominante"
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

    # st.markdown("### Hallazgos principales del análisis comparativo")
    st.markdown("""
    - El **AES tradicional** y el **IJS contemporáneo** presentan similitudes morfosintácticas notables.

    **Fenómenos observados:**
    - Uso excesivo de **pronombres sujeto explícitos**.
    - **Reducción de la morfología flexiva** en:
        - El dominio **nominal**.
        - El dominio **verbal**.
    """)
    
    st.markdown("**Estos fenómenos también se encuentran en lenguas afrohispánicas de América y en varios dialectos del español de herencia.**")
    
    data = {
        "Fenómeno": [
            "Uso de pronombres sujeto explícitos", "", "","",
            "Falta de concordancia verbal phi (persona/número)", "", "", "",
            "Falta de concordancia nominal phi (género/número)", "", "", "",
            "Uso de sujetos explícitos (otras variedades)", "", 
            "Falta de concordancia verbal (otras variedades)", "", 
            "Falta de concordancia nominal (otras variedades)", "", 
        ],
        "Variedad": [
            "AES", "", "IJS", "",
            "AES","", "IJS", "",
            "AES", "", "IJS", "",
            "Afroboliviano", "Español de herencia", 
            "Afrocubano", "Bilingüe mexicano en EE.UU.", 
            "Cubano bozal", "Español de herencia", 
        ],
        "Ejemplo": [
            "a. Nosotro somos de acá porque nosotro vivimo acá desde chico.",
            "b. Yo iba a la ciudad y yo vendía los producto.",
            "a. Yo digo ke yo la kiero a mi ermuera ke está ermoza. (Yo digo que yo la quiero a mi nuera que está hermosa.)",
            "b. Tú merkas los gazetos ke tú meldas el día entero. (Tú compras los periódicos que tú lees el día entero.)",

            "a. Ello dijo que iba al campo.",
            "b. Cuando yo tuvo uso de razón.",
            "a. Muestras madres dize ke a moz plaze komidas buenas. (Nuestras madres dicen que a nosotros nos gustan comidas buenas.)",
            "b. Los sivdades muevas es serka de la mar. (Las ciudades nuevas son cerca del mar.)",
            
            "a. Mis hermano joven.",
            "c. Todo la cerveza fría.",
            "a. Muevos novia están kontente. (Las novias nuevas están contentas.)",
            "b. Estos ombre son mansevo. (Estos hombres son jóvenes.)",
            
            "Claro yo como fue chico yo no acorda vela.",
            "Ella vivía con su mamá y ella quería mucho a su abuelita. Y ella le dijo...",
            
            
            "Tú jabla y no conoce.",
            "Yo bailo y come.",
            
            "Gente branco.",
            "Veo a un nariz rojo."
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    st.image("tabla1.png", caption="Variación dialectal en las tasas generales de expresión del sujeto", use_container_width=True)

    st.markdown("### Observaciones sobre sujetos explícitos no enfáticos y no contrastivos")
    st.markdown("""
    - La expresión explícita de sujetos no enfáticos/contrastivos no es rara en el mundo hispánico.

    ### Antecedentes:
    - Algunos estudios vinculan este uso a un posible **origen criollo** en ciertas variedades (AHLAs).
    - Investigaciones recientes consideran a las AHLAs como **interlenguajes avanzados y convencionalizados**, no necesariamente productos de criollización.
    - Para las **variedades del español de herencia** se asocian los procesos de **atrición** y **adquisición parcial** de la lengua.
    - Aun así, comparten patrones con las AHLAs, lo que ha llevado a clasificarlas como de tipo **"crioloide"**.
    - Los autores plantean un modelo de transmisión lingüística inducida por contacto que puede extenderse al JEI y a otras variedades del español de herencia
    """)
elif opciones == "Análisis de datos":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Análisis de datos</h2>', unsafe_allow_html=True)
    st.markdown("### Enfoque propuesto")
    st.markdown("""
    - Se adopta un marco teórico basado en la **modularidad de la facultad del lenguaje**.
    - Se utiliza el modelo de **arquitectura de la interfaz** de **Reinhart (2006)**.
    - La **sintaxis** mantiene un rol central.
    - Se conecta con otros módulos (semántica, pragmática, etc.) de forma independiente.
    - No se descartan otros modelos alternativos de interfaz lingüística.
    """)

    st.markdown("### Relevancia para ASL y APL: hipótesis de la interfaz ")
    st.markdown("""
    - Ciertas construcciones en la interfaz entre módulos presentan **alta demanda cognitiva**.
    - Estas son más **difíciles de adquirir en ASL** y las primeras en **erosionarse en APL**.
    """)

    st.markdown("""
    - En español, se espera que el sujeto nulo (pro) **no se exprese** en contextos no contrastivos.
    - El uso de sujetos explícitos involucra la interfaz entre **sintaxis y pragmática**.
    - Estudios previos muestran que aprendices de L2 y hablantes con **atrición temprana de L1**:
        - Usan **más sujetos explícitos** de lo esperado.
        - No adquieren plenamente el sistema de pronombres del español.
    """)

    st.markdown("### Datos de AES y JEI")
    st.markdown("""
    - Se observa **uso excesivo de sujetos explícitos no enfáticos y no contrastivos**.
    - Coincide con la **pérdida de sujetos nulos** y un **cambio gramatical** relacionado con el parámetro de sujeto nulo.
    - Esto sugiere una reconfiguración del **"parámetro de abandono del pro"**.
    """)
    st.markdown("""
    - Las **interfaces externas** (sintaxis-pragmática) presentan más dificultad en la SLA/FLA.
    - Incluso, la interfaz **sintaxis-morfología** es vista como un problema en la adquisición.
    """)

    st.markdown("### Desafíos en la ASL y APL")
    st.markdown("""
    - Las **características phi** (persona, número, género) representan una carga significativa en la interfaz **sintaxis-morfología**.
    - En español, estas marcas son **redundantes** y su dominio:
        - Ocurre **tarde** en la adquisición de L2 (ASL).
        - Se **pierde fácilmente** en casos de atrición de L1 (APL).
    - Esto resulta en **variación morfológica** en la concordancia nominal y verbal.
    - Se observan **formas verbales invariables**, especialmente la **tercera persona singular** como forma por defecto.
    """)

    st.markdown("### Propuesta formal")
    st.markdown("""
    - Se postulan dos Tense Heads (T) en la numeración léxica:
        - **T1**: lleva rasgos de tiempo, caso, número y persona (como en español estándar).
        - **T2**: solo lleva **tiempo**, pero no **número ni persona**.
    - Resultado:
        - Si AGREE se da entre sujeto y T1 → **forma plenamente conjugada**.
                Nosotros bailamos.
        - Si AGREE se da entre sujeto y T2 → **forma con tiempo, pero tercera persona singular por defecto**.
                Nosotros baila.
    """)

    st.markdown("""
    - Las **restricciones en la interfaz sintaxis - morfología** no solo afectan la concordancia sujeto-verbo, sino también la **concordancia de género y número** en el **sintagma nominal (DP)**.
    - Estudios previos muestran el uso frecuente del **masculino/singular como valor por defecto**.
    """)

    st.markdown("### Jerarquía de adquisición del DP")
    st.markdown("""
    - Investigaciones en **creolística** y **SLA** proponen una jerarquía de adquisición:
    1. Concordancia en **determinantes definidos** (más temprana y sólida).
    2. Concordancia en **determinantes indefinidos**.
    3. Concordancia en **otros elementos del DP**, como adjetivos.
    - Ejemplo: Estudiantes de inglés aprendiendo francés o español muestran **más concordancia en determinantes** que en adjetivos.
    """)

    st.markdown("### Evidencia empírica")
    st.markdown("""
    - Este patrón se repite en aprendices con L1 muy diversa (italiano, árabe, alemán, etc.).
    - El fenómeno se asocia a **estrategias de economía cognitiva**: los elementos más externos del DP (como los determinantes) son adquiridos primero.
    """)

    st.markdown("""
    - **(13)** D1 y N1 tienen especificaciones completas para género y número → Concordancia estándar.
                Muchas gatas
    - **(14)** D2 y N2 carecen parcialmente de esas especificaciones → **Concordancia empobrecida**.
                Mucho gata
    """)

elif opciones == "La propuesta para las características de AES y IJS":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">La propuesta para las características de AES y IJS</h2>', unsafe_allow_html=True)
    st.markdown("""
        ### Hipótesis central

        La presencia de fenómenos como:
        - Uso de pronombres explícitos no contrastivos.
        - Reducción en la concordancia de género y número.

        El **español afroecuatoriano tradicional (AES)** y el **judeoespañol contemporáneo (IJS)**, así como en otras 
        **variedades de español en contacto o de herencia** son el resultado de procesos sistemáticos de adquisición de lenguaje.

        ---

        ### Fundamento teórico

        - Se postula que estos rasgos provienen de:
            - La **adquisición L1 (nativización)** a partir de **gramáticas avanzadas de L2**.
            - La **atrición temprana de L1**, cuando se pierde el dominio completo del idioma original.

        - La teoría se basa en:
            - La **Gramática Universal (GU)** como mecanismo subyacente tanto en adquisición como en atrición.
            - La idea de que la adquisición de L1 es espontánea, mientras que la L2 es más limitada, especialmente en interfaces como:
                - Concordancia sujeto-verbo.
                - Concordancia nominal.
                - Uso de pronombres.

        ---

        ### Modelo de transmisión transgeneracional

        - Generación 1: hablantes que alcanzan un dominio intermedio/avanzado del español como L2.
            - Su producción genera insumos lingüísticos (PLD) no nativos.
        - Generación 2: adquiere este input como **lengua materna (L1)**, dando origen a una nueva **gramática nativa G2**, que incluye:
            - Rasgos de L2.
            - Rasgos de atrición L1.

        Este proceso es lo que se denomina **"nativización"**.

        ---

        ### “Reciclaje lingüístico intracomunitario”

        - Las características no estándar se **transmiten dentro de la comunidad** de generación en generación.
        - Resultado: cambio sistemático, alejado del español estándar pero **consistente y estructurado**.

        """)

elif opciones == "Comentarios":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Comentarios</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    - La lectura discute una propuesta —de corte **bastante generativista**, dicho sea de paso— para explicar por qué tanto el 
                español afro-ecuatoriano tradicional y el judeo-español estambulí moderno tienen las mismas características 
                gramaticales. En principio, confieso que la elección comparativa entre ambas variedades me sorprende un poco. 
                La justificación es que porque **sociolingüísticamente son muy similares entre sí**, pero, en principio, no creo 
                que el hecho de ser la variedad de una minoría, empleada solamente en espacios de comunidad  y con poco valor "marketero" 
                sea una característica exclusiva de estas dos variedades. Además, a lo largo de la lectura eventualmente meten en el mismo 
                saco a las **lenguas caribeñas**, lo que me hace mucho sentido (¿creo que esta construcción 'hacer sentido' es calco del inglés?), 
                por lo mismo que también tienen un influjo fuerte de lenguas africanas en el español. Asimismo, también se habla de **lenguas 
                de herencia**, como el español en EEUU. Entonces, una vez más, me deja preguntándome **por qué insistir en la comparación entre 
                estas dos variantes**. Además, otro detalle que me parece importante resaltar: **la comparativa es entre el EAE tradicional y el 
                JEE moderno**. No hay procesos paralelos, sino más bien opuestos... Pienso que le han dado una explicación de formación histórica 
                al EAE, que ya se está perdiendo en nuevas generaciones, pero que para el JEE está en un punto de aparición por el contacto con 
                el turco. **Ese punto, en todo caso, queda abandonado y ambas variantes son presentadas realmente como sorprendentemente paralelas; 
                me parece a mí que el paralelismo se debe a un proceso, que ellos mismos defienden, no exclusivo de ambas —porque lo señalan para 
                explicar también procesos en lenguas de herencia y otras variedades de español caribeño— y llevado a cabo en distintos momentos 
                históricos. Sumémosle a esto el hecho de que es un estudio generativista, que apunta a comprender el funcionamiento universal 
                del lenguaje a nivel abstracto: ¿cuál es el punto de la insistencia en la comparación de estas dos variantes?**  
                
    - Como limitaciones encontradas en la lectura puedo referir que, si bien en el estudio se propone un modelo de transmisión 
      lingüística intergeneracional inducida por contacto, que explica la expresión de rasgos compartidos —tales como el uso excesivo 
      de pronombres y la pérdida de concordancia— como paralelismos estructurales entre variedades no relacionadas ni geográfica ni históricamente
      —como en el caso del afroespañol ecuatoriano (AES) y el judeoespañol estambulita (IJS)—, en el ámbito metodológico, **no se precisa el nivel 
      educativo de los 50 hablantes entrevistados de AES ni de los más de 60 de IJS en lo que respecta a su caracterización sociolingüística, pese a que, 
      en los rasgos observados, ciertas diferencias, como de menores grados de escolarización o alfabetizaciones limitadas, podrían también influir en tales**. 
      Asimismo, **se indica que, en el caso de las gramáticas de las lenguas que provienen de un proceso de adquisición incompleta (SLA) y de atrición temprana 
      de L1 (FLA) del español, el dominio incompleto de rasgos phi “da lugar a una variación morfológica en la concordancia entre los dominios nominal y verbal” (p. 73), 
      pero no se precisa, al respecto, por ejemplo, si tal implica procesos de simplificación estructural —en este caso, de eliminación de marcas morfológicas— y/o de fosilización 
      —esto es, de estabilización de formas incorrectas o no estándares en el habla a partir de un dominio incompleto de rasgos—, entre otros**.

    - El artículo trata de la comparación entre dos variedades del español que, a pesar de sus diferencias 
      históricas y geográficas, presentan estructuras similares influenciadas por el contacto lingüístico. 
      Me pareció interesante la noción de interfaz lingüística, que resulta útil para comprender cómo ciertas 
      estructuradas se ven alteradas por procesos de transmisión irregular y cambio lingüístico. Aunque el estudio da 
      a conocer la influencia del contacto en la evolución gramatical de las variedades AES y IJS, **sería necesario 
      profundizar el valor de los factores extralingüísticos, como la identidad cultural y las dinámicas de la comunidad**.        
     
    - La lectura se centra en un análisis comparativo del cambio lingüístico inducido por el contacto en dos 
        variedades hispánicas geográficamente distantes y con historias sociolingüísticas muy diferentes: el judeoespañol 
        hablado en Estambul y el español afroecuatoriano. Su argumento central, sólidamente respaldado por la
        evidencia que presentan, es que, a pesar de la disparidad de sus contextos de contacto, ambas variedades exhiben procesos 
        de cambio lingüístico notables que son resultado directo de la interacción prolongada con otras lenguas. 
        Por otro lado, **explora claramente las influencias léxicas** y, en cierta medida, fonológicas y sintácticas de las lenguas en contacto, 
        me hubiera resultado **aún más enriquecedor una discusión más detallada sobre los mecanismos específicos de estas interfaces**. Por ejemplo, 
        **¿Cómo se manifiesta concretamente la transferencia de estructuras sintácticas? 
        ¿Existen casos de calcos semánticos sutiles que van más allá del simple préstamo léxico?**
                
    """)
    
    

