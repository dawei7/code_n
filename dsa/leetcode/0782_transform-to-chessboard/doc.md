# Transform to Chessboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 782 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/transform-to-chessboard/) |

## Problem Description

### Goal

Given an $n \times n$ binary matrix `board`, one move may swap any two complete rows or any two complete columns. A chessboard is an arrangement in which every pair of horizontally or vertically adjacent cells contains different values.

Return the minimum number of row and column swaps needed to transform `board` into a chessboard. If no sequence of allowed whole-row and whole-column swaps can produce one, return `-1`. Individual cells cannot be swapped independently, and diagonal equality does not violate the chessboard condition.

### Function Contract

**Inputs**

- `board`: a nonempty $n \times n$ matrix containing only `0` and `1`.

**Return value**

- The minimum number of row and column swaps that transforms `board` into a chessboard, or `-1` if transformation is impossible.

### Examples

**Example 1**

- Input: `board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]`
- Output: `2`
- Explanation: One row swap and one column swap create alternating rows and columns.

**Example 2**

- Input: `board = [[0,1],[1,0]]`
- Output: `0`
- Explanation: The board already has chessboard adjacency.

**Example 3**

- Input: `board = [[1,0],[1,0]]`
- Output: `-1`
- Explanation: Swapping whole rows or columns cannot make the two rows complementary.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Identify the invariant row patterns**

In a chessboard, every row is either identical to the first row or its bitwise complement. Row and column swaps preserve the XOR of the four corners of any rectangle. Anchoring each rectangle at `(0, 0)` gives the necessary condition `board[0][0] ^ board[row][0] ^ board[0][column] ^ board[row][column] = 0`. If it holds everywhere, all rows and columns already have exactly the two complementary pattern types required; only their order may be wrong.

**Check that both pattern counts can alternate**

The first column labels the two row types, and the first row labels the two column types. In either label sequence, the counts of zero and one must be equal for even `n` or differ by one for odd `n`. A larger imbalance cannot be repaired by swapping positions.

**Count swaps for each label sequence**

Compare a label sequence with the alternating target `0,1,0,1,...`. For even `n`, either starting bit is allowed, so use the smaller of this mismatch count and its complement. For odd `n`, the value occurring more often fixes the starting bit; equivalently, choose the even one of the two mismatch counts. Every swap repairs two mismatched positions, so divide the chosen count by two. Row and column swaps are independent, and their minimum counts add.

The rectangle condition and balance checks prove that a valid alternating ordering exists. The mismatch calculation is a lower bound because one swap changes at most two wrong positions, and pairing the wrong positions realizes exactly that many swaps. Consequently the summed row and column counts are both feasible and minimal.

#### Complexity detail

Checking all $n^{2}$ cells dominates the work. The two label sequences each take $O(n)$ additional processing, so total time is $O(n^2)$. Materializing the first-column labels uses $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Bitmask row types:** Encode each row as a bitmask and verify that only one mask and its complement occur; this has the same asymptotic cost but can obscure the count logic.
- **Pairwise row comparisons:** Verify every pair of rows across every column; this is correct but takes $O(n^3)$ time.
- **Search over swaps:** Breadth-first search can find a minimum for very small boards, but row and column permutations make it infeasible at scale.
- **Single cell:** Either bit is already a valid one-cell chessboard, requiring zero moves.
- **Odd side length:** Only the alternating pattern beginning with the majority label is feasible.
- **Invalid rectangle parity:** One failed anchored XOR check is enough to return `-1`.
- **Already alternating:** Both mismatch counts select zero swaps.

</details>
