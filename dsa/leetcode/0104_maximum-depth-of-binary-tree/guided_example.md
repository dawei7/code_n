# Guided Example: Maximum Depth of Binary Tree

We trace the step-by-step post-order divide-and-conquer depth recurrence and BFS tier counting on a representative binary tree:

- **Input:** $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7]$
- **Required output:** $3$
- **Base Instances:** $\text{root} = [] \implies 0, \quad \text{root} = [1] \implies 1$

This instance demonstrates recursive post-order subtree height aggregation ($1 + \max(\text{left}, \text{right})$), base case resolution on null pointers, bottom-up inductive depth synthesis, and BFS level counting in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
$$
\begin{gathered}
3 \\
\swarrow \quad \searrow \\
9 \qquad\quad 20 \\
\qquad\quad \swarrow \quad \searrow \\
\qquad\quad 15 \qquad\quad 7
\end{gathered}
$$
return its maximum depth (the number of nodes along the longest path from the root node down to the farthest leaf node).

Paths from the root to each leaf:
1. Path $3 \to 9$: length $2$ nodes.
2. Path $3 \to 20 \to 15$: length $3$ nodes.
3. Path $3 \to 20 \to 7$: length $3$ nodes.
The maximum depth is $\max(2, 3, 3) = 3$.

Depth-First Search computes this bottom-up using optimal substructure: the depth of any node is $1$ plus the maximum of its children's depths.
Alternatively, Breadth-First Search counts the exact number of horizontal tiers processed before the queue empties. Both run in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### Recursive Post-Order Recurrence
We define $\text{maxDepth}(\text{node})$:
1. **Base Case (Empty Subtree):**
   If $\text{node} == \emptyset$:
   $$
   \text{return } 0
   $$
2. **Recursive Divide:**
   Recursively evaluate the maximum depths of left and right subtrees:
   $$
   L = \text{maxDepth}(\text{node.left})
   $$
   $$
   R = \text{maxDepth}(\text{node.right})
   $$
3. **Inductive Conquer:**
   Combine the child heights by selecting the taller subtree and adding $1$ for the current node:
   $$
   \text{maxDepth}(\text{node}) = 1 + \max(L, R)
   $$

> **Invariant.** For every visited node, $\text{maxDepth}(\text{node})$ evaluates to the exact length of the longest simple path from that node down to any descendant leaf.

---

## 3. Step-by-Step Worked Execution

We trace the recursive post-order call stack on $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7]$:

### Step 1: Subtree at Node 9 (Left Child of Root 3)
- Left child is $\emptyset \implies L = 0$.
- Right child is $\emptyset \implies R = 0$.
- Evaluate: $1 + \max(0, 0) = 1$.
- Returns: $\text{maxDepth}(\text{Node}(9)) = 1$.

---

### Step 2: Subtree at Node 15 (Left Child of Node 20)
- Left child is $\emptyset \implies L = 0$.
- Right child is $\emptyset \implies R = 0$.
- Evaluate: $1 + \max(0, 0) = 1$.
- Returns: $\text{maxDepth}(\text{Node}(15)) = 1$.

---

### Step 3: Subtree at Node 7 (Right Child of Node 20)
- Left child is $\emptyset \implies L = 0$.
- Right child is $\emptyset \implies R = 0$.
- Evaluate: $1 + \max(0, 0) = 1$.
- Returns: $\text{maxDepth}(\text{Node}(7)) = 1$.

---

### Step 4: Subtree at Node 20 (Right Child of Root 3)
- Left child $\text{Node}(15)$ returned depth $L = 1$.
- Right child $\text{Node}(7)$ returned depth $R = 1$.
- Evaluate: $1 + \max(1, 1) = 1 + 1 = 2$.
- Returns: $\text{maxDepth}(\text{Node}(20)) = 2$.

---

### Step 5: Root Node 3
- Left child $\text{Node}(9)$ returned depth $L = 1$.
- Right child $\text{Node}(20)$ returned depth $R = 2$.
- Evaluate:
  $$
  \text{maxDepth}(\text{Node}(3)) = 1 + \max(1, 2) = 1 + 2 = \mathbf{3}
  $$
- Root evaluation finishes, returning $\mathbf{3}$.

---

## 4. Complete Execution Trace

```text
                  maxDepth(3) = 1 + max(1, 2) = 3
                 /                              \
       maxDepth(9) = 1               maxDepth(20) = 1 + max(1, 1) = 2
        /         \                   /                          \
     null(0)    null(0)       maxDepth(15) = 1             maxDepth(7) = 1
                               /            \               /           \
                            null(0)       null(0)        null(0)      null(0)
```

| Node Evaluated | Left Subtree Depth $L$ | Right Subtree Depth $R$ | Combination Formula | Returned Depth |
|:---:|:---:|:---:|:---:|:---:|
| $\text{Node}(9)$ | 0 | 0 | $1 + \max(0, 0)$ | 1 |
| $\text{Node}(15)$ | 0 | 0 | $1 + \max(0, 0)$ | 1 |
| $\text{Node}(7)$ | 0 | 0 | $1 + \max(0, 0)$ | 1 |
| $\text{Node}(20)$ | 1 (Node 15) | 1 (Node 7) | $1 + \max(1, 1)$ | 2 |
| **$\text{Node}(3)$ (Root)** | **1 (Node 9)** | **2 (Node 20)** | **$1 + \max(1, 2)$** | **3 (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** By definition, the depth of an empty tree is 0. For any non-empty tree, every path from the root to a leaf begins at the root (cost 1) and continues through either the left or right subtree. Taking $1 + \max(L, R)$ strictly evaluates the maximum path length over all candidate paths.

**Completeness.** The post-order traversal visits every node in the tree. Because base cases return $0$ and internal nodes accurately take the maximum over both children, no deeper path can be overlooked.

---

## 6. Traps This Instance Exposes

- **Base Case Distinction from Minimum Depth:** In *Maximum* Depth, an absent child correctly contributes $0$, and $\max(L, R)$ picks the non-empty branch. In *Minimum* Depth (LeetCode 111), a node with one child cannot use the empty child (which has depth 0) because depth must be measured to a leaf.
- **Degenerate Skew Trees:** If the tree is a straight line ($1 \to 2 \to 3 \to 4$), the recursion stack reaches depth $N$. In languages with small default stack sizes, an iterative BFS or DFS with explicit stack prevents stack overflow.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Every node is visited once and performs $O(1)$ operations.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the tree height ($O(\log N)$ for balanced trees, $O(N)$ for degenerate skewed trees), representing the call stack.