from collections import deque


class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.available = deque(range(maxNumbers))
        self.is_available = [True] * maxNumbers

    def get(self) -> int:
        if not self.available:
            return -1
        number = self.available.popleft()
        self.is_available[number] = False
        return number

    def check(self, number: int) -> bool:
        return self.is_available[number]

    def release(self, number: int) -> None:
        if not self.is_available[number]:
            self.is_available[number] = True
            self.available.append(number)


def solve(max_numbers: int, operations: list[list]) -> list:
    directory = PhoneDirectory(max_numbers)
    results = []
    for operation in operations:
        name = operation[0]
        if name == "get":
            results.append(directory.get())
        elif name == "check":
            results.append(directory.check(operation[1]))
        else:
            directory.release(operation[1])
    return results
