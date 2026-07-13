# Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 120 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/triangle/) |

## Problem Description
### Goal
Given a triangular array of integers, choose a connected path from its single top value to some value in the bottom row. If the current value is at index `j` of one row, the next value must be either index `j` or index $j + 1$ in the row directly below.

Return the minimum path sum, including both endpoints and exactly one value from every row. Choices cannot skip levels or move to nonadjacent positions. Entries may be negative, so the path with the smallest individual early value is not necessarily optimal; a one-row triangle simply returns its sole value.

### Function Contract
**Inputs**

- `triangle`: rows of lengths `1, 2, ..., r` containing integer values

**Return value**

The minimum total of any valid top-to-bottom path.

### Examples
**Example 1**

- Input: `triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]`
- Output: `11`

**Example 2**

- Input: `triangle = [[-10]]`
- Output: `-10`

**Example 3**

- Input: `triangle = [[1], [2, 3], [4, 5, 6]]`
- Output: `7`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Bottom-up state removes boundary cases for the two children**

Copy the final row into `dp`. A bottom cell is already the end of a top-to-bottom path, so its minimum suffix cost is its own value. Copying preserves the caller's triangle rather than overwriting its final row.

**Each parent chooses between exactly two already-solved suffixes**

Moving upward, replace `dp[j]` with `triangle[i][j] + min(dp[j], dp[j + 1])`. Before this overwrite, those two DP entries still represent the two children in the row below. Process only the current row's valid positions; extra entries to the right become irrelevant as the active prefix shrinks.

**The active DP prefix represents one complete triangle row**

After processing row `i`, `dp[j]` is the minimum path sum from `triangle[i][j]` to the bottom for every position in that row.

**Trace the triangle collapsing upward**

The bottom costs `[4,1,8,3]` collapse with row `[6,5,7]` to `[7,6,10]`, then with `[3,4]` to `[9,10]`, and finally with `[2]` to `[11]`.

**Each cell has exactly two possible continuations**

Any path leaving a triangle cell moves to its left child or right child. Once the minimum cost from each child to the bottom is known, choosing the smaller and adding the current cell is both attainable and no worse than any other continuation.

The bottom row supplies exact base costs. Collapsing rows upward applies this exhaustive two-choice argument at every cell until the top entry becomes the global minimum path sum.

#### Complexity detail

Every one of the `N` triangle cells is read once, giving $O(N)$ time. The copied bottom row has length `r`, so auxiliary space is $O(r)$.

#### Alternatives and edge cases

- **Enumerate paths:** explores exponentially many left/right choices.
- **Top-down recursion without memoization:** repeats the same suffix subproblems.
- **Mutate the input triangle:** can achieve $O(1)$ auxiliary space but changes caller-owned data.
- A one-row triangle returns its sole value. Negative values require no special case because the recurrence compares complete suffix costs.
- A greedy choice of the smaller immediate child can fail; the DP compares each child's entire optimal remaining path.

</details>
