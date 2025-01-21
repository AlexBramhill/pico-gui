from spatial.classes import Cell
from spatial.props import GridProps
from spatial.services import GridCellRangeCalculator, GridSpacingConverter, CellCreation


class Grid:
    """
    Represents a grid with specified x_spacing_values and y_spacing_values.

    Provided with the desired proportions of each y_spacing_values and y_spacing_values, this creates a grid of cells

    ie if x_spacing_values = [5, 5, 5] and y_spacing_values = [7.5, 7.5], the grid will be divided into 3 x_spacing_values and 2 y_spacing_values equally spaced.

    It works with absolute and proportional values

    If it is not possible to divide the grid into the specified number of x_spacing_values and y_spacing_values, the last in the x_spacing_values and y_spacing_values list will be shorter
    """
    @staticmethod
    def create_cell_grid_in_cell(parent_cell: Cell, props: GridProps):
        absolute_summation_spacing_grid_props = GridSpacingConverter.convert_spacing_type(
            target_spacing_type='absolute_summation', parent_cell=parent_cell, props=props
        )

        x_cell_ranges, y_cell_ranges = GridCellRangeCalculator.compute_grid_ranges(
            props=absolute_summation_spacing_grid_props, parent_cell=parent_cell
        )

        return CellCreation.create_cell_grid_from_ranges(
            x_ranges=x_cell_ranges, y_ranges=y_cell_ranges
        )
