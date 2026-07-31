def solve(digits: list[int]) -> list[int]:
    for index in range(len(digits) - 1, -1, -1):
        if digits[index] < 9:
            digits[index] += 1
            return digits
        digits[index] = 0
    return [1] + digits
