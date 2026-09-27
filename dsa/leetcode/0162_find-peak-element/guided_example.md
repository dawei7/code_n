# Guided Example: Find Peak Element

We trace the step-by-step local slope evaluation ($\text{nums}[M]$ vs $\text{nums}[M+1]$) and logarithmic peak convergence on representative integer arrays:

- **Input:** $\text{nums} = [1, 2, 3, 1]$
- **Required output:** $2$ (Index 2 holds peak element $3$, where $3 > 2$ and $3 > 1$)
- **Multiple Peaks Instance:** $\text{nums} = [1, 2, 1, 3, 5, 6, 4] \implies 1 \text{ or } 5$ (Either index 1 or index 5 is valid)
- **Monotonically Increasing Instance:** $\text{nums} = [1, 2, 3] \implies 2$ (Because $\text{nums}[3] = -\infty$, the last element is a peak)

This instance demonstrates binary search on an unsorted array, proves why an uphill slope guarantees a peak to the right while a downhill slope guarantees a peak at or to the left of $M$, and achieves guaranteed $O(\log N)$ logarithmic runtime in $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given an array of integers $\text{nums} = [1, 2, \mathbf{3}, 1]$ with virtual negative infinity boundaries:
$$
\text{nums}[-1] = -\infty, \quad \text{nums}[4] = -\infty
$$
Find any index $i$ such that $\text{nums}[i] > \text{nums}[i-1]$ and $\text{nums}[i] > \text{nums}[i+1]$ in $O(\log N)$ time.
Adjacent elements are strictly distinct ($\text{nums}[i] \ne \text{nums}[i+1]$).

At index 2, $\text{nums}[2] = 3$:
- $\text{nums}[1] = 2 < 3$
- $\text{nums}[3] = 1 < 3$
Thus, index 2 is a peak. Output: $2$.

A linear scan checks each element in $O(N)$ time.
Even though the array is **unsorted**, binary search is applicable!
Because virtual boundaries are $-\infty$, any local upward slope must eventually crest and fall before the boundary.
By comparing midpoint $\text{nums}[M]$ with its adjacent neighbor $\text{nums}[M + 1]$, we determine whether we are ascending or descending a slope, halving the candidate search space in $O(1)$ comparisons.

---

## 2. Conceptual Foundation & Invariants

### The Slope Bisection Theorem
For any active index interval $[L, R]$ with $L < R$:
Let $M = L + \lfloor (R - L) / 2 \rfloor$.
Since $L < R$, $M < R$, ensuring $M + 1$ is always a valid array index.

1. **Ascending Slope ($\text{nums}[M] < \text{nums}[M + 1]$):**
   The value increases from $M$ to $M + 1$. Since the sequence must eventually drop down to $-\infty$ at or before index $N$, a peak is **guaranteed to exist in the right half**:
   $$
   L \leftarrow M + 1
   $$
2. **Descending Slope ($\text{nums}[M] > \text{nums}[M + 1]$):**
   The value decreases from $M$ to $M + 1$. Since the sequence starts from $-\infty$ at index $-1$ and reaches $\text{nums}[M]$, a peak is **guaranteed to exist at $M$ or in the left half**:
   $$
   R \leftarrow M
   $$
   *(We set $R = M$ because $M$ itself might be the peak!)*

### Convergence Invariant
Each step reduces the interval size $(R - L)$. When $L == R$, the single remaining element is guaranteed to be a peak.

> **Invariant.** The closed search interval $[L, R]$ always contains at least one local peak element.

---

## 3. Step-by-Step Worked Execution

We trace the binary search on $\text{nums} = [1, 2, 3, 1]$ ($N = 4$):

### Initialization
- $L = 0, \quad R = 3$.
- Active interval: $[0, 3]$.

---

### Iteration 1: Interval $[0, 3]$
- Compute midpoint:
  $$
  M = 0 + \left\lfloor \frac{3 - 0}{2} \right\rfloor = 1
  $$
- Compare adjacent elements:
  - $\text{nums}[M] = \text{nums}[1] = 2$.
  - $\text{nums}[M + 1] = \text{nums}[2] = 3$.
  - Check slope:
    $$
    \text{nums}[M] < \text{nums}[M + 1] \quad (2 < 3)
    $$
- **Uphill Slope Detected!** A peak is guaranteed to the right of $M$.
- Advance lower bound:
  $$
  L \leftarrow M + 1 = 1 + 1 = \mathbf{2}
  $$
- New active interval: $[2, 3]$.

---

### Iteration 2: Interval $[2, 3]$
- Compute midpoint:
  $$
  M = 2 + \left\lfloor \frac{3 - 2}{2} \right\rfloor = 2
  $$
- Compare adjacent elements:
  - $\text{nums}[M] = \text{nums}[2] = 3$.
  - $\text{nums}[M + 1] = \text{nums}[3] = 1$.
  - Check slope:
    $$
    \text{nums}[M] > \text{nums}[M + 1] \quad (3 > 1)
    $$
- **Downhill Slope Detected!** A peak exists at $M$ or to the left.
- Narrow upper bound:
  $$
  R \leftarrow M = \mathbf{2}
  $$
- New active interval: $[2, 2]$.

---

### Termination
- $L == R == 2$.
- Loop terminates.
- Converged index: $\mathbf{2}$.
- Verified peak: $\text{nums}[2] = 3$ is greater than neighbor $2$ and neighbor $1$.

Return index $\mathbf{2}$.

---

## 4. Complete Execution Trace

```text
Array:         [ 1,   2,   3,   1 ]
Indices:         0    1    2    3
Virtual:   -inf                  -inf

Iter 1:        [ L    M         R ]  nums[1]=2 < nums[2]=3 -> Uphill -> L = M+1 = 2
Iter 2:                  [ L=M  R ]  nums[2]=3 > nums[3]=1 -> Downhill -> R = M = 2
Converged:               [ L=R=2 ]   Peak index = 2 (value = 3)
```

| Iteration | Search Interval $[L, R]$ | Midpoint $M$ | $\text{nums}[M]$ | $\text{nums}[M + 1]$ | Slope Condition | Bound Update | New Interval |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $[0, 3]$ | 1 | 2 | 3 | $2 < 3$ (Uphill) | $L \leftarrow M + 1$ | $[2, 3]$ |
| **2** | **$[2, 3]$** | **2** | **3** | **1** | **$3 > 1$ (Downhill)** | **$R \leftarrow M$** | **$[2, 2]$** |
| **End** | **$[2, 2]$** | - | - | - | **$L == R$** | **Return index $L$** | **2 (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** Consider any subsegment $[L, R]$ where $\text{nums}[L-1] < \text{nums}[L]$ and $\text{nums}[R] > \text{nums}[R+1]$. (This property holds initially for $[0, N-1]$ due to the virtual boundaries $-\infty$). If $\text{nums}[M] < \text{nums}[M+1]$, the subsegment $[M+1, R]$ inherits the boundary conditions ($\text{nums}[M] < \text{nums}[M+1]$ and $\text{nums}[R] > \text{nums}[R+1]$). If $\text{nums}[M] > \text{nums}[M+1]$, the subsegment $[L, M]$ inherits the boundary conditions ($\text{nums}[L-1] < \text{nums}[L]$ and $\text{nums}[M] > \text{nums}[M+1]$). By induction, the invariant is preserved until $|L, R| = 1$, where the single element is provably a peak.

**Completeness.** Since $L < R$, $M = \lfloor (L+R)/2 \rfloor < R$. Setting $R = M$ strictly decreases $R$, and setting $L = M + 1$ strictly increases $L$. The algorithm terminates in at most $\lceil \log_2 N \rceil$ steps.

---

## 6. Traps This Instance Exposes

- **Checking Both Neighbors ($M - 1$ and $M + 1$):** Checking both neighbors requires handling boundary out-of-bounds when $M = 0$. By comparing only $\text{nums}[M]$ with $\text{nums}[M + 1]$, boundary checking is eliminated entirely because $M < R \le N - 1$ guarantees $M + 1 < N$.
- **Setting $R = M - 1$:** If $\text{nums}[M] > \text{nums}[M + 1]$, $M$ itself could be the peak (as shown in Step 2 above where $\text{nums}[2] = 3$). Setting $R = M - 1$ would skip the peak! Setting $R = M$ is essential.
- **Single-Element Array:** If $N = 1$, $L = 0, R = 0$. The loop `while L < R` immediately terminates and returns index 0, which is valid since $-\infty < \text{nums}[0] > -\infty$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$, where $N$ is the length of `nums`. Each comparison halves the remaining interval.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, utilizing only index variables $L, R, M$.