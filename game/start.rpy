define child_akira = Character("Child Akira", color="#910101")
define child_ivy = Character("Child Ivy", color="#00974c")
define child_suisei = Character("Child Suisei", color="#000ecf")

define teen_akira = Character("Teen Akira", color="#910101")
define teen_ivy = Character("Teen Ivy", color="#00974c")
define teen_suisei = Character("Teen Suisei", color="#000ecf")

define adult_akira = Character("Adult Akira", color="#910101")
define adult_ivy = Character("Adult Ivy", color="#00974c")
define adult_suisei = Character("Adult Suisei", color="#000ecf")

define mother = Character("Mother")
define father = Character("Father")

define squirtle = Character("Squirtle")
define fangirls = Character("Fangirls")

define config.has_autosave = False

# config
# default preferences.volume.music = 1.0
# default preferences.volume.sfx = 1.0

# backgrounds
image arcade = "arcade.jpeg"
image ascended_plane = "ascended-plane.jpeg"
image bar = "bar.jpeg"
image castle_exterior = "castle-outside.jpeg"
image castle_interior = "boss_battle.jpeg"
image cave = "cave.jpeg"
image coast = "coast.jpeg"
image forest = "forest.jpeg"
image funeral = "funeral.jpeg"
image hospital_room = "hospital_room.jpeg" # MISSING IMAGE
image living_room_day = "living_room_day.jpeg"
image living_room_night = "living_room_night.jpeg"
image mountains = "mountains.jpeg"
image park = "castle_town.jpeg" # MISSING IMAGE
image street = "street.jpeg"
image town = "town.jpeg"
image village = "village.jpeg"

image solid_black = Solid("#000000")
image solid_white = Solid("#FFFFFF")

# The game starts here.

label start:

    jump prologue

    return
