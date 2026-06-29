# Graphs - Capture Regions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP35 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Graphs |
| Official Link | [PREP35](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_12/problems/PREP35) |

---

## Problem Statement

You are given a matrix $A$ of size $N\times N$ where each element of the matrix is either $O$ or $X$.

An *unclaimed territory* in the matrix is defined as a set of $M$ coordinates $(X_i, Y_i)$ such that:
- $M \ge 1$;
- $1 \le X_i, Y_i \le N$;
- $(X_i, Y_i) \neq (X_j, Y_j)$ if $(i\neq j)$, that is, no two coordinates are equal;
- $A_{(X_i, Y_i)} = O$ for all $(1\le i \le M)$;
- A coordinate $(X_i, Y_i)$ exists in the set iff there is a coordinate $(X_j, Y_j)$ present in the set such that $(X_i, Y_i)$ and $(X_j, Y_j)$ are neighbours. Mathematically, **one** of the following is true:
    - $|X_i - X_j| = 1$ and $|Y_i - Y_j| = 0$
    - $|X_i - X_j| = 0$ and $|Y_i - Y_j| = 1$

An *unclaimed territory* is captured if **no** coordinate of the territory lies on the *boundary of the matrix*.

Once an *unclaimed territory* is captured, all its elements change from $O$ to $X$.
Print the final matrix after all the possible captures are done.

Note that, a matrix of size $N\times N$ has four boundaries, that is, the first row, the first column, the last row, and the last column.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the size of the row.
    - The next $N$ lines describe the matrix. The $i^{th}$ of these $N$ lines contains a string of length $N$ consisting of $O$ and $X$.

---

## Output Format

For each test case, output $N$ lines. The $i^{th}$ of these $N$ lines contains a string of length $N$ consisting of $O$ and $X$ representing the final matrix.

---

## Constraints

- $1 \leq T \leq 500$
- $1 \leq N \leq 1000$
- $A_{(i,j)}$ is either $O$ or $X$.
- The sum of $N$ over all test cases won't exceed $2000$.

---

## Examples

**Example 1**

**Input**

```text
4
3
XXX
XOX
XXX
3
OXO
XOX
OXO
3
XXX
XOO
XXX
4
XXXO
XOOX
XXOX
OOXX
```

**Output**

```text
XXX
XXX
XXX
OXO
XXX
OXO
XXX
XOO
XXX
XXXO
XXXX
XXXX
OOXX
```

**Explanation**

**Test case $1$**: There is only one *unclaimed territory*:
- $\{(2,2)\}$: This is captured as there is only element which does not lie on the boundary of the matrix.

**Test case $2$**: There are $5$ *unclaimed territories*, out of which, only one does not lie on the boundary of the matrix.

**Test case $3$**: There is only one *unclaimed territory*:
- $\{(2,2), (2, 3)\}$: This cannot be captured as the coordinate $(2,3)$ lies on the boundary of the matrix.

**Test case $4$**: There are $3$ *unclaimed territories*, out of which, only one does not lie on the boundary of the matrix.
Thus, only the unclaimed territory $\{(2, 2), (2,3), (3,3)\}$ would be captured.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Surrounded Regions Problem - Capturing Unclaimed Territories

In this lesson, we discuss a problem where you are given a matrix of size $N \times N$, and each cell is either $O$ or $X$. An *unclaimed territory* is defined as a group of adjacent $O$s (adjacency is considered in the four cardinal directions). A region is "captured" if **none** of its cells lie on the boundary of the matrix. The goal is to flip all captured regions from $O$ to $X$.

We will explore two proven approaches to solve this problem:

---

## Approach 1: BFS Flood Fill from the Boundaries

### Idea:
Mark all $O$s that are connected to a boundary $O$. These marked $O$s are considered *safe* since their territory touches the border. We perform a Breadth-First Search (BFS) starting from every boundary $O$ and mark all reachable $O$s as safe. Finally, we flip every $O$ that is not marked safe.

### Explanation:
1. **Initialization:**
   Create a `safe` matrix of the same dimensions filled with `false`.

2. **Boundary Traversal:**
   Scan the first row, last row, first column, and last column. For each cell that is $O$, mark it as safe and add its coordinates into a queue.

3. **BFS Process:**
   While the queue is not empty, pop a cell and check all its neighbors in the four cardinal directions. If a neighbor is $O$ and has not been marked safe, mark it safe and enqueue it.

4. **Flip Unreachable $O$s:**
   Loop through the entire matrix and flip any $O$ that is not marked safe to $X$.

### Code Implementations:

#### C++ (BFS)
```cpp
#include
#include
#include
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector matrix(N);
        for (int i = 0; i < N; i++){
            cin >> matrix[i];
        }

        vector> safe(N, vector(N, false));
        queue> q;

        // Check boundary cells and add safe O's to the queue
        for (int i = 0; i < N; i++){
            if(matrix[i][0]=='O' && !safe[i][0]){
                safe[i][0] = true;
                q.push({i,0});
            }
            if(matrix[i][N-1]=='O' && !safe[i][N-1]){
                safe[i][N-1] = true;
                q.push({i,N-1});
            }
        }
        for (int j = 0; j < N; j++){
            if(matrix[0][j]=='O' && !safe[0][j]){
                safe[0][j] = true;
                q.push({0,j});
            }
            if(matrix[N-1][j]=='O' && !safe[N-1][j]){
                safe[N-1][j] = true;
                q.push({N-1,j});
            }
        }

        // BFS to mark all O's connected to the border as safe
        int dx[4] = {1, -1, 0, 0};
        int dy[4] = {0, 0, 1, -1};
        while(!q.empty()){
            auto p = q.front();
            q.pop();
            int x = p.first, y = p.second;
            for(int k = 0; k < 4; k++){
                int newX = x + dx[k];
                int newY = y + dy[k];
                if(newX >= 0 && newX < N && newY >= 0 && newY < N){
                    if(matrix[newX][newY]=='O' && !safe[newX][newY]){
                        safe[newX][newY] = true;
                        q.push({newX, newY});
                    }
                }
            }
        }

        // Flip all captured territories (O's not marked safe)
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                if(matrix[i][j]=='O' && !safe[i][j])
                    matrix[i][j] = 'X';
            }
        }

        // Print final matrix
        for (int i = 0; i < N; i++){
            cout << matrix[i] << "\n";
        }
    }
    return 0;
}
```

#### Python (BFS)
```python
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    matrix = [list(input().strip()) for _ in range(N)]
    safe = [[False] * N for _ in range(N)]
    dq = deque()

    # Check boundary cells and enqueue safe O's
    for i in range(N):
        if matrix[i][0] == 'O' and not safe[i][0]:
            safe[i][0] = True
            dq.append((i, 0))
        if matrix[i][N-1] == 'O' and not safe[i][N-1]:
            safe[i][N-1] = True
            dq.append((i, N-1))
    for j in range(N):
        if matrix[0][j] == 'O' and not safe[0][j]:
            safe[0][j] = True
            dq.append((0, j))
        if matrix[N-1][j] == 'O' and not safe[N-1][j]:
            safe[N-1][j] = True
            dq.append((N-1, j))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 'O' and not safe[nx][ny]:
                safe[nx][ny] = True
                dq.append((nx, ny))

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'O' and not safe[i][j]:
                matrix[i][j] = 'X'

    for row in matrix:
        print("".join(row))
```

---

## Approach 2: DFS Flood Fill from the Boundaries

### Idea:
This approach is similar to the BFS method, but utilizes Depth-First Search (DFS) to mark safe $O$s. Starting from the boundary $O$s, we traverse using DFS to mark all connected $O$s as safe. We then flip the $O$s that were not reached by the DFS.

### Explanation:
1. **Initialization:**
   Create a `safe` matrix and prepare for DFS using an explicit stack (to avoid recursion limits).

2. **Boundary Traversal:**
   For every boundary cell with $O$, start a DFS and mark all connected $O$s as safe.

3. **Mark Safe Cells via DFS:**
   Use an iterative DFS (stack) to mark connected $O$s.

4. **Flip Unprotected Cells:**
   Finally, flip all $O$s not reached by the DFS.

### Code Implementations:

#### C++ (DFS)
```cpp
#include
#include
#include
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector matrix(N);
        for (int i = 0; i < N; i++){
            cin >> matrix[i];
        }

        vector> safe(N, vector(N, false));

        // Lambda for iterative DFS using a stack
        auto dfs = [&](int i, int j){
            stack> st;
            st.push({i, j});
            safe[i][j] = true;
            int dx[4] = {1, -1, 0, 0};
            int dy[4] = {0, 0, 1, -1};
            while(!st.empty()){
                auto [x, y] = st.top();
                st.pop();
                for (int k = 0; k < 4; k++){
                    int nx = x + dx[k], ny = y + dy[k];
                    if (nx >= 0 && nx < N && ny >= 0 && ny < N){
                        if(matrix[nx][ny]=='O' && !safe[nx][ny]){
                            safe[nx][ny] = true;
                            st.push({nx, ny});
                        }
                    }
                }
            }
        };

        // Start DFS from boundary cells
        for (int i = 0; i < N; i++){
            if(matrix[i][0]=='O' && !safe[i][0])
                dfs(i, 0);
            if(matrix[i][N-1]=='O' && !safe[i][N-1])
                dfs(i, N-1);
        }
        for (int j = 0; j < N; j++){
            if(matrix[0][j]=='O' && !safe[0][j])
                dfs(0, j);
            if(matrix[N-1][j]=='O' && !safe[N-1][j])
                dfs(N-1, j);
        }

        // Flip all captured territories
        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                if(matrix[i][j]=='O' && !safe[i][j])
                    matrix[i][j] = 'X';
            }
        }

        for (auto &row : matrix)
            cout << row << "\n";
    }
    return 0;
}
```

#### Python (DFS)
```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    matrix = [list(input().strip()) for _ in range(N)]
    safe = [[False] * N for _ in range(N)]

    def dfs(i, j):
        stack = [(i, j)]
        safe[i][j] = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 'O' and not safe[nx][ny]:
                    safe[nx][ny] = True
                    stack.append((nx, ny))

    # Start DFS from boundary O's
    for i in range(N):
        if matrix[i][0] == 'O' and not safe[i][0]:
            dfs(i, 0)
        if matrix[i][N-1] == 'O' and not safe[i][N-1]:
            dfs(i, N-1)
    for j in range(N):
        if matrix[0][j] == 'O' and not safe[0][j]:
            dfs(0, j)
        if matrix[N-1][j] == 'O' and not safe[N-1][j]:
            dfs(N-1, j)

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'O' and not safe[i][j]:
                matrix[i][j] = 'X'

    for row in matrix:
        print("".join(row))
```

</details>
