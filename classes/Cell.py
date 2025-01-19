from .Range import Range
from .Point import Point
from .Set_Text_In_Cell_Props import SetTextInCellProps
from .Set_Fill_In_Cell_Props import SetFillInCellProps


class Cell:
    """
    A cell is a rectangle on the display that can be filled with a colour and have text written in it.
    """

    def __init__(self, x_display_range: Range, y_display_range: Range, set_text, set_fill):
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

        self.__text = set_text
        self.__fill = set_fill

        def __set_text(props: SetTextInCellProps):
            """
            Sets the text in the cell. Note -- This may require the display to be updated to be visible.
            """
            return set_text(self, props)

        self.set_text = __set_text

        def __set_fill(props: SetFillInCellProps):
            """
            Sets the fill in the cell. Note -- This may require the display to be updated to be visible.
            """
            return set_fill(self, props)

        self.set_fill = __set_fill
