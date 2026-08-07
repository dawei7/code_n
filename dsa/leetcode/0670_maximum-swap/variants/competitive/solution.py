class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = [0] * 10
        for index, digit in enumerate(digits):
            last[int(digit)] = index

        for index, digit in enumerate(digits):
            current = int(digit)
            for replacement in range(9, current, -1):
                replacement_index = last[replacement]
                if replacement_index > index:
                    digits[index], digits[replacement_index] = (
                        digits[replacement_index],
                        digits[index],
                    )
                    return int("".join(digits))
        return num
