from collections import defaultdict, deque


def solve(arr):
    if len(arr) <= 1:
        return 0
    positions = defaultdict(list)
    for i, value in enumerate(arr):
        positions[value].append(i)

    queue = deque([(0, 0)])
    seen = {0}
    while queue:
        i, steps = queue.popleft()
        for nxt in positions[arr[i]] + [i - 1, i + 1]:
            if nxt == len(arr) - 1:
                return steps + 1
            if 0 <= nxt < len(arr) and nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, steps + 1))
        positions[arr[i]].clear()
    return -1
