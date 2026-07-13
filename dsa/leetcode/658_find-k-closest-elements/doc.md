# Find K Closest Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 658 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/find-k-closest-elements/) |

## Problem Description
### Goal
Given an integer array `arr` sorted in ascending order and integers `k` and `x`, select the `k` integers in the array that are closest to `x`. Value `a` is closer than value `b` when $| a - x | < | b - x |$, or when the distances are equal and $a < b$.

Return the selected values sorted in ascending order. Duplicate array occurrences remain separate selectable elements, `x` does not need to appear in the array, and the smaller value wins every equal-distance tie before the final result is ordered.

### Function Contract
**Inputs**

- `arr`: a nonempty list of integers sorted in ascending order
- `k`: the positive number of elements to return, no greater than `len(arr)`
- `x`: the comparison value, which need not occur in the array

**Return value**

- The selected `k` closest values in increasing order

### Examples
**Example 1**

- Input: `arr = [1, 2, 3, 4, 5]`, `k = 4`, `x = 3`
- Output: `[1, 2, 3, 4]`

**Example 2**

- Input: `arr = [1, 2, 3, 4, 5]`, `k = 4`, `x = -1`
- Output: `[1, 2, 3, 4]`

**Example 3**

- Input: `arr = [1, 2, 4, 5]`, `k = 2`, `x = 3`
- Output: `[2, 4]`

### Required Complexity

- **Time:** $O(\log(N - K) + K)$
- **Space:** $O(K)$

<details>
<summary>Approach</summary>

#### General

**The answer is one contiguous window**

Because `arr` is sorted, if two selected values surround an unselected value, that middle value cannot be farther from `x` than both selected endpoints. Therefore some optimal answer consists of `k` consecutive array entries. The problem reduces to finding its starting index between `0` and $N - K$.

**Compare two neighboring candidate windows**

For a possible start `mid`, compare the element leaving the window, `arr[mid]`, with the element that would enter after shifting right, `arr[mid + k]`. If `x - arr[mid]` is greater than `arr[mid + k] - x`, the entering right value is closer, so every optimal start lies to the right of `mid`. Otherwise the current left value is at least as good and the optimal start is at or left of `mid`.

On equality, retaining the left side enforces the rule that the smaller value wins a distance tie.

**Why binary search finds the unique leftmost optimum**

As the window start increases, the left boundary and the competing right boundary both move monotonically. The comparison changes from favoring right shifts to favoring the current or left window only once. Binary search locates that boundary. The resulting slice is already increasing and contains exactly the contiguous optimal window established above.

#### Complexity detail

Binary search examines $O(\log(N - K))$ window starts, and copying the returned slice takes $O(K)$ time. The returned list occupies $O(K)$ space; apart from the output, the search uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Insertion point plus two-pointer expansion:** also runs in $O(\log N + K)$ time and makes individual selections explicit, but must reverse or prepend left-side choices carefully.
- **Sort every value by distance and value:** is straightforward, but discards the existing order and takes $O(N \log N)$ time plus a final sort of the chosen values.
- **Heap of the best values:** takes $O(N \log K)$ time and additional heap space, which is unnecessary for sorted input.
- If $k = N$, the entire array is the only valid window.
- Values may repeat; each occurrence is an eligible array element.
- When `x` lies outside the array range, the optimal window is at the nearest end.
- Equal distances prefer the left, smaller value, so the binary-search comparison must shift right only on strict inequality.

</details>
