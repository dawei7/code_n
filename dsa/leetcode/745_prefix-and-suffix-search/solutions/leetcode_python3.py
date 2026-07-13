from typing import List


class WordFilter:
    def __init__(self, words: List[str]):
        self.lookup = {}
        for index, word in enumerate(words):
            for prefix_end in range(len(word) + 1):
                prefix = word[:prefix_end]
                for suffix_start in range(len(word) + 1):
                    self.lookup[(prefix, word[suffix_start:])] = index

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get((pref, suff), -1)
