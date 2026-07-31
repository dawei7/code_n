def solve(parent: list[int], s: str) -> list[bool]:
    node_count = len(parent)
    children = [[] for _ in range(node_count)]
    for node in range(1, node_count):
        children[parent[node]].append(node)

    starts = [0] * node_count
    ends = [0] * node_count
    postorder = []
    stack = [(0, False)]

    while stack:
        node, expanded = stack.pop()
        if expanded:
            postorder.append(s[node])
            ends[node] = len(postorder)
            continue

        starts[node] = len(postorder)
        stack.append((node, True))
        for child in reversed(children[node]):
            stack.append((child, False))

    transformed = "^#" + "#".join(postorder) + "#$"
    radius = [0] * len(transformed)
    center = 0
    right = 0

    for index in range(1, len(transformed) - 1):
        if index < right:
            mirror = 2 * center - index
            radius[index] = min(right - index, radius[mirror])

        while transformed[index + radius[index] + 1] == transformed[index - radius[index] - 1]:
            radius[index] += 1

        if index + radius[index] > right:
            center = index
            right = index + radius[index]

    return [radius[starts[node] + ends[node] + 1] >= ends[node] - starts[node] for node in range(node_count)]
