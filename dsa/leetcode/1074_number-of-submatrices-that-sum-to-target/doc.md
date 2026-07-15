# Number of Submatrices That Sum to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1074 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/) |

## Problem Description

### Goal

Given an integer `matrix` and an integer `target`, count the non-empty rectangular submatrices whose cell values sum exactly to `target`.

A submatrix is determined by inclusive row boundaries `x1` and `x2` and inclusive column boundaries `y1` and `y2`; it contains every `matrix[x][y]` with $x1 \le x \le x2$ and $y1 \le y \le y2$. Two submatrices are distinct whenever at least one of their four boundary coordinates differs, even if their values or sums are identical.

### Function Contract

**Inputs**

- `matrix`: an $R \times C$ integer matrix, where $1 \le R,C \le 100$ and $-1000 \le \texttt{matrix[i][j]} \le 1000$.
- `target`: an integer satisfying $-10^8 \le \texttt{target} \le 10^8$.
- Let $S=\min(R,C)$ and $L=\max(R,C)$.

**Return value**

- The number of non-empty submatrices having sum exactly `target`.

### Examples

**Example 1**

- Input: `matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]], target = 0`
- Output: `4`
- Explanation: The four zero-valued cells are four distinct `1 x 1` submatrices.

**Example 2**

- Input: `matrix = [[1, -1], [-1, 1]], target = 0`
- Output: `5`
- Explanation: Two full rows, two full columns, and the whole matrix have sum zero.

**Example 3**

- Input: `matrix = [[904]], target = 0`
- Output: `0`

### Required Complexity

- **Time:** $O(S^2L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Square the smaller dimension:** Treat the smaller matrix dimension as the boundary-pair dimension. If rows are no more numerous than columns, pair top and bottom rows and compress columns. Otherwise, pair left and right columns and compress rows. Direct orientation-aware indexing avoids allocating a transposed matrix.

**Compress between two boundaries:** Fix the first boundary and initialize an array of $L$ zeros. As the second boundary advances, add its cells into that array. Each entry then stores the sum along the fixed span for one position in the larger dimension.

**Count one-dimensional target sums:** A contiguous range of the compressed array corresponds exactly to one submatrix with the chosen small-dimension boundaries. Scan its prefix sums with a frequency map. When the running sum is $p$, every earlier prefix equal to $p-\texttt{target}$ defines a range summing to `target`.

Every boundary pair and compressed contiguous range maps to one unique rectangle, so counted ranges are valid and distinct. Conversely, every rectangle has one pair of boundaries in the smaller dimension and one contiguous range in the larger dimension, so it is considered exactly once.

#### Complexity detail

There are $O(S^2)$ boundary pairs. Updating and scanning the compressed array costs $O(L)$ for each pair, giving $O(S^2L)$ time. The compressed sums and prefix-frequency map each contain at most $O(L)$ entries, so auxiliary space is $O(L)$.

#### Alternatives and edge cases

- **Enumerate four boundaries:** A 2D prefix table makes each rectangle sum constant-time, but there are $O(R^2C^2)$ rectangles.
- **Always pair rows:** It is correct but costs $O(R^2C)$ and can be much worse than pairing columns for a tall matrix.
- **Materialize a transpose:** It simplifies orientation logic but adds $O(RC)$ auxiliary space.
- **Negative values:** Sliding-window methods are invalid because extending a range does not change its sum monotonically; prefix frequencies remain correct.
- **All-zero matrix with zero target:** Every non-empty rectangle qualifies.
- **Single row or column:** The method reduces directly to ordinary subarray-sum counting.
- **Equal sums at different boundaries:** Each coordinate tuple is a distinct submatrix and is counted separately.

</details>
