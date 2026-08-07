### 1. Description

Given a positive integer `n`, there exists a **0-indexed** array called `powers`, composed of the **minimum** number of powers of `2` that sum to `n`. The array is sorted in **non-decreasing** order, and there is **only one** way to form the array.

You are also given a **0-indexed** 2D integer array `queries`, where $\text{queries}[i] = [\text{left}_{i}, \text{right}_{i}]$. Each $\text{queries}[i]$ represents a query where you have to find the product of all $\text{powers}[j]$ with $\text{left}_{i} \le j \le \text{right}_{i}$.

Return* an array *`answers`*, equal in length to *`queries`*, where *$\text{answers}[i]$* is the answer to the *$$i^{\text{th}}$$* query*. Since the answer to the $$i^{\text{th}}$$ query may be too large, each $\text{answers}[i]$ should be returned **modulo** $10^{9} + 7$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $n = 15, queries = [[0,1],[2,2],[0,3]]$
- **Output:** `[2,4,64]`
- **Explanation:**
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo $10^{9}$ + 7 yields the same answer, so [2,4,64] is returned.
#### Example 2

- **Input:** $n = 2, queries = [[0,0]]$
- **Output:** `[2]`
- **Explanation:**
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo $10^{9}$ + 7 is the same, so [2] is returned.

### 4. Constraints

- $1 \le n \le 10^{9}$

- $1 \le \text{queries.length} \le 10^{5}$

- $0 \le \text{start}_{i} \le \text{end}_{i} < \text{powers.length}$