image bus = "Bus.png"
image desert4 = "Desert_4People.png"
image desert20 = "Desert_20People.png"
image stepfather = "Drunk_Stepfather.png"
image gangsters = "Gangsters.png"
image hiding = "Hiding_in_Van.png"
image father = "Speaking_to_Father.png"
image van = "Van.png"
image xray = "Xray_Van.png"

transform fit_screen:
    xysize (1920, 1080)

# This is where we initialize the map and define the checkpoints for Soledad's journey.

init python:
    # Define the checkpoints and their locations on the map
    soledad_journey = [
        {"name": "Checkpoint 1", "label": "soledad_cp1", "coords": (300, 550)},
        {"name": "Checkpoint 2", "label": "soledad_cp2", "coords": (320, 500)},
        {"name": "Checkpoint 3", "label": "soledad_cp3", "coords": (340, 420)},
        {"name": "Checkpoint 4", "label": "soledad_cp4", "coords": (100, 300)},
    ]

# Screen for showing the map with clickable checkpoints
screen soledad_map():
    tag map
    add "Watercolor Map of the Americas.png" at fit_screen # Replace with the name of your map image

    # Loop through each checkpoint and create a clickable button for it
    for cp in soledad_journey:
        textbutton cp["name"]:
            action Jump(cp["label"])
            xpos cp["coords"][0]
            ypos cp["coords"][1]
            background "#0008"  # Transparent background for buttons
            padding (10, 5)  # Adjust padding for buttons
            hover_background "#444c"  # Hover effect for buttons

# Label to show the map when called
label show_soledad_map:
    call screen soledad_map
    return

label character_select_hub:
    call screen character_select
    return

screen character_select():
    tag menu
    frame:
        align (0.5, 0.5)
        padding (40, 40)
        background "#000a"
        vbox:
            spacing 20
            text "Choose a story to begin:" size 40

            textbutton "Soledad Castillo":
                action Jump("start_soledad")

            textbutton "Aguilar Ortega Family":
                action Jump("start_aguilar_ortega")

            textbutton "Liset Barrios & Marta Amaro":
                action Jump("start_liset_marta")

# Start of the game
label start:
    call screen character_select
    return

label start_aguilar_ortega:
    "This will be the journey of the Aguilar Ortega family."
    # Add map and checkpoints here later
    return

label start_liset_marta:
    "This will be the journey of Liset Barrios & Marta Amaro."
    # Add map and checkpoints here later
    return

label start_soledad:

    "Welcome to Soledad's journey. Let’s begin the trip."
    jump show_soledad_map

# Checkpoint 1: Honduras
label soledad_cp1:
    scene stepfather at fit_screen
    with dissolve
    "Soledad Castillo was born in Honduras in 1992."
    "Her father left for the U.S. when she was 5."
    "She lived with her mother and sister. They were the poorest in a poor neighborhood."
    "Her stepfather was abusive and a drunk."
    "\"He used to hit my mom and throw chairs at her.\""

    scene father at fit_screen
    with dissolve
    "When she was 12 her father came to visit her. She told him she wanted to go to the U.S. with him."
    "\"I asked him to take me back to the United States because I didn’t have anything left in Honduras and I wanted to start a new life.\""

    jump show_soledad_map

# Checkpoint 2: Guatemala
label soledad_cp2:
    scene bus at fit_screen
    with dissolve
    "They first traveled from Honduras to Guatemala on a bus."

    scene gangsters at fit_screen
    with dissolve
    "\"There were gangsters on board who put a gun to my head, asking for all my money.\""
    "\"I didn’t have any but they didn’t believe me.\""
    "\"They took my pants off. I don’t remember their faces. I just remember their hands.\""
    "\"I was 14.\""

    jump show_soledad_map

# Checkpoint 3: Mexico Desert
label soledad_cp3:
    scene van at fit_screen
    with dissolve
    "They traveled from Guatemala to Mexico in a van."

    scene xray at fit_screen
    with dissolve
    "\"We had to lie down with many people, one on top of the other. The coyotes put cardboard on top of us so la Migra, the authorities, wouldn’t see us if they pulled us over.\""
    "\"It was hard to breathe.\""

    scene desert20 at fit_screen
    with dissolve
    "\"We then walked through the Mexican desert for days. There were around 20 people in our group from all over the world.\""
    "\"On the second day, I became too weak, so my father paid the coyotes extra for a little pill to give me energy.\""

    scene desert4 at fit_screen
    with dissolve
    "\"Some people got lost and didn’t make it.\""
    
    jump show_soledad_map

# Checkpoint 4: California
label soledad_cp4:
    scene hiding at fit_screen
    with dissolve
    "Upon reaching Texas they were put in a van to drive to California."
    "\"There was a hiding place under the floor where they put us. It was a very long trip and we had to stay quiet the whole time.\""
    
    "You have finished Soledad Castillo's Journey."

    scene black with fade
    pause 1.0

    jump start
