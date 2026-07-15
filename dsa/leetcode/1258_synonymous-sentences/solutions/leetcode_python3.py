from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        parent = {}

        def find(word):
            parent.setdefault(word, word)
            if parent[word] != word:
                parent[word] = find(parent[word])
            return parent[word]

        for left, right in synonyms:
            left_root, right_root = find(left), find(right)
            if left_root != right_root:
                parent[right_root] = left_root
        groups = defaultdict(list)
        for word in parent:
            groups[find(word)].append(word)
        for words in groups.values():
            words.sort()
        choices = [groups[find(word)] if word in parent else [word] for word in text.split()]
        return [" ".join(sentence) for sentence in product(*choices)]
