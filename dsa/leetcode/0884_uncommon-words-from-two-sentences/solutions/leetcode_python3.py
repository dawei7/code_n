from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        frequencies = Counter(s1.split())
        frequencies.update(s2.split())
        return [word for word, count in frequencies.items() if count == 1]
