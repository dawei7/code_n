# Trees - Height of a Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP66 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [PREP66](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_07/problems/PREP66) |

---

## Problem Statement

You are given a [tree](https://en.wikipedia.org/wiki/Tree_(graph_theory)) with $N$ nodes. The root of the tree is node $1$.

Find the *height* of the tree.

The *height* of the tree is defined as the number of nodes along the longest path from the root node down to a leaf node.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ — the number of nodes.
    - The next $(N-1)$ lines describe the edges. The $i^{th}$ of these lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge **from** $u_i$ **to** $v_i$.

---

## Output Format

For each test case, output on a new line the *height* of the tree

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^5$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \lt N$.
- Sum of $N$ over all test cases does not exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
1 2
1 3
4
1 2
1 3
2 4
6
1 2
1 3
2 4
2 5
3 6
```

**Output**

```text
2
3
3
```

**Explanation**

**Test case $1$:** One of the longest paths from root node to leaf node is $1\rightarrow 2$. Since there are $2$ nodes in the path, the height of the tree is $2$.

**Test case $2$:** The longest path from root node to leaf node is $1\rightarrow 2\rightarrow 4$. Since there are $3$ nodes in the path, the height of the tree is $3$.

**Test case $3$:** One of the longest paths from root node to leaf node is $1\rightarrow 3\rightarrow 6$. Since there are $3$ nodes in the path, the height of the tree is $3$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Editorial for "Height of Tree" Problem

### Problem Recap

In this problem, you are given a tree with $N$ nodes where the root is node $1$. The goal is to compute the **height** of the tree, which is defined as the number of nodes along the longest path from the root to any leaf node. Since the tree is represented using $N-1$ edges, every node (except the root) is connected through one edge, forming an acyclic graph.

### Approaches to the Problem

We discuss two primary approaches to solve this problem:

1. **Depth First Search (DFS) Approach:**
   In the DFS approach, we recursively traverse the tree from the root, keeping track of the current depth. Each recursive call adds $1$ to the current depth, and when we reach a leaf node (a node with no unvisited children), the current depth represents the length (in terms of nodes) of the path from the root. We update a global maximum depth during the traversal so that by the end, we have the height of the tree.
   **Time Complexity:** $$O(N)$$ per test case.
   **Space Complexity:** $$O(N)$$ due to the recursion stack and the graph storage.

2. **Breadth First Search (BFS) Approach:**
   In the BFS approach, we perform a level order traversal using a queue. Starting from the root, we explore all nodes at the current level before moving to the next level. Each new level increments the depth count. This approach fits naturally with the definition of tree height as it directly counts levels.
   **Time Complexity:** $$O(N)$$ per test case.
   **Space Complexity:** $$O(N)$$ for storing the queue and the graph.

Both approaches work efficiently under the given constraints. While DFS is intuitive with recursion, BFS provides an iterative alternative that is easy to understand in terms of levels.

### Code Implementation

Below are the implementations in both C++ and Python for each approach. In the C++ solutions, please adhere to the provided template structure.

---

#### Approach 1: DFS

**C++ (DFS Approach):**

```cpp
#include
using namespace std;

void dfs(int node, int parent, vector>& adj, int currDepth, int &maxDepth) {
    maxDepth = max(maxDepth, currDepth);
    for (int child : adj[node]) {
        if (child != parent) {
            dfs(child, node, adj, currDepth + 1, maxDepth);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector> adj(N + 1);
        for (int i = 0; i < N - 1; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        int maxDepth = 0;
        dfs(1, 0, adj, 1, maxDepth);
        cout << maxDepth << "\n";
    }

    return 0;
}
```

**Python (DFS Approach):**

```python
def dfs(node, parent, depth, adj):
    max_depth = depth
    for child in adj[node]:
        if child != parent:
            max_depth = max(max_depth, dfs(child, node, depth + 1, adj))
    return max_depth

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        adj = [[] for _ in range(n+1)]
        for i in range(n - 1):
            u = int(data[index])
            v = int(data[index+1])
            index += 2
            adj[u].append(v)
            adj[v].append(u)
        height = dfs(1, 0, 1, adj)
        results.append(str(height))

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
```

---

#### Approach 2: BFS

**C++ (BFS Approach):**

```cpp
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector> adj(N + 1);
        for (int i = 0; i < N - 1; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        vector visited(N + 1, false);
        queue> q;
        q.push({1, 1});
        visited[1] = true;
        int maxDepth = 0;

        while (!q.empty()) {
            auto [node, depth] = q.front();
            q.pop();
            maxDepth = max(maxDepth, depth);
            for (int child : adj[node]) {
                if (!visited[child]) {
                    visited[child] = true;
                    q.push({child, depth + 1});
                }
            }
        }

        cout << maxDepth << "\n";
    }

    return 0;
}
```

**Python (BFS Approach):**

```python
from collections import deque

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        adj = [[] for _ in range(n+1)]
        for i in range(n - 1):
            u = int(data[index])
            v = int(data[index+1])
            index += 2
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * (n + 1)
        q = deque([(1, 1)])
        visited[1] = True
        max_depth = 0
        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)
            for child in adj[node]:
                if not visited[child]:
                    visited[child] = True
                    q.append((child, depth + 1))
        results.append(str(max_depth))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
```

### Conclusion

Both the DFS and BFS approaches efficiently compute the height of the tree in $$O(N)$$ time. The DFS approach leverages recursion to naturally explore each branch, while the BFS approach uses a queue for level order traversal. Understanding these strategies will improve your problem-solving skills and equip you to handle similar tree traversal challenges in interviews.

Happy Coding!

</details>
