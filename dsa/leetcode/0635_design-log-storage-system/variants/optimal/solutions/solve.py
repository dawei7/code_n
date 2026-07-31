class LogSystem:
    def __init__(self):
        self.logs = []
        self.prefix_length = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19,
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
        length = self.prefix_length[granularity]
        lower = start[:length]
        upper = end[:length]
        return [identifier for identifier, timestamp in self.logs if lower <= timestamp[:length] <= upper]


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
