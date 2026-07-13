class TwoSum:
    def __init__(self):
        self.counts: dict[int, int] = {}

    def add(self, number: int) -> None:
        self.counts[number] = self.counts.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for number, count in self.counts.items():
            complement = value - number
            if complement not in self.counts:
                continue
            if complement != number or count >= 2:
                return True
        return False


def solve(operations: list[str], arguments: list[list[int]]) -> list[bool | None]:
    two_sum: TwoSum | None = None
    output: list[bool | None] = []
    for operation, args in zip(operations, arguments):
        if operation == "TwoSum":
            two_sum = TwoSum()
            output.append(None)
        elif operation == "add":
            assert two_sum is not None
            two_sum.add(args[0])
            output.append(None)
        elif operation == "find":
            assert two_sum is not None
            output.append(two_sum.find(args[0]))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
