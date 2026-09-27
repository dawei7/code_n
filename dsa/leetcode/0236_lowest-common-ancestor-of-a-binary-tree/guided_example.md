# Guided Example: Lowest Common Ancestor of a Binary Tree

We trace the step-by-step post-order recursive divide-and-conquer, subtree status bubbling, and ancestor convergence on representative binary trees:

- **Input:** $\text{root} = [3, 5, 1, 6, 2, 0, 8, \text{null}, \text{null}, 7, 4], \quad p = 5, \quad q = 1$
- **Required output:** $3$ (Target $p = 5$ is in the left subtree; target $q = 1$ is in the right subtree; Root $3$ joins both subtrees)
- **Self-Ancestor Instance:** $p = 5, \quad q = 4 \implies 5$ (Target $4$ is a descendant of $5$; Node $5$ is the LCA of itself and $4$)
- **Two Leaves in Same Subtree:** $p = 7, \quad q = 4 \implies 2$ (Both descend from Node $2$)

This instance demonstrates recursive divide-and-conquer on arbitrary binary trees without ordering properties, proves why returning `root` when both `left` and `right` are non-null correctly identifies the unique lowest common ancestor, handles self-descendant queries without traversing deeper subtrees, and operates in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given a general binary tree (not a BST) and two nodes $p = 5$ and $q = 1$:
```text
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```
Find their Lowest Common Ancestor (LCA).

Unlike a Binary Search Tree (where node values direct the search left or right), a general binary tree has no value ordering. Target nodes can appear in arbitrary subtrees.
A recursive post-order traversal explores subtrees bottom-up:
- If a subtree contains neither $p$ nor $q$, it returns `None`.
- If a subtree contains $p$ or $q$, it bubbles up a pointer to that node.
- If a node receives a non-null return from **both its left and right children**, then $p$ and $q$ reside in different branches of that node. That node is **the unique Lowest Common Ancestor**!

---

## 2. Conceptual Foundation & Invariants

### Recursive Contract `lowestCommonAncestor(root, p, q)`
The function returns:
1. `root` if `root` is $p$, $q$, or the confirmed LCA.
2. `None` if neither $p$ nor $q$ exists in the subtree.
3. A non-null reference to $p$ or $q$ if exactly one of them is in the subtree.

### Transition Rules:
1. **Base Case:**
   If `root is None`: return `None`.
   If `root == p or root == q`: return `root`.
2. **Subtree Exploration:**
   $$
   \text{left} = \text{lowestCommonAncestor}(\text{root.left}, p, q)
   $$
   $$
   \text{right} = \text{lowestCommonAncestor}(\text{root.right}, p, q)
   $$
3. **Combination:**
   - **Both Children Non-Null ($\text{left and right}$):**
     Target $p$ was found in one child and target $q$ in the other.
     $$
     \text{return root} \quad (\text{Root is the LCA!})
     $$
   - **Only One Child Non-Null:**
     Pass the non-null result upward:
     $$
     \text{return left if left is not None else right}
     $$
   - **Both Null:**
     Return `None`.

> **Invariant.** If both $p$ and $q$ are in the subtree at `root`, the returned node is their unique Lowest Common Ancestor. If exactly one is present, that node itself is returned.

---

## 3. Step-by-Step Worked Execution

We trace the recursive execution for two representative queries:

### Query 1: $p = 5, \, q = 1$ on Root 3
1. **At Root 3:**
   - Root is neither $p$ nor $q$.
   - Call left: $\text{LCA}(\text{Node 5}, 5, 1)$.
2. **Left Branch at Node 5:**
   - Base case matches: $\text{root} == p$ ($5 == 5$)!
   - Immediately return $\text{Node 5}$!
   - *(Note: Children of 5 are not explored, because if $q$ were below $5$, $5$ would still be the LCA)*.
3. **Right Branch at Node 1:**
   - Call right: $\text{LCA}(\text{Node 1}, 5, 1)$.
   - Base case matches: $\text{root} == q$ ($1 == 1$)!
   - Immediately return $\text{Node 1}$!
4. **Aggregation at Root 3:**
   - Left child returned: $\text{Node 5}$ ($\ne \text{None}$).
   - Right child returned: $\text{Node 1}$ ($\ne \text{None}$).
   - Since both $\text{left}$ and $\text{right}$ are non-null, Root 3 is the split point!
   - **Return $\text{Node 3}$.**

---

### Query 2: $p = 5, \, q = 4$ (Self-Ancestor Case)
1. **At Root 3:**
   - Call left on Node 5.
2. **At Node 5:**
   - $\text{root} == p$ ($5 == 5$)!
   - Base case triggers immediately: **returns $\text{Node 5}$**.
3. **Right Branch of Root 3 (Node 1):**
   - Explores Node 0 (returns `None`) and Node 8 (returns `None`).
   - Node 1 returns `None`.
4. **Aggregation at Root 3:**
   - Left returned $\text{Node 5}$.
   - Right returned `None`.
   - Aggregation rule: $\text{left if left else right} \implies \mathbf{\text{Node 5}}$.
   - **Final LCA is $\text{Node 5}$.**
   *(Even though Node 4 was in the subtree of 5, short-circuiting at Node 5 was completely valid because 5 is the ancestor of 4!)*.

---

### Query 3: $p = 7, \, q = 4$ (Internal Subtree LCA)
1. At Node 5: calls left child Node 6 (returns `None`), calls right child Node 2.
2. At Node 2:
   - Left child Node 7: matches $p = 7 \implies$ returns $\text{Node 7}$.
   - Right child Node 4: matches $q = 4 \implies$ returns $\text{Node 4}$.
   - At Node 2: both `left` and `right` are non-null $\implies$ **returns $\text{Node 2}$**.
3. Back at Node 5:
   - `left` is `None` (from Node 6), `right` is Node 2.
   - Node 5 returns $\text{Node 2}$.
4. Back at Root 3:
   - `left` is Node 2, `right` is `None`.
   - Root 3 returns $\mathbf{\text{Node 2}}$.

---

## 4. Complete Execution Trace

```text
Query 1: p = 5, q = 1
Root 3:
  -> Left child 5: matches p -> returns 5
  -> Right child 1: matches q -> returns 1
  Both children returned non-null! -> LCA = 3

Query 2: p = 5, q = 4
Root 3:
  -> Left child 5: matches p -> returns 5
  -> Right child 1: no targets found -> returns None
  Only left returned non-null -> LCA = 5

Query 3: p = 7, q = 4
Node 2:
  -> Left child 7: matches p -> returns 7
  -> Right child 4: matches q -> returns 4
  Both children returned non-null -> returns 2
Node 2 bubbles up through Node 5 and Node 3 -> LCA = 2
```

| Traversal Node | Left Subtree Result | Right Subtree Result | Decision Rule Applied | Result Bubbled Up |
|:---:|:---:|:---:|:---|:---:|
| Node 5 | - | - | Base case ($== p$) | Node 5 |
| Node 1 | - | - | Base case ($== q$) | Node 1 |
| **Node 3 (Root)** | **Node 5** | **Node 1** | **Both non-null $\implies \text{left and right}$** | **$\mathbf{Node 3}$ (LCA)** |
| Node 6 | `None` | `None` | Both null | `None` |
| Node 7 | - | - | Base case ($== p$) | Node 7 |
| Node 4 | - | - | Base case ($== q$) | Node 4 |
| **Node 2** | **Node 7** | **Node 4** | **Both non-null $\implies$ LCA at 2** | **Node 2** |

---

## 5. Algorithmic Correctness

**Soundness.** A node $u$ receives non-null values from both its left and right children if and only if one target is in $u$'s left subtree and the other target is in $u$'s right subtree. In that case, $u$ is an ancestor of both nodes, and no child of $u$ can be an ancestor of both nodes. Therefore, $u$ is the lowest common ancestor.

**Completeness.** Since $p$ and $q$ are guaranteed to exist as distinct nodes in the tree, either they reside in disjoint subtrees (triggering the dual-child match at their LCA) or one is an ancestor of the other (caught at the upper node by the base case). In both cases, the exact LCA is returned.

---

## 6. Traps This Instance Exposes

- **Over-Exploring Subtrees:** When `root == p`, returning `root` immediately without exploring its subtrees is correct even if $q$ is located inside $p$'s subtree. If $q$ were inside, $p$ is the LCA; if $q$ were outside, the other branch will find $q$ and combine with $p$ higher up.
- **Node Values vs Object Identity:** Tree node values are unique in LeetCode 236, but comparing node pointers (`root == p` or `root is p`) is more robust than comparing integer values.
- **Returning Boolean vs Node Reference:** Some recursive formulations return boolean flags (`found_p`, `found_q`). Bubbling the `TreeNode` reference itself allows returning the node directly without extra global variables.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the total number of nodes in the binary tree. In the worst case, every node in the tree is visited once.
- **Auxiliary Space Complexity:** $O(H)$ auxiliary memory for the call stack, where $H$ is the height of the tree ($O(\log N)$ for balanced trees, $O(N)$ for skewed trees).