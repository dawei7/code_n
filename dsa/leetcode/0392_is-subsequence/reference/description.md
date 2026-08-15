### 1. Description

Given two strings `s` and `t`, return `true`* if *`s`* is a **subsequence** of *`t`*, or *`false`* otherwise*.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"<u>a</u>b<u>c</u>d<u>e</u>"` while `"aec"` is not).

### 2. Function Contract

**Inputs**

- `s`: The candidate subsequence, which may be empty.
- `t`: The source string, which may be empty.

**Return value**

Return `true` if the characters of `s` can be matched in order within `t`; otherwise return `false`.

### 3. Examples

#### Example 1

- **Input:** `s = "abc", t = "ahbgdc"`
- **Output:** `true`

#### Example 2

- **Input:** `s = "axc", t = "ahbgdc"`
- **Output:** `false`

### 4. Constraints

- $0 \le \text{s.length} \le 100$

- $0 \le \text{t.length} \le 10^{4}$

- `s` and `t` consist only of lowercase English letters.

**Follow up:** Suppose there are lots of incoming `s`, say $s_{1}, s_{2}, ..., s_{k}$ where $k \ge 10^{9}$, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?
