### 1. Description

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

- `'.'` Matches any single character.​​​​

- `'*'` Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string (not partial).

### 2. Function Contract

**Inputs**

- `s`: The lowercase input string.
- `p`: The valid pattern containing lowercase letters, `.` and `*`.

**Return value**

Return `True` when `p` matches all of `s`; otherwise return `False`.

### 3. Examples

#### Example 1

- **Input:** `s = "aa", p = "a"`
- **Output:** `false`
- **Explanation:** "a" does not match the entire string "aa".
#### Example 2

- **Input:** `s = "aa", p = "a*"`
- **Output:** `true`
- **Explanation:** '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
#### Example 3

- **Input:** `s = "ab", p = ".*"`
- **Output:** `true`
- **Explanation:** ".*" means "zero or more (*) of any character (.)".

### 4. Constraints

- $1 \le \text{s.length} \le 20$

- $1 \le \text{p.length} \le 20$

- `s` contains only lowercase English letters.

- `p` contains only lowercase English letters, `'.'`, and `'*'`.

- It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.