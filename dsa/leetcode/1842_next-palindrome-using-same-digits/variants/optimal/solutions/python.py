def solve(num: str) -> str:
    """Return the least larger palindrome obtainable from the same digits."""
    digits = list(num)
    half = len(digits) // 2

    pivot = half - 2
    while pivot >= 0 and digits[pivot] >= digits[pivot + 1]:
        pivot -= 1
    if pivot < 0:
        return ""

    successor = half - 1
    while digits[successor] <= digits[pivot]:
        successor -= 1
    digits[pivot], digits[successor] = digits[successor], digits[pivot]
    digits[pivot + 1 : half] = reversed(digits[pivot + 1 : half])

    for index in range(half):
        digits[-1 - index] = digits[index]
    return "".join(digits)
