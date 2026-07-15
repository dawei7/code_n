# Maximum Number of Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1183 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-ones/) |

## Problem Description

### Goal

Consider a binary matrix `M` with `height` rows and `width` columns. Every cell is either `0` or `1`. Its entries may be chosen freely, except that every contiguous square submatrix with dimensions `sideLength * sideLength` must contain at most `maxOnes` cells whose value is `1`.

Determine the maximum possible number of ones in the entire matrix while satisfying that restriction simultaneously for every such square. Only the maximum count is required; the matrix itself does not need to be returned.

### Function Contract

**Inputs**

- `width`: The number of matrix columns, with $1\le\texttt{width}\le100$.
- `height`: The number of matrix rows, with $1\le\texttt{height}\le100$.
- `sideLength`: The side length $s$ of every constrained square, where $1\le s\le\min(\texttt{width},\texttt{height})$.
- `maxOnes`: The inclusive limit on ones in each constrained square, where $0\le\texttt{maxOnes}\le s^2$.

**Return value**

- The greatest total number of `1` cells achievable in the full `height * width` matrix without any `sideLength * sideLength` submatrix exceeding `maxOnes` ones.

### Examples

**Example 1**

- Input: `width = 3`, `height = 3`, `sideLength = 2`, `maxOnes = 1`
- Output: `4`

One optimal matrix places ones at its four corners. Every `2 * 2` submatrix then contains exactly one of them.

**Example 2**

- Input: `width = 3`, `height = 3`, `sideLength = 2`, `maxOnes = 2`
- Output: `6`

For example, the first and third columns can be filled with ones while the middle column remains zero.

### Required Complexity

- **Time:** $O(s^2\log s)$
- **Space:** $O(s^2)$

<details>
<summary>Approach</summary>

#### General

**View the matrix through an $s$-periodic tile.** Every contiguous `sideLength * sideLength` square contains exactly one cell from each coordinate residue pair `(row % sideLength, column % sideLength)`. Therefore, selecting at most `maxOnes` residue pairs and setting every full-matrix cell in those classes to `1` automatically respects every square's limit.

**Measure the value of each residue pair.** A row residue `r` occurs once at `r`, again at `r + sideLength`, and so on while the row remains inside the matrix. Compute the analogous number of occurrences for each column residue. Their product is the number of full-matrix cells contributed by selecting that pair. This multiplication also handles partial tiles along the bottom and right edges, where early residues can occur more often.

**Take the most profitable classes.** The local constraint treats all residue pairs equally—at most `maxOnes` may be selected—but their contributions to the whole matrix differ. Sorting their frequencies and summing the largest `maxOnes` is thus the greedy optimum. The periodic construction realizes that sum, while the square constraint prevents extracting more total benefit than choosing that many most frequent equivalence classes.

#### Complexity detail

There are $s^2$ residue pairs. Computing their frequencies takes $O(s^2)$ time, and sorting them takes $O(s^2\log(s^2))=O(s^2\log s)$ time. The frequency list occupies $O(s^2)$ space. The matrix dimensions affect only constant-time arithmetic for each residue; no full matrix is constructed.

#### Alternatives and edge cases

- **Count every matrix cell by residue:** Iterating over all `height * width` cells and incrementing its residue frequency is correct, but it costs $O(\texttt{height}\cdot\texttt{width}+s^2\log s)$ time instead of deriving each frequency directly.
- **Maximum heap:** Put all $s^2$ frequencies in a heap and extract `maxOnes` values. This costs $O(s^2+\texttt{maxOnes}\log(s^2))$ time and can be useful when `maxOnes` is small.
- **Zero allowed ones:** When `maxOnes == 0`, every cell must be zero and the answer is `0`.
- **All residue classes allowed:** When `maxOnes == sideLength * sideLength`, every matrix cell may be one, so the answer is `height * width`.
- **Partial boundary tiles:** Residue classes need not have equal frequencies when a dimension is not divisible by `sideLength`; choosing arbitrary classes can therefore be suboptimal.
- **Side length one:** There is one residue class. The result is either `0` or the full matrix area according to `maxOnes`.

</details>
