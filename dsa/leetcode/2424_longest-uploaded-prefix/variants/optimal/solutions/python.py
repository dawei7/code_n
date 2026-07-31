class LUPrefix:
    def __init__(self, n: int):
        self.uploaded = [False] * (n + 2)
        self.prefix = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.uploaded[self.prefix + 1]:
            self.prefix += 1

    def longest(self) -> int:
        return self.prefix


def solve(n: int, operations: list[list]) -> list[int | None]:
    server = LUPrefix(n)
    output = []

    for name, arguments in operations:
        if name == "upload":
            server.upload(arguments[0])
            output.append(None)
        else:
            output.append(server.longest())

    return output
