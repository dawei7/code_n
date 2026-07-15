# Largest 1-Bordered Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1139 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/largest-1-bordered-square/) |

## Problem Description

### Goal

You are given a two-dimensional `grid` whose entries are `0` or `1`. A square subgrid is 1-bordered when every cell along its top, bottom, left, and right edges contains `1`; cells strictly inside the border may contain either value.

Find the largest such square and return its number of elements, which is the square of its side length. A single cell containing `1` is a valid square of area `1`. If the grid contains no 1-bordered square at all, return `0`.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ binary matrix, where $1 \le m,n \le 100$.
- Every `grid[row][column]` is either `0` or `1`.

Let $q=\min(m,n)$.

**Return value**

The area of the largest square subgrid whose complete border consists of `1`s, or `0` if none exists.

### Examples

**Example 1**

- Input: `grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]`
- Output: `9`
- Explanation: The outer border is all `1`, so the entire $3 \times 3$ grid qualifies despite its zero center.

**Example 2**

- Input: `grid = [[1, 1, 0, 0]]`
- Output: `1`
- Explanation: A one-row grid cannot contain a square with side greater than one, but each `1` is a valid side-one square.

### Required Complexity

- **Time:** $O(mnq)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Precompute directional evidence.** For every cell, record `right[row][column]`, the number of consecutive `1`s beginning there and extending right, and `down[row][column]`, the analogous downward run. Fill both tables from bottom-right toward top-left so the neighboring run needed by each recurrence is already known.

**Test a border with four table lookups.** Consider a square with upper-left corner `(row, column)` and side `side`. Its top and left edges are complete exactly when `right[row][column] >= side` and `down[row][column] >= side`. Its bottom edge begins at `(row + side - 1, column)`, and its right edge begins at `(row, column + side - 1)`. The corresponding two run-length comparisons certify those edges. Interior entries never participate in these checks.

**Search areas from largest to smallest.** Enumerate `side` from $q$ down to `1`, and try every upper-left corner for which the square fits. The first certified border has the largest possible side because all larger side lengths were exhausted first; return `side * side` immediately. If no side-one square is found, every cell is zero and the answer is `0`.

The four comparisons are both necessary and sufficient: each covers one complete edge, including the corners, and together they cover the entire border. Descending enumeration therefore cannot return an invalid square or overlook a larger valid one.

#### Complexity detail

The run-length tables take $O(mn)$ time to build. There are at most $q$ side lengths and at most $mn$ candidate upper-left corners per length, with $O(1)$ work per candidate, giving $O(mnq)$ time. The two $m \times n$ tables use $O(mn)$ auxiliary space.

#### Alternatives and edge cases

- **Rescan every candidate border:** Directly inspect up to $O(q)$ cells for each of $O(mnq)$ candidates, increasing the worst-case time to $O(mnq^2)$.
- **Row and column prefix sums:** Four range-sum queries can also certify a border in constant time after $O(mn)$ preprocessing, with the same overall enumeration bound.
- **Filled-square dynamic programming:** The recurrence for a square containing only `1`s is too strict because zeros are allowed inside this problem's border.
- **Interior zeros:** They do not disqualify a square; only its four edges matter.
- **Single row or column:** The maximum side is one, so the result is `1` if any cell is `1`, otherwise `0`.
- **Broken corner:** A zero at any corner breaks two edges and invalidates that candidate.

</details>
