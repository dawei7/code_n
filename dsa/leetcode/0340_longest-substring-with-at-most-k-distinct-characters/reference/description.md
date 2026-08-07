### 1. Description

Given a string `s` and an integer `k`, return *the length of the longest **substring** of* `s` *that contains at most* `k` ***distinct** characters*.

### 2. Function Contract

**Inputs**

- `s`: The source string.
- `k`: The maximum number of distinct characters allowed in the substring.

**Return value**

Return the maximum length of a contiguous substring with no more than `k` distinct characters.

### 3. Examples

#### Example 1

- **Input:** `s = "eceba", k = 2`
- **Output:** `3`
- **Explanation:** The substring is "ece" with length 3.
#### Example 2

- **Input:** `s = "aa", k = 1`
- **Output:** `2`
- **Explanation:** The substring is "aa" with length 2.

### 4. Constraints

- $1 \le \text{s.length} \le 5 * 10^{4}$

- $0 \le k \le 50$