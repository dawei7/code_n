### 1. Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

### 2. Function Contract

**Inputs**

- `s`: The lowercase English source string.
- `t`: The lowercase English string to compare with `s`.

**Return value**

Return `true` exactly when both strings have identical character counts; otherwise return `false`.

### 3. Examples

#### Example 1

- **Input:** s = "anagram", t = "nagaram"

- **Output:** true

#### Example 2

- **Input:** s = "rat", t = "car"

- **Output:** false

### 4. Constraints

- $1 \le \text{s.length}, \text{t.length} \le 5 * 10^{4}$

- `s` and `t` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
