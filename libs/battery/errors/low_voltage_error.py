class LowVoltageError(Exception):
    def __init__(self, voltage):
        self.voltage = voltage

    def __str__(self):
        return f"Low voltage error: {self.voltage}V"
