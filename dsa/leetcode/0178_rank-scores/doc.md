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
