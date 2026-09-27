# Guided Example: Maximum Product Subarray

We trace the step-by-step dual-state dynamic programming recurrence tracking running maximums and minimums on representative integer arrays:

- **Input:** $\text{nums} = [2, 3, -2, 4]$
- **Required output:** $6$ (Subarray $[2, 3]$ achieves product $6$)
- **Negative Sign-Flip Instance:** $\text{nums} = [-2, 3, -4] \implies 24$ (Subarray $[-2, 3, -4]$ where $(-6) \times (-4) = 24$)
- **Zero-Reset Instance:** $\text{nums} = [-2, 0, -1] \implies 0$

This instance demonstrates why Kadane's single-value tracking fails under multiplication, establishes the dual-register invariant ($\text{curr\_max}$ and $\text{curr\_min}$), analyzes the sign-swap transformation on negative numbers, and executes in $O(N)$ linear time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [2, 3, -2, 4]$, find a contiguous non-empty subarray that has the largest product, and return that product.

Evaluating all contiguous subarrays:
- $[2] \implies 2$
- $[2, 3] \implies 6$
- $[2, 3, -2] \implies -12$
- $[2, 3, -2, 4] \implies -48$
- $[3] \implies 3, \quad [3, -2] \implies -6, \quad [4] \implies 4$
The maximum product subarray is $[2, 3]$ with product $6$.

In Kadane's algorithm for Maximum Subarray Sum, a negative number strictly decreases the running sum, so the accumulator only tracks the maximum.
Under multiplication, signs invert:
- Multiplying a large positive number by a negative number produces a large **negative** number.
- Multiplying a large-magnitude negative number by a negative number produces a large **positive** number!
A seemingly disastrous negative product can flip into a record-breaking positive product upon encountering a second negative number. The optimal algorithm tracks **both** the minimum and maximum products ending at each index in $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### Dual-State Dynamic Programming Protocol
Let $\text{curr\_max}[i]$ be the maximum product of a subarray ending at index $i$.
Let $\text{curr\_min}[i]$ be the minimum product of a subarray ending at index $i$.

For each element $x = \text{nums}[i]$:
1. **Sign Inversion on Negative Input:**
   If $x < 0$, multiplying by $x$ reverses order: the prior minimum becomes a candidate for the new maximum, and the prior maximum becomes a candidate for the new minimum.
   $$
   \text{if } x < 0: \quad \text{swap}(\text{curr\_max}, \, \text{curr\_min})
   $$
2. **State Transitions:**
   Each state chooses between starting a fresh subarray at $x$ or extending the previous subarray:
   $$
   \text{curr\_max} \leftarrow \max(x, \, \text{curr\_max} \times x)
   $$
   $$
   \text{curr\_min} \leftarrow \min(x, \, \text{curr\_min} \times x)
   $$
3. **Global Maximum Update:**
   $$
   \text{global\_max} \leftarrow \max(\text{global\_max}, \, \text{curr\_max})
   $$

### Zero Element Invariant
If $x = 0$, both $\text{curr\_max}$ and $\text{curr\_min}$ become $0$. At the subsequent element, $\max(x_{i+1}, 0 \times x_{i+1}) = x_{i+1}$, naturally restarting the subarray search.

> **Invariant.** At every index $i$, $\text{curr\_max}$ stores the maximum product of any contiguous subarray ending at index $i$, and $\text{curr\_min}$ stores the minimum product of any contiguous subarray ending at index $i$.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [2, 3, -2, 4]$:

### Initialization (Index 0, $x = 2$)
- $\text{curr\_max} = 2$
- $\text{curr\_min} = 2$
- $\text{global\_max} = 2$

---

### Step 1: Index 1 ($x = 3$)
- $x = 3 \ge 0$ (no swap needed).
- Candidate transitions:
  - $\text{curr\_max} \times x = 2 \times 3 = 6$.
  - Start fresh: $x = 3$.
  - $\text{curr\_max} = \max(3, 6) = \mathbf{6}$.
- Minimum update:
  - $\text{curr\_min} \times x = 2 \times 3 = 6$.
  - Start fresh: $x = 3$.
  - $\text{curr\_min} = \min(3, 6) = \mathbf{3}$.
- Update global:
  $$
  \text{global\_max} = \max(2, 6) = \mathbf{6}
  $$

---

### Step 2: Index 2 ($x = -2$)
- $x = -2 < 0 \implies$ **Swap State Registers!**
  - $\text{curr\_max} \leftarrow 3, \quad \text{curr\_min} \leftarrow 6$.
- Compute transitions:
  - $\text{curr\_max} = \max(-2, \, 3 \times (-2)) = \max(-2, -6) = \mathbf{-2}$.
  - $\text{curr\_min} = \min(-2, \, 6 \times (-2)) = \min(-2, -12) = \mathbf{-12}$.
- Update global:
  $$
  \text{global\_max} = \max(6, -2) = \mathbf{6}
  $$
*(Notice: -12 is preserved in `curr_min` in case another negative number follows!)*

---

### Step 3: Index 3 ($x = 4$)
- $x = 4 \ge 0$ (no swap).
- Compute transitions:
  - $\text{curr\_max} = \max(4, \, -2 \times 4) = \max(4, -8) = \mathbf{4}$.
  - $\text{curr\_min} = \min(4, \, -12 \times 4) = \min(4, -48) = \mathbf{-48}$.
- Update global:
  $$
  \text{global\_max} = \max(6, 4) = \mathbf{6}
  $$

Iteration ends. Global maximum product is $\mathbf{6}$.

---

## 4. Complete Execution Trace

```text
Array:         [ 2,     3,     -2,      4 ]
curr_max:        2  ->  6  ->  -2  ->   4
curr_min:        2  ->  3  -> -12  -> -48
global_max:      2  ->  6  ->   6  ->   6  => RESULT = 6
```

| Index $i$ | Value $x$ | Swapped? | $\text{curr\_max}$ Calculation | $\text{curr\_min}$ Calculation | Updated $\text{curr\_max}$ | Updated $\text{curr\_min}$ | Cumulative $\text{global\_max}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 2 | - | Init | Init | 2 | 2 | 2 |
| 1 | 3 | No | $\max(3, 2 \times 3)$ | $\min(3, 2 \times 3)$ | **6** | 3 | **6** |
| 2 | -2 | **Yes (6 $\leftrightarrow$ 3)** | $\max(-2, 3 \times -2)$ | $\min(-2, 6 \times -2)$ | -2 | **-12** | 6 |
| 3 | 4 | No | $\max(4, -2 \times 4)$ | $\min(4, -12 \times 4)$ | 4 | -48 | **6 (Final)** |

### Contrast: Negative Sign Flip on $[-2, 3, -4]$
- $i=0$ ($x=-2$): $\text{max}=-2, \, \text{min}=-2$.
- $i=1$ ($x=3$): $\text{max}=3, \, \text{min}=-6$.
- $i=2$ ($x=-4$): Swap ($\text{max}=-6, \text{min}=3$).
  $\text{curr\_max} = \max(-4, -6 \times -4) = \mathbf{24}$!

---

## 5. Algorithmic Correctness

**Soundness.** Let $P$ be a non-empty subarray ending at index $i$. If $|P| = 1$, the product is $x_i$. If $|P| > 1$, the product is $P' \times x_i$, where $P'$ is a subarray ending at index $i-1$. If $x_i > 0$, maximizing $P' \times x_i$ requires maximizing $P'$, which is stored in $\text{curr\_max}[i-1]$. If $x_i < 0$, maximizing $P' \times x_i$ requires minimizing $P'$, which is stored in $\text{curr\_min}[i-1]$. By considering both possibilities and a fresh start at $x_i$, the true optimum ending at $i$ is guaranteed.

**Completeness.** Every contiguous subarray ends at some index $i \in [0, N-1]$. Since $\text{global\_max}$ tracks the maximum across all indices, no candidate subarray can be missed.

---

## 6. Traps This Instance Exposes

- **Failing to Track Minimums (Sign Inversion Trap):** Tracking only the maximum misses products where two negative numbers multiply to form a huge positive value (e.g. $[-2, 3, -4] \to 24$).
- **Swapping Overwrite Bug:** When calculating in code without a swap or temporary variable:
  `curr_max = max(x, curr_max * x)`
  `curr_min = min(x, curr_max * x)` $\implies$ `curr_min` erroneously uses the *newly updated* `curr_max`! Pre-swapping when $x < 0$ or using temporary variables avoids this bug.
- **All-Negative Arrays:** If $\text{nums} = [-2]$, the initial $\text{global\_max} = -2$ correctly returns $-2$ instead of 0.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. A single loop processes each element once, performing $O(1)$ scalar multiplications and comparisons.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, requiring only three scalar variables (`curr_max`, `curr_min`, `global_max`).