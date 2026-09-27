# Guided Example: Inorder Successor in BST

We trace the step-by-step binary search tree descent, ancestor successor candidate recording, left-subtree refinement, and null boundary termination on representative BST instances:

- **Input:** $\text{root} = [2, 1, 3], \quad p = 1$
- **Required output:** Node with value $2$ (In-order traversal order is $[1, 2, 3]$; immediate successor of $1$ is $2$)
- **Ancestor Successor Instance:** $\text{root} = [5, 3, 6, 2, 4, \text{null}, \text{null}, 1], \quad p = 4 \implies 5$ (Node 4 has no right child; successor is its lowest ancestor whose left child contains 4)
- **Maximum Node (No Successor):** $\text{root} = [5, 3, 6], \quad p = 6 \implies \text{null}$ (6 is the maximum value in the BST; returns null)
- **Subtree Successor (Right Child Exists):** Node $p$ with a non-empty right subtree has its successor at the leftmost node of that right subtree

This instance demonstrates binary search tree property exploitation for order statistics, explains why tracking the last left-branching ancestor correctly identifies the in-order successor in $O(H)$ time without parent pointers or full tree flattening, and operates in strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given the root of a binary search tree and target node $p = 1$:
```text
Tree topology:
      2
     / \
    1   3
```
Find the **in-order successor** of $p$ in the BST (the node with the smallest key strictly greater than $p.\text{val}$).
In-order traversal: $[1, 2, 3]$.
Immediate successor of node $1$ is node $\mathbf{2}$.

### Why In-Order Traversal is Suboptimal
- Flattening the tree into an array via in-order DFS takes $O(N)$ time and $O(N)$ auxiliary memory.
- In a BST, we can locate the successor in **$O(H)$ time** ($H \le N$ is tree height) using standard BST descent:
  - If $\text{curr.val} > p.\text{val}$: Node $\text{curr}$ is a candidate successor! But a smaller valid candidate might exist in its left subtree. We save $\text{successor} = \text{curr}$ and branch **left**.
  - If $\text{curr.val} \le p.\text{val}$: Neither $\text{curr}$ nor any node in its left subtree can be greater than $p.\text{val}$. We discard the entire left subtree and branch **right**.

---

## 2. Conceptual Foundation & Invariants

### Iterative BST Successor Protocol
Initialize `successor = None` and pointer `curr = root`:
While `curr` is not None:
- **Case 1: $p.\text{val} < \text{curr.val}$**
  Node `curr` is strictly greater than $p$. It is currently the best known ancestor greater than $p$.
  $$
  \text{successor} \leftarrow \text{curr}
  $$
  Could an even smaller node still be greater than $p$?
  Yes, in `curr`'s left subtree!
  $$
  \text{curr} \leftarrow \text{curr.left}
  $$
- **Case 2: $p.\text{val} \ge \text{curr.val}$**
  Node `curr` is less than or equal to $p$, so it cannot be a successor.
  Furthermore, all nodes in `curr.left` are strictly smaller than $\text{curr.val} \le p.\text{val}$, so none of them can be the successor either.
  The successor must lie in the right subtree:
  $$
  \text{curr} \leftarrow \text{curr.right}
  $$

When `curr` reaches `None`, the recorded `successor` is guaranteed to be the exact in-order successor (or `None` if $p$ is the maximum node in the tree).

> **Invariant.** `successor` always stores the node with the smallest value strictly greater than $p.\text{val}$ among all ancestors traversed so far. Any pruned subtree is provably incapable of containing a valid successor smaller than `successor`.

---

## 3. Step-by-Step Worked Execution

We trace the search on $\text{root} = [2, 1, 3]$ with $p = 1$:
Initial state: `successor = None, curr = Node(2)`.

---

### Step 1: Visit Node 2 (Root)
- Node value: $\text{curr.val} = 2$.
- Target value: $p.\text{val} = 1$.
- Compare:
  $$
  p.\text{val} < \text{curr.val} \iff 1 < 2 \quad (\mathbf{\text{True}})
  $$
- Node 2 is greater than 1 $\implies$ Candidate successor!
  $$
  \text{successor} \leftarrow \text{Node}(2)
  $$
- Branch left to search for a closer successor:
  $$
  \text{curr} \leftarrow \text{curr.left} = \text{Node}(1)
  $$

---

### Step 2: Visit Node 1
- Node value: $\text{curr.val} = 1$.
- Target value: $p.\text{val} = 1$.
- Compare:
  $$
  p.\text{val} < \text{curr.val} \iff 1 < 1 \quad (\mathbf{\text{False}})
  $$
- $p.\text{val} \ge \text{curr.val}$ ($1 \ge 1$). Node 1 cannot be strictly greater than itself.
- Branch right:
  $$
  \text{curr} \leftarrow \text{curr.right} = \text{None}
  $$
- `successor` remains `Node(2)`.

---

### Step 3: Termination
- `curr` is `None`. Loop terminates.
- Final successor: $\text{Node}(2)$.
Output value: $\mathbf{2}$.

---

### Extended Trace: Deep Ancestor Successor
Consider $\text{root} = [5, 3, 6, 2, 4, \text{null}, \text{null}, 1]$ with $p = 4$:
```text
          5
         / \
        3   6
       / \
      2   4
     /
    1
```
1. At Node 5: $4 < 5 \implies \text{successor} = 5, \quad \text{curr} \leftarrow 3$.
2. At Node 3: $4 \ge 3 \implies \text{curr} \leftarrow 4$ (`successor` stays 5).
3. At Node 4: $4 \ge 4 \implies \text{curr} \leftarrow \text{curr.right} = \text{None}$ (`successor` stays 5).
4. Terminates with $\text{successor} = \mathbf{5}$! (Correct: in-order sequence is $1, 2, 3, 4, \mathbf{5}, 6$).

---

## 4. Complete Execution Trace

```text
root = [2, 1, 3], p = 1
successor = None, curr = 2

Step 1: curr = 2
  p.val < curr.val (1 < 2) -> successor = 2, curr = curr.left (1)

Step 2: curr = 1
  p.val >= curr.val (1 >= 1) -> curr = curr.right (None)

curr is None -> Terminate
Result: Node(2)
```

| Step | Current Node | $\text{curr.val}$ | Comparison with $p.\text{val} = 1$ | Candidate Updated? | Recorded `successor` | Next Direction |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | Root | 2 | $1 < 2$ | **Yes** | **Node(2)** | Left ($\text{curr} \leftarrow 1$) |
| 2 | Left | 1 | $1 \ge 1$ | No | Node(2) | Right ($\text{curr} \leftarrow \text{None}$) |
| **End** | $\text{None}$ | - | - | - | **Node(2)** | **Terminates** |

---

## 5. Algorithmic Correctness

**Soundness.** A node is recorded as `successor` only when its value is strictly greater than $p.\text{val}$. When branching left, any newly recorded candidate will have a value strictly smaller than the previous candidate but still strictly greater than $p.\text{val}$. Thus, `successor` always tracks the tightest upper bound found.

**Completeness.** By the BST ordering property, if $p$ has a right subtree, the successor is the minimum node in that right subtree, which our algorithm reaches by turning left at all descendants $> p.\text{val}$. If $p$ has no right subtree, the successor is the lowest ancestor whose left child contains $p$, which is exactly the last node where the descent turned left. If $p$ is the maximum node in the BST, the algorithm never turns left, and `successor` remains `None`.

---

## 6. Traps This Instance Exposes

- **Target Has No Right Subtree:** When $p$ has no right child (e.g. node 4 in the extended example), many implementations fail by searching only down $p$'s subtrees. Tracking the last left-branching ancestor during the top-down descent seamlessly finds the ancestor successor.
- **Strict Inequality ($>$ vs $\ge$):** The successor must be **strictly greater** than $p.\text{val}$. At $\text{curr.val} == p.\text{val}$, the code must branch right without recording `curr` as a successor candidate.
- **Handling Non-Existent Successor:** If $p$ is the largest element in the BST (e.g. $p = 6$ in $[5, 3, 6]$), `p.val < curr.val` is never true. `successor` remains `None`, correctly returning `null`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(H)$, where $H$ is the height of the binary search tree. Each iteration descends one level down the tree, performing $O(1)$ operations. For balanced BSTs, $H = O(\log N)$; in the worst case (skewed tree), $H = O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory. The algorithm uses an iterative loop with two node pointer references without recursion or stack allocation.