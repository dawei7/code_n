## Description

You have `n` gardens, labeled from `1` to `n`, and an array `paths` where $\text{paths}[i] = [x_{i}, y_{i}]$ describes a bidirectional path between garden $x_{i}$ to garden $y_{i}$. In each garden, you want to plant one of 4 types of flowers.

All gardens have **at most 3** paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return ***any** such a choice as an array *`answer`*, where *$\text{answer}[i]$* is the type of flower planted in the *$(i+1)^th$* garden. The flower types are denoted *`1`*, *`2`*, *`3`*, or *`4`*. It is guaranteed an answer exists.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $n = 3, paths = [[1,2],[2,3],[3,1]]$
- **Output:** `[1,2,3]`
- **Explanation:**
Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
#### Example 2

- **Input:** $n = 4, paths = [[1,2],[3,4]]$
- **Output:** `[1,2,1,2]`
#### Example 3

- **Input:** $n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]$
- **Output:** `[1,2,3,4]`
### Constraints

- $1 \le n \le 10^{4}$

- $0 \le \text{paths.length} \le 2 * 10^{4}$

- $\text{paths}[i].length = 2$

- $1 \le x_{i}, y_{i} \le n$

- $x_{i} \neq y_{i}$

- Every garden has **at most 3** paths coming into or leaving it.