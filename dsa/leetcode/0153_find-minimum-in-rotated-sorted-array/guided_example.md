# Guided Example: Find Minimum in Rotated Sorted Array

We trace the step-by-step inflection point bisection comparing midpoint against right endpoint on representative rotated sorted array instances:

- **Input:** $\text{nums} = [3, 4, 5, 1, 2]$
- **Required output:** $1$ (Minimum element located at rotation inflection index $3$)
- **Unrotated Array Instance:** $\text{nums} = [11, 13, 15, 17] \implies 11$
- **Larger Rotation Instance:** $\text{nums} = [4, 5, 6, 7, 0, 1, 2] \implies 0$

This instance demonstrates comparing the midpoint $\text{nums}[M]$ against the right boundary $\text{nums}[R]$ to determine which half contains the rotation inflection drop, explains why $R = M$ preserves the candidate while $L = M + 1$ safely discards $M$, and guarantees logarithmic $O(\log N)$ runtime.

---

## 1. Instance & Teaching Goal

Suppose an array of length $n = 5$ originally sorted in ascending order is rotated:
$$
\text{nums} = [3, 4, 5, \mathbf{1}, 2]
$$
Find the minimum element in $O(\log N)$ time. All elements are unique.

In this instance:
- The array consists of two monotonically increasing segments: $[3, 4, 5]$ and $[1, 2]$.
- The transition between $5$ and $1$ represents the inflection drop ($5 > 1$).
- The minimum element of the entire array is the head of the second segment: $1$.

Linear scanning takes $O(N)$ time.
In a rotated array, binary search cannot simply compare $\text{nums}[M]$ against a fixed target.
Instead, comparing $\text{nums}[M]$ against the right boundary $\text{nums}[R]$ reveals with certainty whether the inflection point lies to the left or right of $M$, halving the search space on every iteration.

---

## 2. Conceptual Foundation & Invariants

### The Right-Endpoint Comparison Invariant
Because all elements are unique:

1. **Case A: $\text{nums}[M] > \text{nums}[R]$**
   If the midpoint value is strictly greater than the rightmost value, the interval $[M \dots R]$ contains a drop. The inflection point (and thus the minimum element) **must lie strictly to the right of $M$**.
   Since $\text{nums}[M]$ is greater than $\text{nums}[R]$, $M$ cannot be the minimum:
   $$
   L \leftarrow M + 1
   $$
2. **Case B: $\text{nums}[M] < \text{nums}[R]$**
   If the midpoint value is strictly less than the rightmost value, the segment $[M \dots R]$ is strictly increasing and contains no drop.
   The minimum element could be $\text{nums}[M]$ itself, or it lies strictly to the left of $M$. It **cannot lie strictly to the right of $M$**:
   $$
   R \leftarrow M
   $$
   *(We set $R = M$ rather than $M - 1$ because $M$ itself could be the global minimum)*.

### Convergence Guarantee
Using `while L < R`:
Each iteration strictly decreases $(R - L)$. When $L == R$, the search space narrows to a single element, which is mathematically guaranteed to be the minimum.

> **Invariant.** Throughout the execution, the unique global minimum element is always contained within the closed index interval $[L, R]$.

---

## 3. Step-by-Step Worked Execution

We trace the binary search on $\text{nums} = [3, 4, 5, 1, 2]$:
Array length $N = 5$.

### Initialization
- $L = 0, \quad R = 4$.
- Active interval: $[0, 4]$.

---

### Iteration 1: Interval $[0, 4]$
- Compute midpoint:
  $$
  M = L + \left\lfloor \frac{R - L}{2} \right\rfloor = 0 + \left\lfloor \frac{4 - 0}{2} \right\rfloor = 2
  $$
- Evaluate values:
  - $\text{nums}[M] = \text{nums}[2] = 5$.
  - $\text{nums}[R] = \text{nums}[4] = 2$.
- Compare $\text{nums}[M]$ vs $\text{nums}[R]$:
  $$
  5 > 2
  $$
- Since $5 > 2$, the inflection drop lies strictly in the right half. Node $M(5)$ cannot be the minimum.
- Update lower bound:
  $$
  L \leftarrow M + 1 = 2 + 1 = \mathbf{3}
  $$
- New active interval: $[3, 4]$.

---

### Iteration 2: Interval $[3, 4]$
- Compute midpoint:
  $$
  M = 3 + \left\lfloor \frac{4 - 3}{2} \right\rfloor = 3 + 0 = 3
  $$
- Evaluate values:
  - $\text{nums}[M] = \text{nums}[3] = 1$.
  - $\text{nums}[R] = \text{nums}[4] = 2$.
- Compare $\text{nums}[M]$ vs $\text{nums}[R]$:
  $$
  1 < 2
  $$
- Since $1 < 2$, segment $[3 \dots 4]$ is sorted. The minimum cannot be to the right of $M$, but could be $M$ itself.
- Update upper bound:
  $$
  R \leftarrow M = \mathbf{3}
  $$
- New active interval: $[3, 3]$.

---

### Termination
- Bounds meet: $L == R == 3$.
- Search loop terminates.
- Extract value:
  $$
  \text{nums}[L] = \text{nums}[3] = \mathbf{1}
  $$

Minimum element is $\mathbf{1}$.

---

## 4. Complete Execution Trace

```text
Array:         [ 3,   4,   5,   1,   2 ]
Indices:         0    1    2    3    4
Iter 1:         [L        M          R]   nums[M]=5 > nums[R]=2 -> L = M+1 = 3
Iter 2:                        [L    R]   nums[M]=1 < nums[R]=2 -> R = M = 3
                                M
Converged:                     [L=R=3]    Value = 1
```

| Iteration | Active Interval $[L, R]$ | Midpoint $M$ | Midpoint Value $\text{nums}[M]$ | Right Value $\text{nums}[R]$ | Decision Condition | Bound Update Applied | New Interval |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $[0, 4]$ | 2 | 5 | 2 | $5 > 2 \implies \text{drop in right}$ | $L \leftarrow M + 1$ | $[3, 4]$ |
| **2** | **$[3, 4]$** | **3** | **1** | **2** | **$1 < 2 \implies \text{sorted right}$** | **$R \leftarrow M$** | **$[3, 3]$** |
| **End** | **$[3, 3]$** | - | - | - | **$L == R$ (Converged)** | **Return $\text{nums}[3]$** | **1 (Result)** |

Every case in the package exercises a different amount of rotation, and the midpoint sequence makes the cost of each one visible:

| Array | Minimum index | Midpoint sequence $M$ | Iterations | Answer | What the instance proves |
|:---|:---:|:---:|:---:|:---:|:---|
| $[3, 4, 5, 1, 2]$ | $3$ | $2 \to 3$ | $2$ | $1$ | The traced instance: the second comparison keeps $M$ as the answer with $R \leftarrow M$ |
| $[4, 5, 6, 7, 0, 1, 2]$ | $4$ | $3 \to 5 \to 4$ | $3$ | $0$ | A deeper rotation first throws the midpoint right past the drop, then walks left twice to recover it |
| $[11, 13, 15, 17]$ | $0$ | $1 \to 0$ | $2$ | $11$ | No drop exists, so the $L \leftarrow M + 1$ branch is never taken and the interval walks left to index $0$ |
| $[2, 1]$ | $1$ | $0$ | $1$ | $1$ | The smallest possible rotation: one comparison suffices, and $\text{nums}[M]$ cannot be returned blindly because $\text{nums}[0] > \text{nums}[1]$ |
| $[8, 9, 10, 11, 12, 3, 4, 5, 6, 7]$ | $5$ | $4 \to 7 \to 6 \to 5$ | $4$ | $3$ | With $N = 10$ the loop needs four iterations, matching $\lceil \log_2 10 \rceil = 4$, and the last three steps all shrink $R$ by one |

---

## 5. Algorithmic Correctness

**Soundness.** In any circularly rotated array of distinct elements, the sequence consists of either one sorted segment (no rotation) or two sorted segments separated by a single drop where $\text{nums}[k] > \text{nums}[k+1]$. When $\text{nums}[M] > \text{nums}[R]$, the drop must reside within $[M+1, R]$. When $\text{nums}[M] < \text{nums}[R]$, the right portion contains no drop, so the minimum is at $M$ or left of $M$. Neither update ever discards the true minimum.

**Completeness.** At each step, the search interval size $|R - L + 1|$ strictly decreases. For $R > L$, $M < R$, so $R \leftarrow M$ strictly reduces $R$, and $L \leftarrow M + 1$ strictly increases $L$. Termination in $\lceil \log_2 N \rceil$ steps is mathematically guaranteed.

---

## 6. Traps This Instance Exposes

- **Comparing with Left Instead of Right:** Comparing $\text{nums}[M]$ against $\text{nums}[L]$ fails when the array is already unrotated (e.g. $[1, 2, 3]$). In that case, $\text{nums}[M] > \text{nums}[L]$, which would incorrectly suggest moving right even though the minimum is at index 0! Comparing with $\text{nums}[R]$ works uniformly for both rotated and unrotated arrays.
- **Using $R = M - 1$ instead of $R = M$:** If $\text{nums}[M] < \text{nums}[R]$, $M$ itself could be the minimum (as in Step 2 above where $\text{nums}[3] = 1$). Setting $R = M - 1$ would discard the minimum!
- **Using `while L <= R`:** Because $R = M$ does not eliminate $M$, using `L <= R` without a separate return branch causes an infinite loop when $L == R$. Using `while L < R` terminates cleanly.

The choice of comparison is the whole algorithm, so the candidates are worth running against the same two arrays, one unrotated and one rotated:

| Comparison that drives the decision | Test applied | Result on the unrotated $[11, 13, 15, 17]$ | Result on the rotated $[3, 4, 5, 1, 2]$ | Verdict |
|:---|:---|:---|:---|:---|
| $\text{nums}[M]$ against $\text{nums}[R]$, the current interval end | $L \leftarrow M + 1$ exactly when $\text{nums}[M] > \text{nums}[R]$ | Midpoints $1 \to 0$, returns $11$ | Midpoints $2 \to 3$, returns $1$ | Selected: the test reads the interval's own boundary, so it stays meaningful however far the interval has already shrunk |
| $\text{nums}[M]$ against $\text{nums}[L]$, the current interval start | $L \leftarrow M + 1$ exactly when $\text{nums}[M] > \text{nums}[L]$ | Midpoints $1 \to 2$, returns $15$: wrong, because index $0$ held the minimum and was discarded | Midpoints $2 \to 3$, returns $1$, but only by accident since the interval happens to collapse onto the minimum | Rejected: in an ascending array every midpoint exceeds the left bound, so the search always walks right |
| $\text{nums}[M]$ against the array's fixed last element $\text{nums}[N-1]$ | $L \leftarrow M + 1$ exactly when $\text{nums}[M] > \text{nums}[N-1]$ | Returns $11$ | Returns $1$ | An equivalent variant that agrees with the traced rule on every case in this package; it compares against a fixed element rather than the moving interval end |
| Linear scan of all elements | Compare every value and keep the smallest | Returns $11$ | Returns $1$ | Correct but $O(N)$ time, which the required bound forbids |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$, where $N$ is the number of elements in `nums`. Each step halves the remaining candidate interval. Maximum iterations $\le \lceil \log_2 N \rceil$.
- **Auxiliary Space Complexity:** $O(1)$ constant extra space, utilizing only index variables $L, R, M$.
