# Guided Example: Rotate Function

We trace the step-by-step mathematical difference recurrence ($F(k) = F(k-1) + S - n \cdot nums[n-k]$), coefficient shifting algebra, clockwise array rotation transitions, and linear-time maximum tracking on representative numerical arrays:

- **Input:** $nums = [4, 3, 2, 6]$
- **Required output:** $26$
  - Array length: $n = 4$
  - Total array sum: $S = 4 + 3 + 2 + 6 = 15$
  - Step 1 (Base Rotation $k = 0$):
    - Array: $[4, 3, 2, 6]$
    - $F(0) = 0 \times 4 + 1 \times 3 + 2 \times 2 + 3 \times 6 = 0 + 3 + 4 + 18 = \mathbf{25}$
  - Step 2 (Rotation $k = 1$):
    - Wrapped element: $nums[4 - 1] = nums[3] = 6$
    - Recurrence: $F(1) = 25 + 15 - 4 \times 6 = 40 - 24 = \mathbf{16}$
  - Step 3 (Rotation $k = 2$):
    - Wrapped element: $nums[4 - 2] = nums[2] = 2$
    - Recurrence: $F(2) = 16 + 15 - 4 \times 2 = 31 - 8 = \mathbf{23}$
  - Step 4 (Rotation $k = 3$):
    - Wrapped element: $nums[4 - 3] = nums[1] = 3$
    - Recurrence: $F(3) = 23 + 15 - 4 \times 3 = 38 - 12 = \mathbf{26}$
  - Global maximum: $\max(25, 16, 23, 26) = \mathbf{26}$ (Achieved at rotation $k = 3$)
- **Single Element Array:** $nums = [100] \implies F(0) = 0 \times 100 = 0$
- **All Equal Elements:** $nums = [2, 2, 2] \implies F(k) = 0\cdot 2 + 1\cdot 2 + 2\cdot 2 = 6$ for all $k$

This instance demonstrates algebraic optimization reducing brute-force $O(N^2)$ recalculations to strictly $O(N)$ linear time by deriving the difference relation between adjacent rotation states in $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [4, 3, 2, 6]$ of length $n = 4$:
Let $F(k) = \sum_{j=0}^{n-1} j \cdot arr_k[j]$, where $arr_k$ is the array rotated clockwise by $k$ positions.
Find the maximum value of $F(0), F(1), \dots, F(n-1)$:

```text
k = 0: [ 4, 3, 2, 6 ] -> F(0) = 0*4 + 1*3 + 2*2 + 3*6 = 25
k = 1: [ 6, 4, 3, 2 ] -> F(1) = 0*6 + 1*4 + 2*3 + 3*2 = 16
k = 2: [ 2, 6, 4, 3 ] -> F(2) = 0*2 + 1*6 + 2*4 + 3*3 = 23
k = 3: [ 3, 2, 6, 4 ] -> F(3) = 0*3 + 1*2 + 2*6 + 3*4 = 26

Maximum F(k) = 26 (at k = 3)
```

### The $O(1)$ Recurrence Transition Formula
Computing each $F(k)$ independently by multiplying all $n$ terms takes $O(n)$ time per rotation, resulting in $O(n^2)$ total runtime.
Notice what happens algebraically when moving from $arr_{k-1}$ to $arr_k$:
- Every element shifts one position to the right, so its coefficient increases by $+1$.
- Sum of all elements is $S = \sum_{j=0}^{n-1} nums[j]$. Adding $+1$ to all coefficients adds $+S$ to the total sum.
- However, the tail element (which previously had coefficient $n - 1$) wraps around to index $0$ with coefficient $0$.
- Its net change is $-(n - 1) = +1 - n$.
- Therefore:
$$
F(k) = F(k - 1) + S - n \cdot nums[n - k]
$$

---

## 2. Conceptual Foundation & Invariants

### 1. The Algebraic Recurrence:
- Compute total sum:
  $$
  S = \sum_{j=0}^{n-1} nums[j]
  $$
- Compute initial base rotation $F(0)$:
  $$
  F(0) = \sum_{j=0}^{n-1} j \cdot nums[j]
  $$
- For each $k \in [1, n - 1]$:
  The element that wraps around from the back to the front is $nums[n - k]$.
  $$
  F(k) = F(k - 1) + S - n \cdot nums[n - k]
  $$
- Track the maximum:
  $$
  ans = \max_{0 \le k < n} F(k)
  $$

> **Invariant.** For every rotation step $k$, $F(k)$ is computed in $O(1)$ arithmetic operations from $F(k - 1)$, and $ans$ holds the maximum rotation value among $F(0 \dots k)$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [4, 3, 2, 6]$ ($n = 4$):

---

### Step 1: Initialize Base Parameters
- Compute total sum:
  $$
  S = 4 + 3 + 2 + 6 = \mathbf{15}
  $$
- Compute $F(0)$:
  $$
  F(0) = 0 \times 4 + 1 \times 3 + 2 \times 2 + 3 \times 6 = 0 + 3 + 4 + 18 = \mathbf{25}
  $$
- Initial maximum:
  $$
  ans = \mathbf{25}
  $$

---

### Step 2: Rotation $k = 1$
- Wrapped element: index $n - 1 = 4 - 1 = 3 \implies nums[3] = \mathbf{6}$.
- Apply recurrence:
  $$
  F(1) = F(0) + S - 4 \cdot nums[3]
  $$
  $$
  F(1) = 25 + 15 - 4 \times 6 = 40 - 24 = \mathbf{16}
  $$
- Update maximum:
  $$
  ans = \max(25, \; 16) = \mathbf{25}
  $$

---

### Step 3: Rotation $k = 2$
- Wrapped element: index $n - 2 = 4 - 2 = 2 \implies nums[2] = \mathbf{2}$.
- Apply recurrence:
  $$
  F(2) = F(1) + S - 4 \cdot nums[2]
  $$
  $$
  F(2) = 16 + 15 - 4 \times 2 = 31 - 8 = \mathbf{23}
  $$
- Update maximum:
  $$
  ans = \max(25, \; 23) = \mathbf{25}
  $$

---

### Step 4: Rotation $k = 3$
- Wrapped element: index $n - 3 = 4 - 3 = 1 \implies nums[1] = \mathbf{3}$.
- Apply recurrence:
  $$
  F(3) = F(2) + S - 4 \cdot nums[1]
  $$
  $$
  F(3) = 23 + 15 - 4 \times 3 = 38 - 12 = \mathbf{26}
  $$
- Update maximum:
  $$
  ans = \max(25, \; 26) = \mathbf{26}
  $$

---

### Step 5: Termination
All $n = 4$ rotations evaluated. Return:
$$
\mathbf{26}
$$

---

## 4. Complete Execution Trace

```text
nums = [4, 3, 2, 6], n = 4, S = 15

k=0: F(0) = 0*4 + 1*3 + 2*2 + 3*6 = 25 -> ans = 25
k=1: wrapped = nums[3] = 6 -> F(1) = 25 + 15 - 4*6 = 16 -> ans = 25
k=2: wrapped = nums[2] = 2 -> F(2) = 16 + 15 - 4*2 = 23 -> ans = 25
k=3: wrapped = nums[1] = 3 -> F(3) = 23 + 15 - 4*3 = 26 -> ans = 26

Final Output: 26
```

| Rotation $k$ | Rotated Array $arr_k$ | Wrapped Element $nums[n-k]$ | Recurrence Calculation $F(k-1) + S - n \cdot nums[n-k]$ | Value $F(k)$ | Global Max $ans$ |
|:---:|:---|:---:|:---|:---:|:---:|
| 0 | `[4, 3, 2, 6]` | - | Base calculation | 25 | 25 |
| 1 | `[6, 4, 3, 2]` | $nums[3] = 6$ | $25 + 15 - 4(6) = 40 - 24$ | 16 | 25 |
| 2 | `[2, 6, 4, 3]` | $nums[2] = 2$ | $16 + 15 - 4(2) = 31 - 8$ | 23 | 25 |
| **3** | **`[3, 2, 6, 4]`** | **$nums[1] = 3$** | **$23 + 15 - 4(3) = 38 - 12$** | **26** | **$\mathbf{26}$ (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Consider $F(k) - F(k-1)$:
$$
F(k) = 0 \cdot a_0 + 1 \cdot a_1 + \dots + (n - 1) \cdot a_{n-1}
$$
where $a$ is clockwise-rotated from $b$ (the array at step $k-1$). Thus $a_0 = b_{n-1}$, and $a_j = b_{j-1}$ for $j \ge 1$.
Substituting gives:
$$
F(k) = \sum_{j=1}^{n-1} j \cdot b_{j-1} = \sum_{m=0}^{n-2} (m + 1) \cdot b_m = \sum_{m=0}^{n-2} m \cdot b_m + \sum_{m=0}^{n-2} b_m
$$
Notice that $F(k-1) = \sum_{m=0}^{n-1} m \cdot b_m = \sum_{m=0}^{n-2} m \cdot b_m + (n - 1) b_{n-1}$.
Subtracting yields:
$$
F(k) - F(k-1) = \sum_{m=0}^{n-2} b_m - (n - 1) b_{n-1} = \sum_{m=0}^{n-1} b_m - n \cdot b_{n-1} = S - n \cdot nums[n - k]
$$
The recurrence is an exact algebraic identity.

**Completeness.** All $n$ rotations from $k = 0$ to $k = n - 1$ are systematically generated, ensuring no rotation is missed.

---

## 6. Traps This Instance Exposes

- **Brute Force $O(N^2)$ Recalculation:** Re-evaluating the dot product from scratch for each of the $n$ rotations takes $O(n^2)$ time, which TLEs for $n = 10^5$. The $O(1)$ recurrence reduces total time to $O(N)$.
- **Negative Array Elements:** Elements in $nums$ can be negative (e.g. $-100$). The maximum initial value $ans$ must be initialized to $F(0)$, NOT to $0$.
- **Indexing the Wrapped Element:** At step $i$ ($1 \le i < n$), the wrapped element is $nums[n - i]$, NOT $nums[i]$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = \text{len}(nums)$.
  - Calculating initial sum $S$ and $F(0)$ takes $O(N)$ time.
  - The loop runs $N - 1$ times, each taking $O(1)$ arithmetic time.
  - Overall time is strictly linear $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, storing only scalar variables $S$, $f$, and $ans$.