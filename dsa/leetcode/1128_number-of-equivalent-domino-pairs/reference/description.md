### 1. Description

Given a list of `dominoes`, $\text{dominoes}[i] = [a, b]$ is **equivalent to** $\text{dominoes}[j] = [c, d]$ if and only if either ($a = c$ and $b = d$), or ($a = d$ and $b = c$) - that is, one domino can be rotated to be equal to another domino.

Return *the number of pairs *`(i, j)`* for which *$0 \le i < j < \text{dominoes.length}$*, and *$\text{dominoes}[i]$* is **equivalent to** *$\text{dominoes}[j]$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $dominoes = [[1,2],[2,1],[3,4],[5,6]]$
- **Output:** `1`
#### Example 2

- **Input:** $dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]$
- **Output:** `3`

### 4. Constraints

- $1 \le \text{dominoes.length} \le 4 * 10^{4}$

- $\text{dominoes}[i].length = 2$

- $1 \le \text{dominoes}[i][j] \le 9$