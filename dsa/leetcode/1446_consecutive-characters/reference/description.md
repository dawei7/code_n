### 1. Description

The **power** of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string `s`, return *the **power** of* `s`.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `s = "leetcode"`
- **Output:** `2`
- **Explanation:** The substring "ee" is of length 2 with the character 'e' only.

#### Example 2

- **Input:** `s = "abbcccddddeeeeedcba"`
- **Output:** `5`
- **Explanation:** The substring "eeeee" is of length 5 with the character 'e' only.

### 4. Constraints

- $1 \le \text{s.length} \le 500$

- `s` consists of only lowercase English letters.
