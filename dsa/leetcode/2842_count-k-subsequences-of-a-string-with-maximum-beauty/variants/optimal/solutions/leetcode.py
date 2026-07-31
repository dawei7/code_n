from collections import Counter
from math import comb


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        modulo = 1_000_000_007
        frequencies = sorted(Counter(s).values(), reverse=True)
        if len(frequencies) < k:
            return 0

        cutoff = frequencies[k - 1]
        higher_count = sum(frequency > cutoff for frequency in frequencies)
        tied_count = sum(frequency == cutoff for frequency in frequencies)
        tied_needed = k - higher_count

        answer = 1
        for frequency in frequencies[:higher_count]:
            answer = answer * frequency % modulo

        answer = answer * pow(cutoff, tied_needed, modulo) % modulo
        answer = answer * comb(tied_count, tied_needed) % modulo
        return answer
