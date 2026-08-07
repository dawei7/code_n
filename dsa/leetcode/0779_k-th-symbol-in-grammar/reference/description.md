### 1. Description

We build a table of `n` rows (**1-indexed**). We start by writing `0` in the $1^st$ row. Now in every subsequent row, we look at the previous row and replace each occurrence of `0` with `01`, and each occurrence of `1` with `10`.

- For example, for $n = 3$, the $1^st$ row is `0`, the $2^nd$ row is `01`, and the $3^rd$ row is `0110`.

Given two integer `n` and `k`, return the $$k^{\text{th}}$$ (**1-indexed**) symbol in the $$n^{\text{th}}$$ row of a table of `n` rows.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $n = 1, k = 1$
- **Output:** `0`
- **Explanation:** row 1: <u>0</u>
#### Example 2

- **Input:** $n = 2, k = 1$
- **Output:** `0`
- **Explanation:**
row 1: 0
row 2: <u>0</u>1
#### Example 3

- **Input:** $n = 2, k = 2$
- **Output:** `1`
- **Explanation:**
row 1: 0
row 2: 0<u>1</u>

### 4. Constraints

- $1 \le n \le 30$

- $1 \le k \le 2^n - 1$