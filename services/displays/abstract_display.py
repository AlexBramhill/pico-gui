from classes import Point


class AbstractDisplay:
    def set_backlight_percentage(self, value):
        raise NotImplementedError('Subclasses must implement abstract method')

    def update(self):
        raise NotImplementedError('Subclasses must implement abstract method')

    def get_cell(self):
        raise NotImplementedError('Subclasses must implement abstract method')

    def write_text_in_cell(self, cell, text: str, size, colour, font):
        raise NotImplementedError('Subclasses must implement abstract method')

    def colour_cell(self, cell, colour):
        raise NotImplementedError('Subclasses must implement abstract method')
