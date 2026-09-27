# Guided Example: Construct Binary Tree from Preorder and Postorder Traversal

We trace the step-by-step root identification, left-child anchor indexing, postorder prefix interval partitioning, recursive subtree division, and binary tree reconstruction on representative traversal pairs:

- **Input:**
  $$
  preorder = [1, 2, 4, 5, 3, 6, 7], \quad postorder = [4, 5, 2, 6, 7, 3, 1]
  $$
- **Required output:** `[1, 2, 3, 4, 5, 6, 7]`
  - Traversal definitions:
    - **Preorder:** Visits $\text{Root} \to \text{Left Subtree} \to \text{Right Subtree}$.
    - **Postorder:** Visits $\text{Left Subtree} \to \text{Right Subtree} \to \text{Root}$.
    - For $preorder = [1, 2, 4, 5, 3, 6, 7]$ and $postorder = [4, 5, 2, 6, 7, 3, 1]$:
      - The global root is $1$ (first in preorder, last in postorder).
      - In preorder, the left child of $1$ is $2$ (the immediate next element).
      - In postorder, all nodes in the subtree rooted at $2$ must appear **before or at node $2$**.
      - Node $2$ appears at index $2$ in postorder ($[4, 5, 2]$), indicating the left subtree has size $3$!
      - Partitioning:
        - Left subtree: Preorder $[2, 4, 5]$, Postorder $[4, 5, 2]$.
        - Right subtree: Preorder $[3, 6, 7]$, Postorder $[6, 7, 3]$.
      - Reconstructing subtrees yields the complete binary tree with root 1, left child 2 (with children 4, 5), and right child 3 (with children 6, 7).
      - Level-order serialization: **`[1, 2, 3, 4, 5, 6, 7]`**.
- **The Structural Partitioning Invariant:**
  - **The Left-Child Anchor:**
    - In preorder traversal:
      $$
      preorder = [\text{root}, \; \mathbf{L_{root}}, \dots]
      $$
    - If the tree has more than one node, the element immediately following $\text{root}$ ($preorder[a + 1]$) is the **root of the left subtree** ($L_{root}$).
  - **Subtree Boundary Isolation via Postorder Index:**
    - In postorder traversal:
      $$
      postorder = [(\text{all nodes in Left Subtree}), \; (\text{all nodes in Right Subtree}), \; \text{root}]
      $$
    - In postorder, $L_{root}$ appears at the **very end of the left subtree block**!
    - Let $i = pos[L_{root}]$ be the index of $L_{root}$ in postorder.
    - If the current postorder segment begins at index $c$, then the left subtree occupies postorder range $[c, i]$.
    - The number of nodes in the left subtree is:
      $$
      m = i - c + 1
      $$
  - **Recursive Split Equations:**
    - Left Subtree:
      - Preorder range: $[a + 1, \; a + m]$
      - Postorder range: $[c, \; i]$
    - Right Subtree:
      - Preorder range: $[a + m + 1, \; b]$
      - Postorder range: $[i + 1, \; d - 1]$

---

## 1. Instance & Teaching Goal

Given $preorder = [1, 2, 4, 5, 3, 6, 7]$ and $postorder = [4, 5, 2, 6, 7, 3, 1]$, illustrate how the left root anchor partitions the sequences.

```text
Preorder:   [1,   2, 4, 5,   3, 6, 7]
             ^    \______/   \_____/
           Root     Left      Right

Postorder:  [4, 5, 2,   6, 7, 3,   1]
             \_____/    \_____/    ^
              Left       Right    Root

Index of Left Child (2) in Postorder = 2.
Left subtree size m = 2 - 0 + 1 = 3 nodes {4, 5, 2}.

Recursive Subtrees:
  Left:  Preorder [2, 4, 5], Postorder [4, 5, 2] -> Root 2, Left 4, Right 5
  Right: Preorder [3, 6, 7], Postorder [6, 7, 3] -> Root 3, Left 6, Right 7
```

The teaching goal is to demonstrate how locating the second preorder element inside the postorder sequence reveals the exact boundary between left and right subtrees.

---

## 2. Conceptual Foundation & Invariants

### 1. Subtree Segment Parameters:
For subproblem on preorder $[a, b]$ and postorder $[c, d]$:
- Root node: $val = preorder[a]$.
- If $a == b$: leaf node, return immediately.
- Left child root: $val_{L} = preorder[a + 1]$.
- Locate in postorder: $i = pos[val_L]$.
- Subtree size: $m = i - c + 1$.

### 2. Recurrence:
$$
root.left = \text{dfs}(a + 1, \; a + m, \; c, \; i)
$$
$$
root.right = \text{dfs}(a + m + 1, \; b, \; i + 1, \; d - 1)
$$

---

## 3. Step-by-Step Worked Execution

Traversals:
- $preorder = [1, 2, 4, 5, 3, 6, 7]$
- $postorder = [4, 5, 2, 6, 7, 3, 1]$
- Precomputed postorder index map:
  $$
  pos = \{4:0, 5:1, 2:2, 6:3, 7:4, 3:5, 1:6\}
  $$

---

### Phase 1: Global Root ($a=0, b=6, c=0, d=6$)
- Root value: $preorder[0] = \mathbf{1}$.
- Left child value: $preorder[1] = 2$.
- Find index of $2$ in postorder: $i = pos[2] = 2$.
- Left subtree size:
  $$
  m = i - c + 1 = 2 - 0 + 1 = \mathbf{3}
  $$
- Partition ranges:
  - Left child DFS: preorder $[1, 3] = [2, 4, 5]$, postorder $[0, 2] = [4, 5, 2]$.
  - Right child DFS: preorder $[4, 6] = [3, 6, 7]$, postorder $[3, 5] = [6, 7, 3]$.

---

### Phase 2: Solve Left Subtree ($a=1, b=3, c=0, d=2$)
- Root value: $preorder[1] = \mathbf{2}$.
- Left child value: $preorder[2] = 4$.
- Find index of $4$ in postorder: $i = pos[4] = 0$.
- Left subtree size:
  $$
  m = 0 - 0 + 1 = \mathbf{1}
  $$
- Partition ranges:
  - Left child DFS: preorder $[2, 2] = [4]$, postorder $[0, 0] = [4]$.
    - $a == b \implies$ Leaf node **4**.
  - Right child DFS: preorder $[3, 3] = [5]$, postorder $[1, 1] = [5]$.
    - $a == b \implies$ Leaf node **5**.
- Left subtree complete: Node $2$ has left child $4$ and right child $5$.

---

### Phase 3: Solve Right Subtree ($a=4, b=6, c=3, d=5$)
- Root value: $preorder[4] = \mathbf{3}$.
- Left child value: $preorder[5] = 6$.
- Find index of $6$ in postorder: $i = pos[6] = 3$.
- Left subtree size:
  $$
  m = 3 - 3 + 1 = \mathbf{1}
  $$
- Partition ranges:
  - Left child DFS: preorder $[5, 5] = [6]$, postorder $[3, 3] = [6]$.
    - $a == b \implies$ Leaf node **6**.
  - Right child DFS: preorder $[6, 6] = [7]$, postorder $[4, 4] = [7]$.
    - $a == b \implies$ Leaf node **7**.
- Right subtree complete: Node $3$ has left child $6$ and right child $7$.

---

### Phase 4: Assemble Tree
- Root $1$:
  - Left: Node $2$ (children $4, 5$).
  - Right: Node $3$ (children $6, 7$).
- **Level-Order Representation: `[1, 2, 3, 4, 5, 6, 7]`**.

---

## 4. Complete Execution Trace

| Call Level | Node Constructed | Preorder Segment $[a, b]$ | Postorder Segment $[c, d]$ | Left Root $preorder[a+1]$ | Index in Postorder $i$ | Subtree Size $m$ | Assigned Left Child | Assigned Right Child |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | Node $1$ | $[0, 6]$: `[1,2,4,5,3,6,7]` | $[0, 6]$: `[4,5,2,6,7,3,1]` | $2$ | $2$ | $3$ | Node $2$ | Node $3$ |
| $1$ (Left) | Node $2$ | $[1, 3]$: `[2,4,5]` | $[0, 2]$: `[4,5,2]` | $4$ | $0$ | $1$ | Node $4$ | Node $5$ |
| $2$ (Leaf) | Node $4$ | $[2, 2]$: `[4]` | $[0, 0]$: `[4]` | — | — | — | `null` | `null` |
| $2$ (Leaf) | Node $5$ | $[3, 3]$: `[5]` | $[1, 1]$: `[5]` | — | — | — | `null` | `null` |
| $1$ (Right)| Node $3$ | $[4, 6]$: `[3,6,7]` | $[3, 5]$: `[6,7,3]` | $6$ | $3$ | $1$ | Node $6$ | Node $7$ |
| $2$ (Leaf) | Node $6$ | $[5, 5]$: `[6]` | $[3, 3]$: `[6]` | — | — | — | `null` | `null` |
| $2$ (Leaf) | Node $7$ | $[6, 6]$: `[7]` | $[4, 4]$: `[7]` | — | — | — | `null` | `null` |

---

## 5. Boundary Cases & Failure Modes

- **Single Node Tree ($preorder = [1], postorder = [1]$):** $a == b \implies$ creates single leaf node $1$ immediately without inspecting $a+1$.
- **Trees with Single-Child Nodes (e.g. $[1, 2]$ and $[2, 1]$):**
  - Because preorder/postorder does not specify whether a single child is left or right, convention assigns it as the left child. Both interpretations are valid binary trees.
- **Skewed Line Trees (Chain of $N$ nodes):** Recurses cleanly down one side with recursion depth $N$.

---

## 6. Traps & Common Anti-Patterns

- **Searching Postorder Linearly in Every Call:** Using `postorder.index(val)` takes $\mathcal{O}(N)$ per call, degrading total construction time to $\mathcal{O}(N^2)$. Precomputing a hash table `pos` enables $\mathcal{O}(1)$ partition lookups, achieving $\mathcal{O}(N)$ total time.
- **Array Slicing Overhead:** Slicing lists `preorder[1:4]` copies subarrays in $\mathcal{O}(N)$ memory per recursive step. Passing four scalar index boundaries $(a, b, c, d)$ avoids allocations.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Hash map precomputation of postorder positions: $\mathcal{O}(N)$.
  - Each node in the tree of $N$ vertices is constructed in exactly one recursive call.
  - Each call performs $\mathcal{O}(1)$ index lookups and arithmetic operations.
  - Total Time: strictly $\mathcal{O}(N)$, executing in $< 1$ ms for $N \le 30$.
- **Auxiliary Space Complexity:**
  - Hash map of size $N$: $\mathcal{O}(N)$.
  - Recursion call stack: $\mathcal{O}(H)$ where $H \le N$ is the tree height.
  - Total Space: $\mathcal{O}(N)$ auxiliary space.