from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY
# set up the display and drawing constants

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=90)
display.set_backlight(0.5)
pen = display.create_pen(255, 255, 255)
font = 'bitmap8'
display.set_pen(pen)
display.set_font(font)
display.text('hello world', 0, 0, 0, 2)
display.update()
