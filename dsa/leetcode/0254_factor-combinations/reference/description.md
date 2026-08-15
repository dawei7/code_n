### 1. Description

Numbers can be regarded as the product of their factors.

- For example, $8 = 2 x 2 x 2 = 2 x 4$.

Given an integer `n`, return *all possible combinations of its factors*. You may return the answer in **any order**.

### 2. Function Contract

**Inputs**

- `n`: Target integer.

**Return value**

Return $List[\text{List}[int]]$ containing all possible factor combinations of `n` (factors in range $[2, n-1]$).

### 3. Note

that the factors should be in the range `[2, n - 1]`.

### 4. Examples

#### Example 1

- **Input:** $n = 1$
- **Output:** `[]`

#### Example 2

- **Input:** $n = 12$
- **Output:** `[[2,6],[3,4],[2,2,3]]`

#### Example 3

- **Input:** $n = 37$
- **Output:** `[]`

### 5. Constraints

- $1 \le n \le 10^{7}$
