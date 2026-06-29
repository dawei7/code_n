import sys

def can_save_all(n: int, root: int, graph: list[list[int]], targets: set[int]) -> bool:
    if root in targets:
        return False
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    order: list[int] = []
    stack = [root]
    parent[root] = -1
    while stack:
        node = stack.pop()
        tin[node] = len(order)
        order.append(node)
        for nxt in graph[node]:
            if nxt == parent[node]:
                continue
            parent[nxt] = node
            depth[nxt] = depth[node] + 1
            stack.append(nxt)
    for node in reversed(order):
        end = tin[node] + 1
        for nxt in graph[node]:
            if parent[nxt] == node and tout[nxt] > end:
                end = tout[nxt]
        tout[node] = end
    required = set(targets)
    required = {node for node in required if not any((other != node and tin[other] <= tin[node] < tout[other] for other in required))}
    max_depth = max((depth[node] for node in required)) if required else 0

    def covered_by_promoted(node: int, promoted: list[int]) -> bool:
        pos = tin[node]
        return any((tin[p] <= pos < tout[p] for p in promoted))
    for current_depth in range(max_depth, 0, -1):
        same_depth = [node for node in required if depth[node] == current_depth]
        if len(same_depth) <= 1:
            continue
        if current_depth == 1:
            return False
        parent_frequency: dict[int, int] = {}
        for node in same_depth:
            parent_frequency[parent[node]] = parent_frequency.get(parent[node], 0) + 1
        keep = min(same_depth, key=lambda node: parent_frequency[parent[node]])
        promoted = sorted({parent[node] for node in same_depth if node != keep})
        required = {node for node in required if node not in same_depth or node == keep}
        required = {node for node in required if not covered_by_promoted(node, promoted)}
        required.update(promoted)
    return True

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, root, target_count = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        graph = [[] for _ in range(n + 1)]
        for node in range(1, n + 1):
            count = data[idx]
            idx += 1
            for _ in range(count):
                nxt = data[idx]
                idx += 1
                graph[node].append(nxt)
        targets = set(data[idx:idx + target_count])
        idx += target_count
        out.append('yes' if can_save_all(n, root, graph, targets) else 'no')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
