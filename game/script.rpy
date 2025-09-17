import "overture" 



define child_akira = Character("Akira")
define child_ivy = Character("Ivy")
define child_suisei = Character("Suisei")

define teen_akira = Character("Akira", color="#c8ffc8")
define teen_ivy = Character("Ivy", color="#ffc8c8")
define teen_suisei = Character("Suisei", color="#c8c8ff")

define adult_akira = Character("Akira", color="#c8ffc8")
define adult_ivy = Character("Ivy", color="#ffc8c8")
define adult_suisei = Character("Suisei", color="#c8c8ff")

define mother = Character("Mother", color="#ffffc8")
define father = Character("Father", color="#c8ffff")

define squirtle = Character("Squirtle", color="#c8c8c8")
define fangirls = Character("Fangirls", color="#ffc8ff")

# config
default preferences.volume.music = 0.5
default preferences.volume.sfx = 0.5

# backgrounds
image coast = "coast.jpeg"


# The game starts here.

label start:

    # Scene 1
    scene coast

    play music "audio/music/chill-garden.mp3"

    # play audio [ "<silence .5>", "audio/sfx/airhorn.ogg" ]

    "The year was 2012. The Olympics were in London, Obama was about to be re-elected, and the timeline still kind of made sense."

    "It is upon this backdrop that we discover our heroes for today. Three kids - Akira, Suisei, and Ivy - were enjoying their last weeks of their summer break, lounging in the living room to play the Nintendo Wii, as was customary at the time." 
    
    "Ivy’s phone played a notification tone from “Gangnam Style” as was also customary at the time."

    child_akira "You've created a new Ren'Py game."

    child_akira "Once you add a story, pictures, and music, you can release it to the world!"

    jump overture

    # This ends the game.

    return
