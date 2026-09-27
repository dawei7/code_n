# Guided Example: Number of Provinces

We trace the step-by-step undirected adjacency matrix interpretation ($isConnected[i][j] == 1$), connected component discovery, recursive depth-first search graph traversal ($dfs(i)$), boolean visited set marking ($vis[i]$), and global province count enumeration on representative city networks:

- **Input:**
  $$
  isConnected = \begin{bmatrix}
  1 & 1 & 0 \\
  1 & 1 & 0 \\
  0 & 0 & 1
  \end{bmatrix}
  $$
- **Required output:** `2`
  - Number of cities: $n = 3$ (labeled $0, 1, 2$)
  - Province definition: An equivalence class of cities connected directly or transitively through mutual roads (i.e. a **connected component** of an undirected graph).
  - Graph edges:
    - City $0$ is connected to City $1$ ($isConnected[0][1] = 1, isConnected[1][0] = 1$).
    - City $2$ has no external connections ($isConnected[2][j] = 0$ for $j \ne 2$).
- **Connected Component DFS execution trace:**
  - Initialize visited array of size 3:
    $$
    vis = [\text{False}, \; \text{False}, \; \text{False}]
    $$
  - Initialize province counter: $ans = 0$.
  - **Outer Loop Step 1 ($i = 0$):**
    - City $0$ has not been visited ($vis[0] == \text{False}$).
    - Found a new province! Increment counter:
      $$
      ans \leftarrow 0 + 1 = \mathbf{1}
      $$
    - Launch $dfs(0)$ to mark all cities connected to City $0$:
      - Mark $vis[0] \leftarrow \text{True}$.
      - Inspect row $isConnected[0] = [1, 1, 0]$:
        - $j = 0$: Already visited ($vis[0] == \text{True}$).
        - $j = 1$: Road exists ($isConnected[0][1] == 1$) and unvisited ($vis[1] == \text{False}$).
          - Launch recursive call $dfs(1)$:
            - Mark $vis[1] \leftarrow \text{True}$.
            - Inspect row $isConnected[1] = [1, 1, 0]$:
              - $j = 0$: Already visited.
              - $j = 1$: Already visited.
              - $j = 2$: No road ($isConnected[1][2] == 0$).
            - $dfs(1)$ completes and returns.
        - $j = 2$: No road ($isConnected[0][2] == 0$).
      - $dfs(0)$ completes and returns.
    - Visited state after exploring province 1:
      $$
      vis = [\mathbf{\text{True}}, \; \mathbf{\text{True}}, \; \text{False}]
      $$
  - **Outer Loop Step 2 ($i = 1$):**
    - City $1$ is already visited ($vis[1] == \text{True}$).
    - Belongs to an already counted province $\implies$ **Skip!**
  - **Outer Loop Step 3 ($i = 2$):**
    - City $2$ has not been visited ($vis[2] == \text{False}$).
    - Found another distinct province! Increment counter:
      $$
      ans \leftarrow 1 + 1 = \mathbf{2}
      $$
    - Launch $dfs(2)$:
      - Mark $vis[2] \leftarrow \text{True}$.
      - Inspect row $isConnected[2] = [0, 0, 1]$:
        - Neighbors $j \in \{0, 1\}$ have no connections.
      - $dfs(2)$ completes.
    - Visited state:
      $$
      vis = [\text{True}, \; \text{True}, \; \mathbf{\text{True}}]
      $$
  - All $n = 3$ cities examined.
  - Final province count: **`2`** (Component A: $\{0, 1\}$, Component B: $\{2\}$).
- **Fully Disconnected Cities ($isConnected = \text{Identity Matrix } I_n$):**
  - No edges between any cities $\implies n$ isolated single-city provinces $\implies \mathbf{n}$.
- **Fully Connected Network (All 1s):**
  - First DFS from city 0 visits all $n$ cities $\implies \mathbf{1}$.

This instance demonstrates connected component partition in undirected graphs, mathematically proves why visited tracking guarantees that each connected component increments the answer exactly once, and derives $O(N^2)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ matrix $isConnected$ where $isConnected[i][j] = 1$ if city $i$ and city $j$ are directly connected:
A **province** is a group of directly or indirectly connected cities.
Find the **total number of provinces**.

```text
Adjacency Matrix:
     0  1  2
  0 [1, 1, 0]
  1 [1, 1, 0]
  2 [0, 0, 1]

Graph Representation:
  City 0 <---> City 1      City 2 (isolated)
       (Province 1)           (Province 2)

Total Provinces = 2
```

### Equivalence Class Reduction
- The "connected" relation on cities is:
  1. Reflexive ($isConnected[i][i] = 1$).
  2. Symmetric ($isConnected[i][j] == isConnected[j][i]$).
  3. Transitive (if $i \leftrightarrow j$ and $j \leftrightarrow k$, then $i \leftrightarrow k$).
- An equivalence relation partitions a set into disjoint **equivalence classes** (connected components).
- Counting provinces is equivalent to counting the number of connected components in an undirected graph.

---

## 2. Conceptual Foundation & Invariants

### 1. The Visited State Array:
- Maintain array $vis$ of length $n$, initialized to `False`.
- $vis[i] = \text{True}$ indicates that city $i$ has already been absorbed into a discovered province.

### 2. Connected Component Exploration $dfs(i)$:
- Mark $vis[i] = \text{True}$.
- For each city $j \in [0, n - 1]$:
  If $isConnected[i][j] == 1$ and $vis[j]$ is `False`:
  Recurse: $dfs(j)$.

### 3. Outer Discovery Loop:
Initialize $ans = 0$.
For $i \in [0, n - 1]$:
- If $vis[i]$ is `False`:
  1. We have discovered a new connected component:
     $$
     ans \leftarrow ans + 1
     $$
  2. Run $dfs(i)$ to mark all nodes belonging to this component.
Return $ans$.

> **Component Invariant.** Every time an unvisited node $i$ is encountered in the outer loop, it represents the root of a previously undiscovered connected component.

---

## 3. Step-by-Step Worked Execution

We trace the $3 \times 3$ connection matrix:

---

### Step 1: Initialize
- $vis = [\text{False}, \text{False}, \text{False}]$
- $ans = 0$

---

### Step 2: City $0$
- $vis[0]$ is False $\implies ans \leftarrow 0 + 1 = \mathbf{1}$.
- Start $dfs(0)$:
  - $vis[0] \leftarrow \text{True}$.
  - Neighbors of 0:
    - $j = 1$: $isConnected[0][1] = 1$ and $vis[1]$ is False $\implies$ call $dfs(1)$.
      - $vis[1] \leftarrow \text{True}$.
      - Neighbors of 1: $0$ (already visited), $2$ (not connected).
      - $dfs(1)$ returns.
    - $j = 2$: $isConnected[0][2] = 0$.
  - $dfs(0)$ returns.
- Visited: `[True, True, False]`.

---

### Step 3: City $1$
- $vis[1]$ is True $\implies$ Skip.

---

### Step 4: City $2$
- $vis[2]$ is False $\implies ans \leftarrow 1 + 1 = \mathbf{2}$.
- Start $dfs(2)$:
  - $vis[2] \leftarrow \text{True}$.
  - Neighbors of 2: none connected.
  - $dfs(2)$ returns.
- Visited: `[True, True, True]`.

---

### Step 5: Final Count
$$
ans = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| Outer City Index $i$ | Prior $vis[i]$ | Action Taken | Subroutine $dfs$ Path | Visited Set After Call | Running Province Count $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | **False** | Start new province | $0 \to 1$ | $\{0, 1\}$ | **$1$** |
| $1$ | **True** | Skip (already in province 1) | None | $\{0, 1\}$ | $1$ |
| **$2$** | **False** | Start new province | $2$ (isolated) | $\{0, 1, 2\}$ | **$2$** |
| **Done** | — | — | — | All visited | **Result: $2$** |

---

## 5. Boundary Cases & Failure Modes

- **Single City ($n = 1$):** Trivial connected component $\implies ans = 1$.
- **Complete Graph ($K_n$, all 1s):** First DFS marks all $n$ nodes $\implies ans = 1$.
- **Empty Graph ($n$ isolated vertices, diagonal 1s only):** Every node starts its own DFS $\implies ans = n$.
- **Chain Topology ($0 \leftrightarrow 1 \leftrightarrow 2 \dots \leftrightarrow n-1$):** Traverses entire chain in a single DFS pass $\implies ans = 1$.

---

## 6. Traps & Common Anti-Patterns

- **Counting Symmetrical Matrix Pairs ($isConnected[i][j] == 1$):** Summing the number of 1s in the matrix counts direct edges, not connected components. A chain of 3 cities has 2 edges, but forms 1 province.
- **Forgetting Diagonal Self-Loops:** $isConnected[i][i] = 1$ by definition. The visited check `not vis[j]` prevents infinite recursion on the node itself.
- **Using $O(N^3)$ Matrix Multiplication (Floyd-Warshall):** Transitive closure via all-pairs shortest path is $O(N^3)$. Standard DFS or Breadth-First Search executes in $O(N^2)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Every vertex is visited at most once.
  - When visiting a vertex, we scan its row of $N$ elements in the adjacency matrix.
  - Scanning $N$ rows of size $N$ takes $\mathcal{O}(N^2)$ operations.
  - Total Time: $\mathcal{O}(N^2)$. For $N = 200$, $200^2 = 4 \times 10^4$ operations, completing in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the recursion call stack and boolean visited array $vis$.
