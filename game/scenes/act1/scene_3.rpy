label scene_3:

    scene hospital
    with dissolve

    stop music fadeout 1.0

    pause 1.0

    play music bittersweet volume 0.3
    play sound ekg volume 0.1 loop

    "Akira was laid up in a hospital bed, bandaged all over and hooked up to all sorts of machines."

    "The nurse entered to check his vitals. She fluffed his pillows and tucked him in."

    nurse "You okay? Hanging in there?" 

    nurse "Your friends were out there all night. The loud one kept blaming himself, said he wasn’t fast enough. The girl kept saying “I’m not crying”. She was totally crying." 

    nurse "Stick with it. Your friends are waiting for you."

    stop sound fadeout 0.5
    stop music fadeout 0.5

    window hide
    pause
    window show

    lyrics """
    Why do we cling together?\nWhy do we give punishment to lesser hearts?

    The Planet did not forgive us\nDid not forgive us\nThe Planet did not forgive us\nDid not forgive us

    The pulse of veins flows through the earth\nA faint, faint pulse\nOf a heart drawn to death

    A gentle life returns to the planet\nIs it necessary to sacrifice souls?

    Why do we cling together?\nWhy do we beg for forgiveness?\nIn the Promised Land?
    """

    scene solid_white with flash

    window hide
    pause
    window show

    jump scene_4
