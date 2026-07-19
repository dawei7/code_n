# Pancake Sorting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 969 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [pancake-sorting](https://leetcode.com/problems/pancake-sorting/) |

## Problem Description

### Goal

Given a permutation `arr`, sort it using pancake flips. One flip chooses an integer `k` and reverses the prefix `arr[0:k]`, so only a segment beginning at index `0` may be reversed.

Return the sequence of chosen `k` values. Applying those flips in order must leave `arr` in ascending order, and the sequence may contain at most `10 * arr.length` flips. The sequence does not need to be shortest; any one satisfying these conditions is valid.

### Function Contract

**Inputs**

- `arr`: a permutation of the integers from $1$ through $N$.
- The length satisfies $1 \le N \le 100$.

**Return value**

Return at most $10N$ integers. Every returned `k` must satisfy $1 \le k \le N$, and reversing `arr[0:k]` for each value in order must sort the permutation.

### Examples

**Example 1**

- Input: `arr = [3,2,4,1]`
- Output: `[4,2,4,3]`
- Explanation: Those four prefix reversals transform the input into `[1,2,3,4]`; other valid sequences are also accepted.

**Example 2**

- Input: `arr = [1,2,3]`
- Output: `[]`
