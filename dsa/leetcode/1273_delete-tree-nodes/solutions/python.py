def solve(nodes, parent, value):
    children = [[] for _ in range(nodes)]
    for node in range(1, nodes):
        children[parent[node]].append(node)

    order = []
    stack = [0]
    while stack:
        node = stack.pop()
        order.append(node)
        stack.extend(children[node])

    subtree_sum = list(value)
    retained = [1] * nodes
    for node in reversed(order):
        for child in children[node]:
            subtree_sum[node] += subtree_sum[child]
            retained[node] += retained[child]
        if subtree_sum[node] == 0:
            retained[node] = 0

    return retained[0]
