def solve(num1: int, num2: int) -> int:
    total = 0
    for number in range(num1, num2 + 1):
        digits = [int(character) for character in str(number)]
        for left, middle, right in zip(digits, digits[1:], digits[2:]):
            if (middle - left) * (middle - right) > 0:
                total += 1
    return total
