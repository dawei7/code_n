from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        unvisited = set(wordList)
        if endWord not in unvisited:
            return 0
        queue = deque([(beginWord, 1)])
        unvisited.discard(beginWord)
        while queue:
            word, length = queue.popleft()
            for index, original in enumerate(word):
                for replacement in "abcdefghijklmnopqrstuvwxyz":
                    if replacement == original:
                        continue
                    candidate = word[:index] + replacement + word[index + 1:]
                    if candidate not in unvisited:
                        continue
                    if candidate == endWord:
                        return length + 1
                    unvisited.remove(candidate)
                    queue.append((candidate, length + 1))
        return 0
