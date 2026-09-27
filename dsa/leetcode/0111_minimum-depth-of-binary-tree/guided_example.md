# Guided Example: Minimum Depth of Binary Tree

We trace the step-by-step nearest-leaf BFS early termination and recursive leaf-validity recurrence on representative branching and skewed binary trees:

- **Branching Tree Instance:** $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7] \implies 2$ (Path $3 \to 9$)
- **Skewed Single-Branch Trap:** $\text{root} = [2, \text{null}, 3, \text{null}, 4, \text{null}, 5, \text{null}, 6] \implies 5$

This instance exposes the common "absent-child zero collapse" fallacy ($1 + \min(L, R)$ on non-leaf nodes), explains why a path must strictly terminate at a childless leaf ($\text{left} = \text{right} = \emptyset$), and demonstrates why BFS level-order traversal provides an optimal early-exit strategy.

---

## 1. Instance & Teaching Goal

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the **shortest path from the root node down to the nearest leaf node**.
*(A leaf is strictly defined as a node with no children: $\text{left} == \emptyset$ and $\text{right} == \emptyset$)*.

Consider the skewed tree $[2, \text{null}, 3, \text{null}, 4, \text{null}, 5, \text{null}, 6]$:
$$
2 \longrightarrow 3 \longrightarrow 4 \longrightarrow 5 \longrightarrow 6
$$
- If an algorithm naively applies $1 + \min(\text{depth}(L), \text{depth}(R))$:
  - Root $2$ has left child $\emptyset$ (depth 0) and right child $3$ (depth 4).
  - Computing $1 + \min(0, 4) = 1$ would claim the minimum depth is $1$.
  - **This is false!** Node $2$ has a right child and is therefore **not** a leaf. The only leaf in the tree is Node $6$ at depth $5$.

Thus, an absent child cannot be treated as a zero-cost path to a leaf. If a node is missing one child, the minimum depth must be pursued through its existing child.

---

## 2. Conceptual Foundation & Invariants

### Method 1: BFS Earliest-Leaf Early Exit (Optimal)
In a BFS queue storing pairs `(node, depth)`:
- Enqueue `(root, 1)`.
- While `queue` is not empty:
  - Pop `node, depth = queue.popleft()`.
  - **Leaf Check:** If `node.left` is null and `node.right` is null:
    - This is the very first leaf encountered in level-order!
    - **Immediately return `depth`!**
  - If `node.left`: enqueue `(node.left, depth + 1)`.
  - If `node.right`: enqueue `(node.right, depth + 1)`.

Because BFS traverses horizontally level by level, the first leaf node popped is mathematically guaranteed to have the minimum depth, avoiding exploration of deep subtrees elsewhere.

### Method 2: Recursive Post-Order Leaf Recurrence
If using DFS recursion $\text{minDepth}(\text{node})$:
1. Base: If $\text{node} == \emptyset$, return $0$.
2. Single-child asymmetry:
   - If $\text{node.left} == \emptyset$: return $1 + \text{minDepth}(\text{node.right})$.
   - If $\text{node.right} == \emptyset$: return $1 + \text{minDepth}(\text{node.left})$.
3. Dual-child convergence:
   - If both children exist: return $1 + \min(\text{minDepth}(\text{node.left}), \, \text{minDepth}(\text{node.right}))$.

> **Invariant.** Under BFS, the first node encountered with $\text{left} = \emptyset$ and $\text{right} = \emptyset$ terminates the algorithm with the exact globally minimal path length.

---

## 3. Step-by-Step Worked Execution

We trace BFS on $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7]$:

### Step 1: Enqueue Root
- $\text{queue} = [(\text{Node}(3), \, \text{depth}=1)]$.

---

### Step 2: Pop Root (Node 3, depth 1)
- Children: Left is $\text{Node}(9)$, Right is $\text{Node}(20)$.
- Neither is null $\implies$ Node 3 is not a leaf.
- Enqueue:
  - $(\text{Node}(9), 2)$
  - $(\text{Node}(20), 2)$
- Queue state: $[(\text{Node}(9), 2), \, (\text{Node}(20), 2)]$.

---

### Step 3: Pop Node 9 (depth 2)
- Inspect children of Node 9:
  - Left child: $\emptyset$
  - Right child: $\emptyset$
- **Leaf Detected!** Both children are null.
- **Immediate Return:** Return $\text{depth} = \mathbf{2}$.
- (Subtrees under Node 20 are never visited!).

---

### Contrast: Skewed Tree Trace ($[2, \text{null}, 3]$)
- Pop Node 2 (depth 1): Left is null, right is Node 3. Not a leaf.
- Enqueue $(\text{Node}(3), 2)$.
- Pop Node 3 (depth 2): Left null, right null $\implies$ Leaf detected! Return $2$.

---

## 4. Complete Execution Trace

### BFS Traversal Table on $[3, 9, 20, \text{null}, \text{null}, 15, 7]$

| Step | Popped Node | Depth | Left Child | Right Child | Is Leaf? ($\text{left}=\text{right}=\emptyset$) | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $\text{Node}(3)$ | 1 | $\text{Node}(9)$ | $\text{Node}(20)$ | No | Enqueue children at depth 2 |
| **2** | **$\text{Node}(9)$** | **2** | **$\emptyset$** | **$\emptyset$** | **Yes (First Leaf)** | **Halt & Return Depth 2** |
| - | $\text{Node}(20)$ | 2 | $\text{Node}(15)$ | $\text{Node}(7)$ | - | Pruned (Never evaluated) |
| - | $\text{Node}(15)$ | 3 | $\emptyset$ | $\emptyset$ | - | Pruned |
| - | $\text{Node}(7)$ | 3 | $\emptyset$ | $\emptyset$ | - | Pruned |

---

## 5. Algorithmic Correctness

**Soundness.** A leaf is an external node with no children. BFS explores nodes in non-decreasing order of their distance from the root ($d = 1, 2, 3 \dots$). The first leaf node popped must have depth less than or equal to that of any unvisited leaf in the queue. Thus, returning its depth is provably optimal.

**Completeness.** Since the tree is finite and contains at least one leaf (unless empty, which is checked upfront), BFS will always encounter a leaf and terminate.

---

## 6. Traps This Instance Exposes

- **The Absent-Child Fallacy ($1 + \min(L, R)$):** Blindly taking the minimum child depth fails whenever a node has exactly one child, because $\min(0, R) = 0$, falsely reporting an absent branch as a path of depth 0 to a leaf.
- **BFS vs DFS Efficiency:** In an unbalanced tree where a leaf exists at depth 2 and another branch extends to depth $10^5$, DFS must traverse the entire $10^5$ branch if it visits it first, while BFS terminates at step 2.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **BFS:** $O(M)$, where $M \le N$ is the number of nodes visited up to the depth of the shallowest leaf. In the best case, $O(1)$. In the worst case (skewed tree), $O(N)$.
  - **DFS:** $O(N)$ worst-case node visits.
- **Auxiliary Space Complexity:** $O(W)$ for the BFS queue, bounded by the maximum tier width $W \le N$.