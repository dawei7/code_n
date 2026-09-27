# Guided Example: Inorder Successor in BST II

We trace the step-by-step bidirectional pointer traversal, right-child presence bifurcation ($node.right$ vs $node.right == \text{null}$), leftmost descendant descent in the right subtree, upward parent pointer ascent along right-edge spines, and global maximum null termination on representative binary search trees:

- **Input:**
  - Tree structure:
    $$
    \begin{aligned}
    &\quad 5 \\
    &\enspace / \; \backslash \\
    &3 \quad 6 \\
    / \; \backslash \\
    2 \quad 4 \\
    / \\
    1
    \end{aligned}
    $$
  - Target node: $node = 4$
- **Required output:** Node $5$
  - Node schema: Each node contains $val$, $left$, $right$, and a direct $parent$ pointer.
  - Successor definition: The node with the smallest value strictly greater than $node.val$ in the entire BST (the immediate next node in in-order sequence).
- **Two-case decision trace:**
  - **Case Analysis for $node = 4$:**
    - Does $node.right$ exist?
      - $node.right = \text{None}$.
    - Since there is no right subtree, the successor cannot be among its descendants.
    - The successor must be an **ancestor**!
  - **Upward Parent Ascent Trace for $node = 4$:**
    - Look at parent: $parent(4) = 3$.
    - Is $node (4)$ the right child of $3$?
      - Yes! $3.right = 4$.
      - Being a right child means $4$ is already strictly greater than $3$.
      - Node $3$ cannot be the successor.
      - Ascend: $node \leftarrow parent(4) = 3$.
    - Look at next parent: $parent(3) = 5$.
    - Is $node (3)$ the right child of $5$?
      - No! $3$ is the **left child** of $5$ ($5.left = 3$).
      - Because $3$ is the left child of $5$, node $5$ is the first ancestor whose left subtree contains $4$!
      - By BST invariants, $5$ is strictly greater than all nodes in its left subtree.
      - Ascent terminates!
    - Return $parent$:
      $$
      node.parent = \mathbf{5}
      $$
- **Right Subtree Present Instance ($node = 3$):**
  - $node.right$ exists ($4$).
  - Move to right child: $node \leftarrow 4$.
  - Left child of $4$ is `None` $\implies$ halts at $4$.
  - Successor is $\mathbf{4}$.
- **Tree Maximum Node Instance ($node = 6$):**
  - No right child.
  - Ascends: $6$ is right child of $5 \implies node \leftarrow 5$.
  - $5$ has no parent ($parent = \text{None}$) $\implies$ returns $\mathbf{\text{null}}$ (maximum element has no successor).
- **Leaf Left Child Instance ($node = 1$):**
  - No right child.
  - $1$ is left child of $2 \implies$ loop halts immediately $\implies$ returns parent $\mathbf{2}$.

This instance demonstrates bidirectional BST navigational topologies using explicit parent pointers, mathematically proves why ascending until the first left-branch turn identifies the successor, and derives $O(H)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `node` in a Binary Search Tree (BST) where each node has a reference to its `parent`:
Find the **in-order successor** of that node in the BST.
If no successor exists, return `null`.
You do not have access to the root of the tree directly; you must navigate using only the provided `node` and its child/parent pointers.

```text
Tree:
        5
       / \
      3   6
     / \
    2   4
   /
  1

In-order Sequence: [1,  2,  3,  4,  5,  6]

Successor of 4:
  4 has no right child.
  Ascend: 4 is right child of 3.
  Ascend: 3 is left child of 5 -> First left-child ancestor is 5!
Successor is 5.
```

### The Two Canonical Invariant Cases
In any binary search tree:
1. **Case 1 (Right subtree exists):**
   The successor is the **minimum node in the right subtree**.
   Take one step right ($node \leftarrow node.right$), then follow left pointers until reaching a node with no left child.
2. **Case 2 (Right subtree does not exist):**
   The successor is the **lowest ancestor for which the target node lies in its left subtree**.
   Follow `parent` pointers upward as long as the current node is the right child of its parent.
   The moment the node is the left child of its parent, that parent is the in-order successor!

---

## 2. Conceptual Foundation & Invariants

### 1. Case 1: Right Subtree Minimum Descent:
If $node.right$ is not `None`:
$$
node \leftarrow node.right
$$
While $node.left$ is not `None`:
$$
node \leftarrow node.left
$$
Return $node$.

### 2. Case 2: Right-Spine Ancestor Ascent:
If $node.right$ is `None`:
While $node.parent$ exists and $node.parent.right == node$:
$$
node \leftarrow node.parent
$$
Return $node.parent$.
- If we reach the root while still being on the right spine (e.g. searching for the successor of the tree maximum), $node.parent$ becomes `None`, correctly indicating no successor exists.

> **Ancestor Dominance Invariant.** In Case 2, as long as $node$ is a right child, $node > parent$. The first time $node$ is a left child of $parent$, $parent > node$ and $parent$ is smaller than all higher ancestors, making it the unique in-order successor.

---

## 3. Step-by-Step Worked Execution

We trace $node = 4$ in the tree:
$$
\text{Tree: } 5 \to \text{left: } 3 \to \text{right: } 4
$$

---

### Step 1: Check for Right Subtree
- Inspect $node.right$:
  $$
  node.right = \text{None}
  $$
- Branch to **Case 2 (Ancestor Ascent)**.

---

### Step 2: Traverse Parent Spine

1. **At $node = 4$:**
   - Parent: $node.parent = 3$.
   - Is $node.parent.right == node$?
     - $3.right == 4$ is **True**.
   - $4$ is a right descendant of $3 \implies$ value $4 > 3$.
   - Continue ascending:
     $$
     node \leftarrow node.parent = \mathbf{3}
     $$

2. **At $node = 3$:**
   - Parent: $node.parent = 5$.
   - Is $node.parent.right == node$?
     - $5.right$ is $6$, but $node$ is $3$.
     - $5.right == node$ is **False** ($3$ is the *left* child of $5$!).
   - While loop halts!

---

### Step 3: Return Result
- Successor is the parent of node 3:
  $$
  node.parent = \mathbf{5}
  $$

---

## 4. Complete Execution Trace

| Target Node $val$ | Right Child Exists? | Path Traversed | Halting Condition Met | Returned Successor |
|:---:|:---:|:---|:---|:---:|
| **$4$** | No (`None`) | Up: $4 \to 3 \to 5$ | $3$ is left child of $5$ | **Node $5$** |
| **$3$** | Yes (Node $4$) | Down: $3 \to 4$ | $4.left$ is `None` | **Node $4$** |
| **$1$** | No (`None`) | Up: $1 \to 2$ | $1$ is left child of $2$ | **Node $2$** |
| **$6$** | No (`None`) | Up: $6 \to 5 \to \text{None}$ | Reached root ($parent = \text{None}$) | **`null`** |

---

## 5. Boundary Cases & Failure Modes

- **Global Maximum Node ($node = 6$):** The maximum element in a BST has no successor. The loop ascends all the way to the root and evaluates $node.parent \implies \mathbf{null}$.
- **Root Node with Right Subtree ($node = 5$):** Directly descends to the leftmost node in its right subtree $\implies \mathbf{6}$.
- **Root Node without Right Subtree:** $node.right$ is `None` and $node.parent$ is `None` $\implies$ returns $\mathbf{null}$.
- **Single Node Tree:** $node.right = \text{None}, node.parent = \text{None} \implies \mathbf{null}$.

---

## 6. Traps & Common Anti-Patterns

- **Ascending to the Root to Start from Scratch:** Ascending to the root and then running a full $O(N)$ in-order search works, but wastes unnecessary steps and auxiliary memory. Local navigation uses only the $O(H)$ path directly connected to $node$.
- **Confusing Left vs Right Parent Checking:** In Case 2, we must ascend while `node.parent.right == node`. Stopping when `node.parent.left == node` is the exact condition that halts the loop and identifies the successor.
- **Identity Comparison in Python:** Using pointer identity (`is`) or reference equality ensures that identical values in non-BST configurations are distinguished by node reference.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Case 1 traverses down the height of the right subtree: at most $H$ steps.
  - Case 2 traverses up the ancestor spine: at most $H$ steps.
  - Where $H$ is the height of the BST.
  - Total Time: $\mathcal{O}(H)$, which is $O(\log N)$ for a balanced BST and $O(N)$ in the worst case (skewed tree). Completes in $< 1$ microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ constant extra space with zero recursion stack and zero memory allocations.
