# Guided Example: Binary Tree Inorder Traversal

We trace the step-by-step binary tree inorder traversal using both an explicit call stack and Morris $O(1)$-space threaded tree traversal on a representative binary tree:

- **Input:** $\text{root} = [1, \text{null}, 2, 3]$
- **Required output:** $[1, 3, 2]$

This instance demonstrates the Left $\to$ Root $\to$ Right traversal discipline, left-spine descent with an explicit stack, popping to process roots, transitioning to right subtrees, and threading in-place via Morris traversal in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
$$
\begin{gathered}
1 \\
\quad \searrow \\
\qquad 2 \\
\qquad \swarrow \\
\quad 3
\end{gathered}
$$
return the inorder traversal of its nodes' values.

Inorder traversal recursively visits:
1. **Left subtree**
2. **Current Root**
3. **Right subtree**

For this instance:
- At Root $1$: Left child is $\emptyset$. Emit **$1$**. Proceed to right subtree rooted at $2$.
- At Node $2$: Left child is $3$. Traverse left child first.
- At Node $3$: Left child is $\emptyset$. Emit **$3$**. Right child is $\emptyset$.
- Return to Node $2$: Left subtree finished. Emit **$2$**. Right child is $\emptyset$.
The final sequence is $[1, 3, 2]$.

We trace two standard non-trivial algorithms:
1. **Explicit Stack Iteration:** Simulates recursion using an explicit LIFO stack in $O(H)$ auxiliary memory.
2. **Morris Traversal:** Temporarily modifies the tree by establishing predecessor threads, achieving $O(N)$ time and strictly $O(1)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

### Method 1: Explicit Stack Protocol
Maintain a stack of node pointers and an active pointer `cur` (initially `cur = root`).
While `cur` is not null or `stack` is not empty:
1. **Descend Left Spine:**
   While `cur` is not null:
   - Push `cur` onto stack: $\text{stack.append}(\text{cur})$.
   - Advance: $\text{cur} \leftarrow \text{cur.left}$.
2. **Process Root:**
   - Pop top node: $\text{cur} = \text{stack.pop()}$.
   - Append value to output: $\text{result.append}(\text{cur.val})$.
3. **Branch Right:**
   - Advance to right child: $\text{cur} \leftarrow \text{cur.right}$.

### Method 2: Morris Inorder Traversal
While `cur` is not null:
- If `cur.left` is null:
  - Visit `cur.val`.
  - Advance `cur = cur.right`.
- Else:
  - Find the inorder predecessor (rightmost node of `cur.left`).
  - If predecessor's right pointer is null:
    - Thread it: $\text{pred.right} = \text{cur}$.
    - Move `cur = cur.left`.
  - Else (predecessor's right pointer is already `cur`):
    - Sever thread: $\text{pred.right} = \text{None}$.
    - Visit `cur.val`.
    - Move `cur = cur.right`.

> **Invariant.** A node's value is emitted if and only if its entire left subtree has already been completely visited and emitted.

---

## 3. Step-by-Step Worked Execution

We trace the explicit stack execution on $\text{root} = [1, \text{null}, 2, 3]$:

### Initialization
- Active pointer: $\text{cur} = \text{Node}(1)$.
- Stack: `[]`. Output: `[]`.

---

### Step 1: Left Spine from Root 1
- `cur` is $\text{Node}(1)$. Push to stack: `stack = [Node(1)]`.
- $\text{cur} \leftarrow \text{Node}(1).\text{left} = \emptyset$.
- Left descent stops.

---

### Step 2: Pop and Visit Node 1
- Pop $\text{cur} = \text{Node}(1)$.
- Emit value: $\text{result} = [1]$.
- Move to right child: $\text{cur} \leftarrow \text{Node}(1).\text{right} = \text{Node}(2)$.

---

### Step 3: Left Spine from Node 2
- `cur` is $\text{Node}(2)$. Push to stack: `stack = [Node(2)]`.
- $\text{cur} \leftarrow \text{Node}(2).\text{left} = \text{Node}(3)$.
- `cur` is $\text{Node}(3)$. Push to stack: `stack = [Node(2), Node(3)]`.
- $\text{cur} \leftarrow \text{Node}(3).\text{left} = \emptyset$.
- Left descent stops.

---

### Step 4: Pop and Visit Node 3
- Pop $\text{cur} = \text{Node}(3)$.
- Emit value: $\text{result} = [1, 3]$.
- Move to right child: $\text{cur} \leftarrow \text{Node}(3).\text{right} = \emptyset$.

---

### Step 5: Pop and Visit Node 2
- `cur` is null. Stack is not empty (`[Node(2)]`).
- Pop $\text{cur} = \text{Node}(2)$.
- Emit value: $\text{result} = [1, 3, 2]$.
- Move to right child: $\text{cur} \leftarrow \text{Node}(2).\text{right} = \emptyset$.

---

### Step 6: Termination
- `cur` is null and `stack` is empty.
- Traversal finishes. Output is $[1, 3, 2]$.

---

## 4. Complete Execution Trace

| Step | Active Node $\text{cur}$ | Stack State (Bottom to Top) | Action Taken | Emitted Output |
|:---:|:---:|:---|:---|:---|
| 1 | $\text{Node}(1)$ | `[Node(1)]` | Push Node 1; move left to $\emptyset$ | `[]` |
| 2 | $\emptyset$ | `[]` | Pop Node 1; emit 1; move right to Node 2 | `[1]` |
| 3 | $\text{Node}(2)$ | `[Node(2)]` | Push Node 2; move left to Node 3 | `[1]` |
| 4 | $\text{Node}(3)$ | `[Node(2), Node(3)]` | Push Node 3; move left to $\emptyset$ | `[1]` |
| 5 | $\emptyset$ | `[Node(2)]` | Pop Node 3; emit 3; move right to $\emptyset$ | `[1, 3]` |
| 6 | $\emptyset$ | `[]` | Pop Node 2; emit 2; move right to $\emptyset$ | `[1, 3, 2]` |
| Exit | $\emptyset$ | `[]` | Stack empty & cur null $\implies$ Halt | **`[1, 3, 2]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Left spine descent ensures that every ancestor of a node is pushed onto the stack before the node itself. Because a LIFO stack pops elements in reverse order of entry, the deepest leftmost leaf is popped first, followed by its parent, followed by its right sibling. This strictly reproduces the mathematical inorder sequence.

**Completeness.** Every node in the tree is pushed onto the stack exactly once and popped exactly once. Since right subtrees are visited only after the root is popped, no branch of the binary tree is omitted or prematurely explored.

---

## 6. Traps This Instance Exposes

- **Infinite Loops with `cur`:** Failing to set `cur = None` after popping from the stack causes the left-descent loop to re-push the popped node endlessly. Setting `cur = cur.right` ensures the algorithm advances to the right subtree.
- **Empty Tree Handling:** If $\text{root} == \emptyset$, `cur` is initially null and `stack` is empty, safely returning `[]` immediately.
- **Restoring Tree Structure in Morris Traversal:** If using Morris traversal, every temporary thread ($\text{pred.right} = \text{cur}$) must be reset to $\text{None}$ during the second visit. Leaving threads intact corrupts the tree structure and introduces infinite cycles.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is pushed and popped at most once.
- **Auxiliary Space Complexity:** $O(H)$ for explicit stack iteration, where $H$ is the tree height ($O(\log N)$ average, $O(N)$ worst case for degenerate skew trees). $O(1)$ space when using Morris traversal.