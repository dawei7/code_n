## Description

Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window*** ***substring**** of *`s`* such that every character in *`t`* (**including duplicates**) is included in the window*. If there is no such substring, return *the empty string *`""`.

The testcases will be generated such that the answer is **unique**.
### Function Contract

**Inputs**

- `s`: The string in which a contiguous window is sought.
- `t`: The multiset of required characters, represented as a string.

**Return value**

Return the unique minimum-length substring of `s` containing all characters of `t` with their required multiplicities, or `""` if none exists.

### Examples

#### Example 1

- **Input:** `s = "ADOBECODEBANC", t = "ABC"`
- **Output:** `"BANC"`
- **Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#### Example 2

- **Input:** `s = "a", t = "a"`
- **Output:** `"a"`
- **Explanation:** The entire string s is the minimum window.
#### Example 3

- **Input:** `s = "a", t = "aa"`
- **Output:** `""`
- **Explanation:** Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
### Constraints

- $m = \text{s.length}$

- $n = \text{t.length}$

- $1 \le m, n \le 10^{5}$

- `s` and `t` consist of uppercase and lowercase English letters.

**Follow up:** Could you find an algorithm that runs in $O(m + n)$ time?