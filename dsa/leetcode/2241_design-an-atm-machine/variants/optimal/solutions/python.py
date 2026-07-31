class ATM:
    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.banknotes = [0] * 5

    def deposit(self, banknotesCount: list[int]) -> None:
        for index, count in enumerate(banknotesCount):
            self.banknotes[index] += count

    def withdraw(self, amount: int) -> list[int]:
        used = [0] * 5
        remaining = amount
        for index in range(4, -1, -1):
            count = min(self.banknotes[index], remaining // self.denominations[index])
            used[index] = count
            remaining -= count * self.denominations[index]

        if remaining:
            return [-1]
        for index, count in enumerate(used):
            self.banknotes[index] -= count
        return used


def solve(
    operations: list[str],
    arguments: list[list[object]],
) -> list[object | None]:
    atm = None
    results: list[object | None] = []
    for operation, values in zip(operations, arguments, strict=True):
        if operation == "ATM":
            atm = ATM()
            results.append(None)
            continue
        if atm is None:
            raise ValueError("ATM must be constructed first")
        results.append(getattr(atm, operation)(*values))
    return results
