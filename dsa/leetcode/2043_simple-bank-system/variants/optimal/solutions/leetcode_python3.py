from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.balance = [0] + balance

    def _valid(self, account: int) -> bool:
        return 1 <= account < len(self.balance)

    def transfer(
        self, account1: int, account2: int, money: int
    ) -> bool:
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
