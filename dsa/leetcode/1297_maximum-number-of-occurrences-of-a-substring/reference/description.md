### 1. Description

Given a string `s`, return the maximum number of occurrences of **any** substring under the following rules:

- The number of unique characters in the substring must be less than or equal to `maxLetters`.

- The substring size must be between `minSize` and `maxSize` inclusive.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).
- `maxLetters`: Input parameter (`int`).
- `minSize`: Input parameter (`int`).
- `maxSize`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4`
- **Output:** `2`
- **Explanation:** Substring "aab" has 2 occurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

#### Example 2

- **Input:** `s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3`
- **Output:** `2`
- **Explanation:** Substring "aaa" occur 2 times in the string. It can overlap.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $1 \le maxLetters \le 26$

- $1 \le minSize \le maxSize \le min(26, \text{s.length})$

- `s` consists of only lowercase English letters.
