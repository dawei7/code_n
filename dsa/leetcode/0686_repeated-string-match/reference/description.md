### 1. Description

Given two strings `a` and `b`, return *the minimum number of times you should repeat string *`a`* so that string* `b` *is a substring of it*. If it is impossible for `b` to be a substring of `a` after repeating it, return `-1`.

### 2. Function Contract

**Inputs**

- `a`: Input parameter (`str`).
- `b`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Notice

string `"abc"` repeated 0 times is `""`, repeated 1 time is `"abc"` and repeated 2 times is `"abcabc"`.

### 4. Examples

#### Example 1

- **Input:** $a = "abcd", b = "cdabcdab"$
- **Output:** `3`
- **Explanation:** We return 3 because by repeating a three times "ab**cdabcdab**cd", b is a substring of it.

#### Example 2

- **Input:** $a = "a", b = "aa"$
- **Output:** `2`

### 5. Constraints

- $1 \le \text{a.length}, \text{b.length} \le 10^{4}$

- `a` and `b` consist of lowercase English letters.
