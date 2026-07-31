from collections import defaultdict


def solve(nums: list[int]) -> int:
    seen = defaultdict(int)
    pairs = 0

    for value in sorted(nums):
        digits = list(str(value))
        reachable = {value}
        width = len(digits)

        for first_left in range(width):
            for first_right in range(first_left + 1, width):
                digits[first_left], digits[first_right] = (
                    digits[first_right],
                    digits[first_left],
                )
                reachable.add(int("".join(digits)))

                for second_left in range(width):
                    for second_right in range(second_left + 1, width):
                        digits[second_left], digits[second_right] = (
                            digits[second_right],
                            digits[second_left],
                        )
                        reachable.add(int("".join(digits)))
                        digits[second_left], digits[second_right] = (
                            digits[second_right],
                            digits[second_left],
                        )

                digits[first_left], digits[first_right] = (
                    digits[first_right],
                    digits[first_left],
                )

        pairs += sum(seen[candidate] for candidate in reachable)
        seen[value] += 1

    return pairs
