from collections import defaultdict
from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        word_length = len(words[0])
        by_prefix = defaultdict(list)
        for word in words:
            for length in range(word_length + 1):
                by_prefix[word[:length]].append(word)

        answer = []
        square = []

        def search() -> None:
            row = len(square)
            if row == word_length:
                answer.append(square.copy())
                return

            prefix = "".join(square[previous][row] for previous in range(row))
            for candidate in by_prefix.get(prefix, []):
                square.append(candidate)
                search()
                square.pop()

        search()
        return answer
