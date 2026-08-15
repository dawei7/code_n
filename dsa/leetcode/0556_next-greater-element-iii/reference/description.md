### 1. Description

Given a positive integer `n`, find *the smallest integer which has exactly the same digits existing in the integer* `n` *and is greater in value than* `n`. If no such positive integer exists, return `-1`.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Note

that the returned integer should fit in **32-bit integer**, if there is a valid answer but it does not fit in **32-bit integer**, return `-1`.

### 4. Examples

#### Example 1

- **Input:** $n = 12$
- **Output:** `21`

#### Example 2

- **Input:** $n = 21$
- **Output:** `-1`

### 5. Constraints

- $1 \le n \le 2^{31} - 1$
