# Stamping The Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 936 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Stack, Greedy, Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [stamping-the-sequence](https://leetcode.com/problems/stamping-the-sequence/) |

## Problem Description

### Goal

Given strings `stamp` and `target`, begin with a string `s` of length `target.length` containing only `?` characters. In one turn, place the entire `stamp` within the boundaries of `s` and overwrite the covered positions with the corresponding stamp characters. Later stamps may overwrite characters written by earlier turns.

Transform `s` into `target` using at most `10 * target.length` turns. Return the starting index of the stamp's leftmost character for every turn in execution order. Any sequence satisfying the limit and producing `target` is valid. If no such sequence exists, return an empty list.

### Function Contract

**Inputs**

- `stamp`: a non-empty lowercase string of length $m$.
- `target`: a lowercase string of length $n$, where $m \le n \le 1000$.

**Return value**

Return any list of at most $10n$ valid stamp starting indices that constructs `target` from `"?" * n`, or `[]` when construction is impossible.

### Examples

**Example 1**

- Input: `stamp = "abc", target = "ababc"`
- Output: `[0,2]`
- Explanation: `[1,0,2]` is another valid answer.

**Example 2**

- Input: `stamp = "abca", target = "aabcaca"`
- Output: `[3,0,1]`
