# Largest Submatrix With Rearrangements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1727 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-submatrix-with-rearrangements/) |

## Problem Description

### Goal

You are given an $m\times n$ binary matrix. You may rearrange its columns in any order: moving a column moves that entire column, so the relative vertical contents of every column remain unchanged. After choosing the column order, consider ordinary rectangular submatrices of the rearranged matrix.

Return the largest possible area of a submatrix in which every element is `1`. The column order may be chosen specifically to maximize this one rectangle, but entries within a column and the order of the rows cannot be changed.

### Function Contract

**Inputs**

- `matrix`: an $m\times n$ array whose entries are `0` or `1`, where $1 \le mn \le 10^5$.

**Return value**

- Return the maximum area of an all-ones rectangular submatrix obtainable after one optimal rearrangement of the complete columns.

### Examples

**Example 1**

- Input: `matrix = [[0,0,1],[1,1,1],[1,0,1]]`
- Output: `4`
- Explanation: Reordering complete columns can place two columns with height-two runs next to each other, producing an all-ones rectangle of height two and width two.

**Example 2**

- Input: `matrix = [[1,0,1,0,1]]`
- Output: `3`
- Explanation: Place the three columns containing `1` together to form a one-row rectangle of width three.

**Example 3**

- Input: `matrix = [[1,1,0],[1,0,1]]`
- Output: `2`
- Explanation: Entire columns must move together; the rows cannot select independent column orders.

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Measure the vertical run ending at each row**

Let `heights[column]` be the number of consecutive `1`s ending at the current row in that original column. A current `1` extends the previous height by one, while a current `0` resets it to zero. If $w$ columns have heights of at least $h$, one global column permutation can place those complete columns together, creating an all-ones rectangle of height $h$ and width $w$ ending at this row.

It is valid to evaluate a different best permutation for each possible bottom row: the answer needs only one rectangle. Whichever row produces the maximum also supplies one concrete set of columns that can be moved together by a single permutation.

**Preserve descending height order without sorting again**

Maintain `order`, a list of column indices arranged by non-increasing height after the previous row. Scan those indices in that order for the current row. Put columns containing `1` into a `positive` list and increment their heights; put columns containing `0` into a `zero` list and reset their heights.

Filtering an already ordered sequence preserves the relative order of the selected positive columns. Adding one to every selected height preserves their comparisons as well. All reset columns have height zero, so `order = positive + zero` is again ordered by non-increasing height. This maintains the same information that sorting the height array would provide, using only linear work per row.

**Turn each ordered prefix into a rectangle**

Within `positive`, the height at position `width - 1` is the smallest height among the first `width` columns. Those columns can therefore form a rectangle with area `width * heights[column]`. Evaluate every positive prefix. Every feasible all-ones rectangle ending at this row corresponds to some height threshold and selected-column count, so one of these prefixes attains at least its area.

#### Complexity detail

Each of the $m$ rows scans all $n$ columns once to update the stable order and at most $n$ positive columns once to evaluate areas. The total time is $O(mn)$. The height array, column order, and two temporary column lists each contain at most $n$ indices or values, so the auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Sort heights on every row:** Updating vertical heights and sorting them in descending order is simpler and correct, but takes $O(mn\log n)$ time instead of preserving their order in $O(mn)$.
- **Enumerate column subsets:** Testing which columns can be made adjacent explores exponentially many subsets and ignores that only each column's current height matters.
- **All zeros:** Every height remains zero, so no positive prefix exists and the answer is zero.
- **All ones:** Heights increase on every row and all columns remain positive, yielding the entire matrix area $mn$.
- **Single row:** The answer is the number of `1`s, because all such columns can be placed together.
- **Single column:** Rearrangement has no effect; the answer is the longest vertical run of `1`s.
- **Column integrity:** Reordering cannot combine a top portion of one column with a bottom portion of another; vertical heights always belong to original complete columns.

</details>
