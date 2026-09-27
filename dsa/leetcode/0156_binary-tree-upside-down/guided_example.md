# Guided Example: Binary Tree Upside Down

We trace the step-by-step left-spine pointer rotation and sibling-parent rewiring on representative binary tree instances:

- **Input:** $\text{root} = [1, 2, 3, 4, 5]$
- **Required output:** $[4, 5, 2, \text{null}, \text{null}, 3, 1]$ (Node 4 becomes new root, with 5 as left child and 2 as right child)
- **Base Instances:** $\text{root} = [] \implies [], \quad \text{root} = [1] \implies [1]$

This instance demonstrates in-place structural tree inversion (original left child becomes parent, original right child becomes left child, and original parent becomes right child), models the transformation as left-spine linked list reversal with sibling preservation, and achieves $O(N)$ linear time with strictly $O(1)$ auxiliary memory.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree with the structural guarantee that every node has either 0 or 2 children, and all right nodes are leaf nodes:
$$
\begin{gathered}
1 \\
\swarrow \quad \searrow \\
2 \qquad\quad 3 \\
\swarrow \;\; \searrow \qquad\qquad \\
4 \quad\;\; 5 \qquad\qquad
\end{gathered}
$$
Turn the binary tree upside down such that:
1. The original **left child** becomes the new **root**.
2. The original **right child** becomes the new **left child**.
3. The original **root** becomes the new **right child**.

Applying the rules to the subsegments:
- For node 2 with children 4 and 5: 4 becomes root, 5 becomes 4's left child, and 2 becomes 4's right child.
- For node 1 with child 2 and right sibling 3: 3 becomes 2's left child, and 1 becomes 2's right child.
- Node 1 becomes a leaf with both children set to null.
The resulting inverted tree:
$$
\begin{gathered}
4 \\
\swarrow \quad \searrow \\
5 \qquad\quad 2 \\
\qquad\qquad \swarrow \;\; \searrow \\
\qquad\qquad 3 \quad\;\; 1
\end{gathered}
$$
Level-order output: $[4, 5, 2, \text{null}, \text{null}, 3, 1]$.

Every node keeps its value and its identity; only its position in the parent/child relation moves. The table records the exact new neighbourhood of each node of this instance, which is precisely what the final level order must encode:

| Original node | Role in the input tree | New left child | New right child | Position in `[4, 5, 2, null, null, 3, 1]` |
|:---|:---|:---|:---|:---|
| 4 | deepest node of the left spine | 5, its former right sibling | 2, its former parent | index 0, the new root |
| 2 | middle node of the left spine | 3, the sibling carried down from node 1 | 1, its former parent | index 2, right child of 4 |
| 1 | original root, parent of 2 and of 3 | `null` | `null` | index 6, a leaf |
| 5 | right leaf of node 2 | `null` | `null` | index 1, left child of 4 and still a leaf |
| 3 | right leaf of node 1 | `null` | `null` | index 5, left child of 2 and still a leaf |

A top-down recursive solution uses $O(H)$ stack frames.
The transformation can be understood as an iterative single-linked list reversal along the left spine: as we descend down the left children ($1 \to 2 \to 4$), we reverse the spine pointers while wiring the right siblings into left positions in $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### Iterative Left-Spine Reversal Protocol
Maintain three tracking pointers:
- `curr`: current node along the left spine (starts at `root`).
- `prev`: original parent of `curr` (starts as $\emptyset$).
- `prev_right`: original right sibling of `curr` (starts as $\emptyset$).

While `curr` is not null:
1. **Cache Descendants:**
   $$
   \text{next\_node} = \text{curr.left}
   $$
   $$
   \text{next\_right} = \text{curr.right}
   $$
2. **Rewire Current Node:**
   - Attach original sibling as new left child:
     $$
     \text{curr.left} \leftarrow \text{prev\_right}
     $$
   - Attach original parent as new right child:
     $$
     \text{curr.right} \leftarrow \text{prev}
     $$
3. **Advance Pointers Down Left Spine:**
   $$
   \text{prev} \leftarrow \text{curr}
   $$
   $$
   \text{prev\_right} \leftarrow \text{next\_right}
   $$
   $$
   \text{curr} \leftarrow \text{next\_node}
   $$

When `curr` becomes null, `prev` holds the new root of the upside-down tree.

> **Invariant.** Before processing `curr`, the subtree rooted at `prev` is already completely inverted, and `prev_right` holds the sibling waiting to attach to `curr`.

---

## 3. Step-by-Step Worked Execution

We trace the iterative rewiring on $\text{root} = [1, 2, 3, 4, 5]$:
Initial: `curr = Node(1), prev = null, prev_right = null`.

---

### Step 1: Process Node 1
- Cache forward links:
  - $\text{next\_node} = \text{Node}(1).\text{left} = \text{Node}(2)$.
  - $\text{next\_right} = \text{Node}(1).\text{right} = \text{Node}(3)$.
- Rewire Node 1:
  - $\text{Node}(1).\text{left} = \text{prev\_right} = \text{null}$.
  - $\text{Node}(1).\text{right} = \text{prev} = \text{null}$.
  - *(Node 1 is now a leaf!)*
- Advance:
  - $\text{prev} = \text{Node}(1)$.
  - $\text{prev\_right} = \text{Node}(3)$.
  - $\text{curr} = \text{Node}(2)$.

---

### Step 2: Process Node 2
- Cache forward links:
  - $\text{next\_node} = \text{Node}(2).\text{left} = \text{Node}(4)$.
  - $\text{next\_right} = \text{Node}(2).\text{right} = \text{Node}(5)$.
- Rewire Node 2:
  - $\text{Node}(2).\text{left} = \text{prev\_right} = \mathbf{\text{Node}(3)}$.
  - $\text{Node}(2).\text{right} = \text{prev} = \mathbf{\text{Node}(1)}$.
  - *(Node 2 now has children 3 and 1!)*
- Advance:
  - $\text{prev} = \text{Node}(2)$.
  - $\text{prev\_right} = \text{Node}(5)$.
  - $\text{curr} = \text{Node}(4)$.

---

### Step 3: Process Node 4
- Cache forward links:
  - $\text{next\_node} = \text{Node}(4).\text{left} = \text{null}$.
  - $\text{next\_right} = \text{Node}(4).\text{right} = \text{null}$.
- Rewire Node 4:
  - $\text{Node}(4).\text{left} = \text{prev\_right} = \mathbf{\text{Node}(5)}$.
  - $\text{Node}(4).\text{right} = \text{prev} = \mathbf{\text{Node}(2)}$.
  - *(Node 4 now has children 5 and 2!)*
- Advance:
  - $\text{prev} = \text{Node}(4)$.
  - $\text{prev\_right} = \text{null}$.
  - $\text{curr} = \text{null}$.

---

### Termination
- `curr` is null.
- Return `prev = Node(4)` as the new root.

Final structure verified:
- $\text{Node}(4): \text{left}=5, \text{right}=2$.
- $\text{Node}(2): \text{left}=3, \text{right}=1$.
- $\text{Node}(5), \text{Node}(3), \text{Node}(1)$: all children are null.
Result: $[4, 5, 2, \text{null}, \text{null}, 3, 1]$.

---

## 4. Complete Execution Trace

```text
Initial Tree:                         Inverted Tree:
     1                                     4
    / \                                   / \
   2   3                                 5   2
  / \                                       / \
 4   5                                     3   1
```

| Step | Active Node `curr` | Cached Next Left | Cached Next Right | Reassigned Left (`curr.left`) | Reassigned Right (`curr.right`) | Advance `prev` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $\text{Node}(1)$ | $\text{Node}(2)$ | $\text{Node}(3)$ | $\text{null}$ | $\text{null}$ | $\text{Node}(1)$ |
| 2 | $\text{Node}(2)$ | $\text{Node}(4)$ | $\text{Node}(5)$ | **$\text{Node}(3)$** | **$\text{Node}(1)$** | $\text{Node}(2)$ |
| **3** | **$\text{Node}(4)$** | **$\text{null}$** | **$\text{null}$** | **$\text{Node}(5)$** | **$\text{Node}(2)$** | **$\text{Node}(4)$ (New Root)** |
| End | $\emptyset$ | - | - | - | - | **Return $\text{Node}(4)$** |

---

## 5. Algorithmic Correctness

**Soundness.** At each level along the left spine, the algorithm explicitly assigns the right sibling to `curr.left` and the parent to `curr.right`. Because the problem guarantees all right nodes are childless leaves, attaching them as left children cannot create cycles or overwrite non-empty subtrees.

**Completeness.** Since every non-leaf node along the spine is visited until the deepest left node is reached, all nodes in the original tree are rewired into the new tree structure without omitting any subtree.

---

## 6. Traps This Instance Exposes

- **Overwriting Child References Before Caching:** Attempting to assign `curr.left = prev_right` before saving `curr.left` destroys the pointer to the rest of the left spine! Caching both `next_node` and `next_right` before reassignment is mandatory.
- **Original Root Children:** The original root (Node 1) must have both `left` and `right` set to null; failing to nullify them creates a cycle ($1 \to 2$ and $2 \to 1$).
- **Single Node or Empty Tree:** If `root is None` or `root.left is None`, the loop terminates immediately and returns `root` unchanged.

The authored instances show that one loop covers every degenerate shape without a special branch; the last two rows also show that the protocol is robust on spine shapes that violate the stated 0-or-2-children guarantee:

| Instance | Input | What is degenerate about it | Result | Why the loop-carried pointers still produce it |
|:---|:---|:---|:---|:---|
| Empty tree | `root = []` | no node exists at all | `[]` | `curr` is null before the first iteration, so the body never runs and `prev` is still the null root it was initialised to |
| Single node | `root = [1]` | node 1 has no left child | `[1]` | the root is itself the deepest left node, so it is processed first with `prev` and `prev_right` both null and keeps two null children |
| Left chain | `root = [1, 2, null, 3]` | no right sibling anywhere in the tree | `[3, null, 2, null, 1]` | every cached `next_right` is null, so each new left child is null and each new right child is the previously processed spine node |
| Three paired levels | `root = [1, 2, 3, 4, 5, null, null, 6, 7]` | four spine nodes, three siblings to carry | `[6, 7, 4, null, null, 5, 2, null, null, 3, 1]` | sibling 7 attaches to the deepest spine node 6, sibling 5 to node 4 and sibling 3 to node 2, each one step below its former parent |
| Longest spine | `root = [1, 2, 3, 4, 5, null, null, 6, 7, null, null, 8, 9, null, null, 10]` | five spine nodes; deepest node has no sibling | `[10, null, 8, 9, 6, null, null, 7, 4, null, null, 5, 2, null, null, 3, 1]` | node 8 has no right child, so node 10 receives a null left child and takes `prev = 8` as its right child |

---

## 7. Complexity Derivation

Four formulations produce this same tree. Comparing them shows why the loop-carried pointer walk is the one worth learning for an input whose guarantee bounds the *shape* of the spine but not its length:

| Formulation | Mechanism | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---|:---|
| Recursive descent that rewires while returning | reach the deepest left node, then give each node its sibling and its parent as children as the calls unwind | $O(H)$ call frames | correct and compact, but $H$ can reach $N/2$ spine nodes, so the longest instance consumes linear stack |
| Loop-carried pointer walk, traced above | carry `prev` and `prev_right` down the spine and rewire each node before stepping to its cached left child | $O(1)$ | both forward links must be cached first, because assigning the new left child destroys the pointer to the remaining spine |
| Materialise the spine, then re-link it | collect the spine nodes in an array and rebuild the parent/child relations by index afterwards | $O(H)$ array | the array buys no clarity over recursion and still needs a rule for which sibling belongs to which spine node |
| Detach every right sibling, then reverse the spine | null the right links in a first pass, reverse the spine, then re-attach the stored siblings | $O(H)$ sibling storage | the displaced siblings still have to live somewhere, and a two-pass order makes the attachment step order-sensitive |

- **Time Complexity:** $O(H) = O(N)$ time, where $H$ is the height of the left spine (which is bounded by $N/2$ nodes). Each step performs $O(1)$ pointer swaps.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory, using only scalar pointer references without recursion or heap allocations.
