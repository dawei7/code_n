# Kth Smallest Element in a Sorted Matrix

| | |
|---|---|
| **ID** | `heap_06` |
| **Category** | heap |
| **Complexity (required)** | $O(K log N)$ or $O(N log(Max-Min)$) |
| **Difficulty** | 7/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) |

## Problem statement

Given an N x N matrix where each of the rows and columns is sorted in ascending order, return the K-th smallest element in the matrix.
Note that it is the K-th smallest element in the sorted order, not the K-th distinct element.
You must find an algorithm better than extracting all N^2 elements and sorting them ($O(N^2 log(N^2)$)).

**Input:** An N x N matrix and an integer K.
**Output:** The K-th smallest integer.

## When to use it

- A classic interview problem that beautifully bridges Heaps (Priority Queues) and Binary Search.
- The heap approach is generally preferred if K is small. The Binary Search approach is preferred if K is large (close to N^2).

## Approach

**Approach 1: Min-Heap (Merge N Sorted Lists) — $O(K log N)$**
Think of the matrix as N independent sorted lists (the rows). Finding the K-th smallest element across N sorted lists is a textbook Priority Queue algorithm.
1. Initialize a Min-Heap.
2. Push the first element of *every row* into the heap. Store a tuple: `(value, row, col)`.
3. Pop the smallest element from the heap.
4. Because we popped `(value, r, c)`, we immediately look at the *next* element in that same row `(r, c+1)`. If it exists, push it into the heap!
5. Repeat the pop-and-push K times. The K-th popped element is your answer.

**Approach 2: Binary Search on Value Range — $O(N log(\text{Max} - \text{Min})$)**
We don't search indices, we search *values*!
1. The absolute smallest value is `matrix[0][0]`. The absolute largest is `matrix[N-1][N-1]`.
2. Binary search a `mid` value.
3. How many elements in the matrix are \le mid?
   - Because columns are sorted, we can count this in $O(N)$ time! Start at the bottom-left corner. If the value is > mid, move UP. If it is \le mid, it means *everything above it in that column* is also \le mid! Add `row + 1` to the count, and move RIGHT.
4. If `count < k`, the K-th element must be larger. `low = mid + 1`.
5. If `count >= k`, the K-th element might be `mid` or smaller. `high = mid`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for heap_06: Kth Smallest in a Sorted Matrix.

A matrix where every row and every column is sorted. The first
column is not necessarily sorted, but the matrix has the property
that the smallest element is in [0][0]. Use a min-heap of
(value, row, col) and pop k times.
"""


def solve(matrix, n, k):
    if n == 0 or k <= 0:
        return -1
    import heapq
    heap = [(matrix[0][0], 0, 0)]
    seen = {(0, 0)}
    popped = 0
    while heap:
        v, r, c = heapq.heappop(heap)
        popped += 1
        if popped == k:
            return v
        for dr, dc in [(0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < n and nc < n and (nr, nc) not in seen:
                heapq.heappush(heap, (matrix[nr][nc], nr, nc))
                seen.add((nr, nc))
    return -1
```

</details>

## Walk-through

*(Heap Approach)*
Matrix:
`[ 1,  5,  9]`
`[10, 11, 13]`
`[12, 13, 15]`
`K = 8`.

1. **Init Heap:** `[(1, 0,0), (10, 1,0), (12, 2,0)]`.
2. **Pop 1:** Popped `1`. Push `matrix[0][1]=5`. Heap: `[5, 10, 12]`.
3. **Pop 2:** Popped `5`. Push `matrix[0][2]=9`. Heap: `[9, 10, 12]`.
4. **Pop 3:** Popped `9`. Nothing left in row 0. Heap: `[10, 12]`.
5. **Pop 4:** Popped `10`. Push `11`. Heap: `[11, 12]`.
6. **Pop 5:** Popped `11`. Push `13`. Heap: `[12, 13]`.
7. **Pop 6:** Popped `12`. Push `13`. Heap: `[13, 13]`.
8. **Pop 7:** Popped `13` (from row 1). Push `15` (WAIT, row 1 ends at 13). No push. Heap: `[13]`.
9. **Pop 8:** Popped `13` (from row 2). DONE!
Result = 13. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best (Heap)** | $O(K log(min(N, K)$)) | $O(min(N, K)$) |
| **Best (BS)** | $O(N log(Max - Min)$) | $O(1)$ |

**Heap:** The heap holds at most \min(N, K) elements. We pop/push exactly K times. Time is $O(K log(\min(N, K)$)). Space is $O(\min(N, K)$) for the heap array.
**Binary Search:** The range of values is W = Max - Min. Binary search halves this range, taking log_2 W steps. Each step scans the matrix staircase in exactly $O(N)$ time. Time is $O(N log W)$. Space is strictly $O(1)$.

## Variants & optimizations

- **Selection in X+Y:** Given two unsorted arrays X and Y of size N, find the K-th smallest sum X[i] + Y[j]. If you sort X and Y, the problem instantly perfectly transforms into finding the K-th smallest element in an implicit sorted matrix where `matrix[i][j] = X[i] + Y[j]`! You don't even need to build the matrix, just use the Heap approach mathematically.

## Real-world applications

- **Multi-Sensor Fusion:** Aggregating parallel, independently sorted streams of timestamped telemetry data and extracting the K-th historical event across all streams.

## Related algorithms in cOde(n)

- **[heap_02 - Kth Largest Element](heap_02_kth-largest-element.md)** — The 1D variant.
- **[sort_03 - Merge Sort](../sorting/sort_03_merge-sort.md)** — The Heap approach is literally just the `Merge` step of a K-way Merge Sort.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
