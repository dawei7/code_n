
## Solution

---

### Approach: Shortest Path + Dijkstra

#### Intuition

This problem is an extended version of [3341. Find Minimum Time to Reach Last Room I](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/). The key difference is that the time required for each move alternate: the first move takes 1 second, the second move takes 2 seconds, the third move takes 1 second, and so on.

Since the movement occurs on a two-dimensional grid, each move changes the coordinates $(i, j)$ by exactly 1 in one of the four directions. As a result, the parity of $(i + j)$ changes with every move. This allows us to determine the move's parity directly based on the current coordinates.

Let $d[i][j]$ represent the shortest time required to reach $(i, j)$ from $(0, 0)$. Then, the time to move from $(i, j)$ to an adjacent cell $(u, v)$ is given by:

$\max(d[i][j], \textit{moveTime}[u][v]) + (i + j) \bmod 2 + 1.$

Additionally, since reaching $(n - 1, m - 1)$ is guaranteed, we can optimize the algorithm by checking within the main loop whether the current point is $(n - 1, m - 1)$. If it is, we can exit early to avoid unnecessary computations for other cells.

#### Implementation

```python
class State:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis

    def __lt__(self, other):
        return self.dis < other.dis

class Solution:
    def minTimeToReach(self, moveTime):
        n = len(moveTime)
        m = len(moveTime[0])
        inf = float("inf")
        d = [[inf] * m for _ in range(n)]
        v = [[0] * m for _ in range(n)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        d[0][0] = 0
        q = []
        heapq.heappush(q, State(0, 0, 0))

        while q:
            s = heapq.heappop(q)
            if v[s.x][s.y]:
                continue
            if s.x == n - 1 and s.y == m - 1:
                break
            v[s.x][s.y] = 1
            for dx, dy in dirs:
                nx, ny = s.x + dx, s.y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                dist = max(d[s.x][s.y], moveTime[nx][ny]) + (s.x + s.y) % 2 + 1
                if d[nx][ny] > dist:
                    d[nx][ny] = dist
                    heapq.heappush(q, State(nx, ny, dist))

        return d[n - 1][m - 1]
```

#### Complexity Analysis

Let $n$ and $m$ be the number of rows and columns in $\textit{moveTime}$, respectively.

- Time complexity: $O(nm \log(nm))$.

There are $nm$ points and $O(nm)$ edges. We implement Dijkstra's algorithm using a min-heap, performing at most $O(nm)$ insertions and deletions. Since each heap operation takes $O(\log(nm))$ time, the overall time complexity is $O(nm \log(nm))$.

- Space complexity: $O(nm)$.