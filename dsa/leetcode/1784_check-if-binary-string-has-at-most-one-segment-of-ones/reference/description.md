### 1. Description

Given a binary string `s` **​​​​​without leading zeros**, return `true`​​​ *if *`s`* contains **at most one contiguous segment of ones***. Otherwise, return `false`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "1001"`
- **Output:** `false`
- **Explanation:** The string has two segments of size 1.
#### Example 2

- **Input:** `s = "110"`
- **Output:** `true`

### 4. Constraints

- $1 \le \text{s.length} \le 100$

- $s[i]$​​​​ is either `'0'` or `'1'`.

- $s[0]$ is `'1'`.