# Guided Example: H-Index II

We trace the step-by-step binary search bisection on an ascendingly sorted citations array, monotonic threshold matching ($\text{citations}[m] \ge N - m$), and $O(\log N)$ interval convergence on representative publication profiles:

- **Input:** $\text{citations} = [0, 1, 3, 5, 6]$ (Sorted in ascending order)
- **Required output:** $3$ (Papers at indices $2, 3, 4$ have citations $\ge 3$; total $N - 2 = 3$ qualifying papers)
- **High Citation Outlier:** $\text{citations} = [1, 2, 100] \implies 2$ ($2$ papers have $\ge 2$ citations; $100$ cannot increase $h$ past total paper count)
- **All Zero Citations:** $\text{citations} = [0, 0, 0] \implies 0$ (Zero papers have $\ge 1$ citations)
- **Single Paper Instance:** $\text{citations} = [0] \implies 0, \quad \text{citations} = [10] \implies 1$
- **Uniform Citations Instance:** $\text{citations} = [5, 5, 5, 5, 5] \implies 5$

This instance demonstrates binary search on pre-sorted arrays without comparison-sorting overhead, explains why the suffix length $N - m$ acts as the candidate $h$-index, formalizes the monotonic decision boundary where $\text{citations}[m]$ meets $N - m$, and achieves strictly $O(\log N)$ logarithmic runtime with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a sorted array of citations in ascending order:
$$
\text{citations} = [0, 1, 3, 5, 6] \quad (N = 5)
$$
Find the researcher's $h$-index in **$O(\log N)$ logarithmic time**.

### Suffix Cardinality as Candidate $h$
Because the array is sorted in ascending order:
At any index $m \in [0, N - 1]$, there are exactly $N - m$ papers located from index $m$ through $N - 1$.
Because values are non-decreasing, every paper in that suffix has citation count $\ge \text{citations}[m]$.
Therefore:
If $\text{citations}[m] \ge N - m$, then at least $N - m$ papers have at least $N - m$ citations!
- To **maximize** the $h$-index ($h = N - m$), we must find the **smallest index $m$** that satisfies:
  $$
  \text{citations}[m] \ge N - m
  $$
- As index $m$ increases from $0$ to $N - 1$:
  - $\text{citations}[m]$ is monotonically non-decreasing ($\nearrow$).
  - $N - m$ is strictly monotonically decreasing ($\searrow$).
The difference $\text{citations}[m] - (N - m)$ is strictly increasing, guaranteeing that binary search can locate the crossover point in $O(\log N)$ steps.

---

## 2. Conceptual Foundation & Invariants

### Binary Search Bisection Protocol
Initialize search interval over indices:
$$
L = 0, \quad R = N - 1
$$
While $L \le R$:
1. Compute midpoint:
   $$
   M = L + \lfloor (R - L) / 2 \rfloor
   $$
2. Evaluate candidate threshold $h_{\text{cand}} = N - M$:
   - **Case 1 ($\text{citations}[M] == N - M$):**
     Exact equilibrium! Exactly $N - M$ papers have $\ge N - M$ citations.
     $$
     \text{return } N - M
     $$
   - **Case 2 ($\text{citations}[M] < N - M$):**
     The citation count at $M$ is too low to support a threshold of $N - M$.
     We must seek higher citation counts (further right in the array):
     $$
     L \leftarrow M + 1
     $$
   - **Case 3 ($\text{citations}[M] > N - M$):**
     The citation count at $M$ is more than sufficient for $N - M$.
     A smaller index (further left) might yield an even larger $h$-index:
     $$
     R \leftarrow M - 1
     $$
3. When $L > R$, the first valid index is $L$. The maximum $h$-index is:
   $$
   \text{return } N - L
   $$

> **Invariant.** The optimal boundary index $m^*$ always lies within $[L, R + 1]$. For all $i < L$, $\text{citations}[i] < N - i$.

---

## 3. Step-by-Step Worked Execution

We trace the binary search on $\text{citations} = [0, 1, 3, 5, 6]$ ($N = 5$):
Initial interval: $L = 0, \quad R = 4$.

---

### Step 1: First Bisection ($L = 0, R = 4$)
- Midpoint:
  $$
  M = 0 + \lfloor (4 - 0) / 2 \rfloor = \mathbf{2}
  $$
- Paper citation count: $\text{citations}[2] = \mathbf{3}$.
- Suffix length (candidate $h$):
  $$
  N - M = 5 - 2 = \mathbf{3}
  $$
- Compare:
  $$
  \text{citations}[2] == N - M \iff 3 == 3 \quad (\mathbf{\text{Exact Match!}})
  $$
- The paper at index 2 has 3 citations, and exactly 3 papers exist from index 2 to 4 (papers cited 3, 5, 6).
- An exact equilibrium is reached.
- **Return $3$ immediately!**

---

### Verification across All Indices
| Index $m$ | Citation $\text{citations}[m]$ | Suffix Length $N - m$ | Condition $\text{citations}[m] \ge N - m$ | Resulting $h$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 5 | $0 \ge 5$ (False) | Infeasible |
| 1 | 1 | 4 | $1 \ge 4$ (False) | Infeasible |
| **2** | **3** | **3** | **$3 \ge 3$ (True)** | **3 (Optimal)** |
| 3 | 5 | 2 | $5 \ge 2$ (True) | 2 |
| 4 | 6 | 1 | $6 \ge 1$ (True) | 1 |

The smallest valid index is $m = 2$, yielding maximum $h$-index $N - 2 = \mathbf{3}$.

---

## 4. Complete Execution Trace

```text
citations = [0, 1, 3, 5, 6], N = 5
L = 0, R = 4

Iteration 1:
  M = 2
  citations[2] = 3
  N - M = 5 - 2 = 3
  citations[M] == N - M (3 == 3) -> Exact match found!
  Return 3
```

| Iteration | Search Range $[L, R]$ | Midpoint $M$ | $\text{citations}[M]$ | Suffix Count $N - M$ | Test Outcome | Next Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | $[0, 4]$ | 2 | 3 | 3 | $3 == 3$ (Equilibrium) | **Return $3$ (Terminates)** |

### Contrast: General Case Without Exact Match (`citations = [1, 2, 100]`, $N = 3$)
1. $L = 0, R = 2 \implies M = 1$.
   - $\text{citations}[1] = 2, \quad N - M = 3 - 1 = 2$.
   - $2 == 2 \implies$ Exact match, returns $2$.
2. Single-element zero array: `citations = [0]`, $N = 1$:
   - $L = 0, R = 0 \implies M = 0$.
   - $\text{citations}[0] = 0, \quad N - M = 1$.
   - $0 < 1 \implies L = 0 + 1 = 1$.
   - Loop ends with $L = 1$. Return $N - L = 1 - 1 = \mathbf{0}$.

---

## 5. Algorithmic Correctness

**Soundness.** If $\text{citations}[m] \ge N - m$, then because `citations` is non-decreasing, all elements $\text{citations}[i]$ for $i \ge m$ satisfy $\text{citations}[i] \ge \text{citations}[m] \ge N - m$. Thus, there are at least $N - m$ papers with at least $N - m$ citations, meaning $N - m$ is a valid $h$-index.

**Completeness.** If $\text{citations}[m] < N - m$, then for all $i \le m$, $\text{citations}[i] \le \text{citations}[m] < N - m < N - i$. Thus, no index $i \le m$ can support an $h$-index of $N - i$. Discarding the left half $[L, M]$ safely eliminates only provably invalid configurations. When the bisection terminates, $L$ is the minimal valid index, ensuring $N - L$ is maximal.

---

## 6. Traps This Instance Exposes

- **Linear Scan Regression ($O(N)$):** Scanning the array from left to right takes $O(N)$ time. The problem explicitly requires $O(\log N)$ logarithmic time, which necessitates binary search bisection.
- **Midpoint Suffix Calculation ($N - M$ vs $M$):** Because the array is sorted ascending, the qualifying papers are to the **right** of index $M$ (the suffix of length $N - M$), unlike descending arrays where qualifying papers are the prefix of length $M + 1$.
- **Termination Value ($N - L$):** When no exact equality is found, the binary search terminates with $L$ pointing to the first index where $\text{citations}[L] \ge N - L$. The answer is $N - L$, which naturally yields $0$ if all citations are $0$ ($L = N$).

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$, where $N$ is the number of papers in `citations`. The search range $[L, R]$ of size $N$ is halved in every iteration. The loop executes at most $\lceil \log_2 N \rceil + 1$ times, taking $O(1)$ operations per iteration.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory. Only scalar index pointers ($L, R, M$) are maintained.