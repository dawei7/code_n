# Guided Example: Binary Tree Level Order Traversal II

We trace the step-by-step bottom-up breadth-first level order traversal and deque prepending on a representative binary tree:

- **Input:** $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7]$
- **Required output:** `[[15, 7], [9, 20], [3]]`
- **Single-Node Base:** $\text{root} = [1] \implies [[1]]$

This instance demonstrates level-by-level BFS queue snapshots, maintaining left-to-right internal ordering within tiers while ordering tiers bottom-up (leaves to root) using prepending (`appendleft`), and comparing top-down vs bottom-up level traversal in $O(N)$ time.

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
return the bottom-up level order traversal of its nodes' values (i.e. from left to right, level by level from leaf to root).

Top-down level ordering (LeetCode 102) produces:
- Level 0: $[3]$
- Level 1: $[9, 20]$
- Level 2: $[15, 7]$

Bottom-up ordering inverts the tier sequence while strictly preserving left-to-right ordering within each tier:
- Deepest Level 2: $[15, 7]$
- Intermediate Level 1: $[9, 20]$
- Top Level 0: $[3]$
Final output: `[[15, 7], [9, 20], [3]]`.

By using standard BFS queue level-batching and prepending each completed tier to an accumulator deque via `appendleft`, the bottom-up ordering is synthesized directly without extra memory passes.

---

## 2. Conceptual Foundation & Invariants

### Prepending Level BFS Protocol
Maintain a FIFO traversal queue `queue = deque([root])` and an accumulator deque `result = deque()`.

While `queue` is not empty:
1. **Level Snapshot:**
   Capture active tier count: $k = |\text{queue}|$.
2. **Horizontal Tier Collection:**
   Initialize empty list $\text{current\_level} = []$.
   Repeat $k$ times:
   - Pop node: $\text{node} = \text{queue.popleft()}$.
   - Collect value: $\text{current\_level.append}(\text{node.val})$.
   - Enqueue left child if present: $\text{queue.append}(\text{node.left})$.
   - Enqueue right child if present: $\text{queue.append}(\text{node.right})$.
3. **Bottom-Up Prepend:**
   Insert the finished tier at the front of the output container:
   $$
   \text{result.appendleft}(\text{current\_level})
   $$

> **Invariant.** After processing depth $d$, `result` stores tiers $d, d-1, \dots, 0$ in inverted vertical order, where every tier internally retains strict left-to-right horizontal ordering.

---

## 3. Step-by-Step Worked Execution

We trace $\text{root} = [3, 9, 20, \text{null}, \text{null}, 15, 7]$:

### Initialization
- Traversal queue: $\text{queue} = [\text{Node}(3)]$.
- Accumulator deque: $\text{result} = []$.

---

### Level $d = 0$ (Root Tier)
- Snapshot: $k = 1$.
- Pop $\text{Node}(3)$:
  - $\text{current\_level} = [3]$.
  - Enqueue children: $\text{Node}(9)$, $\text{Node}(20)$.
- Prepend tier: $\text{result.appendleft}([3])$.
- Accumulator state: `[[3]]`.
- Queue state: $[\text{Node}(9), \text{Node}(20)]$.

---

### Level $d = 1$ (Middle Tier)
- Snapshot: $k = 2$.
- Pop $\text{Node}(9)$: $\text{current\_level} = [9]$.
- Pop $\text{Node}(20)$: $\text{current\_level} = [9, 20]$. Enqueue $\text{Node}(15)$, $\text{Node}(7)$.
- Prepend tier: $\text{result.appendleft}([9, 20])$.
- Accumulator state: `[[9, 20], [3]]`.
- Queue state: $[\text{Node}(15), \text{Node}(7)]$.

---

### Level $d = 2$ (Leaf Tier)
- Snapshot: $k = 2$.
- Pop $\text{Node}(15)$: $\text{current\_level} = [15]$.
- Pop $\text{Node}(7)$: $\text{current\_level} = [15, 7]$.
- Prepend tier: $\text{result.appendleft}([15, 7])$.
- Accumulator state: `[[15, 7], [9, 20], [3]]`.
- Queue state: empty `[]`.

Queue is empty. Traversal terminates.
Result: `[[15, 7], [9, 20], [3]]`.

---

## 4. Complete Execution Trace

| Level Depth $d$ | Snapshot $k$ | Nodes Popped & Values Extracted | Child Nodes Enqueued | Output Action | Accumulator Deque State |
|:---:|:---:|:---|:---|:---:|:---|
| 0 | 1 | $\text{Node}(3) \to [3]$ | $\text{Node}(9), \text{Node}(20)$ | $\text{appendleft}([3])$ | `[[3]]` |
| 1 | 2 | $\text{Node}(9), \text{Node}(20) \to [9, 20]$ | $\text{Node}(15), \text{Node}(7)$ | $\text{appendleft}([9, 20])$ | `[[9, 20], [3]]` |
| 2 | 2 | $\text{Node}(15), \text{Node}(7) \to [15, 7]$ | None | $\text{appendleft}([15, 7])$ | `[[15, 7], [9, 20], [3]]` |
| Exit | 0 | Queue empty | - | - | **`[[15, 7], [9, 20], [3]]`** |

### Pop-by-Pop Trace on the Sparse Instance ($[1, 2, 3, \text{null}, 5, 6, \text{null}, 7]$)

The sparse tree has four tiers of different widths, so the prepending accumulator is rewritten four times. Values inside a tier are read from the traversal queue in left-to-right order at the moment they are popped, which is why tier `[5, 6]` is never reversed.

| Pop | Tier $d$ | Node popped | `current_level` after this pop | Children enqueued | Traversal queue after this pop | Accumulator after the tier's prepend |
|:---:|:---:|:---|:---|:---|:---|:---|
| 1 | 0 | $\text{Node}(1)$ | `[1]` | $\text{Node}(2)$, $\text{Node}(3)$ | `[Node(2), Node(3)]` | `[[1]]` |
| 2 | 1 | $\text{Node}(2)$ | `[2]` | Only $\text{Node}(5)$, since $2.\text{left}$ is null | `[Node(3), Node(5)]` | - |
| 3 | 1 | $\text{Node}(3)$ | `[2, 3]` | Only $\text{Node}(6)$, since $3.\text{right}$ is null | `[Node(5), Node(6)]` | `[[2, 3], [1]]` |
| 4 | 2 | $\text{Node}(5)$ | `[5]` | Only $\text{Node}(7)$, since $5.\text{right}$ is null | `[Node(6), Node(7)]` | - |
| 5 | 2 | $\text{Node}(6)$ | `[5, 6]` | None: $6$ is a leaf | `[Node(7)]` | `[[5, 6], [2, 3], [1]]` |
| 6 | 3 | $\text{Node}(7)$ | `[7]` | None: $7$ is a leaf | `[]` | `[[7], [5, 6], [2, 3], [1]]` |

Tier $3$ is prepended last but prints first, and each prepend shifts every earlier tier one position further right. The accumulator therefore ends in exactly the reverse discovery order while no tier's internal sequence was ever touched.

---

## 5. Algorithmic Correctness

**Soundness.** BFS level snapshotting guarantees that all nodes at level $d$ are aggregated into $\text{current\_level}$ in strict left-to-right order. Because $\text{appendleft}$ prepends each successive tier to the front of `result`, earlier levels (closer to the root) are pushed towards the back, naturally producing a bottom-up ordering of tiers.

**Completeness.** Every node in the tree is reached by the BFS queue and assigned to its correct horizontal tier. No nodes are omitted or assigned to incorrect vertical levels.

---

## 6. Traps This Instance Exposes

- **Inverting Internal Tier Ordering:** Bottom-up refers only to the order of the *levels* (vertical inversion). The nodes within each level must remain strictly left-to-right ($[15, 7]$, **not** $[7, 15]$).
- **List `insert(0, ...)` Performance:** Using `list.insert(0, item)` in Python takes $O(K)$ time per insertion to shift existing elements, resulting in $O(H^2)$ time where $H$ is the tree height. Using a `collections.deque` or collecting into a list and reversing once at the end with `levels[::-1]` preserves optimal $O(N)$ runtime.

### Discovery Order, Emitted Order, and Boundary Instances

Let $\text{discovery} = [D_0, D_1, \dots, D_{H-1}]$ be the tiers in the order BFS discovers them, from the root downward. The emitted sequence satisfies the exact reflection relation $\text{emitted}[i] = D_{H-1-i}$ for every $i$, with no change to any tier's internal order.

| Instance | Tier count $H$ | Discovery order (root first) | Emitted order (leaves first) | Peak queue occupancy | Stored nodes $N$ |
|:---|:---:|:---|:---|:---:|:---:|
| Empty tree | 0 | none | `[]` | 0 | 0 |
| Single node | 1 | `[[1]]` | `[[1]]` | 1 | 1 |
| Three-level sample | 3 | `[[3], [9, 20], [15, 7]]` | `[[15, 7], [9, 20], [3]]` | 2 | 5 |
| Complete four-level | 4 | `[[1], [2, 3], [4, 5, 6, 7], [8]]` | `[[8], [4, 5, 6, 7], [2, 3], [1]]` | 4 | 8 |
| Sparse four-level | 4 | `[[1], [2, 3], [5, 6], [7]]` | `[[7], [5, 6], [2, 3], [1]]` | 2 | 6 |

Two rows deserve attention. The single-node instance has $H = 1$, so the reflection is the identity and the reversal is unobservable; a bug that reverses tier contents instead of tier positions still passes it. The complete four-level instance is the opposite extreme, where the widest tier has four nodes and lands at emitted index $1$ rather than index $3$, so both the tier order and each tier's left-to-right order are exercised at once.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is enqueued once, dequeued once, and appended to its tier list. Reversing or prepending the tier sublists takes $O(H)$ time, bounded by $O(N)$.
- **Auxiliary Space Complexity:** $O(W)$, where $W$ is the maximum width of the binary tree ($O(N)$ for full binary trees), to store the BFS traversal queue.
