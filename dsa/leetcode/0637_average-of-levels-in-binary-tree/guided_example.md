# Guided Example: Average of Levels in Binary Tree

We trace the step-by-step breadth-first level-order queue partitioning ($q = \text{deque}([root])$), snapshot level sizing ($n = |q|$), horizontal node value summation ($s = \sum val_i$), arithmetic mean evaluation ($\mu_d = s / n$), child pointer enqueueing, and hierarchical average sequence generation on representative binary tree structures:

- **Input:** $root = [3, 9, 20, \text{null}, \text{null}, 15, 7]$
  - Hierarchical tree layout:
    ```text
          3          (Level 0: Depth 0)
        /   \
       9     20      (Level 1: Depth 1)
            /  \
           15   7    (Level 2: Depth 2)
    ```
- **Required output:** `[3.00000, 14.50000, 11.00000]`
  - Mathematical definition: For each horizontal tree depth $d \ge 0$, calculate the arithmetic mean of all node values located at that depth:
    $$
    \mu_d = \frac{1}{|V_d|} \sum_{u \in V_d} u.val
    $$
- **Breadth-First Queue Snapshot Invariant:**
  - Standard BFS traverses nodes in level order.
  - To compute level statistics without mixing adjacent depths, we take a **queue size snapshot** $n = |q|$ at the start of each level iteration.
  - Exactly $n$ nodes belong to the current level.
  - Popping exactly $n$ nodes and summing their values yields the exact total sum $s$ and node count $n$ for that horizontal level.
  - As these $n$ nodes are processed, their children are pushed to the back of the queue, forming the complete set of nodes for level $d + 1$.
- **Step-by-Step Worked Execution Trace on $[3, 9, 20, \text{null}, \text{null}, 15, 7]$:**
  - Initialize queue:
    $$
    q = [\text{Node } 3], \quad ans = []
    $$
  - **Level 0 Processing:**
    - Level size snapshot:
      $$
      n = |q| = \mathbf{1}
      $$
    - Reset level accumulator: $s = 0$.
    - **Process Node 3:**
      - Pop Node 3 from queue.
      - Accumulate sum:
        $$
        s \leftarrow 0 + 3 = \mathbf{3}
        $$
      - Enqueue left child: Node 9.
      - Enqueue right child: Node 20.
    - Compute Level 0 average:
      $$
      \mu_0 = \frac{s}{n} = \frac{3}{1} = \mathbf{3.0}
      $$
    - Append to results: $ans = [3.0]$.
    - Queue state for next level: $q = [\text{Node } 9, \; \text{Node } 20]$.
  - **Level 1 Processing:**
    - Level size snapshot:
      $$
      n = |q| = \mathbf{2}
      $$
    - Reset level accumulator: $s = 0$.
    - **Pop 1: Node 9:**
      - Accumulate: $s \leftarrow 0 + 9 = 9$.
      - Children of 9: both `null` $\implies$ nothing enqueued.
    - **Pop 2: Node 20:**
      - Accumulate: $s \leftarrow 9 + 20 = \mathbf{29}$.
      - Enqueue left child: Node 15.
      - Enqueue right child: Node 7.
    - Compute Level 1 average:
      $$
      \mu_1 = \frac{s}{n} = \frac{29}{2} = \mathbf{14.5}
      $$
    - Append to results: $ans = [3.0, \; 14.5]$.
    - Queue state for next level: $q = [\text{Node } 15, \; \text{Node } 7]$.
  - **Level 2 Processing:**
    - Level size snapshot:
      $$
      n = |q| = \mathbf{2}
      $$
    - Reset level accumulator: $s = 0$.
    - **Pop 1: Node 15:**
      - Accumulate: $s \leftarrow 0 + 15 = 15$.
      - Children are `null`.
    - **Pop 2: Node 7:**
      - Accumulate: $s \leftarrow 15 + 7 = \mathbf{22}$.
      - Children are `null`.
    - Compute Level 2 average:
      $$
      \mu_2 = \frac{s}{n} = \frac{22}{2} = \mathbf{11.0}
      $$
    - Append to results: $ans = [3.0, \; 14.5, \; 11.0]$.
    - Queue state: $q = []$ (Empty!).
  - **Step 4: Terminate and Emit:**
    - Queue is exhausted $\implies$ Traversal complete.
    - Return:
      $$
      ans = \mathbf{[3.0, \; 14.5, \; 11.0]}
      $$
- **Single Node Tree ($root = [1]$):**
  - Level 0 has 1 node with value 1 $\implies \mu_0 = 1.0 \implies [1.0]$.
- **Degenerate Linked-List Tree ($1 \to 2 \to 3$):**
  - Level 0 has [1] $\implies 1.0$.
  - Level 1 has [2] $\implies 2.0$.
  - Level 2 has [3] $\implies 3.0$.
  - Result: $[1.0, 2.0, 3.0]$.

This instance demonstrates level-synchronized breadth-first graph traversal, mathematically proves why fixed-length queue polling guarantees strict depth-plane partitioning, and derives $O(N)$ runtime and $O(W)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a binary tree:
Return the **average value** of nodes on each level as a list of floating-point numbers.

```text
Tree:
      3       Level 0: sum = 3,       count = 1 -> avg = 3.0
    /   \
   9     20   Level 1: sum = 9+20=29, count = 2 -> avg = 14.5
        /  \
       15   7 Level 2: sum = 15+7=22, count = 2 -> avg = 11.0

Result: [3.0, 14.5, 11.0]
```

### The Invariant of the Level Snapshot
- Standard BFS maintains a single FIFO queue.
- At the start of processing level $d$, the queue contains **only and all** nodes of level $d$.
- Freezing `n = len(q)` allows you to loop exactly $n$ times to sum and average level $d$, while simultaneously buffering the children for level $d + 1$.

---

## 2. Conceptual Foundation & Invariants

### 1. Level Average Formulation:
$$
\mu_d = \frac{1}{|V_d|} \sum_{u \in V_d} u.val
$$

### 2. The BFS Loop Structure:
```text
q = [root]
while q:
    n = len(q)
    s = 0
    repeat n times:
        node = popleft(q)
        s += node.val
        push children to q
    append s / n to ans
```

> **FIFO Stratification Invariant.** In an unweighted graph search, all vertices at geodesic distance $d$ are dequeued strictly before any vertex at distance $d + 1$ is dequeued.

---

## 3. Step-by-Step Worked Execution

We trace $root = [3, 9, 20, \text{null}, \text{null}, 15, 7]$:

---

### Step 1: Level 0
- Queue: `[3]`. $n = 1, s = 3$.
- Children added: `9, 20`.
- Average: $3 / 1 = \mathbf{3.0}$.

---

### Step 2: Level 1
- Queue: `[9, 20]`. $n = 2$.
- Pop 9: $s = 9$.
- Pop 20: $s = 9 + 20 = 29$. Children added: `15, 7`.
- Average: $29 / 2 = \mathbf{14.5}$.

---

### Step 3: Level 2
- Queue: `[15, 7]`. $n = 2$.
- Pop 15: $s = 15$.
- Pop 7: $s = 15 + 7 = 22$.
- Average: $22 / 2 = \mathbf{11.0}$.

---

### Step 4: Output
$$
\mathbf{[3.0, 14.5, 11.0]}
$$

---

## 4. Complete Execution Trace

| Level Index $d$ | Nodes in Level | Snapshot Count $n$ | Sum of Values $s$ | Computed Average $s / n$ | Queue State After Level |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $[3]$ | $1$ | $3$ | **`3.0`** | `[9, 20]` |
| $1$ | $[9, 20]$ | $2$ | $29$ | **`14.5`** | `[15, 7]` |
| $2$ | $[15, 7]$ | $2$ | $22$ | **`11.0`** | `[]` (Exhausted) |
| **Final** | — | — | — | **`[3.0, 14.5, 11.0]`** | — |

---

## 5. Boundary Cases & Failure Modes

- **Single Root Node:** $n = 1 \implies [val]$.
- **Extreme Negative Values:** Sum and division handle negative numbers with full IEEE-754 floating-point accuracy.
- **Large Level Sums ($10^4$ nodes of value $2^{31} - 1$):** Sum exceeds 32-bit integer limits; in languages like Java/C++, use `double` or `long long` for $s$ to avoid overflow.
- **Unbalanced / Skewed Tree:** Traverses single-node levels accurately.

---

## 6. Traps & Common Anti-Patterns

- **Using Integer Division (`s // n`):** Integer division truncates $29 // 2 = 14$ instead of $14.5$. Always use floating-point division `s / n`.
- **Dynamic Queue Size in Loop Header:** Writing `for _ in range(len(q))` where `len(q)` is re-evaluated after pushing children causes the loop to run indefinitely or mix levels. Freeze $n = len(q)$ first.
- **DFS Depth Array Misalignment:** Doing DFS is valid but requires storing separate sum and count arrays per depth, which is more complex than direct BFS.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Every node in the binary tree is enqueued and dequeued exactly once: $\mathcal{O}(N)$ operations.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(W)$ space where $W$ is the maximum width (maximum number of nodes in any level).
  - In a balanced binary tree, $W \le N / 2 \implies \mathcal{O}(N)$.
