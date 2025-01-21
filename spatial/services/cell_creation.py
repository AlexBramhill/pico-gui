from spatial.classes import Cell, Range


class CellCreation:
    @staticmethod
    def create_cell_from_range(x_display_range, y_display_range):
        return Cell(
            x_display_range=x_display_range,
            y_display_range=y_display_range,
        )

    @staticmethod
    def create_cell_grid_from_ranges(x_ranges: list[Range], y_ranges: list[Range]):
        return [
            [
                Cell(
                    x_display_range=x_range,
                    y_display_range=y_range,
                )
                for x_range in y_ranges
            ]
            for y_range in x_ranges
        ]
