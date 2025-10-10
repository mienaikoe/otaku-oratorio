label scene_2:

    scene street
    with dissolve

    play music p5_regret fadeout 0.5 fadein 0.5 volume 0.3

    "Ivy ran out of the bar and down the sidewalk after Akira."
    adult_ivy "Akira! Hey, wait up!"
    "Akira stopped walking, but refused to turn around. Ivy stopped a few feet behind."
    adult_ivy "Did something happen back there? Honestly, you’ve seemed pretty down for the whole day - is the old stuff coming back to haunt you again?"
    adult_akira "…Sorry, I don’t really wanna talk about it right now."
    adult_ivy "…Well, alright. I won’t force ya. But I do just wanna say that Suisei and I have been really worried about you. Ever since all... {i}that{/i} happened, you’ve never been the same, which is understandable, but… it’s been years, and we thought by now we’d have the old Akira back."
    "Akira was silent."
    adult_ivy "Akira… please, talk to me. It feels like we’re strangers. What happened to the Akira I know?"
    adult_akira "…He’s gone. I killed him."
    adult_ivy "What… What are you saying, dude? Cut the bullshit--"
    adult_akira "Sorry, man. Just… {i}please{/i} leave me alone."
    "Akira ran away, dropping a MetroCard in the process. Ivy bent down to pick it up."
    adult_ivy "Dude, you dropped something! Hey--"
    "But when he looked up, Akira was halfway down the street. Realizing he was already out of earshot, he heaved a big sigh of frustration. After staring at the MetroCard for a while, he pocketed it."

    play music rain volume 1.0

    window hide
    pause
    window show

    lyrics """
    I don't feel a thing\nAnd I stop remembering\nThe days are just like moments turned to hours

    Mother used to say\nIf you want, you'll find a way\nBut mother never danced through fire showers

    Walk in the rain\nIn the rain, in the rain

    I walk in the rain, in the rain\nIs it right or is it wrong\nAnd is it here that I belong

    I don't hear a sound\nSilent faces in the ground\nQuiet screams, but I refuse to listen

    If there is a hell\nI'm sure this is how it smells\nWish this were a dream, but no, it isn't
    """

    play sound thunder2 volume 0.8

    lyrics """
    Walk in the rain\nIn the rain, in the rain

    I walk in the rain, in the rain\nAm I right or am I wrong\nAnd is it here that I belong
    """

    play sound thunder volume 1.0

    window hide
    pause
    window show

    stop sound fadeout 1.0

    lyrics """
    Walk in the rain\nIn the rain, in the rain

    I walk in the rain, in the rain\nWhy do I feel so alone\nFor some reason I think of home
    """

    window hide
    pause
    window show

    stop music

    "Akira unwittingly walked into the street. Just then, Ivy caught sight of him half a block away."
    play sound bus_approaching
    "Around the corner, a bus was approaching, but Akira didn’t seem to notice the bright lights that were headed toward him."
    play sound screech
    adult_ivy "Akira, look out!"

    stop music fadeout 1.0
    scene solid_white with flash

    pause 2.0

    jump scene_3
