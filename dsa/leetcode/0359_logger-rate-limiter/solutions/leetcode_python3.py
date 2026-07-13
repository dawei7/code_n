class Logger:

    def __init__(self):
        self.next_allowed = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp < self.next_allowed.get(message, timestamp):
            return False
        self.next_allowed[message] = timestamp + 10
        return True

