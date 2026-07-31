class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord("a")] += 1

        left_parts = []
        middle = ""
        for index, count in enumerate(counts):
            char = chr(ord("a") + index)
            left_parts.append(char * (count // 2))
            if count % 2:
                middle = char

        left = "".join(left_parts)
        return left + middle + left[::-1]
