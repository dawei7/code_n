# Rearrange K Substrings to Form Target String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3365 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/) |

## Problem Description

### Goal

You are given two equal-length lowercase strings `s` and `t` that are anagrams, together with an integer `k`. Split `s` at fixed boundaries into exactly `k` non-empty substrings of equal length. Each character therefore belongs to one predetermined block; characters may not move independently between blocks.

You may rearrange those whole substrings in any order and then concatenate them. Determine whether some ordering produces `t` exactly. Repeated substrings must be respected with their full multiplicities: having the same letters overall is guaranteed, but that alone does not ensure that the required block boundaries match.

### Function Contract

**Inputs**

- `s`: The source lowercase string to divide into equal-sized blocks.
- `t`: The target lowercase string that the reordered blocks must form.
- `k`: The exact number of blocks in the split.

Let $n=\lvert\texttt{s}\rvert=\lvert\texttt{t}\rvert$. The constraints are $1\le n\le2\cdot10^5$, $1\le k\le n$, and $k$ divides $n$. The two strings are anagrams.

**Return value**

- `true` if the complete blocks of `s` can be reordered to equal `t`; otherwise, `false`.

### Examples

#### Example 1

- **Input:** `s = "abcd"`, `t = "cdab"`, `k = 2`
- **Output:** `true`
- **Explanation:** The blocks `["ab", "cd"]` can be ordered as `["cd", "ab"]`.

#### Example 2

- **Input:** `s = "aabbcc"`, `t = "bbaacc"`, `k = 3`
- **Output:** `true`
- **Explanation:** Reordering `["aa", "bb", "cc"]` produces the target blocks `["bb", "aa", "cc"]`.

#### Example 3

- **Input:** `s = "aabbcc"`, `t = "bbaacc"`, `k = 2`
- **Output:** `false`
- **Explanation:** The source blocks are `["aab", "bcc"]`, which do not match the target blocks `["bba", "acc"]`.
