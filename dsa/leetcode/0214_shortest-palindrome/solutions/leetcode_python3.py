class Solution:
    def shortestPalindrome(self, s: str) -> str:
        combined = s + "#" + s[::-1]
        prefix = [0] * len(combined)
        for index in range(1, len(combined)):
            matched = prefix[index - 1]
            while matched and combined[index] != combined[matched]:
                matched = prefix[matched - 1]
            if combined[index] == combined[matched]:
                matched += 1
            prefix[index] = matched
        palindrome_length = prefix[-1] if prefix else 0
        return s[palindrome_length:][::-1] + s
