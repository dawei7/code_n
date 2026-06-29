# Trees - Branch Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP29 |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [PREP29](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/PREP29) |

---

## Problem Statement

You are given a [binary tree](https://en.wikipedia.org/wiki/Binary_tree) with $N$ nodes where the $i^{th}$ node has a value $V_i$ associated to it. The root of the tree is node $1$.
Note that $V_i$ is a single digit from $0$ to $9$.

A *branch* is defined as a path from the root node to a leaf node. The *value* of a branch is calculated by appending the values of each node lying in the path (from root to leaf).
For example, if the nodes $1,2,$ and $3$ have values $1, 0,$ and $2$ respectively, then, the path $1\rightarrow 2\rightarrow 3$ has the value $102$, while the path $2\rightarrow 1\rightarrow 3$ has the value $012$ or $12$ (leading zeroes are insignificant).

Find the sum of the *values* of all the branches in the tree. Since the answer can be huge, print it modulo $10^9+7$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ — the number of nodes.
    - The next line contains $N$ space-separated integers - the array $V$.
    - The next $(N-1)$ lines describe the edges. The $i^{th}$ of these lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge **from** $u_i$ **to** $v_i$.

---

## Output Format

For each test case, output on a new line, the sum of the *values* of all the branches in the tree. Since the answer can be huge, print it modulo $10^9+7$.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^5$
- $0 \leq V_i \leq 9$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \lt N$.
- Sum of $N$ over all test cases does not exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
9 3
1 2
4
0 3 9 5
1 3
3 4
3 2
3
9 0 2
1 2
1 3
```

**Output**

```text
93
188
182
```

**Explanation**

**Test case $1$:** The tree looks like $1 \rightarrow 2$. Thus, there is only $1$ branch $1\rightarrow 2$. The value of the branch would be $93$.

**Test case $2$:** The tree has $2$ branches:
- $1\rightarrow 3\rightarrow 4$: Value of this branch is $95$.
- $1\rightarrow 3\rightarrow 2$: Value of this branch is $93$.

The sum of values is $95+93 = 188$.

**Test case $3$:** The tree has $2$ branches:
- $1\rightarrow 2$: Value of this branch is $90$.
- $1\rightarrow 3$: Value of this branch is $92$.

The sum of values is $90+92 = 182$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
9 3
1 2
4
```

**Output for this case**

```text
93
```



#### Test case 2

**Input for this case**

```text
0 3 9 5
1 3
3 4
3 2
```

**Output for this case**

```text
188
```



#### Test case 3

**Input for this case**

```text
3
9 0 2
1 2
1 3
```

**Output for this case**

```text
182
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we explore the problem of calculating the sum of branch values in a tree. Each branch is defined as a path from the root to a leaf, and its value is obtained by concatenating the single‐digit values of each node along that path. For example, a branch consisting of nodes with values 1, 0, and 2 represents the number 102.

The key observation is that if you are at a node with a current branch value of
$${\text{current}}$$
and the node’s value is
$${V_i}$$,
then the branch value is updated as:
$$
\text{current}' = (\text{current} \times 10 + V_i) \mod (10^9+7).
$$
At each leaf node (a node with no unexplored children), we add the computed branch value to our answer.

Below, we discuss two common approaches to solve this problem.

---

### Approaches to the Problem

1. **DFS Recursive Approach**

   In this approach, we use Depth-First Search (DFS) recursively starting from the root node (node 1). At each recursive call, we pass along the current branch value which is updated using the formula:

   $$
   \text{current} = (\text{current} \times 10 + V[\text{node}]) \mod (10^9+7).
   $$

   When the function reaches a leaf node (i.e. a node with no child other than its parent), the accumulated branch value is added to a global sum. This approach is intuitive and directly applies the definition of branch value, with a time complexity of $O(N)$ per test case.

2. **BFS Iterative Approach**

   Alternatively, we can use Breadth-First Search (BFS) with an iterative method. In this approach, a queue is used to perform a level-order traversal. Each element in the queue consists of the node, its parent (to avoid backtracking), and the current branch value. For every node dequeued, we update the branch value for its children in a manner similar to the DFS approach. If a node has no child except its parent, it is a leaf and its branch value is added to the answer.

   This iterative method is just as efficient, with a similar time complexity of $O(N)$, and it avoids recursion depth issues that might occur with very deep trees.

---

### Code Implementation

Below are the implementations for both the DFS Recursive Approach and the BFS Iterative Approach in C++ and Python. Each implementation follows the code template provided.

---

#### DFS Recursive Approach

**C++ Code (DFS Recursive):**
```cpp
#include
using namespace std;

const int MOD = 1e9 + 7;

void dfs(int node, int parent, long long current, vector& values, vector>& adj, long long &ans) {
    // Update the current branch value modulo MOD.
    current = (current * 10 + values[node]) % MOD;
    bool isLeaf = true;
    for (int child : adj[node]) {
        if (child != parent) {
            isLeaf = false;
            dfs(child, node, current, values, adj, ans);
        }
    }
    if (isLeaf) {
        ans = (ans + current) % MOD;
    }
}

int main() {
	// your code goes here
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector values(N+1);
        // Read node values; nodes are 1-indexed.
        for (int i = 1; i <= N; i++) {
            cin >> values[i];
        }
        vector> adj(N+1);
        // Build the tree in form of an adjacency list.
        for (int i = 0; i < N - 1; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        long long ans = 0;
        dfs(1, 0, 0, values, adj, ans);
        cout << ans << "\n";
    }
    return 0;
}
```

**Python Code (DFS Recursive):**
```python
#cook your code here
import sys
sys.setrecursionlimit(300000)
MOD = 10**9 + 7

def dfs(node, parent, current, values, adj, ans):
    # Update the current branch value using the given formula.
    current = (current * 10 + values[node]) % MOD
    isLeaf = True
    for child in adj[node]:
        if child != parent:
            isLeaf = False
            dfs(child, node, current, values, adj, ans)
    if isLeaf:
        ans[0] = (ans[0] + current) % MOD

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        # Read values and adjust indexing (1-indexed).
        vals = list(map(int, input().split()))
        values = [0] + vals
        adj = [[] for _ in range(N+1)]
        for _ in range(N-1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ans = [0]
        dfs(1, 0, 0, values, adj, ans)
        print(ans[0])

if __name__ == "__main__":
    main()
```

---

#### BFS Iterative Approach

**C++ Code (BFS Iterative):**
```cpp
#include
using namespace std;

const int MOD = 1e9 + 7;

int main() {
	// your code goes here
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector values(N+1);
        for (int i = 1; i <= N; i++) {
            cin >> values[i];
        }
        vector> adj(N+1);
        for (int i = 0; i < N - 1; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        long long ans = 0;
        // The queue holds a tuple of (node, parent, current branch value).
        queue> q;
        q.push({1, 0, 0});

        while (!q.empty()) {
            auto [node, parent, current] = q.front();
            q.pop();
            current = (current * 10 + values[node]) % MOD;
            bool isLeaf = true;
            for (int child : adj[node]) {
                if (child != parent) {
                    isLeaf = false;
                    q.push({child, node, current});
                }
            }
            if (isLeaf) {
                ans = (ans + current) % MOD;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
```

**Python Code (BFS Iterative):**
```python
#cook your code here
import sys
from collections import deque
MOD = 10**9 + 7

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        vals = list(map(int, input().split()))
        values = [0] + vals  # 1-indexed list of values.
        adj = [[] for _ in range(N+1)]
        for _ in range(N-1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ans = 0
        # Queue stores (node, parent, current branch value).
        q = deque()
        q.append((1, 0, 0))
        while q:
            node, parent, current = q.popleft()
            current = (current * 10 + values[node]) % MOD
            isLeaf = True
            for child in adj[node]:
                if child != parent:
                    isLeaf = False
                    q.append((child, node, current))
            if isLeaf:
                ans = (ans + current) % MOD
        print(ans)

if __name__ == "__main__":
    main()
```

---

### Conclusion

Both the DFS Recursive and the BFS Iterative approaches traverse each node exactly once, resulting in a linear time complexity of $O(N)$ per test case. Understanding these traversal techniques is fundamental for efficiently solving tree-related problems. Choose the approach that best suits your style or constraints; for most cases, the recursive DFS solution is more intuitive, while the BFS iterative solution avoids potential recursion depth issues.

</details>
