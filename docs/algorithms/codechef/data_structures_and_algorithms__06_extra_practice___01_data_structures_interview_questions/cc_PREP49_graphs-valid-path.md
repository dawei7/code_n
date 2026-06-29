# Graphs - Valid Path

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP49 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Graphs |
| Official Link | [PREP49](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_12/problems/PREP49) |

---

## Problem Statement

There is a rectangle with the left top cell as $(0, 0)$ and the right bottom cell as $(N_x, N_y)$. There are $M$ circles such that their centers are inside the rectangle where the center of $i^{th}$ circle will be $(X_i, Y_i)$ and the radius of each circle will be $R$.

Find if it is possible that we can move from $(0, 0)$ to $(N_x, N_y)$ without touching any circle.

Note:
- We can move to any adjacent cell which shares a side or corner with its current cell. That means if you are at the cell $(i,j)$ of the grid, you can go to either of the cells $(i + 1, j)$, $(i - 1, j)$, $(i, j + 1)$, $(i, j - 1)$, $(i + 1, j + 1)$, $(i + 1, j - 1)$, $(i - 1, j + 1)$, $(i - 1, j - 1)$ if that inside the rectangle.
- A circle doesn't touch a cell $(i,j)$ if the [Euclidian distance](https://en.wikipedia.org/wiki/Euclidean_distance#Two_dimensions) from its center to $(i,j)$ is greater than $R$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N_x$, $N_y$.
    - The second line contains two space-separated integers $M$, $R$ — the number of circles, radius of each circle.
    - The third line contains $M$ space separated integers $X_1, X_2, \ldots X_M$ — the $X$-coordinate of circles.
    - The fourth line contains $M$ space separated integers $Y_1, Y_2, \ldots Y_M$ — the $Y$-coordinate of circles.

---

## Output Format

For each test case, output $1$ if it is possible that we can move from $(0, 0)$ to $(N_x, N_y)$ without touching any circle otherwise output $0$.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N_x, N_y, M \leq 100$
- $0 \leq X_i \leq N_x$
- $0 \leq Y_i \leq N_y$

---

## Examples

**Example 1**

**Input**

```text
2
2 3
1 1
2
0
2 3
2 2
0 1
3 2
```

**Output**

```text
1
0
```

**Explanation**

**Test case $1$:** We can reach $(2, 3)$ using path $(0, 0) \rightarrow (0, 1) \rightarrow (0, 2) \rightarrow (0, 3) \rightarrow (1, 3) \rightarrow (2, 3)$.

**Test case $2$:** There is no path present.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 3
1 1
2
0
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 3
2 2
0 1
3 2
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial

In this problem, we are given a rectangle with grid coordinates starting at $(0,0)$ and ending at $(N_x,N_y)$. Additionally, there are $M$ circles inside the rectangle with centers at $(X_i,Y_i)$ and each having a radius $R$. A cell $(x,y)$ in the grid is considered unsafe (or "touched by a circle") if the Euclidean distance from the cell to any circle’s center satisfies
$$
(x - X_i)^2 + (y - Y_i)^2 \le R^2.
$$
Our goal is to determine whether it is possible to travel from the starting cell $(0,0)$ to the target cell $(N_x,N_y)$ without entering any unsafe cell. Note that you can move from a cell to any of its $8$ neighbors (including diagonals).

Below, we discuss two well‐known approaches to solve this problem.

---

## Approaches to the Problem

### Approach 1: BFS without Precomputation of the Grid

In this approach, we directly perform a **Breadth-First Search (BFS)** on the grid. At each step, before adding a neighboring cell to our queue, we check if the cell is safe by iterating over all of the circles and verifying the condition:
$$
(x - X_i)^2 + (y - Y_i)^2 > R^2.
$$

**Steps Explained:**
1. **Starting Cell Check:** First, we check if the starting cell $(0,0)$ is safe. If it is touched by a circle, we cannot even begin, so we return 0.
2. **BFS Traversal:** From the current cell, we try moving to all 8 possible adjacent cells. For each neighbor:
   - Ensure it lies within the rectangle bounds.
   - Check that the cell is not visited.
   - Confirm that it does not lie within the danger zone of any circle.
3. **Termination:** If we reach $(N_x,N_y)$, we immediately return 1; otherwise, if all possible cells are exhausted, return 0.

This approach has an advantage of being simple to implement without additional memory overhead for precomputation because safety is checked on the fly.

---

### Approach 2: Precomputation of the Grid then BFS

Given that the grid size is relatively small (maximum of about $101 \times 101$ cells), we can precompute a **safe grid**. In this grid, each cell is marked as safe or unsafe by checking the condition
$$
(x - X_i)^2 + (y - Y_i)^2 \le R^2
$$
for every circle.

**Steps Explained:**
1. **Precompute the Safety Grid:**
   - For every cell $(i,j)$ in the rectangle, iterate over all circles.
   - If any circle satisfies the unsafe condition, mark the cell as unsafe.
2. **BFS Traversal:**
   - Once the grid is precomputed, you only need to check the safety status of a cell (a constant time lookup) while performing a standard BFS.
   - Start from $(0,0)$—if it’s unsafe, return 0 immediately.
   - Try moving in all 8 directions, and if a neighbor is safe and within bounds, proceed with the BFS.
3. **Termination:**
   - If $(N_x,N_y)$ is reached, return 1; otherwise, return 0 if no path exists.

This approach separates the costly safety-check from the traversal and may be conceptually easier to understand since the grid’s status is precomputed.

---

## Code Implementation

Below are the complete implementations for both approaches in **C++** and **Python**. The C++ solutions strictly follow the provided template.

---

### Approach 1: BFS without Precomputation

#### C++ Code
```cpp
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--){
        int Nx, Ny;
        cin >> Nx >> Ny;
        int M, R;
        cin >> M >> R;
        vector circleX(M), circleY(M);
        for (int i = 0; i < M; i++){
            cin >> circleX[i];
        }
        for (int i = 0; i < M; i++){
            cin >> circleY[i];
        }

        auto isBlocked = [&](int x, int y) -> bool {
            for (int i = 0; i < M; i++){
                long long dx = x - circleX[i];
                long long dy = y - circleY[i];
                if(dx * dx + dy * dy <= (long long) R * R)
                    return true;
            }
            return false;
        };

        vector> visited(Nx + 1, vector(Ny + 1, false));

        if(isBlocked(0, 0)){
            cout << 0 << "\n";
            continue;
        }

        queue> q;
        q.push({0, 0});
        visited[0][0] = true;
        bool found = false;

        while(!q.empty()){
            auto [x, y] = q.front();
            q.pop();

            if(x == Nx && y == Ny){
                found = true;
                break;
            }

            for(int dx = -1; dx <= 1; dx++){
                for(int dy = -1; dy <= 1; dy++){
                    if(dx == 0 && dy == 0)
                        continue;
                    int nx = x + dx, ny = y + dy;
                    if(nx >= 0 && nx <= Nx && ny >= 0 && ny <= Ny && !visited[nx][ny]){
                        if(!isBlocked(nx, ny)){
                            visited[nx][ny] = true;
                            q.push({nx, ny});
                        }
                    }
                }
            }
        }

        cout << (found ? 1 : 0) << "\n";
    }

    return 0;
}
```

#### Python Code
```python
from collections import deque
import sys

def is_blocked(x, y, circles, R):
    for cx, cy in circles:
        if (x - cx)**2 + (y - cy)**2 <= R*R:
            return True
    return False

def bfs(Nx, Ny, circles, R):
    if is_blocked(0, 0, circles, R):
        return False
    visited = [[False] * (Ny + 1) for _ in range(Nx + 1)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        if x == Nx and y == Ny:
            return True
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx <= Nx and 0 <= ny <= Ny and not visited[nx][ny]:
                    if not is_blocked(nx, ny, circles, R):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
    return False

data = sys.stdin.read().split()
if not data:
    exit()
index = 0
T = int(data[index])
index += 1
results = []
for _ in range(T):
    Nx = int(data[index]); Ny = int(data[index+1]); index += 2
    M = int(data[index]); R = int(data[index+1]); index += 2
    circleX = list(map(int, data[index:index+M])); index += M
    circleY = list(map(int, data[index:index+M])); index += M
    circles = list(zip(circleX, circleY))
    result = 1 if bfs(Nx, Ny, circles, R) else 0
    results.append(str(result))
sys.stdout.write("\n".join(results))
```

---

### Approach 2: Precomputation of the Grid then BFS

#### C++ Code
```cpp
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--){
        int Nx, Ny;
        cin >> Nx >> Ny;
        int M, R;
        cin >> M >> R;
        vector circleX(M), circleY(M);
        for (int i = 0; i < M; i++){
            cin >> circleX[i];
        }
        for (int i = 0; i < M; i++){
            cin >> circleY[i];
        }

        // Precompute safe grid:
        vector> safe(Nx + 1, vector(Ny + 1, true));
        for (int i = 0; i <= Nx; i++){
            for (int j = 0; j <= Ny; j++){
                for (int k = 0; k < M; k++){
                    long long dx = i - circleX[k];
                    long long dy = j - circleY[k];
                    if(dx * dx + dy * dy <= (long long) R * R){
                        safe[i][j] = false;
                        break;
                    }
                }
            }
        }

        if(!safe[0][0]){
            cout << 0 << "\n";
            continue;
        }

        vector> visited(Nx + 1, vector(Ny + 1, false));
        queue> q;
        q.push({0, 0});
        visited[0][0] = true;
        bool found = false;

        int directions[8][2] = { {-1,-1}, {-1,0}, {-1,1},
                                 {0,-1},          {0,1},
                                 {1,-1},  {1,0},  {1,1} };

        while(!q.empty()){
            auto [x, y] = q.front();
            q.pop();

            if(x == Nx && y == Ny){
                found = true;
                break;
            }

            for(auto &dir: directions){
                int nx = x + dir[0], ny = y + dir[1];
                if(nx >= 0 && nx <= Nx && ny >= 0 && ny <= Ny &&
                   !visited[nx][ny] && safe[nx][ny]){
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            }
        }

        cout << (found ? 1 : 0) << "\n";
    }

    return 0;
}
```

#### Python Code
```python
import sys
from collections import deque

data = sys.stdin.read().split()
if not data:
    exit()
index = 0
T = int(data[index])
index += 1
results = []
for _ in range(T):
    Nx = int(data[index]); Ny = int(data[index+1]); index += 2
    M = int(data[index]); R = int(data[index+1]); index += 2
    circleX = list(map(int, data[index:index+M])); index += M
    circleY = list(map(int, data[index:index+M])); index += M
    safe = [[True] * (Ny + 1) for _ in range(Nx + 1)]

    for i in range(Nx + 1):
        for j in range(Ny + 1):
            for k in range(M):
                if (i - circleX[k])**2 + (j - circleY[k])**2 <= R*R:
                    safe[i][j] = False
                    break

    if not safe[0][0]:
        results.append("0")
        continue

    visited = [[False] * (Ny + 1) for _ in range(Nx + 1)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    found = False
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while queue:
        x, y = queue.popleft()
        if x == Nx and y == Ny:
            found = True
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= Nx and 0 <= ny <= Ny and not visited[nx][ny] and safe[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    results.append("1" if found else "0")
sys.stdout.write("\n".join(results))
```

Both approaches use the key observation of checking the condition
$$
(x - X_i)^2 + (y - Y_i)^2 \le R^2
$$
to determine if a cell is within any circle. You may choose either approach based on your preference. The BFS without precomputation checks safety on the fly, while the precomputation method first builds a grid of safe cells and may be easier to debug for beginners.

Happy coding and best of luck with your DSA interviews!

</details>
