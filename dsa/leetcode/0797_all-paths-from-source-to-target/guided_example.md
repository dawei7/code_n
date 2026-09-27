# Guided Example: All Paths From Source to Target

We trace the step-by-step Directed Acyclic Graph (DAG) traversal mechanics, cycle-free path extension invariant ($path + [v]$), queue-based level-order search frontier ($q = deque([[0]])$), destination detection ($u == n - 1$), and exhaustive path collection on representative directed network graphs:

- **Input:**
  $$
  graph = [[1, 2], \; [3], \; [3], \; []]
  $$
- **Required output:**
  $$
  [[0, 1, 3], \; [0, 2, 3]]
  $$
  - Directed network specifications:
    - The graph is a Directed Acyclic Graph (DAG) with $n$ nodes labeled $0$ to $n - 1$.
    - Edges:
      - $0 \to 1, \quad 0 \to 2$
      - $1 \to 3$
      - $2 \to 3$
      - Node 3 has no outgoing edges.
    - Start node: $0$.
    - Target destination: $n - 1 = 3$.
    - Objective: Find **all possible paths** from node 0 to node $n - 1$ in any order.
    - For the input graph:
      - Path 1: $0 \to 1 \to 3$
      - Path 2: $0 \to 2 \to 3$
      - Exactly 2 valid paths exist $\implies$ return $[[0, 1, 3], [0, 2, 3]]$.
- **DAG Topological Acyclicity & Path Invariant:**
  - **The No-Cycle Guarantee:**
    - Because the problem guarantees a **Directed Acyclic Graph (DAG)**, every path is strictly self-avoiding and finite.
    - Any valid path can visit at most $n$ nodes.
    - No cycle-detection or `visited` set is required to prevent infinite loops!
  - **Path-Queue State Machine:**
    - Initialize a queue containing the initial partial path starting at the source:
      $$
      q = \text{deque}([[0]])
      $$
    - At each iteration:
      1. Dequeue a partial path: $path = q.\text{popleft}()$.
      2. Identify the current head of the path: $u = path[-1]$.
      3. **Termination Check:** If $u == n - 1$, the path has successfully reached the destination!
         - Add a copy of $path$ to the final result list $ans$.
         - Do not extend this path further.
      4. **Branching Extension:** If $u \ne n - 1$:
         - For each neighbor $v \in graph[u]$:
           - Extend the path and enqueue:
             $$
             q.\text{append}(path + [v])
             $$
- **Step-by-Step Worked Execution Trace on the 4-Node Graph:**
  - Graph dimension: $n = 4$, target node $n - 1 = 3$.
  - Initialize: $q = [[0]], ans = []$.
  - **Step 1 (Process Path `[0]`):**
    - Pop path: $path = [0]$. Current node: $u = 0$.
    - $u \ne 3 \implies$ extend along outgoing edges of node 0:
      - Outgoing neighbors: $graph[0] = [1, 2]$.
      - Form extended path 1: $[0] + [1] = [0, 1]$. Enqueue.
      - Form extended path 2: $[0] + [2] = [0, 2]$. Enqueue.
    - Queue state:
      $$
      q = [ [0, 1], \; [0, 2] ]
      $$
  - **Step 2 (Process Path `[0, 1]`):**
    - Pop path: $path = [0, 1]$. Current node: $u = 1$.
    - $u \ne 3 \implies$ extend along outgoing edges of node 1:
      - Outgoing neighbors: $graph[1] = [3]$.
      - Form extended path: $[0, 1] + [3] = [0, 1, 3]$. Enqueue.
    - Queue state:
      $$
      q = [ [0, 2], \; [0, 1, 3] ]
      $$
  - **Step 3 (Process Path `[0, 2]`):**
    - Pop path: $path = [0, 2]$. Current node: $u = 2$.
    - $u \ne 3 \implies$ extend along outgoing edges of node 2:
      - Outgoing neighbors: $graph[2] = [3]$.
      - Form extended path: $[0, 2] + [3] = [0, 2, 3]$. Enqueue.
    - Queue state:
      $$
      q = [ [0, 1, 3], \; [0, 2, 3] ]
      $$
  - **Step 4 (Process Path `[0, 1, 3]`):**
    - Pop path: $path = [0, 1, 3]$. Current node: $u = 3$.
    - Destination reached ($u == n - 1 = 3$)!
    - Record complete path:
      $$
      ans.\text{append}(\mathbf{[0, 1, 3]})
      $$
    - Queue state:
      $$
      q = [ [0, 2, 3] ]
      $$
  - **Step 5 (Process Path `[0, 2, 3]`):**
    - Pop path: $path = [0, 2, 3]$. Current node: $u = 3$.
    - Destination reached ($u == n - 1 = 3$)!
    - Record complete path:
      $$
      ans.\text{append}(\mathbf{[0, 2, 3]})
      $$
  - **Termination:**
    - Queue is now empty.
    - Output:
      $$
      ans = [[0, 1, 3], \; [0, 2, 3]]
      $$
- **Five-Node Multi-Branch Graph Trace ($graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]$):**
  - Node 0 has multiple routes:
    - Direct edge $0 \to 4$.
    - Path $0 \to 3 \to 4$.
    - Paths through 1: $0 \to 1 \to 4$, $0 \to 1 \to 3 \to 4$, $0 \to 1 \to 2 \to 3 \to 4$.
  - All 5 distinct routes are enumerated systematically without omissions or duplicate states.
- **Dead-End Deadlock Paths:**
  - If a path reaches a node $u \ne n - 1$ where $graph[u] = []$, the loop over $graph[u]$ runs 0 times; the path naturally terminates without polluting $ans$.

This instance demonstrates path algebra on directed acyclic posets and exhaustive subtree enumeration, mathematically proves why strict topological ordering guarantees termination of breadth-first path extensions without visited set memoization, and derives $O(2^N \cdot N)$ runtime and $O(2^N \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a Directed Acyclic Graph (DAG) with $n$ nodes:
Find **all paths** from node 0 to node $n - 1$.

```text
graph:
  0 -> [1, 2]
  1 -> [3]
  2 -> [3]
  3 -> []

Paths from 0 to 3:
  1. 0 -> 1 -> 3
  2. 0 -> 2 -> 3

Result: [ [0, 1, 3], [0, 2, 3] ]
```

### The Invariant of DAG Path Extension
- Because the graph is a DAG, no cycles can ever exist.
- We do not need a `visited` set!
- Enqueue paths starting with `[0]`. When $path[-1] == n - 1$, record the complete path.

---

## 2. Conceptual Foundation & Invariants

### 1. Path State Transition:
$$
path = [0, v_1, \dots, u] \implies \forall v \in graph[u]: \; path' = path + [v]
$$

### 2. Destination Condition:
$$
u == n - 1 \implies ans.\text{append}(path)
$$

> **Poset Chain Enumeration Invariant.** A DAG induces a finite strict partial order $(V, \prec)$. All paths from $0$ to $n-1$ correspond to maximal chains in the interval $[0, n-1] \subseteq V$, enumerable in depth-first or breadth-first order without cycle detection.

---

## 3. Step-by-Step Worked Execution

We trace $graph = [[1, 2], [3], [3], []]$:

---

### Step 1: Start at $[0]$
- Neighbors: 1, 2 $\implies$ enqueues $[0, 1]$ and $[0, 2]$.

---

### Step 2: Path $[0, 1]$
- Neighbor of 1: 3 $\implies$ enqueues $[0, 1, 3]$.

---

### Step 3: Path $[0, 2]$
- Neighbor of 2: 3 $\implies$ enqueues $[0, 2, 3]$.

---

### Step 4: Paths Reach Target 3
- $[0, 1, 3]$ reaches 3 $\implies$ added to $ans$.
- $[0, 2, 3]$ reaches 3 $\implies$ added to $ans$.

---

### Step 5: Output
$$
[[0, 1, 3], \; [0, 2, 3]]
$$

---

## 4. Complete Execution Trace

| Step | Dequeued Path | Endpoint Node $u$ | Outgoing Neighbors $graph[u]$ | Enqueued Extended Paths | Destination Reached? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `[0]` | $0$ | `[1, 2]` | `[0, 1], [0, 2]` | No |
| $2$ | `[0, 1]` | $1$ | `[3]` | `[0, 1, 3]` | No |
| $3$ | `[0, 2]` | $2$ | `[3]` | `[0, 2, 3]` | No |
| $4$ | `[0, 1, 3]` | $3$ | `[]` | None | **Yes (Saved to $ans$)** |
| **$5$** | **`[0, 2, 3]`** | **$3$** | **`[]`** | **None** | **Yes (Saved to $ans$)** |

---

## 5. Boundary Cases & Failure Modes

- **Direct Edge to Target ($0 \to n - 1$):** Immediately emits path `[0, n - 1]`.
- **Dead End Nodes:** Path ending at node with no outgoing edges and $u \ne n - 1$ is naturally discarded.
- **Maximum Paths ($2^{n - 1}$):** A complete DAG where each node connects to all subsequent nodes produces $2^{n - 2}$ paths.
- **Two Nodes ($n = 2$):** Only edge $0 \to 1 \implies [[0, 1]]$.

---

## 6. Traps & Common Anti-Patterns

- **Using a Visited Set:** Nodes can be visited multiple times across *different* paths (e.g. node 3 is the destination for both paths). Marking nodes visited globally would block other valid paths!
- **Modifying Shared Path In-Place in DFS without Backtracking:** In recursive DFS, appending to a shared path must be undone upon return: `path.append(v); dfs(v); path.pop()`.
- **Assuming Graph is Sorted:** Neighbors in `graph[u]` may appear in arbitrary order; traversal handles any permutation seamlessly.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In a graph of $N$ nodes, there can be at most $2^{N - 1}$ paths from source to target.
  - Each path has length at most $N$.
  - Total Time: $\mathcal{O}(2^N \cdot N)$ where $N \le 15 \implies \le 32768 \times 15 \approx 5 \times 10^5$ operations. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(2^N \cdot N)$ memory to store all generated paths in the result list.
