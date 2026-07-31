class Solution:
    def calculateScore(self, s: str) -> int:
        unmatched = [[] for _ in range(26)]
        score = 0

        for index, character in enumerate(s):
            letter = ord(character) - ord("a")
            mirror = 25 - letter
            if unmatched[mirror]:
                score += index - unmatched[mirror].pop()
            else:
                unmatched[letter].append(index)

        return score
