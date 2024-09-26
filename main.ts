input.onButtonPressed(Button.A, function () {
    basic.showString("N")
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(input.compassHeading())
})
let grados = 0
let rumbo = "N"
basic.showIcon(IconNames.SmallHeart)
basic.pause(2000)
basic.showNumber(input.compassHeading())
basic.forever(function () {
    grados = input.compassHeading()
    if (grados < 45) {
        rumbo = "N"
        basic.showString(rumbo)
    } else if (grados < 135) {
        rumbo = "E"
        basic.showString(rumbo)
    } else if (grados < 225) {
        rumbo = "S"
        basic.showString(rumbo)
    } else if (grados < 315) {
        rumbo = "W"
        basic.showString(rumbo)
    } else {
        rumbo = "N"
        basic.showString(rumbo)
    }
})
