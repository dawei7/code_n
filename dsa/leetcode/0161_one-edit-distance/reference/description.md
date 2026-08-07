## Description

Given two strings `s` and `t`, return `true` if they are both one edit distance apart, otherwise return `false`.

A string `s` is said to be one distance apart from a string `t` if you can:

- Insert **exactly one** character into `s` to get `t`.

- Delete **exactly one** character from `s` to get `t`.

- Replace **exactly one** character of `s` with **a different character** to get `t`.
### Function Contract

**Inputs**

- `s`: String candidate.
- `t`: String target.

**Return value**

Return `true` if `s` and `t` are exactly one edit distance apart (insert 1 char, delete 1 char, or replace 1 char with a different character), otherwise return `false`.

### Examples
#### Example 1

- **Input:** `s = "ab", t = "acb"`
- **Output:** `true`
- **Explanation:** We can insert 'c' into s to get t.
#### Example 2

- **Input:** `s = "", t = ""`
- **Output:** `false`
- **Explanation:** We cannot get t from s by only one step.
### Constraints

- $0 \le \text{s.length}, \text{t.length} \le 10^{4}$

- `s` and `t` consist of lowercase letters, uppercase letters, and digits.