# Maximum Side Length of a Square with Sum Less than or Equal to Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1292 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Matrix, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/) |

## Problem Description
### Goal
Given an $m \times n$ matrix `mat` of nonnegative integers and an integer `threshold`, consider every contiguous square submatrix and the sum of all values inside it. A candidate square must use the same number of consecutive rows and consecutive columns.

Return the maximum side length among squares whose sum is less than or equal to `threshold`. Return zero when no one-cell square satisfies the limit; otherwise return the largest feasible positive length.

### Function Contract
**Inputs**

- `mat`: an $m \times n$ matrix, where $1 \le m,n \le 300$ and $0 \le \texttt{mat[r][c]} \le 10^4$.
- `threshold`: an integer satisfying $0 \le \texttt{threshold} \le 10^5$.

**Return value**

The largest integer $s$ for which at least one $s \times s$ submatrix has sum at most `threshold`, or zero if no positive side length is valid.

### Examples
**Example 1**

- Input: `mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]`, `threshold = 4`
- Output: `2`

**Example 2**

- Input: `mat = [[2,2],[2,2]]`, `threshold = 1`
- Output: `0`

**Example 3**

- Input: `mat = [[1,0,1],[0,1,0],[1,0,1]]`, `threshold = 2`
- Output: `2`

### Required Complexity
- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Query any square in constant time.** Build a two-dimensional prefix-sum table with an extra zero row and column. Inclusion-exclusion then gives the sum of a square from its four prefix corners in $O(1)$ time.

Maintain the largest valid side length `best` found anywhere so far. At each possible top-left cell, test the square of side `best + 1`; while it fits and its sum is within the threshold, increment `best` and try the next size from that same corner. There is no reason to retest smaller sizes because they cannot improve the answer.

All matrix entries are nonnegative, so enlarging a square at a fixed corner cannot reduce its sum. A failed candidate therefore rules out every larger square from that corner. Conversely, any square capable of improving the answer is eventually tested when its top-left cell is visited. The scan can neither skip a valid improvement nor accept an invalid one, so the final global `best` is exact.

#### Complexity detail

Building the prefix table and visiting all top-left cells take $O(mn)$ time. Each cell performs at most one failing sum query, while successful queries increase one global `best` at most $\min(m,n)$ times over the entire scan. Thus the total remains $O(mn)$. The prefix table uses $O(mn)$ space.

#### Alternatives and edge cases

- **Binary search the side length:** Prefix sums make feasibility monotone, giving $O(mn\log\min(m,n))$ time, but the global incremental scan removes that logarithmic factor.
- **Enumerate every side length:** Testing all placements for every size takes $O(mn\min(m,n))$ even with prefix sums.
- **Direct cell summation:** Recomputing every square from its cells repeats substantial work and is slower still.
- **No valid cell:** If all entries exceed the threshold, the answer remains zero.
- **Zero-valued matrix:** A sufficiently large all-zero rectangle admits a square of side $\min(m,n)$.

</details>
