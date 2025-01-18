from services import PicoDisplay
from classes import Point, Rgb
# set up the display and drawing constants

display = PicoDisplay()
display.set_backlight_percentage(0.5)
display_cell = display.get_cell()
display.colour_cell(display_cell, Rgb(255, 0, 0))
display.write_text_in_cell(display_cell, 'hello world')
display.update()
