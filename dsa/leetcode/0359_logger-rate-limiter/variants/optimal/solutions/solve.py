class Logger:
    def __init__(self):
        self.next_allowed = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp < self.next_allowed.get(message, timestamp):
            return False
        self.next_allowed[message] = timestamp + 10
        return True


def solve(operations: list[list]) -> list[bool]:
    logger = Logger()
    return [logger.shouldPrintMessage(timestamp, message) for _, timestamp, message in operations]
