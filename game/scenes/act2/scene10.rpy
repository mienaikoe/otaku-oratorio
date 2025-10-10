label scene10:
    scene arcade with fade
    play music jojo_peaceful_street_corner volume 0.4

    "One day, Akira had it in his mind to take Suisei on a date (or so he thought)."

    "He had suggested the arcade to show off his unmatched skill in the world's finest arcade game."

    scene ddr:
        zoom 2.3
    with fade

    stop music fadeout 1.0
    pause 1.0

    play sound ddr_ready_set_step volume 0.6
    pause 2.0

    play music hikaru_nara

    window hide
    pause
    window show

    lyrics """
    The rainbow after the rain, the flowers that bloom after the cold,\nBoth are overflowing in different colors\nI fell in love with you that day\nWhen I saw you gazing up at the crimson sky\n

    That moment – a single frame in a drama film –\nWon’t ever vanish, because I’ve engraved it in my heart\n

    You, it was you who taught me\nIf you shine light into the pitch black, it’ll turn into a starry sky\nDon’t hide your sorrow with a smile any longer\nBecause any one of those twinkling stars is enough to make you shine\n

    Having forgotten to sleep, the morning sun pierces right through me\nBut when I see you, I forget all about the headache\nAnd grouchiness I brought with me\n

    The quiet is so romantic – your voice circles around my entire body\nLike a sugar cube melting in tea\n

    You, it was you who smiled at me\nIf you shine light on your tears, they’ll turn into shooting stars\nYour hands have been hurt, but don’t let go\nBecause tomorrow comes from a sky full of wishes\n

    The light that guided me was you\nYou pulled me in and I started to run\nOur paths began to cross without us even realizing it\nSee, if you shine your light, right here, right now…\n

    You, it was you who taught me\nThat because the darkness will come to an end…\n

    You, it was you who taught me\nIf you shine light into the pitch black, it’ll turn into a starry sky\nDon’t hide your sorrow with a smile any longer\nBecause any one of those twinkling stars is enough to make you shine\n

    The answer is always… coincidence? Certainty?\nOne day the path you chose will become your fate\nThe hopes and fears we held onto\nWill surely become the light that moves us forward\n
    """

    window hide
    pause

    stop music fadeout 1.0
    scene arcade with fade

    play sound ddr_stage_clear volume 0.6
    pause 2.0

    teen_suisei "Wowww, I didn't think you'd be that good at DDR!"
    teen_akira "Yeah, I guess the nervous energy has to be put to use somehow."

    scene park with fade
    play music rest fadein 1.0 volume 0.6

    "They moved to the park, where the cherry blossoms were blowing in the wind. Suisei was holding a plushy that Akira had won for her."

    teen_akira "Hey, uh. I just wanted to talk about something important before we go our separate ways. I've wanted to tell you this for a while."
    teen_suisei "Oh of course, you can tell me anything you idiot!"
    teen_akira "We've known each other for a long time, I just get this fuzzy feeling inside, especially when I see you smile or even look at me and I think to myself, “oh god she's not mad at me or anything like that, right?” "
    teen_akira "I guess what I'm saying is that… it feels like you make my heart smile on the inside and I just think I really like you."
    teen_suisei "I… really like you too."
    teen_akira "Oh, so you also?--"
    teen_suisei "–- N-not like that. I mean I like you a lot, you mean a lot to me… You're one of my best friends but… "
    teen_suisei "I've only seen you as a friend… It's not you, it's me… idiot."
    teen_akira "Oh… Well, at least I tried."
    teen_suisei "I'm sorry… I just don't feel the same way as you… But, can we still be friends?"
    teen_akira "Yea…"

    stop music
    window hide
    play sound "<to 3.0>audio/sfx/pururin_ringtone.mp3" volume 0.5
    pause 3.0
    window show

    teen_akira "Hey dad, what's up? What? Wait, slow down. What happened?"

    window hide

    stop sound
    scene solid_black with fade

    jump scene11