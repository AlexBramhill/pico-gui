class FailedToConnectError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Failed to connect to network"
