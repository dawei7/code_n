def solve(nums: list[int]) -> int:
    """
    Finds the smallest index i such that i % 10 == sum of digits of i.
    """
    def get_digit_sum(n: int) -> int:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s

    for i in range(len(nums)):
        if i % 10 == get_digit_sum(i):
            return i
            
    return -1
