# 132 Pattern

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 456 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Stack, Monotonic Stack, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/132-pattern/) |

## Problem Description
### Goal
Given an integer array, look for a subsequence of three positions $i < j < k$ whose values form a `132` pattern: `nums[i] < nums[k] < nums[j]`. The names describe relative sizes, with the first selected value smallest, the second largest, and the third strictly between them.

Return `True` when any qualifying triple exists and `False` otherwise. Selected positions need not be contiguous, but their index order cannot change. Equal values cannot satisfy either strict inequality. Arrays with fewer than three elements return `False`, and the function need not return the indices or values of a found pattern.

### Function Contract
**Inputs**

- `nums`: an integer array

**Return value**

- `True` if a strict 132 pattern exists; otherwise `False`

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `False`

**Example 2**

- Input: `nums = [3, 1, 4, 2]`
- Output: `True`

**Example 3**

- Input: `nums = [-1, 3, 2, 0]`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Search from right to left for the `1`**

Scanning backward ensures every value already processed lies to the right of the current index. Maintain a decreasing stack of candidates for the high `3` value and a variable `middle` containing the strongest confirmed `2` value.

**Promote popped values into a confirmed middle**

When the current value is larger than the stack top, pop smaller values. Each popped value has now been seen to the right of a larger value, so it can serve as the `2` in a valid $3 > 2$ pair. Because stack values are popped in increasing order, the last popped value is the largest confirmed middle and dominates earlier candidates.

**Detect a smaller left endpoint**

Before modifying the stack, if the current value is smaller than `middle`, the indices are automatically ordered: the current value is the leftmost `1`, the value that caused `middle` to be popped is the `3`, and `middle` lies farther right as the `2`. Their strict inequalities establish a 132 pattern. If no value ever falls below a confirmed middle, no such triple exists.

**Keep only useful high candidates**

After popping, push the current value. Every value is pushed once and popped at most once; values hidden beneath a larger current value cannot offer a better unresolved high candidate than that value.

#### Complexity detail

Each element enters and leaves the monotonic stack at most once, so total time is $O(n)$. The stack can contain all elements of a monotone input, requiring $O(n)$ space.

#### Alternatives and edge cases

- **Prefix minimum plus ordered suffix set:** query for a suffix value strictly between the minimum and current value in $O(n \log n)$ time.
- **Prefix minimum plus a suffix scan:** is straightforward but takes $O(n^2)$ on arrays with no pattern.
- **Three nested loops:** directly checks the definition in $O(n^3)$ time.
- **Fewer than three elements:** cannot contain the required three indices.
- **Duplicate values:** inequalities are strict, so equal endpoints never form a pattern by themselves.
- **Increasing array:** contains no smaller later `2`; a decreasing array contains no middle high `3`.
- **Negative values:** initialize the confirmed middle below every finite integer rather than assuming nonnegative input.

</details>
