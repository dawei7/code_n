# Sliding Window Maximum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 239 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sliding-window-maximum/) |

## Problem Description
### Goal
Given a nonempty integer array and a valid width `k`, place a contiguous window over the first `k` elements and move it one position right at a time until it reaches the end. Each position of the window covers exactly `k` consecutive values.

Return the maximum value from every window in left-to-right order, producing `len(nums) - k + 1` results. Duplicate maxima are valid, and a departing maximum must stop influencing later windows. When $k = 1$, return the original values; when `k` equals the array length, return one global maximum. Meet the required linear running time rather than rescanning each window independently.

### Function Contract
**Inputs**

- `nums`: a non-empty list of integers
- `k`: a window width satisfying `1 <= k <= len(nums)`

**Return value**

A list containing the maximum of each of the `len(nums) - k + 1` windows in left-to-right order.

### Examples
**Example 1**

- Input: `nums = [1,3,-1,-3,5,3,6,7], k = 3`
- Output: `[3,3,5,5,6,7]`

**Example 2**

- Input: `nums = [1], k = 1`
- Output: `[1]`

**Example 3**

- Input: `nums = [9,8,7,6], k = 2`
- Output: `[9,8,7]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Discard candidates that a newer value dominates**

Maintain a deque of indices whose values are in non-increasing order. Before adding a new index, remove smaller or equal values from the back because the newer value will outlive and dominate them.

**Expire indices by position, report by value**

Remove the front index when it lies left of the current window. Once the first full window is reached, the deque front is its maximum.

The deque contains exactly the undominated indices in the current window, ordered by position from front to back and by value from largest to smallest.

Every removed-back index has a newer value at least as large, so it can never again be a maximum. Expired fronts cannot belong to the window. Therefore the surviving front is both in the window and at least as large as every other member.

An index missing from the deque is either outside the window or has a later surviving index with an equal or larger value. Following those dominance replacements always leads to a deque member, so the front represents a value at least as large as every current window element.

#### Complexity detail

Each index enters and leaves the deque at most once, giving $O(n)$ time. At most `k` window indices are stored.

#### Alternatives and edge cases

- **Scan every window:** costs $O(nk)$ time.
- **Heap with lazy deletion:** costs $O(n \log n)$ and retains stale entries.
- Width one returns the input values; width `n` returns one maximum; duplicates require index-based expiry.

</details>
