# Cells with Odd Values in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1252 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/) |

## Problem Description

### Goal

Begin with an $m \times n$ matrix whose entries are all zero. Each operation in `indices` is a pair `[r, c]`: increment every cell in row `r` by one, then increment every cell in column `c` by one. The intersection cell receives both increments.

Apply all operations in their given order and return the number of matrix cells containing an odd value afterward. Repeated row or column indices represent repeated increments and must each affect the final parity.

### Function Contract

**Inputs**

- `m`: the row count, with $1 \le m \le 50$.
- `n`: the column count, with $1 \le n \le 50$.
- `indices`: a list of $k$ valid `[r, c]` operations, where $1 \le k \le 100$, $0 \le r < m$, and $0 \le c < n$.

**Return value**

- Return the number of cells whose final value is odd.

### Examples

**Example 1**

- Input: `m = 2`, `n = 3`, `indices = [[0, 1], [1, 1]]`
- Output: `6`

**Example 2**

- Input: `m = 2`, `n = 2`, `indices = [[1, 1], [0, 0]]`
- Output: `0`

**Example 3**

- Input: `m = 1`, `n = 1`, `indices = [[0, 0]]`
- Output: `0`
- Explanation: The sole cell is incremented once through its row and once through its column, ending at the even value `2`.

### Required Complexity

- **Time:** $O(m+n+k)$
- **Space:** $O(m+n)$

<details>
<summary>Approach</summary>

#### General

Only the parity of each increment count matters. Maintain one bit for every row and every column. For operation `[r, c]`, toggle the bit for row `r` and the bit for column `c`; toggling is equivalent to adding one modulo two.

**Deriving a cell's parity**

Cell `(r, c)` receives every increment applied to row `r` and every increment applied to column `c`. Its final parity is therefore the exclusive-or of those two parity bits. The cell is odd exactly when one bit is odd and the other is even. The double increment at an operation's intersection is handled automatically because two toggles cancel modulo two.

**Counting without constructing the matrix**

Let $R$ be the number of rows with odd parity and $C$ the number of columns with odd parity. An odd row paired with an even column contributes $R(n-C)$ odd cells. An even row paired with an odd column contributes $(m-R)C$ more. These groups are disjoint and cover every odd cell, so return $R(n-C)+(m-R)C$.

#### Complexity detail

Toggling the $k$ operations takes $O(k)$ time, and counting the row and column bits takes $O(m+n)$ time. The two parity arrays occupy $O(m+n)$ auxiliary space.

#### Alternatives and edge cases

- **Direct matrix simulation:** Incrementing every affected cell follows the statement literally but costs $O(k(m+n)+mn)$ time and $O(mn)$ space.
- **Sets of odd rows and columns:** Adding or removing each index from a set also tracks parity and uses space proportional to the currently odd indices.
- **Repeated operation:** Applying the same pair twice restores both associated parity bits and has no net parity effect.
- **Single cell:** Every operation increments its row and column, so the cell always receives an even total.
- **All row and column bits equal:** When both sides have the same parity everywhere, no cell is odd.

</details>
