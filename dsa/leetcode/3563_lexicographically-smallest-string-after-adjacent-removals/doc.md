# Lexicographically Smallest String After Adjacent Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3563 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/) |

## Problem Description

### Goal

You may modify a lowercase English string `s` by removing any adjacent pair whose letters are consecutive in the alphabet. Either order is valid, so `ab` and `ba` may both be removed. The alphabet is circular: `az` and `za` are valid pairs as well. After each removal, the remaining characters close the gap and may create new eligible pairs.

Perform the operation any number of times, including zero. Different removal choices can lead to different strings, and stopping early is allowed even when another pair remains. Return the lexicographically smallest string among every result reachable through such choices; the shortest result is not automatically best unless the usual lexicographic comparison makes it so.

### Function Contract

**Inputs**

- `s`: A string consisting only of lowercase English letters.

Its length satisfies $1 \le \lvert s \rvert \le 250$.

**Return value**

Return the lexicographically smallest string obtainable after zero or more valid adjacent-pair removals, where alphabet adjacency includes the circular pair `a` and `z`.

### Examples

**Example 1**

- Input: `s = "abc"`
- Output: `"a"`
- Explanation: Removing `bc` leaves `a`, which is smaller than the result obtained by removing `ab`.

**Example 2**

- Input: `s = "bcda"`
- Output: `""`
- Explanation: Remove `cd`, then remove the newly adjacent `ba` pair.

**Example 3**

- Input: `s = "zdce"`
- Output: `"zdce"`
- Explanation: Removing `dc` would leave `ze`, but the unchanged original is lexicographically smaller than `ze`, so performing zero operations is optimal.

---
