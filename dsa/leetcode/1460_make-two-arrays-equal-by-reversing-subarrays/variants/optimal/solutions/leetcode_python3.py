class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        balance = [0] * 1001
        nonzero = 0

        for value in target:
            if balance[value] == 0:
                nonzero += 1
            balance[value] += 1
        for value in arr:
            if balance[value] == 0:
                nonzero += 1
            balance[value] -= 1
            if balance[value] == 0:
                nonzero -= 1

        return nonzero == 0
