from .Range import Range
from .Point import Point
from .SetTextInCellProps import SetTextInCellProps
from .SetFillInCellProps import SetFillInCellProps


class Cell:
    """
    A cell is a rectangle on the display that can be filled with a colour and have text written in it.
    """

    def __init__(self, x_display_range: Range, y_display_range: Range, text, fill):
        self.top_bounds = y_display_range.start
        self.bottom_bounds = y_display_range.end
        self.left_bounds = x_display_range.start
        self.right_bounds = x_display_range.end

        self.top_left_point = Point(self.left_bounds, self.top_bounds)
        self.top_right_point = Point(self.right_bounds, self.top_bounds)
        self.bottom_left_point = Point(self.left_bounds, self.bottom_bounds)
        self.bottom_right_point = Point(self.right_bounds, self.bottom_bounds)

        self.width = self.right_bounds - self.left_bounds
        self.height = self.bottom_bounds - self.top_bounds

        def __set_text(props: SetTextInCellProps):
            """
            Sets the text in the cell. Note -- This may require the display to be updated to be visible.
            """
            return text(self, props)

        self.set_text = __set_text

        def __set_fill(props: SetFillInCellProps):
            """
            Sets the fill in the cell. Note -- This may require the display to be updated to be visible.
            """
            return fill(self, props)

        self.set_fill = __set_fill
