define child_akira = Character("Child Akira", color="#fd7979")
define child_ivy = Character("Child Ivy", color="#3fe692")
define child_suisei = Character("Child Suisei", color="#7981fa")

define stranger = Character("Stranger", color="#814444")
define teen_akira = Character("Teen Akira", color="#fd7979")
define teen_ivy = Character("Teen Ivy", color="3fe692")
define teen_suisei = Character("Teen Suisei", color="#7981fa")

define adult_akira = Character("Adult Akira", color="#fd7979")
define adult_ivy = Character("Adult Ivy", color="3fe692")
define adult_suisei = Character("Adult Suisei", color="#7981fa")

define nurse = Character("Nurse", color="#fff")

define mother = Character("Mother", color="#fff")
define father = Character("Father", color="#fff")

define squirtle = Character("Squirtle", color="#5856d1")
define fangirls = Character("Fangirls", color="#fff")

define both_1 = Character("Akira and Suisei", color="#fff")

define lyrics = Character(None, what_italic=True)

define config.has_autosave = False
define config.main_menu_music = "audio/bgm/plastic_love.mp3"

# config
default preferences.volume.music = 1.0
default preferences.volume.sfx = 1.0

image solid_black = Solid("#000000")
image solid_white = Solid("#FFFFFF")

define flash = Fade(0.5, 0, 0.5, color="#0f0e0e")

# The game starts here.
label start:
    stop music fadeout 1.0

    # jump overture # for act 1
    # jump prologue # for act 2
    jump scene_2

    return
