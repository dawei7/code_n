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
If $x = 0$, both $\text{curr\_max}$ and $\text{curr\_min}$ become $0$, because every subarray product that ends at this index is $0$. The extension term carried into the next index is then $0 \times x_{i+1} = 0$ for both registers, so the search restarts there:
$$
\text{curr\_max} = \max(x_{i+1}, \, 0), \qquad \text{curr\_min} = \min(x_{i+1}, \, 0)
$$
A positive successor therefore restores $\text{curr\_max} = x_{i+1}$ itself, while a negative successor leaves $\text{curr\_max} = 0$ and parks the negative value in $\text{curr\_min}$ instead. The restart is a genuine fresh start in both directions: no product formed across the zero can ever exceed $0$.

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

### Contrast: Zero Resets and Two Separated Blocks on $[0, -3, 1, -2, -4, 0, 5, -1, 2]$

This instance holds two zeros and two blocks of negatives, and its required answer is $8$. Each row shows the extension term that survives the swap, the fresh start at $x$, and the registers that result:

| Index $i$ | $x$ | Swapped? | Extension into $\text{curr\_max}$ | Extension into $\text{curr\_min}$ | $\text{curr\_max}$ | $\text{curr\_min}$ | $\text{global\_max}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | - | Init | Init | 0 | 0 | 0 |
| 1 | -3 | **Yes (0 $\leftrightarrow$ 0)** | $0 \times -3 = 0$ | $0 \times -3 = 0$ | 0 | **-3** | 0 |
| 2 | 1 | No | $0 \times 1 = 0$ | $-3 \times 1 = -3$ | **1** | -3 | **1** |
| 3 | -2 | **Yes (-3 $\leftrightarrow$ 1)** | $-3 \times -2 = 6$ | $1 \times -2 = -2$ | **6** | -2 | **6** |
| 4 | -4 | **Yes (-2 $\leftrightarrow$ 6)** | $-2 \times -4 = 8$ | $6 \times -4 = -24$ | **8** | **-24** | **8** |
| 5 | 0 | No | $8 \times 0 = 0$ | $-24 \times 0 = 0$ | 0 | 0 | 8 |
| 6 | 5 | No | $0 \times 5 = 0$ | $0 \times 5 = 0$ | **5** | 0 | 8 |
| 7 | -1 | **Yes (0 $\leftrightarrow$ 5)** | $0 \times -1 = 0$ | $5 \times -1 = -5$ | 0 | **-5** | 8 |
| 8 | 2 | No | $0 \times 2 = 0$ | $-5 \times 2 = -10$ | **2** | -10 | **8 (Final)** |

Two rows carry the lesson. At index 1 the fresh start $-3$ loses to the extension $0$, because the zero at index 0 is a legitimate single-element subarray with product $0$; the negative value is preserved in $\text{curr\_min}$ instead. At index 4 the register that was minimised one step earlier becomes the one that maximises, and $8$ comes from a subarray that excludes the earlier $-3$: pairing $-3$ with $-2$ and $-4$ would give $-24$, which is precisely the value parked in $\text{curr\_min}$.

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

Each case in the package stresses a different part of the dual-register argument, and naming a subarray that attains the answer shows what the registers must be able to represent:

| Array | Required answer | A subarray attaining it | What the instance proves |
|:---|:---:|:---|:---|
| $[2, 3, -2, 4]$ | $6$ | $[2, 3]$ | Extending beats every subarray that includes the $-2$, so the maximum can come from a strict prefix |
| $[-2, 0, -1]$ | $0$ | $[0]$ | The answer is the zero itself: a run of negatives cannot recover, and returning the largest negative instead would be wrong |
| $[-2, 3, -4]$ | $24$ | $[-2, 3, -4]$ | The whole array is optimal only because the two negatives cancel, which is exactly the case a maximum-only tracker misses |
| $[0, -3, 1, -2, -4, 0, 5, -1, 2]$ | $8$ | $[1, -2, -4]$ or $[-2, -4]$ | Two separated blocks and two zeros: the best block is bounded by zeros on both sides, so the registers must reset |
| $[2]$ | $2$ | $[2]$ | A non-empty subarray is required, so the single-element initialisation is itself the answer |
| $[2, 2]$ | $4$ | $[2, 2]$ | Positive duplicates make extension strictly better than a fresh start, so the maximum is not simply the largest element |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. A single loop processes each element once, performing $O(1)$ scalar multiplications and comparisons.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, requiring only three scalar variables (`curr_max`, `curr_min`, `global_max`).
