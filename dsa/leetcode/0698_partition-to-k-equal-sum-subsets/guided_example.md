# Guided Example: Partition to K Equal Sum Subsets

We trace the step-by-step sum divisibility gate ($S \pmod k == 0$), target bucket capacity calculation ($target = S / k$), descending order sorting optimization ($\text{largest-first heuristics}$), bucket placement backtracking ($cur[j] += nums[i]$), identical-bucket symmetry pruning ($cur[j] == cur[j-1] \implies \text{skip}$), capacity overshoot rejection ($cur[j] > target$), and valid $k$-subset partition synthesis on representative integer collections:

- **Input:** $nums = [4, 3, 2, 3, 5, 2, 1], \quad k = 4$
- **Required output:** `true`
  - Equal partition requirements:
    - Partition all elements of $nums$ into exactly $k = 4$ non-empty disjoint subsets.
    - Each subset must have the **exact same sum**.
    - For $[4, 3, 2, 3, 5, 2, 1]$:
      - Total sum: $4 + 3 + 2 + 3 + 5 + 2 + 1 = \mathbf{20}$.
      - Target sum per subset:
        $$
        target = \frac{20}{4} = \mathbf{5}
        $$
      - Valid 4-subset partition:
        - Subset 1: $\{5\}$ (sum $= 5$)
        - Subset 2: $\{4, 1\}$ (sum $= 5$)
        - Subset 3: $\{3, 2\}$ (sum $= 5$)
        - Subset 4: $\{3, 2\}$ (sum $= 5$)
      - All 4 subsets have sum 5. Return **`true`**.
- **Combinatorial Bin-Packing & Symmetry Pruning Invariant:**
  - **1. Divisibility & Maximum Element Gate:**
    - If the total sum $S$ is not divisible by $k$ ($S \pmod k \ne 0$), equal partition into integers is impossible $\implies \mathbf{False}$.
    - If the largest element exceeds the target ($\max(nums) > target$), that element can never be placed into any subset $\implies \mathbf{False}$.
  - **2. Descending Order Priority:**
    - Sort $nums$ in **descending order**: $[5, 4, 3, 3, 2, 2, 1]$.
    - Large elements have far fewer placement options than small elements. Placing them first forces early capacity violations near the root of the recursion tree, pruning massive subtrees.
  - **3. Identical Bucket Symmetry Pruning:**
    - At any point, multiple buckets may currently hold the exact same sum ($cur[j] == cur[j-1]$).
    - Placing element $nums[i]$ into bucket $j$ creates a state isomorphic to placing it into bucket $j-1$.
    - Pruning Rule: If $j > 0$ and $cur[j] == cur[j - 1]$, **skip bucket $j$ completely**.
- **Step-by-Step Worked Execution Trace on $[4, 3, 2, 3, 5, 2, 1]$ ($k = 4$):**
  - Total sum: $20, \; k = 4 \implies target = 5$.
  - Sorted array (descending):
    $$
    nums = [5, \; 4, \; 3, \; 3, \; 2, \; 2, \; 1]
    $$
  - Initialize 4 empty buckets:
    $$
    cur = [0, \; 0, \; 0, \; 0]
    $$
  - **Step 1: Place $nums[0] = 5$:**
    - Try Bucket 0: $cur[0] + 5 = 5 \le 5 \implies cur = [5, 0, 0, 0]$.
    - (Buckets 1, 2, 3 all have sum 0, so symmetry pruning skips them).
  - **Step 2: Place $nums[1] = 4$:**
    - Try Bucket 0: $cur[0] + 4 = 5 + 4 = 9 > 5 \implies$ Overshoot!
    - Try Bucket 1: $cur[1] + 4 = 0 + 4 = 4 \le 5 \implies cur = [5, 4, 0, 0]$.
    - (Buckets 2 and 3 have sum 0, skipped by symmetry).
  - **Step 3: Place $nums[2] = 3$:**
    - Try Bucket 0: $5 + 3 = 8 > 5$ (Overshoot).
    - Try Bucket 1: $4 + 3 = 7 > 5$ (Overshoot).
    - Try Bucket 2: $cur[2] + 3 = 0 + 3 = 3 \le 5 \implies cur = [5, 4, 3, 0]$.
  - **Step 4: Place $nums[3] = 3$:**
    - Try Bucket 0: $5 + 3 = 8 > 5$ (Overshoot).
    - Try Bucket 1: $4 + 3 = 7 > 5$ (Overshoot).
    - Try Bucket 2: $3 + 3 = 6 > 5$ (Overshoot).
    - Try Bucket 3: $cur[3] + 3 = 0 + 3 = 3 \le 5 \implies cur = [5, 4, 3, 3]$.
  - **Step 5: Place $nums[4] = 2$:**
    - Try Bucket 0: $5 + 2 = 7 > 5$ (Overshoot).
    - Try Bucket 1: $4 + 2 = 6 > 5$ (Overshoot).
    - Try Bucket 2: $cur[2] + 2 = 3 + 2 = \mathbf{5} \le 5 \implies cur = [5, 4, \mathbf{5}, 3]$.
  - **Step 6: Place $nums[5] = 2$:**
    - Try Bucket 0: $5 + 2 > 5$ (Overshoot).
    - Try Bucket 1: $4 + 2 > 5$ (Overshoot).
    - Try Bucket 2: $5 + 2 > 5$ (Overshoot).
    - Try Bucket 3: $cur[3] + 2 = 3 + 2 = \mathbf{5} \le 5 \implies cur = [5, 4, 5, \mathbf{5}]$.
  - **Step 7: Place $nums[6] = 1$:**
    - Try Bucket 0: $5 + 1 > 5$.
    - Try Bucket 1: $cur[1] + 1 = 4 + 1 = \mathbf{5} \le 5 \implies cur = [5, \mathbf{5}, 5, 5]$.
  - **Step 8: Base Case Reached ($i = 7 = len(nums)$):**
    - All elements placed.
    - Final bucket contents:
      $$
      cur = [5, \; 5, \; 5, \; 5]
      $$
    - Every subset has sum $5 == target$.
    - Unwind recursion immediately with **`true`**.
- **Indivisible Sum Failure Trace ($nums = [1, 2, 3, 4], k = 3$):**
  - Sum $S = 1 + 2 + 3 + 4 = 10$.
  - $10 \pmod 3 = 1 \ne 0$.
  - Ten cannot be evenly divided into 3 equal integer parts $\implies$ Returns **`false`** immediately at Step 1.
- **Single Element Exceeding Target ($nums = [10, 1, 1], k = 2$):**
  - Total sum: $12, \; target = 6$.
  - Largest element $10 > 6 \implies$ Returns **`false`** immediately.

This instance demonstrates NP-complete multi-way number partitioning, constraint satisfaction backtracking, and orbital symmetry breaking, mathematically proves why descending order item allocation maximizes early branch pruning, and derives $O(k^N)$ worst-case / heavily pruned runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array $nums$ and integer $k$:
Determine if $nums$ can be partitioned into **$k$ subsets with equal sums**.

```text
nums = [ 4, 3, 2, 3, 5, 2, 1 ], k = 4

Sum = 20, Target per subset = 20 / 4 = 5
Sorted descending: [ 5, 4, 3, 3, 2, 2, 1 ]

Bucket assignment:
  Bucket 1: [ 5 ]       -> sum = 5
  Bucket 2: [ 4, 1 ]    -> sum = 5
  Bucket 3: [ 3, 2 ]    -> sum = 5
  Bucket 4: [ 3, 2 ]    -> sum = 5

All 4 buckets sum to 5! Return true.
```

### The Invariant of Bin-Packing Symmetry
- Buckets are unlabeled and indistinguishable.
- If bucket $j$ has the same current sum as bucket $j - 1$, trying to put an element into bucket $j$ explores a configuration identical to bucket $j - 1$.
- Skipping identical buckets ($cur[j] == cur[j-1]$) eliminates $k!$ redundant permutations.

---

## 2. Conceptual Foundation & Invariants

### 1. Parity and Feasibility Pre-Check:
$$
target, \; rem = \text{divmod}(\sum nums, \; k)
$$
$$
rem \ne 0 \lor \max(nums) > target \implies \text{return } \mathbf{False}
$$

### 2. Backtracking Step:
For element $nums[i]$:
For bucket $j = 0 \dots k - 1$:
$$
\text{If } j > 0 \land cur[j] == cur[j - 1] \implies \text{continue}
$$
$$
\text{If } cur[j] + nums[i] \le target \implies \text{recurse } dfs(i + 1)
$$

> **Permutation Orbit Reduction Invariant.** The symmetric group $S_k$ acts transitively on the $k$ empty bins; by fixing the canonical orbit representative $cur[0] \ge cur[1] \ge \dots \ge cur[k-1]$, symmetry pruning removes all $k!$ equivalent permutations.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [5, 4, 3, 3, 2, 2, 1], k = 4, target = 5$:

---

### Step 1: Element 5
- Goes into Bucket 0: $cur = [5, 0, 0, 0]$.

---

### Step 2: Element 4
- Bucket 0 overshoots ($5 + 4 = 9 > 5$).
- Goes into Bucket 1: $cur = [5, 4, 0, 0]$.

---

### Step 3: Elements 3 and 3
- First 3 goes into Bucket 2: $cur = [5, 4, 3, 0]$.
- Second 3 goes into Bucket 3: $cur = [5, 4, 3, 3]$.

---

### Step 4: Elements 2, 2, 1
- First 2 completes Bucket 2: $3 + 2 = 5 \implies cur = [5, 4, 5, 3]$.
- Second 2 completes Bucket 3: $3 + 2 = 5 \implies cur = [5, 4, 5, 5]$.
- Element 1 completes Bucket 1: $4 + 1 = 5 \implies cur = [5, 5, 5, 5]$.

---

### Step 5: Output
- All elements assigned, all sums equal 5.
- Return **`true`**.

---

## 4. Complete Execution Trace

| Element $nums[i]$ | Value | Target Bucket | Condition $cur[j] + v \le 5$? | Resulting Bucket State $cur$ | Pruning Notes |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $nums[0]$ | $5$ | Bucket $0$ | $0 + 5 \le 5$ (Yes) | `[5, 0, 0, 0]` | Buckets 1, 2, 3 skipped (symmetry) |
| $nums[1]$ | $4$ | Bucket $1$ | $0 + 4 \le 5$ (Yes) | `[5, 4, 0, 0]` | Bucket 0 overshoots ($9 > 5$) |
| $nums[2]$ | $3$ | Bucket $2$ | $0 + 3 \le 5$ (Yes) | `[5, 4, 3, 0]` | Buckets 0, 1 overshoot |
| $nums[3]$ | $3$ | Bucket $3$ | $0 + 3 \le 5$ (Yes) | `[5, 4, 3, 3]` | Buckets 0, 1, 2 overshoot |
| $nums[4]$ | $2$ | Bucket $2$ | $3 + 2 \le 5$ (Yes) | `[5, 4, 5, 3]` | Bucket 2 reached capacity 5 |
| $nums[5]$ | $2$ | Bucket $3$ | $3 + 2 \le 5$ (Yes) | `[5, 4, 5, 5]` | Bucket 3 reached capacity 5 |
| **$nums[6]$** | **$1$** | **Bucket $1$** | **$4 + 1 \le 5$ (Yes)** | **`[5, 5, 5, 5]`** | **All 4 buckets full!** |
| **Final** | — | — | — | — | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **$k = 1$:** Target equals sum of all elements $\implies$ always `true`.
- **$k = N$:** All elements must be equal to each other; if any differ, returns `false`.
- **Total Sum Not Divisible by $k$:** Returns `false` in $O(1)$ without searching.
- **Max Element $> target$:** Returns `false` in $O(1)$ without searching.

---

## 6. Traps & Common Anti-Patterns

- **Searching in Ascending Order:** Putting small items first leads to deep recursion paths before realizing large items cannot fit. Sorting **descending** triggers early failure near the root.
- **Omission of Duplicate Bucket Pruning:** Without `cur[j] == cur[j-1]` pruning, identical empty buckets trigger $k!$ identical permutations, causing Time Limit Exceeded.
- **Greedy Bin-Packing Without Backtracking:** Greedy heuristics fail on adversarial inputs like $[4, 3, 3, 2, 2, 2], k = 2$ ($target = 8$); exhaustive backtracking with pruning is required.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In the worst case without pruning: $\mathcal{O}(k^N)$.
  - With descending sort, capacity bounds, and symmetry breaking: typical runtime is $\mathcal{O}(k \cdot 2^N)$.
  - For $N \le 16$, executes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ recursion stack depth plus $\mathcal{O}(k)$ bucket array.
