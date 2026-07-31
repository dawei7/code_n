# Select K Disjoint Special Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3458 |
| Difficulty | Medium |
| Topics | Hash Table, String, Dynamic Programming, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/select-k-disjoint-special-substrings/) |

## Problem Description
### Goal
Given a lowercase string `s` and an integer `k`, determine whether `k` pairwise disjoint special substrings can be selected. A substring is special when every character that occurs inside it has all of its occurrences inside the same substring; none of those characters may also appear elsewhere in `s`.

The entire string is explicitly excluded from being special. The chosen substrings may have different lengths, but no two may share an index. Selecting zero substrings is always possible. Return whether a selection satisfying all of these conditions exists.

### Function Contract
**Inputs**

- `s`: A lowercase English string.
- `k`: The required number of pairwise disjoint special substrings.

Let $n=\lvert s\rvert$. The constraints are $2 \le n \le 5\cdot 10^4$ and $0 \le k \le 26$.

**Return value**

Return `True` if at least `k` disjoint special substrings can be selected; otherwise return `False`.

### Examples
**Example 1**

- Input: `s = "abcdbaefab", k = 2`
- Output: `true`

The substrings `"cd"` and `"ef"` are disjoint, and none of their characters occurs outside its selected substring.

**Example 2**

- Input: `s = "cdefdc", k = 3`
- Output: `false`

Only two disjoint special substrings can be selected, for example `"e"` and `"f"`.

**Example 3**

- Input: `s = "abeabe", k = 0`
- Output: `true`

The empty selection already contains the required zero substrings.
