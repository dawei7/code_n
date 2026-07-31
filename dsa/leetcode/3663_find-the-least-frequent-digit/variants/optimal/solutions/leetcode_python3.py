from collections import Counter


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        frequency = Counter(str(n))
        return int(min(frequency, key=lambda digit: (frequency[digit], digit)))
