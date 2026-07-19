# Greatest Common Divisor of Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1071 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/greatest-common-divisor-of-strings/) |

## Problem Description

### Goal

For strings `s` and `t`, say that `t` divides `s` if and only if `s` can be formed by concatenating one or more complete copies of `t` and nothing else. The copies must cover all of `s`; a shared prefix or a pattern followed by unmatched characters is not a divisor.

Given uppercase English strings `str1` and `str2`, return the largest string `x` that divides both inputs. Here largest means greatest length among all strings satisfying the repetition rule for each input. If no non-empty string divides both, return the empty string.

### Function Contract

**Inputs**

- `str1`: an uppercase English string of length $N$, where $1 \le N \le 1000$.
- `str2`: an uppercase English string of length $M$, where $1 \le M \le 1000$.
- Let $G=\gcd(N,M)$.

**Return value**

- The longest string whose repeated concatenation forms both inputs, or `""` when no common divisor string exists.

### Examples

**Example 1**

- Input: `str1 = "ABCABC", str2 = "ABC"`
- Output: `"ABC"`

**Example 2**

- Input: `str1 = "ABABAB", str2 = "ABAB"`
- Output: `"AB"`

**Example 3**

- Input: `str1 = "LEET", str2 = "CODE"`
- Output: `""`

**Example 4**

- Input: `str1 = "AAAAAB", str2 = "AAA"`
- Output: `""`
