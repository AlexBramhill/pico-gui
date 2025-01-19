from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY
from .abstract_display import AbstractDisplay
import errors
from classes import Point, Rgb, Cell, Range, SetTextInCellProps, SetFillInCellProps


class PicoDisplay(AbstractDisplay):
    def __init__(self):
        self.__display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=90)
        super().__init__()

    def __write_text(self, point: Point, text: str, size: float | int = 2, word_wrap=0, colour: Rgb = Rgb(255, 255, 255), font='bitmap8'):
        pen = self.__display.create_pen(colour.r, colour.g, colour.b)
        self.__display.set_pen(pen)
        self.__display.set_font(font)
        self.__display.text(text, point.x, point.y, 0, size)

    def __draw_rectangle(self, top_left_point: Point, width: int, height: int, colour: Rgb = Rgb(0, 0, 0)):
        pen = self.__display.create_pen(colour.r, colour.g, colour.b)
        self.__display.set_pen(pen)
        self.__display.rectangle(
            top_left_point.x, top_left_point.y, width, height)

    def set_backlight_percentage(self, value):
        if (value < 0) or (value > 1):
            raise errors.PercentageError('Backlight', value)

    def update(self):
        self.__display.update()

    def get_cell(self):
        width, height = self.__display.get_bounds()
        return Cell(Range(0, width), Range(0, height), self.__set_text_in_cell, self.__set_fill_in_cell)

    def __set_text_in_cell(self, cell: Cell, props: SetTextInCellProps):
        text = props.text if props.text is not None else ""
        size = props.size if props.size is not None else 2
        colour = props.colour
        font = props.font if props.font is not None else 'bitmap8'

        self.__write_text(point=cell.top_left_point, text=text,
                          size=size, word_wrap=cell.width, colour=colour, font=font)

    def __set_fill_in_cell(self, cell: Cell, props: SetFillInCellProps):
        colour = props.colour

        self.__draw_rectangle(cell.top_left_point,
                              cell.width, cell.height, colour)
