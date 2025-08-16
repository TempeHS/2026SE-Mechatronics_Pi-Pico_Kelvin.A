from coloursensor import ColourSensor


colourSensor = PiicoDev_VEML6040()

colour = ColourSensor(colourSensor, debug=True)
rgb = colour.sensecolour()
print(f"RGB: {rgb}")

