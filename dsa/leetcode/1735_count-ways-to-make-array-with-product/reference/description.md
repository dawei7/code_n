### 1. Description

You are given a 2D integer array, `queries`. For each $\text{queries}[i]$, where $\text{queries}[i] = [n_{i}, k_{i}]$, find the number of different ways you can place positive integers into an array of size $n_{i}$ such that the product of the integers is $k_{i}$. As the number of ways may be too large, the answer to the $$i^{\text{th}}$$ query is the number of ways **modulo** $10^{9} + 7$.

Return *an integer array *`answer`* where *$\text{answer.length} = \text{queries.length}$*, and *$\text{answer}[i]$* is the answer to the *$$i^{\text{th}}$$* query.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $queries = [[2,6],[5,1],[73,660]]$
- **Output:** `[4,1,50734910]`
- **Explanation:** Each query is independent.
[2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
[5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
[73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo $10^{9}$ + 7 = 50734910.
#### Example 2

- **Input:** $queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]$
- **Output:** `[1,2,3,10,5]`

### 4. Constraints

- $1 \le \text{queries.length} \le 10^{4}$

- $1 \le n_{i}, k_{i} \le 10^{4}$