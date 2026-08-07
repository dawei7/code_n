from typing import List


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        minimum_word_cost = {}
        for word, cost in zip(words, costs):
            minimum_word_cost[word] = min(minimum_word_cost.get(word, cost), cost)

        target_length = len(target)
        best = [float("inf")] * (target_length + 1)
        best[0] = 0

        for start in range(target_length):
            if best[start] == float("inf"):
                continue
            for word, cost in minimum_word_cost.items():
                if target.startswith(word, start):
                    end = start + len(word)
                    best[end] = min(best[end], best[start] + cost)

        return -1 if best[target_length] == float("inf") else best[target_length]
