# Guided Example: Count Complete Tree Nodes

We trace the step-by-step subtree depth comparison, perfect binary tree bit-shifting ($2^h$), and sub-linear divide-and-conquer recursion on representative complete binary trees:

- **Input:** $\text{root} = [1, 2, 3, 4, 5, 6]$
- **Required output:** $6$
- **Perfect Binary Tree Instance:** $\text{root} = [1, 2, 3] \implies 3$ ($h_L = h_R \implies 2^2 - 1 = 3$)
- **Single Node Instance:** $\text{root} = [1] \implies 1$
- **Empty Tree Instance:** $\text{root} = [] \implies 0$

This instance demonstrates complete binary tree structural invariants, explains how comparing the left-spine heights of the left and right subtrees identifies which half is a perfect binary tree, replaces full $O(N)$ tree traversal with $O(\log^2 N)$ binary search, and evaluates exact bitwise exponentiation (`1 << h`).

---

## 1. Instance & Teaching Goal

Given the root of a **complete binary tree** with 6 nodes:
```text
        1
       / \
      2   3
     / \  /
    4  5 6
```
Count the total number of nodes in the tree in **strictly less than $O(N)$ time**.

In a standard binary tree, counting nodes requires visiting every node ($O(N)$ DFS/BFS).
However, in a **complete binary tree**, every level except possibly the last is completely filled, and all leaf nodes on the bottom level reside as far left as possible.
This geometric guarantee allows us to determine the exact size of one of the two subtrees in $O(\log N)$ time:
- Measure the leftmost depth of the left child ($h_L$).
- Measure the leftmost depth of the right child ($h_R$).
- **If $h_L == h_R$:** The left subtree is guaranteed to be a **perfect binary tree** of height $h_L$. Its node count is $2^{h_L} - 1$. Together with the root, they contribute $2^{h_L}$ nodes, and we only need to recurse on the right child!
- **If $h_L > h_R$:** The bottom level has not reached the right subtree yet. The right subtree is guaranteed to be a **perfect binary tree** of height $h_R$. Together with the root, they contribute $2^{h_R}$ nodes, and we only need to recurse on the left child!
At each step, one entire subtree is counted in $O(1)$ arithmetic without visiting its nodes!

---

## 2. Conceptual Foundation & Invariants

### Leftmost Spine Depth Function
Define $\text{get\_depth}(\text{node})$:
Traverse down the left pointers:
$$
\text{depth} = 0; \quad \text{while node: } \text{depth} += 1, \, \text{node} = \text{node.left}
$$
Because the tree is complete, the leftmost spine always reaches the bottom-most level of any subtree.

### Recursive Decomposition Protocol:
For current node `root`:
1. If `root is None`, return $0$.
2. Compute $h_L = \text{get\_depth}(\text{root.left})$ and $h_R = \text{get\_depth}(\text{root.right})$.
3. **Case 1 ($h_L == h_R$):**
   The left subtree is completely full to depth $h_L$.
   $$
   \text{Total} = 2^{h_L} + \text{countNodes}(\text{root.right}) = (1 \ll h_L) + \text{countNodes}(\text{root.right})
   $$
4. **Case 2 ($h_L > h_R$):**
   The right subtree is completely full to depth $h_R = h_L - 1$.
   $$
   \text{Total} = 2^{h_R} + \text{countNodes}(\text{root.left}) = (1 \ll h_R) + \text{countNodes}(\text{root.left})
   $$

> **Invariant.** At each recursion level, exactly one child subtree is mathematically proven to be a full perfect binary tree whose size is computed instantly via $(1 \ll h)$, while the algorithm recurses exclusively into the other child.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{root} = [1, 2, 3, 4, 5, 6]$:

### Level 1: Evaluate Root 1
- Examine left child (Node 2):
  - Left spine path: $2 \to 4 \implies h_L = 2$.
- Examine right child (Node 3):
  - Left spine path: $3 \to 6 \implies h_R = 1$.
- Compare heights:
  $$
  h_L = 2 > h_R = 1 \implies \mathbf{\text{Case 2 triggers!}}
  $$
- **Deduction:** The right subtree (rooted at Node 3) is a perfect binary tree of height $h_R = 1$ (containing only Node 3).
- Node 3 + Root 1 contribute $2^{h_R} = 2^1 = \mathbf{2}$ nodes.
- Recurse on left subtree: $\text{countNodes}(\text{Node 2})$.

---

### Level 2: Evaluate Subtree at Node 2
- Examine left child (Node 4):
  - Left spine path: $4 \implies h_L = 1$.
- Examine right child (Node 5):
  - Left spine path: $5 \implies h_R = 1$.
- Compare heights:
  $$
  h_L = 1 == h_R = 1 \implies \mathbf{\text{Case 1 triggers!}}
  $$
- **Deduction:** The left subtree (rooted at Node 4) is a perfect binary tree of height $h_L = 1$ (containing Node 4).
- Node 4 + Root 2 contribute $2^{h_L} = 2^1 = \mathbf{2}$ nodes.
- Recurse on right subtree: $\text{countNodes}(\text{Node 5})$.

---

### Level 3: Evaluate Leaf Node 5
- Node 5 has no children:
  - Left child is None $\implies h_L = 0$.
  - Right child is None $\implies h_R = 0$.
- $h_L == h_R = 0 \implies \text{Case 1 triggers}$:
  $$
  2^0 + \text{countNodes}(\text{None}) = 1 + 0 = \mathbf{1}
  $$

---

### Unwinding Recursion:
- Level 3 returns $1$.
- Level 2 returns $2 + 1 = \mathbf{3}$ (Nodes $\{2, 4, 5\}$).
- Level 1 returns $2 + 3 = \mathbf{6}$ (All nodes $\{1, 2, 3, 4, 5, 6\}$).
Final count: $\mathbf{6}$.

---

## 4. Complete Execution Trace

```text
Tree:
        1
       / \
      2   3
     / \  /
    4  5 6

Node 1:
  h_L = depth(2 -> 4) = 2
  h_R = depth(3 -> 6) = 1
  h_L > h_R -> Right subtree is perfect height 1.
  Total = 2^1 + count(Node 2)

Node 2:
  h_L = depth(4) = 1
  h_R = depth(5) = 1
  h_L == h_R -> Left subtree is perfect height 1.
  Total = 2^1 + count(Node 5)

Node 5:
  h_L = 0, h_R = 0 -> Leaf node -> Total = 2^0 + 0 = 1

Unwind:
  count(Node 2) = 2 + 1 = 3
  count(Node 1) = 2 + 3 = 6
```

| Recursion Frame | Target Node | Left Spine $h_L$ | Right Spine $h_R$ | Active Case | Perfect Subtree Contribution | Recursed Child |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Frame 1** | **Node 1** | 2 | 1 | $h_L > h_R$ | Right child + Root $= 2^1 = 2$ | Left (Node 2) |
| **Frame 2** | **Node 2** | 1 | 1 | $h_L == h_R$ | Left child + Root $= 2^1 = 2$ | Right (Node 5) |
| **Frame 3** | **Node 5** | 0 | 0 | $h_L == h_R$ | Node 5 $= 2^0 = 1$ | None |
| **Result** | - | - | - | - | **$2 + 2 + 1 = \mathbf{6}$** | - |

---

## 5. Algorithmic Correctness

**Soundness.** A complete binary tree filled to height $h$ has exactly $2^h - 1$ nodes. Adding the root yields $2^h$ nodes. When $h_L == h_R$, the bottom level has begun populating the right subtree, meaning the left subtree must be completely filled with height $h_L$. When $h_L > h_R$, the bottom level has not reached the right subtree yet, meaning the right subtree is completely filled with height $h_L - 1$. The bit shift `1 << h` mathematically evaluates this count without inspecting individual nodes.

**Completeness.** At each recursive step, the tree height decreases by 1. The base case `root is None` returns 0. Every node in the tree is either part of an arithmetic perfect subtree evaluation or the root of a recursed frame, ensuring an exact total count.

---

## 6. Traps This Instance Exposes

- **Linear $O(N)$ Traversal:** Counting nodes with `1 + count(root.left) + count(root.right)` visits every node in $O(N)$ time. The problem explicitly asks for less than $O(N)$ complexity ($O(\log^2 N)$).
- **Off-by-One in Depth:** A leaf node has left child `None`, so `depth = 0`. Its contribution is $2^0 = 1$ node.
- **Empty Tree:** When `root is None`, `countNodes` returns $0$ immediately.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log^2 N)$. The height of a complete binary tree with $N$ nodes is $h = \lfloor \log_2 N \rfloor$. At each recursion level, computing left spine depths takes $O(\log N)$ time. The recursion tree descends exactly $h$ times (one branch per level). Total time is $O(h \cdot h) = O(\log^2 N)$. For $N = 50,000$, $\log^2 N \approx 16^2 = 256$ operations, which is thousands of times faster than $O(N)$.
- **Auxiliary Space Complexity:** $O(\log N)$ call stack space for recursion depth.