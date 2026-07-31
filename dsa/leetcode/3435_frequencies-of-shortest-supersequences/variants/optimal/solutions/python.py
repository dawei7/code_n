from itertools import combinations


def solve(words: list[str]) -> list[list[int]]:
    letters = sorted({letter for word in words for letter in word})
    index = {letter: i for i, letter in enumerate(letters)}
    m = len(letters)
    outgoing = [0] * m
    for first, second in words:
        outgoing[index[first]] |= 1 << index[second]

    full = (1 << m) - 1
    for doubled_count in range(m + 1):
        answers: list[list[int]] = []
        for vertices in combinations(range(m), doubled_count):
            doubled = sum(1 << vertex for vertex in vertices)
            remaining = full ^ doubled
            indegree = [0] * m
            for source in range(m):
                if remaining >> source & 1:
                    targets = outgoing[source] & remaining
                    while targets:
                        bit = targets & -targets
                        indegree[bit.bit_length() - 1] += 1
                        targets ^= bit

            ready = 0
            for vertex in range(m):
                if remaining >> vertex & 1 and indegree[vertex] == 0:
                    ready |= 1 << vertex

            visited = 0
            while ready:
                bit = ready & -ready
                ready ^= bit
                source = bit.bit_length() - 1
                visited |= bit
                targets = outgoing[source] & remaining
                while targets:
                    target_bit = targets & -targets
                    target = target_bit.bit_length() - 1
                    indegree[target] -= 1
                    if indegree[target] == 0:
                        ready |= target_bit
                    targets ^= target_bit

            if visited != remaining:
                continue
            frequencies = [0] * 26
            for letter, vertex in index.items():
                frequencies[ord(letter) - ord("a")] = 1 + (
                    doubled >> vertex & 1
                )
            answers.append(frequencies)

        if answers:
            return answers

    return []
