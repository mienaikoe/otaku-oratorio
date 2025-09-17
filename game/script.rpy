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

    jump overture

    return
