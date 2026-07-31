def solve(parent: list[int], s: str) -> int:
    n = len(parent)
    children = [[] for _ in range(n)]

    for node in range(1, n):
        children[parent[node]].append(node)

    frequencies = {0: 1}
    answer = 0
    stack = [(0, 0)]

    while stack:
        node, mask = stack.pop()

        for child in children[node]:
            child_mask = mask ^ (1 << (ord(s[child]) - ord("a")))
            answer += frequencies.get(child_mask, 0)

            for bit in range(26):
                answer += frequencies.get(child_mask ^ (1 << bit), 0)

            frequencies[child_mask] = frequencies.get(child_mask, 0) + 1
            stack.append((child, child_mask))

    return answer
