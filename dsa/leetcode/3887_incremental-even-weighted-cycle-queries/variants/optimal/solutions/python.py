def solve(n: int, edges: list[list[int]]) -> int:
    parent = list(range(n))
    size = [1] * n
    parity = [0] * n

    def find(node: int) -> int:
        if parent[node] != node:
            previous_parent = parent[node]
            parent[node] = find(previous_parent)
            parity[node] ^= parity[previous_parent]
        return parent[node]

    accepted = 0

    for left, right, weight in edges:
        left_root = find(left)
        right_root = find(right)
        left_parity = parity[left]
        right_parity = parity[right]

        if left_root == right_root:
            if left_parity ^ right_parity == weight:
                accepted += 1
            continue

        accepted += 1
        root_parity = left_parity ^ right_parity ^ weight

        if size[left_root] < size[right_root]:
            parent[left_root] = right_root
            parity[left_root] = root_parity
            size[right_root] += size[left_root]
        else:
            parent[right_root] = left_root
            parity[right_root] = root_parity
            size[left_root] += size[right_root]

    return accepted
