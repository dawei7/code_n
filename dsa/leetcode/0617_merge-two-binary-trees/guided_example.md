# Guided Example: Merge Two Binary Trees

We trace the step-by-step structural superposition of two binary trees ($T_1 \oplus T_2$), dual-node presence summation ($val_1 + val_2$), unilateral null subtree short-circuit forwarding ($T_1 = \text{null} \implies T_2$), recursive topological synchronization, and composite tree assembly on representative hierarchical inputs:

- **Input:**
  - Tree 1 ($root_1$):
    ```text
          1
         / \
        3   2
       /
      5
    ```
  - Tree 2 ($root_2$):
    ```text
        2
       / \
      1   3
       \   \
        4   7
    ```
- **Required output:**
  ```text
        3
       / \
      4   5
     / \   \
    5   4   7
  ```
  - Serialization array: `[3, 4, 5, 5, 4, null, 7]`
  - Merge rules:
    1. If both trees have a node at position $P$: create a merged node with value:
       $$
       val = val_1 + val_2
       $$
    2. If only one tree has a node at position $P$ (the other is `null`): inherit the existing node and its entire subtree directly without modification.
    3. If both trees are `null` at position $P$: the merged position is `null`.
- **Topological Superposition & Structural Short-Circuiting:**
  - Let $merge(u, v)$ be the recursive superposition of node $u \in T_1$ and node $v \in T_2$:
    $$
    merge(u, v) = \begin{cases}
    v & \text{if } u \text{ is null} \\
    u & \text{if } v \text{ is null} \\
    \text{Node}(u.val + v.val, \; merge(u.left, v.left), \; merge(u.right, v.right)) & \text{if both exist}
    \end{cases}
    $$
  - When one branch is `null`, recursion does not need to traverse deeper into the non-null branch; the entire existing subtree is adopted as-is in $O(1)$ time!
- **Step-by-Step Recursive Execution Trace:**
  - **Level 1: Root Node ($merge(\text{Node } 1, \; \text{Node } 2)$):**
    - Both roots exist: $val_1 = 1, \; val_2 = 2$.
    - Sum:
      $$
      val = 1 + 2 = \mathbf{3}
      $$
    - Recurse on left children: $merge(\text{Node } 3, \; \text{Node } 1)$.
    - Recurse on right children: $merge(\text{Node } 2, \; \text{Node } 3)$.
  - **Level 2 Left: ($merge(\text{Node } 3, \; \text{Node } 1)$):**
    - Both nodes exist: $val_1 = 3, \; val_2 = 1$.
    - Sum:
      $$
      val = 3 + 1 = \mathbf{4}
      $$
    - Recurse on left children: $merge(\text{Node } 5, \; \text{null})$.
      - Tree 2 is `null` $\implies$ Short-circuit! Inherit **Node 5** directly.
    - Recurse on right children: $merge(\text{null}, \; \text{Node } 4)$.
      - Tree 1 is `null` $\implies$ Short-circuit! Inherit **Node 4** directly.
    - Merged subtree at this position:
      ```text
            4
           / \
          5   4
      ```
  - **Level 2 Right: ($merge(\text{Node } 2, \; \text{Node } 3)$):**
    - Both nodes exist: $val_1 = 2, \; val_2 = 3$.
    - Sum:
      $$
      val = 2 + 3 = \mathbf{5}
      $$
    - Recurse on left children: $merge(\text{null}, \; \text{null}) \implies \mathbf{null}$.
    - Recurse on right children: $merge(\text{null}, \; \text{Node } 7)$.
      - Tree 1 is `null` $\implies$ Short-circuit! Inherit **Node 7** directly.
    - Merged subtree at this position:
      ```text
            5
             \
              7
      ```
  - **Level 1 Assembly:**
    - Attach left child (Root 4) and right child (Root 5) to Root 3:
      ```text
            3
           / \
          4   5
         / \   \
        5   4   7
      ```
- **Disjoint Subtrees Instance:**
  - If Tree 1 has only a left child and Tree 2 has only a right child, the merged tree possesses both children without modifying their values.
- **Empty Tree Base Cases:**
  - $merge(\text{null}, T_2) = T_2$.
  - $merge(T_1, \text{null}) = T_1$.

This instance demonstrates recursive structural homomorphism and algebraic node superposition, mathematically proves why null branch short-circuiting bounds traversal to the intersection of the two tree geometries, and derives $O(\min(N_1, N_2))$ runtime and $O(H)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two binary trees $T_1$ and $T_2$:
Superimpose them into a single merged tree:
- If nodes overlap, sum their values.
- If only one node exists, use that node directly.

```text
Tree 1:        Tree 2:         Merged:
    1             2               3
   / \           / \             / \
  3   2   +     1   3     =     4   5
 /               \   \         / \   \
5                 4   7       5   4   7
```

### The Invariant of Subtree Delegation
- When one tree lacks a subtree ($root_1 = \text{null}$), there is no need to recursively clone or inspect the other tree's nodes.
- Returning $root_2$ immediately reuses or points to the entire remaining sub-hierarchy in $O(1)$ operations.

---

## 2. Conceptual Foundation & Invariants

### 1. Structural Recurrence:
$$
merge(T_1, T_2) =
\begin{cases}
T_2 & \text{if } T_1 = \emptyset \\
T_1 & \text{if } T_2 = \emptyset \\
\text{Node}(T_1.val + T_2.val, \; merge(T_1.L, T_2.L), \; merge(T_1.R, T_2.R)) & \text{otherwise}
\end{cases}
$$

### 2. Preservation of Topology:
- Any node path present in either $T_1$ or $T_2$ is guaranteed to exist in the merged tree.
- The value at each path coordinate $p$ equals $\sum_{T \in \{T_1, T_2\}} T[p].val$.

> **Homomorphic Monoid Invariant.** The merge operation forms a commutative monoid on the space of binary trees with empty tree $\emptyset$ as the identity and node addition as the binary operator.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Root Position
- $T_1[root] = 1, \; T_2[root] = 2 \implies 1 + 2 = \mathbf{3}$.

---

### Step 2: Left Child of Root
- $T_1 = 3, \; T_2 = 1 \implies 3 + 1 = \mathbf{4}$.
  - Left grandchild: $T_1 = 5, \; T_2 = \text{null} \implies \mathbf{5}$ (inherited from $T_1$).
  - Right grandchild: $T_1 = \text{null}, \; T_2 = 4 \implies \mathbf{4}$ (inherited from $T_2$).

---

### Step 3: Right Child of Root
- $T_1 = 2, \; T_2 = 3 \implies 2 + 3 = \mathbf{5}$.
  - Left grandchild: both null $\implies \mathbf{null}$.
  - Right grandchild: $T_1 = \text{null}, \; T_2 = 7 \implies \mathbf{7}$ (inherited from $T_2$).

---

## 4. Complete Execution Trace

| Tree Coordinate | $T_1$ Node Value | $T_2$ Node Value | Merge Case | Merged Value |
|:---:|:---:|:---:|:---:|:---:|
| `Root` | $1$ | $2$ | Both Present | $1 + 2 = \mathbf{3}$ |
| `Left` | $3$ | $1$ | Both Present | $3 + 1 = \mathbf{4}$ |
| `Left -> Left` | $5$ | `null` | $T_2$ is Null | $\mathbf{5}$ |
| `Left -> Right` | `null` | $4$ | $T_1$ is Null | $\mathbf{4}$ |
| `Right` | $2$ | $3$ | Both Present | $2 + 3 = \mathbf{5}$ |
| `Right -> Right` | `null` | $7$ | $T_1$ is Null | $\mathbf{7}$ |

---

## 5. Boundary Cases & Failure Modes

- **Both Trees Empty ($T_1 = T_2 = \text{null}$):** Returns `null`.
- **One Tree Completely Empty ($T_1 = \text{null}, T_2 \ne \text{null}$):** Returns $T_2$ root directly.
- **Identical Shape Trees:** All node values sum pair by pair.
- **Negative Node Values:** $-3 + 5 = 2$ evaluated with standard signed addition.

---

## 6. Traps & Common Anti-Patterns

- **Deeply Traversing When One Tree is Null:** Writing recursive checks when a child is null wastes time; simply returning the non-null child accomplishes the entire subtree merge.
- **Mutating Input Trees Without Permission:** In-place mutation of $T_1$ can corrupt caller references if the trees are reused. Constructing new nodes preserves purity.
- **Losing One-Sided Children:** Forgetting the case where $T_1$ is null but $T_2$ is not drops the right side of asymmetric trees.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The recursion visits only nodes that exist in **both** trees (overlapping intersection) plus the boundary edges where one tree becomes null.
  - Number of visited nodes is bounded by $\mathcal{O}(\min(N_1, N_2))$.
  - Total Time: $\mathcal{O}(\min(N_1, N_2))$. Completes in $< 2$ ms for trees with $N \le 2000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ call stack depth where $H = \min(H_1, H_2)$ is the minimum tree height.