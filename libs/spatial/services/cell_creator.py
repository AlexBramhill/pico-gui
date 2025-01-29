from libs.spatial.classes import Cell, Range


class CellCreator:
    @staticmethod
    def create_cell_from_range(x_display_range: Range, y_display_range: Range):
        return Cell(
            x_display_range=x_display_range,
            y_display_range=y_display_range,
        )

    @staticmethod
    def create_cell_from_display_dimensions(width: int, height: int):
        return Cell(
            x_display_range=Range(0, width),
            y_display_range=Range(0, height),
        )

    @staticmethod
    def create_cell_grid_from_ranges(x_ranges: list[Range], y_ranges: list[Range]):
        return [
            [
                Cell(
                    x_display_range=x_range,
                    y_display_range=y_range,
                )
                for x_range in x_ranges
            ]
            for y_range in y_ranges
        ]
