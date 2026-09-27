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

### Buffer Evolution on a Four-Tier Tree ($[1, 2, 3, 4, 5, 6, 7, 8]$)

This instance separates the two orderings that the algorithm must keep apart: the traversal queue stays left-to-right on every tier, while the committed buffer is reversed only on odd tiers. The buffer is written from its insertion end, so every row shows the resulting left-to-right reading order.

| Pop | Tier $d$ | Polarity | Node popped | Level buffer after insertion | Children enqueued | Traversal queue after pop |
|:---:|:---:|:---|:---|:---|:---|:---|
| 1 | 0 | Left $\to$ Right | $\text{Node}(1)$ | `[1]` | $\text{Node}(2)$, $\text{Node}(3)$ | `[Node(2), Node(3)]` |
| 2 | 1 | Right $\to$ Left | $\text{Node}(2)$ | `[2]` | $\text{Node}(4)$, $\text{Node}(5)$ | `[Node(3), Node(4), Node(5)]` |
| 3 | 1 | Right $\to$ Left | $\text{Node}(3)$ | `[3, 2]` | $\text{Node}(6)$, $\text{Node}(7)$ | `[Node(4), Node(5), Node(6), Node(7)]` |
| 4 | 2 | Left $\to$ Right | $\text{Node}(4)$ | `[4]` | $\text{Node}(8)$ only, since $4.\text{right}$ is null | `[Node(5), Node(6), Node(7), Node(8)]` |
| 5 | 2 | Left $\to$ Right | $\text{Node}(5)$ | `[4, 5]` | None: $5$ is a leaf | `[Node(6), Node(7), Node(8)]` |
| 6 | 2 | Left $\to$ Right | $\text{Node}(6)$ | `[4, 5, 6]` | None: $6$ is a leaf | `[Node(7), Node(8)]` |
| 7 | 2 | Left $\to$ Right | $\text{Node}(7)$ | `[4, 5, 6, 7]` | None: $7$ is a leaf | `[Node(8)]` |
| 8 | 3 | Right $\to$ Left | $\text{Node}(8)$ | `[8]` | None: $8$ is a leaf | `[]` |

At pop $3$ the buffer reads `[3, 2]` even though node $2$ was inserted first, which is precisely the reversal that tier $1$ requires. Tier $2$ flips the polarity back, so the same values are appended at the tail in ascending pop order and the buffer reads `[4, 5, 6, 7]`; the traversal queue itself is never reversed, only the committed tier is.

---

## 5. Algorithmic Correctness

**Soundness.** Level boundary isolation via fixed $k = |\text{queue}|$ ensures that nodes are grouped by depth without inter-tier leakage. Because `appendleft` in a double-ended queue places each subsequent node at the head, reading from left to right within the queue produces a reversed order in $O(1)$ time per node without invoking costly array reversal algorithms.

**Completeness.** Traversal strictly expands every node in the tree in standard FIFO order, guaranteeing that all nodes are visited and inserted into their respective level sublist.

---

## 6. Traps This Instance Exposes

- **Reversing the Main BFS Queue:** If one attempts to pop from the right of the main queue on odd levels, the order in which child nodes are enqueued will become tangled, destroying the ordering of subsequent tiers. The main BFS queue must strictly maintain standard FIFO left-to-right order.
- **Array Slicing Reversal ($O(K)$ Overhead):** Reversing a list via `level[::-1]` at the end of every odd level works, but incurs auxiliary copying overhead. A `collections.deque` achieves $O(1)$ push-front operations.
- **Empty Tree Root:** An empty tree $\text{root} = \emptyset$ must return `[]` immediately.

### Reversal Strategies Compared

Every method below returns the same values; they differ in where the reversal cost is paid and in what breaks.

| Strategy | Where the direction is applied | Time | Auxiliary space | Failure mode |
|:---|:---|:---:|:---:|:---|
| Front insertion into a level deque (used here) | At insertion time: `append` on even tiers, `appendleft` on odd tiers | $O(N)$ total, $O(1)$ per node | $O(W)$ for the traversal queue and the active buffer | None for this contract; the polarity flag must be toggled once per tier, not once per node |
| Tail insertion, then reverse the committed tier | After the tier is complete, reverse the whole sublist | $O(N)$ total but $O(k)$ extra work for each odd tier of width $k$ | $O(W)$ plus a temporary copy for the reversal | Correct but pays a second pass over every odd tier; an in-place reversal avoids the copy but still costs $O(k)$ swaps |
| Alternate child enqueue order per tier | Enqueue $u.\text{right}$ before $u.\text{left}$ on odd tiers | $O(N)$ | $O(W)$ | Corrupts geometry: tier $d+1$ is then built in reversed left-to-right order, so its own required orientation comes out wrong and later tiers inherit the error |
| Pop from either end of the traversal queue | Reverse the traversal queue itself on odd tiers | $O(N)$ | $O(W)$ | Children of a popped node are enqueued in an order that no longer matches the geometric row, so tier boundaries no longer correspond to contiguous runs |
| Depth-first recursion with a depth index | Prepend values into the bucket of an odd depth, append into an even depth | $O(N)$ with deques, $O(N^2)$ with plain list front insertion | $O(H)$ stack plus the buckets | Reaches the right answer but loses the natural tier-by-tier frontier, and front-inserting into a plain list makes odd tiers quadratic |

The comparison isolates the design principle of this problem: keep the structural traversal unbiased and let a single polarity flag control only the committed orientation of each tier.

### Tier Boundary Conditions

| Instance | Level-order encoding | Emitted tiers | Last tier | Result |
|:---|:---|:---|:---|:---|
| Empty tree | `root = []` | none | - | `[]` |
| Single node | `root = [1]` | Left $\to$ Right only | `[1]` | `[[1]]` |
| Two levels | `root = [1, 2, 3]` | Left $\to$ Right, then Right $\to$ Left | `[3, 2]` | `[[1], [3, 2]]` |
| Four levels | `root = [1, 2, 3, 4, 5, 6, 7, 8]` | alternating, ending on an odd tier | `[8]` | `[[1], [3, 2], [4, 5, 6, 7], [8]]` |
| Sparse, four levels | `root = [1, 2, 3, null, 5, 6, null, 7]` | alternating, ending on an odd tier | `[7]` | `[[1], [3, 2], [5, 6], [7]]` |

A tier of width one makes the polarity invisible: `[8]` and `[7]` read identically whichever way they are inserted, so a wrong flag at the final tier is only exposed by a wider tier such as `[3, 2]`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Every node is enqueued once, dequeued once, and inserted into its level deque in $O(1)$ time.
- **Auxiliary Space Complexity:** $O(W)$, where $W$ is the maximum width of the tree ($O(N)$ worst-case for full trees), to store the BFS queue and the active level deque.
