# Maximum Number of Non-overlapping Palindrome Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2472 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/) |

## Problem Description

### Goal

Given a lowercase string `s` and a positive integer `k`, choose as many substrings of `s` as possible. Every chosen substring must be a palindrome and must have length at least `k`.

The chosen substrings may have identical contents, but their index ranges must not overlap. A substring is contiguous, so skipping characters inside one selection is not allowed. Return the maximum number of substrings that can coexist under these rules.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters.
- `k`: The minimum permitted length of every selected palindrome.

The constraints satisfy $1 \le k \le \lvert\texttt{s}\rvert \le 2000$.

**Return value**

Return an integer: the greatest possible number of pairwise non-overlapping palindromic substrings whose lengths are at least `k`.

### Examples

#### Example 1

- **Input:** `s = "abaccdbbd", k = 3`
- **Output:** `2`
- **Explanation:** `"aba"` and `"dbbd"` occupy disjoint ranges and both meet the minimum length.

#### Example 2

- **Input:** `s = "adbcda", k = 2`
- **Output:** `0`
- **Explanation:** No substring of length at least two is palindromic.

#### Example 3

- **Input:** `s = "aaaaa", k = 2`
- **Output:** `2`
- **Explanation:** Two disjoint copies of `"aa"` can be selected; the remaining character cannot form another valid substring.
