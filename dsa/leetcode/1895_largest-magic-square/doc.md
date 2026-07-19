# Largest Magic Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1895 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/largest-magic-square/) |

## Problem Description

### Goal

A square region of side length $k$ is magic when the sum along each of its $k$ rows, the sum along each of its $k$ columns, and the sums along its two corner-to-corner diagonals are all the same. Its entries are not required to be distinct, and every single-cell square satisfies the definition.

Given a rectangular integer matrix, consider every contiguous square subgrid contained within it. Return the side length of the largest one that is magic.

### Function Contract

**Inputs**

- `grid`: an $M \times N$ matrix of positive integers, where $1 \le M, N \le 50$ and every entry is at most $10^6$.

Let $S = \min(M, N)$ be the greatest possible side length of a square inside the matrix.

**Return value**

Return the largest side length $k$ for which some contiguous $k \times k$ subgrid has equal row, column, and diagonal sums. The result is always at least $1$.

### Examples

**Example 1**

- Input: `grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]`
- Output: `3`
- Explanation: The square with top-left entry `5` has every row, column, and diagonal sum equal to $12$.

**Example 2**

- Input: `grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]`
- Output: `2`

**Example 3**

- Input: `grid = [[1000000]]`
- Output: `1`
- Explanation: A single cell is magic by definition.

### Required Complexity

- **Time:** $O(MNS^2)$
- **Space:** $O(MN)$

<details>
<summary>Approach</summary>

#### General

**Make every line sum cheap.** Build independent prefix tables for rows, columns, diagonals running down and right, and diagonals running down and left. A subtraction in the appropriate table then gives the sum of any complete row segment, column segment, or diagonal segment of a candidate square in constant time.

**Search in answer order.** Try side lengths from $S$ down to $2$. For a chosen side length, enumerate every possible top-left corner. Use one diagonal as the candidate target sum and reject the square immediately if the other diagonal differs. Then inspect all of its row sums and column sums through the prefix tables. If every one equals the target, the square is magic. Because side lengths are examined from largest to smallest, the first accepted square is globally optimal.

If no candidate of side at least $2$ succeeds, return $1$. This fallback is valid because the problem explicitly makes every $1 \times 1$ square magic.

#### Complexity detail

Building the four prefix tables takes $O(MN)$ time and space. For a fixed side length $k$, there are $(M-k+1)(N-k+1)$ positions. Each position needs constant-time diagonal checks and at most $2k$ constant-time row and column queries. Summed over all $1 \le k \le S$, this is $O(MNS^2)$ time in the worst case. The prefix tables occupy $O(MN)$ space.

#### Alternatives and edge cases

- **Direct summation:** Recomputing each candidate's row, column, and diagonal sums from the matrix is simpler, but it adds another factor of $k$ to the expensive validation path.
- **Only row and column prefixes:** Diagonals could still be summed cell by cell, but diagonal prefix tables make all four kinds of line query uniform and allow earlier rejection.
- **Non-distinct entries:** A uniform square is magic; uniqueness is never part of the contract.
- **Rectangular matrices:** Candidate side length is limited by $S = \min(M, N)$, while positions still span both matrix dimensions.
- **Partial equality:** Equal diagonal sums, or equal row sums alone, are insufficient. Every row, every column, and both diagonals must share one sum.
- **Single row or column:** No square larger than one fits, so the answer is immediately $1$.

</details>
