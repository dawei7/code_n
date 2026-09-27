# Guided Example: Binary Tree Tilt

We trace the step-by-step bottom-up post-order depth-first search, left and right subtree value summation ($l = dfs(left), \; r = dfs(right)$), local tilt evaluation ($|l - r|$), parent subtree sum propagation ($l + r + root.val$), and tree-wide cumulative tilt aggregation on representative binary trees:

- **Input:** $root = [4, 2, 9, 3, 5, \text{null}, 7]$
  - Tree topology:
    - Root Node $4$ has left child Node $2$ and right child Node $9$.
    - Node $2$ has left child Node $3$ and right child Node $5$.
    - Node $9$ has no left child and right child Node $7$.
    - Nodes $3, 5, 7$ are leaves.
- **Required output:** `15`
  - Tilt definition:
    - For any node, $\text{tilt}(node) = |\text{Sum}(node.left) - \text{Sum}(node.right)|$.
    - An empty subtree contributes a sum of $0$.
    - The **tilt of the whole tree** is the sum of the tilts of **every single node**.
- **Bottom-Up Post-Order Traversal Trace:**
  - Let $dfs(node)$ return the sum of all node values in the subtree rooted at $node$:
    $$
    \text{Sum}(node) = \text{Sum}(node.left) + \text{Sum}(node.right) + node.val
    $$
  - While computing sums, accumulate the node's tilt into a global accumulator:
    $$
    ans \leftarrow ans + |l - r|
    $$
  - **Base Case:** $dfs(None) = 0$.
  - **Evaluating Leaf Node 3:**
    - Left sum: $l = 0$, Right sum: $r = 0$.
    - Local tilt:
      $$
      |l - r| = |0 - 0| = \mathbf{0}
      $$
    - Subtree sum returned: $0 + 0 + 3 = \mathbf{3}$.
  - **Evaluating Leaf Node 5:**
    - $l = 0, \; r = 0 \implies \text{tilt} = |0 - 0| = \mathbf{0}$.
    - Subtree sum returned: $0 + 0 + 5 = \mathbf{5}$.
  - **Evaluating Node 2:**
    - Receives from left: $l = 3$.
    - Receives from right: $r = 5$.
    - Local tilt:
      $$
      \text{tilt}(2) = |l - r| = |3 - 5| = \mathbf{2}
      $$
    - Add to global tilt: $ans \leftarrow 0 + 2 = \mathbf{2}$.
    - Subtree sum returned to parent:
      $$
      l + r + node.val = 3 + 5 + 2 = \mathbf{10}
      $$
  - **Evaluating Leaf Node 7:**
    - $l = 0, \; r = 0 \implies \text{tilt} = \mathbf{0}$.
    - Subtree sum returned: $0 + 0 + 7 = \mathbf{7}$.
  - **Evaluating Node 9:**
    - Left child is None: $l = 0$.
    - Right child is Node 7: $r = 7$.
    - Local tilt:
      $$
      \text{tilt}(9) = |l - r| = |0 - 7| = \mathbf{7}
      $$
    - Add to global tilt: $ans \leftarrow 2 + 7 = \mathbf{9}$.
    - Subtree sum returned to parent:
      $$
      l + r + node.val = 0 + 7 + 9 = \mathbf{16}
      $$
  - **Evaluating Root Node 4:**
    - Left subtree sum (from Node 2): $l = 10$.
    - Right subtree sum (from Node 9): $r = 16$.
    - Local tilt:
      $$
      \text{tilt}(4) = |l - r| = |10 - 16| = |-6| = \mathbf{6}
      $$
    - Add to global tilt:
      $$
      ans \leftarrow 9 + 6 = \mathbf{15}
      $$
    - Subtree sum: $10 + 16 + 4 = 30$.
  - Post-order traversal complete.
  - Final tree-wide tilt sum: **`15`**.
- **Minimal Two-Leaf Tree ($root = [1, 2, 3]$):**
  - Node 2: tilt 0, returns 2.
  - Node 3: tilt 0, returns 3.
  - Node 1: tilt $|2 - 3| = \mathbf{1} \implies ans = \mathbf{1}$.
- **Single Node Tree ($root = [1]$):**
  - $l = 0, r = 0 \implies |0 - 0| = \mathbf{0}$.

This instance demonstrates dual-responsibility post-order tree evaluation, mathematically proves why returning subtree sums while aggregating tilts avoids $O(N^2)$ repeated tree traversals, and derives $O(N)$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
Return the **sum of every tree node's tilt**.
The tilt of a node is the **absolute difference** between the sum of all left subtree node values and all right subtree node values.

```text
Tree:
        4
       / \
      2   9
     / \   \
    3   5   7

Subtree Sums:
  Node 3: 3            (Tilt: |0 - 0| = 0)
  Node 5: 5            (Tilt: |0 - 0| = 0)
  Node 7: 7            (Tilt: |0 - 0| = 0)
  Node 2: 3 + 5 + 2 = 10  (Tilt: |3 - 5| = 2)
  Node 9: 0 + 7 + 9 = 16  (Tilt: |0 - 7| = 7)
  Node 4: 10 + 16 + 4 = 30 (Tilt: |10 - 16| = 6)

Total Tilt = 0 + 0 + 0 + 2 + 7 + 6 = 15
```

### Decoupling Tilt Calculation from Traversal
- If we compute the subtree sum independently for every node, each calculation takes $O(N)$, resulting in an inefficient $O(N^2)$ overall runtime.
- By using a **bottom-up post-order DFS**:
  - The function returns the **subtree sum** ($l + r + node.val$) to its parent.
  - Simultaneously, it calculates the **tilt** ($|l - r|$) and accumulates it into a global counter.
  - Every node is processed in $O(1)$ operations, achieving optimal $O(N)$ linear time!

---

## 2. Conceptual Foundation & Invariants

### 1. Subtree Sum Contract:
Function $dfs(node) \to \text{integer}$:
- If $node$ is `None`: return 0.
- Recursively evaluate children:
  $$
  l = dfs(node.left), \quad r = dfs(node.right)
  $$
- Accumulate tilt:
  $$
  ans \leftarrow ans + |l - r|
  $$
- Return total subtree weight:
  $$
  l + r + node.val
  $$

### 2. Post-Order Invariant:
A node's left and right subtree sums are fully determined before its own tilt is computed.

> **Conservation of Subtree Weight Invariant.** The total value returned by $dfs(node)$ is the exact sum of all node values in its subtree, satisfying the recurrence $\text{Sum}(T) = \text{val}(root) + \sum_{c} \text{Sum}(c)$.

---

## 3. Step-by-Step Worked Execution

We trace $root = [4, 2, 9, 3, 5, \text{null}, 7]$:

---

### Step 1: Initialize
- $ans = 0$

---

### Step 2: Post-Order DFS
1. **Node 3:** $l = 0, r = 0 \implies tilt = 0$. Returns $3$.
2. **Node 5:** $l = 0, r = 0 \implies tilt = 0$. Returns $5$.
3. **Node 2:**
   - Left sum $l = 3$, Right sum $r = 5$.
   - $tilt = |3 - 5| = \mathbf{2}$.
   - $ans \leftarrow 0 + 2 = 2$.
   - Returns $3 + 5 + 2 = \mathbf{10}$.
4. **Node 7:** $l = 0, r = 0 \implies tilt = 0$. Returns $7$.
5. **Node 9:**
   - Left sum $l = 0$, Right sum $r = 7$.
   - $tilt = |0 - 7| = \mathbf{7}$.
   - $ans \leftarrow 2 + 7 = 9$.
   - Returns $0 + 7 + 9 = \mathbf{16}$.
6. **Root Node 4:**
   - Left sum $l = 10$, Right sum $r = 16$.
   - $tilt = |10 - 16| = \mathbf{6}$.
   - $ans \leftarrow 9 + 6 = \mathbf{15}$.
   - Returns $10 + 16 + 4 = 30$.

---

### Step 3: Emit Output
$$
ans = \mathbf{15}
$$

---

## 4. Complete Execution Trace

| Node Visited | Node Value | Left Sum $l$ | Right Sum $r$ | Local Tilt $|l - r|$ | Running Total Tilt $ans$ | Returned Subtree Sum |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Node 3 | $3$ | $0$ | $0$ | $0$ | $0$ | $3$ |
| Node 5 | $5$ | $0$ | $0$ | $0$ | $0$ | $5$ |
| **Node 2** | $2$ | $3$ | $5$ | **$2$** | **$2$** | $10$ |
| Node 7 | $7$ | $0$ | $0$ | $0$ | $2$ | $7$ |
| **Node 9** | $9$ | $0$ | $7$ | **$7$** | **$9$** | $16$ |
| **Node 4** | $4$ | $10$ | $16$ | **$6$** | **$15$** | $30$ |
| **Done** | — | — | — | — | **Result: $15$** | — |

---

## 5. Boundary Cases & Failure Modes

- **Empty Tree ($root = None$):** Returns $0$ immediately.
- **Single Node Tree ($root = [10]$):** $l = 0, r = 0 \implies tilt = 0$.
- **Negative Node Values ($[1, -2, -3]$):** Absolute difference $|l - r| = |-2 - (-3)| = |1| = 1$ handles negative integers correctly.
- **Skewed Tree (Linked List of nodes):** Computes prefix/suffix differences along the chain in linear time.

---

## 6. Traps & Common Anti-Patterns

- **Returning the Tilt Instead of the Subtree Sum:** The DFS must return the **sum of node values** to its parent, NOT the tilt! If a function returns the tilt, the parent cannot compute its own subtree sums.
- **Confusing Node Value with Subtree Sum:** Tilt is the difference between the sum of **all nodes** in the left subtree and right subtree, not just the values of the direct children.
- **Recomputing Subtree Sums ($O(N^2)$):** Calling a separate helper `sumTree(node)` inside `findTilt` causes quadratic runtime and TLE. Returning the sum bottom-up maintains strictly linear $O(N)$ execution.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Post-order DFS visits each of the $N$ nodes exactly once.
  - At each node, computing the difference, absolute value, and sum takes $O(1)$ operations.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ call stack space where $H$ is the tree height ($O(\log N)$ balanced, $O(N)$ worst-case).