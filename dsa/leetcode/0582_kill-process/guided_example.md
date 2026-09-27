# Guided Example: Kill Process

We trace the step-by-step parent-to-child adjacency graph construction ($g[ppid].\text{append}(pid)$), subtree rooting at target kill process (`dfs(kill)`), cascade termination propagation, depth-first pre-order process traversal, and collective killed process ID collection on representative process hierarchies:

- **Input:**
  - Process IDs: $pid = [1, 3, 10, 5]$
  - Parent IDs: $ppid = [3, 0, 5, 3]$
  - Target process to terminate: $kill = 5$
- **Required output:** `[5, 10]`
  - Process tree structure:
    - Root process: Process $3$ ($ppid = 0$, no parent).
    - Children of Process $3$: Process $1$ ($ppid = 3$) and Process $5$ ($ppid = 3$).
    - Children of Process $5$: Process $10$ ($ppid = 5$).
  - Cascading kill rule: Terminating a process automatically terminates all of its direct children, their children, and all transitive descendants in its subtree.
- **Tree Subtree Depth-First Search Trace:**
  - **Step 1: Invert Parent Pointers to Build Child Adjacency Map $g$:**
    - For each pair $(pid[i], ppid[i])$:
      - Pair $(1, 3) \implies g[3].\text{append}(1)$
      - Pair $(3, 0) \implies g[0].\text{append}(3)$
      - Pair $(10, 5) \implies g[5].\text{append}(10)$
      - Pair $(5, 3) \implies g[3].\text{append}(5)$
    - Adjacency structure $g$:
      - Node $0$ (virtual root): $\to [3]$
      - Node $3$: $\to [1, 5]$
      - Node $5$: $\to [10]$
      - Node $1$: $\to []$
      - Node $10$: $\to []$
  - **Step 2: Subtree Traversal Rooted at `kill = 5`:**
    - Start DFS at target node $i = 5$:
      - **Visit Process $5$:**
        - Append $5$ to result list:
          $$
          ans = [5]
          $$
        - Inspect children of Process $5$: $g[5] = [10]$.
      - **Recurse on Child Process $10$:**
        - Append $10$ to result list:
          $$
          ans = [5, \; 10]
          $$
        - Inspect children of Process $10$: $g[10] = []$ (Leaf node).
        - Traversal of Process $10$'s branch completes.
      - Traversal of Process $5$'s branch completes.
  - **Step 3: Collect Terminated Processes:**
    - The gathered subtree members are:
      $$
      ans = \mathbf{[5, 10]}
      $$
    - *(Processes $3$ and $1$ are upstream/independent and remain active)*.
- **Kill Root Process ($kill = 3$):**
  - Traversal from Node 3 visits: $3$, $1$, $5$, $10$ $\implies$ All $4$ processes terminated.
- **Kill Leaf Process ($kill = 10$):**
  - Node 10 has no children $\implies$ Only Process $10$ terminated: $[10]$.
- **Single Process System ($pid = [1], ppid = [0], kill = 1$):**
  - Single node $\implies [1]$.

This instance demonstrates cascade tree termination via inverted pointer adjacency graphs, mathematically proves why pre-order DFS visits every descendant in the target subtree exactly once, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two arrays $pid$ (process IDs) and $ppid$ (parent process IDs), and a target $kill$:
When a process is terminated, all of its descendants are also terminated.
Return the **list of all process IDs that will be killed**.

```text
Process Tree:
         0 (OS Kernel)
         |
         3 (Root)
       /   \
      1     5
             \
             10

Kill Process 5:
  Terminates Process 5 and its entire subtree (Process 10).
  Killed list = [5, 10]
```

### Inverting Pointers to Enable Top-Down Traversal
- The input provides parent pointers ($child \to parent$).
- Following parent pointers upwards only reveals ancestors, but we need to find all **descendants**.
- By building an adjacency list $parent \to [children]$:
  - The problem transforms into standard graph reachability.
  - Running a DFS or BFS starting from the node `kill` extracts all terminated processes in linear time.

---

## 2. Conceptual Foundation & Invariants

### 1. Adjacency Graph Construction:
For each index $i \in [0, n - 1]$:
$$
g[ppid[i]].\text{append}(pid[i])
$$

### 2. Subtree Traversal $dfs(u)$:
1. Add $u$ to result list $ans$.
2. For each child $v \in g[u]$:
   Recurse: $dfs(v)$.

> **Subtree Closure Invariant.** Because the process relationships form a rooted tree with no cycles, a DFS initiated at `kill` traverses the exact reflexive transitive closure of the child relation from `kill`.

---

## 3. Step-by-Step Worked Execution

We trace $kill = 5$:

---

### Step 1: Build Adjacency List
- $g[3] = [1, 5]$
- $g[0] = [3]$
- $g[5] = [10]$
- $g[1] = []$
- $g[10] = []$

---

### Step 2: Traverse from $kill = 5$
- Visit Node 5:
  - $ans.\text{append}(5)$
  - Children of 5: $[10]$
- Visit Node 10:
  - $ans.\text{append}(10)$
  - Children of 10: none.

---

### Step 3: Final Output
$$
ans = \mathbf{[5, 10]}
$$

---

## 4. Complete Execution Trace

| Call Stack | Current Node $u$ | Action | Children to Visit $g[u]$ | Accumulated $ans$ |
|:---:|:---:|:---:|:---:|:---:|
| $dfs(5)$ | $5$ | Add $5$ to $ans$ | `[10]` | `[5]` |
| $dfs(10)$ | $10$ | Add $10$ to $ans$ | `[]` | **`[5, 10]`** |
| Return | — | Subtree exhausted | — | **Result: `[5, 10]`** |

---

## 5. Boundary Cases & Failure Modes

- **Kill Root Process ($ppid = 0$):** Visits every node in the tree $\implies$ returns all $N$ processes.
- **Kill Leaf Process:** Node has empty child list $\implies$ returns $[kill]$ alone.
- **Single Process ($N = 1$):** Returns $[kill]$.
- **Deep Process Tree ($N = 5 \times 10^4$):** Standard DFS or iterative queue BFS traverses $50{,}000$ nodes in $< 10$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Searching by Filtering $ppid$ in Repeated Passes ($O(N^2)$):** Iteratively scanning the arrays to find children of killed processes takes quadratic time. Building a hash map adjacency list reduces lookup to $O(1)$ per edge.
- **Cycles in Process Tree:** By operating system definition, process trees have no cycles and every process (except the root) has exactly one parent. Visited sets are not required for simple trees.
- **Preserving Output Order:** The problem allows the result to be returned in any order (`unordered_list` validator).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Building the adjacency map from $N$ pairs: $\mathcal{O}(N)$ time.
  - DFS visits each node in the killed subtree at most once: $\mathcal{O}(K)$ where $K \le N$ is the size of the subtree.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 5 \times 10^4$, completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the child adjacency graph $g$ and the recursion stack.