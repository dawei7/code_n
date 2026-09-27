# Guided Example: Lowest Common Ancestor of a Binary Search Tree

We trace the step-by-step BST value-directed navigation, divergence split detection, and iterative pointer descent on representative Binary Search Trees:

- **Input:** $\text{root} = [6, 2, 8, 0, 4, 7, 9, \text{null}, \text{null}, 3, 5], \quad p = 2, \quad q = 8$
- **Required output:** $6$ (Root $6$ has $p = 2$ in its left subtree and $q = 8$ in its right subtree; path divergence occurs at $6$)
- **Self-Descendant Instance:** $p = 2, \quad q = 4 \implies 2$ (Node $2$ is the ancestor of its own child $4$)
- **Subtree Internal Split:** $p = 3, \quad q = 5 \implies 4$ (Both descend into left subtree of $6$, then into right child $4$, splitting at $4$)

This instance demonstrates exploiting the Binary Search Tree ordering invariant ($\text{Left} < \text{Root} < \text{Right}$) to eliminate backtracking, mathematically proves why the first node where paths diverge is the unique lowest common ancestor, achieves strictly $O(H)$ runtime, and executes in $O(1)$ auxiliary space without recursion.

---

## 1. Instance & Teaching Goal

Given the root of a Binary Search Tree (BST) and two query nodes $p = 2$ and $q = 8$:
```text
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5
```
Find the **Lowest Common Ancestor (LCA)** of $p$ and $q$.

By definition, the Lowest Common Ancestor is the deepest node in the tree that has both $p$ and $q$ as descendants (allowing a node to be a descendant of itself).
In an arbitrary binary tree, finding the LCA requires a full $O(N)$ post-order traversal searching both subtrees.
In a **Binary Search Tree**, value ordering provides immediate directional steering:
- If both nodes are smaller than the current node, both must lie in the **left subtree**.
- If both nodes are larger than the current node, both must lie in the **right subtree**.
- The very first node where this symmetry breaks (where $p$ and $q$ fall on opposite sides, or where one equals the current node) is **guaranteed to be the Lowest Common Ancestor**!

---

## 2. Conceptual Foundation & Invariants

### The BST Divergence Principle
For any current node `curr`:
1. **Both on Left ($\min(p\text{.val}, q\text{.val}) < \text{curr.val}$ and $\max(p\text{.val}, q\text{.val}) < \text{curr.val}$):**
   Both targets are in the left subtree. Advance:
   $$
   \text{curr} \leftarrow \text{curr.left}
   $$
2. **Both on Right ($\min(p\text{.val}, q\text{.val}) > \text{curr.val}$ and $\max(p\text{.val}, q\text{.val}) > \text{curr.val}$):**
   Both targets are in the right subtree. Advance:
   $$
   \text{curr} \leftarrow \text{curr.right}
   $$
3. **The Divergence Point (Split):**
   If neither condition holds:
   - Either $p\text{.val} \le \text{curr.val} \le q\text{.val}$ (they lie in opposite subtrees),
   - Or $\text{curr.val} == p\text{.val}$ (one target is the ancestor of the other),
   - Or $\text{curr.val} == q\text{.val}$.
   `curr` is the lowest common ancestor! Return `curr` immediately.

> **Invariant.** The lowest common ancestor of $p$ and $q$ is guaranteed to reside in the subtree rooted at `curr`. When `curr` falls between $p\text{.val}$ and $q\text{.val}$ inclusive, `curr` is the LCA.

---

## 3. Step-by-Step Worked Execution

We trace the traversal for two representative queries on the tree:

### Execution 1: Query $p = 2, \, q = 8$
Start at $\text{curr} = \text{Node } 6$.
- Examine values: $p\text{.val} = 2, \, q\text{.val} = 8, \, \text{curr.val} = 6$.
- Compare:
  $$
  2 < 6 \quad \text{and} \quad 8 > 6
  $$
- Target $p$ lies in the left subtree, while target $q$ lies in the right subtree.
- Divergence detected!
- Root Node $6$ is the Lowest Common Ancestor.
- **Return $\text{Node } 6$.** (Completed in 1 step!).

---

### Execution 2: Query $p = 2, \, q = 4$ (Self-Descendant Case)
Start at $\text{curr} = \text{Node } 6$.
- **Step 1 (At Node 6):**
  - $p\text{.val} = 2 < 6$ and $q\text{.val} = 4 < 6$.
  - Both targets are strictly smaller than $6$.
  - Both descend into the left subtree: $\text{curr} \leftarrow \text{curr.left}$ (Node 2).
- **Step 2 (At Node 2):**
  - $p\text{.val} = 2 == \text{curr.val}$.
  - $q\text{.val} = 4 > \text{curr.val}$.
  - Current node matches $p$, and $q$ is in its right child subtree.
  - Node $2$ is an ancestor of Node $4$, and is a descendant of itself.
  - Divergence condition met!
  - **Return $\text{Node } 2$.**

---

### Execution 3: Query $p = 3, \, q = 5$ (Deep Subtree Split)
- **At Node 6:** Both $3, 5 < 6 \implies$ Go left to Node 2.
- **At Node 2:** Both $3, 5 > 2 \implies$ Go right to Node 4.
- **At Node 4:**
  - $3 < 4$ (Node 3 is in left child).
  - $5 > 4$ (Node 5 is in right child).
  - Split occurs at Node 4!
  - **Return $\text{Node } 4$.**

---

## 4. Complete Execution Trace

```text
Query 1: p = 2, q = 8
curr = 6: 2 < 6 and 8 > 6 -> SPLIT DETECTED -> LCA = 6

Query 2: p = 2, q = 4
curr = 6: 2 < 6 and 4 < 6 -> go left to 2
curr = 2: 2 == 2 (curr == p) -> SPLIT DETECTED -> LCA = 2

Query 3: p = 3, q = 5
curr = 6: 3 < 6 and 5 < 6 -> go left to 2
curr = 2: 3 > 2 and 5 > 2 -> go right to 4
curr = 4: 3 < 4 and 5 > 4 -> SPLIT DETECTED -> LCA = 4
```

| Query Query $(p, q)$ | Current Node | $\text{curr.val}$ | Left Condition ($p, q < \text{curr}$) | Right Condition ($p, q > \text{curr}$) | Decision / Transition |
|:---:|:---:|:---:|:---:|:---:|:---|
| $(2, 8)$ | Node 6 | 6 | False ($8 \not< 6$) | False ($2 \not> 6$) | **Split point $\implies \mathbf{6}$** |
| $(2, 4)$ | Node 6 | 6 | **True** ($2, 4 < 6$) | False | Advance left $\to$ Node 2 |
| $(2, 4)$ | Node 2 | 2 | False | False ($p == \text{curr}$) | **Self-ancestor $\implies \mathbf{2}$** |
| $(3, 5)$ | Node 6 | 6 | **True** ($3, 5 < 6$) | False | Advance left $\to$ Node 2 |
| $(3, 5)$ | Node 2 | 2 | False | **True** ($3, 5 > 2$) | Advance right $\to$ Node 4 |
| $(3, 5)$ | Node 4 | 4 | False | False | **Split point $\implies \mathbf{4}$** |

---

## 5. Algorithmic Correctness

**Soundness.** If both $p$ and $q$ are in the left subtree of `curr`, any common ancestor must also be in the left subtree (since `curr` cannot be the lowest if a deeper node contains both). When `curr` separates $p$ and $q$ into different subtrees, no child of `curr` can contain both nodes simultaneously. Thus, `curr` must be the lowest common ancestor.

**Completeness.** Since $p$ and $q$ are guaranteed to exist in the BST, the search path must eventually reach either the split node or one of the query nodes, terminating with the exact LCA.

---

## 6. Traps This Instance Exposes

- **Treating BST as General Binary Tree:** Using LeetCode 236's post-order DFS visits all $N$ nodes in $O(N)$ time. The BST property enables directed bisection in $O(H)$ time.
- **Node as Its Own Ancestor:** If $p$ is an ancestor of $q$, the traversal stops at $p$ because $q$ is in a child subtree. The algorithm naturally handles $p == \text{curr}$ without special branching.
- **Unordered Inputs ($p > q$):** The code must handle cases where $p\text{.val} > q\text{.val}$ just as easily as $p\text{.val} < q\text{.val}$. Testing `p.val < curr.val and q.val < curr.val` handles any input order.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(H)$, where $H$ is the height of the BST. In each step, the algorithm descends one level down the tree.
  - In a balanced BST: $H = O(\log N)$.
  - In a degenerate linked-list tree: $H = O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant memory when using an iterative `while` loop (or $O(H)$ call stack space if written recursively).