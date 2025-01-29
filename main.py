
from picographics import PicoGraphics, DISPLAY_INKY_PACK, PEN_1BIT
from libs.spatial import *
from libs.battery import BatteryStatus

display = PicoGraphics(display=DISPLAY_INKY_PACK, pen_type=PEN_1BIT)
width, height = display.get_bounds()

display_cell = CellCreator.create_cell_from_display_dimensions(
    width, height)

white = 15
black = 0

display.set_pen(white)
display.rectangle(0, 0, width, height)

display.set_pen(black)
subgrid = Grid.create_cell_grid_in_cell(display_cell, props=GridProps(
    spacing_type='percentage_summation', x_spacing_values=[0.0], y_spacing_values=[0], margin=2))

for row in subgrid:
    for cell in row:
        display.rectangle(cell.left_bounds, cell.top_bounds,
                          cell.width, cell.height)

is_on_battery = BatteryStatus.is_on_battery()
display.set_pen(white)
display.text(f"Hello, World! \n{BatteryStatus.get_battery_percentage() if is_on_battery else 'N/A'}%, \n{BatteryStatus.get_voltage() if is_on_battery else 'N/A'}V\n"
             f"{'discharging' if is_on_battery else 'charging'}", 10, 10, scale=1)
display.set_update_speed(0)
display.update()
