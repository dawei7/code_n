# Find Valid Matrix Given Row and Column Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1605 |
| Difficulty | Medium |
| Topics | Array, Greedy, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/) |

## Problem Description
### Goal
Arrays `rowSum` and `colSum` describe the margins of an unknown matrix of non-negative integers. Value `rowSum[i]` is the required sum of row $i$, while `colSum[j]` is the required sum of column $j$.

Construct and return any matrix with `len(rowSum)` rows and `len(colSum)` columns that realizes all of those sums. A valid matrix is guaranteed to exist, so the totals of the two margin arrays agree; the individual cell values are not required to match one particular arrangement.

### Function Contract
**Inputs**

- `rowSum`: an array of $m$ non-negative row totals, where $1 \le m \le 500$ and every total is at most $10^8$.
- `colSum`: an array of $n$ non-negative column totals, where $1 \le n \le 500$ and every total is at most $10^8$.
- The inputs satisfy $\sum_{i=0}^{m-1}\texttt{rowSum[i]}=\sum_{j=0}^{n-1}\texttt{colSum[j]}$.

**Return value**

Return any $m \times n$ matrix of non-negative integers whose row sums equal `rowSum` and whose column sums equal `colSum`.

### Examples
**Example 1**

- Input: `rowSum = [3, 8]`, `colSum = [4, 7]`
- Output: `[[3, 0], [1, 7]]`
- Explanation: Its row sums are 3 and 8, and its column sums are 4 and 7. `[[1, 2], [3, 5]]` would be valid as well.

**Example 2**

- Input: `rowSum = [5, 7, 10]`, `colSum = [8, 6, 8]`
- Output: `[[5, 0, 0], [3, 4, 0], [0, 2, 8]]`
