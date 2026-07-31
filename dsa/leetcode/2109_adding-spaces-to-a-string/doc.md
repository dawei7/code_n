# Adding Spaces to a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2109 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [adding-spaces-to-a-string](https://leetcode.com/problems/adding-spaces-to-a-string/) |

## Problem Description

### Goal

You are given a 0-indexed string `s` containing lowercase and uppercase English letters, together with a strictly increasing array `spaces`. Every value in `spaces` is an index in the original string and requests one space immediately before the character at that index.

Apply all requested insertions without changing the order of the original characters. Earlier inserted spaces do not shift the meaning of later indices because every index refers to the unchanged input `s`. Return the resulting string, including a leading space when `spaces` contains index $0$.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $1 \le n \le 3 \cdot 10^5$, containing only English letters.
- `spaces`: A strictly increasing array of $m$ insertion indices, where $1 \le m \le 3 \cdot 10^5$ and $0 \le \texttt{spaces[i]} < n$.

**Return value**

Return `s` with one space inserted before every original index listed in `spaces`.

### Examples

**Example 1**

- Input: `s = "LeetcodeHelpsMeLearn", spaces = [8, 13, 15]`
- Output: `"Leetcode Helps Me Learn"`

**Example 2**

- Input: `s = "icodeinpython", spaces = [1, 5, 7, 9]`
- Output: `"i code in py thon"`

**Example 3**

- Input: `s = "spacing", spaces = [0, 1, 2, 3, 4, 5, 6]`
- Output: `" s p a c i n g"`
- Explanation: An insertion at index $0$ places a space before the first character.
