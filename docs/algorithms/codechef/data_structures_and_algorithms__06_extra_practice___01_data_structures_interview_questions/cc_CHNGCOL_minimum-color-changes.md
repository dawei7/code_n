# Minimum Color Changes 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHNGCOL |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [CHNGCOL](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_09/problems/CHNGCOL) |

---

## Problem Statement

We have a square matrix of size $N \times N$, each cell is colored either white or black. You have to go from $(1 , 1)$ to $(N , N)$ by traveling on a cell with only one color, for the same you can change the color of some cells. From a cell you can go in all four directions (up, left, down and right). More formally, from cell $(i , j)$ you can go to cell $(i-1 , j)$, $(i , j-1)$, $(i+1 , j)$ and $(i , j+1)$.

You have to find out a minimum number of changes required so that you can reach $(N , N)$ from $(1 , 1)$.

---

## Input Format

- The first line of input contains $2$ integers $N$ - number of columns and rows in the matrix.
- Next $N$ lines each contain $N$ space separated integers where $j^{th}$ integer in $i^{th}$ line denotes color of cell $(i,j)$, $1$ means black and $0$ means white.

---

## Output Format

Output a single integer - minimum number of color changes required.

---

## Constraints

- $2 \leq N \leq 500$

---

## Examples

**Example 1**

**Input**

```text
2
0 1
1 1
```

**Output**

```text
1
```

**Explanation**

- Case 1 : Choose white (0) as path color then one of the best paths would be $(1,1) \rightarrow (1,2) \rightarrow (2,2)$
Number of changes = 2 for changing color of cell $(1,2)$ and $(2,2)$.
- Case 2 : Choose black (1) as path color then one of the best paths would be  $(1,1) \rightarrow (1,2) \rightarrow (2,2)$
Number of changes = 1 for changing color of cell $(1,1)$.

Among both the cases minimum number of changes = 1

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial

In this problem, we are given a square matrix of size $N \times N$, where each cell is either white ($0$) or black ($1$). We need to travel from cell $(1,1)$ to cell $(N,N)$ by moving only in four directions (up, down, left, right). The twist is that the entire connected path must have the same color. If a cell encountered does not have the chosen color for the path, we have to change its color at the cost of $1$. Our goal is to minimize the number of color changes required.

Since there are only two possible colors, we can solve the problem by considering both possibilities:
- **Case 1:** Use white ($0$) as the path color.
- **Case 2:** Use black ($1$) as the path color.

For each case, we compute the minimum cost (i.e., the number of changes) needed to construct a valid path from $(1,1)$ to $(N,N)$ and then choose the optimum result.

Below is the **correct approach** used in this solution:

---

## Approach: 0-1 BFS Using Deque

### Explanation
Since the cost to change a cell's color is either $0$ (if the cell already matches the target color) or $1$ (if it needs to be changed), we deal with a graph where the edge weights are $0$ or $1$. In such cases, the **0-1 BFS** algorithm is ideal because it efficiently processes nodes in order of increasing cost. Here, for a given target color (either $0$ or $1$), we use a deque (double-ended queue) to perform the BFS. When a neighboring cell has the desired color, it incurs no extra cost and is added to the front of the deque. Otherwise, if a change is required, the cell is added to the back of the deque. After processing all reachable cells, we obtain the minimum cost to reach the bottom-right cell, $(N,N)$. We then choose the minimum result among the two possible target colors.

### C++ Implementation
```cpp
#include
#include
#include
#include
using namespace std;

const int INF = 1e9;

int zeroOneBFS(int N, const vector> &matrix, int targetColor) {
    vector> cost(N, vector(N, INF));
    deque> dq;
    int initialCost = (matrix[0][0] == targetColor) ? 0 : 1;
    cost[0][0] = initialCost;
    dq.push_back({0, 0});

    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, -1, 0, 1};

    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
            int add = (matrix[nx][ny] == targetColor) ? 0 : 1;
            int newCost = cost[x][y] + add;
            if (newCost < cost[nx][ny]) {
                cost[nx][ny] = newCost;
                if (add == 0)
                    dq.push_front({nx, ny});
                else
                    dq.push_back({nx, ny});
            }
        }
    }
    return cost[N-1][N-1];
}

int main(){
    int N;
    cin >> N;
    vector> matrix(N, vector(N));
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> matrix[i][j];

    int result0 = zeroOneBFS(N, matrix, 0);
    int result1 = zeroOneBFS(N, matrix, 1);
    cout << min(result0, result1) << endl;
    return 0;
}
```

### Python Implementation
```python
import sys
from collections import deque

def zero_one_bfs(N, matrix, target):
    INF = 10**9
    cost = [[INF] * N for _ in range(N)]
    dq = deque()
    initial_cost = 0 if matrix[0][0] == target else 1
    cost[0][0] = initial_cost
    dq.append((0, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                add = 0 if matrix[nx][ny] == target else 1
                new_cost = cost[x][y] + add
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    if add == 0:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))
    return cost[N-1][N-1]

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    matrix = []
    idx = 1
    for _ in range(N):
        row = list(map(int, data[idx:idx+N]))
        matrix.append(row)
        idx += N
    result0 = zero_one_bfs(N, matrix, 0)
    result1 = zero_one_bfs(N, matrix, 1)
    print(min(result0, result1))

if __name__ == '__main__':
    main()
```

---

**Summary:**

- This solution employs the **0-1 BFS** algorithm using a deque, which is well-suited for scenarios where edge weights can only be $0$ or $1$.
- The algorithm is run for both target colors ($0$ and $1$) and the minimum number of changes required to form a valid path is determined.
- This approach provides an optimal solution for grid-based shortest path problems where selective cell modifications are allowed.

</details>
