# Guided Example: Find Largest Value in Each Tree Row

We trace the step-by-step row-wise breadth-first search (BFS), queue boundary snapshotting ($\text{len}(q)$), negative infinity accumulator initialization ($x \leftarrow -\infty$), per-level maximum reduction ($x = \max(x, node.val)$), and hierarchical peak vector assembly on representative binary trees:

- **Input:** $root = [1, 3, 2, 5, 3, \text{null}, 9]$
  - Tree structure:
    - Row 0: Node $1$
    - Row 1: Node $3$ (left), Node $2$ (right)
    - Row 2: Node $5$ (left of $3$), Node $3$ (right of $3$), Node $9$ (right of $2$)
- **Required output:** `[1, 3, 9]`
  - Objective: Return an array where the $i$-th element is the maximum value found in row $i$ of the tree.
- **Level-order BFS execution trace:**
  - Initialize output vector $ans = []$ and queue $q = [root]$.
  - **Row 0 (Root Level):**
    - Current queue size: $1$ (Node $1$)
    - Initialize row maximum: $x \leftarrow -\infty$
    - Dequeue $1$:
      - Update row max: $x \leftarrow \max(-\infty, 1) = \mathbf{1}$
      - Enqueue left child $3$, enqueue right child $2$
    - End of Row 0: append $x = \mathbf{1}$ to $ans \implies ans = [1]$
    - Next level queue: $q = [3, 2]$
  - **Row 1:**
    - Current queue size: $2$ (Nodes $3, 2$)
    - Initialize row maximum: $x \leftarrow -\infty$
    - Dequeue $3$:
      - Update row max: $x \leftarrow \max(-\infty, 3) = 3$
      - Enqueue left child $5$, enqueue right child $3$
    - Dequeue $2$:
      - Update row max: $x \leftarrow \max(3, 2) = \mathbf{3}$
      - Enqueue right child $9$
    - End of Row 1: append $x = \mathbf{3}$ to $ans \implies ans = [1, 3]$
    - Next level queue: $q = [5, 3, 9]$
  - **Row 2:**
    - Current queue size: $3$ (Nodes $5, 3, 9$)
    - Initialize row maximum: $x \leftarrow -\infty$
    - Dequeue $5$:
      - Update row max: $x \leftarrow \max(-\infty, 5) = 5$
      - No children
    - Dequeue $3$:
      - Update row max: $x \leftarrow \max(5, 3) = 5$
      - No children
    - Dequeue $9$:
      - Update row max: $x \leftarrow \max(5, 9) = \mathbf{9}$
      - No children
    - End of Row 2: append $x = \mathbf{9}$ to $ans \implies ans = [1, 3, 9]$
    - Next level queue is empty ($q = []$).
  - BFS terminates.
  - Final peak vector: **`[1, 3, 9]`**.
- **All Negative Values Instance ($root = [-1, -5, -10]$):**
  - Initializing $x = -\infty$ guarantees that negative numbers like $-5$ and $-1$ are correctly preserved without colliding with zero $\implies [-1, -5]$.
- **Empty Tree Instance ($root = \text{null}$):** Returns $\mathbf{[]}$.
- **Single Node Tree ($root = [42]$):** Returns $\mathbf{[42]}$.

This instance demonstrates level-order reduction and extreme-value tracking, mathematically proves why queue snapshotting partitions tree rows without inter-level node mixing, and derives $O(N)$ runtime and $O(W)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree $root = [1, 3, 2, 5, 3, \text{null}, 9]$:
Find the **largest value in each row** of the binary tree (0-indexed).

```text
Tree by Rows:
  Row 0:        [ 1 ]               -> Max = 1
               /     \
  Row 1:     [ 3 ]   [ 2 ]          -> Max = max(3, 2) = 3
            /     \       \
  Row 2:  [ 5 ]   [ 3 ]   [ 9 ]     -> Max = max(5, 3, 9) = 9

Output Vector: [1, 3, 9]
```

### The Level-Order Snapshot Pattern
- A standard BFS queue flattens nodes in chronological order.
- By taking the **queue length snapshot** $K = \text{len}(q)$ at the start of each level:
  - We strictly process exactly the $K$ nodes that belong to the current row.
  - Any children added during this loop are placed at the back of the queue and belong exclusively to the next row.
  - This allows us to compute the maximum value across the current row in a single pass before advancing.

---

## 2. Conceptual Foundation & Invariants

### 1. BFS Level Reduction State Machine:
1. Handle empty tree: If $root == \text{null}$, return `[]`.
2. Initialize $q = [root]$ and $ans = []$.
3. While $q$ is non-empty:
   - Let $K = \text{len}(q)$ be the number of nodes in the current row.
   - Initialize row peak accumulator:
     $$
     x = -\infty
     $$
   - Repeat $K$ times:
     - Pop node $u = q.\text{popleft}()$.
     - Update running row peak:
       $$
       x \leftarrow \max(x, \; u.val)
       $$
     - Push children:
       $$
       \text{If } u.left: q.\text{append}(u.left); \quad \text{If } u.right: q.\text{append}(u.right)
       $$
   - Record row peak: $ans.\text{append}(x)$.
4. Return $ans$.

### 2. Negative Value Handling Invariant:
Because node values can be negative (e.g. $node.val \in [-2^{31}, 2^{31} - 1]$):
Initializing $x = -\infty$ (or $-2^{31} - 1$) guarantees that negative maximums are never overwritten by an arbitrary zero default.

> **Level Isolation Invariant.** At the beginning of while-loop iteration $d$, the queue contains precisely all nodes at depth $d$, and exactly $K = \text{len}(q)$ pops process all depth-$d$ nodes before depth-$(d+1)$ nodes are touched.

---

## 3. Step-by-Step Worked Execution

We trace the sample tree:

---

### Step 1: Initialize
- $root = 1 \ne \text{null}$.
- $q = [\text{Node } 1]$.
- $ans = []$.

---

### Step 2: Row 0 (Depth 0)
- Snapshot size: $K = 1$.
- Initialize $x = -\infty$.
- **Node 1:**
  - $x \leftarrow \max(-\infty, 1) = \mathbf{1}$.
  - Enqueue left child 3, right child 2.
- Append to answer:
  $$
  ans.\text{append}(1) \implies ans = [1]
  $$
- Queue state: $[3, 2]$.

---

### Step 3: Row 1 (Depth 1)
- Snapshot size: $K = 2$.
- Initialize $x = -\infty$.
- **Node 3:**
  - $x \leftarrow \max(-\infty, 3) = 3$.
  - Enqueue left child 5, right child 3.
- **Node 2:**
  - $x \leftarrow \max(3, 2) = \mathbf{3}$.
  - Enqueue right child 9.
- Append to answer:
  $$
  ans.\text{append}(3) \implies ans = [1, 3]
  $$
- Queue state: $[5, 3, 9]$.

---

### Step 4: Row 2 (Depth 2)
- Snapshot size: $K = 3$.
- Initialize $x = -\infty$.
- **Node 5:** $x \leftarrow \max(-\infty, 5) = 5$.
- **Node 3:** $x \leftarrow \max(5, 3) = 5$.
- **Node 9:** $x \leftarrow \max(5, 9) = \mathbf{9}$.
- Append to answer:
  $$
  ans.\text{append}(9) \implies ans = [1, 3, 9]
  $$
- Queue is now empty.

---

### Step 5: Termination
Output array:
$$
\mathbf{[1, 3, 9]}
$$

---

## 4. Complete Execution Trace

| Level Index | Queue Contents | Snapshot Size $K$ | Values Evaluated | Maximum $x = \max(val)$ | Output Vector $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Row 0** | `[1]` | $1$ | $1$ | **$1$** | `[1]` |
| **Row 1** | `[3, 2]` | $2$ | $3, 2$ | **$3$** | `[1, 3]` |
| **Row 2** | `[5, 3, 9]` | $3$ | $5, 3, 9$ | **$9$** | **`[1, 3, 9]`** |
| **Complete** | `[]` | — | — | — | **Result: `[1, 3, 9]`** |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = \text{null}$):** Handled before queue initialization $\implies \mathbf{[]}$.
- **Single Node Tree ($root = [10]$):** 1 row $\implies \mathbf{[10]}$.
- **All Negative Values ($[-2, -5, -3]$):** Initializing $x = -\infty$ ensures $\max(-\infty, -2) = -2$, avoiding false zero maximums $\implies \mathbf{[-2, -3]}$.
- **Unbalanced Skewed Tree ($1 \to 2 \to 3$):** Each row has size 1 $\implies \mathbf{[1, 2, 3]}$.

---

## 6. Traps & Common Anti-Patterns

- **Initializing $x = 0$:** If a tree level contains only negative numbers (e.g. $[-10, -20]$), initializing $x = 0$ falsely returns $0$ as the maximum! $x$ must be initialized to $-\infty$ or the value of the first node popped.
- **Dynamic Queue Length Loop:** Writing `while q:` and popping without snapshotting `len(q)` mixes parents with children, destroying row boundaries.
- **Using Level Number Hash Maps Unnecessarily:** Collecting all nodes in a dictionary `defaultdict(list)` indexed by depth takes $O(N)$ extra memory. Computing the maximum in-flight during BFS takes $O(1)$ extra space per level.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - BFS visits each node and pushes each edge once.
  - Finding the maximum of $K$ elements takes $O(K)$ comparisons.
  - Across all rows, $\sum K_i = N$.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(W)$ where $W$ is the maximum tree width to store the BFS queue.
