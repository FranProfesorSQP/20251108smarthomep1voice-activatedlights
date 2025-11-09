sonido = 0
luz = 0
led.enable(False)
strip = neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB)

def on_forever():
    global luz, sonido
    luz = smarthome.read_light_intensity(AnalogPin.P3)
    if luz < 50:
        sonido = smarthome.read_noise(AnalogPin.P2)
        if sonido > 70:
            strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
            basic.pause(10000)
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
basic.forever(on_forever)
