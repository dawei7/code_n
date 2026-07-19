# Stone Game VII

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1690 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/stone-game-vii/) |

## Problem Description
### Goal

Alice and Bob play with a row of $n$ stones whose positive values appear in `stones` from left to right. Alice moves first, and the players alternate turns. A move removes exactly one endpoint: either the current leftmost stone or the current rightmost stone. The moving player then earns the sum of the values that remain in the row, rather than the value of the removed stone.

Play continues until the row is empty. Alice chooses moves to maximize the final difference between her score and Bob's, while Bob chooses moves to minimize that same difference; both play optimally. Return Alice's final score minus Bob's final score. The last removal earns zero points because no stones remain afterward.

### Function Contract
**Inputs**

- `stones`: a list of $n$ positive integers in their left-to-right order, where $2 \le n \le 1000$ and each value is at most $1000$

**Return value**

Alice's score minus Bob's score when both players choose optimally.

### Examples
**Example 1**

- Input: `stones = [5, 3, 1, 4, 2]`
- Output: `6`

Alice can finish with 18 points against Bob's 12. Every turn accounts for the sum after the chosen endpoint has been removed.

**Example 2**

- Input: `stones = [7, 90, 5, 1, 100, 10, 10, 2]`
- Output: `122`

**Example 3**

- Input: `stones = [1, 2]`
- Output: `2`

Alice removes the value `1`, scores the remaining value `2`, and Bob's final removal scores zero.
