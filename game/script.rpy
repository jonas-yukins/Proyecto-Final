################################################################################
# IMAGE DEFINITIONS
################################################################################

image map = "Watercolor Map of the Americas.png"
image bus = "Bus.png"
image desert4 = "Desert_4People.png"
image desert20 = "Desert_20People.png"
image stepfather = "Drunk_Stepfather.png"
image gangsters = "Gangsters.png"
image hiding = "Hiding_in_Van.png"
image father = "Speaking_to_Father.png"
image van = "Van.png"
image xray = "Xray_Van.png"

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
        {"name": "Colombia", "label": "ortega_cp1", "coords": (1025, 788)},
        {"name": "Darien Gap", "label": "ortega_cp2", "coords": (950, 759)},
        {"name": "Mexico City", "label": "ortega_cp3", "coords": (440, 420)},
        {"name": "New York City", "label": "ortega_cp4", "coords": (1125, 323)},
        {"name": "Texas", "label": "ortega_cp5", "coords": (400, 300)},
    ]

    liset_marta_journey = [
        {"name": "Cuba", "label": "liset_cp1", "coords": (1000, 506)},
        {"name": "Guyana", "label": "liset_cp2", "coords": (1150, 801)},
        {"name": "Brazil", "label": "liset_cp3", "coords": (1250, 971)},
        {"name": "Peru", "label": "liset_cp4", "coords": (950, 886)},
        {"name": "Ecuador", "label": "liset_cp5", "coords": (967, 844)},
        {"name": "Darien Gap", "label": "liset_cp6", "coords": (950, 759)},
        {"name": "Mexico", "label": "liset_cp7", "coords": (700, 605)},
        {"name": "Chicago", "label": "liset_cp8", "coords": (900, 267)},
    ]

    soledad_journey = [
        {"name": "Honduras", "label": "soledad_cp1", "coords": (650, 550)},
        {"name": "Guatemala", "label": "soledad_cp2", "coords": (600, 500)},
        {"name": "Mexico", "label": "soledad_cp3", "coords": (440, 420)},
        {"name": "Texas", "label": "soledad_cp4", "coords": (400, 300)},
    ]

################################################################################
# MAP SCREENS
################################################################################

screen ortega_map():
    tag map
    add "map" at fit_screen
    for cp in ortega_journey:
        textbutton cp["name"]:
            action Jump(cp["label"])
            xpos cp["coords"][0]
            ypos cp["coords"][1]
            background "#0008"
            padding (10, 5)
            hover_background "#444c"

screen liset_marta_map():
    tag map
    add "map" at fit_screen
    for cp in liset_marta_journey:
        textbutton cp["name"]:
            action Jump(cp["label"])
            xpos cp["coords"][0]
            ypos cp["coords"][1]
            background "#0008"
            padding (10, 5)
            hover_background "#444c"

screen soledad_map():
    tag map
    add "map" at fit_screen
    for cp in soledad_journey:
        textbutton cp["name"]:
            action Jump(cp["label"])
            xpos cp["coords"][0]
            ypos cp["coords"][1]
            background "#0008"
            padding (10, 5)
            hover_background "#444c"

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
            text "Choose a story to begin:" size 40
            textbutton "Soledad Castillo":
                action Jump("start_soledad")
            textbutton "Aguilar Ortega Family":
                action Jump("start_aguilar_ortega")
            textbutton "Liset Barrios & Marta Amaro":
                action Jump("start_liset_marta")

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
    call screen character_select
    return

################################################################################
# AGUILAR ORTEGA STORYLINE
################################################################################

label start_aguilar_ortega:
    scene map at fit_screen
    "This will be the journey of the Aguilar Ortega family."
    jump show_ortega_map

label ortega_cp1:
    scene bg room at fit_screen with dissolve
    "The Aguilar Ortega family began their journey in Colombia."
    "Political instability and threats from armed groups made it unsafe to remain."
    jump show_ortega_map

label ortega_cp2:
    scene bg jungle at fit_screen with dissolve
    "They crossed through the dangerous Darien Gap between Colombia and Panama."
    "\"The jungle felt endless. We carried our kids on our backs through mud and rain.\""
    jump show_ortega_map

label ortega_cp3:
    scene bg city at fit_screen with dissolve
    "They reached Mexico City and found temporary shelter in a migrant aid center."
    "\"We stayed in a crowded building, but at least we had food and a mattress.\""
    jump show_ortega_map

label ortega_cp4:
    scene bg nyc at fit_screen with dissolve
    "Eventually, they made it to New York City, hoping to reunite with relatives."
    "\"We thought it was the end of the journey, but it was only the beginning.\""
    jump show_ortega_map

label ortega_cp5:
    scene bg texas at fit_screen with dissolve
    "The family was processed in Texas before being released to a sponsor family."
    "\"We were tired, but we were together. That’s what mattered most.\""
    scene black with fade
    jump character_select

################################################################################
# LISET & MARTA STORYLINE
################################################################################

label start_liset_marta:
    scene map at fit_screen
    "This will be the journey of Liset Barrios & Marta Amaro."
    jump show_liset_marta_map

label liset_cp1:
    scene bg cuba at fit_screen with dissolve
    "Liset and Marta left Cuba, fleeing economic hardship and a lack of medical supplies."
    "They took a flight to Guyana—the first leg of their long journey."
    jump show_liset_marta_map

label liset_cp2:
    scene bg guyana at fit_screen with dissolve
    "Guyana was unfamiliar and overwhelming."
    "\"We didn’t know the language or customs, but we couldn’t turn back.\""
    jump show_liset_marta_map

label liset_cp3:
    scene bg brazil at fit_screen with dissolve
    "In Brazil, they worked small jobs to save up for the next bus ticket."
    "\"We cleaned houses and sold snacks in the street.\""
    jump show_liset_marta_map

label liset_cp4:
    scene bg peru at fit_screen with dissolve
    "They crossed the border into Peru on foot, dodging immigration patrols."
    "\"At night, we slept in tents. During the day, we kept moving.\""
    jump show_liset_marta_map

label liset_cp5:
    scene bg ecuador at fit_screen with dissolve
    "Ecuador offered brief relief. They contacted a smuggler to guide them north."
    jump show_liset_marta_map

label liset_cp6:
    scene bg jungle at fit_screen with dissolve
    "Crossing the Darien Gap was the most harrowing part of their trip."
    "\"There were bodies. Real people who never made it out. We cried and kept walking.\""
    jump show_liset_marta_map

label liset_cp7:
    scene bg mexico at fit_screen with dissolve
    "They made it to Mexico, where they were detained briefly and then released."
    jump show_liset_marta_map

label liset_cp8:
    scene bg chicago at fit_screen with dissolve
    "Finally, they arrived in Chicago, where they applied for asylum."
    "\"After everything, we just want a quiet place to start over.\""
    scene black with fade
    jump character_select

################################################################################
# SOLEDAD STORYLINE
################################################################################

label start_soledad:
    scene map at fit_screen
    "Welcome to Soledad's journey. Let’s begin the trip."
    jump show_soledad_map

label soledad_cp1:
    scene stepfather at fit_screen with dissolve
    "Soledad Castillo was born in Honduras in 1992."
    "Her father left for the U.S. when she was 5."
    "She lived with her mother and sister. They were the poorest in a poor neighborhood."
    "Her stepfather was abusive and a drunk."
    "\"He used to hit my mom and throw chairs at her.\""

    scene father at fit_screen with dissolve
    "When she was 12 her father came to visit her. She told him she wanted to go to the U.S. with him."
    "\"I asked him to take me back to the United States because I didn’t have anything left in Honduras and I wanted to start a new life.\""
    jump show_soledad_map

label soledad_cp2:
    scene bus at fit_screen with dissolve
    "They first traveled from Honduras to Guatemala on a bus."

    scene gangsters at fit_screen with dissolve
    "\"There were gangsters on board who put a gun to my head, asking for all my money.\""
    "\"I didn’t have any but they didn’t believe me.\""
    "\"They took my pants off. I don’t remember their faces. I just remember their hands.\""
    "\"I was 14.\""
    jump show_soledad_map

label soledad_cp3:
    scene van at fit_screen with dissolve
    "They traveled from Guatemala to Mexico in a van."

    scene xray at fit_screen with dissolve
    "\"We had to lie down with many people, one on top of the other. The coyotes put cardboard on top of us so la Migra, the authorities, wouldn’t see us if they pulled us over.\""
    "\"It was hard to breathe.\""

    scene desert20 at fit_screen with dissolve
    "\"We then walked through the Mexican desert for days. There were around 20 people in our group from all over the world.\""
    "\"On the second day, I became too weak, so my father paid the coyotes extra for a little pill to give me energy.\""

    scene desert4 at fit_screen with dissolve
    "\"Some people got lost and didn’t make it.\""
    jump show_soledad_map

label soledad_cp4:
    scene hiding at fit_screen with dissolve
    "Upon reaching Texas they were put in a van to drive to California."
    "\"There was a hiding place under the floor where they put us. It was a very long trip and we had to stay quiet the whole time.\""

    scene map at fit_screen with dissolve
    "You have finished Soledad Castillo's Journey."
    jump start
