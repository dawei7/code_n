# Guided Example: Array Nesting

We trace the step-by-step permutation cycle decomposition, functional digraph degree conservation (in-degree 1, out-degree 1), disjoint cycle orbit traversal ($i \to nums[i]$), visited node memoization ($vis$), and maximum cycle length extraction on representative permutations:

- **Input:** $nums = [5, 4, 0, 3, 1, 6, 2]$
- **Required output:** `4`
  - Permutation property: An array of length $n = 7$ containing every integer from $0$ to $n - 1$ exactly once.
  - Sequence generation rule: Starting from index $k$, generate the set:
    $$
    S[k] = \{nums[k], \; nums[nums[k]], \; nums[nums[nums[k]]], \dots\}
    $$
    until an element repeats (completing a closed cycle).
  - Objective: Find the maximum cardinality $\max_k |S[k]|$.
- **Permutation Cycle Decomposition Trace:**
  - In any finite permutation of $\{0, 1, \dots, n-1\}$:
    - Every node $i$ has exactly one outgoing edge: $i \to nums[i]$.
    - Since elements are unique, every node $i$ has exactly one incoming edge: $nums^{-1}[i] \to i$.
    - **Fundamental Graph Theorem:** Every vertex in such a graph belongs to **exactly one simple directed cycle**! The graph is a collection of disjoint cycles with no branches, trees, or dangling tails.
    - Any node in a cycle generates the **exact same set of elements** as any other node in that same cycle.
    - Therefore, each cycle needs to be traversed and counted **only once**!
  - **Step 1: Initialize Visited State:**
    $$
    vis = [\text{False}, \text{False}, \text{False}, \text{False}, \text{False}, \text{False}, \text{False}]
    $$
    $$
    res = 0
    $$
  - **Step 2: Inspect Index $i = 0$ ($vis[0] == \text{False}$):**
    - Start a new cycle from $i = 0$:
      - Hop 1: $cur = nums[0] = \mathbf{5}$. Mark $vis[5] \leftarrow \text{True}$. Length $m = 1$.
      - Hop 2: $cur = nums[5] = \mathbf{6}$. Mark $vis[6] \leftarrow \text{True}$. Length $m = 2$.
      - Hop 3: $cur = nums[6] = \mathbf{2}$. Mark $vis[2] \leftarrow \text{True}$. Length $m = 3$.
      - Hop 4: $cur = nums[2] = \mathbf{0}$. Mark $vis[0] \leftarrow \text{True}$. Length $m = 4$.
      - Next hop: $nums[0] = 5 == nums[i]$ $\implies$ Returned to start! Cycle closes.
    - Cycle 1 discovered: $\{5, 6, 2, 0\}$ with length $m = 4$.
    - Update maximum:
      $$
      res \leftarrow \max(0, 4) = \mathbf{4}
      $$
    - Visited state:
      $$
      vis = [\mathbf{\text{True}}, \text{False}, \mathbf{\text{True}}, \text{False}, \text{False}, \mathbf{\text{True}}, \mathbf{\text{True}}]
      $$
  - **Step 3: Inspect Index $i = 1$ ($vis[1] == \text{False}$):**
    - Start cycle from $i = 1$:
      - Hop 1: $cur = nums[1] = \mathbf{4}$. Mark $vis[4] \leftarrow \text{True}$. Length $m = 1$.
      - Hop 2: $cur = nums[4] = \mathbf{1}$. Mark $vis[1] \leftarrow \text{True}$. Length $m = 2$.
      - Next hop: $nums[1] = 4 == nums[i] \implies$ Cycle closes.
    - Cycle 2 discovered: $\{4, 1\}$ with length $m = 2$.
    - Update maximum: $res \leftarrow \max(4, 2) = \mathbf{4}$.
  - **Step 4: Inspect Index $i = 2$ ($vis[2] == \text{True}$):**
    - Already measured in Cycle 1 $\implies$ **Skip!**
  - **Step 5: Inspect Index $i = 3$ ($vis[3] == \text{False}$):**
    - Start cycle from $i = 3$:
      - Hop 1: $cur = nums[3] = \mathbf{3}$. Mark $vis[3] \leftarrow \text{True}$. Length $m = 1$.
      - Next hop: $nums[3] = 3 == nums[i] \implies$ Self-loop closes.
    - Cycle 3 discovered: $\{3\}$ with length $m = 1$.
    - $res \leftarrow \max(4, 1) = \mathbf{4}$.
  - **Step 6: Inspect Indices $i = 4, 5, 6$:**
    - All are marked `True` $\implies$ **Skip!**
  - All indices examined.
  - Final maximum cycle length: **`4`**.
- **Identity Permutation ($nums = [0, 1, 2]$):**
  - Every element is a self-loop ($0 \to 0, 1 \to 1, 2 \to 2$) $\implies$ length is **`1`**.
- **Single Global Hamiltonian Cycle ($nums = [1, 2, 3, 0]$):**
  - Single traversal visits all elements $\implies$ length is **`4`**.

This instance demonstrates functional digraph decomposition into disjoint periodic orbits, mathematically proves why marking visited nodes prevents duplicate work and preserves linear time, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a permutation $nums$ of numbers from $0$ to $n - 1$:
Define set $S[k] = \{nums[k], nums[nums[k]], \dots\}$ stopping when an element repeats.
Find the **maximum size of set $S[k]$**.

```text
nums = [ 5,  4,  0,  3,  1,  6,  2 ]

Graph Representation (i -> nums[i]):
  Cycle 1:  0 -> 5 -> 6 -> 2 -> 0   (Size 4)
  Cycle 2:  1 -> 4 -> 1             (Size 2)
  Cycle 3:  3 -> 3                  (Size 1)

Max Cycle Size = 4
```

### The Disjoint Cycle Property of Permutations
- Because $nums$ is a **permutation**:
  - Every index has an out-degree of 1 (maps to $nums[i]$).
  - Every value appears exactly once, so every index has an in-degree of 1.
- In any finite directed graph where every vertex has in-degree 1 and out-degree 1:
  - The graph partitions into a set of **mutually disjoint simple cycles**.
  - There are no tree structures, branchings, or dead ends.
- Every node in a cycle generates the exact same cycle!
- Measuring a cycle once and marking all its nodes as visited guarantees that every node is touched at most once.

---

## 2. Conceptual Foundation & Invariants

### 1. The Algorithm:
1. Initialize boolean array $vis$ of length $n$ with `False`.
2. Initialize $res = 0$.
3. For each index $i \in [0, n - 1]$:
   - If $vis[i]$ is `True`: continue.
   - Trace the cycle starting from $nums[i]$:
     - Mark $vis[cur] = \text{True}$.
     - Increment cycle length $m$.
     - Move to $cur = nums[cur]$ until returning to $nums[i]$.
   - Update $res \leftarrow \max(res, m)$.
4. Return $res$.

> **Disjoint Partition Invariant.** Because every index belongs to exactly one cycle, the sum of lengths across all disjoint cycles equals $n$, bounding total step transitions to $O(N)$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [5, 4, 0, 3, 1, 6, 2]$:

---

### Step 1: Initialize
- $vis = [\text{False}] \times 7$
- $res = 0$

---

### Step 2: Cycle from $i = 0$
- $nums[0] = 5$ is unvisited.
- $cur = 5 \to vis[5] = \text{True}, \; m = 1$.
- $nums[5] = 6 \to cur = 6, \; vis[6] = \text{True}, \; m = 2$.
- $nums[6] = 2 \to cur = 2, \; vis[2] = \text{True}, \; m = 3$.
- $nums[2] = 0 \to cur = 0, \; vis[0] = \text{True}, \; m = 4$.
- $nums[0] = 5 == nums[i] \implies$ Cycle complete!
- $res \leftarrow \max(0, 4) = \mathbf{4}$.

---

### Step 3: Cycle from $i = 1$
- $nums[1] = 4$ is unvisited.
- $cur = 4 \to vis[4] = \text{True}, \; m = 1$.
- $nums[4] = 1 \to cur = 1, \; vis[1] = \text{True}, \; m = 2$.
- $nums[1] = 4 == nums[i] \implies$ Cycle complete!
- $res \leftarrow \max(4, 2) = \mathbf{4}$.

---

### Step 4: Indices $2, 3, 4, 5, 6$
- $i = 2$: $vis[2]$ is True $\implies$ Skip.
- $i = 3$: Unvisited self-loop $3 \to 3 \implies m = 1 \implies res = 4$.
- $i = 4, 5, 6$: All visited $\implies$ Skip.

---

### Step 5: Final Result
$$
res = \mathbf{4}
$$

---

## 4. Complete Execution Trace

| Cycle Index | Start Node | Traversal Orbit ($cur \to nums[cur]$) | Cycle Length $m$ | Nodes Marked Visited | Running Max $res$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Cycle 1** | $0$ | $5 \to 6 \to 2 \to 0 \to 5$ | **$4$** | $\{0, 2, 5, 6\}$ | **$4$** |
| **Cycle 2** | $1$ | $4 \to 1 \to 4$ | $2$ | $\{1, 4\}$ | $4$ |
| **Cycle 3** | $3$ | $3 \to 3$ | $1$ | $\{3\}$ | $4$ |
| **Done** | — | All 7 vertices partitioned | — | All True | **Result: $4$** |

---

## 5. Boundary Cases & Failure Modes

- **Identity Permutation ($[0, 1, 2]$):** $n$ independent self-loops of size 1 $\implies res = 1$.
- **Full Transposition Cycle ($[1, 2, 3, 0]$):** Entire array forms a single cycle of size $n \implies res = n$.
- **Two-Element Swaps ($[1, 0, 3, 2]$):** Multiple disjoint 2-cycles $\implies res = 2$.
- **Large $N = 10^5$:** Single-pass visited checks guarantee linear runtime with zero recursion overhead.

---

## 6. Traps & Common Anti-Patterns

- **Using a Set for Each Starting Index ($O(N^2)$):** Re-tracing the cycle for every starting index without global visited tracking causes quadratic runtime on large cycles. A global $vis$ array guarantees each node is visited once.
- **Modifying the Input Array In-Place Without Permutation:** Marking visited by setting `nums[cur] = -1` works only if modifying input is permissible; using an auxiliary boolean array preserves input immutability.
- **Expecting Dead Ends:** In a permutation, no path can ever terminate in a dead end or merge into another cycle; every path is strictly a pure simple cycle.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Outer loop runs $N$ times.
  - The while loop visits each element in a cycle exactly once.
  - Since cycles are disjoint, each element in the array is processed at most twice (once in the while loop, once checked in the outer loop).
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 10^5$, completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the boolean array $vis$.
