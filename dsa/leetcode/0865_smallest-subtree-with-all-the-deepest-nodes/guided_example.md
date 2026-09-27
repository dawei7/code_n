# Guided Example: Smallest Subtree with All the Deepest Nodes

We trace the step-by-step bottom-up postorder tree traversal, subtree depth measurement, lowest common ancestor (LCA) convergence, and subproblem return tuple propagation on representative binary trees:

- **Input:**
  $$
  root = [3, 5, 1, 6, 2, 0, 8, \text{null}, \text{null}, 7, 4]
  $$
- **Required output:** `[2, 7, 4]`
  - Tree topology and depth evaluation:
    - Root $3$ (depth 0):
      - Left child $5$ (depth 1):
        - Left child $6$ (depth 2, leaf).
        - Right child $2$ (depth 2):
          - Left child $7$ (depth 3, leaf).
          - Right child $4$ (depth 3, leaf).
      - Right child $1$ (depth 1):
        - Left child $0$ (depth 2, leaf).
        - Right child $8$ (depth 2, leaf).
    - Maximum depth in tree: depth $3$.
    - The deepest nodes are $7$ and $4$.
    - Smallest subtree containing all deepest nodes:
      - Node $7$ is contained in subtrees rooted at $7, 2, 5, 3$.
      - Node $4$ is contained in subtrees rooted at $4, 2, 5, 3$.
      - The intersection of containing subtrees is $\{2, 5, 3\}$.
      - The smallest (deepest) among these is the subtree rooted at **Node 2**.
      - Serialized subtree: **`[2, 7, 4]`**.
- **Bottom-Up Depth & LCA Invariant:**
  - **The Lowest Common Ancestor Equivalence:**
    - The smallest subtree containing all deepest nodes is mathematically equivalent to the **Lowest Common Ancestor (LCA)** of all deepest nodes!
  - **The Dual-Value Postorder Return Tuple:**
    - In a single bottom-up pass, each node queries its left and right subtrees.
    - Each call returns a tuple $(\text{node}, \text{depth})$ representing:
      1. $\text{depth}$: The maximum leaf depth reachable from this subtree.
      2. $\text{node}$: The LCA of the deepest leaves within this subtree.
  - **Convergence Cases:**
    - **Case 1 ($left\_depth > right\_depth$):**
      - All globally deepest nodes in this subtree lie exclusively on the left side.
      - The right subtree cannot contribute to the deepest set.
      - Propagate: $(left\_node, left\_depth + 1)$.
    - **Case 2 ($right\_depth > left\_depth$):**
      - All globally deepest nodes lie exclusively on the right side.
      - Propagate: $(right\_node, right\_depth + 1)$.
    - **Case 3 ($left\_depth == right\_depth$):**
      - Deepest nodes are found at equal maximum depth on both left and right sides (or the node is a leaf with $0 == 0$).
      - Therefore, the current node is the lowest common ancestor joining both sides!
      - Propagate: $(current\_node, left\_depth + 1)$.

---

## 1. Instance & Teaching Goal

Given the tree rooted at $3$, identify the root of the minimal subtree containing all deepest nodes.

```text
                 3 (depth: 4, lca: 2)
               /   \
 (depth: 3)  5       1 (depth: 2)
  (lca: 2)  / \     / \
           6   2   0   8
     (d:1)    / \      (d:1, each)
             7   4
           (d:1, d:1)

Under Node 2:
  left_depth(7) = 1, right_depth(4) = 1 -> Equal!
  -> Node 2 is the LCA with depth 2.

Under Node 5:
  left_depth(6) = 1, right_depth(2) = 2 -> right is deeper!
  -> Propagates (Node 2, depth 3).

Under Node 3:
  left_depth(5) = 3, right_depth(1) = 2 -> left is deeper!
  -> Propagates (Node 2, depth 4).

Root result: Node 2!
```

The teaching goal is to demonstrate how bottom-up synthesis resolves LCA without requiring prior knowledge of the maximum tree height or multi-pass node collection.

---

## 2. Conceptual Foundation & Invariants

### 1. Recursive Function Contract:
$$
\text{dfs}(u) \longrightarrow (\text{LCA}, \text{height})
$$
- Base case:
  $$
  \text{dfs}(\text{null}) = (\text{null}, 0)
  $$
- Induction step for node $u$:
  $$
  (L, ld) = \text{dfs}(u.left), \quad (R, rd) = \text{dfs}(u.right)
  $$
  $$
  \text{dfs}(u) = \begin{cases}
  (L, ld + 1) & \text{if } ld > rd \\
  (R, rd + 1) & \text{if } rd > ld \\
  (u, ld + 1) & \text{if } ld = rd
  \end{cases}
  $$

---

## 3. Step-by-Step Worked Execution

We trace the postorder traversal from the leaves up to root $3$:

---

### Step 1: Leaves $7$ and $4$
- **At Node $7$:**
  - $\text{left} = \text{null} \implies 0, \quad \text{right} = \text{null} \implies 0$.
  - Depths equal ($0 == 0$) $\implies$ returns $(7, 1)$.
- **At Node $4$:**
  - Depths equal ($0 == 0$) $\implies$ returns $(4, 1)$.

---

### Step 2: Node $2$
- Left return: $(7, 1) \implies ld = 1, L = 7$.
- Right return: $(4, 1) \implies rd = 1, R = 4$.
- Compare depths:
  $$
  ld == rd = 1
  $$
- Both branches contain leaves at the same maximum depth.
- **Node $2$ becomes the LCA!**
- Returns: $(2, 1 + 1) = \mathbf{(2, 2)}$.

---

### Step 3: Node $6$
- Leaf node $\implies$ returns $(6, 1)$.

---

### Step 4: Node $5$
- Left return: $(6, 1) \implies ld = 1, L = 6$.
- Right return: $(2, 2) \implies rd = 2, R = 2$.
- Compare depths:
  $$
  rd = 2 > ld = 1
  $$
- The right branch contains strictly deeper nodes ($2$ contains nodes at depth 3; $6$ is only depth 2).
- **LCA remains $R = 2$.**
- Returns: $(2, rd + 1) = \mathbf{(2, 3)}$.

---

### Step 5: Subtree of Node $1$
- At $0$: leaf $\implies (0, 1)$.
- At $8$: leaf $\implies (8, 1)$.
- At Node $1$: $ld = 1, rd = 1 \implies$ returns $(1, 2)$.

---

### Step 6: Tree Root $3$
- Left return (from $5$): $(2, 3) \implies ld = 3, L = 2$.
- Right return (from $1$): $(1, 2) \implies rd = 2, R = 1$.
- Compare depths:
  $$
  ld = 3 > rd = 2
  $$
- The left branch is strictly deeper than the right branch ($3 > 2$).
- **LCA remains $L = 2$.**
- Returns: $(2, ld + 1) = \mathbf{(2, 4)}$.

---

### Conclusion:
The root returns $(2, 4)$. The LCA node is **Node 2**.
Subtree output: **`[2, 7, 4]`**.

---

## 4. Complete Execution Trace

| Node Visited | Left Child Return $(L, ld)$ | Right Child Return $(R, rd)$ | Depth Comparison | Decided LCA Candidate | Propagated Tuple |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $7$ | $(\text{null}, 0)$ | $(\text{null}, 0)$ | $0 == 0$ | $7$ | $(7, 1)$ |
| $4$ | $(\text{null}, 0)$ | $(\text{null}, 0)$ | $0 == 0$ | $4$ | $(4, 1)$ |
| **$2$** | $(7, 1)$ | $(4, 1)$ | **$1 == 1$** | **$2$** | **$(2, 2)$** |
| $6$ | $(\text{null}, 0)$ | $(\text{null}, 0)$ | $0 == 0$ | $6$ | $(6, 1)$ |
| $5$ | $(6, 1)$ | $(2, 2)$ | $2 > 1$ (Right deeper) | $2$ | $(2, 3)$ |
| $0$ | $(\text{null}, 0)$ | $(\text{null}, 0)$ | $0 == 0$ | $0$ | $(0, 1)$ |
| $8$ | $(\text{null}, 0)$ | $(\text{null}, 0)$ | $0 == 0$ | $8$ | $(8, 1)$ |
| $1$ | $(0, 1)$ | $(8, 1)$ | $1 == 1$ | $1$ | $(1, 2)$ |
| **$3$ (Root)** | $(2, 3)$ | $(1, 2)$ | **$3 > 2$ (Left deeper)** | **$2$** | **$(2, 4)$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node Tree ($root = [1]$):** Leaf at depth 1. Returns $(1, 1) \implies [1]$.
- **Degenerate Linked-List Tree (Single Branch):** Every node has only one child; the lone deepest leaf is itself returned as the LCA.
- **Deepest Leaves in Opposite Subtrees of Root:** Left depth equals right depth at root $\implies$ root itself is the answer.

---

## 6. Traps & Common Anti-Patterns

- **Multi-Pass Tree Traversal:** Doing one pass to find max depth, a second pass to collect all deepest nodes, and a third pass to compute their LCA requires $\mathcal{O}(N)$ memory and three separate traversals. Single-pass bottom-up postorder computes depth and LCA simultaneously.
- **Returning Depth from Root Instead of Subtree Height:** Calculating global depth top-down prevents natural bottom-up subtree comparisons; height (distance to deepest leaf below) naturally aggregates bottom-up.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard postorder DFS visits each node in the binary tree exactly once: $\mathcal{O}(N)$.
  - Fixed number of comparisons and additions per node: $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(N)$, executing in $< 2$ ms for $N \le 500$.
- **Auxiliary Space Complexity:**
  - Call stack bounded by maximum tree height $H$: $\mathcal{O}(H)$, which is $\mathcal{O}(\log N)$ for balanced trees and $\mathcal{O}(N)$ in the worst-case degenerate chain.
