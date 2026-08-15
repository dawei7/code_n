### 1. Description

Return the number of **distinct** non-empty substrings of `text` that can be written as the concatenation of some string with itself (i.e. it can be written as $a + a$ where `a` is some string).

### 2. Function Contract

**Inputs**

- `text`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $text = "abcabcabc"$
- **Output:** `3`
- **Explanation:** The 3 substrings are "abcabc", "bcabca" and "cabcab".

#### Example 2

- **Input:** $text = "leetcodeleetcode"$
- **Output:** `2`
- **Explanation:** The 2 substrings are "ee" and "leetcodeleetcode".

### 4. Constraints

- $1 \le \text{text.length} \le 2000$

- `text` has only lowercase English letters.
