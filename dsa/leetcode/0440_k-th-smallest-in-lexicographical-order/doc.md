# K-th Smallest in Lexicographical Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 440 |
| Difficulty | Hard |
| Topics | Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/) |

## Problem Description
### Goal
Given positive integers `n` and `k`, arrange every integer from `1` through `n` by lexicographical order of its decimal representation. This is dictionary order, so a prefix such as `1` appears before `10`, and the complete `1` prefix subtree appears before `2`.

Return the integer at the valid one-based position `k`. Do not materialize or sort all `n` values, because the range may be large. Count how many valid integers lie beneath each decimal prefix and skip whole prefix subtrees until the target rank is reached, never including zero or values above `n`.

### Function Contract
**Inputs**

- `n`: the inclusive upper bound of the integer range
- `k`: a one-based position in lexicographic order

**Return value**

- Return the integer occupying position `k` without materializing the full sorted range.

### Examples
**Example 1**

- Input: `n = 13, k = 2`
- Output: `10`

**Example 2**

- Input: `n = 1, k = 1`
- Output: `1`

**Example 3**

- Input: `n = 100, k = 10`
- Output: `17`
