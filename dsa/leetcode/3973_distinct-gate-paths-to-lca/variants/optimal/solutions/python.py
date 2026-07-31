MODULO = 1_000_000_007


def solve(
    n: int,
    parent: list[int],
    gates: list[list[int]],
    queries: list[list[int]],
) -> int:
    levels = n.bit_length()
    children = [[] for _ in range(n)]
    for node in range(1, n):
        children[parent[node]].append(node)

    depth = [0] * n
    stack = [0]
    while stack:
        node = stack.pop()
        for child in children[node]:
            depth[child] = depth[node] + 1
            stack.append(child)

    ancestors = [[0] * n for _ in range(levels)]
    ancestors[0] = [0 if node == 0 else parent[node] for node in range(n)]
    matrices = [[(0, 0, 0, 0) for _ in range(n)] for _ in range(levels)]
    matrices[0] = [
        (blue, white, white, red) for red, blue, white in gates
    ]

    def multiply(
        left: tuple[int, int, int, int],
        right: tuple[int, int, int, int],
    ) -> tuple[int, int, int, int]:
        a, b, c, d = left
        e, f, g, h = right
        return (
            (a * e + b * g) % MODULO,
            (a * f + b * h) % MODULO,
            (c * e + d * g) % MODULO,
            (c * f + d * h) % MODULO,
        )

    for bit in range(1, levels):
        previous_ancestors = ancestors[bit - 1]
        current_ancestors = ancestors[bit]
        previous_matrices = matrices[bit - 1]
        current_matrices = matrices[bit]
        for node in range(n):
            middle = previous_ancestors[node]
            current_ancestors[node] = previous_ancestors[middle]
            current_matrices[node] = multiply(
                previous_matrices[node], previous_matrices[middle]
            )

    def lift(node: int, distance: int) -> int:
        bit = 0
        while distance:
            if distance & 1:
                node = ancestors[bit][node]
            distance >>= 1
            bit += 1
        return node

    def lowest_common_ancestor(first: int, second: int) -> int:
        if depth[first] < depth[second]:
            first, second = second, first
        first = lift(first, depth[first] - depth[second])
        if first == second:
            return first

        for bit in range(levels - 1, -1, -1):
            if ancestors[bit][first] != ancestors[bit][second]:
                first = ancestors[bit][first]
                second = ancestors[bit][second]
        return ancestors[0][first]

    def count_paths(node: int, ancestor: int, card: int) -> int:
        product = (1, 0, 0, 1)
        distance = depth[node] - depth[ancestor]
        bit = 0
        while distance:
            if distance & 1:
                product = multiply(product, matrices[bit][node])
                node = ancestors[bit][node]
            distance >>= 1
            bit += 1

        row = 2 * card
        return (product[row] + product[row + 1]) % MODULO

    answer = 0
    for alice_node, alice_card, bob_node, bob_card in queries:
        ancestor = lowest_common_ancestor(alice_node, bob_node)
        alice_paths = count_paths(alice_node, ancestor, alice_card)
        bob_paths = count_paths(bob_node, ancestor, bob_card)
        answer ^= alice_paths * bob_paths % MODULO
    return answer
