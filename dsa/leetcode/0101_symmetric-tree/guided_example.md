# Guided Example: Symmetric Tree

We trace the step-by-step cross-subtree mirror symmetry recursion and BFS queue verification on representative symmetric and asymmetric binary trees:

- **Symmetric Mirror Instance:** $\text{root} = [1, 2, 2, 3, 4, 4, 3] \implies \text{True}$
- **Asymmetric Structure Trap:** $\text{root} = [1, 2, 2, \text{null}, 3, \text{null}, 3] \implies \text{False}$

This instance demonstrates cross-pairing mirror invariants ($t_1.\text{left} \leftrightarrow t_2.\text{right}$ and $t_1.\text{right} \leftrightarrow t_2.\text{left}$), distinguishing identical shapes from reflected shapes, handling asymmetric null children, and iterative queue state tracking in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree, check whether it is a mirror of itself (i.e. symmetric around its center).

Consider the tree $[1, 2, 2, 3, 4, 4, 3]$:
$$
\begin{gathered}
1 \\
\swarrow \quad \searrow \\
2 \qquad\quad 2 \\
\swarrow \;\; \searrow \quad \swarrow \;\; \searrow \\
3 \quad\;\; 4 \quad 4 \quad\;\; 3
\end{gathered}
$$
To be symmetric around the vertical axis:
- The root values must match ($1 == 1$).
- The left subtree's left child ($3$) must mirror the right subtree's right child ($3$).
- The left subtree's right child ($4$) must mirror the right subtree's left child ($4$).

Notice the critical distinction between **identical** trees (LeetCode 100, which compares left to left and right to right) and **mirror** trees (LeetCode 101, which cross-compares outer to outer and inner to inner).
In $[1, 2, 2, \text{null}, 3, \text{null}, 3]$, both subtrees have right children with value $3$, but their reflection requires one right child and one left child, failing symmetry.

---

## 2. Conceptual Foundation & Invariants

### Cross-Subtree Mirror Protocol
Two subtrees rooted at $t_1$ and $t_2$ are mirrors if:
1. **Both Null:** If $t_1 == \emptyset$ and $t_2 == \emptyset$, return $\text{True}$.
2. **Asymmetric Null:** If $t_1 == \emptyset$ or $t_2 == \emptyset$, return $\text{False}$.
3. **Value Match:** If $t_1.\text{val} \ne t_2.\text{val}$, return $\text{False}$.
4. **Cross-Linked Reflection:**
   - Outer children must be mirrors: $\text{isMirror}(t_1.\text{left}, \, t_2.\text{right})$
   - Inner children must be mirrors: $\text{isMirror}(t_1.\text{right}, \, t_2.\text{left})$
   $$
   \text{isMirror}(t_1, t_2) = (t_1.\text{val} == t_2.\text{val}) \land \text{isMirror}(t_1.\text{left}, t_2.\text{right}) \land \text{isMirror}(t_1.\text{right}, t_2.\text{left})
   $$

### Iterative Queue BFS Invariant
Initialize a double-ended queue with pair $(root.\text{left}, root.\text{right})$.
At each step, dequeue pair $(u, v)$:
- Verify null status and value equality.
- Enqueue outer pair: $(u.\text{left}, v.\text{right})$.
- Enqueue inner pair: $(u.\text{right}, v.\text{left})$.

> **Invariant.** Every node pair $(u, v)$ popped from the queue occupies symmetrical, mirrored coordinate positions across the tree's vertical axis.

---

## 3. Step-by-Step Worked Execution

We trace the recursive mirror evaluation on $\text{root} = [1, 2, 2, 3, 4, 4, 3]$:

### Step 1: Initialize at Root's Children
- Call: $\text{isMirror}(t_1 = \text{Left Node}(2), \, t_2 = \text{Right Node}(2))$.
- Compare values: $2 == 2$. Match!
- Spawn two cross-mirror branches:
  - Branch A (Outers): $\text{isMirror}(t_1.\text{left} = \text{Node}(3), \, t_2.\text{right} = \text{Node}(3))$.
  - Branch B (Inners): $\text{isMirror}(t_1.\text{right} = \text{Node}(4), \, t_2.\text{left} = \text{Node}(4))$.

---

### Step 2: Evaluate Outer Pair (Branch A: $3$ vs $3$)
- Nodes: $t_1.\text{left} = \text{Node}(3)$, $t_2.\text{right} = \text{Node}(3)$.
- Values: $3 == 3$. Match!
- Children of both Node $3$s:
  - Outer outers: $(\emptyset, \emptyset) \implies \text{True}$.
  - Outer inners: $(\emptyset, \emptyset) \implies \text{True}$.
- Branch A evaluates to $\text{True}$.

---

### Step 3: Evaluate Inner Pair (Branch B: $4$ vs $4$)
- Nodes: $t_1.\text{right} = \text{Node}(4)$, $t_2.\text{left} = \text{Node}(4)$.
- Values: $4 == 4$. Match!
- Children of both Node $4$s:
  - Inner outers: $(\emptyset, \emptyset) \implies \text{True}$.
  - Inner inners: $(\emptyset, \emptyset) \implies \text{True}$.
- Branch B evaluates to $\text{True}$.

---

### Step 4: Aggregate Conjunction
- Total: $\text{Branch A} \land \text{Branch B} = \text{True} \land \text{True} = \mathbf{True}$.

---

## 4. Complete Execution Trace

### Mirror Cross-Pairing Trace ($[1, 2, 2, 3, 4, 4, 3]$)

| Step | Pair Tested $(u, v)$ | Type | Null States | Values Compared | Subtree Mirror Verdict | Next Enqueued Pairs |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $(\text{Node}(2_L), \text{Node}(2_R))$ | Root Children | Non-null | $2 == 2$ | Pending | $(\text{Node}(3_L), \text{Node}(3_R))$, $(\text{Node}(4_L), \text{Node}(4_R))$ |
| 2 | $(\text{Node}(3_L), \text{Node}(3_R))$ | Outer Pair | Non-null | $3 == 3$ | **True** | $(\emptyset, \emptyset)$, $(\emptyset, \emptyset)$ |
| 3 | $(\text{Node}(4_L), \text{Node}(4_R))$ | Inner Pair | Non-null | $4 == 4$ | **True** | $(\emptyset, \emptyset)$, $(\emptyset, \emptyset)$ |
| Leaves | 4 pairs of $(\emptyset, \emptyset)$ | Leaf Base | Both null | - | **True** | None |
| Final | Full Conjunction | - | - | - | **Return True** | - |

### Asymmetric Structure Trace ($[1, 2, 2, \text{null}, 3, \text{null}, 3]$)
- Step 1: Pair $(\text{Node}(2_L), \text{Node}(2_R))$. $2 == 2$.
- Step 2: Enqueue outers: $(2_L.\text{left}, 2_R.\text{right}) = (\emptyset, \text{Node}(3))$.
- Step 3: Dequeue $(\emptyset, \text{Node}(3))$. Exactly one is null!
- **Discrepancy:** Structural asymmetry $\implies$ returns $\mathbf{False}$ immediately.

---

## 5. Algorithmic Correctness

**Soundness.** A tree is symmetric if and only if its left subtree is a reflection of its right subtree. By induction, two subtrees are reflections if their roots match, the left-outer subchild reflects the right-outer subchild, and the left-inner subchild reflects the right-inner subchild. Any structural or value mismatch breaks this invariant and propagates `False`.

**Completeness.** Every node in the tree is paired with its exact mirror counterpart. BFS queue iteration or recursive DFS explores all nodes until all pairs are verified or an early mismatch is encountered.

---

## 6. Traps This Instance Exposes

- **Confusing Same Tree with Symmetric Tree:** Calling `isSameTree(root.left, root.right)` tests translation equality rather than reflection symmetry. In a mirror reflection, left must be paired with right, not left with left.
- **Identical Shapes That Are Asymmetric:** A tree where both $2$s have right children with value $3$ is translationally identical, but axially asymmetric.
- **Empty Root:** If $\text{root} == \emptyset$, the tree is trivially symmetric, returning `True`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Every node is visited and compared at most once.
- **Auxiliary Space Complexity:** $O(H)$ for recursion stack depth ($O(\log N)$ for balanced trees, $O(N)$ for skewed trees), or $O(W) = O(N)$ queue memory for BFS at the widest tree level.