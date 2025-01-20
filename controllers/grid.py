import classes
import props
import services


class Grid:
    """
    Represents a grid with specified x_spacing_values and y_spacing_values.

    Provided with the desired proportions of each y_spacing_values and y_spacing_values, this creates a grid of cells

    ie if x_spacing_values = [5, 5, 5] and y_spacing_values = [7.5, 7.5], the grid will be divided into 3 x_spacing_values and 2 y_spacing_values equally spaced.

    It works with absolute and proportional values

    If it is not possible to divide the grid into the specified number of x_spacing_values and y_spacing_values, the last in the x_spacing_values and y_spacing_values list will be shorter
    """
    @staticmethod
    def create_cells(parent_cell: classes.Cell, create_child_cell, props: props.GridProps):
        absolute_summation_spacing_grid_props = services.GridSpacingConverter.convert_spacing_type(
            target='absolute_summation', parent_cell=parent_cell, props=props)
        
        x_cell_ranges, y_cell_ranges = services.GridCellRangeCalculator.compute_grid_ranges(
            props=absolute_summation_spacing_grid_props, parent_cell=parent_cell)

        cells = []
        for y_range in y_cell_ranges:
            y_spacing_values = []
            for x_range in x_cell_ranges:
                y_spacing_values.append(
                    create_child_cell(
                        x_display_range=x_range,
                        y_display_range=y_range,
                    )
                )
            cells.append(y_spacing_values)
        return cells
