### 1. Description

Given a string `s`, return `true` *if it is possible to split the string* `s` *into three **non-empty** palindromic substrings. Otherwise, return *`false`.​​​​​

A string is said to be palindrome if it the same string when reversed.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "abcbdd"`
- **Output:** `true`
- **Explanation:** "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
#### Example 2

- **Input:** `s = "bcbddxy"`
- **Output:** `false`
- **Explanation:** s cannot be split into 3 palindromes.

### 4. Constraints

- $3 \le \text{s.length} \le 2000$

- `s`​​​​​​ consists only of lowercase English letters.