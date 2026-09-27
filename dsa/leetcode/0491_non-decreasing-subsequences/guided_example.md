# Guided Example: Non-decreasing Subsequences

We trace the step-by-step pick-or-skip decision tree, non-decreasing order enforcement ($nums[u] \ge last$), sibling branch deduplication ($nums[u] \ne last$), minimum length filtering ($\text{len}(t) \ge 2$), and duplicate avoidance on representative numeric sequences:

- **Input:** $nums = [4, 6, 7, 7]$
- **Required output:**
  $$
  [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]
  $$
  (Order of subsequences does not matter)
- **Subsequence decision trace:**
  - Length of input: $N = 4$
  - Initial call: $u = 0, \; last = -\infty, \; t = []$
  - **Level 0 (Inspect $nums[0] = 4$):**
    - $4 \ge -\infty \implies$ **Branch Pick 4:** $t = [4], \; last = 4$
    - **Branch Skip 4:** $t = [], \; last = -\infty$
  - **Subtree starting with $[4]$ ($last = 4$):**
    - **Level 1 (Inspect $nums[1] = 6$):**
      - $6 \ge 4 \implies$ **Pick 6:** $t = [4, 6], \; last = 6$
        - At end of array or extensions: emits $[4, 6]$!
        - Level 2 ($nums[2] = 7 \ge 6$):
          - **Pick 7:** $t = [4, 6, 7]$, emits $[4, 6, 7]$
            - Level 3 ($nums[3] = 7 \ge 7$):
              - **Pick 7:** $t = [4, 6, 7, 7]$, emits $[4, 6, 7, 7]$
              - Skip 7: Since $nums[3] == last (7)$, skip branch is **pruned** to avoid emitting duplicate $[4, 6, 7]$!
          - **Skip 7:** $t = [4, 6]$
            - Level 3 ($nums[3] = 7$): Pick 7 would produce $[4, 6, 7]$ which was already emitted.
      - **Skip 6:** $t = [4], \; last = 4$
        - Level 2 ($nums[2] = 7 \ge 4$):
          - **Pick 7:** $t = [4, 7]$, emits $[4, 7]$
            - Level 3 ($nums[3] = 7 \ge 7$):
              - **Pick 7:** $t = [4, 7, 7]$, emits $[4, 7, 7]$
  - **Subtree starting without $[4]$:**
    - Subtree starting with $[6] \implies$ emits $[6, 7], [6, 7, 7]$
    - Subtree starting with $[7] \implies$ emits $[7, 7]$
  - Total valid non-decreasing subsequences: exactly **8 unique lists**.
- **Descending Array Instance:** $nums = [4, 3, 2, 1] \implies$ no pairs satisfy $nums[j] \ge nums[i] \implies \mathbf{[]}$
- **Two Identical Elements:** $nums = [4, 4] \implies \mathbf{[[4, 4]]}$

This instance demonstrates constrained combinatorial subsequence enumeration, mathematically proves how duplicate sibling skipping eliminates identical list emissions, and derives $O(2^N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [4, 6, 7, 7]$:
Return all the **different possible non-decreasing subsequences** of the given array with **at least two elements**.
The output can be returned in any order, but must contain **no duplicate subsequences**.

```text
Input: [ 4,  6,  7,  7 ]

Subsequences of Length 2:
  [4, 6], [4, 7], [6, 7], [7, 7]

Subsequences of Length 3:
  [4, 6, 7], [4, 7, 7], [6, 7, 7]

Subsequences of Length 4:
  [4, 6, 7, 7]

Notice: nums contains two 7s, but [4, 7] is emitted exactly ONCE!
```

### The In-Place Preservation of Subsequence Order
- Because subsequences must maintain their original relative order in $nums$, **we cannot sort $nums$**.
- Instead, we must perform Depth-First Search over the original indices, enforcing:
  1. **Non-decreasing condition:** $nums[u] \ge last$
  2. **Deduplication rule:** When multiple identical numbers appear at the same level, only one branch is allowed to skip or take them, preventing identical outputs.

---

## 2. Conceptual Foundation & Invariants

### 1. The Decision State $(u, last, t)$:
- $u$: current index in $nums$ being considered ($0 \le u \le N$).
- $last$: the value of the most recently added element in the current subsequence $t$.
- $t$: the current subsequence of chosen elements.

### 2. Recursive Transitions:
At index $u$:
1. **Branch A (Include $nums[u]$):**
   Feasible if $nums[u] \ge last$:
   $$
   t.\text{append}(nums[u]) \implies dfs(u + 1, \; nums[u], \; t) \implies t.\text{pop}()
   $$
2. **Branch B (Exclude $nums[u]$):**
   To avoid duplicate permutations when $nums[u] == last$:
   $$
   \text{If } nums[u] \ne last: \quad dfs(u + 1, \; last, \; t)
   $$
   If $nums[u] == last$, the option of excluding $nums[u]$ produces the exact same future search space as having included the previous copy, so skipping is pruned.

### 3. Collection Base Case:
When $u == N$:
If $|t| \ge 2$:
$$
ans.\text{append}(t)
$$

> **Deduplication Invariant.** Pruning the skip branch whenever $nums[u] == last$ guarantees that every unique non-decreasing sequence of values is visited via a unique path in the recursion tree.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [4, 6, 7, 7]$ ($N = 4$):

---

### Step 1: Root Call $dfs(0, -1000, [])$
- $nums[0] = 4 \ge -1000$:
  - Include $4 \implies dfs(1, 4, [4])$.
  - Exclude $4 \implies dfs(1, -1000, [])$.

---

### Step 2: Exploring Path $t = [4]$ ($last = 4$)
- At $u = 1$ ($nums[1] = 6 \ge 4$):
  - **Include 6:** $dfs(2, 6, [4, 6])$.
    - At $u = 2$ ($nums[2] = 7 \ge 6$):
      - **Include 7:** $dfs(3, 7, [4, 6, 7])$.
        - At $u = 3$ ($nums[3] = 7 \ge 7$):
          - **Include 7:** $dfs(4, 7, [4, 6, 7, 7]) \implies$ Base case: Emit **`[4, 6, 7, 7]`**!
          - **Exclude 7:** $nums[3] == last (7) \implies$ Skip pruned!
        - Backtrack to $u = 3$ base: Emit **`[4, 6, 7]`**!
      - **Exclude 7:** $dfs(3, 6, [4, 6])$:
        - At $u = 3$ ($nums[3] = 7$): Include 7 would duplicate $[4, 6, 7]$.
    - Backtrack: Emit **`[4, 6]`**!
  - **Exclude 6:** $dfs(2, 4, [4])$:
    - At $u = 2$ ($nums[2] = 7 \ge 4$):
      - **Include 7:** $dfs(3, 7, [4, 7])$.
        - Include second 7: emits **`[4, 7, 7]`**!
        - Base: Emit **`[4, 7]`**!

---

### Step 3: Exploring Path Without 4
- Include 6: emits **`[6, 7]`**, **`[6, 7, 7]`**.
- Exclude 6:
  - Include both 7s: emits **`[7, 7]`**.

---

### Summary of Emitted Subsequences:
1. `[4, 6]`
2. `[4, 7]`
3. `[4, 6, 7]`
4. `[4, 6, 7, 7]`
5. `[4, 7, 7]`
6. `[6, 7]`
7. `[6, 7, 7]`
8. `[7, 7]`
Total: 8 subsequences.

---

## 4. Complete Execution Trace

| Subsequence Formed | Length $\ge 2$? | Non-decreasing Check | Duplicate Status | Emitted to Answer? |
|:---:|:---:|:---:|:---:|:---:|
| `[4, 6]` | Yes (2) | $4 \le 6$ | First occurrence | **Yes** |
| `[4, 7]` | Yes (2) | $4 \le 7$ | First occurrence | **Yes** |
| `[4, 6, 7]` | Yes (3) | $4 \le 6 \le 7$ | First occurrence | **Yes** |
| `[4, 6, 7, 7]` | Yes (4) | $4 \le 6 \le 7 \le 7$ | Unique | **Yes** |
| `[4, 7, 7]` | Yes (3) | $4 \le 7 \le 7$ | Unique | **Yes** |
| `[6, 7]` | Yes (2) | $6 \le 7$ | First occurrence | **Yes** |
| `[6, 7, 7]` | Yes (3) | $6 \le 7 \le 7$ | Unique | **Yes** |
| `[7, 7]` | Yes (2) | $7 \le 7$ | Unique | **Yes** |

---

## 5. Boundary Cases & Failure Modes

- **Strictly Decreasing Array ($[5, 4, 3, 2, 1]$):** No pair can satisfy $nums[j] \ge nums[i] \implies \mathbf{[]}$.
- **All Identical Elements ($[2, 2, 2]$):** Emits $[2, 2]$ and $[2, 2, 2]$ without duplicates.
- **Short Input ($N = 1$):** Minimum length requires $\ge 2$ elements $\implies \mathbf{[]}$.
- **Negative Numbers ($[-10, -5, 0]$):** $last$ initialized to $-1000$ ensures negative numbers $\ge -100$ are correctly included.

---

## 6. Traps & Common Anti-Patterns

- **Sorting the Input Array:** Sorting destroys the subsequence order (e.g. $[4, 6, 7, 7]$ might be sorted, but $[4, 7, 6, 7]$ would have its relative ordering reversed). Subsequences must be drawn strictly in index-increasing order.
- **Using a Global Set of Tuples:** Collecting all subsequences in a Python `set(tuple(t))` works, but generates exponential duplicate branches that waste time and memory. In-tree deduplication via `nums[u] != last` or level-wise sets prevents generating duplicates altogether.
- **Forgetting Length $\ge 2$ Condition:** Emitting single-element subsequences like $[4]$ or $[6]$ violates the problem requirement. The length check `len(t) > 1` must guard all insertions into $ans$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In the worst case (all non-decreasing), every subset of size $\ge 2$ is a valid subsequence.
  - The number of subsets of size $N$ is $2^N$.
  - For $N \le 15$, $2^{15} = 32,768$ states, executing in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ recursion call stack and temporary list buffer $t$.
