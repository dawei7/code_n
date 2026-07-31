class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.streak = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.streak += 1
        else:
            self.streak = 0
        return self.streak >= self.k


def solve(commands: list[str], inputs: list[list[int]]) -> list[bool | None]:
    stream = None
    results = []

    for command, arguments in zip(commands, inputs):
        if command == "DataStream":
            stream = DataStream(arguments[0], arguments[1])
            results.append(None)
        else:
            results.append(stream.consec(arguments[0]))

    return results
