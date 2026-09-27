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

### Every Left Spine This Instance Walks

Only four spines are ever measured, and two of the six nodes are never touched at all. This table accounts for both the measurements and the omissions, because the omissions are what make the method sub-linear.

| Node | Left-spine path | Spine length (nodes counted) | Consulted by | Why that path is the deepest path of its subtree |
|:---|:---|:---:|:---|:---|
| Node 2 | $2 \to 4 \to \text{None}$ | 2 | Frame 1, as $h_L$ | Node 2's subtree occupies two levels, and completeness puts the leftmost node of the lower level beneath the leftmost parent |
| Node 3 | $3 \to 6 \to \text{None}$ | 2 | Frame 1, as $h_R$ | Node 3's subtree also occupies two levels, and that equality is exactly what makes the root fire Case 1 |
| Node 6 | $6 \to \text{None}$ | 1 | Frame 2, as $h_L$ | Node 6 is a leaf, so its spine is itself and nothing more |
| the missing right child of Node 3 | empty | 0 | Frame 2, as $h_R$; frame 3, as both children | An absent child contributes no node, so its spine length is 0 and the frame's own node is paid for by $2^0$ |
| Node 4 | $4 \to \text{None}$ | 1 | never measured | Node 4 lies inside the perfect left subtree detected at frame 1, so its size is included in the arithmetic payment $2^2$ |
| Node 5 | $5 \to \text{None}$ | 1 | never measured | Same reason: frame 1 never descends into Nodes 4 or 5 |
| Node 1 | $1 \to 2 \to 4 \to \text{None}$ | 3 | never measured | A frame measures only the spines of its two children, so the root's own spine is never walked |

Each frame therefore costs one spine walk of length at most $h$ plus one arithmetic step, and the number of frames equals the number of levels along the un-counted side — three frames for six nodes.

### Level 1: Evaluate Root 1
- Examine left child (Node 2):
  - Left spine path: $2 \to 4 \implies h_L = 2$.
- Examine right child (Node 3):
  - Left spine path: $3 \to 6 \implies h_R = 2$.
- Compare heights:
  $$
  h_L = 2 == h_R = 2 \implies \mathbf{\text{Case 1 triggers!}}
  $$
- **Deduction:** The left subtree (rooted at Node 2) is a perfect binary tree of height $h_L = 2$ (containing Nodes 2, 4, 5).
- Node 2's perfect subtree + Root 1 contribute $2^{h_L} = 2^2 = \mathbf{4}$ nodes.
- Recurse on right subtree: $\text{countNodes}(\text{Node 3})$.

---

### Level 2: Evaluate Subtree at Node 3
- Examine left child (Node 6):
  - Left spine path: $6 \implies h_L = 1$.
- Examine right child (None):
  - A missing child has no spine at all, so $h_R = 0$.
- Compare heights:
  $$
  h_L = 1 > h_R = 0 \implies \mathbf{\text{Case 2 triggers!}}
  $$
- **Deduction:** The right subtree of Node 3 is the empty perfect binary tree of height $h_R = 0$; the bottom level stopped before reaching it.
- Node 3 and that empty subtree contribute $2^{h_R} = 2^0 = \mathbf{1}$ node.
- Recurse on left subtree: $\text{countNodes}(\text{Node 6})$.

---

### Level 3: Evaluate Leaf Node 6
- Node 6 has no children:
  - Left child is None $\implies h_L = 0$.
  - Right child is None $\implies h_R = 0$.
- $h_L == h_R = 0 \implies \text{Case 1 triggers}$:
  $$
  2^0 + \text{countNodes}(\text{None}) = 1 + 0 = \mathbf{1}
  $$

---

### Unwinding Recursion:
- Level 3 returns $1$.
- Level 2 returns $1 + 1 = \mathbf{2}$ (Nodes $\{3, 6\}$).
- Level 1 returns $4 + 2 = \mathbf{6}$ (All nodes $\{1, 2, 3, 4, 5, 6\}$).
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
  h_R = depth(3 -> 6) = 2
  h_L == h_R -> Left subtree is perfect height 2.
  Total = 2^2 + count(Node 3)

Node 3:
  h_L = depth(6) = 1
  h_R = depth(None) = 0
  h_L > h_R -> Right subtree is empty (perfect height 0).
  Total = 2^0 + count(Node 6)

Node 6:
  h_L = 0, h_R = 0 -> Leaf node -> Total = 2^0 + 0 = 1

Unwind:
  count(Node 3) = 1 + 1 = 2
  count(Node 1) = 4 + 2 = 6
```

| Recursion Frame | Target Node | Left Spine $h_L$ | Right Spine $h_R$ | Active Case | Perfect Subtree Contribution | Recursed Child |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Frame 1** | **Node 1** | 2 | 2 | $h_L == h_R$ | Left child + Root $= 2^2 = 4$ | Right (Node 3) |
| **Frame 2** | **Node 3** | 1 | 0 | $h_L > h_R$ | Empty right child + Root $= 2^0 = 1$ | Left (Node 6) |
| **Frame 3** | **Node 6** | 0 | 0 | $h_L == h_R$ | Node 6 $= 2^0 = 1$ | None |
| **Result** | - | - | - | - | **$4 + 1 + 1 = \mathbf{6}$** | - |

---

## 5. Algorithmic Correctness

**Soundness.** A complete binary tree filled to height $h$ has exactly $2^h - 1$ nodes. Adding the root yields $2^h$ nodes. When $h_L == h_R$, the bottom level has begun populating the right subtree, meaning the left subtree must be completely filled with height $h_L$. When $h_L > h_R$, the bottom level has not reached the right subtree yet, meaning the right subtree is completely filled with height $h_L - 1$. The bit shift `1 << h` mathematically evaluates this count without inspecting individual nodes.

**Completeness.** At each recursive step, the tree height decreases by 1. The base case `root is None` returns 0. Every node in the tree is either part of an arithmetic perfect subtree evaluation or the root of a recursed frame, ensuring an exact total count.

**Shape boundaries, and the frames that decide each one.** The degenerate shapes are where the spine-length convention is tested hardest, because a missing child must measure $0$ rather than being skipped. The empty, single-node, six-node and seven-node rows are the package's own shapes; the two sparse rows are constructed extremes that exercise Case 2 with an empty right subtree.

| Shape | Level-order input | Answer | Frames taken, and the fact that settles the count |
|:---|:---|:---:|:---|
| Empty tree | `[]` | 0 | The base case returns 0 before any spine is measured, so no frame ever reads a child |
| Single node | `[1]` | 1 | Frame 1 finds $h_L = h_R = 0$ with both children absent, so Case 1 pays $2^0 + \text{count}(\text{None}) = 1$ |
| Root with only a left child | `[1, 2]` | 2 | Frame 1: $h_L = 1$ against $h_R = 0$ fires Case 2 and pays $2^0 = 1$ for the root alone; the recursion then pays 1 more for the leaf |
| Perfect three-node tree | `[1, 2, 3]` | 3 | Frame 1: $h_L = h_R = 1$ fires Case 1 and pays $2^1 = 2$ for the root plus Node 2; frame 2 handles Node 3 as a leaf |
| Left-leaning chain | `[1, 2, null, 3]` | 3 | $h_R$ stays $0$ at every frame, so Case 2 fires twice and the frame count equals the number of levels: $1 + 1 + 1 = 3$ |
| The six-node instance traced above | `[1, 2, 3, 4, 5, 6]` | 6 | Case 1 at the root pays $2^2 = 4$, Case 2 at Node 3 pays $2^0 = 1$, and the leaf frame pays 1 |
| Perfect seven-node tree | `[1, 2, 3, 4, 5, 6, 7]` | 7 | Case 1 pays 4 at the root, 2 at Node 3 and 1 at Node 7: $4 + 2 + 1 = 7$. A perfect tree is never recognised in a single step at the root, because Case 1 still recurses into the right child |

---

## 6. Traps This Instance Exposes

- **Linear $O(N)$ Traversal:** Counting nodes with `1 + count(root.left) + count(root.right)` visits every node in $O(N)$ time. The problem explicitly asks for less than $O(N)$ complexity ($O(\log^2 N)$).
- **Off-by-One in Depth:** A leaf node has left child `None`, so `depth = 0`. Its contribution is $2^0 = 1$ node.
- **Empty Tree:** When `root is None`, `countNodes` returns $0$ immediately.

**Alternative formulations, and the cost each one carries.** All four methods return $6$ on the traced tree; they differ in how much of the tree they must actually look at.

| Approach | Mechanism | Time | Auxiliary space | Failure mode or tradeoff |
|:---|:---|:---:|:---:|:---|
| Full traversal (DFS or BFS) | Visit every node and add one per visit | $O(N)$ | $O(\log N)$ stack or $O(N)$ queue | Trivially correct, but the follow-up asks for strictly better than $O(N)$, and a complete tree with $N = 50{,}000$ forces $50{,}000$ visits where the spine method needs at most $256$ steps |
| Left-spine comparison recursion (the method traced here) | Measure both children's leftmost spine lengths, pay $2^{h}$ for the perfect side plus the root, and recurse into the other child | $O(\log^2 N)$ | $O(\log N)$ call stack | Requires one consistent convention: a leaf measures $1$ and a missing child measures $0$. Mixing that with edge counts breaks the case analysis and produces a total that is off by a factor rather than by one |
| Iterative spine accumulation | Keep the current frame node in a variable, add $1 \ll h$ to a running total, and move to the un-counted child in a loop | $O(\log^2 N)$ | $O(1)$ | Same arithmetic as the recursion with no call stack, but the loop must pay for the terminal frame as well; omitting the final $2^0 = 1$ under-counts every tree by exactly one node |
| Binary search over the last level with bit-path probes | Measure the height, binary-search how many nodes the last level holds, and test a candidate position by descending from the root and reading the position's bits as left/right choices | $O(\log^2 N)$ | $O(1)$ | Each probe still costs one root-to-bottom walk, so the constant factor is larger than the spine method's, and inverting the bit convention (dropping the leading bit, $0$ for left, $1$ for right) silently returns a plausible but wrong count |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log^2 N)$. The height of a complete binary tree with $N$ nodes is $h = \lfloor \log_2 N \rfloor$. At each recursion level, computing left spine depths takes $O(\log N)$ time. The recursion tree descends exactly $h$ times (one branch per level). Total time is $O(h \cdot h) = O(\log^2 N)$. For $N = 50,000$, $\log^2 N \approx 16^2 = 256$ operations, which is thousands of times faster than $O(N)$.
- **Auxiliary Space Complexity:** $O(\log N)$ call stack space for recursion depth.