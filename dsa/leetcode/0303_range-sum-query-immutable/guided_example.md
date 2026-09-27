# Guided Example: Range Sum Query - Immutable

We trace the step-by-step 1D prefix sum array construction, boundary zero sentinel indexing, algebraic cancellation of prefix segments, and $O(1)$ query evaluation on representative integer sequence instances:

- **Input:**
  $$
  \text{nums} = [-2, 0, 3, -5, 2, -1]
  $$
  $$
  \text{queries} = [\text{sumRange}(0, 2), \; \text{sumRange}(2, 5), \; \text{sumRange}(0, 5)]
  $$
- **Required output:** $[1, -1, -3]$
  - $\text{sumRange}(0, 2) = (-2) + 0 + 3 = 1$
  - $\text{sumRange}(2, 5) = 3 + (-5) + 2 + (-1) = -1$
  - $\text{sumRange}(0, 5) = (-2) + 0 + 3 + (-5) + 2 + (-1) = -3$
- **Single Element Query:** $\text{sumRange}(i, i) = s[i+1] - s[i] = \text{nums}[i]$
- **Full Array Query:** $\text{sumRange}(0, N-1) = s[N] - s[0] = s[N]$ (Entire array sum)
- **Negative and Zero Elements:** Prefix sum properties hold universally across positive, negative, and zero values

This instance demonstrates constant-time range sum querying via prefix difference decomposition, explains why a 1-based prefix array with a leading zero ($s[0] = 0$) eliminates edge-case branching for left index zero, contrasts $O(1)$ querying with $O(N)$ repetitive naive loops, and achieves $O(N)$ construction time and space.

---

## 1. Instance & Teaching Goal

Given an integer array:
$$
\text{nums} = [-2, 0, 3, -5, 2, -1] \quad (N = 6)
$$
We need to process multiple range sum queries $\text{sumRange}(left, right) = \sum_{i=left}^{right} \text{nums}[i]$ efficiently.

```text
Array:        [-2,  0,  3, -5,  2, -1]
Indices:        0   1   2   3   4   5

Query (0, 2): [-2,  0,  3]                -> Sum = 1
Query (2, 5):          [3, -5,  2, -1]    -> Sum = -1
Query (0, 5): [-2,  0,  3, -5,  2, -1]    -> Sum = -3
```

### Naive Loop vs Prefix Sums
- Naively summing from `left` to `right` costs $O(R - L + 1) = O(N)$ per query. For $Q = 10^4$ queries, total runtime degrades to $O(Q \cdot N) \approx 10^8$ operations.
- By spending $O(N)$ preprocessing time to build cumulative prefix sums, every query can be answered via a single subtraction in **$O(1)$ time**!

---

## 2. Conceptual Foundation & Invariants

### 1-Based Prefix Sum Definition
Define array $s$ of length $N + 1$ such that $s[k]$ stores the sum of the first $k$ elements:
$$
s[0] = 0
$$
$$
s[k] = \sum_{j=0}^{k-1} \text{nums}[j] = s[k-1] + \text{nums}[k-1] \quad \text{for } k \in [1, N]
$$

### The Telescoping Range Sum Formula:
For any query $[left, right]$:
$$
\sum_{i=left}^{right} \text{nums}[i] = \left(\sum_{j=0}^{right} \text{nums}[j]\right) - \left(\sum_{j=0}^{left-1} \text{nums}[j]\right) = s[right + 1] - s[left]
$$

```text
Elements:   nums[0] ... nums[left-1] | nums[left] ... nums[right] | nums[right+1] ...
s[left]:    [----------------------]
s[right+1]: [---------------------------------------------------]
Difference:                          [--------------------------] = Sum(left..right)
```

> **Invariant.** For all $0 \le left \le right < N$, $s[right + 1] - s[left]$ algebraically cancels all elements before index $left$, leaving precisely the sum of the closed interval $[left, right]$.

---

## 3. Step-by-Step Worked Execution

We trace the preprocessing and queries on $\text{nums} = [-2, 0, 3, -5, 2, -1]$:

---

### Step 1: Precompute Prefix Array $s$
Initialize $s$ of size $N + 1 = 7$ with $s[0] = 0$:
- $k = 1$: $s[1] = s[0] + \text{nums}[0] = 0 + (-2) = \mathbf{-2}$
- $k = 2$: $s[2] = s[1] + \text{nums}[1] = -2 + 0 = \mathbf{-2}$
- $k = 3$: $s[3] = s[2] + \text{nums}[2] = -2 + 3 = \mathbf{1}$
- $k = 4$: $s[4] = s[3] + \text{nums}[3] = 1 + (-5) = \mathbf{-4}$
- $k = 5$: $s[5] = s[4] + \text{nums}[4] = -4 + 2 = \mathbf{-2}$
- $k = 6$: $s[6] = s[5] + \text{nums}[5] = -2 + (-1) = \mathbf{-3}$

Final prefix array:
$$
s = [0, \; -2, \; -2, \; 1, \; -4, \; -2, \; -3]
$$

---

### Step 2: Evaluate Query 1 — $\text{sumRange}(0, 2)$
- $left = 0, \; right = 2$.
- Formula:
  $$
  \text{Sum} = s[right + 1] - s[left] = s[3] - s[0]
  $$
- Substitute values:
  $$
  s[3] = 1, \quad s[0] = 0 \implies 1 - 0 = \mathbf{1}
  $$

---

### Step 3: Evaluate Query 2 — $\text{sumRange}(2, 5)$
- $left = 2, \; right = 5$.
- Formula:
  $$
  \text{Sum} = s[right + 1] - s[left] = s[6] - s[2]
  $$
- Substitute values:
  $$
  s[6] = -3, \quad s[2] = -2 \implies -3 - (-2) = -3 + 2 = \mathbf{-1}
  $$

---

### Step 4: Evaluate Query 3 — $\text{sumRange}(0, 5)$
- $left = 0, \; right = 5$.
- Formula:
  $$
  \text{Sum} = s[right + 1] - s[left] = s[6] - s[0]
  $$
- Substitute values:
  $$
  s[6] = -3, \quad s[0] = 0 \implies -3 - 0 = \mathbf{-3}
  $$

---

## 4. Complete Execution Trace

```text
nums = [-2, 0, 3, -5, 2, -1]
s    = [ 0, -2, -2,  1, -4, -2, -3]

Query (0, 2): s[3] - s[0] =  1 - (0)  =  1
Query (2, 5): s[6] - s[2] = -3 - (-2) = -1
Query (0, 5): s[6] - s[0] = -3 - (0)  = -3

Results: [1, -1, -3]
```

| Index $k$ | $\text{nums}[k-1]$ | Cumulative Sum $s[k]$ | Prefix Covered in $\text{nums}$ |
|:---:|:---:|:---:|:---|
| 0 | - | **0** | Empty prefix $(\emptyset)$ |
| 1 | -2 | **-2** | $\text{nums}[0..0]$ |
| 2 | 0 | **-2** | $\text{nums}[0..1]$ |
| 3 | 3 | **1** | $\text{nums}[0..2]$ |
| 4 | -5 | **-4** | $\text{nums}[0..3]$ |
| 5 | 2 | **-2** | $\text{nums}[0..4]$ |
| 6 | -1 | **-3** | $\text{nums}[0..5]$ |

| Query $[left, right]$ | Suffix Boundary $s[right + 1]$ | Prefix Boundary $s[left]$ | Subtraction Formula | Computed Result |
|:---:|:---:|:---:|:---:|:---:|
| $[0, 2]$ | $s[3] = 1$ | $s[0] = 0$ | $1 - 0$ | **1** |
| $[2, 5]$ | $s[6] = -3$ | $s[2] = -2$ | $-3 - (-2)$ | **-1** |
| $[0, 5]$ | $s[6] = -3$ | $s[0] = 0$ | $-3 - 0$ | **-3** |

---

## 5. Algorithmic Correctness

**Soundness.** By mathematical definition, $s[right + 1] = \sum_{j=0}^{right} \text{nums}[j]$ and $s[left] = \sum_{j=0}^{left-1} \text{nums}[j]$. Subtracting the latter from the former cancels all terms from $j = 0$ up to $left - 1$, leaving the exact summation from $j = left$ to $j = right$.

**Completeness.** The array $s$ has length $N + 1$, where index 0 represents the empty prefix sum. For any valid query $0 \le left \le right < N$, both $s[right + 1]$ and $s[left]$ are within valid bounds $[0, N]$. Thus, all possible range queries are supported without edge-case out-of-bounds access.

---

## 6. Traps This Instance Exposes

- **Missing Leading Zero:** If $s$ is built with length $N$ where $s[i]$ is the sum up to index $i$, queries starting at $left = 0$ require special conditional handling (`return s[right] if left == 0 else s[right] - s[left-1]`). A leading zero ($s[0] = 0$) makes the formula $s[right + 1] - s[left]$ uniform for all queries.
- **Off-by-One in Ending Index:** Writing $s[right] - s[left]$ mistakenly excludes $\text{nums}[right]$. Because $s$ is shifted by 1, the prefix containing elements up to $right$ is stored at index $right + 1$.
- **Mutable vs Immutable Contract:** This data structure assumes `nums` is static. If elements were updated dynamically, modifying a single value would invalidate up to $N$ entries in $s$, requiring a Segment Tree or Fenwick Tree ($O(\log N)$ update and query).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initialization: $O(N)$ linear time to compute the $N + 1$ prefix sums.
  - `sumRange(left, right)`: $O(1)$ constant time, performing a single array lookup and subtraction.
  - Total time for $Q$ queries: $O(N + Q)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the prefix sum array $s$ of size $N + 1$.
