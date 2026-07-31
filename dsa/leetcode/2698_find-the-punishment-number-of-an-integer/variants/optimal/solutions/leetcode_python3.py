class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(value: int, target: int) -> bool:
            if target < 0:
                return False
            if value == target:
                return True
            divisor = 10
            while divisor <= value:
                if can_partition(value // divisor, target - value % divisor):
                    return True
                divisor *= 10
            return False

        total = 0
        for value in range(1, n + 1):
            if value % 9 not in (0, 1):
                continue
            square = value * value
            if can_partition(square, value):
                total += square
        return total
