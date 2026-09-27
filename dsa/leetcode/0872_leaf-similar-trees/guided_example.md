# Guided Example: Leaf-Similar Trees

We trace the step-by-step depth-first search leaf harvesting, left-to-right leaf boundary detection ($left == right == \text{null}$), tree shape invariance, and leaf sequence comparison on representative binary tree pairs:

- **Input:**
  $$
  root1 = [3, 5, 1, 6, 2, 9, 8, \text{null}, \text{null}, 7, 4]
  $$
  $$
  root2 = [3, 5, 1, 6, 7, 4, 2, \text{null}, \text{null}, \text{null}, \text{null}, \text{null}, \text{null}, 9, 8]
  $$
- **Required output:** `true`
  - Leaf-similar definition:
    - In a binary tree, all leaves (nodes with no children) ordered from left to right form the **leaf value sequence**.
    - Two binary trees are considered **leaf-similar** if and only if their leaf value sequences are identical in both values and ordering.
    - The interior structures and heights of the trees may be completely different.
    - Leaf extraction for Tree 1:
      - Left subtree of $3$: leaf $6$, leaf $7$, leaf $4$.
      - Right subtree of $3$: leaf $9$, leaf $8$.
      - Sequence 1: `[6, 7, 4, 9, 8]`.
    - Leaf extraction for Tree 2:
      - Left subtree of $3$: leaf $6$, leaf $7$.
      - Right subtree of $3$: leaf $4$, leaf $9$, leaf $8$.
      - Sequence 2: `[6, 7, 4, 9, 8]`.
    - Both sequences equal $[6, 7, 4, 9, 8]$!
    - Result: **`true`**.
- **The Left-to-Right DFS Invariant:**
  - **The Leaf Condition:**
    - A node $u$ is a terminal leaf if and only if:
      $$
      u.left == \text{null} \quad \land \quad u.right == \text{null}
      $$
    - In languages with unified null pointer comparison, this is compactly written as $u.left == u.right == \text{null}$.
  - **Preorder Sequence Preservation:**
    - Any standard depth-first search that visits the left child before the right child will visit every leaf in strict left-to-right horizontal projection order.
    - When visiting an internal node, recursively traverse its left child (if non-null), then its right child (if non-null).
    - When visiting a leaf node, append its value to the tree's leaf accumulator list and return immediately.
    - Compare $L_1 == L_2$ element by element.

---

## 1. Instance & Teaching Goal

Given two structurally distinct binary trees, extract and compare their leaf value sequences.

```text
Tree 1:                        Tree 2:
          3                              3
        /   \                          /   \
       5     1                        5     1
      / \   / \                      / \   / \
    [6]  2 [9] [8]                 [6] [7][4] 2
        / \                                  / \
      [7] [4]                              [9] [8]

Leaves in Tree 1: [6, 7, 4, 9, 8]
Leaves in Tree 2: [6, 7, 4, 9, 8]

Sequences match identically!
Output: true
```

The teaching goal is to show that internal branching permutations do not disturb the global projection order of terminal leaves.

---

## 2. Conceptual Foundation & Invariants

### 1. Leaf Extraction DFS Specification:
$$
\text{extract\_leaves}(u, \text{list}):
$$
$$
\begin{cases}
\text{list}.\text{append}(u.val) & \text{if } u.left == \text{null} \land u.right == \text{null} \\
\text{extract\_leaves}(u.left) \text{ then } \text{extract\_leaves}(u.right) & \text{otherwise}
\end{cases}
$$

### 2. Equivalence Criterion:
$$
\text{leafSimilar}(T_1, T_2) \iff |L(T_1)| = |L(T_2)| \quad \land \quad \forall k, \; L(T_1)[k] = L(T_2)[k]
$$

---

## 3. Step-by-Step Worked Execution

---

### Phase 1: Leaf Extraction on Tree 1
1. Start at root $3$ (internal node):
   - Traverse left child $5$.
2. At node $5$ (internal node):
   - Traverse left child $6$.
3. **At node $6$:**
   - Both children null $\implies$ **Leaf Found!**
   - Append **$6$**. Accumulator: $[6]$.
   - Backtrack to $5$, traverse right child $2$.
4. At node $2$ (internal node):
   - Traverse left child $7$.
5. **At node $7$:**
   - Both children null $\implies$ **Leaf Found!**
   - Append **$7$**. Accumulator: $[6, 7]$.
   - Backtrack to $2$, traverse right child $4$.
6. **At node $4$:**
   - Both children null $\implies$ **Leaf Found!**
   - Append **$4$**. Accumulator: $[6, 7, 4]$.
   - Backtrack to $2 \to 5 \to 3$.
7. At root $3$, traverse right child $1$.
8. At node $1$ (internal node):
   - Traverse left child $9$.
9. **At node $9$:**
   - Both children null $\implies$ **Leaf Found!**
   - Append **$9$**. Accumulator: $[6, 7, 4, 9]$.
   - Backtrack to $1$, traverse right child $8$.
10. **At node $8$:**
    - Both children null $\implies$ **Leaf Found!**
    - Append **$8$**. Accumulator: $[6, 7, 4, 9, 8]$.

Sequence for Tree 1: $L_1 = [6, 7, 4, 9, 8]$.

---

### Phase 2: Leaf Extraction on Tree 2
1. Start at root $3$ (internal node):
   - Traverse left child $5$.
2. At node $5$ (internal node):
   - Traverse left child $6 \implies$ **Leaf $6$**.
   - Traverse right child $7 \implies$ **Leaf $7$**.
   - Backtrack to $3$, traverse right child $1$.
3. At node $1$ (internal node):
   - Traverse left child $4 \implies$ **Leaf $4$**.
   - Traverse right child $2$ (internal node).
4. At node $2$ (internal node):
   - Traverse left child $9 \implies$ **Leaf $9$**.
   - Traverse right child $8 \implies$ **Leaf $8$**.

Sequence for Tree 2: $L_2 = [6, 7, 4, 9, 8]$.

---

### Phase 3: Sequence Comparison
$$
L_1 = [6, 7, 4, 9, 8]
$$
$$
L_2 = [6, 7, 4, 9, 8]
$$
$$
L_1 == L_2 \implies \mathbf{true}
$$

---

## 4. Complete Execution Trace

| Traversal Step | Tree 1 Node Evaluated | Tree 1 Action | $L_1$ State | Tree 2 Node Evaluated | Tree 2 Action | $L_2$ State |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | Node $6$ | Leaf detected | $[6]$ | Node $6$ | Leaf detected | $[6]$ |
| $2$ | Node $7$ | Leaf detected | $[6, 7]$ | Node $7$ | Leaf detected | $[6, 7]$ |
| $3$ | Node $4$ | Leaf detected | $[6, 7, 4]$ | Node $4$ | Leaf detected | $[6, 7, 4]$ |
| $4$ | Node $9$ | Leaf detected | $[6, 7, 4, 9]$ | Node $9$ | Leaf detected | $[6, 7, 4, 9]$ |
| **$5$** | **Node $8$** | **Leaf detected** | **`[6, 7, 4, 9, 8]`** | **Node $8$** | **Leaf detected** | **`[6, 7, 4, 9, 8]`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Node Trees ($[1]$ and $[1]$):** Root is itself a leaf. Leaves are $[1]$ and $[1] \implies$ returns `true`.
- **Different Leaf Values (e.g. $[1, 2]$ vs $[2, 2]$):** Leaves differ $\implies$ returns `false`.
- **Different Sequence Lengths:** Tree 1 has 3 leaves and Tree 2 has 2 leaves $\implies$ returns `false`.
- **Mirror Trees:** Tree with leaves $[1, 2]$ vs mirror tree with leaves $[2, 1] \implies$ returns `false` (order matters).

---

## 6. Traps & Common Anti-Patterns

- **Mistaking Degree-1 Nodes for Leaves:** A node with one null child and one non-null child is **not** a leaf. Both children must be null simultaneously.
- **Level-Order (BFS) Traversal:** BFS collects leaves layer by layer according to depth rather than horizontal left-to-right order, producing out-of-order leaf sequences when tree branches have different heights. DFS is required for true left-to-right ordering.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - DFS on Tree 1 visits $N_1$ nodes: $\mathcal{O}(N_1)$.
  - DFS on Tree 2 visits $N_2$ nodes: $\mathcal{O}(N_2)$.
  - Sequence comparison of length $L \le \min(N_1, N_2)$: $\mathcal{O}(L)$.
  - Total Time: $\mathcal{O}(N_1 + N_2)$, completing in $< 2$ ms for $N_1, N_2 \le 200$.
- **Auxiliary Space Complexity:**
  - Call stack bounded by tree height $H_1, H_2$: $\mathcal{O}(H_1 + H_2)$.
  - Storing leaf lists of size at most $N_1, N_2$: $\mathcal{O}(N_1 + N_2)$ space.
