### 1. Description

Given a binary string `s`, return *the number of substrings with all characters* `1`*'s*. Since the answer may be too large, return it modulo $10^{9} + 7$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "0110111"`
- **Output:** `9`
- **Explanation:** There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
#### Example 2

- **Input:** `s = "101"`
- **Output:** `2`
- **Explanation:** Substring "1" is shown 2 times in s.
#### Example 3

- **Input:** `s = "111111"`
- **Output:** `21`
- **Explanation:** Each substring contains only 1's characters.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $s[i]$ is either `'0'` or `'1'`.