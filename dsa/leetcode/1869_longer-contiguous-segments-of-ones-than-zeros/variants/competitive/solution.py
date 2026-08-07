class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest = [0, 0]
        current_digit = s[0]
        current_length = 0

        for digit in s:
            if digit == current_digit:
                current_length += 1
            else:
                index = 1 if current_digit == "1" else 0
                longest[index] = max(longest[index], current_length)
                current_digit = digit
                current_length = 1

        index = 1 if current_digit == "1" else 0
        longest[index] = max(longest[index], current_length)
        return longest[1] > longest[0]
