from collections import deque


def solve(n: int, p: int, banned: list[int], k: int) -> list[int]:
    values = [list(range(parity, n, 2)) for parity in range(2)]
    parent = [list(range(len(values[parity]) + 1)) for parity in range(2)]

    def find(parity: int, index: int) -> int:
        root = index
        while parent[parity][root] != root:
            root = parent[parity][root]
        while parent[parity][index] != index:
            nxt = parent[parity][index]
            parent[parity][index] = root
            index = nxt
        return root

    def remove(index: int) -> None:
        parity = index & 1
        compressed = index // 2
        parent[parity][compressed] = find(parity, compressed + 1)

    for index in banned:
        remove(index)
    remove(p)

    answer = [-1] * n
    answer[p] = 0
    queue = deque([p])

    while queue:
        current = queue.popleft()
        left_start = max(0, current - k + 1)
        right_start = min(n - k, current)
        low = 2 * left_start + k - 1 - current
        high = 2 * right_start + k - 1 - current
        parity = low & 1

        first = max(0, (low - parity + 1) // 2)
        last = (high - parity) // 2
        cursor = find(parity, first)
        while cursor <= last:
            nxt = values[parity][cursor]
            answer[nxt] = answer[current] + 1
            queue.append(nxt)
            parent[parity][cursor] = find(parity, cursor + 1)
            cursor = find(parity, cursor)

    return answer
