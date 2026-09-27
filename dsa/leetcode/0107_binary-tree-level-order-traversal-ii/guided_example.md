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

---

## 5. Algorithmic Correctness

**Soundness.** BFS level snapshotting guarantees that all nodes at level $d$ are aggregated into $\text{current\_level}$ in strict left-to-right order. Because $\text{appendleft}$ prepends each successive tier to the front of `result`, earlier levels (closer to the root) are pushed towards the back, naturally producing a bottom-up ordering of tiers.

**Completeness.** Every node in the tree is reached by the BFS queue and assigned to its correct horizontal tier. No nodes are omitted or assigned to incorrect vertical levels.

---

## 6. Traps This Instance Exposes

- **Inverting Internal Tier Ordering:** Bottom-up refers only to the order of the *levels* (vertical inversion). The nodes within each level must remain strictly left-to-right ($[15, 7]$, **not** $[7, 15]$).
- **List `insert(0, ...)` Performance:** Using `list.insert(0, item)` in Python takes $O(K)$ time per insertion to shift existing elements, resulting in $O(H^2)$ time where $H$ is the tree height. Using a `collections.deque` or collecting into a list and reversing once at the end with `levels[::-1]` preserves optimal $O(N)$ runtime.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is enqueued once, dequeued once, and appended to its tier list. Reversing or prepending the tier sublists takes $O(H)$ time, bounded by $O(N)$.
- **Auxiliary Space Complexity:** $O(W)$, where $W$ is the maximum width of the binary tree ($O(N)$ for full binary trees), to store the BFS traversal queue.