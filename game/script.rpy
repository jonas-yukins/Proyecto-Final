image bus = "Bus.png"
image desert4 = "Desert_4People.png"
image desert20 = "Desert_20People.png"
image stepfather = "Drunk_Stepfather.png"
image gangsters = "Gangsters.png"
image hiding = "Hiding_in_Van.png"
image father = "Speaking_to_Father.png"
image van = "Van.png"
image xray = "Xray_Van.png"

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
    add "Watercolor Map of the Americas.png"  # Replace with the name of your map image (e.g., map_placeholder.jpg)

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

# Start of the game
label start:
    "Welcome to Soledad's journey. Let’s begin the trip."
    jump show_soledad_map

# Checkpoint 1: Honduras
label soledad_cp1:
    scene stepfather  # First image
    with dissolve
    "This is Checkpoint 1: Soledad’s first stop in Honduras."

    scene father  # Second image
    with dissolve
    "She spent the night at a crowded shelter before continuing her journey."

    jump show_soledad_map


# Checkpoint 2: Guatemala
label soledad_cp2:
    scene bus  # Placeholder image for Checkpoint 2 (replace with actual image)
    with dissolve
    "This is Checkpoint 2: Soledad's journey in Guatemala."

    scene gangsters
    with dissolve
    "Gangsters on board"

    jump show_soledad_map

# Checkpoint 3: Mexico Desert
label soledad_cp3:
    scene bg_checkpoint_3  # Placeholder image for Checkpoint 3 (replace with actual image)
    with dissolve
    "This is Checkpoint 3: Soledad's challenging walk through the Mexico desert."
    menu:
        "Back to map":
            jump show_soledad_map

# Checkpoint 4: California
label soledad_cp4:
    scene bg_checkpoint_4  # Placeholder image for Checkpoint 4 (replace with actual image)
    with dissolve
    "This is Checkpoint 4: Soledad's arrival in California."
    menu:
        "Back to map":
            jump show_soledad_map
