# Queens That Can Attack the King

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1222 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/queens-that-can-attack-the-king/) |

## Problem Description

### Goal

On an $8\times8$ chessboard, each coordinate is written as `[row, column]`, with both components between `0` and `7`. You are given the distinct coordinates in `queens` occupied by black queens and the coordinate `king` occupied by the white king. No queen shares the king's square.

A queen can attack along its row, column, or either diagonal. However, another queen between it and the king blocks that line of attack.

Return the coordinates of every queen that can directly attack the king. The coordinates may be returned in any order.

### Function Contract

**Inputs**

- `queens`: A list of $q$ distinct queen coordinates, where $1\le q\le63$ and each row and column lies from `0` through `7`.
- `king`: The king's coordinate on an unoccupied square of the same board.

**Return value**

- The coordinates of all queens with an unobstructed row, column, or diagonal attack on the king, in any order.

### Examples

**Example 1**

- Input: `queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]`, `king = [0,0]`
- Output: `[[0,1],[1,0],[3,3]]`

The queens at `[4,0]` and `[0,4]` are blocked by nearer queens on their respective rays.

**Example 2**

- Input: `queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]`, `king = [3,3]`
- Output: `[[2,2],[3,4],[4,4]]`

**Example 3**

- Input: `queens = [[5,6],[7,7],[2,1]]`, `king = [4,5]`
- Output: `[[5,6]]`

### Required Complexity

- **Time:** $O(q)$
- **Space:** $O(q)$

<details>
<summary>Approach</summary>

#### General

**Index occupied squares.** Convert every queen coordinate to a tuple in a hash set. This makes each board-square occupancy test constant expected time and separates lookup order from the input order.

**Scan outward on the eight attack rays.** From the king, step through each of the horizontal, vertical, and diagonal direction vectors. The first occupied square encountered on a ray contains the only queen on that ray that can attack: record it and stop scanning that direction. If the board edge is reached first, that direction contributes nothing.

**Why only the first queen matters.** Every attacking queen must lie on exactly one of the eight rays from the king. On a fixed ray, the nearest queen has no queen between it and the king, so it attacks. Any farther queen has that nearest queen between it and the king and is blocked. Therefore selecting the first occupied square from each ray returns all and only the direct attackers.

#### Complexity detail

Building the occupied set takes $O(q)$ time and space. The eight ray scans examine at most seven squares each on the fixed $8\times8$ board, which is constant additional work, so total time is $O(q)$ and space is $O(q)$.

#### Alternatives and edge cases

- **Check every queen and every blocker:** Classifying each queen's line and scanning all other queens for an intervening piece is correct but takes $O(q^2)$ time.
- **Materialize an $8\times8$ board:** A Boolean board also supports constant-time lookup and uses constant board space, but the coordinate set is more direct.
- **Multiple queens on one ray:** Only the nearest one is returned; every farther queen is blocked.
- **Adjacent queen:** A queen one square from the king attacks immediately because no square can lie between them.
- **No aligned queen:** The result is empty even when many queens occupy other squares.
- **Corner king:** Five directions leave the board immediately; the same direction loop needs no special case.
- **Output order:** Direction order is an implementation detail because the contract permits any order.

</details>
