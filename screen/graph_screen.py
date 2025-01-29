from time import sleep
import sys
from picographics import PicoGraphics, DISPLAY_INKY_PACK, PEN_1BIT
from libs.spatial import *
from .graph_screen_data import GraphScreenData

"""
 A quick screen to look at how long a 1200mAh battery would last
"""


class GraphScreen ():
    display = PicoGraphics(display=DISPLAY_INKY_PACK, pen_type=PEN_1BIT)

    foreground = 0
    background = 15

    @staticmethod
    def write_header_to_graphics_buffer(header_cell, battery_props):
        header_subgrid = Grid.create_cell_grid_in_cell(header_cell,
                                                       props=GridProps(
                                                           spacing_type='percentage_summation',
                                                           x_spacing_values=[
                                                               0.5],
                                                           y_spacing_values=[
                                                               0],
                                                           margin=1
                                                       )
                                                       )

        header_left_cell = header_subgrid[0][0]
        header_right_cell = header_subgrid[0][1]

        GraphScreen.display.set_pen(GraphScreen.foreground)
        GraphScreen.display.text(
            f"Graph Screen\n"
            f"Is on battery: {battery_props["is_on_battery"]}\n",
            header_left_cell.left_bounds,
            header_left_cell.top_bounds,
            scale=1
        )

        left_side_text = f"Battery Percentage: {battery_props["battery_percentage"]}\nVoltage: {battery_props["voltage"]}" if battery_props[
            "is_on_battery"] else 'Use battery power to see battery data'
        GraphScreen.display.text(
            left_side_text,
            header_right_cell.left_bounds,
            header_right_cell.top_bounds,
            wordwrap=header_right_cell.width,
            scale=1
        )

    @staticmethod
    def write_last_update_information_to_graphics_buffer(last_update_grid, last_updated_props):
        GraphScreen.display.set_pen(GraphScreen.foreground)
        GraphScreen.display.rectangle(last_update_grid.left_bounds, last_update_grid.top_bounds,
                                      last_update_grid.width, last_update_grid.height)

        last_update_subgrid = Grid.create_cell_grid_in_cell(last_update_grid, props=GridProps(
            spacing_type='absolute',
            x_spacing_values=[100],
            y_spacing_values=[8, 8, 8],
            margin=1
        ))

        GraphScreen.display.set_pen(GraphScreen.background)

        GraphScreen.display.text(
            "First Sync Time:",
            last_update_subgrid[0][0].left_bounds,
            last_update_subgrid[0][0].top_bounds,
            scale=1
        )

        GraphScreen.display.text(
            f"{last_updated_props['first_sync_time']}",
            last_update_subgrid[0][1].left_bounds,
            last_update_subgrid[0][1].top_bounds,
            scale=1
        )

        GraphScreen.display.text(
            "Last Updated:",
            last_update_subgrid[1][0].left_bounds,
            last_update_subgrid[1][0].top_bounds,
            scale=1
        )

        GraphScreen.display.text(
            f"{GraphScreenData.get_time()}",
            last_update_subgrid[1][1].left_bounds,
            last_update_subgrid[1][1].top_bounds,
            scale=1
        )

        GraphScreen.display.text(
            "Failed to update:",
            last_update_subgrid[2][0].left_bounds,
            last_update_subgrid[2][0].top_bounds,
            scale=1
        )

        GraphScreen.display.text(
            f"{last_updated_props['failed_time_update_count']}",
            last_update_subgrid[2][1].left_bounds,
            last_update_subgrid[2][1].top_bounds,
            scale=1
        )

    @staticmethod
    def write_x_axis_to_graphics_buffer(x_axis_master_cell):
        x_axis_grid = Grid.create_cell_grid_in_cell(x_axis_master_cell, props=GridProps(
            spacing_type='percentage',
            x_spacing_values=[0.9],
            y_spacing_values=[1/8] * 8,
            margin=1
        ))

        GraphScreen.display.set_pen(GraphScreen.foreground)

        for i in range(len(x_axis_grid)):
            cell = x_axis_grid[i][1]
            GraphScreen.display.rectangle(cell.left_bounds, cell.top_bounds,
                                          cell.width, 1)

        GraphScreen.display.set_pen(GraphScreen.foreground)

        # Interesting and not nice copilot way of doing this...
        voltage_text = 4.2
        for i in range(len(x_axis_grid)):
            cell = x_axis_grid[i][0]
            GraphScreen.display.text(
                f"{voltage_text:.1f}V", cell.left_bounds, cell.top_bounds - 3, scale=0.5)
            voltage_text -= 0.2

    @staticmethod
    def write_graph_to_graphics_buffer(graph_master_cell, historical_data):
        graph_length = len(historical_data)
        graph_divisions = Grid.create_cell_grid_in_cell(graph_master_cell, props=GridProps(
            spacing_type='percentage',
            x_spacing_values=[1/graph_length] * graph_length,
            y_spacing_values=[0],
            margin=0
        ))

        GraphScreen.display.set_pen(GraphScreen.foreground)

        for i in range(graph_length):
            data = historical_data[i]
            if data["battery_percentage"] == "N/A%":
                pass
            else:
                percentage = float(
                    data["battery_percentage"].split("%")[0])/100

                if percentage <= 0.0:
                    continue

                to_colour_area = Grid.create_cell_grid_in_cell(graph_divisions[0][i], props=GridProps(
                    spacing_type='percentage',
                    x_spacing_values=[0],
                    y_spacing_values=[
                        1 - percentage],
                    margin=0
                ))

                GraphScreen.display.set_pen(GraphScreen.foreground)
                GraphScreen.display.rectangle(
                    to_colour_area[-1][0].left_bounds,
                    to_colour_area[-1][0].top_bounds,
                    to_colour_area[-1][0].width,
                    to_colour_area[-1][0].height
                )

    @staticmethod
    def write_graph_information_to_graphics_buffer(graph_cell, historical_data):
        GraphScreen.display.set_pen(GraphScreen.foreground)
        GraphScreen.display.rectangle(graph_cell.left_bounds, graph_cell.top_bounds,
                                      graph_cell.width, graph_cell.height)

        graph_grid = Grid.create_cell_grid_in_cell(graph_cell, props=GridProps(
            spacing_type='absolute',
            x_spacing_values=[22],
            y_spacing_values=[graph_cell.height - 10],
            margin=1
        ))

        GraphScreen.display.set_pen(GraphScreen.background)
        for row in graph_grid:
            for cell in row:
                GraphScreen.display.rectangle(cell.left_bounds, cell.top_bounds,
                                              cell.width, cell.height)

        graph_x_axis_cell = graph_grid[0][0]
        graph_y_axis_cell = graph_grid[0][1]
        graph_data_cell = graph_grid[0][1]

        GraphScreen.write_x_axis_to_graphics_buffer(graph_x_axis_cell)
        GraphScreen.write_graph_to_graphics_buffer(
            graph_data_cell, historical_data)

    @staticmethod
    def render(data_props):
        width, height = GraphScreen.display.get_bounds()

        display_cell = CellCreator.create_cell_from_display_dimensions(
            width, height)

        GraphScreen.display.set_pen(GraphScreen.foreground)
        GraphScreen.display.rectangle(0, 0, width, height)

        GraphScreen.display.set_pen(GraphScreen.background)
        main_grid = Grid.create_cell_grid_in_cell(display_cell, props=GridProps(
            spacing_type='absolute', x_spacing_values=[0.0], y_spacing_values=[8 * 2, 8 * 3, 8], margin=0))

        # Background colour through colouring the cells
        for row in main_grid:
            for cell in row:
                GraphScreen.display.rectangle(cell.left_bounds, cell.top_bounds,
                                              cell.width, cell.height)

        GraphScreen.write_header_to_graphics_buffer(
            main_grid[0][0], data_props
        )

        GraphScreen.write_last_update_information_to_graphics_buffer(
            main_grid[1][0], data_props
        )

        GraphScreen.write_graph_information_to_graphics_buffer(
            main_grid[3][0], data_props['historical_data']
        )
        GraphScreen.display.set_update_speed(0)
        GraphScreen.display.update()

    @staticmethod
    def run():
        iteration_count = 0
        failed_time_update_count = 0
        first_sync_time = "No sync yet"
        last_sync_time = "No sync yet"

        historical_data = []

        # while True:
        try:
            time = GraphScreenData.get_time_from_api()
            GraphScreenData.set_time(time)
            # This needs improving to avoid microsecond misreporting
            time_now = GraphScreenData.get_time()

            if (first_sync_time == "No sync yet"):
                first_sync_time = time_now
            last_sync_time = time_now

        except Exception as e:
            print(e)
            sys.print_exception(e)  # type: ignore

            failed_time_update_count += 1

        finally:
            iteration_count += 1

            data_props = GraphScreenData.get_data()
            data_props["failed_time_update_count"] = failed_time_update_count
            data_props["first_sync_time"] = first_sync_time
            data_props["last_sync_time"] = last_sync_time
            historical_data.append({
                'time': time_now,
                'iteration_count': iteration_count,
                'voltage': data_props['voltage'],
                'battery_percentage': data_props['battery_percentage'],
                'is_on_battery': data_props['is_on_battery']
            })

            data_props['historical_data'] = historical_data

            GraphScreen.render(data_props)
