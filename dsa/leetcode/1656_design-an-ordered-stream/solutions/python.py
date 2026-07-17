class OrderedStream:
    def __init__(self, n: int):
        self.values: list[str | None] = [None] * (n + 1)
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.values[idKey] = value
        chunk: list[str] = []
        while self.pointer < len(self.values) and self.values[self.pointer] is not None:
            chunk.append(self.values[self.pointer])
            self.pointer += 1
        return chunk


def solve(operations: list[str], arguments: list[list[object]]) -> list[object]:
    stream = None
    results: list[object] = []
    for operation, values in zip(operations, arguments, strict=True):
        if operation == "OrderedStream":
            stream = OrderedStream(*values)
            results.append(None)
            continue
        if stream is None:
            raise ValueError("OrderedStream must be constructed before insert")
        results.append(stream.insert(*values))
    return results
