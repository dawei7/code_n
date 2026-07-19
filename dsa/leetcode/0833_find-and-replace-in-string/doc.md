# Find And Replace in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 833 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-and-replace-in-string/) |

## Problem Description
### Goal
You are given a 0-indexed string `s` and three 0-indexed parallel arrays, `indices`, `sources`, and `targets`, each containing $k$ entries. Operation $i$ examines the original string at `indices[i]`. If `sources[i]` occurs there as a substring, that occurrence must be replaced by `targets[i]`; otherwise, that operation makes no change.

All operations occur simultaneously, so one replacement must not shift the position used by another. The input guarantees that replacements which occur do not overlap. A substring is a contiguous sequence of characters. Return the string produced after every applicable replacement has been performed on `s`.

### Function Contract
**Inputs**

- `s`: the original lowercase English string, with $1 \leq \lvert s \rvert \leq 1000$.
- `indices`: $k$ starting positions in the original string.
- `sources`: $k$ nonempty lowercase strings to test at the corresponding positions.
- `targets`: $k$ nonempty lowercase replacement strings.
- The parallel arrays have equal length, with $1 \leq k \leq 100$; every source and target has length from $1$ through $50$.
- Define the total represented text size as

$$
C = \lvert s \rvert + \sum_{i=0}^{k-1}\left(\lvert \texttt{sources}[i] \rvert + \lvert \texttt{targets}[i] \rvert\right).
$$

**Return value**

Return the resulting string after applying every source that matches at its specified index in the original `s`.

### Examples
**Example 1**

- Input: `s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]`
- Output: `"eeebffff"`

Both sources match their original positions, so both replacements occur.

**Example 2**

- Input: `s = "abcd", indices = [0, 2], sources = ["ab", "ec"], targets = ["eee", "ffff"]`
- Output: `"eeecd"`

The first source matches. The second does not start at index `2`, so `"cd"` remains unchanged.

**Example 3**

- Input: `s = "abc", indices = [1], sources = ["b"], targets = ["xyz"]`
- Output: `"axyzc"`
