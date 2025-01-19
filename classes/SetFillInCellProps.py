from .Rgb import Rgb


class SetFillInCellProps ():
    """
    A class that allows for safe typing of the set fill of a cell.
    """
    def __init__(self,  colour: Rgb = Rgb(255, 255, 255)):
        self.colour = colour
