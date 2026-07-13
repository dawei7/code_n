from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        unvisited = set(bank)
        if endGene not in unvisited:
            return -1

        queue = deque([(startGene, 0)])
        for_gene = "ACGT"
        while queue:
            gene, distance = queue.popleft()
            for index, original in enumerate(gene):
                for replacement in for_gene:
                    if replacement == original:
                        continue
                    candidate = gene[:index] + replacement + gene[index + 1 :]
                    if candidate == endGene:
                        return distance + 1
                    if candidate in unvisited:
                        unvisited.remove(candidate)
                        queue.append((candidate, distance + 1))
        return -1
