# Sum in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2679 |
| Difficulty | Medium |
| Topics | Array, Sorting, Heap (Priority Queue), Matrix, Simulation |
| Official Link | [sum-in-a-matrix](https://leetcode.com/problems/sum-in-a-matrix/) |

## Problem Description & Examples
### Goal
Given an `m x n` integer matrix, `nums`, simulate a process for `n` operations. In each operation, identify the maximum element within each individual row. From this collection of `m` row-maximums, find the single largest value. Add this largest value to a running total score. After adding, conceptually remove the chosen maximum element from each row (meaning it cannot be selected again in subsequent operations). Repeat this process `n` times and return the final accumulated score.

### Function Contract
**Inputs**

- `nums`: A `List[List[int]]` representing an `m x n` integer matrix.
  - `m` is the number of rows, `n` is the number of columns.
  - `1 <= m, n <= 50`
  - `1 <= nums[i][j] <= 1000`

**Return value**

- An `int` representing the total score accumulated after `n` operations.

### Examples
**Example 1**

- Input: `nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]`
- Output: `15`
- Explanation:
  1. Sort each row: `[[1,2,7],[2,4,6],[3,5,6],[1,2,3]]`
  2. Operation 1 (rightmost elements): Max of `[7,6,6,3]` is `7`. Score = `7`.
  3. Operation 2 (second rightmost elements): Max of `[2,4,5,2]` is `5`. Score = `7 + 5 = 12`.
  4. Operation 3 (leftmost elements): Max of `[1,2,3,1]` is `3`. Score = `12 + 3 = 15`.

**Example 2**

- Input: `nums = [[1]]`
- Output: `1`
- Explanation:
  1. Sort each row: `[[1]]`
  2. Operation 1: Max of `[1]` is `1`. Score = `1`.

**Example 3**

- Input: `nums = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `24`
- Explanation:
  1. Sort each row: `[[1,2,3],[4,5,6],[7,8,9]]`
  2. Operation 1: Max of `[3,6,9]` is `9`. Score = `9`.
  3. Operation 2: Max of `[2,5,8]` is `8`. Score = `9 + 8 = 17`.
  4. Operation 3: Max of `[1,4,7]` is `7`. Score = `17 + 7 = 24`.

---

## Underlying Base Algorithm(s)
The core idea relies on **Sorting** and **Simulation**.
1.  **Sorting:** To efficiently find the maximum available element in each row repeatedly, it's optimal to sort each row initially. Once sorted, the largest available element will always be at the rightmost position among the unpicked elements.
2.  **Simulation (Iterative Max Selection):** After sorting, the problem transforms into iterating `n` times. In each iteration, we consider the `k`-th largest element from each row (where `k` goes from 1 to `n`). We then find the maximum among these `m` `k`-th largest elements and add it to the total score. This is equivalent to iterating through the columns of the sorted matrix from right to left, finding the maximum element in that column, and summing it up.

---

## Complexity Analysis
Let `m` be the number of rows and `n` be the number of columns in the `nums` matrix.

- **Time Complexity**: `O(m * n log n)`
    - Sorting each of the `m` rows takes `O(n log n)` time. Since there are `m` rows, the total time for sorting all rows is `O(m * n log n)`.
    - After sorting, we iterate `n` times (once for each "column" of sorted elements). In each iteration, we traverse `m` rows to find the maximum element among them. This takes `O(m)` time per iteration. The total for this step is `O(n * m)`.
    - Combining these, the dominant factor is `O(m * n log n)`.

- **Space Complexity**: `O(n)`
    - If the sorting algorithm used for each row (e.g., Python's Timsort) requires `O(n)` auxiliary space in the worst case for a list of size `n`, and we sort rows one by one, the peak auxiliary space used is `O(n)`.
    - If sorting is done in-place and no additional data structures proportional to input size are used, the space complexity would be `O(1)` (excluding the input matrix itself). Given Python's list sort behavior, `O(n)` is a more accurate worst-case auxiliary space complexity.
