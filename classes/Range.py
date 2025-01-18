class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.length = end - start

    def __str__(self):
        return f'start: {self.start}, end: {self.end}, length: {self.length}'
