from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY
import services.display
import errors
from classes import Point, Rgb


class PicoDisplay(services.display.Display):
    def __init__(self):
        self.__display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=90)
        super().__init__()

    def set_backlight_percentage(self, value):
        if (value < 0) or (value > 1):
            raise errors.PercentageError('Backlight', value)

    def write_text(self, point: Point, text: str, size: float | int = 2, colour: Rgb = Rgb(255, 255, 255), font='bitmap8'):
        pen = self.__display.create_pen(colour.r, colour.g, colour.b)
        self.__display.set_pen(pen)
        self.__display.set_font(font)
        self.__display.text(text=text, x=point.x, y=point.y, scale=size)

    def update(self):
        self.__display.update()
