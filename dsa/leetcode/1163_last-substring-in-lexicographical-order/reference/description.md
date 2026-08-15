### 1. Description

Given a string `s`, return *the last substring of* `s` *in lexicographical order*.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** `s = "abab"`
- **Output:** `"bab"`
- **Explanation:** The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

#### Example 2

- **Input:** `s = "leetcode"`
- **Output:** `"tcode"`

### 4. Constraints

- $1 \le \text{s.length} \le 4 * 10^{5}$

- `s` contains only lowercase English letters.
