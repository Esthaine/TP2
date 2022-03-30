"""

var1 = "Esthaine Itela"

basic.show_string(var1)

"""
# exo2

def on_forever():
    led.plot(3, 2)
    led.unplot(2, 3)
    basic.pause(500)
basic.forever(on_forever)

# exo3

def on_forever():
    if input.button_is_pressed(Button.A):
        images.icon_image(IconNames.HEART).show_image(0)
    elif input.button_is_pressed(Button.B):
          images.icon_images(IconNames.SAD).show_image(0)
basic.forever(on_forever)


# exo4

var2 = 0

def on_forever():
    global var2
    for var1 in range(10):
        var2 = var1 % 2
        if var2 == 0:
            basic.show_number(var1)
basic.forever(on_forever)

def on_forever2():
    global var2
    for var12 in range(10):
        var2 = 0 % 2
        if var2 == 0:
            basic.show_number(var12)
        else:
            var2 = 0 - 0
basic.forever(on_forever2)

# exo6

def on_forever():
    basic.show_leds("""
        # # # # #
                . # # # #
                . . # # #
                . . . # #
                . . . . #
    """)
    basic.clear_screen()
    basic.pause(200)
basic.forever(on_forever)

# exo7

def on_forever():
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    led.plot(1, 2)
    led.unplot(0, 4)
    led.unplot(0, 4)
    basic.pause(500)
basic.forever(on_forever)


# exo8

img4: Image = None
img3: Image = None
img2: Image = None
img1: Image = None
liste: List[Image] = []
pose = 0

def on_forever():
    global img1, img2, img3, img4, liste
    img1 = images.icon_image(IconNames.HEART)
    img2 = images.icon_image(IconNames.SMALL_HEART)
    img3 = images.icon_image(IconNames.YES)
    img4 = images.icon_image(IconNames.TSHIRT)
    liste = [img1, img2, img3, img4]
    
    def on_button_pressed_b():
        global pose
        pose = 0
        while pose < len(liste):
            basic.show_string("" + ("" + str(liste[pose])))
            pose += 1
    input.on_button_pressed(Button.B, on_button_pressed_b)
    
basic.forever(on_forever)


