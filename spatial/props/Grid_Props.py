from consts import SpacingTypeArray


class GridProps:
    def __init__(self, spacing_type: str, x_spacing_values: list[int] | list[float | int], y_spacing_values: list[int] | list[float | int], margin: int = 0):
        if spacing_type not in SpacingTypeArray:
            raise ValueError(
                f"Unsupported spacing type: {spacing_type}. Supported types: {SpacingTypeArray}")
        self.spacing_type = spacing_type
        self.x_spacing_values = x_spacing_values
        self.y_spacing_values = y_spacing_values
        self.margin = margin
