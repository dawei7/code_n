class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        available = [0] * 26
        required = [0] * 26

        for character in s:
            available[ord(character) - ord("a")] += 1
        for character in target:
            required[ord(character) - ord("a")] += 1

        return min(available[index] // required[index] for index in range(26) if required[index])
