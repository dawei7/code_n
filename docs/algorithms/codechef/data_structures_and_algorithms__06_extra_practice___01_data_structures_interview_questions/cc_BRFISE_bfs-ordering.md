# BFS Ordering

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BRFISE |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [BRFISE](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_10/problems/BRFISE) |

---

## Problem Statement

You are given an undirected connected graph with $N$ nodes and $M$ edges. You are also given a node $X$.

A sequence in which all the nodes of a graph appear exactly once is called a **BFS ordering** if and only the breadth first search algorithm starting from the node $X$ can output it as a result.

You need to print the lexicographically minimal **BFS ordering** of the given graph that starts from the node $X$.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains three space-separated integers $N$, $M$ and $X$.

- $M$ lines follow. The $i$-th of these lines contains two space-separated integers $u_i$ and $v_i$ denoting an edge of the graph.

---

## Output Format

- For each test case, print a single line.

- In that line, print $N$ space-separated integers ― the lexicographically minimal **BFS ordering** of the given graph.

---

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 2 \cdot 10^5$
- $N-1 \leq M \leq min(2 \cdot 10^5, (N \cdot (N-1))/2)$
- $1 \le X \le N$
- $1 \le u_i,v_i \le N$ for each valid $i$
- $u_i \neq v_i$ for each valid $i$
- For each pair of nodes there is at most one edge that connects them directly
- The undirected graph described on the input is guaranteed to be connected
- The sum of $N$ over all test cases does not exceed $4 \cdot 10^5$
- The sum of $M$ over all test cases does not exceed $4 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
5 5 2
4 2
1 3
2 1
3 4
2 5
5 7 5
1 2
2 5
5 4
2 4
1 4
1 3
3 4
```

**Output**

```text
2 1 4 5 3
5 2 4 1 3
```

**Explanation**

**Example case 1:** The given sequence is a **BFS ordering** because the breadth first search algorithm can indeed start from the node $X=2$, visit its adjacent nodes $1$, $4$ and $5$, and finally visit the node $3$ which is the farthest away from $X=2$. Note that this is the only correct answer. For example, sequences $2,1,5,4,3$ and $2,5,1,4,3$ are **BFS orderings** as well, but they are not lexicographically minimal.

**Example case 2:** The given sequence is a **BFS ordering** because the breadth first search algorithm can indeed start from the node $X=5$, visit its adjacent nodes $2$ and $4$, and finally visit nodes $1$ and $3$. Moreover, it is lexicographically minimal.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 5 2
4 2
1 3
2 1
3 4
2 5
5 7 5
```

**Output for this case**

```text
2 1 4 5 3
```



#### Test case 2

**Input for this case**

```text
1 2
2 5
5 4
2 4
1 4
1 3
3 4
```

**Output for this case**

```text
5 2 4 1 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Lexicographically Minimal BFS Ordering

In this lesson, we study how to determine the lexicographically minimal BFS (Breadth First Search) ordering of an undirected connected graph. A BFS ordering is a sequence in which every node appears exactly once and the sequence can be produced by a BFS traversal starting from a given node $X$. Among all possible BFS orderings, we are asked to output the one that is lexicographically smallest.

Recall that in a lexicographical comparison, two sequences are compared element by element, and the first point of difference determines the ordering. To ensure that our BFS ordering is minimal, we need to make sure that when several nodes are available to be visited, we choose the smallest one first.

Below, we discuss a robust approach to solve this problem.

## Approach: Standard BFS with Pre-sorted Neighbors

The idea behind this approach is to perform a standard BFS using a FIFO queue while ensuring that the neighbors of each node are processed in increasing order. To achieve this, we pre-sort the adjacency list for every vertex before starting the BFS. Then, when processing a vertex, we iterate over its neighbor list (which is already sorted) and enqueue any unvisited neighbor.

Since the graph is connected and the BFS processes vertices level by level, the lexicographical minimality is maintained by processing nodes in sorted order whenever there is a choice.

### Explanation:

1. **Preprocessing:**
   For every vertex $v$, sort its list of adjacent nodes. This guarantees that when examining the neighbors, you always consider the smallest available vertex first.

2. **BFS Traversal:**
   - Start from the given node $X$, mark it as visited, and push it into a queue.
   - While the queue is not empty, dequeue a vertex.
   - For each unvisited neighbor (which is already sorted), mark it as visited and enqueue it.
   - Print (or store) the node as soon as it is dequeued.

3. **Result:**
   The output sequence is a valid BFS ordering with lexicographical order maintained among nodes of the same level.

### C++ Code:

```cpp
#include
#include
#include
#include
using namespace std;

const int MAX_N = 200005;
vector adj[MAX_N];
bool visited[MAX_N];

void bfs(int start, int N) {
    queue q;
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        cout << curr << " ";

        // Gather unvisited neighbors
        vector neighbors;
        for (int next : adj[curr]) {
            if (!visited[next]) {
                visited[next] = true;
                neighbors.push_back(next);
            }
        }
        // Process neighbors in increasing order
        sort(neighbors.begin(), neighbors.end());
        for (int next : neighbors) {
            q.push(next);
        }
    }
    cout << "\n";
}

void solve() {
    int N, M, X;
    cin >> N >> M >> X;

    for (int i = 1; i <= N; i++) {
        adj[i].clear();
        visited[i] = false;
    }

    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Pre-sort the adjacency lists
    for (int i = 1; i <= N; i++) {
        sort(adj[i].begin(), adj[i].end());
    }

    bfs(X, N);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        solve();
    }

    return 0;
}
```

### Python Code:

```python
from collections import deque
import sys

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    out_lines = []
    for _ in range(T):
        N = int(next(it)); M = int(next(it)); X = int(next(it))
        # Build the graph
        adj = [[] for _ in range(N + 1)]
        for _ in range(M):
            u = int(next(it)); v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)
        # Pre-sort each vertex's neighbor list
        for i in range(1, N + 1):
            adj[i].sort()

        visited = [False] * (N + 1)
        q = deque([X])
        visited[X] = True
        res = []

        while q:
            curr = q.popleft()
            res.append(curr)
            temp = []
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    temp.append(neighbor)
            # Ensure neighbors are added in lexicographical order
            temp.sort()
            for node in temp:
                q.append(node)

        out_lines.append(" ".join(map(str, res)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
```

## Summary

This approach guarantees that the output is a valid BFS ordering and is lexicographically minimal due to the pre-sorting of neighbors before enqueuing them. The method is both efficient and straightforward, making it a robust solution for problems involving lexicographically minimal BFS traversal.

Happy Coding!

</details>
