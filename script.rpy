# Declare characters here
# Format: define characterVariable = Character(_("characterName"), color="#colorHexCode")
define t = Character("Terry")


# True when comparing a VN to a book
default book = False

#Game starts here
label start:

    play music "nekoAtsume.mp3"

    scene bg park
    with fade

    "Today, we will be following me on my adventure to find my favourite sunflower seed!"

    show terry
    with fade

    "Oh look! That's me, Terry. My mom likes calling me Ter Bear!"

    t "I decided to go to the park to find my sunflower seed."

    t "Oh no, there are two paths I can go down!"

    t "I seem to be in a pickle, can you help me pick a path to go down?"

    menu:
        t "Which path should I go down?"

        "Go left.":
            jump left

        "Go right.":
            jump right

label right:
    t "Woah! It is really hot out here..."

    "The path was long and winding on this hot and sunny day..."

    "But look up ahead!"

    t "Oh my golly gee, could that be..?"

    "Yes Terry! It is!"

    show sunflower seed
    with fade

    "Your beloved sunflower seed!"

    "And what's that?"

    show water
    with fade

    "And some water to quench your thirsty little hammy throat!"

    "{b}Good Ending: Terry found his sunflower seed and drank to refreshing water!{/b}"

    return

label left:

    show sun
    with fade

    t "Woah! It is really hot out here..."

    "The path was long and winding on this hot and sunny day..."

    scene black
    with dissolve

    "It seems that maybe the path was too long, and too winding, on this very hot and sunny day..."

    "{b}Bad Ending: Terry did not find his sunflower seed...{/b}"

    return
