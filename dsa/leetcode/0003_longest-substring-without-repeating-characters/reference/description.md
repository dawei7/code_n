### 1. Description

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

### 2. Function Contract

**Inputs**

- `s`: The string to examine.

**Return value**

Return the greatest length of a substring containing no duplicate character.

### 3. Examples

#### Example 1

- **Input:** `s = "abcabcbb"`
- **Output:** `3`
- **Explanation:** The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
#### Example 2

- **Input:** `s = "bbbbb"`
- **Output:** `1`
- **Explanation:** The answer is "b", with the length of 1.
#### Example 3

- **Input:** `s = "pwwkew"`
- **Output:** `3`
- **Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### 4. Constraints

- $0 \le \text{s.length} \le 10^{5}$

- `s` consists of English letters, digits, symbols and spaces.