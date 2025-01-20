from classes import Cell, Range
from math import ceil, floor


class GridCellCreator:
    @staticmethod
    def create(
        x_range: Range,
        y_range: Range,
        set_text_in_cell,
        set_fill_in_cell
    ):
        return Cell(
            x_display_range=x_range,
            y_display_range=y_range,
            set_text=set_text_in_cell,
            set_fill=set_fill_in_cell
        )

    @staticmethod
    def create_cells_from_2d_array(
        x_cell_ranges: list[Range],
        y_cell_ranges: list[Range],
        set_text_in_cell,
        set_fill_in_cell
    ) -> list[list[Cell]]:
        cells = []

        for y_range in y_cell_ranges:
            y_spacing_values = []
            for x_range in x_cell_ranges:
                y_spacing_values.append(
                    GridCellCreator.create(
                        x_range=x_range,
                        y_range=y_range,
                        set_text_in_cell=set_text_in_cell,
                        set_fill_in_cell=set_fill_in_cell
                    )
                )
            cells.append(y_spacing_values)
        return cells
