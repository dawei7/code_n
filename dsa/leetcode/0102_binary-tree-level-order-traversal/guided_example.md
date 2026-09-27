# Guided Example: Binary Tree Level Order Traversal

We trace the step-by-step level-by-level breadth-first queue processing on a representative binary tree:

- **Input:** $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7]$
- **Required output:** `[[3], [9, 20], [15, 7]]`
- **Single-Node Base:** $\text{root} = [1] \implies [[1]]$

This instance demonstrates queue snapshot isolation via `len(queue)`, processing distinct horizontal tiers of the tree, maintaining strict left-to-right ordering, enqueuing valid child nodes, and achieving $O(N)$ linear time and space.

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
return the level order traversal of its nodes' values (from left to right, level by level).

In this tree:
- **Level 0 (Depth 0):** Root node $[3]$
- **Level 1 (Depth 1):** Left child $9$, Right child $20 \implies [9, 20]$
- **Level 2 (Depth 2):** Children of $20$: $15, 7 \implies [15, 7]$
The output is `[[3], [9, 20], [15, 7]]`.

Depth-First Search (DFS) dives down vertical branches, requiring auxiliary depth indexing to group values into level buckets.
Breadth-First Search (BFS) naturally traverses nodes in order of depth. By snapshotting the queue size at the start of each level loop, nodes belonging to the current horizontal tier are completely extracted before any child nodes from the next tier are processed.

---

## 2. Conceptual Foundation & Invariants

### Level-Snapshot BFS Protocol
Maintain a FIFO double-ended queue `queue` (seeded with `root` if non-null):

While `queue` is non-empty:
1. **Snapshot Level Boundary:**
   Record the number of nodes in the active tier:
   $$
   k = |\text{queue}|
   $$
2. **Batch Level Extraction:**
   Initialize an empty list $\text{current\_level} = []$.
   Repeat $k$ times:
   - Pop front node: $\text{node} = \text{queue.popleft()}$.
   - Record value: $\text{current\_level.append}(\text{node.val})$.
   - Enqueue left child if present:
     $$
     \text{if node.left:} \quad \text{queue.append}(\text{node.left})
     $$
   - Enqueue right child if present:
     $$
     \text{if node.right:} \quad \text{queue.append}(\text{node.right})
     $$
3. **Commit Tier:**
   Append $\text{current\_level}$ to the global result list.

> **Invariant.** At the beginning of iteration $d$, the queue contains precisely the nodes at tree depth $d$ in strict left-to-right geometric order, and no nodes of any other depth.

---

## 3. Step-by-Step Worked Execution

We trace the queue evolution on $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7]$:

### Initialization
- Enqueue root: $\text{queue} = [\text{Node}(3)]$.
- Result accumulator: `[]`.

---

### Level $d = 0$:
- Snapshot size: $k = |\text{queue}| = 1$.
- Pop $\text{Node}(3)$:
  - $\text{current\_level} = [3]$.
  - Left child exists: enqueue $\text{Node}(9)$.
  - Right child exists: enqueue $\text{Node}(20)$.
- Queue after tier 0: $[\text{Node}(9), \text{Node}(20)]$.
- Commit: Append `[3]` to results.

---

### Level $d = 1$:
- Snapshot size: $k = |\text{queue}| = 2$.
- **Iteration 1 of 2:** Pop $\text{Node}(9)$:
  - $\text{current\_level} = [9]$.
  - Node 9 has no children.
- **Iteration 2 of 2:** Pop $\text{Node}(20)$:
  - $\text{current\_level} = [9, 20]$.
  - Left child exists: enqueue $\text{Node}(15)$.
  - Right child exists: enqueue $\text{Node}(7)$.
- Queue after tier 1: $[\text{Node}(15), \text{Node}(7)]$.
- Commit: Append `[9, 20]` to results.

---

### Level $d = 2$:
- Snapshot size: $k = |\text{queue}| = 2$.
- **Iteration 1 of 2:** Pop $\text{Node}(15)$:
  - $\text{current\_level} = [15]$.
  - Node 15 has no children.
- **Iteration 2 of 2:** Pop $\text{Node}(7)$:
  - $\text{current\_level} = [15, 7]$.
  - Node 7 has no children.
- Queue after tier 2: empty `[]`.
- Commit: Append `[15, 7]` to results.

Queue is empty. Traversal terminates.
Final output: `[[3], [9, 20], [15, 7]]`.

---

## 4. Complete Execution Trace

| Level Index $d$ | Initial Queue State | Snapshot Size $k$ | Nodes Popped & Values Collected | Children Enqueued | Emitted Sublist | Queue State at Tier End |
|:---:|:---|:---:|:---|:---|:---:|:---|
| 0 | `[Node(3)]` | 1 | $\text{Node}(3) \to 3$ | $\text{Node}(9), \text{Node}(20)$ | `[3]` | `[Node(9), Node(20)]` |
| 1 | `[Node(9), Node(20)]` | 2 | $\text{Node}(9) \to 9$, $\text{Node}(20) \to 20$ | $\text{Node}(15), \text{Node}(7)$ | `[9, 20]` | `[Node(15), Node(7)]` |
| 2 | `[Node(15), Node(7)]` | 2 | $\text{Node}(15) \to 15$, $\text{Node}(7) \to 7$ | None | `[15, 7]` | `[]` |
| Exit | `[]` | 0 | - | - | - | **`[[3], [9, 20], [15, 7]]`** |

### Per-Pop Operations on the Sparse Instance ($[1, 2, 3, \text{null}, 5, \text{null}, 7, 8]$)

The sparse tree has four tiers, and its queue never holds more than two nodes. This log shows the exact pop-by-pop mechanics, including the fact that a null child costs nothing at all: it is never enqueued, so it never occupies a later snapshot.

| Pop | Tier $d$ (snapshot $k$) | Node popped | `current_level` after this pop | Children enqueued | Queue after this pop |
|:---:|:---:|:---|:---|:---|:---|
| 1 | 0 ($k = 1$) | $\text{Node}(1)$ | `[1]` | $\text{Node}(2)$ then $\text{Node}(3)$ | `[Node(2), Node(3)]` |
| 2 | 1 ($k = 2$) | $\text{Node}(2)$ | `[2]` | Only $\text{Node}(5)$, since $2.\text{left}$ is null | `[Node(3), Node(5)]` |
| 3 | 1 ($k = 2$) | $\text{Node}(3)$ | `[2, 3]` | Only $\text{Node}(7)$, since $3.\text{left}$ is null | `[Node(5), Node(7)]` |
| 4 | 2 ($k = 2$) | $\text{Node}(5)$ | `[5]` | Only $\text{Node}(8)$, since $5.\text{right}$ is null | `[Node(7), Node(8)]` |
| 5 | 2 ($k = 2$) | $\text{Node}(7)$ | `[5, 7]` | None: $7$ is a leaf | `[Node(8)]` |
| 6 | 3 ($k = 1$) | $\text{Node}(8)$ | `[8]` | None: $8$ is a leaf | `[]` |

Tier $2$ holds only two stored nodes although its row in the encoding spans four positions $(\text{null}, 5, \text{null}, 7)$, and tier $3$ holds the single node $8$. The traversal emits stored values only, so the output is `[[1], [2, 3], [5, 7], [8]]` with no placeholder entry for any null child.

---

## 5. Algorithmic Correctness

**Soundness.** Because a queue maintains First-In-First-Out (FIFO) discipline, all nodes at depth $d$ are enqueued before any nodes at depth $d+1$. Fixing $k = \text{len}(\text{queue})$ and popping exactly $k$ nodes guarantees that nodes from different levels are never mixed into the same sublist.

**Completeness.** Every non-null node in the tree is enqueued exactly once when its parent is processed, and popped exactly once to have its value recorded. No reachable node in the connected tree can be omitted.

---

## 6. Traps This Instance Exposes

- **Dynamic Queue Length Mutation:** Writing `for i in range(len(queue)):` directly in environments where `len(queue)` is evaluated dynamically each loop iteration will mix parent and child nodes! Capturing $k = \text{len}(\text{queue})$ upfront fixes the level boundary.
- **Empty Root Input:** If $\text{root} == \emptyset$, checking `if not root: return []` upfront avoids attempting to initialize a queue with `None` and appending `[None]` to the output.
- **Enqueuing Null Children:** Always check `if node.left:` before enqueuing to prevent polluting the queue with `None` sentinels.

### Instance Boundary Matrix and Peak Queue Occupancy

Peak occupancy is the largest queue length observed at any moment, which is the quantity that the auxiliary-space bound actually measures. It is a property of the widest frontier, not of the node count.

| Instance | Level-order encoding | Emitted levels | Peak queue occupancy | Stored nodes $N$ | What the instance tests |
|:---|:---|:---|:---:|:---:|:---|
| Empty tree | `root = []` | none | 0 | 0 | The early return fires before any queue exists, so the answer is `[]` rather than `[[]]` |
| Single node | `root = [1]` | `[[1]]` | 1 | 1 | One tier, one pop, zero enqueues; the queue empties after the first snapshot |
| Three-level sample | `root = [3, 9, 20, null, null, 15, 7]` | `[[3], [9, 20], [15, 7]]` | 2 | 5 | Null children of $9$ are skipped, so tier $1$ contributes exactly two entries |
| Complete tree | `root = [1, 2, 3, 4, 5, 6, 7]` | `[[1], [2, 3], [4, 5, 6, 7]]` | 4 | 7 | Peak occupancy $4 = \lceil N / 2 \rceil$: the bottom tier is the widest frontier |
| Sparse tree | `root = [1, 2, 3, null, 5, null, 7, 8]` | `[[1], [2, 3], [5, 7], [8]]` | 2 | 6 | Height $3$ forces four tiers of output, while the eight-position encoding hides the two null children of tier $2$ |

The complete-tree row is the worst case for this family: its frontier doubles at the last tier, which is why the space bound must be written $O(W)$ with $W = \lceil N / 2 \rceil$ rather than a fixed constant.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. Each node is pushed into the queue once and popped from the queue once, performing $O(1)$ operations per node.
- **Auxiliary Space Complexity:** $O(W)$, where $W$ is the maximum width of the tree. In the worst case (a full binary tree), the bottom tier contains $W = \lceil N / 2 \rceil$ nodes, taking $O(N)$ queue memory.