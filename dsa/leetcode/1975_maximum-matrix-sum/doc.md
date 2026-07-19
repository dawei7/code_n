# Maximum Matrix Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1975 |
| Difficulty | Medium |
| Topics | Array, Greedy, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-matrix-sum/) |

## Problem Description
### Goal
You are given an $n\times n$ integer matrix. In one operation, choose two
cells that share an edge and multiply both values by `-1`. You may perform the
operation any number of times and may reuse cells.

Return the greatest possible sum of all matrix entries after applying an
optimal sequence of operations. Adjacency is only horizontal or vertical;
diagonally touching cells are not adjacent.

### Function Contract
**Inputs**

- `matrix`: an $n\times n$ integer grid, where $2 \le n \le 250$.
- Every value lies in the inclusive range from $-10^5$ through $10^5$.
- Let $M=n^2$ denote the number of cells.

**Return value**

- The maximum achievable sum of all $M$ entries after any number of legal
  adjacent-pair sign flips.

### Examples
**Example 1**

- Input: `matrix = [[1, -1], [-1, 1]]`
- Output: `4`

**Example 2**

- Input: `matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]`
- Output: `16`

**Example 3**

- Input: `matrix = [[-1, 0], [-2, -3]]`
- Output: `6`

### Required Complexity
- **Time:** $O(M)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate magnitudes from sign parity**

Every operation changes two signs and never changes an absolute value.
Because the grid's adjacency graph is connected, sign changes can be moved
along paths: two negative signs can be brought together and eliminated.
Consequently, an even number of negative entries permits every magnitude to
be positive.

If the negative count is odd and no zero is available, an odd negative count
must remain because every operation changes that count by an even amount.
To maximize the sum, assign the unavoidable negative sign to the entry with
the smallest absolute value. A zero has magnitude zero, so the same formula
also handles it without a separate branch.

**Compute the best sum in one scan**

Accumulate the sum of every absolute value, count negative entries, and track
the smallest magnitude. With an even negative count, return the absolute-value
sum. With an odd count, changing the smallest magnitude from positive to
negative reduces that sum by twice its magnitude, so return

$$
\sum_{i,j}\lvert\texttt{matrix[i][j]}\rvert
-2\min_{i,j}\lvert\texttt{matrix[i][j]}\rvert.
$$

The construction argument shows this bound is reachable, while parity shows
that no arrangement can avoid the stated loss when the negative count is odd.

#### Complexity detail

There are $M=n^2$ cells. The algorithm reads each cell once and performs
constant work, giving $O(M)$ time. The accumulated sum, negative count, and
smallest magnitude use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Simulate sign-flip operations:** Searching sequences of adjacent flips
  creates an enormous state space and is unnecessary once the parity invariant
  is identified.
- **Sort all magnitudes:** Sorting reveals the smallest magnitude but costs
  $O(M\log M)$ time and $O(M)$ storage when a running minimum suffices.
- **Repeated minimum scans:** Recomputing the global minimum while processing
  every cell remains correct but takes $O(M^2)$ time.
- Zero absorbs the unavoidable odd sign at no sum cost because `-0 == 0`.
- With an even negative count, every entry can contribute its full absolute
  value regardless of where those negatives initially occur.
- With an odd negative count, the smallest magnitude is sacrificed even when
  that entry was initially positive.
- Large values require a return type capable of holding sums beyond 32-bit
  signed range.

</details>
