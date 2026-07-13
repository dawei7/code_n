from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        unvisited = set(wordList)
        if endWord not in unvisited:
            return []

        parents = defaultdict(list)
        current_level = {beginWord}
        while current_level and endWord not in current_level:
            unvisited.difference_update(current_level)
            next_level = set()
            for word in current_level:
                for index, original in enumerate(word):
                    for replacement in "abcdefghijklmnopqrstuvwxyz":
                        if replacement == original:
                            continue
                        candidate = word[:index] + replacement + word[index + 1:]
                        if candidate in unvisited:
                            parents[candidate].append(word)
                            next_level.add(candidate)
            current_level = next_level

        if endWord not in current_level:
            return []

        result = []
        reverse_path = [endWord]

        def build(word):
            if word == beginWord:
                result.append(reverse_path[::-1])
                return
            for parent in parents[word]:
                reverse_path.append(parent)
                build(parent)
                reverse_path.pop()

        build(endWord)
        return result
