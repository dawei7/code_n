def solve(s: str, queries: list[list[int]]) -> list[int]:
    modulus = 1_000_000_007
    digits = [ord(character) - ord("0") for character in s if character != "0"]

    boundary_rank = [0]
    retained = 0
    for character in s:
        retained += character != "0"
        boundary_rank.append(retained)

    concatenated = [0] * (len(digits) + 1)
    digit_totals = [0] * (len(digits) + 1)
    decimal_shifts = [1] * (len(digits) + 1)
    for length, digit in enumerate(digits, start=1):
        concatenated[length] = (concatenated[length - 1] * 10 + digit) % modulus
        digit_totals[length] = digit_totals[length - 1] + digit
        decimal_shifts[length] = decimal_shifts[length - 1] * 10 % modulus

    results = []
    for left, right in queries:
        start = boundary_rank[left]
        stop = boundary_rank[right + 1]
        width = stop - start
        value = (
            concatenated[stop] - concatenated[start] * decimal_shifts[width]
        ) % modulus
        results.append(value * (digit_totals[stop] - digit_totals[start]) % modulus)
    return results
