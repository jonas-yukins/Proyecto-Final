################################################################################
# IMAGE DEFINITIONS
################################################################################

image map = "Watercolor Map of the Americas.png"

# Soledad Castillo
image SC = "Soledad_Castillo.png"
image SC_desert4 = "Desert_4People.png"
image SC_bus = "Bus.png"
image SC_desert20 = "Desert_20People.png"
image SC_stepfather = "Drunk_Stepfather.png"
image SC_gangsters = "Gangsters.png"
image SC_hiding = "Hiding_in_Van.png"
image SC_father = "Speaking_to_Father.png"
image SC_van = "Van.png"
image SC_xray = "Xray_Van.png"

# Liset & Marta
image LM = "L&M.png"
image LM_Airplane = "L&M_airplane.png"
image LM_Airplane2 = "L&M_airplane2.png"
image LM_Bus = "L&M_Bus.png"
image LM_Taxi = "L&M_Bolivia_taxi.png"
image LM_Canoe = "L&M_canoe.png"
image LM_Chickenshop = "L&M_chicken.png"
image LM_Coffeshop = "L&M_coffee.png"
image LM_Darien = "L&M_Darien.png"
image LM_Hike = "L&M_hike.png"
image LM_Money = "L&M_counting_money.png"
image LM_Potatoes = "L&M_Potatoes.png"
image LM_Crowded_van = "L&M_crowded_van.png"
image LM_Dancing1 = "L&M_dancing.png"
image LM_Dancing2 = "L&M_dancing2.png"
image LM_Horses = "L&M_horses.png"
image LM_Raft = "L&M_Raft.png"

# Ortega Family
image AO_Family = "A_O_Family.png"
image AO_Apartment = "A_O_Apartment.png"
image AO_Border = "A_O_Border.png"
image AO_Gap = "A_O_Gap.png"
image AO_Missionaries= "A_O_Missionaries.png"
image AO_NYC = "A_O_NYC.png"
image AO_Plaza = "A_O_Plaza.png"
image AO_Police = "A_O_Police.png"
image AO_River = "A_O_River.png"
image AO_Tent = "A_O_Tent.png"
image AO_Train = "A_O_Train.png"
image AO_Van = "A_O_Van.png"

################################################################################
# TRANSFORMS
################################################################################

transform fit_screen:
    xysize (1920, 1080)

################################################################################
# MAP CHECKPOINT DATA
################################################################################

init python:
    ortega_journey = [
        {"name": "1. Colombia", "label": "ortega_cp1", "coords": (850, 700)},
        {"name": "2. Tapón del Darién", "label": "ortega_cp2", "coords": (750, 620)},
        {"name": "3. Ciudad de México", "label": "ortega_cp3", "coords": (440, 420)},
        {"name": "4. Texas", "label": "ortega_cp4", "coords": (400, 300)},
        {"name": "5. Nueva York", "label": "ortega_cp5", "coords": (750, 200)},
    ]

    liset_marta_journey = [
        {"name": "1. Cuba", "label": "liset_cp1", "coords": (850, 450)},
        {"name": "2. Guyana", "label": "liset_cp2", "coords": (1150, 700)},
        {"name": "3. Brasil", "label": "liset_cp3", "coords": (1200, 925)},
        {"name": "4. Perú", "label": "liset_cp4", "coords": (850, 886)},
        {"name": "5. Ecuador", "label": "liset_cp5", "coords": (800, 800)},
        {"name": "6. Tapón del Darién", "label": "liset_cp6", "coords": (750, 620)},
        {"name": "7. México", "label": "liset_cp7", "coords": (440, 420)},
        {"name": "8. Chicago", "label": "liset_cp8", "coords": (550, 100)},
    ]

    soledad_journey = [
        {"name": "1. Honduras", "label": "soledad_cp1", "coords": (650, 550)},
        {"name": "2. Guatemala", "label": "soledad_cp2", "coords": (600, 500)},
        {"name": "3. México", "label": "soledad_cp3", "coords": (440, 420)},
        {"name": "4. Texas", "label": "soledad_cp4", "coords": (400, 300)},
    ]


################################################################################
# MAP SCREENS
################################################################################

screen ortega_map():
    tag map
    add "map" at fit_screen
    for cp in ortega_journey:
        textbutton cp["name"]:
            action [Play("sound", "audio/click.mp3"), Jump(cp["label"])]
            xpos cp["coords"][0]
            ypos cp["coords"][1]
            background "#0008"
            padding (10, 5)
            hover_background "#444c"
    
    ## RETURN BUTTON ##
    textbutton "Regresar":
        action [Play("sound", "audio/back.mp3"), Jump("start")]
        xpos 0.98
        ypos 0.02
        xanchor 1.0
        yanchor 0.0
        background "#FFFFFF"
        padding (10, 5)
        hover_background "#F0F0F0"

screen liset_marta_map():
    tag map
    add "map" at fit_screen
    for cp in liset_marta_journey:
        textbutton cp["name"]:
            action [Play("sound", "audio/click.mp3"), Jump(cp["label"])]
            xpos cp["coords"][0]
            ypos cp["coords"][1]
            background "#0008"
            padding (10, 5)
            hover_background "#444c"
        
    ## RETURN BUTTON ##
    textbutton "Regresar":
        action [Play("sound", "audio/back.mp3"), Jump("start")]
        xpos 0.98
        ypos 0.02
        xanchor 1.0
        yanchor 0.0
        background "#FFFFFF"
        padding (10, 5)
        hover_background "#F0F0F0"

screen soledad_map():
    tag map
    add "map" at fit_screen
    for cp in soledad_journey:
        textbutton cp["name"]:
            action [Play("sound", "audio/click.mp3"), Jump(cp["label"])]
            xpos cp["coords"][0]
            ypos cp["coords"][1]
            background "#0008"
            padding (10, 5)
            hover_background "#444c"
        
    ## RETURN BUTTON ##
    textbutton "Regresar":
        action [Play("sound", "audio/back.mp3"), Jump("start")]
        xpos 0.98
        ypos 0.02
        xanchor 1.0
        yanchor 0.0
        background "#FFFFFF"
        padding (10, 5)
        hover_background "#F0F0F0"

################################################################################
# CHARACTER SELECTION SCREEN
################################################################################

screen character_select():
    tag menu
    add "map" at fit_screen 
    frame:
        align (0.5, 0.5)
        padding (40, 40)
        background "#000a"
        vbox:
            spacing 20
            text "Elige una historia para comenzar:" size 40
            textbutton "Soledad Castillo":
                action [Stop("music", fadeout=1.0), Jump("start_soledad")]            
            textbutton "Aguilar Ortega Family":
                action [Stop("music", fadeout=1.0), Jump("start_aguilar_ortega")] 
            textbutton "Liset Barrios & Marta Amaro":
                action [Stop("music", fadeout=1.0), Jump("start_liset_marta")] 

################################################################################
# MAP CALL LABELS
################################################################################

label show_ortega_map:
    call screen ortega_map
    return

label show_liset_marta_map:
    call screen liset_marta_map
    return

label show_soledad_map:
    call screen soledad_map
    return

################################################################################
# GAME START
################################################################################

label start:
    play music "audio/menu.mp3" fadein 0.5
    call screen character_select
    return

################################################################################
# AGUILAR ORTEGA STORYLINE
################################################################################

label start_aguilar_ortega:
    scene map at fit_screen
    "Este es el viaje de la familia Aguilar Ortega."
    "Los puntos están enumerados en orden secuencial para ayudarte a seguir la aventura."
    jump show_ortega_map

label ortega_cp1:
    scene AO_Family at fit_screen with dissolve
    "Henry Aguilar y sus tres hijos, Hayli, Samuel y Josué, vivían en Ecuador cuando conoció a Leivy Ortega."
    "Ambos venezolanos, ambos habían abandonado Venezuela después de la crisis económica que ocurrió bajo el gobierno del presidente Nicolás Maduro."

    scene AO_Van at fit_screen with dissolve
    play sound "audio/car_keys.mp3"
    "Decidieron emprender el viaje a Estados Unidos para tener una vida mejor para ellos y sus hijos."
    "Sra. Ortega tenía una hija de 13 años, pero ella estaba muy enferma y no podía viajar."
    "Después de conocerse en Ecuador, la familia viajó a Perú antes de llegar a Colombia sin dinero ni plan ni lugar para dormir."

    scene AO_Plaza at fit_screen with dissolve
    "La familia se duerme en una plaza por dos semanas en Colombia antes de salir por el próximo lugar."
    "En la plaza, montaban en bici y se entrenaron por su viaje por el Tapiz del Darién."

    jump show_ortega_map

label ortega_cp2:
    scene AO_Gap at fit_screen with dissolve
    "Para entrar el Tapon del Darien, necesitaban pagar 300 dólares por persona a los soldados armados que tenían control de la entrada."
    "Cada persona necesitaba conseguir una pulsera rosa para entrar."
    "Había cientos de personas tratando de entrar el Tapón."

    scene AO_River at fit_screen with dissolve
    play music "audio/river.mp3"
    "Cuando estaban en su viaje dentro el Tapon del Darien, necesitaban caminar en la selva en un camino muy embarrado. También necesitaban cruzar algunos ríos, con sus cosas encima de sus cabezas."
    "Otras personas gritaban “muerto, muerto” cuando pasaban los cuerpos de migrantes muertos que murieron en el Tapón."
    "Estaban en la selva por seis días, y en los últimos dos días del viaje necesitaban sobrevivir bebiendo solo agua del río."

    stop music
    jump show_ortega_map

label ortega_cp3:
    scene AO_Police at fit_screen with dissolve
    "Entre el Tapón del Darién y la ciudad de méxico, el viaje no fue mucho más fácil."
    "Las compañías de autobuses les cobraron el doble o no vendieron los boletos a la familia porque eran migrantes."
    "La policía intentó robar a la familia. Tuvieron que guardar el dinero en las chaquetas de los niños para que no se lo robaran."

    scene AO_Border at fit_screen with dissolve
    "En la ciudad de México, la situación no era mucho mejor."
    "La familia dormía en una tienda de campaña en la calle."

    scene AO_Train at fit_screen with dissolve
    play music "audio/train.mp3"
    "Para viajar por la frontera de Estados Unidos, la familia abordó un tren de carga y usó ropa y cobijas para asegurarse al tren. Los trenes de mercancías fueron apodados \"la bestia\"."
    stop music
    jump show_ortega_map

label ortega_cp4:
    scene AO_Missionaries at fit_screen with dissolve
    "Al llegar a una ciudad fronteriza, utilizaron una aplicación de migración para asegurarse un tiempo para cruzar la frontera. Este aplicación fue creada durante la presidencia de Biden."
    "Entraron los EEUU su tiempo específico, y los atendientes de la frontera tomaron sus fotos, NDA, y huellas dactilares."
    "En El Paso, tuvieron problemas para encontrar un hogar, y los oficiales les dijeron que no podían tener boletos gratuitos para viajar fuera de Texas en autobús."
    "Conocieron a unos misioneros cristianos. Los misioneros ayudaron a la familia y encontraron $2000 para pagar por sus boletos de avión a Nueva York."
    jump show_ortega_map

label ortega_cp5:
    scene AO_NYC at fit_screen with dissolve
    "Llegaron a Nueva York con un total de 20 sentados, y todos sus cosas en una maleta rosa."

    scene map at fit_screen with dissolve
    "Has terminado el viaje de la familia Aguilar Ortega."
    jump start

################################################################################
# LISET & MARTA STORYLINE
################################################################################

label start_liset_marta:
    scene map at fit_screen
    "Este es el viaje de Liset Barrios y Marta Amaro."
    "Los puntos están enumerados en orden secuencial para ayudarte a seguir la aventura."
    jump show_liset_marta_map

label liset_cp1:
    scene LM at fit_screen with dissolve
    "Liset Barrios & Marta Amaro son de Cuba."

    scene LM_Dancing1 at fit_screen with dissolve
    "Al hacerse amiga con turistas masculinos con dinero para gastar en Cuba – una situación que a menudo se convierte de novia a escort – Liset vivió bien, después de haber vivido una vez en un contenedor."
    
    scene LM_Coffeshop at fit_screen with dissolve
    "Marta, que tenía 53 años, ganaba 5 pesos cubanos diarios trabajando en cafés, hospitales y un asilo."
    "Las dos mujeres querían una vida mejor."

    scene LM_Dancing2 at fit_screen with dissolve
    play music "audio/cuba.mp3"
    "Liset tenía un novio en Chicago, que se había enamorado de Liset durante un viaje a La Habana."
    "Se ofreció a ayudar a traer a las dos mujeres al norte."
    stop music
    jump show_liset_marta_map

label liset_cp2:
    scene LM_Airplane at fit_screen with dissolve
    "La ruta más corta de Cuba a los EEUU es 90 millas. Pero esto está al otro lado del estrecho de Florida, y Liset se pone nerviosa en las barcas."
    "Por esta razón, las mujeres abordaron un avión para emprender su viaje a Estados Unidos. El viaje duró 12800 kilómetros y 51 días."
    "En Guyana conocieron a un contrabandista que los llevó a Brasil."
    jump show_liset_marta_map

label liset_cp3:
    scene LM_Crowded_van at fit_screen with dissolve
    "Tuvieron que viajar en una camioneta durante 18 horas hasta la frontera con Brasil."
    
    scene LM_Canoe at fit_screen with dissolve
    play music "audio/jungle.mp3"
    "Cruzaron la frontera con Brasil en canoa y luego se dirigieron a Manaos, en plena selva tropical."
    "Allí abordaron un avión hacia el suroeste de Brasil, ahorrando 22 horas de viaje por tierra."
    stop music

    scene LM_Taxi at fit_screen with dissolve
    "Después, alquilaron un taxi hasta la frontera con Bolivia, un remoto rincón que cruzaron camino a Perú."
    jump show_liset_marta_map

label liset_cp4:
    scene LM_Money at fit_screen with dissolve
    "El autobús por los Andes a Lima cuesta $150. Las dos mujeres han gastado $2300 de casi $8000 total para el viaje por cada persona."
    "En mucho del viaje, Liset pagó por Marta."
    jump show_liset_marta_map

label liset_cp5:
    scene LM_Bus at fit_screen with dissolve
    play sound "audio/truck_honk.mp3"
    "Por la noche, se embarcaron en un autobús a Ecuador, donde Liset habló con los oficiales de immigracion."
    "El primer autobús en Ecuador estaba lleno de haitianos, quienes después del terremoto de 2010 también ganaron el derecho a entrar a los Estados Unidos."
    "También había personas de Bangladesh, que comenzó su viaje a 11,000 millas de distancia."
    jump show_liset_marta_map

label liset_cp6:
    scene LM_Horses at fit_screen with dissolve
    "Cruzaron a Colombia en caballo, donde conocieron al próximo Coyote en un restaurante de pollo."
    "\"Cada movimiento de los migrantes es bajo las instrucciones de los coyotes, quienes envían fotos del próximo coyote a los migrantes para que sepan a quien deben buscar en la próxima parada.\""

    scene LM_Potatoes at fit_screen with dissolve
    play music "audio/engine.mp3"
    "Liset y Marta se unen a una docena de personas bajo la lona de un camión cargado de papas."
    "Viajan a Medellín, luego a Panamá, luego en motocicletas hasta una lancha, y luego en carreta tirada por caballos hasta el borde del Tapón del Darién."
    stop music

    scene LM_Darien at fit_screen with dissolve
    play music "audio/jungle.mp3"
    "La caminata fue brutal, por empinadas colinas llamadas \"Adiós, mi Ciudad\" y \"la Colina de la Muerte\"."
    "\"Quería que me tragara la tierra\", dijo Marta, quien se lastimó la pierna el primer día. \"No pensé que lo lograría.\""
    stop music

    scene map at fit_screen with dissolve
    "En Costa Rica, Marta abandona el grupo tras una discusión económica. Llegará a Estados Unidos ella sola, 12 días después que Liset."

    jump show_liset_marta_map

label liset_cp7:
    scene LM_Hike at fit_screen with dissolve
    "Liset entró a Nicaragua a caballo, luego caminó por otro sendero en la jungla marcado con cintas rojas en árboles de teca."
    "La gente bebía agua de los charcos y dormía de pie."

    scene LM_Raft at fit_screen with dissolve
    play music "audio/river.mp3"
    "Cruzó un río hacia Honduras a pie y luego entró a Guatemala por el mismo camino."
    "A México se llega en balsa."
    stop music

    jump show_liset_marta_map

label liset_cp8:
    scene LM_Airplane2 at fit_screen with dissolve
    "Liset tomó un avión a la Ciudad de México, y luego otro a Matamoros, donde se presentó a los oficiales de inmigración de Estados Unidos en la frontera de Brownsville."
    "Allí le dieron una licencia para entrar. Un día después, llegó al aeropuerto O’Hare de Chicago."

    scene map at fit_screen with dissolve
    "Has terminado el viaje de Liset y Marta."
    jump start

################################################################################
# SOLEDAD STORYLINE
################################################################################

label start_soledad:
    scene map at fit_screen
    "Este es el viaje de Soledad Castillo."
    "Los puntos están enumerados en orden secuencial para ayudarte a seguir la aventura."
    jump show_soledad_map

label soledad_cp1:
    scene SC_stepfather at fit_screen with dissolve
    "Soledad Castillo nació en Honduras en 1992."
    "Su padre se fue a los Estados Unidos cuando ella tenía 5 años."
    "Ella vivía con su mamá y su hermana. Eran las personas más pobres en su barrio."
    "Su padrastro era abusivo y un borracho." 
    "\"Él golpeó a mi mama y le tiró las sillas.\""

    scene SC_father at fit_screen with dissolve
    "Cuando ella tenía 12 años, su papá fue a visitarla. Ella le dijo que quería ir a los Estados Unidos con él."
    "\"Le dije a mi papá que quería ir a los Estados Unidos porque no tenía nada en Honduras y quería empezar una vida nueva.\""
    jump show_soledad_map

label soledad_cp2:
    scene SC_bus at fit_screen with dissolve
    play sound "audio/truck_honk.mp3"
    "Primero, viajaron de Honduras a Guatemala en autobús."

    scene SC_gangsters at fit_screen with dissolve
    "\"Habían gángsters en el autobús que me pusieron una pistola en la cabeza, y me pidieron todo mi dinero.\""
    "\"No tenía dinero, pero no me creyeron.\""
    "\"Ellos me quitaron los pantalones. No recuerdo sus caras. Solo recuerdo sus manos.\""
    "\"Tenía 14 años.\""
    jump show_soledad_map

label soledad_cp3:
    scene SC_van at fit_screen with dissolve
    "Viajaron de Guatemala a Honduras en una camioneta."

    scene SC_xray at fit_screen with dissolve
    "\"Tuvimos que acostarnos con muchísimas personas, una encima de la otra. Los coyotes nos pusieron cartones encima de nosotros para que la Migra, las autoridades, no pudieran vernos si nos detuvo.\""
    "\"Fue muy difícil respirar.\""

    scene SC_desert20 at fit_screen with dissolve
    play sound "audio/eagle.mp3"
    "\"Nosotros caminamos por el desierto mexicano por muchos días. Había alrededor de 20 personas en nuestro grupo de todas partes del mundo.\""
    "\"Al segundo día, no tuve energía, y mi papá les pagó a los coyotes por una pastilla para darme energía.\""

    scene SC_desert4 at fit_screen with dissolve
    "\"Algunas personas se perdieron y no llegaron al otro lado.\""
    jump show_soledad_map

label soledad_cp4:
    scene SC_hiding at fit_screen with dissolve
    "Cuando llegaron a Texas, los subieron a una camioneta para llevarlos a California."
    "\"Había un lugar donde podíamos escondernos debajo del suelo donde nos ponían. Fue un viaje muy largo y necesitábamos estar callados todo el tiempo.\""

    scene map at fit_screen with dissolve
    "Has terminado el viaje de Soledad Castillo."
    jump start
