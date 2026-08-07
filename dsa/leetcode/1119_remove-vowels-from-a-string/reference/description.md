## Description

Given a string `s`, remove the vowels `'a'`, `'e'`, `'i'`, `'o'`, and `'u'` from it, and return the new string.
### Function Contract

**Input**

- `s`: a nonempty string containing only lowercase English letters.

Process every character from left to right. Discard a character exactly when it belongs to `{a, e, i, o, u}`; retain every other character without changing the retained characters' order.

**Return value**

- The new string formed by concatenating all retained characters. Its length may be zero when every input character is a vowel.

### Examples
#### Example 1

- **Input:** `s = "leetcodeisacommunityforcoders"`
- **Output:** `"ltcdscmmntyfrcdrs"`
#### Example 2

- **Input:** `s = "aeiou"`
- **Output:** `""`
### Constraints

- $1 \le \text{s.length} \le 1000$

- `s` consists of only lowercase English letters.