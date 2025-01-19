from classes import SetTextInCellProps, SetFillInCellProps, Cell


class AbstractDisplay:
    """
    Abstract display class to be inherited by all display classes.

    Due to MicroPython's limitations, abstract methods are not supported, so this class is not truly abstract.
    """

    def set_backlight_percentage(self, value: float) -> None:
        """
        Set the backlight percentage of the display. Uses a float between 0 and 1.
        """
        raise NotImplementedError('Subclasses must implement abstract method')

    def update(self) -> None:
        """
        Sends the display buffer to the display.
        """
        raise NotImplementedError('Subclasses must implement abstract method')

    def get_cell(self) -> None:
        """
        Gets the cell object for the display.
        """
        raise NotImplementedError('Subclasses must implement abstract method')

    def __set_text_in_cell(self, cell: Cell, props: SetTextInCellProps) -> None:
        """
        Function passed to the cell object, and allows for the display to control how drawing text is implemented.

        Note: Display specific default values are set in the SetTextInCellProps class to None, and should be overrided in the display class.
        """
        raise NotImplementedError('Subclasses must implement abstract method')

    def __set_fill_in_cell(self, cell: Cell, colour: SetFillInCellProps) -> None:
        """
        Function passed to the cell object, and allows for the display to control how drawing a fill is implemented.

        Note: Display specific default values are set in the SetTextInCellProps class to None, and should be overrided in the display class.
        """
        raise NotImplementedError('Subclasses must implement abstract method')
