from math import isqrt


def solve(nums: list[list[int]]) -> int:
    def is_prime(value: int) -> bool:
        if value < 2:
            return False
        if value == 2:
            return True
        if value % 2 == 0:
            return False
        limit = isqrt(value)
        divisor = 3
        while divisor <= limit:
            if value % divisor == 0:
                return False
            divisor += 2
        return True

    n = len(nums)
    answer = 0
    for i in range(n):
        for value in (nums[i][i], nums[i][n - 1 - i]):
            if value > answer and is_prime(value):
                answer = value
    return answer
