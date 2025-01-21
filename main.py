
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY
from spatial import *

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=90)
width, height = display.get_bounds()

display_cell = CellCreation.create_cell_from_range(
    Range(0, width), Range(0, height))

white = display.create_pen(255, 255, 255)
black = display.create_pen(0, 0, 0)

display.set_pen(white)
display.rectangle(0, 0, width, height)

display.set_pen(black)
subgrid = Grid.create_cell_grid_in_cell(display_cell, props=GridProps(
    spacing_type='percentage', x_spacing_values=[5, 5, 5], y_spacing_values=[7.5, 7.5], margin=5))

for row in subgrid:
    for cell in row:
        display.rectangle(cell.left_bounds, cell.top_bounds,
                          cell.width, cell.height)
