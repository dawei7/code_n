from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counts = Counter(word)

        for character in counts:
            counts[character] -= 1
            positive_frequencies = {frequency for frequency in counts.values() if frequency > 0}
            counts[character] += 1

            if len(positive_frequencies) <= 1:
                return True

        return False
