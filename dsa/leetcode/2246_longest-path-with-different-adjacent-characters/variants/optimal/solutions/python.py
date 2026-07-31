def solve(parent: list[int], s: str) -> int:
    node_count = len(parent)
    children = [[] for _ in range(node_count)]
    for node in range(1, node_count):
        children[parent[node]].append(node)

    order = []
    stack = [0]
    while stack:
        node = stack.pop()
        order.append(node)
        stack.extend(children[node])

    downward = [1] * node_count
    answer = 1
    for node in reversed(order):
        longest = second_longest = 0
        for child in children[node]:
            if s[child] == s[node]:
                continue
            length = downward[child]
            if length > longest:
                longest, second_longest = length, longest
            elif length > second_longest:
                second_longest = length
        downward[node] = longest + 1
        answer = max(answer, longest + second_longest + 1)
    return answer
