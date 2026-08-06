from collections import deque


def solve(startGene: str, endGene: str, bank: list[str]) -> int:
    if startGene == endGene:
        return 0

    unvisited = set(bank)
    if endGene not in unvisited:
        return -1
    unvisited.discard(startGene)

    queue = deque([(startGene, 0)])
    alphabet = "ACGT"
    while queue:
        gene, distance = queue.popleft()
        for i, c in enumerate(gene):
            for replacement in alphabet:
                if replacement == c:
                    continue
                candidate = gene[:i] + replacement + gene[i + 1 :]
                if candidate == endGene:
                    return distance + 1
                if candidate in unvisited:
                    unvisited.remove(candidate)
                    queue.append((candidate, distance + 1))
    return -1
