### 1. Description

You are given three integers `n`, `m`, `k`. A **good array** `arr` of size `n` is defined as follows:

- Each element in `arr` is in the **inclusive** range `[1, m]`.

- *Exactly* `k` indices `i` (where $1 \le i < n$) satisfy the condition $arr[i - 1] = \text{arr}[i]$.

Return the number of **good arrays** that can be formed.

Since the answer may be very large, return it **modulo **$10^{9} + 7$.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).
- `m`: Input parameter (`int`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** n = 3, m = 2, k = 1

- **Output:** 4

- **Explanation:** 

- There are 4 good arrays. They are `[1, 1, 2]`, `[1, 2, 2]`, `[2, 1, 1]` and `[2, 2, 1]`.

- Hence, the answer is 4.

#### Example 2

- **Input:** n = 4, m = 2, k = 2

- **Output:** 6

- **Explanation:** 

- The good arrays are `[1, 1, 1, 2]`, `[1, 1, 2, 2]`, `[1, 2, 2, 2]`, `[2, 1, 1, 1]`, `[2, 2, 1, 1]` and `[2, 2, 2, 1]`.

- Hence, the answer is 6.

#### Example 3

- **Input:** n = 5, m = 2, k = 0

- **Output:** 2

- **Explanation:** 

- The good arrays are `[1, 2, 1, 2, 1]` and `[2, 1, 2, 1, 2]`. Hence, the answer is 2.

### 4. Constraints

- $1 \le n \le 10^{5}$

- $1 \le m \le 10^{5}$

- $0 \le k \le n - 1$
