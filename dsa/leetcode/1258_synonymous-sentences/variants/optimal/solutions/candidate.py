from collections import defaultdict
from itertools import product
from typing import List


def solve(synonyms: List[List[str]], text: str) -> List[str]:
    parent: dict[str, str] = {}
    size: dict[str, int] = {}

    def find(word: str) -> str:
        if word not in parent:
            parent[word] = word
            size[word] = 1
        if parent[word] != word:
            parent[word] = find(parent[word])
        return parent[word]

    for left, right in synonyms:
        left_root, right_root = find(left), find(right)
        if left_root == right_root:
            continue
        if size[left_root] < size[right_root]:
            left_root, right_root = right_root, left_root
        parent[right_root] = left_root
        size[left_root] += size[right_root]

    groups: dict[str, list[str]] = defaultdict(list)
    for word in parent:
        groups[find(word)].append(word)
    for words in groups.values():
        words.sort()

    choices = [groups[find(word)] if word in parent else [word] for word in text.split()]
    return [" ".join(sentence) for sentence in product(*choices)]
