# Number of Paths with Max Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1301 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-paths-with-max-score](https://leetcode.com/problems/number-of-paths-with-max-score/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-paths-with-max-score/).

### Goal
On a square board, move from `S` at the bottom-right to `E` at the top-left using up, left, or diagonal up-left moves. Avoid obstacles and maximize the sum of digit cells visited. Return the maximum score and the number of maximum-score paths.

### Function Contract
**Inputs**

- `board`: list of strings containing digits, `S`, `E`, and obstacles `X`.

**Return value**

`[maxScore, pathCount]`, modulo `1_000_000_007` for the path count. Return `[0,0]` if no path exists.

### Examples
**Example 1**

- Input: `board = ["E23","2X2","12S"]`
- Output: `[7,1]`

**Example 2**

- Input: `board = ["E12","1X1","21S"]`
- Output: `[4,2]`

**Example 3**

- Input: `board = ["E11","XXX","11S"]`
- Output: `[0,0]`

---

## Solution
### Approach
Grid dynamic programming with score/count pairs.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n^2)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(board):
    mod = 1_000_000_007
    n = len(board)
    score = [[-1] * n for _ in range(n)]
    ways = [[0] * n for _ in range(n)]
    score[n - 1][n - 1] = 0
    ways[n - 1][n - 1] = 1

    for r in range(n - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            if board[r][c] == "X" or (r == n - 1 and c == n - 1):
                continue
            best = -1
            count = 0
            for nr, nc in ((r + 1, c), (r, c + 1), (r + 1, c + 1)):
                if nr < n and nc < n and score[nr][nc] >= 0:
                    if score[nr][nc] > best:
                        best = score[nr][nc]
                        count = ways[nr][nc]
                    elif score[nr][nc] == best:
                        count = (count + ways[nr][nc]) % mod
            if best >= 0:
                value = 0 if board[r][c] == "E" else int(board[r][c])
                score[r][c] = best + value
                ways[r][c] = count

    if ways[0][0] == 0:
        return [0, 0]
    return [score[0][0], ways[0][0] % mod]
```
</details>
