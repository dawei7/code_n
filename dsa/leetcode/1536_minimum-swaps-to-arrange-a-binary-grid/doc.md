# Minimum Swaps to Arrange a Binary Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1536 |
| Difficulty | Medium |
| Topics | Array, Greedy, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/) |

## Problem Description
### Goal

Given an $n\times n$ binary grid, one step may swap two adjacent complete rows. A grid is valid when every cell strictly above the main diagonal is zero.

Return the minimum number of adjacent-row swaps needed to produce a valid grid. If no ordering of the existing rows can satisfy the requirement, return `-1`; columns and the contents within each row cannot be rearranged.

### Function Contract
**Inputs**

- `grid`: An $n\times n$ matrix of zeros and ones, where $1\leq n\leq200$.

**Return value**

Return the minimum adjacent-row swap count that makes every position $(i,j)$ with $j>i$ equal to zero, or `-1` if this is impossible.

### Examples
**Example 1**

- Input: `grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]`
- Output: `3`
- Explanation: The row with two trailing zeros must move to the top, requiring two swaps, and the row with one trailing zero then moves to the middle.

**Example 2**

- Input: four identical rows `[0, 1, 1, 0]`
- Output: `-1`
- Explanation: No row has the three trailing zeros required at the top.

**Example 3**

- Input: `grid = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]`
- Output: `0`
- Explanation: The grid already has only zeros above its main diagonal.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reduce each row to its trailing-zero capacity**

At final row position `i`, all columns after `i` are above the diagonal and must be zero. Therefore, that row needs at least `n - i - 1` trailing zeros. The rest of its contents do not affect validity, so first record one trailing-zero count per row.

**Choose the earliest feasible row greedily**

Process target positions from top to bottom. Find the first row at or below the current position whose trailing-zero count meets the requirement, then move it upward by adjacent swaps. If no such row exists, no later rearrangement can fill this position and the answer is `-1`.

Choosing the earliest feasible row is optimal. Any valid arrangement must bring some feasible remaining row to the current position. A row farther down costs at least as many swaps and passes over every row crossed by the earliest candidate; using the earliest candidate preserves all other rows in their relative order and cannot make a later requirement harder.

The implementation moves only trailing-zero counts, not matrix rows. Adding the candidate's displacement gives exactly the number of adjacent swaps needed to perform the same stable row move.

#### Complexity detail

Counting trailing zeros inspects at most $n^2$ cells. For each of $n$ positions, searching for a feasible row and shifting the capacity list can take $O(n)$ time, for $O(n^2)$ total.

The capacity list contains $n$ integers, giving $O(n)$ auxiliary space. The input grid need not be modified.

#### Alternatives and edge cases

- **Physical row bubbling:** produces the same minimum but copying full rows during each swap can cost $O(n^3)$ time.
- **Try every row permutation:** guarantees a minimum but requires factorial time.
- **Sort by trailing zeros:** unrestricted sorting does not directly account for the adjacent-swap cost or stable minimum movement.
- **Single-cell grid:** there are no cells above the diagonal, so zero swaps are needed.
- **Already valid:** every position immediately finds its current row and contributes zero.
- **Impossible top row:** absence of any row with at least $n-1$ trailing zeros proves impossibility immediately.
- **Extra trailing zeros:** a row may exceed its current requirement and remains feasible.
- **Duplicate capacities:** rows with equal trailing-zero counts are interchangeable for validity; choosing the first minimizes movement.

</details>
