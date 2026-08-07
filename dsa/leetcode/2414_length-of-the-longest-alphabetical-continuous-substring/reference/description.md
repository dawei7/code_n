### 1. Description

An **alphabetical continuous string** is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string `"abcdefghijklmnopqrstuvwxyz"`.

- For example, `"abc"` is an alphabetical continuous string, while `"acb"` and `"za"` are not.

Given a string `s` consisting of lowercase letters only, return the *length of the **longest** alphabetical continuous substring.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "abacaba"`
- **Output:** `2`
- **Explanation:** There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.
#### Example 2

- **Input:** `s = "abcde"`
- **Output:** `5`
- **Explanation:** "abcde" is the longest continuous substring.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of only English lowercase letters.