class Solution:
    def minSteps(self, s: str, t: str) -> int:
        differences = [0] * 26
        for character in s:
            differences[ord(character) - ord("a")] += 1
        for character in t:
            differences[ord(character) - ord("a")] -= 1
        return sum(abs(difference) for difference in differences)
