class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        current = sum(character in vowels for character in s[:k])
        best = current

        if best == k:
            return best

        for right in range(k, len(s)):
            current += s[right] in vowels
            current -= s[right - k] in vowels
            if current > best:
                best = current
                if best == k:
                    return best

        return best
