class Bank:
    def __init__(self, balance: list[int]):
        self.balance = [0] + balance

    def _valid(self, account: int) -> bool:
        return 1 <= account < len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            not self._valid(account1)
            or not self._valid(account2)
            or self.balance[account1] < money
        ):
            return False

        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False

        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if (
            not self._valid(account)
            or self.balance[account] < money
        ):
            return False

        self.balance[account] -= money
        return True


def solve(operations: list[str], arguments: list[list]) -> list[bool | None]:
    bank: Bank | None = None
    output: list[bool | None] = []

    for operation, args in zip(operations, arguments):
        if operation == "Bank":
            bank = Bank(args[0])
            output.append(None)
        elif operation == "transfer":
            assert bank is not None
            output.append(bank.transfer(args[0], args[1], args[2]))
        elif operation == "deposit":
            assert bank is not None
            output.append(bank.deposit(args[0], args[1]))
        elif operation == "withdraw":
            assert bank is not None
            output.append(bank.withdraw(args[0], args[1]))
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output
