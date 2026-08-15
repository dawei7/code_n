### 1. Description

An integer has **monotone increasing digits** if and only if each pair of adjacent digits `x` and `y` satisfy $x \le y$.

Given an integer `n`, return *the largest number that is less than or equal to *`n`* with **monotone increasing digits***.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $n = 10$
- **Output:** `9`

#### Example 2

- **Input:** $n = 1234$
- **Output:** `1234`

#### Example 3

- **Input:** $n = 332$
- **Output:** `299`

### 4. Constraints

- $0 \le n \le 10^{9}$
