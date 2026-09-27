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