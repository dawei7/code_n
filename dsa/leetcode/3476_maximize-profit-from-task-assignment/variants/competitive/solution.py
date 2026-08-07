from collections import Counter, defaultdict
from heapq import heapify, heappop
from typing import List


class Solution:
    def maxProfit(self, workers: List[int], tasks: List[List[int]]) -> int:
        tasks_by_skill = defaultdict(list)
        for required_skill, profit in tasks:
            tasks_by_skill[required_skill].append(-profit)

        for heap in tasks_by_skill.values():
            heapify(heap)

        total_profit = 0
        for skill, worker_count in Counter(workers).items():
            heap = tasks_by_skill.get(skill)
            if not heap:
                continue
            for _ in range(min(worker_count, len(heap))):
                total_profit -= heappop(heap)

        extra_profit = 0
        for heap in tasks_by_skill.values():
            if heap:
                extra_profit = max(extra_profit, -heap[0])

        return total_profit + extra_profit
