class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))

        pivot = len(digits) - 2
        while pivot >= 0 and digits[pivot] >= digits[pivot + 1]:
            pivot -= 1

        if pivot < 0:
            return -1

        successor = len(digits) - 1
        while digits[successor] <= digits[pivot]:
            successor -= 1

        digits[pivot], digits[successor] = (
            digits[successor],
            digits[pivot],
        )
        digits[pivot + 1 :] = reversed(digits[pivot + 1 :])

        result = int("".join(digits))
        return result if result <= 2_147_483_647 else -1

