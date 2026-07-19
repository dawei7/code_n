def solve(queries: list[list[int]]) -> list[bool]:
    max_coord = max(query[1] for query in queries) + 1
    size = max_coord + 1

    bit = [0] * (size + 1)

    def bit_add(index: int, delta: int) -> None:
        index += 1
        while index <= size:
            bit[index] += delta
            index += index & -index

    def bit_sum(index: int) -> int:
        if index < 0:
            return 0
        index = min(index, max_coord) + 1
        total = 0
        while index > 0:
            total += bit[index]
            index -= index & -index
        return total

    def bit_find(order: int) -> int:
        index = 0
        step = 1 << (size.bit_length() - 1)
        while step:
            nxt = index + step
            if nxt <= size and bit[nxt] < order:
                index = nxt
                order -= bit[nxt]
            step >>= 1
        return index

    tree_size = 1
    while tree_size < size:
        tree_size <<= 1
    seg = [0] * (2 * tree_size)

    def seg_set(index: int, value: int) -> None:
        node = index + tree_size
        seg[node] = value
        node >>= 1
        while node:
            seg[node] = max(seg[node << 1], seg[node << 1 | 1])
            node >>= 1

    def seg_max(left: int, right: int) -> int:
        if left > right:
            return 0
        left += tree_size
        right += tree_size
        answer = 0
        while left <= right:
            if left & 1:
                answer = max(answer, seg[left])
                left += 1
            if not (right & 1):
                answer = max(answer, seg[right])
                right -= 1
            left >>= 1
            right >>= 1
        return answer

    present = [False] * size
    present[0] = True
    present[max_coord] = True
    bit_add(0, 1)
    bit_add(max_coord, 1)
    seg_set(max_coord, max_coord)

    result: list[bool] = []
    for query in queries:
        if query[0] == 1:
            x = query[1]
            if present[x]:
                continue
            before = bit_sum(x)
            prev_obstacle = bit_find(before)
            next_obstacle = bit_find(before + 1)

            present[x] = True
            bit_add(x, 1)
            seg_set(x, x - prev_obstacle)
            seg_set(next_obstacle, next_obstacle - x)
        else:
            _, x, block_size = query
            prev_obstacle = bit_find(bit_sum(x))
            best_gap = max(seg_max(0, x), x - prev_obstacle)
            result.append(best_gap >= block_size)

    return result
