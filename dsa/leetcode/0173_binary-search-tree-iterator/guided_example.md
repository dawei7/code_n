# Guided Example: Binary Search Tree Iterator

We trace the step-by-step controlled left-spine stack simulation achieving $O(h)$ memory and $O(1)$ amortized next operations on representative binary search trees:

- **Input BST:** $\text{root} = [7, 3, 15, \text{null}, \text{null}, 9, 20]$
- **Operations:** `["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]`
- **Required outputs:** `[null, 3, 7, true, 9, true, 15, true, 20, false]` (In-order sorted sequence: $3 \to 7 \to 9 \to 15 \to 20$)

This instance demonstrates lazy in-order generator simulation with an explicit LIFO call stack, proves why memory is strictly bounded by the tree height $O(h)$ rather than total nodes $O(N)$, derives the $O(1)$ amortized time complexity via aggregate push/pop accounting, and enforces non-destructive traversal without modifying tree nodes.

---

## 1. Instance & Teaching Goal

Given a Binary Search Tree (BST):
$$
\begin{gathered}
7 \\
\swarrow \quad \searrow \\
3 \qquad\quad 15 \\
\qquad\quad \swarrow \;\; \searrow \\
\qquad\quad 9 \quad\;\; 20
\end{gathered}
$$
Design an iterator that outputs nodes in strictly non-decreasing in-order traversal ($3 \to 7 \to 9 \to 15 \to 20$) with:
- $O(1)$ average time per operation.
- $O(h)$ memory, where $h$ is the tree height.

A naive approach pre-computes the entire in-order traversal into an array during initialization:
- While `next()` is $O(1)$, initialization takes $O(N)$ time and stores all $N$ nodes simultaneously, violating the $O(h)$ space requirement.

Controlled iterative in-order traversal simulates recursion lazily:
- Maintain an explicit stack that stores only the active ancestors along the current left spine.
- At initialization, push all nodes along the left spine starting from the root down to the leftmost leaf ($7 \to 3$).
- On `next()`, pop the top node (the current minimum). If that node has a right subtree, push the left spine of that right subtree onto the stack.
- Stack depth never exceeds tree height $h$, and each node is pushed and popped exactly once, yielding $O(1)$ amortized time.

---

## 2. Conceptual Foundation & Invariants

### Controlled In-Order Stack Protocol
Maintain an explicit stack: `self.stack = []`.

#### Helper Routine: `push_left_spine(node)`
While `node` is not null:
$$
\text{self.stack.append}(\text{node})
$$
$$
\text{node} \leftarrow \text{node.left}
$$

#### 1. Constructor `BSTIterator(root)`:
Initialize the left spine from root:
$$
\text{push\_left\_spine}(\text{root})
$$

#### 2. Method `hasNext()` ($O(1)$ Worst-Case):
Check whether any unvisited nodes remain:
$$
\text{return len}(\text{self.stack}) > 0
$$

#### 3. Method `next()` ($O(1)$ Amortized):
Pop the smallest unvisited node:
$$
\text{curr} = \text{self.stack.pop()}
$$
If `curr` has a right child, traverse into it and push its entire left spine:
$$
\text{if curr.right}: \quad \text{push\_left\_spine}(\text{curr.right})
$$
Return `curr.val`.

> **Invariant.** The node on top of `self.stack` is always the global in-order successor among all remaining unvisited nodes. The maximum number of nodes in `self.stack` at any point never exceeds $h + 1$.

---

## 3. Step-by-Step Worked Execution

We trace the operations on BST $[7, 3, 15, \text{null}, \text{null}, 9, 20]$:

### Step 1: `BSTIterator(root = Node(7))`
- `push_left_spine(Node(7))`:
  - Push `Node(7)`. Move left to `Node(3)`.
  - Push `Node(3)`. Move left to `null`.
- Stack state: `[Node(7), Node(3)]`.
- Output: `null`.

---

### Step 2: `next()`
- Pop top of stack: $\text{curr} = \text{Node}(3)$.
- Right child check: `Node(3).right is None`.
- Stack remains: `[Node(7)]`.
- Return $\text{curr.val} = \mathbf{3}$.

---

### Step 3: `next()`
- Pop top of stack: $\text{curr} = \text{Node}(7)$.
- Right child check: `Node(7).right` is `Node(15)`.
- Push left spine of `Node(15)`:
  - Push `Node(15)`. Move left to `Node(9)`.
  - Push `Node(9)`. Move left to `null`.
- Stack state: `[Node(15), Node(9)]`.
- Return $\text{curr.val} = \mathbf{7}$.

---

### Step 4: `hasNext()`
- `len(self.stack) = 2 > 0`.
- Return $\mathbf{True}$.

---

### Step 5: `next()`
- Pop top of stack: $\text{curr} = \text{Node}(9)$.
- Right child check: `Node(9).right is None`.
- Stack remains: `[Node(15)]`.
- Return $\text{curr.val} = \mathbf{9}$.

---

### Step 6: `hasNext()`
- `len(self.stack) = 1 > 0`.
- Return $\mathbf{True}$.

---

### Step 7: `next()`
- Pop top of stack: $\text{curr} = \text{Node}(15)$.
- Right child check: `Node(15).right` is `Node(20)`.
- Push left spine of `Node(20)`:
  - Push `Node(20)`. Move left to `null`.
- Stack state: `[Node(20)]`.
- Return $\text{curr.val} = \mathbf{15}$.

---

### Step 8: `hasNext()`
- `len(self.stack) = 1 > 0`.
- Return $\mathbf{True}$.

---

### Step 9: `next()`
- Pop top of stack: $\text{curr} = \text{Node}(20)$.
- Right child check: `Node(20).right is None`.
- Stack remains: `[]` (Empty!).
- Return $\text{curr.val} = \mathbf{20}$.

---

### Step 10: `hasNext()`
- `len(self.stack) == 0`.
- Return $\mathbf{False}$.

---

## 4. Complete Execution Trace

```text
BST:
      7
     / \
    3   15
       /  \
      9    20

Operation     Stack State Before Pop     Node Popped     Pushed to Stack      Return Value
init:         -                          -               7, 3                 null
next():       [7, 3]                     3               None                 3
next():       [7]                        7               15, 9                7
hasNext():    [15, 9]                    -               -                    true
next():       [15, 9]                    9               None                 9
hasNext():    [15]                       -               -                    true
next():       [15]                       15              20                   15
hasNext():    [20]                       -               -                    true
next():       [20]                       20              None                 20
hasNext():    []                         -               -                    false
```

| Step | Invoc. | Initial Stack State | Popped Node | Subtree Spines Pushed | Resulting Stack | Emitted Output |
|:---:|:---:|:---|:---:|:---:|:---|:---:|
| 1 | `init` | `[]` | - | `7, 3` | `[7, 3]` | `null` |
| 2 | `next` | `[7, 3]` | `Node(3)` | None | `[7]` | **3** |
| 3 | `next` | `[7]` | `Node(7)` | `15, 9` | `[15, 9]` | **7** |
| 4 | `hasNext` | `[15, 9]` | - | - | `[15, 9]` | **`true`** |
| 5 | `next` | `[15, 9]` | `Node(9)` | None | `[15]` | **9** |
| 6 | `hasNext` | `[15]` | - | - | `[15]` | **`true`** |
| 7 | `next` | `[15]` | `Node(15)` | `20` | `[20]` | **15** |
| 8 | `hasNext` | `[20]` | - | - | `[20]` | **`true`** |
| 9 | `next` | `[20]` | `Node(20)` | None | `[]` | **20** |
| 10 | `hasNext` | `[]` | - | - | `[]` | **`false`** |

---

## 5. Algorithmic Correctness

**Soundness.** In a BST, the in-order successor of a node $u$ is either: (1) the leftmost node in $u$'s right subtree, or (2) the lowest ancestor of $u$ whose left child is also an ancestor of $u$. The stack tracks unvisited ancestors. Popping $u$ and pushing the left spine of $u.\text{right}$ preserves this exact ordering.

**Completeness.** Every node in the BST is pushed onto the stack exactly once when its left ancestor or right sibling root is visited, and popped once when its turn in the in-order traversal arrives.

---

## 6. Traps This Instance Exposes

- **$O(N)$ Space Precomputation:** Flattening the entire tree to an array or list during `__init__` violates the $O(h)$ space requirement. On a balanced tree of $10^5$ nodes, $h \approx 17$, where $O(h)$ uses only 17 references while $O(N)$ uses $100,000$.
- **Worst-Case vs Amortized Complexity:** A single call to `next()` can take $O(h)$ time when descending a long left spine (e.g. step 3 above where 15 and 9 are pushed). However, across all $N$ elements, exactly $N$ total pushes occur, yielding strictly $O(1)$ amortized time.
- **Tree Mutation:** Flattening the tree by re-pointing node references modifies the underlying BST, which breaks caller expectations if the tree is concurrently read elsewhere. The stack simulation is completely read-only.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `hasNext()`: $O(1)$ strictly worst-case time (inspecting stack length).
  - `next()`: $O(1)$ amortized time. Across a full traversal of all $N$ nodes, every node is pushed onto the stack exactly once and popped exactly once, totaling $2N$ operations over $N$ queries ($2N / N = O(1)$).
- **Auxiliary Space Complexity:** $O(h)$, where $h$ is the height of the binary search tree. The stack stores at most one simple path from the root to a leaf node ($h \le N$, with $h = O(\log N)$ on balanced trees).