from collections import deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {character: set() for word in words for character in word}
        indegree = {character: 0 for character in graph}
        for first, second in zip(words, words[1:]):
            if len(first) > len(second) and first.startswith(second):
                return ""
            for left, right in zip(first, second):
                if left == right:
                    continue
                if right not in graph[left]:
                    graph[left].add(right)
                    indegree[right] += 1
                break
        available = deque(character for character, degree in indegree.items() if degree == 0)
        order = []
        while available:
            character = available.popleft()
            order.append(character)
            for neighbor in graph[character]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    available.append(neighbor)
        return "".join(order) if len(order) == len(graph) else ""
