from .Range import Range
from .Point import Point


class Cell:
    def __init__(self, x_display_range: Range, y_display_range: Range):
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
