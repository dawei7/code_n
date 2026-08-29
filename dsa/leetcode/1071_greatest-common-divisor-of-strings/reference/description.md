### 1. Description

For two strings `s` and `t`, we say "`t` divides `s`" if and only if $s = t + t + t + ... + t + t$ (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return *the largest string *`x`* such that *`x`* divides both *`str1`* and *`str2`.

### 2. Function Contract

**Inputs**

- `str1`: Input parameter (`str`).
- `str2`: Input parameter (`str`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** str1 = "ABCABC", str2 = "ABC"

- **Output:** "ABC"

#### Example 2

- **Input:** str1 = "ABABAB", str2 = "ABAB"

- **Output:** "AB"

#### Example 3

- **Input:** str1 = "LEET", str2 = "CODE"

- **Output:** ""

#### Example 4

- **Input:** str1 = "AAAAAB", str2 = "AAA"

- **Output:** ""

### 4. Constraints

- $1 \le \text{str1.length}, \text{str2.length} \le 1000$

- `str1` and `str2` consist of English uppercase letters.
