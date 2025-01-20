from classes import Rgb


class SetTextInCellProps ():
    """
    A class that allows for safe typing of the set text of a cell.
    """

    def __init__(self, text: str, size: float | int | None = None, colour: Rgb = Rgb(255, 255, 255), font: str | None = None):
        self.text = text
        self.size = size
        self.colour = colour
        self.font = font
