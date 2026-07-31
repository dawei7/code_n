from typing import List


def solve(s: str, queries: List[List[int]]) -> List[int]:
    chars = list(s)
    n = len(chars)
    bit = [0] * (n + 1)

    def add(index: int, delta: int) -> None:
        index += 1
        while index <= n:
            bit[index] += delta
            index += index & -index

    def prefix(end: int) -> int:
        total = 0
        while end > 0:
            total += bit[end]
            end -= end & -end
        return total

    def equal_edge(index: int) -> int:
        return int(index > 0 and chars[index] == chars[index - 1])

    for index in range(1, n):
        if chars[index] == chars[index - 1]:
            add(index, 1)
    answer = []
    for query in queries:
        if query[0] == 1:
            index = query[1]
            affected = []
            if index > 0:
                affected.append(index)
            if index + 1 < n:
                affected.append(index + 1)
            for edge in affected:
                add(edge, -equal_edge(edge))
            chars[index] = "B" if chars[index] == "A" else "A"
            for edge in affected:
                add(edge, equal_edge(edge))
        else:
            left, right = (query[1], query[2])
            answer.append(prefix(right + 1) - prefix(left + 1))
    return answer
