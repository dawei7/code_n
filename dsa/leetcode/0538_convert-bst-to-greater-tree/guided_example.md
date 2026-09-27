# Guided Example: Convert BST to Greater Tree

We trace the step-by-step reverse in-order depth-first traversal ($Right \to Root \to Left$), monotonic descending key sequence generation, running suffix sum accumulation ($s \mathrel{+}= root.val$), in-place node value overwrite ($root.val \leftarrow s$), and Greater Tree transformation on representative binary search trees:

- **Input:** $root = [4, 1, 6, 0, 2, 5, 7, \text{null}, \text{null}, \text{null}, 3, \text{null}, \text{null}, \text{null}, 8]$
  - Original tree nodes: $\{0, 1, 2, 3, 4, 5, 6, 7, 8\}$
- **Required output:**
  Level-order serialization: `[30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8]`
  - Greater Tree rule: Each node's new value equals its original value plus the sum of **all nodes strictly greater than it** in the BST.
- **Reverse In-Order Traversal Invariant:**
  - Standard in-order traversal ($L \to Node \to R$) visits nodes in ascending order:
    $$
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    $$
  - **Reverse in-order traversal ($R \to Node \to L$)** visits nodes in **strictly descending order**:
    $$
    [8, 7, 6, 5, 4, 3, 2, 1, 0]
    $$
  - In descending order, all nodes visited *prior* to node $u$ are guaranteed to be greater than $u$.
  - Therefore, maintaining a single running sum $s$ across the reverse traversal transforms each node value in-place!
- **Step-by-step reverse in-order execution trace:**
  - Initialize global accumulator: $s = 0$.
  - **Node 8 (Rightmost leaf, maximum value):**
    - $s \leftarrow 0 + 8 = \mathbf{8}$
    - Overwrite: $root.val \leftarrow \mathbf{8}$.
  - **Node 7:**
    - $s \leftarrow 8 + 7 = \mathbf{15}$
    - Overwrite: $root.val \leftarrow \mathbf{15}$.
  - **Node 6:**
    - $s \leftarrow 15 + 6 = \mathbf{21}$
    - Overwrite: $root.val \leftarrow \mathbf{21}$.
  - **Node 5:**
    - $s \leftarrow 21 + 5 = \mathbf{26}$
    - Overwrite: $root.val \leftarrow \mathbf{26}$.
  - **Node 4 (Tree Root):**
    - $s \leftarrow 26 + 4 = \mathbf{30}$
    - Overwrite: $root.val \leftarrow \mathbf{30}$.
  - **Node 3:**
    - $s \leftarrow 30 + 3 = \mathbf{33}$
    - Overwrite: $root.val \leftarrow \mathbf{33}$.
  - **Node 2:**
    - $s \leftarrow 33 + 2 = \mathbf{35}$
    - Overwrite: $root.val \leftarrow \mathbf{35}$.
  - **Node 1:**
    - $s \leftarrow 35 + 1 = \mathbf{36}$
    - Overwrite: $root.val \leftarrow \mathbf{36}$.
  - **Node 0 (Leftmost leaf, minimum value):**
    - $s \leftarrow 36 + 0 = \mathbf{36}$
    - Overwrite: $root.val \leftarrow \mathbf{36}$.
  - Traversal finishes.
  - All nodes updated in-place with exact cumulative suffix sums.
- **Small Tree Instance ($root = [0, \text{null}, 1]$):**
  - Reverse in-order: Node 1 $\to s = 1$, Node 0 $\to s = 1 + 0 = 1 \implies [1, \text{null}, 1]$.
- **Single Node Tree ($root = [5]$):**
  - $s = 5 \implies [5]$.
- **Empty Tree ($root = \text{null}$):**
  - Returns `null`.

This instance demonstrates symmetric duality between prefix and suffix sums over ordered tree structures, mathematically proves why reverse in-order visitation guarantees single-pass prefix updates, and derives $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a Binary Search Tree (BST):
Convert it into a **Greater Tree** such that every key in the original tree is updated to:
$$
\text{New Value} = \text{Original Value} + \sum_{k > \text{Original Value}} k
$$
Return the modified root node.

```text
Original BST:
          4
        /   \
       1     6
      / \   / \
     0   2 5   7
          \     \
           3     8

Reverse In-Order Order (R -> Root -> L):
  8, 7, 6, 5, 4, 3, 2, 1, 0

Running Sum Accumulation:
  s = 8  -> Node 8 becomes 8
  s = 15 -> Node 7 becomes 15
  s = 21 -> Node 6 becomes 21
  s = 26 -> Node 5 becomes 26
  s = 30 -> Node 4 becomes 30
  s = 33 -> Node 3 becomes 33
  s = 35 -> Node 2 becomes 35
  s = 36 -> Node 1 becomes 36
  s = 36 -> Node 0 becomes 36
```

### Why Reverse In-Order Traversal Works
- Standard In-Order ($Left \to Root \to Right$) visits nodes in **ascending** order ($A_1 \le A_2 \le \dots \le A_n$).
- Reverse In-Order ($Right \to Root \to Left$) visits nodes in **descending** order ($A_n \ge A_{n-1} \ge \dots \ge A_1$).
- When visiting a node in descending order, **every node strictly greater than it has already been visited**.
- By maintaining a running sum $s$:
  - Every time we arrive at a node, $s$ contains the sum of all strictly greater nodes.
  - Adding the current node's value to $s$ produces its exact updated value!

---

## 2. Conceptual Foundation & Invariants

### 1. Reverse In-Order DFS Formulation:
Function $dfs(root)$:
- If $root$ is `None`: return.
- 1. Recurse right:
  $$
  dfs(root.right)
  $$
- 2. Accumulate current value:
  $$
  s \leftarrow s + root.val
  $$
- 3. Overwrite current node value:
  $$
  root.val \leftarrow s
  $$
- 4. Recurse left:
  $$
  dfs(root.left)
  $$

> **Descending Prefix Invariant.** Because reverse in-order traversal visits nodes in monotonically decreasing key order, the cumulative sum $s$ at step $k$ is identically the suffix sum $\sum_{i=k}^n val_i$ of the sorted tree sequence.

---

## 3. Step-by-Step Worked Execution

We trace the sub-branch $4 \to 6 \to 7 \to 8$:

---

### Step 1: Descend Right
From Root 4, traverse down right spine: $4 \to 6 \to 7 \to 8$.
Node 8 has no right child.

---

### Step 2: Process Node 8
- $s \leftarrow 0 + 8 = \mathbf{8}$.
- $root.val \leftarrow \mathbf{8}$.
- Recurse left of 8 (None). Return to Node 7.

---

### Step 3: Process Node 7
- $s \leftarrow 8 + 7 = \mathbf{15}$.
- $root.val \leftarrow \mathbf{15}$.
- Recurse left of 7 (None). Return to Node 6.

---

### Step 4: Process Node 6
- $s \leftarrow 15 + 6 = \mathbf{21}$.
- $root.val \leftarrow \mathbf{21}$.
- Recurse left child of 6 (Node 5):
  - Node 5 has no right child.
  - $s \leftarrow 21 + 5 = \mathbf{26}$.
  - Node 5 becomes $26$.
- Return to Root 4.

---

### Step 5: Process Root 4
- $s \leftarrow 26 + 4 = \mathbf{30}$.
- Root 4 becomes $30$.
- Recurse into left subtree of 4 (Nodes 1, 2, 3, 0).
- Sequence continues until all nodes are updated.

---

## 4. Complete Execution Trace

| Reverse Step | Node Visited | Old $root.val$ | Prior Running Sum | New Running Sum $s$ | New $root.val$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$1$** | $8$ | $8$ | $0$ | $0 + 8 = 8$ | **$8$** |
| **$2$** | $7$ | $7$ | $8$ | $8 + 7 = 15$ | **$15$** |
| **$3$** | $6$ | $6$ | $15$ | $15 + 6 = 21$ | **$21$** |
| **$4$** | $5$ | $5$ | $21$ | $21 + 5 = 26$ | **$26$** |
| **$5$** | $4$ | $4$ | $26$ | $26 + 4 = 30$ | **$30$** |
| **$6$** | $3$ | $3$ | $30$ | $30 + 3 = 33$ | **$33$** |
| **$7$** | $2$ | $2$ | $33$ | $33 + 2 = 35$ | **$35$** |
| **$8$** | $1$ | $1$ | $35$ | $35 + 1 = 36$ | **$36$** |
| **$9$** | $0$ | $0$ | $36$ | $36 + 0 = 36$ | **$36$** |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = \text{None}$):** Returns `None`.
- **Single Node Tree ($root = [10]$):** $s \leftarrow 0 + 10 = 10 \implies [10]$.
- **Skewed Line Left Tree ($3 \to 2 \to 1$):** Traverses $3$, then $2$, then $1$. Sums accumulate $3 \to 5 \to 6$.
- **Negative Node Values:** Accumulator handles negative numbers correctly (e.g. adding $-5$ decreases $s$).

---

## 6. Traps & Common Anti-Patterns

- **Visiting Left Before Right:** Standard in-order traversal ($Left \to Root \to Right$) visits the smallest elements first, requiring a second pass or sum-precomputation. Reverse in-order ($Right \to Root \to Left$) visits the largest elements first, solving the problem in a single pass.
- **Overwriting Node Value Before Accumulating:** If you write `root.val = s` before `s += root.val`, the node's own value is omitted and $s$ fails to advance.
- **Allocating New Trees:** The transformation can be performed strictly in-place on the existing nodes, saving memory.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Reverse in-order traversal visits each of the $N$ nodes exactly once.
  - At each node, arithmetic addition and pointer updates take $O(1)$ operations.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ call stack space where $H$ is the tree height ($O(\log N)$ average, $O(N)$ worst-case). Zero additional tree allocations.
