class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pairs = 0

        for first_index in range(len(words)):
            first = words[first_index]

            for second_index in range(first_index + 1, len(words)):
                second = words[second_index]
                if second.startswith(first) and second.endswith(first):
                    pairs += 1

        return pairs
