from functools import lru_cache


DIGIT_FACTORS = (
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (2, 0, 0, 0),
    (0, 0, 1, 0),
    (1, 1, 0, 0),
    (0, 0, 0, 1),
    (3, 0, 0, 0),
    (0, 2, 0, 0),
)
PACK_DIGITS = (
    (2, 1, 0),
    (3, 0, 1),
    (4, 2, 0),
    (6, 1, 1),
    (8, 3, 0),
    (9, 0, 2),
)


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        required = []
        remainder = t
        for prime in (2, 3, 5, 7):
            exponent = 0
            while remainder % prime == 0:
                remainder //= prime
                exponent += 1
            required.append(exponent)

        if remainder != 1:
            return "-1"

        @lru_cache(None)
        def pack_twos_threes(twos: int, threes: int) -> str:
            if twos == 0 and threes == 0:
                return ""

            best = None
            for digit, adds_two, adds_three in PACK_DIGITS:
                next_twos = max(0, twos - adds_two)
                next_threes = max(0, threes - adds_three)
                if next_twos == twos and next_threes == threes:
                    continue

                candidate = "".join(sorted(str(digit) + pack_twos_threes(next_twos, next_threes)))
                if best is None or (len(candidate), candidate) < (len(best), best):
                    best = candidate

            return best

        def deficits(exponents):
            return tuple(max(0, required[index] - exponents[index]) for index in range(4))

        def minimum_digits(missing):
            return len(pack_twos_threes(missing[0], missing[1])) + missing[2] + missing[3]

        def smallest_suffix(length, missing):
            packed = pack_twos_threes(missing[0], missing[1]) + "5" * missing[2] + "7" * missing[3]
            packed = "".join(sorted(packed))
            return "1" * (length - len(packed)) + packed

        total = [0, 0, 0, 0]
        first_zero = len(num)
        for index, char in enumerate(num):
            digit = ord(char) - ord("0")
            if digit == 0:
                first_zero = index
                break
            factors = DIGIT_FACTORS[digit]
            for prime_index in range(4):
                total[prime_index] += factors[prime_index]

        if first_zero == len(num) and all(total[index] >= required[index] for index in range(4)):
            return num

        start = min(first_zero, len(num) - 1)
        prefix = [0, 0, 0, 0]
        for char in num[:start]:
            factors = DIGIT_FACTORS[ord(char) - ord("0")]
            for prime_index in range(4):
                prefix[prime_index] += factors[prime_index]

        for index in range(start, -1, -1):
            if index < start:
                factors = DIGIT_FACTORS[ord(num[index]) - ord("0")]
                for prime_index in range(4):
                    prefix[prime_index] -= factors[prime_index]

            suffix_length = len(num) - index - 1
            current = ord(num[index]) - ord("0")
            for digit in range(current + 1, 10):
                factors = DIGIT_FACTORS[digit]
                covered = tuple(prefix[prime_index] + factors[prime_index] for prime_index in range(4))
                missing = deficits(covered)
                if minimum_digits(missing) <= suffix_length:
                    return num[:index] + str(digit) + smallest_suffix(suffix_length, missing)

        missing = tuple(required)
        answer_length = max(
            len(num) + 1,
            minimum_digits(missing),
        )
        return smallest_suffix(answer_length, missing)


def solve(num: str, t: int) -> str:
    return Solution().smallestNumber(num, t)
