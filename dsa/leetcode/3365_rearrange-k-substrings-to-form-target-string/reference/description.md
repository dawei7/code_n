## Description

You are given two strings `s` and `t`, both of which are anagrams of each other, and an integer `k`.

Your task is to determine whether it is possible to split the string `s` into `k` equal-sized substrings, rearrange the substrings, and concatenate them in *any order* to create a new string that matches the given string `t`.

Return `true` if this is possible, otherwise, return `false`.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

A **substring** is a contiguous **non-empty** sequence of characters within a string.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "abcd", t = "cdab", k = 2

**Output:** true

**Explanation:**

- Split `s` into 2 substrings of length 2: `["ab", "cd"]`.

- Rearranging these substrings as `["cd", "ab"]`, and then concatenating them results in `"cdab"`, which matches `t`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "aabbcc", t = "bbaacc", k = 3

**Output:** true

**Explanation:**

- Split `s` into 3 substrings of length 2: `["aa", "bb", "cc"]`.

- Rearranging these substrings as `["bb", "aa", "cc"]`, and then concatenating them results in `"bbaacc"`, which matches `t`.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "aabbcc", t = "bbaacc", k = 2

**Output:** false

**Explanation:**

- Split `s` into 2 substrings of length 3: `["aab", "bcc"]`.

- These substrings cannot be rearranged to form $t = "bbaacc"$, so the output is `false`.

</div>
### Constraints

- $1 \le \text{s.length} = \text{t.length} \le 2 * 10^{5}$

- $1 \le k \le \text{s.length}$

- `s.length` is divisible by `k`.

- `s` and `t` consist only of lowercase English letters.

- The input is generated such that<!-- notionvc: 53e485fc-71ce-4032-aed1-f712dd3822ba --> `s` and `t` are anagrams of each other.