# Rank Scores

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 178 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/rank-scores/) |

## Problem Description
### Goal
The `Scores` table contains one score per row, and multiple rows may have the same score. Assign rankings by descending score so that the highest distinct score receives rank `1` and equal score values receive the same rank.

Return every input score together with its column named `rank`, ordered from highest score to lowest. Use dense ranking: after any tie, the next lower distinct score receives the immediately following integer without a gap. Preserve a result row for every source row rather than collapsing duplicates, and expose only the requested `score` and `rank` columns.

### Function Contract
**Inputs**

- `Scores(id, score)`: score rows, including possible ties

**Return value**

A result grid with columns `score` and `rank`, ordered by score descending.

### Examples
**Example 1**

- Scores: `3.50, 3.65, 4.00, 3.85, 4.00, 3.65`
- Ranks: both `4.00` rows rank 1, `3.85` ranks 2, both `3.65` rows rank 3, and `3.50` ranks 4

**Example 2**

- One score receives rank 1.

**Example 3**

- Three equal scores all receive rank 1.

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

This problem requires **dense ranking**. Equal scores share a rank, and moving to the next lower distinct score increases the rank by exactly one, regardless of how many tied rows came before it.

`DENSE_RANK() OVER (ORDER BY score DESC)` implements those rules directly. The window order determines rank values but does not guarantee the final presentation order, so the outer query should also order by score descending. A stable secondary key such as `id` may make tied rows deterministic without including it in the window order; including `id` inside the window would break ties and assign different ranks.

For `4.00, 4.00, 3.85, 3.65, 3.65, 3.50`, the window encounters four distinct score levels. Both `4.00` rows receive rank 1; the next distinct level receives 2 rather than 3; both `3.65` rows receive 3; and `3.50` receives 4.

The distinction among SQL ranking functions is essential:

- `ROW_NUMBER()` assigns a unique position to every row, so tied scores differ.
- `RANK()` shares ranks across ties but leaves gaps afterward.
- `DENSE_RANK()` shares ranks and leaves no gaps, matching this contract.

Descending window order encounters score values from greatest to least. `DENSE_RANK` starts at one and increments exactly when the ordering value changes, so a row's rank is one plus the number of distinct scores greater than its score. This is precisely the required dense-rank definition. Because window functions retain every original row, all tied rows remain present and receive the same value. The outer ordering then presents the complete correct result from highest to lowest.

#### Complexity detail

Without an appropriate index, the engine generally sorts `n` rows for $O(n \log n)$ work and may use $O(n)$ sorting/window storage. An index ordered by score can reduce or eliminate explicit sorting, subject to the query optimizer.

#### Alternatives and edge cases

- A correlated subquery can compute `1 + COUNT(DISTINCT higher_score)` for every row, but may perform $O(n^2)$ comparisons without decorrelation or indexing.
- `RANK` and `ROW_NUMBER` have different tie semantics and are not interchangeable with `DENSE_RANK` here.
- All-equal scores all receive rank one. A single row also receives rank one.
- Fractional, zero, or negative scores follow ordinary numeric descending order.
- A secondary output sort key may stabilize ties, but it must not participate in the rank window.

</details>
