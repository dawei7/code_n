# Remove All Adjacent Duplicates in String II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1209 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) |

## Problem Description

### Goal

You are given a lowercase English string `s` and an integer `k`. One `k` duplicate removal chooses exactly `k` adjacent, equal letters and deletes them. The portions of the string on the left and right of the removed block then concatenate, so letters that were previously separated may become adjacent.

Repeatedly perform any available `k` duplicate removal until no qualifying block remains. Return the resulting string. Different choices of which available block to remove first are guaranteed to lead to the same final answer.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$, where $1\le n\le10^5$.
- `k`: The exact size of a removable equal-letter block, where $2\le k\le10^4$.

**Return value**

- The unique string remaining after all possible groups of exactly `k` adjacent equal letters have been removed.

### Examples

**Example 1**

- Input: `s = "abcd"`, `k = 2`
- Output: `"abcd"`

No adjacent equal pair exists.

**Example 2**

- Input: `s = "deeedbbcccbdaa"`, `k = 3`
- Output: `"aa"`

Removing `"eee"` and `"ccc"` creates `"ddbbbdaa"`; removing `"bbb"` then creates `"dddaa"`, and removing `"ddd"` leaves `"aa"`.

**Example 3**

- Input: `s = "pbbcggttciiippooaais"`, `k = 2`
- Output: `"ps"`
