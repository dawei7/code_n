# Parallel World

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INC_HEIGHTS |
| Difficulty Rating | 1700 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [INC_HEIGHTS](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_09/problems/INC_HEIGHTS) |

---

## Problem Statement

You are currently in a parallel world. There are two unique things about this world.
First is that you have a speed of infinite, i.e. you can reach from location $X$ to another location $Y$ in $0$ unit time if it is possible to reach location $Y$ from location $X$.
Second is that at the time $t$ heights of all locations having $heights \lt t$, increases by $1$, whereas the heights of other location remain unchanged.
The parallel world is represented by a 2D-matrix $A$ of size $N*N$. You are currently located at $(0,0)$ and you want to reach $(n-1,n-1)$ location (so that you can return to the normal world). You can move from one square to another only if they share a side and the height of both the squares is equal. Find the minimum amount of time required for you to reach from $(0,0)$ to $(n-1,n-1)$.
Initially the time $t = 0$.

---

## Input Format

- The first line contains an integer $T$, representing $T$ test cases.

- The first line of each test case contains an integer $N$.

- Next $N$ line contains $N$ integer, representing $A_{i,j}$ ( $j'th$ character in $i'th$ line)

---

## Output Format

- For each test case, print a single integer representing the time required.

---

## Constraints

- $1 \le T \le100$

- $2 \le N \le 500$

- $0 \le A_{i,j} \lt N*N$

- All element in 2-D matrix $A$ are distinct

- Sum of $N*N$ overall test cases doesn’t exceed $2*10^6$

---

## Examples

**Example 1**

**Input**

```text
2
2
0 2
1 3
3
6 0 7
8 5 4
3 2 1
```

**Output**

```text
3
6
```

**Explanation**

Possible path for test case $1$ are $\{0,2,3\}$ or $\{0,1,3\}$ (Elements of matrix $A$ are indicated)

Path for test case $2$ is $\{6,0,5,2,1\}$

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Minimum Time to Reach Destination in a Parallel World

In this problem, we are given a $N \times N$ matrix where each cell represents a height. You start at cell $(0,0)$ and need to reach cell $(n-1,n-1)$ in minimum time. The twist is that time is indirectly tied to the heights: at time $t$, any cell whose height is less than $t$ becomes accessible. The challenge is to find a path from the start to the destination such that the maximum height encountered along the path is minimized. In other words, we need to find the minimum $T$ such that water has risen enough to cover every cell along a valid path.

We will discuss **two approaches** that can solve this problem.

---

## Approach 1: Dijkstra / Best-First Search

**Idea:**
We use a priority queue (min-heap) to simulate a modified Dijkstra’s algorithm. The "cost" to reach a cell is defined as the maximum height encountered so far along the path from $(0,0)$ to that cell. At every step, we explore the neighbor with the smallest “cost.” When we finally reach $(n-1,n-1)$, the cost will be the minimum required time.

**Key Steps:**
- Start from $(0,0)$, and push the initial cell (with its height) into a min-heap.
- For each cell popped from the heap, explore its four adjacent cells.
- For each neighbor, update the cost as $ \max(\text{current cost}, \text{neighbor's height}) $.
- Once the destination is reached, that cost is the answer.

### C++ Implementation:
```cpp
#include
#include
#include
#include
using namespace std;

const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

int solve(vector>& grid) {
    int n = grid.size();
    vector> visited(n, vector(n, false));
    priority_queue>, vector>>, greater>>> pq;

    pq.push({grid[0][0], {0, 0}});
    visited[0][0] = true;

    while (!pq.empty()) {
        int height = pq.top().first;
        int x = pq.top().second.first;
        int y = pq.top().second.second;
        pq.pop();

        if (x == n - 1 && y == n - 1)
            return height;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                visited[nx][ny] = true;
                pq.push({max(height, grid[nx][ny]), {nx, ny}});
            }
        }
    }

    return -1;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector> grid(n, vector(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> grid[i][j];
            }
        }

        cout << solve(grid) << endl;
    }

    return 0;
}
```

### Python Implementation:
```python
import heapq

def solve(grid):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    heap = [(grid[0][0], 0, 0)]
    visited[0][0] = True

    while heap:
        t, x, y = heapq.heappop(heap)
        if x == n - 1 and y == n - 1:
            return t
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                heapq.heappush(heap, (max(t, grid[nx][ny]), nx, ny))
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(solve(grid))
```

---

## Approach 2: Union-Find / Disjoint Set

**Idea:**
This approach simulates the rising water by processing the cells in increasing order of height. We convert each cell into a tuple $(\text{height}, x, y)$, sort all these cells, and then use a Union-Find data structure to unify adjacent cells as soon as they become accessible. Once the start $(0,0)$ and the destination $(n-1,n-1)$ are connected, the current height is the minimum required time.

**Key Steps:**
- Create a list of cells with their height and coordinates. Sort this list.
- Use a Union-Find (Disjoint Set) to union adjacent cells that are accessible.
- Check if the start and destination are in the same set; if so, output the current cell's height.

### C++ Implementation:
```cpp
#include
#include
#include
#include
using namespace std;

struct UF {
    vector parent;
    UF(int n) : parent(n) {
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }
    int find(int x) {
        return parent[x] = (parent[x] == x ? x : find(parent[x]));
    }
    void unionn(int x, int y) {
        x = find(x);
        y = find(y);
        if (x < y)
            parent[y] = x;
        else
            parent[x] = y;
    }
};

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector> grid(n, vector(n));
        vector> cells;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> grid[i][j];
                cells.push_back({grid[i][j], i, j});
            }
        }

        sort(cells.begin(), cells.end());
        UF uf(n * n);
        vector> seen(n, vector(n, false));
        int ans = 0;
        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, -1, 1};

        for (auto &[h, x, y] : cells) {
            seen[x][y] = true;
            int id = x * n + y;
            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && seen[nx][ny]) {
                    int nid = nx * n + ny;
                    uf.unionn(id, nid);
                }
            }
            if (uf.find(0) == uf.find(n * n - 1)) {
                ans = h;
                break;
            }
        }
        cout << ans << endl;
    }

    return 0;
}
```

### Python Implementation:
```python
def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    rx, ry = find(x, parent), find(y, parent)
    if rx < ry:
        parent[ry] = rx
    else:
        parent[rx] = ry

t = int(input())
for _ in range(t):
    n = int(input())
    grid = []
    cells = []
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
        for j in range(n):
            cells.append((row[j], i, j))
    cells.sort()
    parent = [i for i in range(n * n)]
    seen = [[False] * n for _ in range(n)]
    ans = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for h, x, y in cells:
        seen[x][y] = True
        id = x * n + y
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and seen[nx][ny]:
                union(id, nx * n + ny, parent)
        if find(0, parent) == find(n * n - 1, parent):
            ans = h
            break
    print(ans)
```

</details>
