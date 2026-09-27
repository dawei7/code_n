# Guided Example: Binary Tree Preorder Traversal

We trace the step-by-step Root-Left-Right preorder tree traversal using both explicit LIFO stack simulation and $O(1)$ auxiliary space Morris threading on representative binary tree instances:

- **Input:** $\text{root} = [1, \text{null}, 2, 3]$
- **Required output:** $[1, 2, 3]$
- **Full Hierarchy Instance:** $\text{root} = [1, 2, 3, 4, 5] \implies [1, 2, 4, 5, 3]$

This instance demonstrates the Root $\to$ Left $\to$ Right visiting invariant, explains why child push order onto an explicit LIFO stack must be reversed (push Right before Left), contrasts stack simulation with Morris threading via temporary in-order predecessor links in $O(1)$ auxiliary space, and guarantees linear $O(N)$ runtime.

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
Return the **preorder traversal** of its nodes' values.

In a preorder traversal, every subtree is visited in the strict recursive order:
$$
\mathbf{\text{Root}} \longrightarrow \mathbf{\text{Left Subtree}} \longrightarrow \mathbf{\text{Right Subtree}}
$$
For $\text{root} = [1, \text{null}, 2, 3]$:
1. Visit root: $1$.
2. Left child is null.
3. Visit right subtree rooted at $2$:
   - Visit root: $2$.
   - Visit left child: $3$.
   - Right child is null.
Emitted order: $[1, 2, 3]$.

While recursive traversal is straightforward, system stack frames consume $O(H)$ memory.
An explicit stack models the recursion iteratively: because a stack is Last-In-First-Out (LIFO), pushing the **right** child before the **left** child guarantees that the left child is popped and processed first.
Alternatively, Morris traversal uses temporary threaded pointers to achieve $O(1)$ auxiliary space without any stack or recursion.

---

## 2. Conceptual Foundation & Invariants

### Method 1: Explicit LIFO Stack Protocol
Initialize `stack = [root]` and `result = []`.
If `root` is null: return `[]`.

While `stack` is non-empty:
1. **Pop and Visit:**
   $$
   \text{curr} = \text{stack.pop()}
   $$
   $$
   \text{result.append}(\text{curr.val})
   $$
2. **Push Right Child First:**
   If $\text{curr.right}$ exists:
   $$
   \text{stack.append}(\text{curr.right})
   $$
   *(Pushing right first ensures it waits beneath the left subtree)*.
3. **Push Left Child Second:**
   If $\text{curr.left}$ exists:
   $$
   \text{stack.append}(\text{curr.left})
   $$
   *(Left child sits at the top of the stack, ready to pop next)*.

### Method 2: Morris Preorder Threading ($O(1)$ Space)
When at `curr`:
- If `curr.left` is null:
  - Visit `curr.val`.
  - Advance `curr = curr.right`.
- Else:
  - Find in-order predecessor `pred` (rightmost node in left subtree).
  - If `pred.right` is null:
    - **Visit `curr.val` immediately (Preorder property)!**
    - Create temporary thread: `pred.right = curr`.
    - Advance `curr = curr.left`.
  - Else (`pred.right == curr`):
    - Sever thread: `pred.right = null`.
    - Advance `curr = curr.right`.

> **Invariant.** Under explicit stack traversal, the top of the stack always contains the next node scheduled for visitation in the preorder sequence.

---

## 3. Step-by-Step Worked Execution

We trace the explicit stack method on $\text{root} = [1, \text{null}, 2, 3]$:

### Step 0: Initialization
- `stack = [Node(1)]`
- `result = []`

---

### Step 1: Pop Node 1
- Pop `curr = Node(1)`.
- Visit: `result.append(1)`.
- Children of Node 1:
  - Right child: `Node(2)` exists $\implies$ Push `Node(2)`.
  - Left child: `None` $\implies$ No push.
- Stack: `[Node(2)]`.
- Current result: `[1]`.

---

### Step 2: Pop Node 2
- Pop `curr = Node(2)`.
- Visit: `result.append(2)`.
- Children of Node 2:
  - Right child: `None` $\implies$ No push.
  - Left child: `Node(3)` exists $\implies$ Push `Node(3)`.
- Stack: `[Node(3)]`.
- Current result: `[1, 2]`.

---

### Step 3: Pop Node 3
- Pop `curr = Node(3)`.
- Visit: `result.append(3)`.
- Children of Node 3:
  - Leaf node (no children).
- Stack: `[]` (empty!).
- Current result: `[1, 2, 3]`.

Stack is empty. Traversal completes!
Output: $[1, 2, 3]$.

---

## 4. Complete Execution Trace

### Stack State Evolution Table

```text
Tree:        [1]
               \
               [2]
               /
             [3]

Order:       Pop 1 (push 2) -> Pop 2 (push 3) -> Pop 3 -> Done
Result:      [1, 2, 3]
```

| Iteration | Stack Before Pop | Popped Node `curr` | Visited Value Appended | Children Evaluated | Stack After Push |
|:---:|:---|:---:|:---:|:---|:---|
| 0 (Init) | - | - | - | - | `[Node(1)]` |
| 1 | `[Node(1)]` | $\text{Node}(1)$ | **1** | Right: $\text{Node}(2)$, Left: $\emptyset$ | `[Node(2)]` |
| 2 | `[Node(2)]` | $\text{Node}(2)$ | **2** | Right: $\emptyset$, Left: $\text{Node}(3)$ | `[Node(3)]` |
| 3 | `[Node(3)]` | $\text{Node}(3)$ | **3** | Right: $\emptyset$, Left: $\emptyset$ | `[]` |
| Final | `[]` | - | - | Loop terminates | **`[1, 2, 3]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Preorder traversal requires processing the root before its subtrees, and the left subtree before the right subtree. Because the root is appended to `result` immediately upon popping, and its left child is pushed onto the stack after the right child, the left child is popped first. By mathematical induction, every subtree obeys the Root $\to$ Left $\to$ Right discipline.

**Completeness.** Every node in the tree is pushed onto the stack exactly once (when its parent is popped) and popped exactly once. No nodes are omitted.

---

## 6. Traps This Instance Exposes

- **Reversed Push Order Bug:** Pushing left before right onto a LIFO stack causes the right child to sit on top of the left child, reversing the traversal into Root $\to$ Right $\to$ Left! Pushing right before left is required.
- **Empty Tree Handling:** If $\text{root} == \emptyset$, `stack` is initialized empty or early-returned, correctly producing `[]`.
- **Morris Traversal Visit Timing:** In Morris Inorder traversal, a node is visited when the thread is removed (`pred.right == curr`). In Morris Preorder traversal, the node must be visited when the thread is *first created* (`pred.right is None`), ensuring the parent is recorded before descending into its left subtree.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is pushed onto the stack once and popped once, performing $O(1)$ operations.
- **Auxiliary Space Complexity:** $O(H)$ for explicit stack simulation, where $H$ is the tree height ($O(\log N)$ balanced, $O(N)$ skewed). Morris traversal achieves $O(1)$ auxiliary space.