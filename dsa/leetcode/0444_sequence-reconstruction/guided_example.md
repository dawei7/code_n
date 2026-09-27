# Guided Example: Sequence Reconstruction

We trace the step-by-step directed graph construction from sequence pairs, Kahn's algorithm in-degree tracking, the strict single-candidate queue invariant ($|Q| == 1$), topological ambiguity branch detection, and unique shortest supersequence verification on representative permutation instances:

- **Input:**
  - $nums = [1, 2, 3]$
  - $sequences = [[1, 2], [1, 3], [2, 3]]$
- **Required output:** `true`
  - Total vertices: $n = 3$, values in range $[1, 3]$
  - Directed edges from adjacent sequence pairs:
    - From $[1, 2]$: edge $1 \to 2$
    - From $[1, 3]$: edge $1 \to 3$
    - From $[2, 3]$: edge $2 \to 3$
  - Initial in-degrees:
    - Node $1$: in-degree $0$
    - Node $2$: in-degree $1$ (from $1$)
    - Node $3$: in-degree $2$ (from $1$ and $2$)
  - Initial zero-in-degree queue: $Q = [1]$ (Size $|Q| = 1$, unique starter!)
  - **Topological Step 1:**
    - Queue size check: $|Q| = 1$ (Pass: No ambiguity)
    - Dequeue Node $1$
    - Decrement neighbor in-degrees:
      - $indeg[2] \leftarrow 1 - 1 = 0 \implies$ Enqueue $2$
      - $indeg[3] \leftarrow 2 - 1 = 1$
    - Queue state: $Q = [2]$
  - **Topological Step 2:**
    - Queue size check: $|Q| = 1$ (Pass: No ambiguity)
    - Dequeue Node $2$
    - Decrement neighbor in-degrees:
      - $indeg[3] \leftarrow 1 - 1 = 0 \implies$ Enqueue $3$
    - Queue state: $Q = [3]$
  - **Topological Step 3:**
    - Queue size check: $|Q| = 1$ (Pass: No ambiguity)
    - Dequeue Node $3$
    - Queue state: $Q = []$ (Empty)
  - Processed all $n = 3$ vertices with strictly $|Q| = 1$ at every single transition.
  - Reconstructed sequence is uniquely determined: $[1, 2, 3] \implies$ Return `true`
- **Ambiguous Branching Instance:** $nums = [1, 2, 3], sequences = [[1, 2], [1, 3]]$
  - Removing $1$ makes both $2$ and $3$ reach in-degree $0 \implies Q = [2, 3]$ ($|Q| = 2 > 1$).
  - Both $[1, 2, 3]$ and $[1, 3, 2]$ are valid supersequences $\implies$ **Not unique $\implies$ `false`**
- **Missing Elements Instance:** $sequences = [[1, 2]]$ for $nums = [1, 2, 3] \implies$ Node $3$ unconstrained $\implies$ `false`

This instance demonstrates modeling sequence constraints as a Directed Acyclic Graph (DAG), mathematically proves why a topological ordering is unique if and only if the zero-in-degree frontier has cardinality strictly 1 at every step (Hamiltonian path in tournament subgraphs), and achieves $O(V + E)$ runtime and $O(V + E)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [1, 2, 3]$ (a permutation of $1 \dots n$) and a list of subsequences $sequences$:
Determine whether $nums$ is the **unique shortest supersequence** of $sequences$:
- A supersequence contains all arrays in $sequences$ as subsequences.
- $nums$ is the unique shortest supersequence if and only if:
  1. $nums$ is a valid supersequence.
  2. No other supersequence of minimal length exists.

```text
Dependency Graph:
     (1)
    /   \
   v     v
  (2) -> (3)

Topological Peel Sequence:
  Step 1: In-degree 0 -> Only Node 1  (Queue: [1], |Q| = 1)
  Step 2: In-degree 0 -> Only Node 2  (Queue: [2], |Q| = 1)
  Step 3: In-degree 0 -> Only Node 3  (Queue: [3], |Q| = 1)

Every step has a unique choice -> Unique Reconstruction -> true
```

### The Unique Topological Sort Criterion
A directed edge $u \to v$ expresses the constraint: "node $u$ must appear before node $v$."
In Kahn's algorithm for topological sorting:
- The queue $Q$ holds all nodes whose prerequisites have all been fulfilled (in-degree $= 0$).
- **If at any point $|Q| > 1$:** There are multiple eligible nodes that could legally occupy the current position. Swapping their order produces another distinct valid topological sequence, meaning the sequence is **not unique**!
- **Uniqueness Theorem:** A directed acyclic graph has a unique topological sort if and only if at every step of Kahn's algorithm, the queue of zero-in-degree vertices contains **exactly one element** ($|Q| == 1$).

---

## 2. Conceptual Foundation & Invariants

### 1. Directed Graph Modeling:
For each sequence $[s_0, s_1, \dots, s_k]$ in $sequences$:
Add a directed edge for every adjacent pair:
$$
s_i \to s_{i+1} \quad \forall i \in [0, k - 1]
$$
Increment $indeg[s_{i+1}] \leftarrow indeg[s_{i+1}] + 1$.

### 2. The Strict Singlet Queue Invariant:
Initialize $Q$ with all nodes having $indeg[v] == 0$:
- **Loop Condition:** While $|Q| == 1$:
  - Pop the unique active node $u = Q.\text{popleft}()$.
  - For each neighbor $v$ of $u$:
    - Decrement $indeg[v] \leftarrow indeg[v] - 1$.
    - If $indeg[v] == 0$: append $v$ to $Q$.
- **Termination Check:**
  - If the loop terminates with $|Q| == 0$, exactly $n$ nodes were popped, each chosen without ambiguity $\implies$ Return `True`.
  - If the loop terminates with $|Q| > 1$, multiple branches exist $\implies$ Return `False`.
  - If the loop terminates with $|Q| == 0$ before processing $n$ nodes, a cycle or disconnected component exists $\implies$ Return `False`.

> **Singlet Invariant.** At step $t$, if $|Q| = 1$, the choice of the $t$-th element in the sequence is unconditionally forced, with zero degrees of freedom.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 3]$ with $sequences = [[1, 2], [1, 3], [2, 3]]$ ($n = 3$):

---

### Step 1: Graph Construction & In-Degree Calculation
Process sequence pairs:
- Pair $(1, 2)$: edge $1 \to 2, \; indeg[2] += 1$
- Pair $(1, 3)$: edge $1 \to 3, \; indeg[3] += 1$
- Pair $(2, 3)$: edge $2 \to 3, \; indeg[3] += 1$
In-degrees:
$$
indeg = \{1: 0, \; 2: 1, \; 3: 2\}
$$
Adjacency lists:
$$
g[1] = [2, 3], \quad g[2] = [3], \quad g[3] = []
$$

---

### Step 2: Initialize Queue
Find all nodes with in-degree 0:
- Only Node $1$ has $indeg[1] == 0$.
- Queue: $Q = [1]$.
- Size $|Q| = 1$.

---

### Step 3: Topological Iteration 1
- Verify $|Q| == 1$: Holds ($Q = [1]$).
- Dequeue $u = 1$.
- Examine neighbors in $g[1] = [2, 3]$:
  - Neighbor $2$: $indeg[2] \leftarrow 1 - 1 = \mathbf{0} \implies Q.\text{append}(2)$
  - Neighbor $3$: $indeg[3] \leftarrow 2 - 1 = \mathbf{1} \implies$ Not zero
- Queue after step: $Q = [2]$.
- Size $|Q| = 1$.

---

### Step 4: Topological Iteration 2
- Verify $|Q| == 1$: Holds ($Q = [2]$).
- Dequeue $u = 2$.
- Examine neighbors in $g[2] = [3]$:
  - Neighbor $3$: $indeg[3] \leftarrow 1 - 1 = \mathbf{0} \implies Q.\text{append}(3)$
- Queue after step: $Q = [3]$.
- Size $|Q| = 1$.

---

### Step 5: Topological Iteration 3
- Verify $|Q| == 1$: Holds ($Q = [3]$).
- Dequeue $u = 3$.
- Neighbors in $g[3]$: None.
- Queue after step: $Q = []$.
- Size $|Q| = 0$.

---

### Termination:
Loop condition `while len(q) == 1` stops because `len(q) == 0`.
Check: Did $Q$ end empty after processing all nodes?
Yes: `len(q) == 0` evaluates to **`true`**.

---

## 4. Complete Execution Trace

| Iteration | Initial Queue $Q$ | Queue Size $|Q|$ | Dequeued Node $u$ | Neighbors Updated | New In-Degrees | Enqueued Nodes | Final Queue State |
|:---:|:---:|:---:|:---:|:---|:---|:---:|:---:|
| **Init** | $[1]$ | $1$ | — | — | $\{1:0, 2:1, 3:2\}$ | — | $[1]$ |
| **1** | $[1]$ | **$1$ (Unique)** | $1$ | $2, 3$ | $indeg[2]: 1 \to 0$<br>$indeg[3]: 2 \to 1$ | $2$ | $[2]$ |
| **2** | $[2]$ | **$1$ (Unique)** | $2$ | $3$ | $indeg[3]: 1 \to 0$ | $3$ | $[3]$ |
| **3** | $[3]$ | **$1$ (Unique)** | $3$ | None | None | None | `[]` (Empty) |
| **End** | `[]` | $0$ | — | — | All in-degrees $0$ | — | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Ambiguous Topo Sort ($sequences = [[1, 2], [1, 3]]$):**
  - After removing $1$, both $2$ and $3$ reach in-degree $0 \implies Q = [2, 3]$.
  - Size $|Q| = 2 \ne 1$. Loop halts immediately.
  - Return condition `len(q) == 0` evaluates to $2 == 0 \implies \mathbf{false}$.
- **Single Element ($nums = [1], sequences = [[1]]$):** $indeg[1] = 0, Q = [1]$. Loops once, queue becomes empty $\implies \mathbf{true}$.
- **Disconnected Subsequence ($nums = [1, 2], sequences = [[1], [2]]$):** No edges $\implies indeg = \{1: 0, 2: 0\} \implies Q = [1, 2]$ ($|Q| = 2 > 1$) $\implies \mathbf{false}$.
- **Cycle in Sequences:** Queue empties before all $n$ nodes are visited $\implies$ not all in-degrees reach 0 $\implies$ returns `false`.

---

## 6. Traps & Common Anti-Patterns

- **Only Checking if `nums` is a Valid Supersequence:** Confirming that each sequence is a subsequence of `nums` is necessary but not sufficient; one must also verify that *no other* sequence is valid. Testing $|Q| == 1$ is the only robust guarantee of uniqueness.
- **Transitive Edge Explosion:** Adding edges between *all* pairs in a sequence $[s_0, s_1, s_2]$ creates $O(K^2)$ edges. Only consecutive pairs $(s_i, s_{i+1})$ are needed because reachability is transitive, keeping total edges bounded by $\sum |seq|$.
- **0-Indexed Conversion Mishap:** Permutation values are in $[1, n]$. Subtracting 1 consistently maps values to $[0, n - 1]$ without array out-of-bounds indexing.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $V = n$ be the number of nodes and $E = \sum (|seq| - 1)$ be the total number of adjacent pairs in `sequences`.
  - Building the graph takes $O(V + E)$ time.
  - Kahn's algorithm visits each vertex and edge at most once, performing $O(1)$ queue operations per node.
  - Total Time: $\mathcal{O}(V + E)$. For $V, E \le 10^5$, executes in under 20 ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(V + E)$ to store the adjacency list $g$, in-degree array $indeg$, and BFS queue $Q$.
