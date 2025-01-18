from classes import Point


class AbstractDisplay:
    def set_backlight_percentage(self, value):
        raise NotImplementedError('Subclasses must implement abstract method')

    def draw_rectangle(self, domain, colour):
        raise NotImplementedError('Subclasses must implement abstract method')

    def write_text(self, point: Point, text: str, size, colour, font):
        raise NotImplementedError('Subclasses must implement abstract method')

    def update(self):
        raise NotImplementedError('Subclasses must implement abstract method')

    def get_height(self):
        raise NotImplementedError('Subclasses must implement abstract method')

    def get_width(self):
        raise NotImplementedError('Subclasses must implement abstract method')

    def get_cell(self):
        raise NotImplementedError('Subclasses must implement abstract method')

    def write_text_in_cell(self, cell, text: str, size, colour, font):
        self.write_text(cell.top_left_point, text, size, colour, font)
