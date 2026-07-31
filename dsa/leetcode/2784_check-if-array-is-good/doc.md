# Check if Array is Good

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2784 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-array-is-good/) |

## Problem Description

### Goal

You are given an integer array `nums`. For a positive integer $n$, define `base[n]` as the array

$$
[1, 2, \ldots, n-1, n, n].
$$

Thus `base[n]` has length $n+1$: every integer from $1$ through $n-1$ occurs exactly once, while $n$ occurs exactly twice. For example, `base[1] = [1, 1]` and `base[3] = [1, 2, 3, 3]`.

An array is good when it is a permutation of `base[n]` for some positive integer $n$. Return whether `nums` is good. The order of its elements is irrelevant, but its length, value range, and every required multiplicity must match.

### Function Contract

**Inputs**

- `nums`: An integer array of length $m$, where $1 \le m \le 100$ and every value is between $1$ and $200$.

If `nums` is good, its only possible parameter is $n=m-1$.

**Return value**

Return `True` exactly when `nums` is a permutation of `base[n]` for a positive integer $n$; otherwise return `False`.

### Examples

**Example 1**

- Input: `nums = [2, 1, 3]`
- Output: `False`
- Explanation: The maximum is $3$, but `base[3]` has four elements, so this three-element array cannot be its permutation.

**Example 2**

- Input: `nums = [1, 3, 3, 2]`
- Output: `True`
- Explanation: Reordering the values produces `base[3] = [1, 2, 3, 3]`.

**Example 3**

- Input: `nums = [1, 1]`
- Output: `True`
- Explanation: The array already equals `base[1]`.

**Example 4**

- Input: `nums = [3, 4, 4, 1, 2, 1]`
- Output: `False`
- Explanation: `base[4]` has five elements and contains only one `1`, whereas this array has six elements and two occurrences of `1`.
