from collections import deque


def solve(arr, start):
    queue = deque([start])
    seen = {start}
    while queue:
        i = queue.popleft()
        if arr[i] == 0:
            return True
        for nxt in (i + arr[i], i - arr[i]):
            if 0 <= nxt < len(arr) and nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False
