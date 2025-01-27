class IncorrectStateError(Exception):
    def __init__(self, current_state, expected_state):
        self.current_state = current_state
        self.expected_state = expected_state

    def __str__(self):
        return f"State {self.current_state} is incorrect for this operation ({self.expected_state} expected)"
