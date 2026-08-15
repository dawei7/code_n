### 1. Description

Given a string `s` consisting of lowercase English letters. Perform the following operation:

- Select any non-empty substring then replace every letter of the substring with the preceding letter of the English alphabet. For example, 'b' is converted to 'a', and 'a' is converted to 'z'.

Return the **lexicographically smallest** string **after performing the operation**.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** s = "cbabc"

- **Output:** "baabc"

- **Explanation:** Perform the operation on the substring starting at index 0, and ending at index 1 inclusive.

#### Example 2

- **Input:** s = "aa"

- **Output:** "az"

- **Explanation:** Perform the operation on the last letter.

#### Example 3

- **Input:** s = "acbbc"

- **Output:** "abaab"

- **Explanation:** Perform the operation on the substring starting at index 1, and ending at index 4 inclusive.

#### Example 4

- **Input:** s = "leetcode"

- **Output:** "kddsbncd"

- **Explanation:** Perform the operation on the entire string.

### 4. Constraints

- $1 \le \text{s.length} \le 3 * 10^{5}$

- `s` consists of lowercase English letters
