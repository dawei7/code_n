class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        pairs = 0

        for word in words:
            if word[::-1] in seen:
                pairs += 1
            else:
                seen.add(word)

        return pairs
