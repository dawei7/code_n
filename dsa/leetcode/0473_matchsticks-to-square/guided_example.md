# Guided Example: Matchsticks to Square

We trace the step-by-step 4-way side length validation ($side = \sum L / 4$), descending greedy sort pruning, recursive backtracking assignment to 4 edge buckets, and symmetric branch deduplication ($edges[i] == edges[i-1]$) on representative matchstick sets:

- **Input:** $matchsticks = [1, 1, 2, 2, 2]$
- **Required output:** `true`
  - Total length sum:
    $$
    S = 1 + 1 + 2 + 2 + 2 = 8
    $$
  - Divisibility check: $8 \pmod 4 = 0$ (Pass)
  - Target side length:
    $$
    side = 8 / 4 = \mathbf{2}
    $$
  - Max stick length check: $\max(matchsticks) = 2 \le side$ (Pass)
  - **Step 1: Sort descending:**
    $$
    matchsticks = [2, \; 2, \; 2, \; 1, \; 1]
    $$
  - **Step 2: Backtracking with symmetry pruning across 4 edges:**
    - Edge buckets: $edges = [0, 0, 0, 0]$
    - **Stick 0 (Length 2):**
      - Place on Edge 0: $edges[0] \leftarrow 0 + 2 = 2$. Bucket state: $[2, 0, 0, 0]$.
    - **Stick 1 (Length 2):**
      - Edge 0 is full ($2 + 2 > 2$).
      - Place on Edge 1: $edges[1] \leftarrow 0 + 2 = 2$. Bucket state: $[2, 2, 0, 0]$.
    - **Stick 2 (Length 2):**
      - Edges 0 and 1 full.
      - Place on Edge 2: $edges[2] \leftarrow 0 + 2 = 2$. Bucket state: $[2, 2, 2, 0]$.
    - **Stick 3 (Length 1):**
      - Edges 0, 1, 2 full.
      - Place on Edge 3: $edges[3] \leftarrow 0 + 1 = 1$. Bucket state: $[2, 2, 2, 1]$.
    - **Stick 4 (Length 1):**
      - Place on Edge 3: $edges[3] \leftarrow 1 + 1 = 2$. Bucket state: $[2, 2, 2, 2]$.
    - All 5 matchsticks placed ($u = 5 == N$), and all 4 edges reach exactly $side = 2$.
    - Return **`true`**.
- **Impossible Partition Instance:** $matchsticks = [3, 3, 3, 3, 4]$
  - Sum $S = 16 \implies side = 4$.
  - Stick 4 occupies Edge 0 ($edges[0] = 4$).
  - Remaining sticks $[3, 3, 3, 3]$ must fill three edges of length 4.
  - Adding stick 3 to any edge of length 0 leaves remaining needed length 1. No stick of length 1 exists $\implies$ **`false`**
- **Non-Divisible Sum:** $matchsticks = [1, 2, 3] \implies \sum = 6 \pmod 4 \ne 0 \implies \mathbf{false}$
- **Stick Exceeds Side Length:** $matchsticks = [5, 1, 1, 1] \implies S = 8, side = 2$, but stick $5 > 2 \implies \mathbf{false}$

This instance demonstrates 4-partition bin packing, mathematically proves why descending sort ordering and equal-bucket deduplication prune exponential search trees, and derives $O(4^N)$ pruned runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $matchsticks = [1, 1, 2, 2, 2]$:
You want to use **all** the matchsticks to make one square.
You cannot break any stick, and each stick must be used exactly once.
Return `true` if you can make the square, and `false` otherwise.

```text
Matchsticks Available: [ 2,  2,  2,  1,  1 ]
Total Length: 8
Target Side Length: 8 / 4 = 2

Assembled Square (Side Length = 2):
       [ 2 ]
     +-------+
 [2] |       | [2]
     +-------+
     [1] + [1]

All 4 sides reach length 2 -> true
```

### The 4-Partition Problem
A square requires 4 edges of identical length:
1. **Geometric Divisibility:** The sum of all matchstick lengths must be divisible by 4:
   $$
   S = \sum matchsticks, \quad S \pmod 4 == 0, \quad side = S / 4
   $$
2. **Stick Length Feasibility:** No individual stick can be longer than the target side:
   $$
   \max(matchsticks) \le side
   $$
3. **Subset Partitioning:** The set of sticks must partition into 4 disjoint subsets, each summing to exactly $side$.

---

## 2. Conceptual Foundation & Invariants

### 1. Descending Sort Optimization:
Sorting the matchsticks in **descending order** is the single most critical performance optimization:
- If a partition configuration is invalid, larger sticks fail to fit into buckets much earlier in the recursion tree.
- Trying a large stick of length 10 when space is 8 fails immediately at depth 1, pruning entire subtrees of $4^{N-1}$ branches compared to testing small 1s first.

### 2. Symmetry / Isomorphism Pruning:
In the recursive loop over the 4 edge buckets ($i \in [0, 3]$):
- If bucket $i$ and bucket $i - 1$ have the **exact same current sum** ($edges[i] == edges[i - 1]$):
  Placing the current stick into bucket $i$ produces an identical set of edge lengths as placing it into bucket $i - 1$.
- Skipping bucket $i$ eliminates redundant isomorphic permutations of the 4 indistinguishable edges.

> **Backtracking Invariant.** At depth $u$, matchsticks $0 \dots u-1$ are validly assigned to edge buckets with $edges[k] \le side$ for all $k \in [0, 3]$.

---

## 3. Step-by-Step Worked Execution

We trace $matchsticks = [1, 1, 2, 2, 2]$:

---

### Step 1: Pre-Verification & Sorting
- Sum: $S = 8$.
- Modulo: $8 \pmod 4 = 0$. Target: $side = 2$.
- Max stick: $2 \le 2$ (Pass).
- Sort descending:
  $$
  matchsticks = [2, \; 2, \; 2, \; 1, \; 1]
  $$
- Initialize edge buckets: $edges = [0, 0, 0, 0]$.

---

### Step 2: Backtracking Assignments
Call $dfs(0)$:

- **Depth 0 (Stick length 2):**
  - Try Edge 0 ($edges[0] = 0$): $0 + 2 \le 2 \implies edges[0] \leftarrow 2$.
  - State: $edges = [2, 0, 0, 0]$. Recurse to $dfs(1)$.

- **Depth 1 (Stick length 2):**
  - Edge 0: $2 + 2 = 4 > 2$ (Full: skip).
  - Edge 1 ($edges[1] = 0$): $0 + 2 \le 2 \implies edges[1] \leftarrow 2$.
  - State: $edges = [2, 2, 0, 0]$. Recurse to $dfs(2)$.

- **Depth 2 (Stick length 2):**
  - Edge 0, 1 full.
  - Edge 2 ($edges[2] = 0$): $0 + 2 \le 2 \implies edges[2] \leftarrow 2$.
  - State: $edges = [2, 2, 2, 0]$. Recurse to $dfs(3)$.

- **Depth 3 (Stick length 1):**
  - Edges 0, 1, 2: $2 + 1 = 3 > 2$ (Full: skip).
  - Edge 3 ($edges[3] = 0$): $0 + 1 \le 2 \implies edges[3] \leftarrow 1$.
  - State: $edges = [2, 2, 2, 1]$. Recurse to $dfs(4)$.

- **Depth 4 (Stick length 1):**
  - Edges 0, 1, 2 full.
  - Edge 3: $1 + 1 = 2 \le 2 \implies edges[3] \leftarrow 2$.
  - State: $edges = [2, 2, 2, 2]$. Recurse to $dfs(5)$.

- **Depth 5 (Base Case Reached):**
  - $u = 5 == N$.
  - All sticks placed. All edges equal 2.
  - Return **`true`**.

---

## 4. Complete Execution Trace

| Recursion Depth $u$ | Current Stick Length | Edge Targeted | Edge Sum Before | Edge Sum After | Fits $\le 2$? | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **$0$** | $2$ | Edge 0 | $0$ | $2$ | **Yes** | Advance to depth 1 |
| **$1$** | $2$ | Edge 1 | $0$ | $2$ | **Yes** | Advance to depth 2 |
| **$2$** | $2$ | Edge 2 | $0$ | $2$ | **Yes** | Advance to depth 3 |
| **$3$** | $1$ | Edge 3 | $0$ | $1$ | **Yes** | Advance to depth 4 |
| **$4$** | $1$ | Edge 3 | $1$ | $2$ | **Yes** | Advance to depth 5 |
| **$5$** | — | — | — | — | — | **Base Case: Return `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Total Not Divisible by 4 ($[3, 3, 3]$):** Sum 9 is not divisible by 4 $\implies \mathbf{false}$.
- **Individual Stick Exceeds Side ($[10, 1, 1, 2]$):** Sum 14 not divisible, or if sum 16 with $side = 4$, stick $10 > 4 \implies \mathbf{false}$.
- **Fewer Than 4 Sticks ($[1, 1, 2]$):** A square has 4 sides and sticks cannot be broken $\implies \mathbf{false}$.
- **All Sticks Equal ($[2, 2, 2, 2]$):** Exactly 4 sticks, each occupies one side $\implies \mathbf{true}$.

---

## 6. Traps & Common Anti-Patterns

- **Searching in Ascending Order:** Sorting in ascending order causes massive branch explosion, leading to Time Limit Exceeded on large inputs ($N = 15$). Descending sort places big constraints first, cutting 99.9% of dead-end search trees.
- **Forgetting Equal-Edge Pruning:** If $edges[i] == edges[i-1]$, placing a stick into bucket $i$ tests the exact same partition configuration as bucket $i-1$. Skipping equal buckets avoids $4!$ factorial permutations of the same assignment.
- **Floating-Point Division:** Using `sum / 4` with floating-point numbers risks rounding inaccuracies. Integer division `divmod(sum, 4)` guarantees strict modular divisibility.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In the unpruned worst case, each of the $N$ sticks can be placed into any of the 4 edges: $O(4^N)$.
  - With descending sort and symmetry pruning, invalid branches are pruned at top recursion levels.
  - For $N \le 15$, execution finishes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ recursion call stack depth, plus $O(1)$ for the 4-element edge array.