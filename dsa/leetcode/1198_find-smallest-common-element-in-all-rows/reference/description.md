## Description

Given an `m x n` matrix `mat` where every row is sorted in **strictly** **increasing** order, return *the **smallest common element** in all rows*.

If there is no common element, return `-1`.
### Function Contract

**Input**

- `mat`: A nonempty rectangular integer matrix whose rows are strictly increasing.

Let $m$ be `mat.length` and let $n$ be the length of each row. An element is common only when it appears in all $m$ rows.

**Return value**

Return the smallest integer present in every row of `mat`, or `-1` when no such integer exists.

### Examples

#### Example 1

- **Input:** $mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]$
- **Output:** `5`
#### Example 2

- **Input:** $mat = [[1,2,3],[2,3,4],[2,3,5]]$
- **Output:** `2`
### Constraints

- $m = \text{mat.length}$

- $n = \text{mat}[i].length$

- $1 \le m, n \le 500$

- $1 \le \text{mat}[i][j] \le 10^{4}$

- $\text{mat}[i]$ is sorted in strictly increasing order.