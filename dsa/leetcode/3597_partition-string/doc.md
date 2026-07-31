# Partition String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3597 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Trie, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-string/) |

## Problem Description
### Goal
Scan a lowercase string `s` from left to right and divide its characters into segments according to a greedy uniqueness rule. Begin a candidate at the next unused index and extend it one character at a time. As soon as that whole candidate string has never been emitted as a segment before, record it and start the next candidate at the following character.

Continue until the scan reaches the end of `s`, then return the recorded segments in creation order. Uniqueness refers to equality with previously recorded whole segments; characters inside one segment may repeat. If the final characters form only a segment that was already recorded and there is no further character with which to extend it, no additional segment is created.

### Function Contract
**Inputs**

- `s`: a nonempty string containing only lowercase English letters

The input length satisfies $1 \le \lvert\texttt{s}\rvert \le 10^5$.

**Return value**

A list of the distinct segments emitted by the prescribed left-to-right procedure, in order.

### Examples
**Example 1**

- Input: `s = "abbccccd"`
- Output: `["a", "b", "bc", "c", "cc", "d"]`

At the second `b`, the one-character candidate has already appeared, so it extends to the new segment `"bc"`. The same rule later extends a repeated `"c"` to `"cc"`.

**Example 2**

- Input: `s = "aaaa"`
- Output: `["a", "aa"]`

After recording `"a"`, the next candidate grows to `"aa"`. The last `"a"` is already seen and cannot be extended, so it creates no segment.

**Example 3**

- Input: `s = "abc"`
- Output: `["a", "b", "c"]`

Every one-character candidate is new, so every character becomes its own segment.
