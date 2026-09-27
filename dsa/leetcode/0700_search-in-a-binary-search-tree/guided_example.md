# Guided Example: Search in a Binary Search Tree

We trace the step-by-step binary search tree directional navigation ($u.val > val \implies \text{left}$, $u.val < val \implies \text{right}$), target equality matching ($u.val == val$), subtree root pointer preservation, search path bisection, and null termination on representative BST query instances:

- **Input:**
  - Tree: $root = [4, 2, 7, 1, 3]$
  - Target value: $val = 2$
  - Tree topology:
    ```text
            4
          /   \
         2     7
        / \
       1   3
    ```
- **Required output:** `[2, 1, 3]`
  - Output subtree:
    ```text
         2
        / \
       1   3
    ```
  - Problem objective:
    - Locate the node with value $val$ within the Binary Search Tree.
    - Return the complete subtree rooted at that node.
    - If the value does not exist anywhere in the tree, return `null`.
- **Binary Search Tree Invariant & Directional Pruning:**
  - **The BST Property:**
    - For every node $u$ in a Binary Search Tree:
      - Every key in the left subtree is strictly less than the node's key:
        $$
        \forall w \in \text{left}(u): \quad w.val < u.val
        $$
      - Every key in the right subtree is strictly greater than the node's key:
        $$
        \forall w \in \text{right}(u): \quad w.val > u.val
        $$
  - **Single-Branch Pruning Decisions:**
    - When comparing current node $u$ with target $val$:
      1. **Match Found ($u.val == val$):**
         - The target node is located! Return node $u$ (along with its entire intact subtree).
      2. **Overshoot ($u.val > val$):**
         - Because all nodes in the right subtree are $> u.val > val$, the target can never exist in the right subtree.
         - Prune the entire right subtree and branch exclusively to the left:
           $$
           \text{search}(u) \leftarrow \text{search}(u.left)
           $$
      3. **Undershoot ($u.val < val$):**
         - All nodes in the left subtree are $< u.val < val$.
         - Prune the entire left subtree and branch exclusively to the right:
           $$
           \text{search}(u) \leftarrow \text{search}(u.right)
           $$
      4. **Exhaustion ($u == \text{null}$):**
         - A null pointer is reached without finding $val$ $\implies$ the target does not exist in the tree. Return `null`.
- **Step-by-Step Worked Execution Trace for Target $val = 2$:**
  - **Step 1: Inspect Root Node 4:**
    - Current node value: $4$.
    - Target value: $2$.
    - Compare values:
      $$
      4 > 2 \implies \mathbf{Overshoot\ (Target\ is\ Smaller)}
      $$
    - Subtree pruning: The right child (Node 7) and all its descendants are $> 4 > 2$, so they are completely eliminated from consideration.
    - Branch to left child:
      $$
      u \leftarrow 4.left = \text{Node } 2
      $$
  - **Step 2: Inspect Node 2:**
    - Current node value: $2$.
    - Target value: $2$.
    - Compare values:
      $$
      2 == 2 \implies \mathbf{Target\ Node\ Found!}
      $$
    - Target matched.
    - Halt search and return Node 2.
  - **Step 3: Return Result:**
    - Returning Node 2 retains its full underlying subtree:
      - Left child: Node 1
      - Right child: Node 3
    - Serialized representation: `[2, 1, 3]`.
- **Search for Absent Value Trace ($val = 5$ on the same tree):**
  - **Step 1: Root Node 4:**
    - $4 < 5 \implies$ Target is larger. Branch right to Node 7.
  - **Step 2: Node 7:**
    - $7 > 5 \implies$ Target is smaller. Branch left to $7.left$.
  - **Step 3: Child of 7:**
    - $7.left$ is $\text{null}$.
    - Base case reached: node is `null`.
    - Value 5 does not exist in the BST.
    - Return **`null`**.
- **Root Match Immediate Trace ($val = 4$):**
  - Root value is $4 == val$.
  - Returns entire original tree `[4, 2, 7, 1, 3]` in 1 comparison.

This instance demonstrates binary search tree logarithmic bisection and single-path search decimation, mathematically proves why strict order trichotomy guarantees at most one search path per key, and derives $O(H)$ runtime and $O(1)$ iterative / $O(H)$ recursive space bounds.

---

## 1. Instance & Teaching Goal

Given a BST and a target value $val$:
Find the node with value equal to $val$ and return its **entire subtree**.
If not found, return `null`.

```text
BST:
        4
      /   \
     2     7   <- Target = 2
    / \
   1   3

Search Path:
  1. At Root 4: 4 > 2 -> Target is in the LEFT subtree.
  2. At Node 2: 2 == 2 -> MATCH! Return Node 2.

Subtree at Node 2:
     2
    / \
   1   3
Result: [ 2, 1, 3 ]
```

### The Invariant of BST Directional Bisection
- At every step, comparing $val$ with $u.val$ eliminates half of the remaining tree:
  - If $val < u.val$, only the left subtree can contain $val$.
  - If $val > u.val$, only the right subtree can contain $val$.
- At most one path from the root to a leaf is ever explored.

---

## 2. Conceptual Foundation & Invariants

### 1. The Search Recurrence:
$$
\text{search}(u, val) = \begin{cases} u & \text{if } u = \text{null} \lor u.val = val \\ \text{search}(u.left, val) & \text{if } u.val > val \\ \text{search}(u.right, val) & \text{if } u.val < val \end{cases}
$$

### 2. Monotonicity Trichotomy:
Every comparison partitions the key universe into three disjoint sets: $\{x < u.val\}, \{u.val\}, \{x > u.val\}$.

> **Order-Theoretic Geodesic Invariant.** In any tree representing an order-convex lattice partition, the node holding key $k$ (if it exists) lies on a unique geodesic path from the root governed strictly by the sign of the comparator $k - u.val$.

---

## 3. Step-by-Step Worked Execution

We trace $val = 2$ on $root = [4, 2, 7, 1, 3]$:

---

### Step 1: Root Node 4
- $u.val = 4, val = 2$.
- $4 > 2 \implies$ Recurse on $u.left$ (Node 2).

---

### Step 2: Node 2
- $u.val = 2, val = 2$.
- $2 == 2 \implies$ Match!
- Return Node 2.

---

### Step 3: Output
- Subtree rooted at 2:
  $$
  [\mathbf{2}, \; \mathbf{1}, \; \mathbf{3}]
  $$

---

## 4. Complete Execution Trace

| Step | Current Node $u$ | Node Value $u.val$ | Comparator with $val = 2$ | Action Taken | Search State |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | Root | $4$ | $4 > 2$ | Branch Left | Move to $4.left$ |
| **$2$** | **Left Child** | **$2$** | **$2 == 2$** | **Match Found** | **Return Node 2** |
| Post | Node 2 Subtree | — | — | Serialize `[2, 1, 3]` | Output Emitted |

---

## 5. Boundary Cases & Failure Modes

- **Target is at the Root:** Found on step 1 $\implies$ returns entire tree.
- **Target is a Leaf:** Traverses to the bottom leaf, returns that leaf node.
- **Value Not in Tree ($val = 5$):** Branches until reaching `null` $\implies$ returns `null`.
- **Empty Tree ($root = \text{null}$):** Returns `null` immediately.

---

## 6. Traps & Common Anti-Patterns

- **Searching Both Subtrees ($O(N)$):** Searching both left and right children treats the tree as an ordinary binary tree, discarding the BST property. Only search one child.
- **Returning Just the Value Instead of the Node/Subtree:** The problem asks for the node/subtree rooted at that node, not a boolean or integer.
- **Modifying Node Values:** Search is read-only; do not alter pointers or values.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - At each step, moves down by 1 level in the tree.
  - Number of visited nodes is at most the tree height $H$.
  - Balanced BST: $\mathcal{O}(\log N)$.
  - Skewed BST: $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(H)$. Completes in $< 0.1$ ms for $N = 5000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ auxiliary space for recursive call stack, or $\mathcal{O}(1)$ auxiliary space using an iterative while loop (`while root and root.val != val: root = root.left if root.val > val else root.right`).
