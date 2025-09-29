define child_akira = Character("Child Akira", color="#fd7979")
define child_ivy = Character("Child Ivy", color="#3fe692")
define child_suisei = Character("Child Suisei", color="#7981fa")

define stranger = Character("Stranger", color="#814444")
define teen_akira = Character("Teen Akira", color="#814444")
define teen_ivy = Character("Teen Ivy", color="#008a45")
define teen_suisei = Character("Teen Suisei", color="#000ecf")

define adult_akira = Character("Adult Akira", color="#520101")
define adult_ivy = Character("Adult Ivy", color="#00481d")
define adult_suisei = Character("Adult Suisei", color="#00065e")

define nurse = Character("Nurse")

define mother = Character("Mother")
define father = Character("Father")

define squirtle = Character("Squirtle")
define fangirls = Character("Fangirls")

define both_1 = Character("Akira and Suisei")

define config.has_autosave = False
define config.main_menu_music = "audio/music/plastic_love.mp3"

# config
# default preferences.volume.music = 1.0
# default preferences.volume.sfx = 1.0

# backgrounds
image park = "town.png" # MISSING IMAGE

image solid_black = Solid("#000000")
image solid_white = Solid("#FFFFFF")

# The game starts here.
label start:
    stop music fadeout 1.0

    # jump overture # for act 1
    # jump prologue # for act 2
    jump scene_8

    return
