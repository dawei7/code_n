def solve(n: int) -> int:
    digits = str(n)
    length = len(digits)
    total = (9**length - 9) // 8
    suffix_count = 9 ** (length - 1)

    for character in digits:
        digit = int(character)
        if digit == 0:
            return total
        total += (digit - 1) * suffix_count
        suffix_count //= 9

    return total + 1
