# Guided Example: Find Bottom Left Tree Value

We trace the step-by-step level-order breadth-first search (BFS), queue boundary snapshotting ($\text{len}(q)$), front-of-queue leftmost identification ($q[0].val$), child insertion order (left child then right child), and deepest-level preservation on representative binary trees:

- **Input:** $root = [1, 2, 3, 4, \text{null}, 5, 6, \text{null}, \text{null}, 7]$
  - Tree structure:
    - Level 0: Node $1$
    - Level 1: Node $2$ (left), Node $3$ (right)
    - Level 2: Node $4$ (left of $2$), Node $5$ (left of $3$), Node $6$ (right of $3$)
    - Level 3: Node $7$ (left of $5$)
- **Required output:** `7`
  - Definition: The leftmost value in the deepest row of the tree.
- **Level-order BFS execution trace:**
  - Initialize queue: $q = [1]$, variable $ans = 0$.
  - **Level 0 (Depth 0):**
    - Queue contains: $[1]$
    - Leftmost node at this level: $q[0].val = \mathbf{1}$
    - Update candidate: $ans \leftarrow 1$
    - Dequeue $1$, enqueue its children $2$ and $3$:
      $$
      q = [2, \; 3]
      $$
  - **Level 1 (Depth 1):**
    - Queue contains: $[2, 3]$
    - Leftmost node at this level: $q[0].val = \mathbf{2}$
    - Update candidate: $ans \leftarrow 2$
    - Dequeue $2$: enqueues left child $4$
    - Dequeue $3$: enqueues left child $5$ and right child $6$
    - Queue for next level:
      $$
      q = [4, \; 5, \; 6]
      $$
  - **Level 2 (Depth 2):**
    - Queue contains: $[4, 5, 6]$
    - Leftmost node at this level: $q[0].val = \mathbf{4}$
    - Update candidate: $ans \leftarrow 4$
    - Dequeue $4$: no children
    - Dequeue $5$: enqueues left child $7$
    - Dequeue $6$: no children
    - Queue for next level:
      $$
      q = [7]
      $$
  - **Level 3 (Depth 3, Deepest Level):**
    - Queue contains: $[7]$
    - Leftmost node at this level: $q[0].val = \mathbf{7}$
    - Update candidate: $ans \leftarrow \mathbf{7}$
    - Dequeue $7$: no children
    - Queue is now empty ($q = []$).
  - Loop terminates.
  - Candidate retained from the deepest level:
    $$
    ans = \mathbf{7}
    $$
- **Balanced Tree Instance ($root = [2, 1, 3]$):**
  - Level 0: $[2] \implies ans = 2$
  - Level 1: $[1, 3] \implies ans = \mathbf{1}$
- **Single Node Tree ($root = [10]$):**
  - Only Level 0 exists $\implies ans = \mathbf{10}$
- **Right-Skewed Tree with Single Left Leaf at Deepest Level:**
  - Deepest row has only 1 node, so it is automatically the leftmost of that row.

This instance demonstrates level-wise BFS snapshotting, mathematically proves why queue head observation at level boundaries isolates the leftmost element, and derives $O(N)$ runtime and $O(W)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
Find the **leftmost value** in the **last (deepest) row** of the tree.

```text
Tree:
            1           <- Level 0: Leftmost is 1
          /   \
         2     3         <- Level 1: Leftmost is 2
        /     / \
       4     5   6       <- Level 2: Leftmost is 4
            /
           7             <- Level 3 (Deepest): Leftmost is 7!

Result: 7
```

### Clarifying "Bottom-Left"
- "Bottom-left" does **not** mean the leftmost node in the entire tree (in this example, node $4$ is the leftmost node overall).
- It strictly means:
  1. Find the **deepest row** (maximum depth).
  2. In that deepest row, select the **first node from the left**.
- By using **Level-Order Traversal (BFS)**:
  - We process the tree row by row.
  - At the beginning of each level's processing, the node at the **very front of the queue** is guaranteed to be the leftmost node of that row!
  - When the traversal finishes, the last value recorded is from the deepest row.

---

## 2. Conceptual Foundation & Invariants

### 1. The Level-by-Level BFS Algorithm:
1. Initialize queue with root: $q = [root]$.
2. While $q$ is non-empty:
   - **Capture Leftmost:** The first element in $q$ is the leftmost node of the current level:
     $$
     ans \leftarrow q[0].val
     $$
   - **Process Level:** Iterate $\text{len}(q)$ times:
     - Pop front node $u$.
     - If $u.left$ exists, push $u.left$.
     - If $u.right$ exists, push $u.right$.
3. Return $ans$.

> **FIFO Left-to-Right Invariant.** Because children are enqueued in left-to-right order ($u.left$ before $u.right$), every level in the queue is ordered strictly from left to right, guaranteeing that index 0 is always the leftmost node of that level.

---

## 3. Step-by-Step Worked Execution

We trace the sample tree:

---

### Step 1: Initialize
- $q = [1]$
- $ans = 0$

---

### Step 2: Depth 0
- Queue: `[Node 1]`.
- Record leftmost: $ans \leftarrow 1$.
- Dequeue 1:
  - Enqueue left child 2.
  - Enqueue right child 3.
- Next level queue: `[Node 2, Node 3]`.

---

### Step 3: Depth 1
- Queue: `[Node 2, Node 3]`.
- Record leftmost: $ans \leftarrow 2$.
- Dequeue 2: enqueues 4.
- Dequeue 3: enqueues 5, 6.
- Next level queue: `[Node 4, Node 5, Node 6]`.

---

### Step 4: Depth 2
- Queue: `[Node 4, Node 5, Node 6]`.
- Record leftmost: $ans \leftarrow 4$.
- Dequeue 4: no children.
- Dequeue 5: enqueues 7.
- Dequeue 6: no children.
- Next level queue: `[Node 7]`.

---

### Step 5: Depth 3 (Deepest Row)
- Queue: `[Node 7]`.
- Record leftmost:
  $$
  ans \leftarrow \mathbf{7}
  $$
- Dequeue 7: no children.
- Queue becomes empty `[]`.

---

### Final Output:
$$
ans = \mathbf{7}
$$

---

## 4. Complete Execution Trace

| Level / Depth | Queue at Start of Level | Leftmost Node ($q[0].val$) | Nodes Dequeued | Children Enqueued |
|:---:|:---:|:---:|:---:|:---:|
| **Level 0** | `[1]` | $1$ | $1$ | $2, 3$ |
| **Level 1** | `[2, 3]` | $2$ | $2, 3$ | $4, 5, 6$ |
| **Level 2** | `[4, 5, 6]` | $4$ | $4, 5, 6$ | $7$ |
| **Level 3** | `[7]` | **$7$** | $7$ | None |
| **Complete** | `[]` | — | — | **Result: $7$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node Tree ($[1]$):** Queue has 1 element, runs 1 level $\implies \mathbf{1}$.
- **Degenerate Left Line ($1 \to 2 \to 3$):** Each level has 1 node $\implies$ returns deepest node $\mathbf{3}$.
- **Degenerate Right Line ($1 \to 2 \to 3$):** Each level has 1 node $\implies$ returns deepest node $\mathbf{3}$ (only node in that row).
- **Deepest Node on the Right Side:** If left subtree has depth 2 and right subtree has depth 4, the deepest row is solely in the right subtree, and its leftmost node is correctly selected.

---

## 6. Traps & Common Anti-Patterns

- **Traversing Pure Left Pointers (`while node.left: node = node.left`):** If the deepest node is inside the right subtree (like node 7 in our example), following left pointers from the root leads to node 4 (depth 2), completely missing node 7 (depth 3). Full BFS or depth-tracking DFS is required.
- **Enqueueing Right Child Before Left Child:** If you enqueue $u.right$ before $u.left$, the queue is reversed, and $q[0]$ becomes the rightmost node instead of the leftmost.
- **Using Unbounded Recursion without Depth Tracking:** In DFS, returning the leftmost node requires explicitly passing `(depth, col)` and only updating the answer when a strictly greater depth is seen for the first time. BFS naturally orders by depth without manual depth counters.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - BFS visits every node and edge in the binary tree exactly once.
  - Enqueue and dequeue operations take $O(1)$ amortized time.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 4$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(W)$ where $W$ is the maximum width of the binary tree ($W \le N / 2$ for balanced trees) to store the queue.