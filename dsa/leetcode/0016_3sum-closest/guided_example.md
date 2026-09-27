# Guided Example: 3Sum Closest

We trace the step-by-step execution of the sorted two-pointer search on a representative array instance:

- **Input:** $\text{nums} = [-1, 2, 1, -4]$, $\text{target} = 1$
- **Required output:** $2$

This instance demonstrates sorting-induced monotonicity, two-pointer distance minimization, directional pointer adjustment based on the target error sign, and early-exit elimination of suboptimal search branches.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums}$ of length $N = 4$ and a target value $\text{target} = 1$, we must choose three distinct indices $(i, j, k)$ such that their sum $S = \text{nums}[i] + \text{nums}[j] + \text{nums}[k]$ minimizes the absolute difference $|S - \text{target}|$.

For $\text{nums} = [-1, 2, 1, -4]$:
- Triplet $(-4, -1, 2)$ gives sum $-3$, distance $|-3 - 1| = 4$.
- Triplet $(-4, 1, 2)$ gives sum $-1$, distance $|-1 - 1| = 2$.
- Triplet $(-1, 1, 2)$ gives sum $2$, distance $|2 - 1| = 1$.

The optimal sum is $2$, achieving the minimal distance $1$ to target $1$.

A naive brute-force search enumerates all $\binom{N}{3} = O(N^3)$ triplets. By sorting the array first, we fix one element and reduce the remaining two-element search to an $O(N)$ monotonic two-pointer scan, bringing the total time down to $O(N^2)$.

---

## 2. Conceptual Foundation & Invariants

### Sorting and Monotonicity
We first sort $\text{nums}$ in non-decreasing order:
$$
\text{nums} = [-4, -1, 1, 2]
$$

For each fixed anchor index $i$ ($0 \le i \le N - 3$), we position two pointers over the remaining right subsegment:
- Left pointer $j = i + 1$ (starts at smallest available element).
- Right pointer $k = N - 1$ (starts at largest available element).

At each step, we evaluate the triplet sum:
$$
S = \text{nums}[i] + \text{nums}[j] + \text{nums}[k]
$$

### Pointer Adjustment Rules
1. If $|S - \text{target}| < |\text{closest} - \text{target}|$, update $\text{closest} \leftarrow S$.
2. **Error Sign Direction:**
   - If $S < \text{target}$: To bring the sum closer to $\text{target}$, we need a larger value. Because the array is sorted, any pair $(j, k')$ with $k' < k$ would produce a sum $\le S < \text{target}$, which is strictly further from $\text{target}$. Hence, index $j$ cannot form any better triplet with remaining candidates; we advance $j \leftarrow j + 1$.
   - If $S > \text{target}$: To reduce the sum toward $\text{target}$, we need a smaller value. By symmetry, pair $(j', k)$ with $j' > j$ produces a sum $\ge S > \text{target}$; we decrement $k \leftarrow k - 1$.
   - If $S = \text{target}$: The distance is $0$, the theoretical minimum. We return $S$ immediately.

> **Invariant.** At every stage, $\text{closest}$ stores the best triplet sum among all evaluated configurations. Monotonicity ensures no discarded $(j, k)$ pair could have produced a strictly smaller distance $|S - \text{target}|$.

---

## 3. Step-by-Step Worked Execution

We initialize $\text{closest} = \infty$. Sorted array: $\text{nums} = [-4, -1, 1, 2]$.

### Outer Iteration $i = 0$ (Anchor $\text{nums}[0] = -4$)
Pointers initialize at $j = 1$ ($\text{nums}[1] = -1$) and $k = 3$ ($\text{nums}[3] = 2$).

- **Step 1 ($j=1, k=3$):**
  - Triplet: $(-4, -1, 2)$.
  - Sum: $S = -4 + (-1) + 2 = -3$.
  - Distance: $|-3 - 1| = 4$.
  - Comparison: $4 < \infty \implies \text{closest} \leftarrow -3$.
  - Direction check: $S = -3 < \text{target} = 1$. Advance left pointer: $j \leftarrow 2$.

- **Step 2 ($j=2, k=3$):**
  - Triplet: $(-4, 1, 2)$.
  - Sum: $S = -4 + 1 + 2 = -1$.
  - Distance: $|-1 - 1| = 2$.
  - Comparison: $2 < 4 \implies \text{closest} \leftarrow -1$.
  - Direction check: $S = -1 < \text{target} = 1$. Advance left pointer: $j \leftarrow 3$.
  - Pointers meet ($j = k = 3$). Inner loop for $i = 0$ terminates.

---

### Outer Iteration $i = 1$ (Anchor $\text{nums}[1] = -1$)
Pointers initialize at $j = 2$ ($\text{nums}[2] = 1$) and $k = 3$ ($\text{nums}[3] = 2$).

- **Step 3 ($j=2, k=3$):**
  - Triplet: $(-1, 1, 2)$.
  - Sum: $S = -1 + 1 + 2 = 2$.
  - Distance: $|2 - 1| = 1$.
  - Comparison: $1 < 2 \implies \text{closest} \leftarrow 2$.
  - Direction check: $S = 2 > \text{target} = 1$. Decrement right pointer: $k \leftarrow 2$.
  - Pointers meet ($j = k = 2$). Inner loop for $i = 1$ terminates.

### Outer Loop Termination
The anchor index reaches $N - 2$. All candidate triplets have been explored or pruned.
Final answer: $2$.

---

## 4. Complete Execution Trace

| Iteration | Anchor $i$ ($\text{nums}[i]$) | Left $j$ ($\text{nums}[j]$) | Right $k$ ($\text{nums}[k]$) | Triplet Sum $S$ | Absolute Error $\|S - \text{target}\|$ | Best Sum So Far | Direction Shift | Elimination Rationale |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 ($-4$) | 1 ($-1$) | 3 ($2$) | $-3$ | $|-3 - 1| = 4$ | $-3$ | $j \leftarrow 2$ | $S < 1$; pairing $-1$ with smaller right elements yields even smaller sums |
| 2 | 0 ($-4$) | 2 ($1$) | 3 ($2$) | $-1$ | $|-1 - 1| = 2$ | $-1$ | $j \leftarrow 3$ | $S < 1$; advance left pointer |
| 3 | 1 ($-1$) | 2 ($1$) | 3 ($2$) | $2$ | $|2 - 1| = 1$ | **$2$** | $k \leftarrow 2$ | $S > 1$; pairing $2$ with larger left elements yields even larger sums |

---

## 5. Algorithmic Correctness

**Soundness.** Every evaluated sum $S$ is formed by three distinct indices $i < j < k$. The output is always a real, reachable triplet sum from the input array.

**Completeness.** By fixing every possible anchor $i$ from $0$ to $N - 3$ and systematically shrinking $[j, k]$, the two-pointer invariant guarantees that no pair $(j, k)$ capable of achieving a smaller distance to $\text{target}$ than the current best is ever pruned. If an exact sum $S = \text{target}$ exists, the distance reaches $0$ and triggers an immediate return.

---

## 6. Traps This Instance Exposes

- **Duplicate Skipping Optimization:** If consecutive elements are identical (e.g. $\text{nums}[i] = \text{nums}[i-1]$), skipping the duplicate anchor avoids redundant searches without compromising completeness.
- **Initial Accumulator Value:** Initializing $\text{closest}$ with $0$ is an error because $0$ might falsely masquerade as a candidate sum. Initializing with $\text{nums}[0] + \text{nums}[1] + \text{nums}[2]$ or $\infty$ guarantees correctness.
- **Integer Overflow with Sentinel:** When using $\infty$, one must take care in languages with fixed integer widths not to trigger overflow when computing $|S - \text{target}|$. In Python, arbitrary-precision integers handle this natively.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Sorting the array of length $N$ takes $O(N \log N)$ time. The outer loop runs $N - 2$ times, and each inner two-pointer traversal takes at most $N$ steps, contributing $O(N^2)$ time. The overall runtime is dominated by $O(N^2)$.
- **Auxiliary Space Complexity:** $O(1)$ beyond sorting. In-place sorting algorithms require $O(1)$ or $O(\log N)$ stack space, and the two-pointer search uses only scalar pointer variables.
