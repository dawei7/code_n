# Count Square Submatrices with All Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1277 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) |

## Problem Description

### Goal

Given a rectangular binary matrix, count all square submatrices whose cells are entirely `1`. Squares of every possible side length contribute separately, and overlapping squares are each counted at their own position.

For example, an all-ones $2 \times 2$ region contributes its four individual cells as side-one squares and the whole region as one side-two square. Return the total across the complete matrix.

### Function Contract

**Inputs**

- `matrix`: an $m \times n$ matrix whose entries are either `0` or `1`, where $1 \le m,n \le 300$.

**Return value**

- Return the number of axis-aligned square submatrices containing only `1` values.

### Examples

**Example 1**

- Input: `matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]`
- Output: `15`

**Example 2**

- Input: `matrix = [[1,0,1],[1,1,0],[1,1,0]]`
- Output: `7`

**Example 3**

- Input: `matrix = [[1]]`
- Output: `1`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

For each cell containing `1`, determine the largest all-ones square whose bottom-right corner is that cell. A side-one square always exists there. A larger square can extend only as far as the squares ending immediately above, immediately left, and diagonally above-left all permit. Therefore its side length is one plus the minimum of those three values.

Every all-ones square ending at a cell is a suffix of the largest one there: if the largest side length is $k$, that endpoint contributes exactly one square of each side from $1$ through $k$. Adding the computed side length to the answer therefore counts every square once, at its unique bottom-right corner.

Store the previous row's values in a one-dimensional array. While scanning the current row left to right, the array entry at the current column is still the value from above, the preceding entry has already become the value from the left, and a saved value carries the old above-left entry. A matrix `0` resets the current entry to zero because no all-ones square can end there.

#### Complexity detail

Each of the $mn$ cells performs constant work, so the time complexity is $O(mn)$. The dynamic-programming row has $n+1$ entries and the remaining state is constant, giving $O(n)$ auxiliary space without modifying the input matrix.

#### Alternatives and edge cases

- **Update the input matrix in place:** It implements the same recurrence with $O(1)$ auxiliary space, but it destroys the caller's matrix.
- **Full two-dimensional dynamic programming:** It is straightforward and also takes $O(mn)$ time, but stores $O(mn)$ values when only one previous row is needed.
- **Prefix sums plus every candidate square:** A prefix sum checks a chosen square in constant time, yet enumerating every side length at every position requires $O(mn\min(m,n))$ time.
- **All zeros:** Every dynamic-programming value remains zero and the answer is `0`.
- **Single row or column:** Only side-one squares are possible, so the answer equals the number of ones.
- **Overlapping squares:** Each has a distinct top-left or bottom-right placement and must be counted separately.

</details>
