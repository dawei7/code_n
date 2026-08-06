"""Candidate solution for LeetCode 1088: Confusing Number II."""


ROTATABLE_DIGITS = "01689"
NONZERO_ROTATABLE_DIGITS = "1689"
UNCHANGED_CENTER_DIGITS = "018"
ROTATION = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}


def solve(n: int) -> int:
    digits = str(n)

    def count_rotatable() -> int:
        total = sum(4 * 5 ** (length - 1) for length in range(1, len(digits)))
        for position, digit in enumerate(digits):
            choices = NONZERO_ROTATABLE_DIGITS if position == 0 else ROTATABLE_DIGITS
            remaining = len(digits) - position - 1
            total += sum(choice < digit for choice in choices) * 5**remaining
            if digit not in choices:
                return total
        return total + 1

    def choices_at(length: int, position: int) -> str:
        if position == 0:
            return "18" if length == 1 else NONZERO_ROTATABLE_DIGITS
        if position * 2 == length - 1:
            return UNCHANGED_CENTER_DIGITS
        return ROTATABLE_DIGITS

    def count_unchanged() -> int:
        total = 0
        for length in range(1, len(digits)):
            combinations = 1
            for position in range((length + 1) // 2):
                combinations *= len(choices_at(length, position))
            total += combinations

        half_length = (len(digits) + 1) // 2
        for position in range(half_length):
            choices = choices_at(len(digits), position)
            remaining_combinations = 1
            for remaining_position in range(position + 1, half_length):
                remaining_combinations *= len(choices_at(len(digits), remaining_position))
            total += sum(choice < digits[position] for choice in choices) * remaining_combinations
            if digits[position] not in choices:
                return total

        candidate = list(digits)
        for position in range(half_length):
            candidate[-position - 1] = ROTATION[digits[position]]
        if int("".join(candidate)) <= n:
            total += 1
        return total

    return count_rotatable() - count_unchanged()
