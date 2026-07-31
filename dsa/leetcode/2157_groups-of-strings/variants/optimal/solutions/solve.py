def solve(words: list[str]) -> list[int]:
    mask_counts: dict[int, int] = {}
    for word in words:
        mask = 0
        for letter in word:
            mask |= 1 << (ord(letter) - ord("a"))
        mask_counts[mask] = mask_counts.get(mask, 0) + 1

    masks = list(mask_counts)
    indices = {mask: index for index, mask in enumerate(masks)}
    parent = list(range(len(masks)))
    sizes = [mask_counts[mask] for mask in masks]
    group_count = len(masks)
    largest_group = max(sizes)

    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(first, second):
        nonlocal group_count, largest_group
        first_root = find(first)
        second_root = find(second)
        if first_root == second_root:
            return
        if sizes[first_root] < sizes[second_root]:
            first_root, second_root = second_root, first_root
        parent[second_root] = first_root
        sizes[first_root] += sizes[second_root]
        group_count -= 1
        largest_group = max(largest_group, sizes[first_root])

    deleted_owner = {}
    for index, mask in enumerate(masks):
        for bit in range(26):
            neighbor = mask ^ (1 << bit)
            if neighbor in indices:
                union(index, indices[neighbor])

        remaining = mask
        while remaining:
            bit = remaining & -remaining
            deleted = mask ^ bit
            if deleted in deleted_owner:
                union(index, deleted_owner[deleted])
            else:
                deleted_owner[deleted] = index
            remaining ^= bit

    return [group_count, largest_group]
