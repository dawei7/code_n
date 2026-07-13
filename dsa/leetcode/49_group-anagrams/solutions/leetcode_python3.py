from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            counts = [0] * 26
            for character in word:
                counts[ord(character) - ord("a")] += 1
            key = tuple(counts)
            groups.setdefault(key, []).append(word)
        return list(groups.values())
