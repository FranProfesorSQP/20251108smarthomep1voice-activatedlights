let sonido = 0
let luz = 0
led.enable(false)
let strip = neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB)
basic.forever(function () {
    luz = smarthome.ReadLightIntensity(AnalogPin.P3)
    if (luz < 50) {
        sonido = smarthome.ReadNoise(AnalogPin.P2)
        if (sonido > 70) {
            strip.showColor(neopixel.colors(NeoPixelColors.White))
            basic.pause(10000)
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
        }
    }
})
