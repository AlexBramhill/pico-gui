class PercentageError(Exception):
    def __init__(self, name: str, value: float | int):
        self.message = f'{
            name} is a percentage must be between 0 and 1, current value: {value}'
        super().__init__(self.message)
