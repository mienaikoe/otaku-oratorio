define child_akira = Character("Child Akira", color="#910101")
define child_ivy = Character("Child Ivy", color="#00974c")
define child_suisei = Character("Child Suisei", color="#000ecf")

define teen_akira = Character("Teen Akira", color="#910101")
define teen_ivy = Character("Teen Ivy", color="#00974c")
define teen_suisei = Character("Teen Suisei", color="#000ecf")

define adult_akira = Character("Adult Akira", color="#910101")
define adult_ivy = Character("Adult Ivy", color="#00974c")
define adult_suisei = Character("Adult Suisei", color="#000ecf")

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
# image arcade = "arcade.jpeg"
# image ascended_plane = "ascended-plane.png"
# image bar = "bar.jpeg"
# image beach = "beach.png"
# image castle_exterior = "castle_exterior.png"
# image castle_interior = "castle_interior.png"
# image cave = "cave.png"
# image forest = "forest.png"
# image funeral = "funeral.png"
# image game_over = "game_over.png"
image hospital_room = "hospital_room.png" # MISSING IMAGE
# image living_room_day = "living_room_day.png"
# image living_room_night = "living_room_night.png"
# image mountains = "mountains.png"
image park = "town.png" # MISSING IMAGE
# image street = "street.png"
# image town = "town.png"
# image village = "village.png"

image solid_black = Solid("#000000")
image solid_white = Solid("#FFFFFF")

# The game starts here.

label start:

    stop music fadeout 1.0

    jump overture # for act 1
    # jump prologue # for act 2

    return
