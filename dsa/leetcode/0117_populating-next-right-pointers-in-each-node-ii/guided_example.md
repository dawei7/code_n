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

Zooming out first, each outer-loop pass is one descent that converts a whole
tier into the next tier's chain:

| Pass (level $d$) | Nodes traversed as `curr` | Chain assembled at level $d+1$ | Surviving nodes at $d+1$ | `curr` after `curr = dummy.next` |
|:---:|:---|:---|:---:|:---:|
| 0 | $\text{Node}(1)$ | $2 \to 3$ | 2 | $\text{Node}(2)$ |
| 1 | $\text{Node}(2), \text{Node}(3)$ | $4 \to 5 \to 7$ | 3 | $\text{Node}(4)$ |
| 2 | $\text{Node}(4), \text{Node}(5), \text{Node}(7)$ | none | 0 | $\text{NULL}$ |

Pass 1 is the decisive one: level 1 holds two nodes, so level 2 has four child
slots, but only three of them are occupied. The chain still comes out gap-free
because each append is conditional on the child being non-null, so the pass
shrinks the tier from four *positions* to three *nodes* — which is exactly why
node $5$ and node $7$ end up adjacent.

The same information at child granularity, in execution order:

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

The boundary shapes separate the protocols more sharply than the main instance
does, and each one is handled by the same loop rather than by a special branch:

| Scenario | Input | Required chains | How the sentinel protocol reaches it |
|:---|:---|:---|:---|
| Empty tree | `root` is NULL | no nodes | The first descent `curr = dummy.next` is NULL, so the outer loop body never executes |
| Single node | $[1]$ | $1 \to \text{NULL}$ | Pass 0 appends nothing, `dummy.next` stays NULL, and the loop ends after one empty pass |
| Missing left child | $[1,2,3,4,5,\text{null},7]$ | $4 \to 5 \to 7 \to \text{NULL}$ | Node $3$'s null left slot is skipped, so the append of node $7$ lands directly behind node $5$ |
| Missing right child | $[1,2,3,\text{null},5,6,\text{null}]$ | $5 \to 6 \to \text{NULL}$ | The null slots under node $2$'s left and node $3$'s right are skipped, leaving the two occupied children adjacent |
| Sparse non-leaf level | $[1,2,3,4,\text{null},\text{null},7,\text{null},5,6]$ | $5 \to 6 \to \text{NULL}$ on the last tier | The single surviving child under node $4$ heads the next pass, so `curr` is never taken from `curr.left` |
| Perfect tree (LeetCode 116) | $[1,2,3,4,5,6,7]$ | $4 \to 5 \to 6 \to 7 \to \text{NULL}$ | Every append fires, so the sentinel protocol degenerates to the two-rule version and stays correct |

The last row matters: the sentinel protocol is strictly more general than the
116 algorithm, which is why it needs no `curr.next.left` lookup and therefore no
guarantee that a horizontal successor even has a left child.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Every node is visited once as `curr` and stitched once as a child in $O(1)$ operations.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, utilizing only a few pointer references (`dummy`, `tail`, `curr`).
