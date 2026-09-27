# Guided Example: Same Tree

We trace the step-by-step dual-tree simultaneous structural and value equivalence recursion on representative matching and mismatching binary trees:

- **Matching Identical Trees:** $p = [1, 2, 3], q = [1, 2, 3] \implies \text{True}$
- **Structural Mismatch Trap:** $p = [1, 2], q = [1, \text{null}, 2] \implies \text{False}$
- **Value Mismatch Trap:** $p = [1, 2, 1], q = [1, 1, 2] \implies \text{False}$

This instance demonstrates recursive lockstep DFS on dual binary trees, checking base identity conditions ($p = q = \emptyset$), catching asymmetrical null structures, comparing scalar node values, and short-circuiting on the first discrepancy in $O(\min(N, M))$ time.

---

## 1. Instance & Teaching Goal

Given the roots of two binary trees $p$ and $q$, write a function to check if they are the same or not.
Two binary trees are considered the same if they are:
1. **Structurally identical:** every node in $p$ has a corresponding child structure in $q$.
2. **Value equivalent:** all corresponding nodes have equal values ($p.\text{val} == q.\text{val}$).

Consider three distinct scenarios:
- **Case 1 (Identical):**
  $p = (1 \to (2, 3)), \quad q = (1 \to (2, 3)) \implies \text{True}$.
- **Case 2 (Structural Mismatch):**
  In $p$, node $2$ is the **left** child of $1$.
  In $q$, node $2$ is the **right** child of $1$.
  Even though their values are identical ($\{1, 2\}$), their topologies differ $\implies \text{False}$.
- **Case 3 (Value Mismatch):**
  Both trees have identical topology $1 \to (L, R)$, but $p$ has $(2, 1)$ while $q$ has $(1, 2) \implies \text{False}$.

A naive approach serializing trees to strings must preserve null markers; otherwise $[1, 2]$ and $[1, \text{null}, 2]$ produce identical preorder sequences (`"1, 2"`).
A recursive lockstep traversal tests both structure and values simultaneously without serialization overhead.

---

## 2. Conceptual Foundation & Invariants

### Dual-Tree Lockstep DFS Protocol
We define $\text{isSameTree}(p, q)$:

1. **Both Null Base Case:**
   If $p == \emptyset$ and $q == \emptyset$:
   - Both subtrees are empty $\implies$ return $\text{True}$.
2. **Asymmetric Null Discrepancy:**
   If $p == \emptyset$ or $q == \emptyset$:
   - Exactly one node is null while the other exists $\implies$ structural mismatch!
   - Return $\text{False}$.
3. **Value Equality Check:**
   If $p.\text{val} \ne q.\text{val}$:
   - Values differ $\implies$ return $\text{False}$.
4. **Recursive Lockstep Conjunction:**
   Both current nodes match. Recurse on both left children and both right children:
   $$
   \text{isSameTree}(p.\text{left}, \, q.\text{left}) \land \text{isSameTree}(p.\text{right}, \, q.\text{right})
   $$

> **Invariant.** A call $\text{isSameTree}(p, q)$ returns true if and only if the subtrees rooted at $p$ and $q$ are isomorphic in shape and identical in node values.

---

## 3. Step-by-Step Worked Execution

We trace $p = [1, 2, 3]$ and $q = [1, 2, 3]$:

### Step 1: Compare Roots $p_1$ and $q_1$
- Neither is null: $p = \text{Node}(1), q = \text{Node}(1)$.
- Compare values: $p.\text{val} = 1 == q.\text{val} = 1$. Match!
- Recurse left: $\text{isSameTree}(p.\text{left}, q.\text{left})$.
- Recurse right: $\text{isSameTree}(p.\text{right}, q.\text{right})$.

---

### Step 2: Compare Left Children ($p_2$ vs $q_2$)
- Neither is null: $p = \text{Node}(2), q = \text{Node}(2)$.
- Compare values: $2 == 2$. Match!
- Children of Node 2:
  - Both left children are null $\implies \text{isSameTree}(\emptyset, \emptyset) = \text{True}$.
  - Both right children are null $\implies \text{isSameTree}(\emptyset, \emptyset) = \text{True}$.
- Left subtree conjunction: $\text{True} \land \text{True} = \text{True}$.

---

### Step 3: Compare Right Children ($p_3$ vs $q_3$)
- Neither is null: $p = \text{Node}(3), q = \text{Node}(3)$.
- Compare values: $3 == 3$. Match!
- Children of Node 3:
  - Both left children null $\implies \text{True}$.
  - Both right children null $\implies \text{True}$.
- Right subtree conjunction: $\text{True} \land \text{True} = \text{True}$.

---

### Step 4: Final Conjunction
- Root conjunction: $\text{LeftResult} \land \text{RightResult} = \text{True} \land \text{True} = \mathbf{True}$.

---

## 4. Complete Execution Trace

### Lockstep Comparison Matrix

| Step | Pair $(p, q)$ Evaluated | Null Status | Values Compared | Subtree Match Verdict | Action |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $(p_1, q_1)$ | Both non-null | $1 == 1$ (Equal) | Pending children | Recurse Left & Right |
| 2 | $(p_2, q_2)$ | Both non-null | $2 == 2$ (Equal) | Pending leaves | Recurse Left & Right |
| 2.1 | $(p_2.\text{left}, q_2.\text{left})$ | Both null | - | **True** | Base leaf return |
| 2.2 | $(p_2.\text{right}, q_2.\text{right})$ | Both null | - | **True** | Base leaf return |
| 3 | $(p_3, q_3)$ | Both non-null | $3 == 3$ (Equal) | Pending leaves | Recurse Left & Right |
| 3.1 | $(p_3.\text{left}, q_3.\text{left})$ | Both null | - | **True** | Base leaf return |
| 3.2 | $(p_3.\text{right}, q_3.\text{right})$ | Both null | - | **True** | Base leaf return |
| Final | Root Conjunction | - | - | $\text{True} \land \text{True}$ | **Return True** |

### Structural Mismatch Trace ($p = [1, 2], q = [1, \text{null}, 2]$)
- Step 1: Root $1 == 1$.
- Step 2: Compare left children: $p.\text{left} = \text{Node}(2)$, but $q.\text{left} = \emptyset$.
- Condition: Exactly one is null!
- **Early Return:** Returns $\text{False}$ immediately without visiting right subtrees.

### Deep Value Mismatch Trace ($p = [4, 2, 6, 1, 3, 5, 7]$, $q = [4, 2, 6, 1, 3, 8, 7]$)

Both trees are complete binary trees over the same level-order skeleton, so structure is never the deciding factor here; only one value differs. The conjunction short-circuits left-to-right, so the traversal order determines how many pairs are inspected before the verdict.

| Visit | Node pair $(p, q)$ | Position in the skeleton | Value comparison | Verdict | What happens next |
|:---:|:---|:---|:---:|:---:|:---|
| 1 | $(4, 4)$ | depth 0, root | $4 = 4$ | match | Descend into the left pair first |
| 2 | $(2, 2)$ | depth 1, root's left | $2 = 2$ | match | Descend into its left pair |
| 3 | $(1, 1)$ | depth 2, left-left | $1 = 1$ | match | Both children null, so this leaf pair is complete |
| 4 | $(3, 3)$ | depth 2, left-right | $3 = 3$ | match | Left subtree resolved as matching |
| 5 | $(6, 6)$ | depth 1, root's right | $6 = 6$ | match | Descend into its left pair |
| 6 | $(5, 8)$ | depth 2, right-left | $5 \ne 8$ | mismatch | Return $\text{False}$; the pair $(7, 7)$ is never inspected |

The tree pair $(7, 7)$ stays unvisited even though its values agree, because the left-to-right conjunction already returned false. This is why the running time is bounded by the number of pairs inspected before the first discrepancy, not by the total size of the trees.

---

## 5. Algorithmic Correctness

**Soundness.** A tree is defined inductively by its root and its left and right subtrees. If the roots match in value and both subtrees are inductively identical, the entire trees are identical. If at any point values differ or a node exists in one tree but not the other, the inductive condition fails.

**Completeness.** Lockstep traversal visits every corresponding pair of nodes in preorder until all nodes are confirmed identical or a discrepancy triggers an early return.

---

## 6. Traps This Instance Exposes

- **Order of Null Checks:** Checking `p.val == q.val` before checking whether `p` or `q` is null causes an immediate `AttributeError` / `NullPointerException`. The dual null check `not p and not q` must precede any attribute access.
- **Asymmetric Null Check:** Using `if not p and not q: return True` followed by `if not p or not q: return False` cleanly catches the case where one node exists and the other is null.
- **Serialization Traps:** Serializing trees into strings without explicit null indicators confuses left vs right skew trees (e.g. $[1, 2]$ vs $[1, \text{null}, 2]$).

### Boundary Case Matrix

The lesson's instances can be classified by which rule of the protocol terminates the comparison. The final column counts only pairs where both nodes exist and their values are actually read; null-structure calls cost a visit but never a value comparison.

| Instance | Level-order encoding | Deciding rule | Non-null value pairs compared | Result |
|:---|:---|:---|:---:|:---:|
| Both trees empty | `p = []`, `q = []` | Dual-null base case on the very first call | 0 | True |
| Exactly one tree empty | `p = [0]`, `q = []` | Asymmetric null: the root exists in $p$ but not in $q$ | 0 | False |
| Equal values, different shape | `p = [1, 2]`, `q = [1, null, 2]` | Left-position mismatch: $2$ is $p$'s left child but $q$'s right child | 1 | False |
| Sibling values swapped | `p = [1, 2, 1]`, `q = [1, 1, 2]` | Value mismatch at the left pair, even though both trees hold the multiset $\{1, 1, 2\}$ | 1 | False |
| Deep single-value mismatch | `p = [4, 2, 6, 1, 3, 5, 7]`, `q = [4, 2, 6, 1, 3, 8, 7]` | Value mismatch at the sixth pair, after five confirming pairs | 6 | False |
| Fully identical | `p = [1, 2, 3]`, `q = [1, 2, 3]` | Every pair matches and every child pair is doubly null | 3 | True |

The swapped-sibling row is the sharpest trap: the two trees contain the same values, and a multiset or sorted-serialization test would accept them. Only a position-aware comparison rejects them, because equivalence is required per corresponding node, not per set of values.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\min(N, M))$, where $N$ and $M$ are the node counts of $p$ and $q$. If the trees match, it visits all $N = M$ nodes. If they differ, it terminates at the first structural or value mismatch.
- **Auxiliary Space Complexity:** $O(\min(H_p, H_q))$, where $H$ is the tree height, representing the recursion stack depth.
