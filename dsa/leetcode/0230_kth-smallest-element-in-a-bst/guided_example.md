# Guided Example: Kth Smallest Element in a BST

We trace the step-by-step ascending inorder traversal, call-stack left-spine descent, and early-termination rank selection on representative Binary Search Trees:

- **Input:** $\text{root} = [5, 3, 6, 2, 4, \text{null}, \text{null}, 1], \quad k = 3$
- **Required output:** $3$ (Inorder sorted sequence: $[1, 2, \mathbf{3}, 4, 5, 6]$; the 3rd smallest value is $3$)
- **Minimum Element Instance:** $k = 1 \implies 1$ (Deepest left-spine leaf is the absolute minimum)
- **Root Element Instance:** $\text{root} = [3, 1, 4, \text{null}, 2], \quad k = 3 \implies 3$
- **Right Subtree Instance:** $k = 6 \implies 6$ (Largest element in the tree)

This instance demonstrates the fundamental BST inorder monotonicity theorem ($\text{Left} < \text{Root} < \text{Right}$), explains iterative stack-based simulation of recursive inorder traversal, implements immediate short-circuiting once the $k^{\text{th}}$ node is popped, and runs in $O(H + k)$ time.

---

## 1. Instance & Teaching Goal

Given the root of a Binary Search Tree (BST) and an integer $k = 3$:
```text
        5
       / \
      3   6
     / \
    2   4
   /
  1
```
Find the $k^{\text{th}}$ smallest element (1-indexed).

### The BST Inorder Monotonicity Theorem
In any Binary Search Tree:
- For every node, all values in its left subtree are strictly smaller than its own value.
- All values in its right subtree are strictly larger than its own value.
Consequently, an **inorder traversal** ($\text{Left} \to \text{Root} \to \text{Right}$) visits all values in **strictly non-decreasing sorted order**:
$$
\text{Inorder Sequence: } [1, 2, \mathbf{3}, 4, 5, 6]
$$
The $k^{\text{th}}$ smallest element is precisely the **$k^{\text{th}}$ node visited** during an inorder traversal!
Sorting a tree array takes $O(N \log N)$ or $O(N)$ full traversal.
An iterative stack-based inorder traversal halts immediately upon visiting the $k^{\text{th}}$ element, taking only $O(H + k)$ time and leaving the remainder of the tree unvisited.

---

## 2. Conceptual Foundation & Invariants

### Iterative Stack Inorder Traversal
Maintain an explicit traversal stack `stack = []` and pointer `curr = root`:
1. **Left-Spine Descent:**
   While `curr` is not null:
   Push `curr` onto `stack` and advance `curr = curr.left`.
   *(Pushes the path from current root down to the smallest unvisited element)*.
2. **Process Minimum Node:**
   Pop `curr = stack.pop()`.
   Increment counter: $\text{count} \leftarrow \text{count} + 1$.
   - **Early Exit Check:**
     If $\text{count} == k$:
     Return $\text{curr.val}$ immediately!
3. **Traverse Right:**
   Advance to right child:
   $$
   \text{curr} \leftarrow \text{curr.right}
   $$
   Repeat from Step 1.

> **Invariant.** The $m^{\text{th}}$ node popped from `stack` has a value strictly greater than the $(m-1)^{\text{th}}$ popped node and strictly less than all remaining unpopped nodes in the tree.

---

## 3. Step-by-Step Worked Execution

We trace the traversal for $k = 3$ on $\text{root} = [5, 3, 6, 2, 4, \text{null}, \text{null}, 1]$:

### Step 1: Initial Left-Spine Descent
- Start at `curr = Node 5`.
- Push 5 $\implies \text{stack} = [5]$, move to left child (Node 3).
- Push 3 $\implies \text{stack} = [5, 3]$, move to left child (Node 2).
- Push 2 $\implies \text{stack} = [5, 3, 2]$, move to left child (Node 1).
- Push 1 $\implies \text{stack} = [5, 3, 2, 1]$, move to left child (`None`).
- Descent finishes. `stack = [5, 3, 2, 1]`.

---

### Step 2: Pop 1st Smallest Element
- Pop `curr = stack.pop()` $\implies \text{Node 1}$.
- Increment $\text{count} = 1$.
- Check: $\text{count} = 1 \ne 3$.
- `curr.right` is `None` $\implies \text{curr} \leftarrow \text{None}$.

---

### Step 3: Pop 2nd Smallest Element
- Pop `curr = stack.pop()` $\implies \text{Node 2}$.
- Increment $\text{count} = 2$.
- Check: $\text{count} = 2 \ne 3$.
- `curr.right` is `None` $\implies \text{curr} \leftarrow \text{None}$.

---

### Step 4: Pop 3rd Smallest Element ($k^{\text{th}}$ Found!)
- Pop `curr = stack.pop()` $\implies \mathbf{\text{Node 3}}$.
- Increment $\text{count} = 3$.
- Check: $\text{count} = 3 == k$ ($3 == 3$)!
- **Match Found!**
- **Short-circuit and return $\text{curr.val} = \mathbf{3}$.**

Notice: Nodes 4, 5, and 6 were never visited or evaluated. The traversal terminates early.

---

## 4. Complete Execution Trace

```text
BST:
        5
       / \
      3   6
     / \
    2   4
   /
  1

Descent: Push 5, 3, 2, 1. Stack = [5, 3, 2, 1]

Pop 1: count = 1, val = 1 (right is null)
Pop 2: count = 2, val = 2 (right is null)
Pop 3: count = 3 == k! -> MATCH! Return 3
```

| Step | Operation / Action | Active Stack State | Popped Node | Traversal Count | Match Check ($== k$)? |
|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | Push left spine $(5 \to 3 \to 2 \to 1)$ | `[5, 3, 2, 1]` | - | 0 | - |
| 2 | Pop smallest | `[5, 3, 2]` | Node 1 | 1 | $1 \ne 3$ |
| 3 | Pop next smallest | `[5, 3]` | Node 2 | 2 | $2 \ne 3$ |
| **4** | **Pop next smallest** | **`[5]`** | **Node 3** | **3** | **$3 == 3 \implies \mathbf{3}$ (Return)** |

### 4.1 Rank Identity for Every Node of the Instance

The early exit stops the trace at rank 3, so the remaining nodes are never
popped. Their ranks still exist, and they are what the traversal would have
produced had $k$ been larger. Recording them makes the correspondence between
inorder position and rank unambiguous.

| Node value | Inorder position (rank) | Stack state immediately after this node is popped | `curr` set to after the pop | Would the traversal have stopped here for $k = 3$? |
|:---:|:---:|:---|:---|:---|
| 1 | 1 | `[5, 3, 2]` | `None`; Node 1 has no right child, so the next iteration pops the stack | No; the counter reaches 1 |
| 2 | 2 | `[5, 3]` | `None`; Node 2 has no right child either | No; the counter reaches 2 |
| 3 | 3 | `[5]` | not assigned; the traversal returns immediately | Yes; this is the requested rank |
| 4 | 4 | would leave `[5]` | `None`; Node 4 is a leaf | Not reached; the early exit already fired |
| 5 | 5 | would leave `[]` | Node 6, its right child | Not reached |
| 6 | 6 | would leave `[]` | `None`; Node 6 is a leaf | Not reached |

Two structural facts are visible in this table. Node 3 sits at rank 3 even though
its own value is 3, which is a coincidence of this instance rather than a rule:
rank and value are different quantities, and a BST such as the trial
`[9]` has rank 1 with value 9. Also, every node that has no right child leaves
`curr` empty and forces the next step to pop, which is exactly the moment the
counter advances. Nodes 4, 5, and 6 are never pushed, so the work saved by the
early exit is not just the pops but the entire right-spine traversal that would
have followed them.

### 4.2 Boundary and Trap Instances

| Trial input | $k$ | Inorder sequence | Popped nodes before the exit | Answer | Why the instance matters |
|:---|:---:|:---|:---:|:---:|:---|
| `[9]` | 1 | `[9]` | 1 | 9 | Degenerate case: the left spine is a single node, and `count == k` fires on the first pop, so the loop body never runs a second time |
| `[3, 1, 4, null, 2]` | 1 | `[1, 2, 3, 4]` | 1 | 1 | The answer is the deepest left-spine leaf, reached only after the full descent rather than at the root |
| `[3, 1, 4, null, 2]` | 3 | `[1, 2, 3, 4]` | 3 | 3 | The rank lands on the root, but the root is popped third, not first; the descent must still find the two smaller values |
| `[1, null, 2, null, 3, null, 4, null, 5]` | 5 | `[1, 2, 3, 4, 5]` | 5 | 5 | A right-skewed tree: the left spine holds only one node at a time, so the stack never grows beyond one entry but the traversal still visits every node |
| `[5, 3, 6, 2, 4, null, null, 1]` | 6 | `[1, 2, 3, 4, 5, 6]` | 6 | 6 | The maximum rank, where the early exit coincides with exhausting the tree and no work is saved at all |

The last row is the honest counterweight to the early-exit claim: when $k = N$ the
traversal degenerates to a complete inorder walk. The claimed saving is
proportional to how much of the tree lies above rank $k$, not a constant factor.
The right-skewed row shows the opposite extreme for auxiliary space, where the
stack depth is $H = 5$ while the total node count is also 5.

---

## 5. Algorithmic Correctness

**Soundness.** By the BST ordering property, every node popped from the stack is strictly greater than all previously popped nodes and strictly less than all nodes remaining in the stack or in unexplored subtrees. Therefore, the $k^{\text{th}}$ node popped is guaranteed to be the $k^{\text{th}}$ smallest element in the entire BST.

**Completeness.** Since $1 \le k \le N$, the $k^{\text{th}}$ smallest element is guaranteed to exist. The left-first traversal visits elements in complete ascending order, ensuring the target rank is reached and emitted.

---

## 6. Traps This Instance Exposes

- **Full Tree Traversal:** Extracting the entire tree into a list (`inorder = []`) and returning `inorder[k - 1]` takes $O(N)$ time and $O(N)$ space. Stopping immediately when $\text{count} == k$ optimizes runtime to $O(H + k)$.
- **1-Indexed Rank:** The rank $k$ is 1-indexed ($k = 1$ is the minimum element). Incrementing `count` before checking equality matches 1-based indexing.
- **Modifications (Follow-up):** If the BST is modified frequently with inserts and deletes, augmenting each tree node with a `count` field (recording the size of its subtree) enables $O(H)$ rank lookups directly from the root.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(H + k)$, where $H$ is the tree height and $k$ is the requested rank.
  - In a balanced BST, $H = O(\log N)$, yielding $O(\log N + k)$ time.
  - In a degenerate linked-list tree, $H = O(N)$.
  - In all cases, only $k$ nodes are visited, achieving optimal early exit.
- **Auxiliary Space Complexity:** $O(H)$ auxiliary memory for the stack, storing at most $H$ nodes along the left-spine branch ($O(\log N)$ on balanced trees).

### 7.1 Alternatives Compared on This Instance

| Approach | How the rank is reached | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| Iterative inorder with an explicit stack and early exit (traced above) | Descend the left spine, pop in ascending order, stop at the $k^{\text{th}}$ pop | $O(H + k)$ | $O(H)$ | Chosen. Visits only the nodes at or below the requested rank, and never touches Nodes 4, 5, or 6 |
| Recursive inorder with a counter | Recurse left, count the node, recurse right, unwinding once the count hits $k$ | $O(H + k)$ | $O(H)$ call frames | Same asymptotics and easier to read, but the recursion cannot stop the sibling calls cleanly without an extra guard at every level |
| Materialize the full inorder sequence | Collect every value, then index the $k - 1$ position | $O(N)$ | $O(N)$ list plus $O(H)$ | Always correct, but pays for all $N$ nodes even when $k = 1$; on this instance it visits 4, 5, and 6 unnecessarily |
| Morris threaded traversal | Thread each left subtree to its predecessor and walk without a stack | $O(N)$ | $O(1)$ | Best possible auxiliary space, but it must temporarily rewrite child pointers, so the tree is mutated during the walk and the early exit has to undo the last thread before returning |
| Subtree-size augmentation (follow-up direction) | Store the left-subtree size at each node and descend by comparing sizes with $k$ | $O(H)$ | $O(H)$ for the descent, $O(N)$ extra storage | The fastest option for repeated rank queries after inserts and deletes, but it requires changing the node representation, which a single-query interface does not justify |

The first two rows dominate the others for one query because the rank is reached
without materializing anything. The augmentation row is the answer to the
follow-up question rather than to this instance: it trades extra stored state for
a query that no longer depends on $k$ at all. The Morris row is the only
alternative that improves auxiliary space, and it does so by paying a traversal
cost that the early exit avoids.

### 7.2 Where the Time Bound Comes From

| Contribution | Nodes or steps | On this instance ($k = 3$) | Where it appears in the trace |
|:---|:---|:---:|:---|
| Left-spine descent pushes | At most $H + 1$ pushes total across the whole run | 4 pushes: Nodes 5, 3, 2, 1 | Step 1, giving `stack = [5, 3, 2, 1]` |
| Pops that advance the counter | Exactly $k$ pops | 3 pops: Nodes 1, 2, 3 | Steps 2 through 4 |
| Right-child descents after a pop | One check per popped node, and a new spine only when a right child exists | 3 checks, all `None` | Steps 2, 3, and the implicit check before returning |
| Work avoided by the early exit | The remaining $N - k$ ranks | 3 ranks: Nodes 4, 5, 6 | Never executed; the return fires as soon as the third pop occurs |

Summing the first two rows gives the $O(H + k)$ bound: the stack can be filled
only along a single root-to-leaf path, and the counter can advance only once per
pop. Nothing in the loop depends on the total node count, which is why a tree
with $N = 6$ and one with $N = 10^5$ cost the same for a fixed small $k$ on a
balanced shape.