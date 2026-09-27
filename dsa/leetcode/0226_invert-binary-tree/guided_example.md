# Guided Example: Invert Binary Tree

We trace the step-by-step mirror reflection pointer swaps, recursive post-order subtree inversion, and iterative BFS level-order pointer mutation on representative binary trees:

- **Input:** $\text{root} = [4, 2, 7, 1, 3, 6, 9]$
- **Required output:** $[4, 7, 2, 9, 6, 3, 1]$ (Every node's left and right child pointers are swapped)
- **Three Node Instance:** $\text{root} = [2, 1, 3] \implies [2, 3, 1]$
- **Single Node Instance:** $\text{root} = [1] \implies [1]$
- **Empty Tree Instance:** $\text{root} = [] \implies []$

This instance demonstrates in-place pointer transposition on directed binary tree topologies, proves the equivalence of recursive DFS and iterative BFS queue traversals, explains why simultaneous tuple assignment (`node.left, node.right = node.right, node.left`) eliminates temporary pointer variables, and runs in strictly $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
```text
        4
       / \
      2   7
     / \ / \
    1  3 6  9
```
Invert the tree so that every left child becomes a right child and vice versa (producing a mirror reflection):
```text
        4
       / \
      7   2
     / \ / \
    9  6 3  1
```

### The Geometric Reflection Invariant
A mirror reflection of a tree requires:
1. Swapping the root's left and right subtrees.
2. Recursively inverting the left subtree.
3. Recursively inverting the right subtree.
Whether executed top-down (pre-order), bottom-up (post-order), or level-by-level (BFS queue), every single node in the tree must have its `left` and `right` pointers swapped exactly once.

---

## 2. Conceptual Foundation & Invariants

### Method A: Recursive Inversion (DFS)
Define `invertTree(node)`:
1. **Base Case:** If `node is None`, return `None`.
2. **Recursive Subtree Inversion:**
   $$
   \text{inverted\_left} = \text{invertTree}(\text{node.left})
   $$
   $$
   \text{inverted\_right} = \text{invertTree}(\text{node.right})
   $$
3. **Pointer Transposition:**
   Attach the inverted subtrees to opposite child references:
   $$
   \text{node.left} \leftarrow \text{inverted\_right}, \quad \text{node.right} \leftarrow \text{inverted\_left}
   $$
4. Return `node`.

### Method B: Iterative Queue Traversal (BFS)
Maintain a queue $Q = \text{deque}([\text{root}])$:
While $Q$ is not empty:
- Pop `curr = Q.popleft()`.
- Swap child pointers:
  $$
  \text{curr.left}, \text{curr.right} = \text{curr.right}, \text{curr.left}
  $$
- Enqueue any non-null children:
  If `curr.left`: $Q.\text{append}(\text{curr.left})$.
  If `curr.right`: $Q.\text{append}(\text{curr.right})$.
Return `root`.

> **Invariant.** For every node $u$ in the tree, after the algorithm visits $u$, the left pointer of $u$ references what was originally in the right subtree of $u$, and the right pointer references what was originally in the left subtree.

---

## 3. Step-by-Step Worked Execution

We trace the recursive bottom-up inversion on $\text{root} = [4, 2, 7, 1, 3, 6, 9]$:

### Step 1: Invert Leaves (Depth 2)
- Node 1: `left = None, right = None` $\implies$ Swapping leaves it unchanged. Returns Node 1.
- Node 3: `left = None, right = None` $\implies$ Returns Node 3.
- Node 6: `left = None, right = None` $\implies$ Returns Node 6.
- Node 9: `left = None, right = None` $\implies$ Returns Node 9.

---

### Step 2: Invert Left Subtree at Node 2 (Depth 1)
- Original children: `node.left = Node 1`, `node.right = Node 3`.
- Swap pointers:
  $$
  \text{Node 2.left} \leftarrow \text{Node 3}, \quad \text{Node 2.right} \leftarrow \text{Node 1}
  $$
- Inverted subtree at 2:
  ```text
      2
     / \
    3   1
  ```
- Returns Node 2.

---

### Step 3: Invert Right Subtree at Node 7 (Depth 1)
- Original children: `node.left = Node 6`, `node.right = Node 9`.
- Swap pointers:
  $$
  \text{Node 7.left} \leftarrow \text{Node 9}, \quad \text{Node 7.right} \leftarrow \text{Node 6}
  $$
- Inverted subtree at 7:
  ```text
      7
     / \
    9   6
  ```
- Returns Node 7.

---

### Step 4: Invert Root Node 4 (Depth 0)
- Original children: `node.left = Node 2`, `node.right = Node 7`.
- Swap pointers:
  $$
  \text{Node 4.left} \leftarrow \text{Node 7}, \quad \text{Node 4.right} \leftarrow \text{Node 2}
  $$
- Full inverted tree:
  ```text
          4
         / \
        7   2
       / \ / \
      9  6 3  1
  ```
- Level-order serialization: $[4, 7, 2, 9, 6, 3, 1]$.

---

## 4. Complete Execution Trace

```text
Original Tree:
        4
       / \
      2   7
     / \ / \
    1  3 6  9

Node 2: swap children (1, 3) -> (3, 1)
Node 7: swap children (6, 9) -> (9, 6)
Node 4: swap children (Subtree 2, Subtree 7) -> (Subtree 7, Subtree 2)

Resulting Tree:
        4
       / \
      7   2
     / \ / \
    9  6 3  1

Output: [4, 7, 2, 9, 6, 3, 1]
```

| Traversal Step | Node Evaluated | Left Child Before Swap | Right Child Before Swap | Pointers After Swap | Subtree Mirror Status |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Node 1 | `None` | `None` | `None, None` | Mirror leaf |
| 2 | Node 3 | `None` | `None` | `None, None` | Mirror leaf |
| **3** | **Node 2** | **Node 1** | **Node 3** | **`left: 3, right: 1`** | **Inverted** |
| 4 | Node 6 | `None` | `None` | `None, None` | Mirror leaf |
| 5 | Node 9 | `None` | `None` | `None, None` | Mirror leaf |
| **6** | **Node 7** | **Node 6** | **Node 9** | **`left: 9, right: 6`** | **Inverted** |
| **7** | **Node 4 (Root)** | **Node 2** | **Node 7** | **`left: 7, right: 2`** | **Complete Tree Inverted** |

### 4.1 Recursion Depth at Every Node

A post-order inversion suspends the current node on the call stack while both
child subtrees are fully processed. At the moment the swap for a node is
actually performed, that node's frame sits at the depth recorded below, and the
number below each framed node is the depth at which the deepest suspended frame
rests.

| Node | Frame depth when its swap executes | Deepest stack depth reached during its subtree | Why the swap waits |
|:---:|:---:|:---:|:---|
| Node 1 | 3 | 3 | Leaf; no children to wait for, so the frame is created and retired in the same step |
| Node 3 | 3 | 3 | Leaf on the opposite side of Node 2 |
| Node 2 | 2 | 3 | Blocks until both leaf frames of Nodes 1 and 3 have returned |
| Node 6 | 3 | 3 | Leaf on the left of Node 7 |
| Node 9 | 3 | 3 | Leaf on the right of Node 7 |
| Node 7 | 2 | 3 | Blocks until both leaf frames of Nodes 6 and 9 have returned |
| Node 4 | 1 | 3 | Blocks until the whole subtrees rooted at Node 2 and Node 7 have been mirrored |

The deepest column never exceeds 3 for this instance, and $3 = H + 1$ with
$H = 2$. That equality is not a coincidence: the recursion can descend at most
one frame per level along a root-to-leaf path, so the auxiliary stack is exactly
the tree height (plus the root frame) for a balanced shape and degenerates to
$N$ frames when each node has a single child.

### 4.2 The Same Instance Under Iterative BFS

The queue-driven method reaches the identical result by swapping before it
descends instead of after. Each swap transposes only the two references stored
at the dequeued node, so the queue always carries the yet-unvisited frontier.

| Level | Nodes dequeued at this level | Queue after all swaps of this level | Max queue size observed in this level | Nodes now positioned as |
|:---:|:---|:---|:---:|:---|
| 0 | Node 4 | `[7, 2]` | 2 | Root's children already mirrored |
| 1 | Node 7, then Node 2 | `[9, 6, 3, 1]` | 4 | Depth-1 children mirrored; level-2 order flipped |
| 2 | Node 9, Node 6, Node 3, Node 1 | `[]` | 1 | Leaves enqueue nothing; traversal ends |

Level 1 is the informative row. Its peak occupancy of 4 is the largest the queue
ever becomes, and that peak is the maximum level width $W$ of the tree. In a
complete tree $W$ is about $N/2$, which is why the BFS bound is stated as
$O(W) = O(N)$ rather than as a height bound. Note also that the dequeued pairs
at level 1 are `7, 2` rather than `2, 7`: the swap performed at the root is what
put Node 7 at the front of the frontier, so the level-order output
$[4, 7, 2, 9, 6, 3, 1]$ follows directly from the queue order.

---

## 5. Algorithmic Correctness

**Soundness.** Swapping `node.left` and `node.right` mirrors the child structure at that specific node. Applying this swap across every single node inductively inverts every horizontal relationship across all levels of the tree.

**Completeness.** Every reachable node in the binary tree is visited exactly once. No node is skipped, ensuring the entire tree topology is mirrored.

---

## 6. Traps This Instance Exposes

- **Sequential Overwrite Without Swap:** In languages without simultaneous tuple assignment, writing `root.left = invertTree(root.right)` overwrites `root.left` before it is passed to the right subtree! A temporary variable `temp = root.left` is required, or Python tuple unpacking `root.left, root.right = root.right, root.left`.
- **Empty Tree:** When `root is None`, immediately returning `None` guards against null-pointer dereferencing.
- **Asymmetric / Skewed Trees:** A node with only one child (e.g. `left = Node(2), right = None`) correctly swaps to `left = None, right = Node(2)`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the total number of nodes in the binary tree. Each node is visited once and its child pointers are swapped in $O(1)$ time.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the height of the tree.
  - In a balanced tree, $H = O(\log N)$ call stack frames.
  - In a completely skewed tree, $H = O(N)$ call stack frames.
  - Using BFS queue, space is $O(W) = O(N)$ where $W$ is maximum level width.

### 7.1 Alternatives Compared on This Instance

| Approach | What it changes per step | Time | Auxiliary space | Why it is or is not chosen here |
|:---|:---|:---:|:---:|:---|
| Recursive post-order DFS | Both child pointers at a node, after its subtrees return | $O(N)$ | $O(H)$, i.e. 3 frames on this instance | Chosen. Fewest moving parts: one swap per node, and the mirror property is established bottom-up |
| Iterative BFS with a deque | Both child pointers at a node, before enqueuing its children | $O(N)$ | $O(W)$, i.e. 4 frontier slots on this instance | Equivalent result and immune to stack limits on a skewed tree, but needs an explicit container |
| Pre-order DFS (swap, then recurse) | Both child pointers at a node, before recursing | $O(N)$ | $O(H)$ | Correct, yet it consumes the original child order, so each subtree must be descended through the references captured before the swap |
| Swapping node values instead of pointers | Only the `val` payloads travel; topology is untouched | $O(N)$ | $O(H)$ | Wrong for an unbalanced instance. On $[1, 2, 3, null, 4]$ the values would land at positions whose child structure no longer matches, so the serialization is not `[1, 3, 2, null, null, 4]` |
| Mirroring the level-order array only | Permutes the serialized list | $O(N)$ | $O(N)$ | Wrong. A flat permutation cannot express which original subtree must become which, and it destroys the parent/child relations |

The two correct pointer methods differ only in *when* the swap happens relative
to descending, which is why both visit each node exactly once. The last two rows
are the tempting shortcuts this instance is designed to rule out: the mirror
lives in the pointer structure, not in the values and not in the serialization.

### 7.2 Where the Mirror Property Moves Each Node

For the asymmetric trial input $\text{root} = [1, 2, 3, null, 4]$, inversion
relocates every node within its own level, so the level-order serialization must
be re-derived rather than permuted by hand.

| Node | Original level-order position | Original child links | Inverted level-order position | Inverted child links |
|:---:|:---:|:---|:---:|:---|
| 1 | 0 | `left: 2`, `right: 3` | 0 | `left: 3`, `right: 2` |
| 3 | 2 | none | 1 | none; occupies the slot the null left child of Node 1 vacated |
| 2 | 1 | `left: None`, `right: 4` | 2 | `left: 4`, `right: None` |
| 4 | 4 | none | 5 | none; shifted right because Node 2's left slot is now occupied |

Under level-order serialization the slots that are explicitly `null` record
missing children, and inversion changes which slots those are. The original
encoding `[1, 2, 3, null, 4]` carries one `null` marker, at position 3, which is
Node 2's absent left child; Node 4 then occupies position 4 as Node 2's right
child. After inversion the absent slots are positions 3 and 4 (Node 3's two
missing children), and Node 4 moves to position 5 because it is now the left child
of Node 2, so the corrected serialization is `[1, 3, 2, null, null, 4]`. Dropping
either `null` would shift Node 4 into position 4 and produce the malformed array
`[1, 3, 2, null, 4]`, which decodes as a tree whose only missing link is Node 3's
left child and which no longer matches the inverted topology.