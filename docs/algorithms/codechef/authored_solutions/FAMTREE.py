import sys


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    worth = [0] + data[1:1 + n]
    parents = [0] + data[1 + n:1 + 2 * n]

    children = [[] for _ in range(n + 1)]
    root = 1
    for node in range(1, n + 1):
        parent = parents[node]
        if parent == -1:
            root = node
        else:
            children[parent].append(node)

    order = [root]
    for node in order:
        order.extend(children[node])

    min_sub = worth[:]
    max_sub = worth[:]
    answer = 0
    for node in reversed(order):
        for child in children[node]:
            answer = max(answer, abs(worth[node] - min_sub[child]), abs(worth[node] - max_sub[child]))
            min_sub[node] = min(min_sub[node], min_sub[child])
            max_sub[node] = max(max_sub[node], max_sub[child])
    print(answer)


if __name__ == "__main__":
    solve()
