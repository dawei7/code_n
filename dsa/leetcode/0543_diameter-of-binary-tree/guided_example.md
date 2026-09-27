# Guided Example: Diameter of Binary Tree

We trace the step-by-step bottom-up post-order depth-first search, left and right subtree height extraction ($l = dfs(left), \; r = dfs(right)$), local turning-point diameter aggregation ($l + r$), global maximum diameter tracking ($ans = \max(ans, l + r)$), and 1-hop parent depth contribution ($1 + \max(l, r)$) on representative binary trees:

- **Input:** $root = [1, 2, 3, 4, 5]$
  - Tree topology:
    - Root $1$ has left child $2$ and right child $3$.
    - Node $2$ has left child $4$ and right child $5$.
    - Nodes $4, 5, 3$ are leaves.
- **Required output:** `3`
  - Diameter definition: The **number of edges** on the longest simple path between any two nodes in the tree.
  - Key structural property: The longest path does **not** necessarily pass through the global root; it may be contained entirely within a deep subtree.
- **Post-Order Subtree Depth Trace:**
  - Let $dfs(node)$ return the maximum number of edges from $node$ down to any leaf in its subtree.
  - Base case: If $node$ is `None`, depth is $0$.
  - For any node, the longest path that uses $node$ as its highest turning point has length:
    $$
    \text{local diameter} = l + r
    $$
    where $l = dfs(node.left)$ and $r = dfs(node.right)$.
  - **Node 4 (Leaf):**
    - $dfs(None) = 0, \; dfs(None) = 0$.
    - Local diameter: $l + r = 0 + 0 = 0$.
    - Return depth to parent: $1 + \max(0, 0) = \mathbf{1}$.
  - **Node 5 (Leaf):**
    - $l = 0, \; r = 0 \implies l + r = 0$.
    - Return depth to parent: $1 + \max(0, 0) = \mathbf{1}$.
  - **Node 2:**
    - Left child depth (Node 4): $l = 1$.
    - Right child depth (Node 5): $r = 1$.
    - Local diameter using Node 2 as apex:
      $$
      l + r = 1 + 1 = \mathbf{2}
      $$
      *(Path: $4 \to 2 \to 5$, length 2 edges)*
    - Update global maximum: $ans \leftarrow \max(0, 2) = \mathbf{2}$.
    - Return depth to parent:
      $$
      1 + \max(1, 1) = 1 + 1 = \mathbf{2}
      $$
  - **Node 3 (Leaf):**
    - $l = 0, \; r = 0 \implies l + r = 0$.
    - Return depth to parent: $1 + \max(0, 0) = \mathbf{1}$.
  - **Node 1 (Root):**
    - Left child depth (Node 2): $l = 2$.
    - Right child depth (Node 3): $r = 1$.
    - Local diameter using Node 1 as apex:
      $$
      l + r = 2 + 1 = \mathbf{3}
      $$
      *(Path: $4 \to 2 \to 1 \to 3$ or $5 \to 2 \to 1 \to 3$, length 3 edges)*
    - Update global maximum:
      $$
      ans \leftarrow \max(2, 3) = \mathbf{3}
      $$
    - Return depth: $1 + \max(2, 1) = 3$.
  - Post-order traversal complete.
  - Final global diameter: **`3`**.
- **Off-Root Diameter Instance:**
  - Suppose a deep subtree has left depth 4 and right depth 4 ($diameter = 8$), while the root's right child has depth 0 ($diameter at root = 5$).
  - The algorithm evaluates $l + r$ at every node $\implies$ correctly identifies $8$ in the subtree!
- **Two-Node Tree ($root = [1, 2]$):**
  - Node 2 has depth 1, Node 1 has $l = 1, r = 0 \implies 1 + 0 = \mathbf{1}$.
- **Single Node Tree ($root = [1]$):**
  - $l = 0, r = 0 \implies ans = \mathbf{0}$.

This instance demonstrates tree diameter decomposition via dynamic programming over tree heights, mathematically proves why updating $ans = \max(ans, l + r)$ at every node captures off-root maxima, and derives $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
Return the **length of the diameter** of the tree.
The diameter is the length of the longest path between any two nodes, measured in **edges**.

```text
Tree:
        1
       / \
      2   3
     / \
    4   5

Longest Path:
    4 -> 2 -> 1 -> 3   (or 5 -> 2 -> 1 -> 3)
Edges counted: (4-2), (2-1), (1-3) -> 3 edges

Diameter = 3
```

### The Subtree Turning Point Theorem
- Any simple path in a binary tree has a unique highest node (the Lowest Common Ancestor of the path's endpoints), called its **turning point** (or apex).
- For a turning point node $u$:
  - The longest path turning at $u$ consists of:
    - The deepest path down its left subtree (length $l$).
    - The deepest path down its right subtree (length $r$).
  - Total edges: $l + r$.
- Because every possible path in the tree has some node as its apex, the global diameter is simply:
  $$
  \text{Diameter} = \max_{u \in \text{Tree}} (depth(u.left) + depth(u.right))
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. Depth Definition:
Let $dfs(node)$ return the maximum number of edges from $node$ down to any leaf in its subtree:
- If $node$ is `None`: return 0.
- Otherwise:
  $$
  depth(node) = 1 + \max(depth(node.left), \; depth(node.right))
  $$

### 2. Post-Order Maximum Diameter Aggregation:
During the bottom-up calculation of $dfs(node)$:
1. $l = dfs(node.left)$
2. $r = dfs(node.right)$
3. Update global maximum:
   $$
   ans \leftarrow \max(ans, \; l + r)
   $$
4. Return $1 + \max(l, r)$ to the parent.

> **Turning-Point Exhaustion Invariant.** Because post-order DFS visits every node $u$ after fully resolving its children, evaluating $l + r$ at every step considers all possible turning points in the tree.

---

## 3. Step-by-Step Worked Execution

We trace $root = [1, 2, 3, 4, 5]$:

---

### Step 1: Initialize
- $ans = 0$.

---

### Step 2: Bottom-Up Post-Order DFS

1. **Leaf Node 4:**
   - $l = 0, \; r = 0$.
   - $ans = \max(0, 0 + 0) = 0$.
   - Return: $1 + \max(0, 0) = \mathbf{1}$.

2. **Leaf Node 5:**
   - $l = 0, \; r = 0$.
   - $ans = \max(0, 0 + 0) = 0$.
   - Return: $1 + \max(0, 0) = \mathbf{1}$.

3. **Node 2:**
   - Receives from left (Node 4): $l = 1$.
   - Receives from right (Node 5): $r = 1$.
   - Path through Node 2:
     $$
     l + r = 1 + 1 = \mathbf{2}
     $$
   - $ans \leftarrow \max(0, 2) = \mathbf{2}$.
   - Return to parent: $1 + \max(1, 1) = \mathbf{2}$.

4. **Leaf Node 3:**
   - $l = 0, \; r = 0 \implies ans = 2$.
   - Return: $1 + \max(0, 0) = \mathbf{1}$.

5. **Root Node 1:**
   - Receives from left (Node 2): $l = 2$.
   - Receives from right (Node 3): $r = 1$.
   - Path through Node 1:
     $$
     l + r = 2 + 1 = \mathbf{3}
     $$
   - $ans \leftarrow \max(2, 3) = \mathbf{3}$.
   - Return: $1 + \max(2, 1) = 3$.

---

### Step 3: Result
$$
ans = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Node Visited | Left Depth $l$ | Right Depth $r$ | Path Length $l + r$ | Running Max $ans$ | Returned Depth $1 + \max(l, r)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Node 4 | $0$ | $0$ | $0$ | $0$ | $1$ |
| Node 5 | $0$ | $0$ | $0$ | $0$ | $1$ |
| **Node 2** | $1$ | $1$ | **$2$** | **$2$** | $2$ |
| Node 3 | $0$ | $0$ | $0$ | $2$ | $1$ |
| **Node 1** | $2$ | $1$ | **$3$** | **$3$** | $3$ |
| **Done** | — | — | — | — | **Result: $3$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node ($root = [1]$):** $l = 0, r = 0 \implies ans = 0$ (0 edges).
- **Two Nodes ($root = [1, 2]$):** Node 2 has depth 1, Node 1 has $l = 1, r = 0 \implies ans = 1$.
- **Diameter Does Not Pass Through Root:**
  ```text
            1
           /
          2
         / \
        3   4
       /     \
      5       6
  ```
  Path $5 \to 3 \to 2 \to 4 \to 6$ has length 4, while any path through root 1 has length at most 3. The algorithm evaluates $2 + 2 = 4$ at Node 2, correctly discovering the off-root diameter.

---

## 6. Traps & Common Anti-Patterns

- **Assuming Diameter Always Passes Through the Root:** Restricting the calculation to `dfs(root.left) + dfs(root.right)` misses cases where a deep branch contains the entire diameter. Global tracking across all nodes via `ans = max(ans, l + r)` is mandatory.
- **Counting Nodes Instead of Edges:** A path with $k$ nodes contains $k - 1$ edges. The base case $dfs(None) = 0$ and adding $l + r$ directly counts edges.
- **Double Traversal ($O(N^2)$):** Computing height separately for every node causes quadratic runtime. A single bottom-up post-order pass computes heights and the diameter simultaneously in $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Post-order DFS visits each node in the tree exactly once.
  - At each node, computing the maximum of two numbers and integer addition takes $O(1)$ operations.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ call stack space where $H$ is the tree height ($O(\log N)$ balanced, $O(N)$ worst-case).