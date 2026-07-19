def solve(s: str) -> int:
    length = len(s)
    mismatches_starting_zero = 0
    mismatches_starting_one = 0
    minimum_flips = length

    for right in range(2 * length):
        character = s[right % length]
        expected_zero = "0" if right % 2 == 0 else "1"
        mismatches_starting_zero += character != expected_zero
        mismatches_starting_one += character == expected_zero

        if right >= length:
            left = right - length
            outgoing = s[left % length]
            outgoing_expected_zero = "0" if left % 2 == 0 else "1"
            mismatches_starting_zero -= outgoing != outgoing_expected_zero
            mismatches_starting_one -= outgoing == outgoing_expected_zero

        if right >= length - 1:
            minimum_flips = min(
                minimum_flips,
                mismatches_starting_zero,
                mismatches_starting_one,
            )

    return minimum_flips
