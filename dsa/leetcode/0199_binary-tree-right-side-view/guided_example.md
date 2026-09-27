# Guided Example: Binary Tree Right Side View

We trace the step-by-step level-order breadth-first search and right-first depth-first search on representative binary trees:

- **Input Tree:** `root = [1, 2, 3, null, 5, null, 4]`
- **Required output:** `[1, 3, 4]` (Nodes visible when standing on the right side)
- **Left-Overhang Trap Instance:** `root = [1, 2, 3, 4, null, null, null, 5] \implies [1, 3, 4, 5]` (Proves right view is not merely the right spine: deeper left children become visible when the right subtree terminates early!)
- **Linear Left Chain Instance:** `root = [1, 2, null, 3] \implies [1, 2, 3]` (Entire left spine is visible)
- **Empty Tree Instance:** `root = [] \implies []`

This instance demonstrates level-order frontier partitioning, contrasts queue-based BFS (`last element of level`) with recursive DFS (`root -> right -> left` where `depth == len(result)`), exposes the right-spine misconception, and runs in strictly $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
```text
        1            <-- Level 0: [1]       -> Visible: 1
      /   \
     2     3         <-- Level 1: [2, 3]    -> Visible: 3
      \     \
       5     4       <-- Level 2: [5, 4]    -> Visible: 4
```
Imagine standing to the right of the tree looking left. Return the values of the nodes you can see, ordered from top to bottom:
$$
\text{Right Side View} = \mathbf{[1, 3, 4]}
$$

### The Right-Spine Fallacy
A common misconception is that the right side view simply follows `node.right` pointers (`root -> root.right -> ...`).
Consider a tree where the right branch is shallow:
```text
        1            <-- Visible: 1
      /   \
     2     3         <-- Visible: 3
    /
   4                 <-- Visible: 4 (Left child visible because Node 3 has no children!)
  /
 5                   <-- Visible: 5
```
Here, nodes 4 and 5 reside in the **left subtree**, yet because node 3 has no descendants at levels 2 and 3, nodes 4 and 5 are completely unobstructed from the right!
Thus, the right side view is fundamentally a **level-by-level visibility problem**: for each depth level $d$, find the **rightmost existing node**.

---

## 2. Conceptual Foundation & Invariants

### Method A: Level-Order BFS with Queue (Recommended)
Use a double-ended queue `queue = deque([root])`.

While `queue` is not empty:
1. Record current level width: $S = \text{len}(\text{queue})$.
2. Iterate $i$ from $0$ to $S - 1$:
   - Pop node $u = \text{queue.popleft()}$.
   - If $i == S - 1$ (the last node processed at this level):
     Append $u.\text{val}$ to `result`.
   - Enqueue children in standard left-to-right order:
     - If $u.\text{left}$: `queue.append(u.left)`
     - If $u.\text{right}$: `queue.append(u.right)`

### Method B: Right-First DFS (`Root -> Right -> Left`)
Traverse recursively with tracking parameter `depth`:
1. If `node is None`: return.
2. If `depth == len(result)`:
   Because the traversal explores the right child before the left child, the first node reached at any given `depth` is guaranteed to be the rightmost node at that level!
   $$
   \text{result.append(node.val)}
   $$
3. Recurse right: $\text{dfs}(\text{node.right}, \text{depth} + 1)$.
4. Recurse left: $\text{dfs}(\text{node.left}, \text{depth} + 1)$.

> **Invariant.** For any depth level $d$, exactly one node value is emitted into `result[d]`, corresponding to the node with the maximum horizontal coordinate at depth $d$.

---

## 3. Step-by-Step Worked Execution

We trace BFS on `root = [1, 2, 3, null, 5, null, 4]`:

### Level 0:
- Queue contents: `[Node 1]`.
- Level size: $S = 1$.
- Node $i = 0$ ($u = \text{Node 1}$):
  - Is $i == S - 1$ ($0 == 0$)? **Yes!**
  - Record value: `result = [1]`.
  - Enqueue children: left child $2$, right child $3$.
- Next level queue: `[Node 2, Node 3]`.

---

### Level 1:
- Queue contents: `[Node 2, Node 3]`.
- Level size: $S = 2$.
- Node $i = 0$ ($u = \text{Node 2}$):
  - $i == S - 1$ ($0 == 1$)? No.
  - Enqueue child: right child $5$.
- Node $i = 1$ ($u = \text{Node 3}$):
  - $i == S - 1$ ($1 == 1$)? **Yes!**
  - Record value: `result = [1, 3]`.
  - Enqueue child: right child $4$.
- Next level queue: `[Node 5, Node 4]`.

---

### Level 2:
- Queue contents: `[Node 5, Node 4]`.
- Level size: $S = 2$.
- Node $i = 0$ ($u = \text{Node 5}$):
  - $i == S - 1$ ($0 == 1$)? No.
  - No children to enqueue.
- Node $i = 1$ ($u = \text{Node 4}$):
  - $i == S - 1$ ($1 == 1$)? **Yes!**
  - Record value: `result = [1, 3, 4]`.
  - No children to enqueue.
- Next level queue: `[]` (Empty).

Queue exhausted. The final right side view is $\mathbf{[1, 3, 4]}$.

---

## 4. Complete Execution Trace

```text
Level 0: Queue = [ 1 ]
         Last in level: 1 -> Result: [1]
         Next Q: [ 2, 3 ]

Level 1: Queue = [ 2, 3 ]
         Last in level: 3 -> Result: [1, 3]
         Next Q: [ 5, 4 ]

Level 2: Queue = [ 5, 4 ]
         Last in level: 4 -> Result: [1, 3, 4]
         Next Q: []

Final Output: [1, 3, 4]
```

| Depth Level | Nodes at Level (Left $\to$ Right) | Level Width $S$ | Rightmost Node ($i = S-1$) | Visible Value Added | Cumulative `result` |
|:---:|:---|:---:|:---:|:---:|:---|
| 0 | `[Node 1]` | 1 | Node 1 | 1 | `[1]` |
| 1 | `[Node 2, Node 3]` | 2 | Node 3 | 3 | `[1, 3]` |
| **2** | **`[Node 5, Node 4]`** | **2** | **Node 4** | **4** | **`[1, 3, 4]` (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** In BFS, the queue maintains nodes sorted strictly by increasing depth, and within each depth, strictly from left to right. The last node processed in a level is therefore the rightmost node existing in the tree at that depth. In DFS, traversing right children before left children guarantees that the first time `depth == len(result)`, the current node is the rightmost node at that depth.

**Completeness.** Every reachable node in the tree is visited. Since all depths present in the tree are evaluated, no visible layer can be omitted.

---

## 6. Traps This Instance Exposes

- **Following Only Right Pointers:** If node 3 had no children while node 2 had children (as in `[1, 2, 3, 4]`), node 4 is visible from the right side. Greedily descending `node = node.right` fails to see node 4!
- **Queue Mutation During Level Loop:** Modifying the loop limit dynamically (`for u in queue:`) while appending children breaks level boundaries. Freezing level size $S = \text{len}(\text{queue})$ beforehand is essential.
- **Empty Tree:** Passing `root = None` should immediately return `[]` without attempting to access `.val` or initialize an empty level.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Every node is enqueued and dequeued exactly once in BFS, or visited once in DFS.
- **Auxiliary Space Complexity:** $O(W) \le O(N)$ for BFS, where $W$ is the maximum width of the tree (at most $\lceil N/2 \rceil$ nodes in the queue for a full binary tree); $O(H) \le O(N)$ for DFS stack frames.