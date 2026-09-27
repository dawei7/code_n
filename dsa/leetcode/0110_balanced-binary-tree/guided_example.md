# Guided Example: Balanced Binary Tree

We trace the step-by-step bottom-up post-order height evaluation and sentinel short-circuiting on representative balanced and unbalanced binary trees:

- **Balanced Tree Instance:** $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7] \implies \text{True}$
- **Unbalanced Tree Trap:** $\text{root} = [1, 2, 2, 3, 3, \text{null}, \text{null}, 4, 4] \implies \text{False}$

This instance demonstrates avoiding top-down $O(N^2)$ redundant height computations by using bottom-up post-order aggregation, signaling height imbalance via an error sentinel ($-1$), short-circuiting recursion upon first violation, and achieving optimal $O(N)$ linear time.

---

## 1. Instance & Teaching Goal

Given a binary tree, determine if it is **height-balanced** (a binary tree in which the left and right subtrees of *every* node differ in height by no more than 1).

Consider two contrasting trees:
- **Tree 1 ($[3, 9, 20, \text{null}, \text{null}, 15, 7]$):**
  - Left subtree (node 9) has height $1$.
  - Right subtree (node 20) has height $2$.
  - Difference: $|1 - 2| = 1 \le 1$.
  - Nodes 9 and 20 are internally balanced. Result is $\text{True}$.
- **Tree 2 ($[1, 2, 2, 3, 3, \text{null}, \text{null}, 4, 4]$):**
  - Left subtree of root $1$ has height $3$ (path $1 \to 2 \to 3 \to 4$).
  - Right subtree of root $1$ has height $1$ (single leaf $2$).
  - Difference: $|3 - 1| = 2 > 1$. Result is $\text{False}$.

A naive top-down approach calls `height(node.left)` and `height(node.right)` repeatedly at every node, recalculating heights of descendant nodes $O(N^2)$ times.
The optimal bottom-up post-order method calculates height from the leaves upward in a single pass. If any subproblem detects $|H_L - H_R| > 1$, it immediately returns a sentinel value $-1$, short-circuiting all remaining ancestor computations in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### Bottom-Up Height Sentinel Protocol
We define $\text{checkHeight}(\text{node})$ returning either the non-negative tree height or $-1$ (unbalanced):

1. **Base Case:**
   If $\text{node} == \emptyset$:
   $$
   \text{return } 0
   $$
2. **Left Subtree Evaluation:**
   $$
   L = \text{checkHeight}(\text{node.left})
   $$
   If $L == -1$: return $-1$ (early short-circuit; left subtree already unbalanced).
3. **Right Subtree Evaluation:**
   $$
   R = \text{checkHeight}(\text{node.right})
   $$
   If $R == -1$: return $-1$ (early short-circuit; right subtree already unbalanced).
4. **Balance Condition Check:**
   If $|L - R| > 1$:
   $$
   \text{return } -1 \quad (\text{Node is unbalanced})
   $$
5. **Inductive Height Return:**
   $$
   \text{return } 1 + \max(L, R)
   $$

The root is balanced if and only if $\text{checkHeight}(\text{root}) \ne -1$.

> **Invariant.** If $\text{checkHeight}(\text{node}) \ge 0$, the subtree is strictly height-balanced with that exact height. If $\text{checkHeight}(\text{node}) = -1$, at least one node within the subtree violates the balance condition.

---

## 3. Step-by-Step Worked Execution

### Instance 1: Balanced Tree ($[3, 9, 20, \text{null}, \text{null}, 15, 7]$)
- **Node 9:** $L = 0, R = 0 \implies |0 - 0| = 0 \le 1$. Returns height $1 + \max(0, 0) = 1$.
- **Node 15:** $L = 0, R = 0 \implies$ Returns height $1$.
- **Node 7:** $L = 0, R = 0 \implies$ Returns height $1$.
- **Node 20:** $L = 1, R = 1 \implies |1 - 1| = 0 \le 1$. Returns height $1 + \max(1, 1) = 2$.
- **Root 3:** $L = 1$ (Node 9), $R = 2$ (Node 20).
  - Difference: $|1 - 2| = 1 \le 1$.
  - Returns height $1 + 2 = 3$.
- Since $3 \ne -1$, tree is **Balanced** ($\text{True}$).

---

### Instance 2: Unbalanced Tree ($[1, 2, 2, 3, 3, \text{null}, \text{null}, 4, 4]$)
- **Leaves Node 4:** Height is $1$.
- **Node 3:** $L = 1$ (left 4), $R = 1$ (right 4) $\implies$ Returns height $2$.
- **Node 2 (Left child of 1):**
  - Left child is Node 3 (height $2$).
  - Right child is Node 3 (height $2$).
  - Difference: $|2 - 2| = 0 \le 1$. Returns height $1 + 2 = 3$.
- **Node 2 (Right child of 1):**
  - Both children are null $\implies$ Returns height $1$.
- **Root Node 1:**
  - Left subtree height: $L = 3$.
  - Right subtree height: $R = 1$.
  - Balance check: $|3 - 1| = 2 > 1$.
  - **Imbalance Detected!** Returns sentinel $-1$.
- Tree is **Unbalanced** ($\text{False}$).

---

## 4. Complete Execution Trace

### Bottom-Up Check Table for Unbalanced Instance

```text
                  Root 1: L=3, R=1 -> |3-1| = 2 > 1 -> UNBALANCED (-1)
                 /      \
            Node 2 (H=3)  Node 2 (H=1)
             /      \
        Node 3 (H=2) Node 3 (H=2)
         /      \
      Node 4   Node 4
```

| Traversal Step | Node Inspected | Left Subtree Height $L$ | Right Subtree Height $R$ | Height Difference $|L - R|$ | Balanced? | Returned Value |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Node 4 | 0 | 0 | 0 | Yes | 1 |
| 2 | Left Node 3 | 1 (Node 4) | 1 (Node 4) | 0 | Yes | 2 |
| 3 | Right Node 3 | 0 | 0 | 0 | Yes | 1 |
| 4 | Left Node 2 | 2 (Node 3) | 1 (Node 3) | 1 | Yes | 3 |
| 5 | Right Node 2 | 0 | 0 | 0 | Yes | 1 |
| **6** | **Root 1** | **3 (Left Node 2)** | **1 (Right Node 2)** | **$|3 - 1| = 2$** | **No ($> 1$)** | **$-1$ (Error)** |
| Exit | Root Return | - | - | - | - | **False** |

---

## 5. Algorithmic Correctness

**Soundness.** Height balance requires $|H_L - H_R| \le 1$ for *every* node in the tree. Because $\text{checkHeight}$ evaluates this predicate at every node before returning its height to its parent, any single violating node causes $-1$ to propagate up the recursion chain, correctly triggering a `False` output.

**Completeness.** By visiting all nodes in post-order, child heights are fully resolved before evaluating their parent. Short-circuiting on $-1$ guarantees no false negatives while pruning unnecessary evaluation of remaining subtrees once a violation is discovered.

---

## 6. Traps This Instance Exposes

- **Top-Down $O(N^2)$ Trap:** Calling a separate `height()` function from `isBalanced(node)` revisits nodes repeatedly, degrading performance from linear $O(N)$ to quadratic $O(N^2)$ on skewed trees. Combining height calculation and balance verification into a single bottom-up function achieves $O(N)$.
- **Checking Only the Root:** Verifying $|H_L - H_R| \le 1$ only at the root node is insufficient; both subtrees must also be internally balanced.
- **Empty Tree Handling:** If $\text{root} == \emptyset$, $\text{checkHeight}$ returns $0 \ne -1$, correctly evaluating to `True`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is visited at most once, performing $O(1)$ operations.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the tree height, for the recursion call stack ($O(\log N)$ for balanced trees, $O(N)$ for skewed trees).