# Guided Example: Validate Binary Search Tree

We trace the step-by-step open-interval $(-\infty, +\infty)$ bound propagation and inorder monotonicity checking on representative valid and invalid binary trees:

- **Valid BST Instance:** $\text{root} = [2, 1, 3] \implies \text{True}$
- **Classic Subtree Violation Trap:** $\text{root} = [5, 1, 4, \text{null}, \text{null}, 3, 6] \implies \text{False}$

This instance demonstrates why local parent-child comparisons are insufficient for BST validation, how global ancestor intervals $(\text{low}, \text{high})$ enforce that all nodes in a right subtree exceed root ancestors, and how inorder traversal provides an equivalent strictly increasing sequence check in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree, determine if it is a valid Binary Search Tree (BST).

A valid BST requires that for **every** node:
1. All node values in its left subtree are **strictly less** than the node's value.
2. All node values in its right subtree are **strictly greater** than the node's value.
3. Both left and right subtrees must also be valid BSTs.

Consider the tree $[5, 1, 4, \text{null}, \text{null}, 3, 6]$:
$$
\begin{gathered}
5 \\
\swarrow \quad \searrow \\
1 \qquad\quad 4 \\
\qquad\quad \swarrow \quad \searrow \\
\qquad\quad 3 \qquad\quad 6
\end{gathered}
$$
- Looking locally at node $4$: its left child $3 < 4$ and right child $6 > 4$. Local checks pass!
- However, node $3$ resides in the **right subtree of root $5$**, requiring all values to be $> 5$.
- Because $3 \le 5$, the entire tree is **invalid** ($\text{False}$).

This teaches that validation cannot be performed locally between a parent and its immediate children. Each node must satisfy an open interval constraint $(\text{low}, \text{high})$ inherited from all its ancestors.

---

## 2. Conceptual Foundation & Invariants

### Method 1: Ancestor Open-Interval Propagation
We define $\text{isValid}(\text{node}, \text{low}, \text{high})$:
1. **Base Case:**
   If $\text{node}$ is null, return $\text{True}$.
2. **Strict Range Invariant:**
   If $\text{node.val} \le \text{low}$ or $\text{node.val} \ge \text{high}$:
   - Return $\text{False}$ (violates strict inequality constraint).
3. **Subtree Bound Updates:**
   - For left child: all descendant values must remain above $\text{low}$, and must be strictly less than $\text{node.val}$:
     $$
     \text{new\_range}_{\text{left}} = (\text{low}, \, \text{node.val})
     $$
   - For right child: all descendant values must be strictly greater than $\text{node.val}$, and remain below $\text{high}$:
     $$
     \text{new\_range}_{\text{right}} = (\text{node.val}, \, \text{high})
     $$
4. Return $\text{isValid}(\text{node.left}, \text{low}, \text{node.val}) \land \text{isValid}(\text{node.right}, \text{node.val}, \text{high})$.

### Method 2: Inorder Monotonicity
Perform an inorder traversal (Left $\to$ Root $\to$ Right) while maintaining $\text{prev\_val}$:
- At each node, verify $\text{node.val} > \text{prev\_val}$.
- If $\text{node.val} \le \text{prev\_val}$, return $\text{False}$ immediately.

> **Invariant.** For every node visited, its value lies strictly within the open interval $(\text{low}, \text{high})$ established by all preceding ancestor routing decisions.

---

## 3. Step-by-Step Worked Execution

We trace the failing instance $\text{root} = [5, 1, 4, \text{null}, \text{null}, 3, 6]$:

### Step 1: Root Node 5
- Initial interval: $(-\infty, +\infty)$.
- Check: $-\infty < 5 < +\infty$. Valid!
- Dispatch left child: interval $(-\infty, 5)$.
- Dispatch right child: interval $(5, +\infty)$.

---

### Step 2: Left Child Node 1
- Assigned interval: $(-\infty, 5)$.
- Check: $-\infty < 1 < 5$. Valid!
- Both children of Node 1 are null $\implies$ left subtree evaluates to $\text{True}$.

---

### Step 3: Right Child Node 4
- Assigned interval: $(5, +\infty)$ (inherited because Node 4 is in the right subtree of Root 5).
- Check: $4 \in (5, +\infty) \implies 4 > 5$?
- **Violation Detected!** $4 \ngtr 5$.
- Node 4 fails the ancestor interval condition immediately.
- Returns $\text{False}$.

Global result: $\mathbf{False}$.

---

## 4. Complete Execution Trace

### Interval Verification Trace for $[5, 1, 4, \text{null}, \text{null}, 3, 6]$

| Traversal Step | Active Node | Node Value | Permitted Interval $(\text{low}, \text{high})$ | Condition Check | Verdict |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Root | 5 | $(-\infty, +\infty)$ | $-\infty < 5 < +\infty$ | Valid |
| 2 | Left | 1 | $(-\infty, 5)$ | $-\infty < 1 < 5$ | Valid |
| **3** | **Right** | **4** | **$(5, +\infty)$** | **$4 > 5$ (Fails!)** | **Invalid ($\text{False}$)** |

### Inorder Sequence Comparison

| Binary Tree | Inorder Sequence Visited | Monotonically Increasing? | BST Verdict |
|:---|:---:|:---:|:---:|
| $[2, 1, 3]$ | $[1, 2, 3]$ | Strictly increasing ($1 < 2 < 3$) | **Valid (True)** |
| $[5, 1, 4, \text{null}, \text{null}, 3, 6]$ | $[1, 5, 3, 4, 6]$ | Non-monotonic ($5 \to 3$ drops!) | **Invalid (False)** |
| $[2, 2, 2]$ | $[2, 2, 2]$ | Duplicate values ($2 \not< 2$) | **Invalid (False)** |

---

## 5. Algorithmic Correctness

**Soundness.** A node's left child can only contain values smaller than the node, while still being restricted by the lower bounds imposed by left turns of earlier ancestors. Passing $(\text{low}, \text{high})$ down the tree enforces the universal BST invariant across all ancestors, not merely immediate parents.

**Completeness.** Pre-order interval checks evaluate every node in the tree. If any node in any subtree violates BST ordering with respect to any ancestor, that node will fail its locally inherited $(\text{low}, \text{high})$ constraint.

---

## 6. Traps This Instance Exposes

- **Checking Only Immediate Children:** Testing `if node.left and node.left.val >= node.val` only catches direct child violations, completely missing deep ancestor violations like node 3 under root 5.
- **Strict Inequality Requirement:** BST definition requires strictly $<$, not $\le$. If a tree has duplicate values (e.g. $[2, 2, 2]$), it is **not** a valid BST.
- **32-Bit Integer Extremes:** Initializing bounds with $-2^{31}$ and $2^{31} - 1$ causes false rejections if the tree contains nodes with value $-2^{31}$ or $2^{31} - 1$. Using `float('-inf')` and `float('inf')` or `None` bounds handles full integer ranges safely.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. Each node is visited once and evaluated in $O(1)$ time.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the height of the tree ($O(\log N)$ for balanced trees, $O(N)$ for degenerate skew trees) representing the recursion call stack.