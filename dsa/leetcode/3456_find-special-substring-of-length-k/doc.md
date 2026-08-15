# Find Special Substring of Length K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3456 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/find-special-substring-of-length-k/) |

## Problem Description

### Goal

Determine whether `s` contains a substring of exactly `k` copies of one lowercase letter. The substring must be a complete run: if a character exists immediately before it, that character must be different, and the same condition applies to a character immediately after it.

Consequently, selecting `k` characters from inside a longer equal-character run is not valid, even though those selected characters are identical. A qualifying substring may begin at the first character or end at the final character, where the corresponding outside-neighbor condition is absent.

### Function Contract

**Inputs**

- `s`: A nonempty lowercase English string.
- `k`: The exact required length of the uniform substring.

The constraints are $1 \le k \le \lvert s\rvert \le 100$.

**Return value**

Return `True` if `s` has a maximal equal-character run of length exactly `k`; otherwise return `False`.

### Examples

#### Example 1

- **Input:** `s = "aaabaaa", k = 3`
- **Output:** `true`

The final `aaa` has length three, is preceded by `b`, and has no following character.

#### Example 2

- **Input:** `s = "abc", k = 2`
- **Output:** `false`

No two adjacent characters are equal.

#### Example 3

- **Input:** `s = "aaaa", k = 3`
- **Output:** `false`

Every three-character selection belongs to a longer run, so its outside boundary repeats `a`.
