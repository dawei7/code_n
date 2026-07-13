def _next(number: int) -> int:
    total = 0
    while number:
        number, digit = divmod(number, 10)
        total += digit * digit
    return total


def solve(n: int) -> bool:
    slow = n
    fast = _next(n)
    while slow != fast:
        slow = _next(slow)
        fast = _next(_next(fast))
    return slow == 1
