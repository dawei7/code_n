def solve(fruits: list[int], baskets: list[int]) -> int:
    basket_count = len(baskets)
    leaf_count = 1
    while leaf_count < basket_count:
        leaf_count *= 2

    maximum = [0] * (2 * leaf_count)
    maximum[leaf_count : leaf_count + basket_count] = baskets
    for node in range(leaf_count - 1, 0, -1):
        maximum[node] = max(maximum[2 * node], maximum[2 * node + 1])

    unplaced = 0
    for fruit in fruits:
        if maximum[1] < fruit:
            unplaced += 1
            continue

        node = 1
        while node < leaf_count:
            left_child = 2 * node
            if maximum[left_child] >= fruit:
                node = left_child
            else:
                node = left_child + 1

        maximum[node] = 0
        node //= 2
        while node:
            maximum[node] = max(maximum[2 * node], maximum[2 * node + 1])
            node //= 2

    return unplaced
