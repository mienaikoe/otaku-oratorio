image ssbb_credits = Movie(play="video/ssbb_credits.webm", loop=False)

label epilogue:

    scene living_room_day_present with fade
    play music jojo_peaceful_street_corner volume 0.1

    "Akira, Suisei, and Ivy returned to the living room where they used to play as children. Ivy quickly wired up the Wii while Akira dusted it off."

    adult_suisei "You're not supposed to blow on it like an NES cartridge."
    adult_akira "Gotta take care of her. She's been there for me through middle school, high school, losing my mom, a couple of failed confessions… and now getting hit by a bus…"
    adult_ivy "And we'll keep being there for you too!"
    adult_suisei "Yeah… we're not going anywhere."

    play music wii_startup fadeout 1.0 noloop

    adult_ivy "Well, just because you just got out of the hospital doesn't mean I'll take it easy on you!"
    adult_akira "Still cocky I see."
    adult_ivy "Not cocky, just confident."

    play sound ssbb_wii_menu_banner volume 0.2

    adult_suisei "Shut up, I'm gonna beat you both."

    $ renpy.music.set_volume(1.0, delay=0.0, channel='music')
    $ renpy.music.set_volume(1.0, delay=0.0, channel='sound')
    scene ssbb_credits with fade

    adult_akira "Final destination, no items, Fox only. Let's go!"
    adult_akira "And no skipping the intro!"

    window hide
    pause
    pause
    pause

