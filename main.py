from services import PicoDisplay
from classes import Point
# set up the display and drawing constants

display = PicoDisplay()
display.set_backlight_percentage(0.5)
display.write_text(Point(30, 30), 'hello world')
display.update()
