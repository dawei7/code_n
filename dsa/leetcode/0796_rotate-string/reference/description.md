### 1. Description

Given two strings `s` and `goal`, return `true` *if and only if* `s` *can become* `goal` *after some number of **shifts** on* `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "abcde", goal = "cdeab"`
- **Output:** `true`
#### Example 2

- **Input:** `s = "abcde", goal = "abced"`
- **Output:** `false`

### 4. Constraints

- $1 \le \text{s.length}, \text{goal.length} \le 100$

- `s` and `goal` consist of lowercase English letters.