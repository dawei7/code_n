### 1. Description

Given a string `s` and an integer `k`, reverse the first `k` characters for every `2k` characters counting from the start of the string.

If there are fewer than `k` characters left, reverse all of them. If there are less than `2k` but greater than or equal to `k` characters, then reverse the first `k` characters and leave the other as original.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "abcdefg", k = 2`
- **Output:** `"bacdfeg"`
#### Example 2

- **Input:** `s = "abcd", k = 2`
- **Output:** `"bacd"`

### 4. Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of only lowercase English letters.

- $1 \le k \le 10^{4}$