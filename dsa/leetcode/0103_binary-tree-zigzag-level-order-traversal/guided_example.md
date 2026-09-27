# Guided Example: Binary Tree Zigzag Level Order Traversal

We trace the step-by-step alternating directional BFS level order traversal on a representative binary tree:

- **Input:** $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7]$
- **Required output:** `[[3], [20, 9], [15, 7]]`
- **Single-Node Base:** $\text{root} = [1] \implies [[1]]$

This instance demonstrates decoupling structural tree exploration (enqueuing children consistently from left to right) from level output ordering (using a double-ended deque to alternate between `append` and `appendleft`), flipping direction flags per level, and achieving $O(N)$ linear time and space.

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
return the zigzag level order traversal of its nodes' values (i.e. from left to right, then right to left for the next level and alternate between).

For this instance:
- **Level 0 (Even depth, Left $\to$ Right):** $[3]$
- **Level 1 (Odd depth, Right $\to$ Left):** $[20, 9]$ (node $20$ precedes $9$)
- **Level 2 (Even depth, Left $\to$ Right):** $[15, 7]$
Result: `[[3], [20, 9], [15, 7]]`.

A naive attempt that alters child enqueuing order (e.g. enqueuing right child before left child on odd levels) breaks the spatial relationships of grandchildren on subsequent tiers.
The optimal technique keeps the tree traversal queue strictly left-to-right, while using a double-ended queue (`deque`) for the level output buffer, inserting either at the tail (`append`) or at the head (`appendleft`).

---

## 2. Conceptual Foundation & Invariants

### Alternating Deque Insertion Protocol
1. **FIFO Traversal Queue:**
   Maintain `queue = deque([root])`. Children are **always** enqueued in standard geometry:
   - First `node.left`, then `node.right`.
2. **Direction Flag:**
   Maintain a boolean `left_to_right = True`.
3. **Level Processing Loop:**
   For each level with $k = |\text{queue}|$ nodes:
   - Initialize an empty level buffer: $\text{level} = \text{deque}()$.
   - Repeat $k$ times:
     - Pop node from queue: $\text{node} = \text{queue.popleft()}$.
     - **Directional Insertion:**
       - If $\text{left\_to\_right}$: $\text{level.append}(\text{node.val})$
       - Else: $\text{level.appendleft}(\text{node.val})$
     - Enqueue `node.left` (if present) and `node.right` (if present).
   - Commit: $\text{results.append}(\text{list}(\text{level}))$.
   - **Toggle Direction:** $\text{left\_to\_right} = \lnot \text{left\_to\_right}$.

> **Invariant.** The traversal queue processes nodes strictly in left-to-right order across all depths, guaranteeing child nodes are enqueued at correct geometric coordinates. The level buffer's insertion polarity solely controls the orientation of each tier.

---

## 3. Step-by-Step Worked Execution

We trace the queue and level buffer on $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7]$:

### Initialization
- $\text{queue} = [\text{Node}(3)]$.
- $\text{left\_to\_right} = \text{True}$.
- $\text{results} = []$.

---

### Level $d = 0$ ($\text{left\_to\_right} = \text{True}$):
- Snapshot size: $k = 1$.
- Pop $\text{Node}(3)$:
  - $\text{left\_to\_right}$ is True $\implies$ `level.append(3)`. $\text{level} = [3]$.
  - Enqueue children left-to-right: $\text{Node}(9)$, $\text{Node}(20)$.
- Commit: Append `[3]` to results.
- Toggle: $\text{left\_to\_right} \leftarrow \text{False}$.
- Next queue state: $[\text{Node}(9), \text{Node}(20)]$.

---

### Level $d = 1$ ($\text{left\_to\_right} = \text{False}$, Right $\to$ Left):
- Snapshot size: $k = 2$.
- **Iteration 1 of 2:** Pop $\text{Node}(9)$:
  - $\text{left\_to\_right}$ is False $\implies$ `level.appendleft(9)`.
  - $\text{level} = [9]$.
  - Node 9 has no children.
- **Iteration 2 of 2:** Pop $\text{Node}(20)$:
  - $\text{left\_to\_right}$ is False $\implies$ `level.appendleft(20)`.
  - $20$ is inserted at the front! $\text{level} = [20, 9]$.
  - Enqueue children left-to-right: $\text{Node}(15)$, $\text{Node}(7)$.
- Commit: Append `[20, 9]` to results.
- Toggle: $\text{left\_to\_right} \leftarrow \text{True}$.
- Next queue state: $[\text{Node}(15), \text{Node}(7)]$.

---

### Level $d = 2$ ($\text{left\_to\_right} = \text{True}$, Left $\to$ Right):
- Snapshot size: $k = 2$.
- **Iteration 1 of 2:** Pop $\text{Node}(15)$:
  - $\text{left\_to\_right}$ is True $\implies$ `level.append(15)`. $\text{level} = [15]$.
- **Iteration 2 of 2:** Pop $\text{Node}(7)$:
  - $\text{left\_to\_right}$ is True $\implies$ `level.append(7)`. $\text{level} = [15, 7]$.
- Commit: Append `[15, 7]` to results.
- Toggle: $\text{left\_to\_right} \leftarrow \text{False}$.
- Next queue state: empty `[]`.

Queue is empty. Traversal halts.
Final output: `[[3], [20, 9], [15, 7]]`.

---

## 4. Complete Execution Trace

| Level Depth $d$ | Polarity Flag | Initial Queue | Snapshot $k$ | Nodes Processed & Insertion Action | Emitted Sublist | Next Queue State |
|:---:|:---:|:---|:---:|:---|:---:|:---|
| 0 | Left $\to$ Right | `[Node(3)]` | 1 | $\text{append}(3)$ | `[3]` | `[Node(9), Node(20)]` |
| 1 | Right $\to$ Left | `[Node(9), Node(20)]` | 2 | $\text{appendleft}(9)$, then $\text{appendleft}(20)$ | `[20, 9]` | `[Node(15), Node(7)]` |
| 2 | Left $\to$ Right | `[Node(15), Node(7)]` | 2 | $\text{append}(15)$, then $\text{append}(7)$ | `[15, 7]` | `[]` |
| Exit | - | `[]` | 0 | - | - | **`[[3], [20, 9], [15, 7]]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Level boundary isolation via fixed $k = |\text{queue}|$ ensures that nodes are grouped by depth without inter-tier leakage. Because `appendleft` in a double-ended queue places each subsequent node at the head, reading from left to right within the queue produces a reversed order in $O(1)$ time per node without invoking costly array reversal algorithms.

**Completeness.** Traversal strictly expands every node in the tree in standard FIFO order, guaranteeing that all nodes are visited and inserted into their respective level sublist.

---

## 6. Traps This Instance Exposes

- **Reversing the Main BFS Queue:** If one attempts to pop from the right of the main queue on odd levels, the order in which child nodes are enqueued will become tangled, destroying the ordering of subsequent tiers. The main BFS queue must strictly maintain standard FIFO left-to-right order.
- **Array Slicing Reversal ($O(K)$ Overhead):** Reversing a list via `level[::-1]` at the end of every odd level works, but incurs auxiliary copying overhead. A `collections.deque` achieves $O(1)$ push-front operations.
- **Empty Tree Root:** An empty tree $\text{root} = \emptyset$ must return `[]` immediately.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Every node is enqueued once, dequeued once, and inserted into its level deque in $O(1)$ time.
- **Auxiliary Space Complexity:** $O(W)$, where $W$ is the maximum width of the tree ($O(N)$ worst-case for full trees), to store the BFS queue and the active level deque.