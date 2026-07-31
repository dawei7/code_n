class Solution:
    def digitCount(self, num: str) -> bool:
        frequencies = [0] * 10
        for digit in num:
            frequencies[ord(digit) - ord("0")] += 1

        return all(
            frequencies[index] == ord(required) - ord("0")
            for index, required in enumerate(num)
        )
