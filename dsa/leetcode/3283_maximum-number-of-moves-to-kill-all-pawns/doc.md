# Maximum Number of Moves to Kill All Pawns

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3283 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation, Breadth-First Search, Game Theory, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-moves-to-kill-all-pawns](https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/).

### Goal
Given a knight's starting position on a chessboard and a list of target pawns, determine the total number of moves made in a game where Alice and Bob take turns moving the knight. Alice aims to maximize the total number of moves until all pawns are captured, while Bob aims to minimize it. Each turn, the current player moves the knight to capture a remaining pawn, and the game ends when no pawns are left.

### Function Contract
**Inputs**

- `kx`: An integer representing the starting row of the knight.
- `ky`: An integer representing the starting column of the knight.
- `positions`: A list of lists, where each sub-list `[px, py]` represents the coordinates of a pawn.

**Return value**

- An integer representing the total number of moves made in the game assuming optimal play from both sides.

### Examples
**Example 1**

- Input: `kx = 1, ky = 1, positions = [[0, 0]]`
- Output: `4`

**Example 2**

- Input: `kx = 0, ky = 2, positions = [[1, 1], [2, 2], [3, 3]]`
- Output: `8`

**Example 3**

- Input: `kx = 0, ky = 0, positions = [[1, 2], [2, 4]]`
- Output: `3`

---

## Solution
### Approach
The problem is solved using a combination of Breadth-First Search (BFS) to precompute the shortest distance between all pairs of points (start position and all pawns), followed by Minimax with Memoization (Dynamic Programming with Bitmasking) to determine the optimal game outcome.

### Complexity Analysis
- **Time Complexity**: $O(N^2 + 2^N \cdot N^2)$, where $N$ is the number of pawns. The BFS takes $O(N \cdot 50^2)$ and the DP state space is $2^N \cdot N$.
- **Space Complexity**: $O(N^2 + 2^N \cdot N)$ to store the distance matrix and the memoization table.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(kx: int, ky: int, positions: list[list[int]]) -> int:
    n = len(positions)
    all_points = [[kx, ky]] + positions
    num_points = len(all_points)

    def knight_distance(a: list[int], b: list[int]) -> int:
        ax, ay = a
        bx, by = b
        corner_pairs = (
            ((0, 0), (1, 1)),
            ((0, 49), (1, 48)),
            ((49, 0), (48, 1)),
            ((49, 49), (48, 48)),
        )
        endpoints = {(ax, ay), (bx, by)}
        if any(endpoints == {p, q} for p, q in corner_pairs):
            return 4

        dx = abs(ax - bx)
        dy = abs(ay - by)
        if dx < dy:
            dx, dy = dy, dx
        if dx == 0 and dy == 0:
            return 0
        if dx == 1 and dy == 0:
            return 3
        if dx == 2 and dy == 2:
            return 4
        moves = max((dx + 1) // 2, (dx + dy + 2) // 3)
        return moves + ((moves + dx + dy) & 1)

    dist = [[0] * num_points for _ in range(num_points)]
    for i in range(num_points):
        for j in range(num_points):
            dist[i][j] = knight_distance(all_points[i], all_points[j])

    memo = {}

    def get_moves(last_idx, mask, turn):
        state = (last_idx, mask, turn)
        if mask == (1 << n) - 1:
            return 0
        if state in memo:
            return memo[state]

        if turn == 0:  # Alice's turn (Maximize)
            res = -float('inf')
            for i in range(n):
                if not (mask & (1 << i)):
                    res = max(res, dist[last_idx][i + 1] + get_moves(i + 1, mask | (1 << i), 1))
            memo[state] = res
            return res
        else:  # Bob's turn (Minimize)
            res = float('inf')
            for i in range(n):
                if not (mask & (1 << i)):
                    res = min(res, dist[last_idx][i + 1] + get_moves(i + 1, mask | (1 << i), 0))
            memo[state] = res
            return res

    return get_moves(0, 0, 0)
```
</details>
