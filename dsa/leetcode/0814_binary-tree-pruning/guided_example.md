# Guided Example: Binary Tree Pruning

We trace the step-by-step binary tree structural subtree elimination (removal of all subtrees containing no 1s), post-order depth-first traversal ($L \to R \to Root$), bottom-up leaf zero detection ($val == 0 \land left == null \land right == null$), recursive branch disconnection, and pruned tree root return on representative binary trees:

- **Input:**
  $$
  root = [1, \; \text{null}, \; 0, \; 0, \; 1]
  $$
- **Required output:**
  $$
  [1, \; \text{null}, \; 0, \; \text{null}, \; 1]
  $$
  - Subtree pruning definitions:
    - A binary tree contains nodes with values in $\{0, 1\}$.
    - A node's **subtree** consists of the node itself plus all its descendants.
    - We must remove every subtree that **does not contain any node with value 1**.
    - For $root = [1, \text{null}, 0, 0, 1]$:
      - Node 1 (root): has right child Node 0.
      - Node 0 (right child): has left child Node 0 and right child Node 1.
      - Inspect left child of Node 0: it is a leaf with value 0. Its subtree has no 1s $\implies$ **Pruned!**
      - Inspect right child of Node 0: it is a leaf with value 1 $\implies$ **Retained.**
      - Now Node 0 has right child Node 1 (which contains a 1) $\implies$ Node 0 is **Retained.**
      - Root 1 contains a 1 $\implies$ **Retained.**
      - Result: `[1, null, 0, null, 1]`.
- **Post-Order Bottom-Up Pruning Invariant:**
  - **Why Post-Order Traversal is Necessary:**
    - A parent node cannot determine whether its entire subtree contains a 1 until **both of its children have already been fully pruned**!
    - By visiting children first ($L \to R \to Root$), all zero-only descendant branches are pruned away before the parent evaluates its own status.
  - **The Zero-Leaf Pruning Condition:**
    - When visiting a node $u$ after its children have been processed:
      $$
      u.left \leftarrow \text{pruneTree}(u.left)
      $$
      $$
      u.right \leftarrow \text{pruneTree}(u.right)
      $$
    - If:
      $$
      u.val == 0 \quad \text{and} \quad u.left == \text{null} \quad \text{and} \quad u.right == \text{null}
      $$
      Then node $u$ is now a leaf with value 0, which means the entire subtree rooted at $u$ contained no 1s!
    - Return `null` to sever the connection from its parent.
    - Otherwise, return $u$.
- **Step-by-Step Worked Execution Trace on $[1, \text{null}, 0, 0, 1]$:**
  - Let the nodes be:
    - $N_A$ (Root, val = 1)
    - $N_B$ (Right child of $N_A$, val = 0)
    - $N_C$ (Left child of $N_B$, val = 0)
    - $N_D$ (Right child of $N_B$, val = 1)
  - Execution begins at root $N_A$:
  - **Step 1: Visit $N_A$ (val = 1):**
    - Prune left child: `null` $\implies$ returns `null`.
    - Prune right child: recurse on $N_B$.
  - **Step 2: Visit $N_B$ (val = 0):**
    - Prune left child: recurse on $N_C$.
    - Prune right child: recurse on $N_D$.
  - **Step 3: Visit $N_C$ (val = 0, Leaf):**
    - Both left and right children are `null`.
    - Sizing check:
      $$
      N_C.val == 0 \quad \text{and} \quad N_C.left == \text{null} \quad \text{and} \quad N_C.right == \text{null}
      $$
    - Node $N_C$ is a zero-leaf $\implies \mathbf{Prune\ Subtree!}$
    - Return `null` to parent $N_B$.
    - $N_B.left \leftarrow \text{null}$.
  - **Step 4: Visit $N_D$ (val = 1, Leaf):**
    - Both left and right children are `null`.
    - Sizing check:
      $$
      N_D.val = 1 \ne 0
      $$
      Contains a 1 $\implies \mathbf{Retain\ Node!}$
    - Return $N_D$ to parent $N_B$.
    - $N_B.right \leftarrow N_D$.
  - **Step 5: Return to $N_B$ (val = 0):**
    - Current children:
      $$
      N_B.left = \text{null}, \quad N_B.right = N_D \ne \text{null}
      $$
    - Because $N_B.right \ne \text{null}$, the subtree contains $N_D$ (value 1).
    - Node $N_B$ is NOT a zero-leaf $\implies \mathbf{Retain\ Node!}$
    - Return $N_B$ to root $N_A$.
    - $N_A.right \leftarrow N_B$.
  - **Step 6: Return to Root $N_A$ (val = 1):**
    - $N_A.val = 1 \implies \mathbf{Retain\ Root!}$
    - Return $N_A$.
  - **Output Tree Structure:**
    - Root $1$ has left child `null` and right child $0$.
    - Right child $0$ has left child `null` and right child $1$.
    - Result:
      $$
      ans = [1, \; \text{null}, \; 0, \; \text{null}, \; 1]
      $$
- **All Zeros Tree Trace ($root = [0, 0, 0]$):**
  - Left child 0 is pruned $\to null$.
  - Right child 0 is pruned $\to null$.
  - Root 0 becomes a zero-leaf $\to null$.
  - Entire tree collapses to `null`!
- **All Ones Tree Trace ($root = [1, 1, 1]$):**
  - No node has value 0 with empty children $\implies$ tree remains unchanged.

This instance demonstrates inductive tree surgery and bottom-up kernel elimination via post-order depth-first traversal, mathematically proves why post-order processing maintains topological closure of subtree reachability properties, and derives $O(N)$ execution time and $O(H)$ auxiliary call-stack space bounds.

---

## 1. Instance & Teaching Goal

Given a binary tree of 0s and 1s:
Remove every subtree that does not contain a 1.

```text
       1
        \
         0
        / \
       0   1

Post-order evaluation:
  Left child of 0 (val 0): is a leaf -> PRUNED!
  Right child of 0 (val 1): contains 1 -> KEPT!
  Parent 0: now has right child 1 -> KEPT!
  Root 1: val is 1 -> KEPT!

Result:
       1
        \
         0
          \
           1
```

### The Invariant of Bottom-Up Pruning
- We must evaluate children before parents (post-order).
- A node is pruned if and only if:
  $$
  root.val == 0 \quad \text{and} \quad root.left == null \quad \text{and} \quad root.right == null
  $$
- Pruned nodes return `null` to disconnect themselves from their parents.

---

## 2. Conceptual Foundation & Invariants

### 1. Post-Order Tree Recurrence:
$$
root.left \leftarrow \text{pruneTree}(root.left)
$$
$$
root.right \leftarrow \text{pruneTree}(root.right)
$$

### 2. Elimination Predicate:
$$
\text{pruneTree}(root) = \begin{cases}
null & root == null \;\lor\; (root.val == 0 \land root.left == null \land root.right == null) \\
root & \text{otherwise}
\end{cases}
$$

> **Subtree Monad Invariant.** Let $\mu(T) = \sum_{v \in T} val(v)$ be the total 1-weight of subtree $T$. The pruning operator eliminates the maximal forest of connected components with $\mu(T') = 0$. Post-order traversal guarantees that $\mu(T_{left}) = 0$ and $\mu(T_{right}) = 0$ are certified before testing $val(root)$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Recurse to Leaf $N_C$ (0)
- Children are `null`, $val = 0 \implies$ pruned to `null`.

---

### Step 2: Recurse to Leaf $N_D$ (1)
- $val = 1 \implies$ retained.

---

### Step 3: Evaluate Parent $N_B$ (0)
- Left is `null`, right is $N_D \ne null \implies$ retained.

---

### Step 4: Evaluate Root $N_A$ (1)
- $val = 1 \implies$ retained.

---

### Step 5: Output
$$
[1, \; \text{null}, \; 0, \; \text{null}, \; 1]
$$

---

## 4. Complete Execution Trace

| Node Visited | Node Value | Left Child Status | Right Child Status | Is Zero-Leaf? | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $N_C$ | $0$ | `null` | `null` | **Yes** | **Prune (Return `null`)** |
| $N_D$ | $1$ | `null` | `null` | No ($val=1$) | Retain |
| $N_B$ | $0$ | `null` (Pruned) | $N_D$ (Retained) | No (Right child exists) | Retain |
| **$N_A$** | **$1$** | **`null`** | **$N_B$** | **No ($val=1$)** | **Retain (Root)** |

---

## 5. Boundary Cases & Failure Modes

- **Root is 0 and Entire Tree is 0 ($[0, 0, 0]$):** Every node prunes; returns `null`.
- **Single Node 0 ($[0]$):** Pruned $\implies$ `null`.
- **Single Node 1 ($[1]$):** Retained $\implies [1]$.
- **Right/Left Skewed Trees:** Linear recursion depth handled cleanly up to $H \le 200$.

---

## 6. Traps & Common Anti-Patterns

- **Pre-Order Traversal:** Deciding whether to prune a parent before visiting its children can falsely delete subtrees that contain 1s deeper down, or fail to delete parents whose children become empty. Post-order is mandatory.
- **Checking `root.left == root.right`:** In Python, `root.left == root.right` works only if both are `None`, but explicitly checking `root.left is None and root.right is None` avoids any accidental object equality confusion.
- **Forgetting to Reassign Child Pointers:** Must write `root.left = pruneTree(root.left)` to update parent references when children are pruned.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Every node in the binary tree is visited exactly once: $\mathcal{O}(N)$.
  - Constant-time checks per node: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 200$. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ call-stack space where $H$ is the height of the tree ($H \le N \le 200$).