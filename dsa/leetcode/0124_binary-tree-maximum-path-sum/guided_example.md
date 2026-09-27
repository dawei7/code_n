# Guided Example: Binary Tree Maximum Path Sum

We trace the step-by-step post-order gain propagation and dual-purpose apex path evaluation on a representative binary tree:

- **Input:** $\text{root} = [-10, 9, 20, \text{null}, \text{null}, 15, 7]$
- **Required output:** $42$ (Path $15 \to 20 \to 7 = 42$)
- **All-Negative Trap:** $\text{root} = [-3] \implies -3$ (Single negative node must be valid)

This instance demonstrates the crucial distinction between the **linear branch gain** reported upward to a parent ($u.\text{val} + \max(0, \max(L, R))$) versus the **turnaround apex sum** evaluated at $u$ ($u.\text{val} + \max(0, L) + \max(0, R)$), pruning negative child contributions, and tracking the global maximum across all possible path apexes in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given the root of a binary tree:
$$
\begin{gathered}
-10 \\
\swarrow \qquad \searrow \\
9 \qquad\qquad 20 \\
\qquad\qquad \swarrow \;\; \searrow \\
\qquad\qquad 15 \quad\;\; 7
\end{gathered}
$$
find the maximum path sum of any non-empty path. A path is a sequence of adjacent connected nodes visiting each node at most once. It does not need to pass through the root.

Candidate paths in this tree:
- From root down left: $-10 + 9 = -1$
- From root down right: $-10 + 20 + 15 = 25$
- Root bridging both subtrees: $9 + (-10) + 20 + 15 = 34$
- Subtree inverted-V path: $15 \to 20 \to 7 = 15 + 20 + 7 = \mathbf{42}$

### The Forking Constraint
Why can't a path include $9$, $-10$, $20$, $15$, **and** $7$?
Because that would form a "T" or fork! A valid simple path cannot branch into both children of node $20$ *and* continue upward to $-10$.
Therefore, every node has two distinct mathematical roles:
1. **As a Path Apex (Turnaround Point):** It can connect its left branch, itself, and its right branch.
2. **As an Intermediate Stepping Stone:** When contributing to an ancestor's path, it can only pick **one** child branch (left or right).

---

## 2. Conceptual Foundation & Invariants

### Dual-Purpose Post-Order Protocol
Maintain a global variable $\text{max\_sum} = -\infty$.
Define $\text{maxGain}(\text{node})$:

1. **Base Case:**
   If $\text{node} == \emptyset$: return $0$.
2. **Evaluate Child Gains with Negative Pruning:**
   Recursively evaluate left and right subtrees. If a child yields a negative contribution, prune it by clamping to $0$:
   $$
   L = \max(0, \, \text{maxGain}(\text{node.left}))
   $$
   $$
   R = \max(0, \, \text{maxGain}(\text{node.right}))
   $$
3. **Update Global Maximum with Apex Sum:**
   Treat $\text{node}$ as the highest point (apex) of a path:
   $$
   \text{apex\_sum} = \text{node.val} + L + R
   $$
   $$
   \text{max\_sum} \leftarrow \max(\text{max\_sum}, \, \text{apex\_sum})
   $$
4. **Report Upward Single-Branch Gain:**
   Return the maximum sum of a linear path starting at $\text{node}$ and extending down into one child:
   $$
   \text{return } \text{node.val} + \max(L, R)
   $$

> **Invariant.** For every node $u$, $\text{maxGain}(u)$ returns the maximum sum of a simple downward path starting at $u$, while $\text{max\_sum}$ continuously tracks the globally optimal path sum over all examined apexes.

---

## 3. Step-by-Step Worked Execution

We trace the recursive calls on $\text{root} = [-10, 9, 20, \text{null}, \text{null}, 15, 7]$:

### Step 1: Leaf Node 9 (Left child of -10)
- $L = 0, R = 0$.
- Apex sum: $\text{apex} = 9 + 0 + 0 = 9$.
- Update: $\text{max\_sum} = \max(-\infty, 9) = 9$.
- Upward return: $9 + \max(0, 0) = 9$.

---

### Step 2: Leaf Node 15 (Left child of 20)
- $L = 0, R = 0$.
- Apex sum: $\text{apex} = 15 + 0 + 0 = 15$.
- Update: $\text{max\_sum} = \max(9, 15) = 15$.
- Upward return: $15 + \max(0, 0) = 15$.

---

### Step 3: Leaf Node 7 (Right child of 20)
- $L = 0, R = 0$.
- Apex sum: $\text{apex} = 7 + 0 + 0 = 7$.
- Update: $\text{max\_sum} = \max(15, 7) = 15$.
- Upward return: $7 + \max(0, 0) = 7$.

---

### Step 4: Internal Node 20
- Left child Node 15 returned $15 \implies L = \max(0, 15) = 15$.
- Right child Node 7 returned $7 \implies R = \max(0, 7) = 7$.
- **Apex Sum at Node 20:**
  $$
  \text{apex} = 20 + L + R = 20 + 15 + 7 = \mathbf{42}
  $$
- Update: $\text{max\_sum} = \max(15, 42) = \mathbf{42}$.
- **Upward Return to Parent -10:**
  Must choose only the heavier child branch:
  $$
  \text{return } 20 + \max(15, 7) = 20 + 15 = \mathbf{35}
  $$

---

### Step 5: Root Node -10
- Left child Node 9 returned $9 \implies L = \max(0, 9) = 9$.
- Right child Node 20 returned $35 \implies R = \max(0, 35) = 35$.
- **Apex Sum at Root -10:**
  $$
  \text{apex} = -10 + L + R = -10 + 9 + 35 = 34
  $$
- Update: $\text{max\_sum} = \max(42, 34) = \mathbf{42}$.
- Upward return: $-10 + \max(9, 35) = -10 + 35 = 25$.

Traversal completes. Final maximum path sum: $\mathbf{42}$.

---

## 4. Complete Execution Trace

```text
               [-10] (Apex: -10 + 9 + 35 = 34)
              /     \
             /       \  (reports 35)
     [9] (reports 9)  [20] -> APEX PEAK: 20 + 15 + 7 = 42!
                      /  \
                     /    \
        [15] (rep 15)      [7] (rep 7)
```

| Node Evaluated | Clamped Left $L$ | Clamped Right $R$ | Local Apex Sum ($V + L + R$) | Global $\text{max\_sum}$ Updated | Single Branch Gain Returned ($V + \max(L, R)$) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $\text{Node}(9)$ | 0 | 0 | $9 + 0 + 0 = 9$ | 9 | $9 + 0 = 9$ |
| $\text{Node}(15)$ | 0 | 0 | $15 + 0 + 0 = 15$ | 15 | $15 + 0 = 15$ |
| $\text{Node}(7)$ | 0 | 0 | $7 + 0 + 0 = 7$ | 15 | $7 + 0 = 7$ |
| **$\text{Node}(20)$** | **15** | **7** | **$20 + 15 + 7 = 42$** | **42 (Global Max)** | **$20 + 15 = 35$** |
| $\text{Node}(-10)$ | 9 | 35 | $-10 + 9 + 35 = 34$ | 42 | $-10 + 35 = 25$ |

---

## 5. Algorithmic Correctness

**Soundness.** Any non-empty simple path in a binary tree has a unique highest node (the lowest common ancestor of all nodes in the path), which we call the apex. At this apex $u$, the path consists of $u$, an optional simple downward path in $u$'s left subtree, and an optional simple downward path in $u$'s right subtree. Because the downward paths in both subtrees are independently maximized, $u.\text{val} + L + R$ is the true maximum sum for any path with apex $u$.

**Completeness.** Every node in the tree is considered as a potential apex during the post-order traversal. Taking the maximum across all nodes guarantees finding the global maximum path sum.

---

## 6. Traps This Instance Exposes

- **Returning Apex Sum to Parent:** Returning $u.\text{val} + L + R$ to the parent violates the path definition by creating a 3-way fork at $u$. The function must return $u.\text{val} + \max(L, R)$.
- **Pruning Negative Branches:** If a subtree returns a negative gain (e.g. $-5$), including it in any path would reduce the sum. Clamping with $\max(0, \text{gain})$ safely discards harmful subtrees.
- **Trees with All Negative Values:** If the tree contains only negative numbers (e.g. `[-3, -2, -5]`), initializing $\text{max\_sum} = 0$ will return $0$, which is wrong (the answer is $-2$). Initializing $\text{max\_sum} = -\infty$ guarantees that the least negative single node is returned.

### Boundary and Degenerate Instances

Each row names the attaining path and the exact value the method reports; the last column says which part of the protocol produces that value.

| Instance | Structural condition | Optimal path | Attained sum | Why the protocol returns it |
|:---|:---|:---:|:---:|:---|
| `root = [1, 2, 3]` | Apex sits at the root and both children are positive | $2 \to 1 \to 3$ | $1 + 2 + 3 = 6$ | $L = 2$ and $R = 3$, so the root apex sum $6$ exceeds every single-node path. |
| `root = [-3]` | Single node, no children | $-3$ | $-3$ | $L = R = 0$ and the apex sum is $-3$; a running maximum seeded at $-\infty$ retains it. |
| `root = [2, -1]` | The only child returns a negative gain | $2$ | $2$ | The child is clamped by $\max(0, -1) = 0$, so the root apex sum is $2$, not the bridging $2 + (-1) = 1$. |
| `root = [-8, -3, -10, -4, -5]` | Every value is negative; the best apex is the internal node $-3$ | $-3$ | $-3$ | Every clamped gain is $0$, so only single-node apex sums survive; seeding the maximum at $0$ would wrongly answer $0$. |
| `root = [-10, 9, 20, null, null, 15, 7]` | The optimal apex lies strictly below the root | $15 \to 20 \to 7$ | $15 + 20 + 7 = 42$ | The root's own apex sum is only $34$, so the maximum is not monotone along any root-to-leaf descent. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. Each node is visited once during post-order traversal, performing $O(1)$ arithmetic operations.
- **Auxiliary Space Complexity:** $O(H)$, where $H$ is the tree height, for the recursion call stack ($O(\log N)$ average, $O(N)$ worst case).

### Why the Clamped-Gain Recursion Wins

| Approach | Mechanism | Time | Auxiliary space | Failure mode or tradeoff |
|:---|:---|:---:|:---:|:---|
| **Explicit path enumeration** | Walk the unique connecting path of each of the $\frac{N(N+1)}{2}$ node pairs and sum its values. | $\mathcal{O}(N^3)$ naive | $\mathcal{O}(N)$ for the current path | Correct but hopeless at $N = 3 \cdot 10^{4}$; caching prefix sums only reaches $\mathcal{O}(N^2)$. |
| **Downward-gain search restarted at every node** | Treat each node in turn as a start, descend to the best single branch, and combine the two child gains there. | $\mathcal{O}(N^2)$ | $\mathcal{O}(H)$ | Recomputes the same subtree gains repeatedly and times out at the constraint limit. |
| **Post-order clamped gain with apex update** (used here) | One post-order pass returns $u.\text{val} + \max(L, R)$ upward while recording $u.\text{val} + L + R$ in a global maximum. | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ | Requires the two return values to stay distinct; reporting the apex sum upward silently admits a fork. |
| **Running maximum seeded at $0$** | The same recursion, but the global best starts at $0$ rather than $-\infty$. | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ | Fails on all-negative trees: `root = [-3]` produces $0$ instead of $-3$. |