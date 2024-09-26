def on_button_pressed_a():
    basic.show_string("N")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(input.compass_heading())
input.on_button_pressed(Button.AB, on_button_pressed_ab)

grados = 0
rumbo = "N"
basic.show_icon(IconNames.SMALL_HEART)
basic.pause(2000)
basic.show_number(input.compass_heading())

def on_forever():
    global grados, rumbo
    grados = input.compass_heading()
    if grados < 45:
        rumbo = "N"
        basic.show_string(rumbo)
    elif grados < 135:
        rumbo = "E"
        basic.show_string(rumbo)
    elif grados < 225:
        rumbo = "S"
        basic.show_string(rumbo)
    elif grados < 315:
        rumbo = "W"
        basic.show_string(rumbo)
    else:
        basic.show_string("N")
basic.forever(on_forever)
