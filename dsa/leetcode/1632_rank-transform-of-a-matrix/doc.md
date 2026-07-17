# Rank Transform of a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1632 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Union-Find, Graph Theory, Topological Sort, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rank-transform-of-a-matrix/) |

## Problem Description
### Goal
Given an $R\times C$ integer matrix, assign a positive integer rank to every cell. Within any one row or column, a smaller value must have a smaller rank, an equal value must have the same rank, and a larger value must have a larger rank. Equal values that are linked through a chain of shared rows or columns must therefore be coordinated together.

Among all assignments satisfying those comparisons, every rank must be as small as possible. The test data guarantees a unique resulting matrix. Return that rank matrix without changing the input values.

### Function Contract
**Inputs**

- `matrix`: an $R\times C$ integer matrix, where $1 \le R,C \le 500$ and $-10^9 \le \texttt{matrix[r][c]} \le 10^9$.
- Let $V=RC$ be the number of cells.

**Return value**

Return an $R\times C$ matrix containing the unique minimum valid positive rank for every input cell.

### Examples
**Example 1**

- Input: `matrix = [[1,2],[3,4]]`
- Output: `[[1,2],[2,3]]`

The largest cell must exceed the rank-2 cells that precede it in its row and column.

**Example 2**

- Input: `matrix = [[7,7],[7,7]]`
- Output: `[[1,1],[1,1]]`

Every cell is connected through equal row or column values, so all receive the smallest rank.

**Example 3**

- Input: `matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]`
- Output: `[[4,2,3],[1,3,4],[5,1,6],[1,3,4]]`

### Required Complexity
- **Time:** $O(V\log V)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Process values from low to high.** Maintain the greatest rank already assigned in every row and every column. When handling value $x$, all strictly smaller values have finalized ranks, while no larger value has influenced the trackers. A cell `(r,c)` with value $x$ must therefore receive at least `1 + max(row_rank[r], column_rank[c])`.

**Unify equal cells before assigning ranks.** Equal cells sharing a row or column must have the same rank. For the current value, represent each involved row and column as a union-find node and union the row node with the column node for every cell. Connected components are exactly the transitive groups of equal cells constrained to share a rank.

**Assign a whole value batch atomically.** For each component, take one plus the maximum existing row or column rank over all its cells. Record every component rank before updating any tracker. This atomic step prevents one equal component from incorrectly influencing another disconnected component of the same value. Then write the answers and raise the affected row and column trackers.

Every assigned component rank exceeds all smaller values in each participating row and column, so all strict comparisons are respected. Equal connected cells are unified and receive one rank. Conversely, any valid assignment must exceed the same previously finalized tracker maximum, so the chosen rank is the smallest possible for that component. Induction over sorted values proves the complete matrix is the unique minimum assignment.

#### Complexity detail

Grouping and sorting the $V$ cells by value takes $O(V\log V)$ time. Across all value batches, union-find, grouping, assignment, and tracker updates process $O(V)$ cells with near-constant amortized union-find cost. Total time is $O(V\log V)$. The value groups, temporary components, trackers, and answer use $O(V)$ space.

#### Alternatives and edge cases

- **Component DAG:** Build equality components, add directed constraints from smaller to larger components within rows and columns, then compute longest-path ranks. This is correct but materializing and deduplicating the graph is more involved.
- **Repeatedly scan for the next value:** Avoiding the initial sort by linearly searching all unprocessed cells for each distinct value can take $O(V^2)$ time.
- **Rank equal cells independently:** This violates the equality rule when equal cells share a row or column, including through a transitive chain.
- Equal values in different rows and columns are not necessarily connected and can receive different ranks.
- All-equal matrices receive rank 1 everywhere.
- A value batch must be assigned before its row and column trackers are updated.
- Negative values and large magnitude do not affect the relative-order reasoning.

</details>
