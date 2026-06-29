# The White Knight

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | E1 |
| Difficulty Rating | 1530 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [E1](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/E1) |

---

## Problem Statement

You are given a chessboard of size NxN. There is a white knight and several black pawns located on the board. The knight can move similarly to the normal knight in the game of chess; however it can only move towards the right of the board (see the below figure).

The mission of the knight is to capture as many black pawns as possible. Its journey ends when it moves to the rightmost column of the board.

Compute the maximum number of black pawns the white knight can capture.

### Input

The first line contains t, the number of test cases (about 10). Then t test cases follow.

Each test case has the following form:

- The first line contains N, the size of the chessboard (4 ≤ N ≤ 1000).

- Then N lines follow, each line containing N characters which may be '.', 'K' or 'P', corresponding to the empty cell, the white knight, and the black pawn, respectively. There is exactly one 'K' character in the whole of the board.

### Output

For each test case, print in a single line the maximum number of black pawns that can be captured.

---

## Examples

**Example 1**

**Input**

```text
1
5
K....
..P..
.P...
...P.
.....
```

**Output**

```text
2
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### [](#problem-statement-1)Problem Statement

You are given a chessboard of size N × N. There is a white knight and several black pawns located on the board. The knight can move similarly to the normal knight in the game of chess; however, it can only move towards the right of the board. The mission of the knight is to capture as many black pawns as possible. Its journey ends when it moves to the rightmost column of the board. Compute the maximum number of black pawns the white knight can capture.

### [](#approach-2)Approach

The code uses a recursive function with memoization to compute the maximum number of pawns that the knight can capture starting from its initial position. It checks each valid knight move (`up-left`, `down-left`, `up-right`, and `down-right`) and accumulates the count of pawns captured (`'P'`) while ensuring the knight remains within the grid boundaries. The `dp` table stores previously computed results to optimize performance and avoid redundant calculations.

### [](#time-complexity-3)Time Complexity

The time complexity is O(N^2) because each cell in the N×N grid is processed once.

### [](#space-complexity-4)Space Complexity

The space complexity is O(N^2) due to the `dp` table storing the results for each cell.

</details>
