# Range Addition II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 598 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/range-addition-ii/) |

## Problem Description
### Goal
Begin with an $m \times n$ matrix `M` whose entries are all `0`. For every operation `[a, b]` in `ops`, increment by one each cell `M[x][y]` satisfying $0 \le x < a$ and $0 \le y < b$; every operation therefore updates a rectangle anchored at the matrix's upper-left corner.

After performing all operations, return the number of cells containing the maximum integer in the matrix. If `ops` is empty, every cell remains tied at the maximum value `0`, so all $m \cdot n$ cells must be counted.

### Function Contract
**Inputs**

- `m: int`: matrix row count
- `n: int`: matrix column count
- `ops: list[list[int]]`: each `[a, b]` increments cells with `0 <= row < a` and `0 <= column < b`

**Return value**

- The number of cells attaining the largest final value

### Examples
**Example 1**

- Input: `m = 3, n = 3, ops = [[2,2],[3,3]]`
- Output: `4`

**Example 2**

- Input: `m = 3, n = 3, ops = []`
- Output: `9`

**Example 3**

- Input: `m = 4, n = 5, ops = [[3,4],[2,5]]`
- Output: `8`

### Required Complexity

- **Time:** $O(k)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Maximum cells belong to every operation**

Each operation adds exactly one to its prefix rectangle. A cell receives the largest possible total only when it lies inside every operation; missing any rectangle leaves it at least one increment behind cells in the common intersection.

**Intersect prefix rectangles by their minimum dimensions**

All rectangles share the origin, so their intersection has height equal to the smallest `a` and width equal to the smallest `b`. Every cell in that rectangle receives all `k` increments, and every cell outside misses at least one.

**Handle no operations as the whole matrix**

When `ops` is empty, every cell remains zero and ties for the maximum. Initialize the intersection dimensions to `m` and `n`, update them for each operation, and return their product.

**Why the product is exact**

The maintained height and width are the coordinate-wise minimum across all processed rectangles, so their product counts precisely the cells contained in every one. Those cells receive the full number of increments. Any cell outside the intersection violates at least one minimum boundary and receives fewer increments, proving that no other cell ties them unless there are no operations, when the initialized whole matrix is correct.

#### Complexity detail

For `k` operations, scan each pair once and maintain two minima, taking $O(k)$ time and $O(1)$ extra space. Matrix dimensions do not affect the work.

#### Alternatives and edge cases

- **Simulate the matrix:** is correct but may require $O(mn)$ space and $O(sum(a b))$ update time.
- **Two-dimensional difference array:** reduces rectangle updates but still allocates and scans the full matrix unnecessarily.
- **No operations:** all `m n` cells share the maximum zero value.
- **One operation:** its `a b` cells are maximal.
- **Operation covering the whole matrix:** does not shrink the common intersection.
- **Repeated operations:** contribute multiple increments but leave the intersection dimensions unchanged.
- **Different limiting operations:** one may supply the minimum height and another the minimum width.

</details>
