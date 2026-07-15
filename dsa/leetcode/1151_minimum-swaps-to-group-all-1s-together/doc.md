# Minimum Swaps to Group All 1's Together

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1151 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/) |

## Problem Description

### Goal

Given a binary array `data`, group every `1` present in the array into one contiguous block located anywhere in the array. A swap may exchange the values at any two positions; the positions do not need to be adjacent.

Return the minimum number of swaps required. The relative order of equal values is irrelevant, and the array may already satisfy the condition. In particular, zero or one occurrence of `1` is already grouped and requires no swap.

### Function Contract

**Inputs**

- `data`: a binary array of length $n$, where $1 \le n \le 10^5$ and every element is `0` or `1`.
- Let $k$ be the total number of `1` values in `data`.

**Return value**

The fewest arbitrary-position swaps needed to place all $k$ ones in one contiguous block.

### Examples

**Example 1**

- Input: `data = [1,0,1,0,1]`
- Output: `1`

**Example 2**

- Input: `data = [0,0,0,1,0]`
- Output: `0`

**Example 3**

- Input: `data = [1,0,1,0,1,0,0,1,1,0,1]`
- Output: `3`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Fix the final block length.** The number of ones never changes under swaps, so any completed block has exactly $k$ positions. Choosing its location is therefore equivalent to choosing a length-$k$ window.

**Count the misplaced values.** Every zero inside a chosen window must be exchanged with a one outside it. Their counts are equal, and one arbitrary-position swap fixes one pair, so the window's zero count is both necessary and sufficient. The answer is the minimum zero count over all length-$k$ windows.

**Reuse adjacent-window work.** Count zeros in the first window, then slide its boundaries one position at a time. Remove the contribution of the departing value and add the entering value. This examines every possible block, and taking the smallest maintained count proves optimality.

#### Complexity detail

Counting $k$ and scanning all windows each take $O(n)$ time. The window boundaries, current zero count, and best value use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Recount every window:** Correctly finds the minimum but takes $O(nk)$ time in the worst case.
- **Simulate swaps:** Constructing each resulting array adds work without changing the zero-count criterion.
- **No ones:** The empty collection is already grouped, so return `0`.
- **One one:** A single value is already a contiguous block.
- **All ones:** The only length-$n$ window contains no zeros.
- **Arbitrary versus adjacent swaps:** Distance does not affect the cost because one swap may exchange any two positions.

</details>
