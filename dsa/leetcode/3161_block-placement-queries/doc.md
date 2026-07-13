# Block Placement Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3161 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Binary Indexed Tree, Segment Tree, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [block-placement-queries](https://leetcode.com/problems/block-placement-queries/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/block-placement-queries/).

### Goal
We are managing a linear space of size `x` (from 0 to `x`). We receive a sequence of queries: either placing an obstacle at a specific coordinate `x` or checking if a block of size `sz` can fit into any empty segment between existing obstacles (including the boundaries 0 and `x`).

### Function Contract
**Inputs**

- `queries`: A list of lists, where each inner list is either `[1, x]` (place an obstacle at `x`) or `[2, x, sz]` (check if a gap of size `sz` exists within the range `[0, x]`).

**Return value**

- A list of booleans indicating the result of each type-2 query.

### Examples
**Example 1**

- Input: `queries = [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]`
- Output: `[false, true, true]`

**Example 2**

- Input: `queries = [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]`
- Output: `[true, true, false]`

**Example 3**

- Input: `queries = [[2, 1, 1], [1, 2], [1, 3], [2, 3, 1]]`
- Output: `[true, true]`

---

## Solution
### Approach
The problem is solved using a **Segment Tree** that maintains the maximum gap size within specific intervals. Since the coordinates can be large, we use a coordinate-compressed or fixed-size segment tree (up to 50,000). Each node in the tree stores the length of the longest empty segment in its range, the length of the empty segment starting at the left boundary, and the length of the empty segment ending at the right boundary.

### Complexity Analysis
- **Time Complexity**: `O(Q log N)`, where `Q` is the number of queries and `N` is the maximum coordinate value (50,000). Each update and query operation on the segment tree takes logarithmic time.
- **Space Complexity**: `O(N)`, required to store the segment tree nodes.

### Reference Implementations
<details>
<summary>python</summary>

```python
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
```
</details>
