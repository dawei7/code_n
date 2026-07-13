class LogSystem:
    PREFIX_LENGTH = {
        "Year": 4,
        "Month": 7,
        "Day": 10,
        "Hour": 13,
        "Minute": 16,
        "Second": 19,
    }

    def __init__(self):
        self._logs: list[tuple[int, str]] = []

    def put(self, identifier: int, timestamp: str) -> None:
        self._logs.append((identifier, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
        length = self.PREFIX_LENGTH[granularity]
        lower = start[:length]
        upper = end[:length]
        return [
            identifier
            for identifier, timestamp in self._logs
            if lower <= timestamp[:length] <= upper
        ]


def solve(operations: list[str], arguments: list[list[object]]) -> list[object]:
    storage: LogSystem | None = None
    output: list[object] = []
    for operation, args in zip(operations, arguments):
        if operation == "LogSystem":
            storage = LogSystem()
            output.append(None)
        elif operation == "put":
            storage.put(*args)
            output.append(None)
        else:
            output.append(storage.retrieve(*args))
    return output
