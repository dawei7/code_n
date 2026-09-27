# Guided Example: Russian Doll Envelopes

We trace the step-by-step two-dimensional sorting transformation (Widths ascending, Heights descending: `key=lambda x: (x[0], -x[1])`), the reduction to 1D Longest Increasing Subsequence (LIS), patience sorting binary search (`bisect_left`), and greedy tail array maintenance (`d`) on representative envelope sets:

- **Input:** `envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]`
- **Required output:** $3$
  - Custom sort transformation:
    - Widths in ascending order: $2 < 5 < 6$
    - For tied width $6$: sort heights in descending order $\implies [6, 7]$ precedes $[6, 4]$
    - Sorted envelopes: `[[2, 3], [5, 4], [6, 7], [6, 4]]`
  - Projected heights sequence: $[3, 4, 7, 4]$
  - LIS on heights:
    - Process $3 \implies d = [3]$
    - Process $4 \implies d = [3, 4]$
    - Process $7 \implies d = [3, 4, 7]$
    - Process $4 \implies$ replaces $4$ at index 1 $\implies d = [3, 4, 7]$
  - Length of LIS: $3$
  - Optimal nested chain: `[2, 3] -> [5, 4] -> [6, 7]` (Length 3)
- **Tied Width Multiplicity:** `[[1, 1], [1, 1], [1, 1]] \implies 1` (Only 1 envelope can be chosen)
- **Strict Inequality Requirement:** Width and height must both be strictly greater; $\le$ nesting is disallowed

This instance demonstrates dimensional reduction via composite sorting keys, mathematically proves why descending height order on tied widths enforces width uniqueness in $O(1)$ comparisons, and establishes $O(N \log N)$ time and $O(N)$ space complexity.

---

## 1. Instance & Teaching Goal

Given a 2D collection of envelopes `envelopes[i] = [w_i, h_i]`:
An envelope $(w_1, h_1)$ can fit inside $(w_2, h_2)$ if and only if:
$$
w_1 < w_2 \quad \text{and} \quad h_1 < h_2
$$
Find the maximum number of envelopes that can be nested inside one another (Russian dolled):

```text
Input Envelopes: [[5, 4], [6, 4], [6, 7], [2, 3]]

Sort Strategy: Width ASC, Height DESC for ties:
[2, 3]  (w = 2, h = 3)
[5, 4]  (w = 5, h = 4)
[6, 7]  (w = 6, h = 7)  <-- height 7 placed before 4
[6, 4]  (w = 6, h = 4)  <-- height 4 cannot extend height 7

Extracted Heights: [3, 4, 7, 4]
Longest Increasing Subsequence (LIS): 3 -> 4 -> 7 (Length 3)
```

### The $O(N^2)$ Dynamic Programming vs $O(N \log N)$ LIS Goal
- A naive 2D DP checks every pair $(i, j)$, requiring $O(N^2)$ time, which times out on $N = 10^5$.
- By sorting widths ascending, width ordering is guaranteed ($w_i \le w_j$ for all $i < j$).
- Sorting heights in **descending order for equal widths** guarantees that no two envelopes with identical width can appear in an increasing subsequence of heights!
- This reduces the 2D problem strictly to 1D LIS on heights, solvable in $O(N \log N)$ via patience sorting.

---

## 2. Conceptual Foundation & Invariants

### 1. The Composite Sorting Key: `(w, -h)`
Sort all envelopes using:
$$
\text{key} = (x[0], \; -x[1])
$$
- If $w_1 < w_2$: envelope 1 appears before envelope 2.
- If $w_1 == w_2$: the envelope with **larger height** appears first.
*Why descending height for ties?*
Suppose we have $[6, 4]$ and $[6, 7]$. They have identical width $6$, so neither can fit inside the other.
If we sorted heights ascending ($4, 7$), a standard LIS would pick both $4$ and $7$ (since $4 < 7$), falsely concluding they can nest!
Sorting descending ($7, 4$) ensures $4 < 7$ is reversed ($7$ then $4$). Since $4 \not> 7$, an increasing subsequence can select at most one of them!

### 2. Patience Sorting LIS Maintenance
Let $d$ be an array where $d[k]$ stores the smallest tail value of an increasing subsequence of length $k + 1$:
- For each height $h$:
  - If $h > d[-1]$: append $h$ to $d$ ($d.\text{append}(h)$).
  - Else: find replacement index $idx = \text{bisect\_left}(d, h)$ and overwrite $d[idx] = h$.

> **Invariant.** The length of array $d$ at all times equals the length of the Longest Increasing Subsequence of valid nesting envelopes processed so far.

---

## 3. Step-by-Step Worked Execution

We trace `envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]`:

---

### Step 1: Composite Key Sort
Sort with `key = (w, -h)`:
1. $[2, 3]$: $w = 2, -h = -3$
2. $[5, 4]$: $w = 5, -h = -4$
3. $[6, 7]$: $w = 6, -h = -7$
4. $[6, 4]$: $w = 6, -h = -4$
Sorted Array:
$$
[[2, 3], \; [5, 4], \; [6, 7], \; [6, 4]]
$$
Heights stream: $[3, 4, 7, 4]$.

---

### Step 2: Initialize LIS Array $d$
- First height $h = 3$:
  $$
  d = [\mathbf{3}]
  $$

---

### Step 3: Process Envelope 1 ($[5, 4] \implies h = 4$)
- Compare $h = 4$ against current tail $d[-1] = 3$:
  $$
  4 > 3 \implies \text{Can extend sequence!}
  $$
- Append to $d$:
  $$
  d = [3, \; \mathbf{4}]
  $$
- Longest chain length so far: $2$.

---

### Step 4: Process Envelope 2 ($[6, 7] \implies h = 7$)
- Compare $h = 7$ against current tail $d[-1] = 4$:
  $$
  7 > 4 \implies \text{Can extend sequence!}
  $$
- Append to $d$:
  $$
  d = [3, 4, \; \mathbf{7}]
  $$
- Longest chain length so far: $3$.

---

### Step 5: Process Envelope 3 ($[6, 4] \implies h = 4$)
- Compare $h = 4$ against current tail $d[-1] = 7$:
  $$
  4 \not> 7 \implies \text{Cannot extend.}
  $$
- Binary search for replacement index:
  $$
  idx = \text{bisect\_left}([3, 4, 7], \; 4) = \mathbf{1}
  $$
- Overwrite $d[1]$ with $4$:
  $$
  d[1] = 4 \implies d = [3, \; \mathbf{4}, \; 7]
  $$
- Array length remains $3$.

---

### Step 6: Final Result
All envelopes evaluated.
$$
\text{Result} = \text{len}(d) = \mathbf{3}
$$

---

## 4. Complete Execution Trace

```text
Input: [[5, 4], [6, 4], [6, 7], [2, 3]]
Sorted (w ASC, h DESC): [[2, 3], [5, 4], [6, 7], [6, 4]]
Heights Sequence: [3, 4, 7, 4]

Step 0: Envelope [2, 3] -> h = 3 -> d = [3]
Step 1: Envelope [5, 4] -> h = 4 > 3 -> d = [3, 4]
Step 2: Envelope [6, 7] -> h = 7 > 4 -> d = [3, 4, 7]
Step 3: Envelope [6, 4] -> h = 4 <= 7 -> bisect_left gives idx 1 -> d[1]=4 -> d = [3, 4, 7]

Final LIS Length: len(d) = 3
Optimal Nesting Chain: [2, 3] -> [5, 4] -> [6, 7]
```

| Step | Envelope $(w, h)$ | Height $h$ | Condition vs $d[-1]$ | Binary Search Index | Tail Array $d$ State | Current LIS Length |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `[2, 3]` | 3 | Initial | - | `[3]` | 1 |
| 1 | `[5, 4]` | 4 | $4 > 3$ (Extend) | - | `[3, 4]` | 2 |
| **2** | **`[6, 7]`** | **7** | **$7 > 4$ (Extend)** | **-** | **`[3, 4, 7]`** | **3 (Max)** |
| 3 | `[6, 4]` | 4 | $4 \le 7$ (Replace) | 1 | `[3, 4, 7]` | 3 |
| **Exit** | - | - | - | - | **$\text{len}(d) = 3$** | **$\mathbf{3}$ (Output)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every pair of envelopes $(w_1, h_1)$ and $(w_2, h_2)$ in the extracted subsequence satisfies $h_1 < h_2$ (by virtue of strict LIS). Because the array was sorted by width, $w_1 \le w_2$. If $w_1 == w_2$, our sorting rule placed the larger height first ($h_1 \ge h_2$), contradicting $h_1 < h_2$. Therefore, $w_1 == w_2$ is impossible in an increasing subsequence, which proves that $w_1 < w_2$ strictly holds. Hence, every selected pair is strictly nestable in both dimensions.

**Completeness.** Any valid nested sequence must have strictly increasing widths and strictly increasing heights. Because envelopes are ordered by width, the maximum nestable subset corresponds to an increasing subsequence of heights. Patience sorting guarantees finding the exact maximum length of any LIS.

---

## 6. Traps This Instance Exposes

- **Sorting Tied Widths Ascending:** If sorted as `key=lambda x: (x[0], x[1])`, `[6, 4]` comes before `[6, 7]`. The LIS on heights would select both $4$ and $7$, falsely claiming `[6, 4]` fits inside `[6, 7]` even though their widths are identical ($6 \not< 6$). Descending height for ties is mandatory.
- **Weak Inequality Fallacy:** The problem requires strict nesting ($w_1 < w_2$ and $h_1 < h_2$). An envelope of size $(4, 5)$ cannot fit inside $(4, 6)$ or $(4, 5)$.
- **Patience Sorting vs Actual Subsequence:** The tail array $d$ computes the correct **length** of the LIS in $O(N \log N)$, but $d$ itself does not necessarily contain the exact original chain elements. For finding length, tracking $d$ is optimal.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$, where $N$ is the number of envelopes.
  - Sorting $N$ pairs takes $O(N \log N)$ time.
  - The LIS pass iterates $N$ times, executing binary search `bisect_left` in $O(\log N)$ time per element.
  - Total runtime is strictly $O(N \log N)$, easily handling $N = 10^5$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space to store the tail array $d$.
