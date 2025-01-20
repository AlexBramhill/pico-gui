from services import PicoDisplay
from classes import Rgb
from props import SetFillInCellProps, SetTextInCellProps

display = PicoDisplay()
display.set_backlight_percentage(0.5)
display_cell = display.get_cell()
display_cell.set_fill(SetFillInCellProps(Rgb(255, 0, 0)))
grid_cells = display_cell.create_grid(
    'percentage', [0.25, 0.25, 0.25], [0.33, 0.33], 5)
for y in grid_cells:
    for x in y:
        x.set_fill(SetFillInCellProps(Rgb(0, 255, 0)))
display_cell.set_text(SetTextInCellProps("Hello, World!", colour=Rgb(0, 0, 0)))
display.update()
