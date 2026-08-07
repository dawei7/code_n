## Description

Given a `m x n` matrix `mat` and an integer `threshold`, return *the maximum side-length of a square with a sum less than or equal to *`threshold`* or return *`0`* if there is no such square*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

![](images/e1.png)

- **Input:** $mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4$
- **Output:** `2`
- **Explanation:** The maximum side length of square with sum less than or equal to 4 is 2 as shown.
#### Example 2

- **Input:** $mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1$
- **Output:** `0`
### Constraints

- $m = \text{mat.length}$

- $n = \text{mat}[i].length$

- $1 \le m, n \le 300$

- $0 \le \text{mat}[i][j] \le 10^{4}$

- $0 \le threshold \le 10^{5}$