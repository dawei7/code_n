# Diagonal Traverse II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1424 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/diagonal-traverse-ii/) |

## Problem Description

### Goal

The nested array `nums` contains nonempty rows that may have different lengths. Treat each value as occupying coordinate `(row, column)`. Values whose coordinate sum `row + column` is equal belong to the same diagonal.

Return all values by increasing diagonal sum. Within one diagonal, visit values from the largest row index to the smallest row index, which moves upward and to the right through the jagged structure.

### Function Contract

**Inputs**

- `nums`: a list of nonempty integer rows.
- The total number of values is $N$, where $1 \le N \le 10^5$, and every value is between $1$ and $10^9$.

**Return value**

- A flat array containing every input value once in increasing `row + column` order and decreasing row order within each diagonal.

### Examples

**Example 1**

- Input: `nums = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[1,4,2,7,5,3,8,6,9]`

**Example 2**

- Input: `nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]`
- Output: `[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]`

**Example 3**

- Input: `nums = [[1],[2,3],[4,5,6]]`
- Output: `[1,2,4,3,5,6]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Bucket by coordinate sum.** Scan rows from top to bottom and values within each row from left to right. Place `nums[row][column]` into the bucket at index `row + column`. Grow the bucket list whenever a new largest diagonal index appears.

**Restore direction within each diagonal.** Because rows are scanned in increasing order, values enter each bucket from the smallest row index to the largest. The required order inside a diagonal is the reverse, so after collection, visit the buckets by increasing index and append each bucket in reverse insertion order.

**Why the buckets preserve exact order.** Every coordinate belongs to exactly one sum bucket, and bucket indices directly encode the required global diagonal ordering without a sort. Reversing a bucket changes its top-to-bottom insertion order into the required bottom-to-top traversal. Thus every value appears once in exactly its specified position.

#### Complexity detail

Each of the $N$ values is appended once and read once. The largest possible diagonal index is $O(N)$ because rows are nonempty and the total row and column extent is bounded by the number of values. Time is therefore $O(N)$, and the buckets plus output use $O(N)$ space.

#### Alternatives and edge cases

- **Sort coordinate triples:** Store `(row + column, -row, value)` for every element and sort. It is correct but takes $O(N\log N)$ time.
- **Rescan rows for every diagonal:** Check possible coordinates one diagonal at a time. This repeats row work and can become superlinear.
- **Queue traversal:** Seed the first element of each row at the appropriate time and use a queue. It can achieve $O(N)$ but is more intricate for jagged rows.
- **Single row:** Increasing diagonal sums preserve ordinary left-to-right order.
- **One value per row:** Each value occupies a new diagonal and remains in row order.
- **Long later row:** Bucket indices may extend far beyond earlier row lengths, so grow storage dynamically.
- **Duplicate values:** Ordering depends only on coordinates, not value identity.

</details>
