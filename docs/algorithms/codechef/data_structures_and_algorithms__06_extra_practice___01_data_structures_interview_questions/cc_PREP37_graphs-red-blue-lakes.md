# Graphs - Red Blue Lakes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP37 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Graphs |
| Official Link | [PREP37](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_12/problems/PREP37) |

---

## Problem Statement

You are given a matrix $A$ of size $N \times M$.
The height of the cell $(i, j)$ is represented by a non-negative integer $A_{(i, j)}$.

Water can only flow from a cell to an adjacent cell (left, right, up, and down) if the height of the adjacent cell is **equal to or lower** than the current cell.

There is a *red lake* that touches the right and bottom border of the matrix and a *blue lake* that touches the left and top border of the matrix. Both lakes are at **zero** height.

Find the number of cells in the matrix from which water can flow to both *red* and *blue* lakes.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of rows and columns of the matrix, respectively.
    - The next $N$ lines describe the rows. The $i^{th}$ of these $M$ lines contain $M$ space-separated integers, denoting the $i^{th}$ column.

---

## Output Format

For each test case, output on a new line, the number of cells in the matrix from which water can flow to both *red* and *blue* lakes.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N, M \leq 1000$
- $1 \leq A_{(i, j)} \leq 10^9$
- Sum of $N\times M$ over all test cases won't exceed $2\cdot 10^6$.

---

## Examples

**Example 1**

**Input**

```text
3
2 2
1 2
2 1
1 3
7 1 4
2 3
1 2 3
4 5 6
```

**Output**

```text
2
3
4
```

**Explanation**

**Test case $1$:** Water from cells $A_{(1, 2)}$ and $A_{(2, 1)}$ can flow to both *red* and *blue* lakes. These two cells are directly attached to both lakes.

**Test case $2$:** Water from cells $A_{(1, 1)}, A_{(1, 2)}$ and $A_{(1, 3)}$ can flow to both *red* and *blue* lakes. These three cells are directly attached to both lakes.

**Test case $3$:** Water from cells $A_{(1, 3)}, A_{(2, 1)}, A_{(2, 2)}$ and $A_{(2, 3)}$ can flow to both *red* and *blue* lakes.
- $A_{(1, 3)}$: Directly attached to red lake. Possible path to blue lake: $(1, 3) \rightarrow (1, 2) \rightarrow (1, 1) \rightarrow$ *blue lake*.
- $A_{(2, 1)}$: Directly attached to both lakes.
- $A_{(2, 2)}$: Directly attached to red lake. Possible path to blue lake: $(2, 2) \rightarrow (2, 1) \rightarrow$ *blue lake*.
- $A_{(2, 3)}$: Directly attached to red lake. Possible path to blue lake: $(2, 3) \rightarrow (2, 2) \rightarrow (2, 1) \rightarrow$ *blue lake*.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we explore how to solve the water flow problem using multiple algorithmic approaches. The problem asks us to determine the number of cells from which water can flow to both the *red lake* (touching the right and bottom borders) and the *blue lake* (touching the left and top borders). Water can flow from a cell to an adjacent cell if and only if the adjacent cell’s height is less than or equal to the current cell. In our solution, we reverse the flow: we start from the lakes’ border cells and move “uphill” (i.e. to adjacent cells of greater or equal height). This reverse method allows us to mark all cells that can reach the border.

Below, we discuss two distinct approaches:

---

### **Approach 1: Two Separate BFS Traversals**

**Idea:**
We use a multi-source Breadth-First Search (BFS) for each lake separately. For the red lake, we start from all cells on the right and bottom borders. For the blue lake, we start from the left and top borders. During each BFS, a cell is added to the queue if its height is at least as high as the cell from which we arrived. After completing both BFS traversals, we count the cells that are reachable by **both** searches.

**Mathematical note:**
For two cells with heights $h_1$ and $h_2$, the water can flow in reverse if
$$
h_{\text{neighbor}} \ge h_{\text{current}},
$$
which is the condition we use in our BFS.

**Implementation Explanation:**
We maintain two visited matrices (one for each lake). The BFS propagates from the border cells, exploring in all four directions. Finally, we count the number of cells where both visited matrices have been marked true.

**C++ Code:**

```cpp
#include
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	while(T--){
	    int N, M;
	    cin >> N >> M;
	    vector> A(N, vector(M));
	    for (int i = 0; i < N; i++) {
	        for (int j = 0; j < M; j++) {
	            cin >> A[i][j];
	        }
	    }

	    vector> red(N, vector(M, false));
	    vector> blue(N, vector(M, false));

	    queue> qr, qb;

	    // Red lake touches right and bottom borders
	    for (int i = 0; i < N; i++) {
	        int j = M - 1;
	        if (!red[i][j]) {
	            red[i][j] = true;
	            qr.push({i, j});
	        }
	    }
	    for (int j = 0; j < M; j++) {
	        int i = N - 1;
	        if (!red[i][j]) {
	            red[i][j] = true;
	            qr.push({i, j});
	        }
	    }

	    // Blue lake touches left and top borders
	    for (int i = 0; i < N; i++) {
	        int j = 0;
	        if (!blue[i][j]) {
	            blue[i][j] = true;
	            qb.push({i, j});
	        }
	    }
	    for (int j = 0; j < M; j++){
	        int i = 0;
	        if (!blue[i][j]) {
	            blue[i][j] = true;
	            qb.push({i, j});
	        }
	    }

	    int dirs[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

	    // BFS for red reachable cells
	    while(!qr.empty()){
	        auto [r, c] = qr.front();
	        qr.pop();
	        for(auto &d: dirs){
	            int nr = r + d[0], nc = c + d[1];
	            if(nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
	            if(red[nr][nc]) continue;
	            if(A[nr][nc] >= A[r][c]){
	                red[nr][nc] = true;
	                qr.push({nr, nc});
	            }
	        }
	    }

	    // BFS for blue reachable cells
	    while(!qb.empty()){
	        auto [r, c] = qb.front();
	        qb.pop();
	        for(auto &d: dirs){
	            int nr = r + d[0], nc = c + d[1];
	            if(nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
	            if(blue[nr][nc]) continue;
	            if(A[nr][nc] >= A[r][c]){
	                blue[nr][nc] = true;
	                qb.push({nr, nc});
	            }
	        }
	    }

	    int count = 0;
	    for (int i = 0; i < N; i++){
	        for (int j = 0; j < M; j++){
	            if(red[i][j] && blue[i][j])
	                count++;
	        }
	    }
	    cout << count << "\n";
	}

	return 0;
}
```

**Python Code:**

```python
import sys
from collections import deque
input = sys.stdin.readline

def bfs(starts, A, N, M):
    visited = [[False]*M for _ in range(N)]
    dq = deque(starts)
    for i, j in starts:
        visited[i][j] = True
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    while dq:
        i, j = dq.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and A[ni][nj] >= A[i][j]:
                visited[ni][nj] = True
                dq.append((ni, nj))
    return visited

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    red_starts = []
    blue_starts = []
    for i in range(N):
        red_starts.append((i, M-1))
    for j in range(M):
        red_starts.append((N-1, j))
    for i in range(N):
        blue_starts.append((i, 0))
    for j in range(M):
        blue_starts.append((0, j))

    red = bfs(red_starts, A, N, M)
    blue = bfs(blue_starts, A, N, M)
    ans = 0
    for i in range(N):
        for j in range(M):
            if red[i][j] and blue[i][j]:
                ans += 1
    print(ans)
```

---

### **Approach 2: Two Separate DFS Traversals**

**Idea:**
In a similar spirit to our BFS solution, we can perform Depth-First Search (DFS) starting from the borders. For each lake, we initiate DFS from all corresponding border cells (red for the bottom and right; blue for the top and left). The DFS explores “uphill” cells, checking if the next cell’s height is at least as high as the current one.

**Why DFS?**
DFS allows for recursion or an iterative stack-based approach. It might be more natural for those who are comfortable with recursive algorithms. However, careful attention must be paid to the recursion depth when using recursion (especially in Python).

**Implementation Explanation:**
We maintain two visited matrices (one for each lake). We launch DFS from the border cells and mark every reachable cell. In the end, we count the cells that are marked as reachable by both DFS traversals.

**C++ Code:**

```cpp
#include
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	while(T--){
	    int N, M;
	    cin >> N >> M;
	    vector> A(N, vector(M));
	    for(int i = 0; i < N; i++){
	        for(int j = 0; j < M; j++){
	            cin >> A[i][j];
	        }
	    }
	    vector> red(N, vector(M, false));
	    vector> blue(N, vector(M, false));

	    vector> startsRed;
	    vector> startsBlue;
	    // Red lake: right and bottom borders
	    for(int i = 0; i < N; i++){
	        startsRed.push_back({i, M-1});
	    }
	    for(int j = 0; j < M; j++){
	        startsRed.push_back({N-1, j});
	    }
	    // Blue lake: top and left borders
	    for(int i = 0; i < N; i++){
	        startsBlue.push_back({i, 0});
	    }
	    for(int j = 0; j < M; j++){
	        startsBlue.push_back({0, j});
	    }

	    auto dfs = [&](vector>& vis, const vector>& starts) {
	        int dirs[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};
	        stack> st;
	        for(auto &cell : starts){
	            int i = cell.first, j = cell.second;
	            if(!vis[i][j]){
	                vis[i][j] = true;
	                st.push({i, j});
	            }
	        }
	        while(!st.empty()){
	            auto [i, j] = st.top();
	            st.pop();
	            for(auto &d: dirs){
	                int ni = i + d[0], nj = j + d[1];
	                if(ni < 0 || ni >= N || nj < 0 || nj >= M) continue;
	                if(vis[ni][nj]) continue;
	                if(A[ni][nj] >= A[i][j]){
	                    vis[ni][nj] = true;
	                    st.push({ni, nj});
	                }
	            }
	        }
	    };

	    dfs(red, startsRed);
	    dfs(blue, startsBlue);

	    int count = 0;
	    for(int i = 0; i < N; i++){
	        for(int j = 0; j < M; j++){
	            if(red[i][j] && blue[i][j]){
	                count++;
	            }
	        }
	    }
	    cout << count << "\n";
	}

	return 0;
}
```

**Python Code:**

```python
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(starts, A, N, M):
    visited = [[False]*M for _ in range(N)]
    stack = list(starts)
    for i, j in starts:
        visited[i][j] = True
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    while stack:
        i, j = stack.pop()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and A[ni][nj] >= A[i][j]:
                visited[ni][nj] = True
                stack.append((ni, nj))
    return visited

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    red_starts = []
    blue_starts = []
    for i in range(N):
        red_starts.append((i, M-1))
    for j in range(M):
        red_starts.append((N-1, j))
    for i in range(N):
        blue_starts.append((i, 0))
    for j in range(M):
        blue_starts.append((0, j))

    red = dfs(red_starts, A, N, M)
    blue = dfs(blue_starts, A, N, M)

    count = sum(1 for i in range(N) for j in range(M) if red[i][j] and blue[i][j])
    print(count)
```

---

**Conclusion:**
Each approach leverages reverse traversal (moving toward higher or equal heights) to determine whether water can reach the lake boundaries. Approach 1 and Approach 2 use separate traversals (BFS and DFS respectively). Choose the method that best suits your comfort level and the constraints of your environment.

Happy coding!

</details>
