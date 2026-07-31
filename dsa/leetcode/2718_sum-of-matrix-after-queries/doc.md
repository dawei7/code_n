# Sum of Matrix After Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2718 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/sum-of-matrix-after-queries/) |

## Problem Description

### Goal

Begin with an $n \times n$ integer matrix whose cells are all zero. Apply the entries of `queries` in their given order. Every query has the form `[type, index, value]` and overwrites a complete line rather than adding to its existing cells.

When `type == 0`, set every cell in row `index` to `value`. When `type == 1`, set every cell in column `index` to `value`. Later queries may overwrite some or all values written earlier. After all $q$ queries have been processed, return the sum of every matrix entry without requiring the final matrix itself.

### Function Contract

**Inputs**

- `n`: The row and column count, where $1 \le n \le 10^4$.
- `queries`: A list of $q$ triplets `[type, index, value]`, where $1 \le q \le 5\cdot10^4$, `type` is $0$ or $1$, $0 \le \texttt{index} < n$, and $0 \le \texttt{value} \le 10^5$.

**Return value**

Return the sum of all $n^2$ matrix cells after applying the queries in order.

### Examples

**Example 1**

- Input: `n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]`
- Output: `23`
- Explanation: The final matrix is `[[4,1,2],[4,0,2],[4,3,3]]`, whose entries sum to $23$.

**Example 2**

- Input: `n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]`
- Output: `17`
- Explanation: The last assignments to columns $0$ and $2$ overwrite one cell in each previously assigned row.

**Example 3**

- Input: `n = 4, queries = [[0,1,2],[1,2,3]]`
- Output: `18`
- Explanation: The row contributes three cells of value $2$ after its intersection is overwritten, while the column contributes four cells of value $3$.
