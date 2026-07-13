"""Optimal app-local solution for LeetCode 433."""

from collections import deque


def solve(startGene: str, endGene: str, bank: list[str]) -> int:
    if startGene == endGene:
        return 0
    unvisited = set(bank)
    if endGene not in unvisited:
        return -1

    queue = deque([(startGene, 0)])
    alphabet = "ACGT"
    while queue:
        gene, distance = queue.popleft()
        for index, original in enumerate(gene):
            for replacement in alphabet:
                if replacement == original:
                    continue
                candidate = gene[:index] + replacement + gene[index + 1 :]
                if candidate == endGene:
                    return distance + 1
                if candidate in unvisited:
                    unvisited.remove(candidate)
                    queue.append((candidate, distance + 1))
    return -1
