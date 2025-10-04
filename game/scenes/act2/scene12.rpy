label scene12:
    scene street with fade

    play music thunder volume 0.5

    window show

    "A few weeks later, Akira was walking alone on a rainy street. After his mother's passing, he'd spent most of his free time wandering the streets like this, aimless and empty."

    "He stopped to sit on a bench and watched his reflection contort in the ripples of a puddle." 
    
    "His phone rang: a call from Suisei."

    play sound pururin_ringtone volume 0.3 
    pause 2.0
    stop sound

    "But he turned it off and put it away."

    stop music fadeout 1.0

    window hide
    pause
    window show

    lyrics """
    Sleep children,\nSleep soundly together, in your warm,\ncomfy and good bed.\n

    I watch over you, always you,\nI will always be by your side, even alone, don't worry,\nI am here by your side.\n

    In the realm of sleep,\nIn a field of flowers, sleep children,\nSleep soundly with me.\n
    """

    teen_akira "Now that you're no longer here, I don't know what to do. I know I was never the best son, but you always loved me in your own way. I've been doing my best to wait for the stars to shine. But all I see is more darkness. What if darkness is all that there is?"

    lyrics """
    Don't worry, children,\nEven if father is not here, don't worry, children,\nYour mother is here.\n

    I watch over you, always you,\nI will always be by your side, children, without feeling,\nGo quickly to sleep.\n

    In their bedroom, without mother.\nIn their bedroom, till the day arrives.\n
    """

    window hide
    pause
    window show

    teen_akira "What if darkness is all that there is?"

    stop music fadeout 1.0

    window hide
    scene solid_black with fade
    pause

    jump scene13
