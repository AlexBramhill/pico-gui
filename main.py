from services import PicoDisplay
from classes import Point, Rgb, SetFillInCellProps, SetTextInCellProps
# set up the display and drawing constants

display = PicoDisplay()
display.set_backlight_percentage(0.5)
display_cell = display.get_cell()
display_cell.set_fill(SetFillInCellProps(Rgb(255, 0, 0)))
display_cell.set_text(SetTextInCellProps("Hello, World!"))
display.update()
