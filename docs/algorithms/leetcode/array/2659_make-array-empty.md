# Make Array Empty

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2659 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Greedy, Binary Indexed Tree, Segment Tree, Sorting, Ordered Set |
| Official Link | [make-array-empty](https://leetcode.com/problems/make-array-empty/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums`, the task is to calculate the minimum total cost to make the array empty. The operation allowed is to choose an element `x` at its current index `i` (0-indexed), remove it, and add `i + 1` to the total cost. When an element is removed, all elements to its right shift one position to the left. The crucial constraint is that elements must always be removed in strictly increasing order of their *values*. If multiple elements share the smallest current value, any of them can be chosen. The goal is to find the minimum total cost.

### Function Contract
**Inputs**

- `nums`: A list of integers, representing the initial array.
  - `1 <= nums.length <= 10^5`
  - `0 <= nums[i] <= 10^9`

**Return value**

- An integer, representing the minimum total cost to empty the array.

### Examples
**Example 1**

- Input: `nums = [3,4,-1]`
- Output: `5`
- Explanation:
  1. Smallest value is -1, at original index 2. Its current index is 2. Cost = 2 + 1 = 3. Array becomes `[3,4]`. Total cost = 3.
  2. Smallest value is 3, at original index 0. Its current index is 0. Cost = 0 + 1 = 1. Array becomes `[4]`. Total cost = 3 + 1 = 4.
  3. Smallest value is 4, at original index 1. Its current index is 0. Cost = 0 + 1 = 1. Array becomes `[]`. Total cost = 4 + 1 = 5.

**Example 2**

- Input: `nums = [1,2,3]`
- Output: `3`
- Explanation:
  1. Smallest value is 1, at original index 0. Current index 0. Cost = 1. Array `[2,3]`. Total cost = 1.
  2. Smallest value is 2, at original index 1. Current index 0. Cost = 1. Array `[3]`. Total cost = 1 + 1 = 2.
  3. Smallest value is 3, at original index 2. Current index 0. Cost = 1. Array `[]`. Total cost = 2 + 1 = 3.

**Example 3**

- Input: `nums = [1,2,4,3]`
- Output: `5`
- Explanation:
  1. Smallest value is 1, at original index 0. Current index 0. Cost = 1. Array `[2,4,3]`. Total cost = 1.
  2. Smallest value is 2, at original index 1. Current index 0. Cost = 1. Array `[4,3]`. Total cost = 1 + 1 = 2.
  3. Smallest value is 3, at original index 3. Current index 1. Cost = 1 + 1 = 2. Array `[4]`. Total cost = 2 + 2 = 4.
  4. Smallest value is 4, at original index 2. Current index 0. Cost = 0 + 1 = 1. Array `[]`. Total cost = 4 + 1 = 5.

---

## Underlying Base Algorithm(s)
The problem requires processing elements in a specific order (sorted by value) and calculating costs based on their *current* positions, which dynamically change as elements are removed. This dynamic nature, coupled with the need to efficiently query the "rank" or "current index" of an element and then "remove" it (effectively updating the ranks of subsequent elements), points to the use of a **Fenwick Tree (BIT)**, also known as a Binary Indexed Tree.

Here's the breakdown of the approach:
1.  **Pair and Sort:** Create pairs of `(value, original_index)` for each element in `nums`. Sort these pairs primarily by `value` in ascending order. If values are equal, sort by `original_index` in ascending order. This secondary sort is crucial because if multiple elements have the same smallest value, removing the one with the smallest original index first will result in the minimum total cost (as it shifts fewer subsequent elements). Python's `sorted()` function is stable, so sorting `[(num, i) for i, num in enumerate(nums)]` naturally achieves this.
2.  **Fenwick Tree Initialization:** Initialize a Fenwick Tree of size `N` (where `N` is the length of `nums`). This BIT will track the *presence* of elements. Initially, all elements are present. We can represent this by updating the BIT with `+1` at each `original_index + 1` (using 1-based indexing for the BIT). A query `ft.query(k)` will then return the count of elements still present up to original index `k-1`. This count directly corresponds to the current 1-based index of the element at original index `k-1`.
3.  **Iterative Removal and Cost Calculation:** Iterate through the sorted `(value, original_index)` pairs:
    *   For each `(value, original_index)`:
        *   Query the Fenwick Tree at `original_index + 1`. The result is the current 1-based index of this element in the array. Add this value to the `total_cost`.
        *   Update the Fenwick Tree at `original_index + 1` with `-1`. This marks the element as "removed," effectively reducing the counts for any subsequent elements whose original indices were greater than `original_index`.
4.  **Return Total Cost:** After processing all elements, the accumulated `total_cost` is the minimum cost.

## Complexity Analysis
-   **Time Complexity**: `O(N log N)`
    *   Creating `(value, original_index)` pairs takes `O(N)`.
    *   Sorting these pairs takes `O(N log N)`.
    *   Initializing the Fenwick Tree by adding `N` elements takes `N` updates, each `O(log N)`, so `O(N log N)`.
    *   Iterating through the `N` sorted elements: each step involves one Fenwick Tree query and one Fenwick Tree update, both `O(log N)`. Total `O(N log N)`.
    *   Overall, the dominant factor is `O(N log N)`.

-   **Space Complexity**: `O(N)`
    *   Storing the `(value, original_index)` pairs takes `O(N)` space.
    *   The Fenwick Tree itself requires `O(N)` space.
    *   Overall, the space complexity is `O(N)`.
