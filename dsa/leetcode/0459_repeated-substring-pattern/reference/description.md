### 1. Description

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

**Return value**

- Return `True` if one proper nonempty substring repeated at least twice equals all of `s`; otherwise, return `False`.

### 3. Examples

#### Example 1

- **Input:** `s = "abab"`
- **Output:** `true`
- **Explanation:** It is the substring "ab" twice.
#### Example 2

- **Input:** `s = "aba"`
- **Output:** `false`
#### Example 3

- **Input:** `s = "abcabcabcabc"`
- **Output:** `true`
- **Explanation:** It is the substring "abc" four times or the substring "abcabc" twice.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of lowercase English letters.