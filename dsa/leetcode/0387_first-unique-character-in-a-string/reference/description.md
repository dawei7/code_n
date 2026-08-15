### 1. Description

Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

**Return value**

Return the smallest index whose character has total frequency one, or `-1` if every character repeats.

### 3. Examples

#### Example 1

- **Input:** s = "leetcode"

- **Output:** 0

- **Explanation:** The character `'l'` at index 0 is the first character that does not occur at any other index.

#### Example 2

- **Input:** s = "loveleetcode"

- **Output:** 2

#### Example 3

- **Input:** s = "aabb"

- **Output:** -1

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of only lowercase English letters.
