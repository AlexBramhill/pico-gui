from classes import Point


class Display:
    def set_backlight_percentage(self, value):
        raise NotImplementedError('Subclasses must implement abstract method')

    def draw_rectangle(self, domain, colour):
        raise NotImplementedError('Subclasses must implement abstract method')

    def write_text(self, point: Point, text: str, size, colour, font):
        raise NotImplementedError('Subclasses must implement abstract method')

    def update(self):
        raise NotImplementedError('Subclasses must implement abstract method')
