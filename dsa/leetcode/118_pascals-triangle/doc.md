# Pascal's Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 118 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/pascals-triangle/) |

## Problem Description
### Goal
Given a positive integer `num_rows`, generate that many rows of Pascal's triangle. The triangle begins with the single value `1`; each later row contains one more entry than the row above it, starts and ends with `1`, and derives every interior entry from the two adjacent values above.

Return all rows in top-to-bottom order, with row lengths increasing from one through `num_rows`. Values must be represented as integers and grouped by row rather than flattened into one sequence. For example, requesting one row returns only `[[1]]`, while larger requests must preserve the triangle's symmetry and addition rule at every position.

### Function Contract
**Inputs**

- `num_rows`: the positive number of rows to generate

**Return value**

The triangle as a list of rows from top to bottom.

### Examples
**Example 1**

- Input: `num_rows = 5`
- Output: `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`

**Example 2**

- Input: `num_rows = 1`
- Output: `[[1]]`

**Example 3**

- Input: `num_rows = 3`
- Output: `[[1], [1, 1], [1, 2, 1]]`

### Required Complexity

- **Time:** $O(num_rows^2)$
- **Space:** $O(num_rows^2)$

<details>
<summary>Approach</summary>

#### General

**Allocate each row with its boundary coefficients already fixed**

For zero-based row index `i`, allocate $i + 1$ entries initialized to `1`. Pascal's boundary identity $\binom{i}{0} = \binom{i}{i} = 1$ means the first and last entries need no recurrence calculation.

**Every interior coefficient has exactly two parents**

For each `j` from `1` through $i - 1$, assign `previous[j - 1] + previous[j]`. These are the two diagonally adjacent entries above the new position. Only the immediately preceding row is needed for computation, while older rows remain because the output contract requires the full triangle.

**Completed rows are immutable inputs to the next row**

Before constructing row `i`, every earlier row is complete and satisfies Pascal's recurrence. After filling the interior, row `i` has correct boundaries and every interior sum, extending the invariant.

**Trace the fifth row from its two-parent sums**

From `[1, 3, 3, 1]`, the interior values become $1+3=4$, $3+3=6$, and $3+1=4$. With boundary ones, the new row is `[1, 4, 6, 4, 1]`.

**Boundary ones and adjacent sums are Pascal's definition**

The first row contains the single boundary value one. For every later row, the two boundaries are again one, while each interior entry is the sum of the two entries above it in the preceding row.

Those assignments are exactly Pascal's recurrence. Starting from the correct base row and applying it to every position constructs each requested row without omission or alteration.

#### Complexity detail

The triangle contains $1 + 2 + \dots + num_rows = O(num_rows^2)$ values, each written once. Time and returned storage are therefore both $O(num_rows^2)$; auxiliary working storage beyond the output is $O(num_rows)$ for the current row.

#### Alternatives and edge cases

- **Compute binomial coefficients independently:** can avoid previous-row access but performs more arithmetic or requires careful multiplicative formulas.
- **Recursive definition:** repeats the same coefficient subproblems without memoization.
- **Return only the final row:** solves Problem 119, not this full-triangle contract.
- `num_rows = 1` returns only `[1]`; no previous-row access occurs.
- Each returned row must be a distinct list. Reusing one mutable row object would make earlier output rows change during later updates.

</details>
