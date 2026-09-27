# Guided Example: Find Minimum in Rotated Sorted Array II

We trace the step-by-step ternary decision bisection and duplicate boundary shrinking ($R \leftarrow R - 1$) on representative rotated sorted arrays with duplicate elements:

- **Input:** $\text{nums} = [2, 2, 2, 0, 1]$
- **Required output:** $0$ (Inflection drop located at index $3$)
- **Duplicate Ambiguity Instance:** $\text{nums} = [3, 3, 1, 3] \implies 1$ (Where $\text{nums}[M] == \text{nums}[R]$ triggers safe boundary contraction)
- **All-Identical Plateau Instance:** $\text{nums} = [2, 2, 2, 2] \implies 2$

This instance demonstrates addressing binary search breakdown under duplicates ($\text{nums}[M] == \text{nums}[R]$), proves why decrementing the right pointer $R \leftarrow R - 1$ preserves the global minimum, and analyzes the complexity spectrum from $O(\log N)$ average time to $O(N)$ worst-case time.

---

## 1. Instance & Teaching Goal

Suppose a sorted array containing **duplicate elements** is rotated:
$$
\text{nums} = [2, 2, 2, \mathbf{0}, 1]
$$
Find the minimum element of the array.

In LeetCode 153 (all unique elements), comparing midpoint $\text{nums}[M]$ against right endpoint $\text{nums}[R]$ yields a strict dichotomy:
- $\text{nums}[M] > \text{nums}[R] \implies$ right half.
- $\text{nums}[M] < \text{nums}[R] \implies$ left half.

When duplicates exist, a third case arises:
$$
\text{nums}[M] == \text{nums}[R]
$$
Consider two opposing arrays where $M = 2$:
1. $[1, 0, 1, 1, 1]$: $\text{nums}[M] = 1, \text{nums}[R] = 1$. The minimum ($0$) is in the **left** half.
2. $[1, 1, 1, 0, 1]$: $\text{nums}[M] = 1, \text{nums}[R] = 1$. The minimum ($0$) is in the **right** half.
Because $\text{nums}[M] == \text{nums}[R]$, halving the search space is mathematically impossible without risking discarding the minimum.
The optimal strategy decrements $R \leftarrow R - 1$, safely chipping away redundant boundary duplicates until strict inequality is restored.

---

## 2. Conceptual Foundation & Invariants

### Ternary Bisection Protocol with Boundary Contraction
Maintain active interval $[L, R]$ with `while L < R`.
Compute midpoint:
$$
M = L + \left\lfloor \frac{R - L}{2} \right\rfloor
$$

1. **Strictly Greater ($\text{nums}[M] > \text{nums}[R]$):**
   The right half contains the inflection drop. The minimum lies strictly in $[M + 1, R]$:
   $$
   L \leftarrow M + 1
   $$
2. **Strictly Lesser ($\text{nums}[M] < \text{nums}[R]$):**
   The segment $[M \dots R]$ is sorted. The minimum lies in $[L \dots M]$:
   $$
   R \leftarrow M
   $$
3. **Equality Ambiguity ($\text{nums}[M] == \text{nums}[R]$):**
   Because the value at index $R$ is also present at index $M$, discarding index $R$ cannot permanently remove the minimum value from the candidate set:
   - If $\text{nums}[R]$ was not the minimum, discarding it is obviously safe.
   - If $\text{nums}[R]$ was the minimum, its duplicate at $M$ remains inside the interval $[L, R - 1]$.
   $$
   R \leftarrow R - 1
   $$

> **Invariant.** Throughout all pointer adjustments ($L \leftarrow M+1, R \leftarrow M, R \leftarrow R-1$), the minimum value in `nums` is guaranteed to exist at at least one index within the remaining interval $[L, R]$.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [3, 3, 1, 3]$ ($N = 4$):

### Initialization
- $L = 0, \quad R = 3$.
- Active interval: $[0, 3]$.

---

### Iteration 1: Ambiguity Resolution
- Midpoint:
  $$
  M = 0 + \left\lfloor \frac{3 - 0}{2} \right\rfloor = 1
  $$
- Evaluate values:
  - $\text{nums}[M] = \text{nums}[1] = 3$.
  - $\text{nums}[R] = \text{nums}[3] = 3$.
- Compare:
  $$
  \text{nums}[M] == \text{nums}[R] \quad (3 == 3)
  $$
- Ambiguity encountered! Safely decrement upper boundary:
  $$
  R \leftarrow R - 1 = 3 - 1 = \mathbf{2}
  $$
- New active interval: $[0, 2]$.

---

### Iteration 2: Definite Bisection
- Midpoint:
  $$
  M = 0 + \left\lfloor \frac{2 - 0}{2} \right\rfloor = 1
  $$
- Evaluate values:
  - $\text{nums}[M] = \text{nums}[1] = 3$.
  - $\text{nums}[R] = \text{nums}[2] = 1$.
- Compare:
  $$
  \text{nums}[M] > \text{nums}[R] \quad (3 > 1)
  $$
- Strict inequality restored! The drop lies strictly to the right:
  $$
  L \leftarrow M + 1 = 1 + 1 = \mathbf{2}
  $$
- New active interval: $[2, 2]$.

---

### Termination
- $L == R == 2$. Loop terminates.
- Extract minimum:
  $$
  \text{nums}[L] = \text{nums}[2] = \mathbf{1}
  $$

Minimum element is $\mathbf{1}$.

---

## 4. Complete Execution Trace

```text
Instance 1: nums = [3, 3, 1, 3]
Iter 1: [L=0, M=1, R=3] -> nums[1]=3 == nums[3]=3 -> Ambiguity! R = R - 1 = 2
Iter 2: [L=0, M=1, R=2] -> nums[1]=3  > nums[2]=1 -> L = M + 1 = 2
Result: [L=2, R=2]     -> Minimum is nums[2] = 1

Instance 2: nums = [2, 2, 2, 0, 1]
Iter 1: [L=0, M=2, R=4] -> nums[2]=2  > nums[4]=1 -> L = M + 1 = 3
Iter 2: [L=3, M=3, R=4] -> nums[3]=0  < nums[4]=1 -> R = M = 3
Result: [L=3, R=3]     -> Minimum is nums[3] = 0
```

| Iteration | Interval $[L, R]$ | Midpoint $M$ | $\text{nums}[M]$ | $\text{nums}[R]$ | Decision Case | Action Applied | New Bounds |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| 1 | $[0, 3]$ | 1 | 3 | 3 | $\text{nums}[M] == \text{nums}[R]$ | $R \leftarrow R - 1$ | $[0, 2]$ |
| **2** | **$[0, 2]$** | **1** | **3** | **1** | **$\text{nums}[M] > \text{nums}[R]$** | **$L \leftarrow M + 1$** | **$[2, 2]$** |
| **End** | **$[2, 2]$** | - | - | - | **$L == R$** | **Return $\text{nums}[2]$** | **1 (Result)** |

A second case places the unique minimum at the far right, $[3, 3, 3, 3, 1, 3]$, and shows how little work the ambiguity branch needs there: one contraction removes the duplicated right end, and strict comparisons take over immediately.

| Iteration | Interval $[L, R]$ | Midpoint $M$ | $\text{nums}[M]$ | $\text{nums}[R]$ | Decision Case | Action Applied | New Bounds |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| 1 | $[0, 5]$ | 2 | 3 | 3 | $\text{nums}[M] == \text{nums}[R]$ | $R \leftarrow R - 1$ | $[0, 4]$ |
| 2 | $[0, 4]$ | 2 | 3 | 1 | $\text{nums}[M] > \text{nums}[R]$ | $L \leftarrow M + 1$ | $[3, 4]$ |
| 3 | $[3, 4]$ | 3 | 3 | 1 | $\text{nums}[M] > \text{nums}[R]$ | $L \leftarrow M + 1$ | $[4, 4]$ |
| **End** | **$[4, 4]$** | - | - | - | **$L == R$** | **Return $\text{nums}[4]$** | **1 (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** When $\text{nums}[M] > \text{nums}[R]$, the minimum must be in $[M+1, R]$. When $\text{nums}[M] < \text{nums}[R]$, the minimum must be in $[L, M]$. When $\text{nums}[M] == \text{nums}[R]$, removing index $R$ retains index $M$ which holds the exact same value. In all three cases, at least one instance of the global minimum remains inside $[L, R]$.

**Completeness.** In every step, either $(R - L)$ is halved or $R$ decreases by $1$. The length $R - L$ is a strictly decreasing non-negative integer, guaranteeing convergence to $L == R$.

---

## 6. Traps This Instance Exposes

- **Attempting $O(\log N)$ Worst-Case Guarantee:** When all elements are identical except one (e.g. $[1, 1, 1, 0, 1, 1]$), binary search cannot eliminate half the array in one comparison. Any algorithm must examine $O(N)$ elements in the worst case to distinguish between $[1, 1, \dots, 0]$ and $[0, 1, \dots, 1]$.
- **Using $L = L + 1$ instead of $R = R - 1$:** When comparing against $\text{nums}[R]$, the duplicate value is confirmed between $M$ and $R$. Chipping away from the left ($L \leftarrow L + 1$) without verifying $\text{nums}[L] == \text{nums}[M]$ can inadvertently delete an inflection point!
- **Single Element Input:** If $N = 1$, $L == R == 0$ immediately terminates and returns $\text{nums}[0]$.

Counting which branch fires, and how often, is what separates the easy cases from the degenerate ones:

| Array | Answer | Branch that decides it | Why the instance matters |
|:---|:---:|:---|:---|
| $[1, 3, 5]$ | $1$ | Strict lesser at both iterations, so $R \leftarrow M$ | No duplicates exist, so the ambiguity branch never fires and the search halves cleanly |
| $[2, 2, 2, 0, 1]$ | $0$ | Strict greater at $M = 2$, then strict lesser at $M = 3$ | Duplicates surround the minimum, yet both comparisons stay strict because the right end holds a strictly smaller value each time |
| $[1, 1, 1, 1]$ | $1$ | Equality at every iteration, so $R \leftarrow R - 1$ | The degenerate plateau: no strict comparison is ever available, so one index is removed per iteration and the whole search is linear |
| $[3, 3, 3, 3, 1, 3]$ | $1$ | One equality, then strict greater twice | A single contraction strips the duplicated right end and hands the search back to strict bisection |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$ average time on general rotated arrays where bisection halves the search space. $O(N)$ worst-case time on degenerate inputs with massive duplicate plateaus (e.g. all elements identical except one), where $R \leftarrow R - 1$ runs $N$ times.

Splitting the iteration count into contractions and strict bisections makes that spectrum concrete on measured instances:

| Array | Contractions $R \leftarrow R - 1$ | Strict bisections | Total iterations | Answer |
|:---|:---:|:---:|:---:|:---:|
| $[1, 3, 5]$ | $0$ | $2$ | $2$ | $1$ |
| $[2, 2, 2, 0, 1]$ | $0$ | $2$ | $2$ | $0$ |
| $[1, 1, 1, 1, 0]$ | $0$ | $2$ | $2$ | $0$ |
| $[3, 3, 3, 3, 1, 3]$ | $1$ | $2$ | $3$ | $1$ |
| $[1, 1, 1, 0, 1, 1]$ | $2$ | $2$ | $4$ | $0$ |
| $[0, 1, 1, 1, 1]$ | $3$ | $1$ | $4$ | $0$ |
| $[1, 1, 1, 1]$ | $3$ | $0$ | $3$ | $1$ |

The first three arrays keep every comparison strict and finish in two steps regardless of where the minimum sits, because a strict comparison halves the interval. The last row is the degenerate case: with all values equal, every comparison is an equality, so exactly one index is discarded per iteration and the loop runs $N - 1$ times in total. The two rows above it show where the cost really comes from: $[0, 1, 1, 1, 1]$ pays three contractions because the right end keeps holding a value that also appears at the midpoint, while $[1, 1, 1, 1, 0]$ pays none because its unique minimum is itself the right end, so the comparison is strict every time.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, requiring only index variables $L, R, M$.
