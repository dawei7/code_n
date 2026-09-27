# Guided Example: Populating Next Right Pointers in Each Node II

We trace the step-by-step dummy sentinel level-stitching algorithm on an imperfect, sparse binary tree in $O(1)$ extra space:

- **Input:** $\text{root} = [1, 2, 3, 4, 5, \text{null}, 7]$
- **Required output:** $[1, \text{\#}, 2, 3, \text{\#}, 4, 5, 7, \text{\#}]$
- **Single-Node Base:** $\text{root} = [1] \implies [1, \text{\#}]$

This instance demonstrates handling missing child nodes and irregular tree geometries, using a reusable dummy head sentinel to assemble the next level's horizontal linked list on the fly, seamlessly bridging multi-node cousin gaps ($5 \to 7$), and achieving strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an arbitrary binary tree:
$$
\begin{gathered}
1 \\
\swarrow \quad \searrow \\
2 \qquad\quad 3 \\
\swarrow \;\; \searrow \qquad\quad \searrow \\
4 \quad\;\; 5 \qquad\qquad 7
\end{gathered}
$$
populate each node's `next` pointer to point to its next right neighbor (or `NULL` if none exists).

Notice the key challenges that distinguish this problem from LeetCode 116:
1. Node $3$ is missing its left child ($\text{left} = \emptyset$).
2. At the leaf tier, Node $5$ must connect directly across a structural void to Node $7$ ($4 \to 5 \to 7 \to \text{NULL}$).
3. The leftmost node of the next tier is not guaranteed to be `root.left` (e.g. if the left child is missing).

A standard BFS queue solves this in $O(N)$ memory.
To achieve strictly $O(1)$ auxiliary space on arbitrary trees, we introduce a **dummy sentinel node** that acts as the anchor head for the next tier. As the current tier is traversed horizontally, existing children are appended to `tail = tail.next`, naturally stitching the subsequent tier into a continuous chain regardless of missing nodes.

---

## 2. Conceptual Foundation & Invariants

### The Dummy Sentinel Next-Tier Stitching Protocol
Maintain a sentinel node $\text{dummy} = \text{TreeNode}(0)$ and a pointer `tail = dummy`.
Let `curr` traverse the already-stitched current level:

1. **Child Link Helper:**
   Define a helper to append non-null children to the next tier's chain:
   $$
   \text{processChild}(\text{child}):
   $$
   $$
   \text{if child is not null:} \quad \text{tail.next} \leftarrow \text{child}, \quad \text{tail} \leftarrow \text{tail.next}
   $$
2. **Current Level Traversal:**
   While `curr` is not null:
   - $\text{processChild}(\text{curr.left})$
   - $\text{processChild}(\text{curr.right})$
   - Advance: $\text{curr} \leftarrow \text{curr.next}$
3. **Descend to Next Tier:**
   Once `curr` reaches `NULL`, the entire next tier has been linked starting at $\text{dummy.next}$:
   - $\text{curr} \leftarrow \text{dummy.next}$
   - Reset sentinel: $\text{dummy.next} \leftarrow \emptyset$, $\text{tail} \leftarrow \text{dummy}$
4. **Halt Condition:**
   Repeat until `curr` is `NULL` (no children exist on the next tier).

> **Invariant.** During the traversal of level $d$, `tail.next` points to the most recently discovered node at level $d+1$, and `dummy.next` points to the leftmost surviving node of level $d+1$.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{root} = [1, 2, 3, 4, 5, \text{null}, 7]$:

### Level $d = 0$ (`curr = Node(1)`)
- Initialize: `dummy = TreeNode(0)`, `tail = dummy`.
- **Examine `curr = Node(1)`:**
  - Has left child $\text{Node}(2)$:
    $$
    \text{tail.next} \leftarrow \text{Node}(2), \quad \text{tail} \leftarrow \text{Node}(2)
    $$
  - Has right child $\text{Node}(3)$:
    $$
    \text{tail.next} \leftarrow \text{Node}(3), \quad \text{tail} \leftarrow \text{Node}(3)
    $$
  - `curr.next` is NULL $\implies$ tier 0 finished.
- Descend to next tier:
  - Next tier starts at $\text{dummy.next} = \text{Node}(2)$.
  - `curr = Node(2)`.
  - Reset `dummy.next = None`, `tail = dummy`.
- Level 1 is now linked: $2 \to 3 \to \text{NULL}$.

---

### Level $d = 1$ (`curr = Node(2)`)
- Initialize: `tail = dummy`.

#### At `curr = Node(2)`:
- Has left child $\text{Node}(4)$:
  $$
  \text{tail.next} \leftarrow \text{Node}(4), \quad \text{tail} \leftarrow \text{Node}(4)
  $$
- Has right child $\text{Node}(5)$:
  $$
  \text{tail.next} \leftarrow \text{Node}(5), \quad \text{tail} \leftarrow \text{Node}(5)
  $$
- Level 2 chain so far: $\text{dummy} \to 4 \to 5$.
- Advance: `curr = curr.next = Node(3)`.

#### At `curr = Node(3)`:
- Left child is NULL ($\emptyset$) $\implies$ no action taken.
- Has right child $\text{Node}(7)$:
  $$
  \text{tail.next} \leftarrow \text{Node}(7), \quad \text{tail} \leftarrow \text{Node}(7)
  $$
  *(Notice: Node 5's `next` pointer is now connected directly to Node 7, bridging the gap left by 3's missing left child!)*
- `curr.next` is NULL $\implies$ tier 1 finished.
- Descend to next tier:
  - Next tier starts at $\text{dummy.next} = \text{Node}(4)$.
  - `curr = Node(4)`.
  - Reset `dummy.next = None`, `tail = dummy`.
- Level 2 is now linked: $4 \to 5 \to 7 \to \text{NULL}$.

---

### Level $d = 2$ (`curr = Node(4)`)
- Nodes $4, 5, 7$ are all leaves; none have children.
- After loop, $\text{dummy.next}$ remains NULL.
- `curr = None`. Traversal halts!

Output structure:
- Level 0: $1 \to \text{NULL}$
- Level 1: $2 \to 3 \to \text{NULL}$
- Level 2: $4 \to 5 \to 7 \to \text{NULL}$.

---

## 4. Complete Execution Trace

```text
Level 0:           1 -> NULL
                  / \
Level 1:         2 -> 3 -> NULL
                / \     \
Level 2:       4-> 5 ---->7 -> NULL
```

| Active Level | Current Node `curr` | Child Inspected | Action on Next Tier Chain | Chain Attached to `dummy` |
|:---:|:---:|:---:|:---|:---|
| 0 | $\text{Node}(1)$ | $\text{Node}(2)$ (Left) | Append Node 2 | $\text{dummy} \to 2$ |
| 0 | $\text{Node}(1)$ | $\text{Node}(3)$ (Right) | Append Node 3 | $\text{dummy} \to 2 \to 3$ |
| 1 | $\text{Node}(2)$ | $\text{Node}(4)$ (Left) | Append Node 4 | $\text{dummy} \to 4$ |
| 1 | $\text{Node}(2)$ | $\text{Node}(5)$ (Right) | Append Node 5 | $\text{dummy} \to 4 \to 5$ |
| 1 | $\text{Node}(3)$ | $\emptyset$ (Left) | Skipped (Null) | $\text{dummy} \to 4 \to 5$ |
| 1 | $\text{Node}(3)$ | $\text{Node}(7)$ (Right) | **Append Node 7 (Bridges Gap)** | $\text{dummy} \to 4 \to 5 \to 7$ |
| 2 | $\text{Node}(4), 5, 7$ | None | No children found | $\text{dummy.next} = \text{None} \implies$ Halt |

---

## 5. Algorithmic Correctness

**Soundness.** Because `curr` traverses level $d$ sequentially from left to right, its children are visited in strictly geometric left-to-right order. Appending non-null children to `tail.next` guarantees that adjacent surviving nodes at level $d+1$ are linked together regardless of whether they share a parent or have missing cousins in between.

**Completeness.** Every node at level $d$ is inspected. Every non-null child at level $d+1$ is attached to the chain. The transition `curr = dummy.next` correctly identifies the first node of the next tier without requiring knowledge of whether it was a left or right child.

---

## 6. Traps This Instance Exposes

- **Assuming Left Child Always Exists:** In arbitrary binary trees, writing `curr = curr.left` to descend will crash if the leftmost node has no left child. Using `curr = dummy.next` dynamically resolves the true leftmost surviving child.
- **Forgetting to Reset `dummy.next`:** If `dummy.next` is not severed (`dummy.next = None`) before processing the next level, a leaf level that adds no children might reuse the old pointer and enter an infinite loop.
- **Multi-Node Cousin Gaps:** Trees can have multiple consecutive missing children (e.g. three nodes with no children). The dummy pointer handles arbitrarily wide horizontal gaps with zero special cases.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Every node is visited once as `curr` and stitched once as a child in $O(1)$ operations.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, utilizing only a few pointer references (`dummy`, `tail`, `curr`).