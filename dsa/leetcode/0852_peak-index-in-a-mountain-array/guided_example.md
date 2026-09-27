# Guided Example: Peak Index in a Mountain Array

We trace the step-by-step binary search on first-order difference signs ($arr[mid] > arr[mid + 1]$), discrete slope orientation testing, search interval halving over $[1, n - 2]$, convergence to the unique unimodal maximum, and $O(\log N)$ runtime guarantees on representative mountain arrays:

- **Input:**
  $$
  arr = [0, 2, 1, 0]
  $$
- **Required output:** `1`
  - Mountain array specifications:
    - An array of length $n \ge 3$ is guaranteed to be a mountain:
      - Strictly increasing up to some unknown peak index $p \in [1, n - 2]$:
        $$
        arr[0] < arr[1] < \dots < arr[p]
        $$
      - Strictly decreasing from $p$ to the end:
        $$
        arr[p] > arr[p+1] > \dots > arr[n - 1]
        $$
    - Objective: Find the peak index $p$ in strictly $\mathcal{O}(\log N)$ time.
    - For $arr = [0, 2, 1, 0]$ ($n = 4$):
      - $arr[0] = 0 < arr[1] = 2$ (ascending climb).
      - $arr[1] = 2 > arr[2] = 1 > arr[3] = 0$ (descending descent).
      - The peak occurs at index **`1`** (with peak value 2).
- **Monotonic Derivative & Binary Search Invariant:**
  - **The Slope Sign Change:**
    - Consider the adjacent difference at index $k$:
      $$
      \Delta(k) = arr[k + 1] - arr[k]
      $$
    - Before the peak ($k < p$):
      $$
      arr[k] < arr[k + 1] \iff \Delta(k) > 0 \quad (\text{Ascending})
      $$
    - At and after the peak ($k \ge p$):
      $$
      arr[k] > arr[k + 1] \iff \Delta(k) < 0 \quad (\text{Descending})
      $$
    - The sequence of booleans $\mathbb{I}[arr[k] > arr[k + 1]]$ transitions from `False` to `True` **exactly once**, at the peak index $p$!
  - **Binary Search Elimination Rule:**
    - Inspect midpoint $mid$:
      - **Case 1 ($arr[mid] > arr[mid + 1]$):**
        - The slope is decreasing at $mid$.
        - Therefore, the peak $p$ is either at $mid$ itself or somewhere to its left.
        - Contract search space:
          $$
          right \leftarrow mid
          $$
      - **Case 2 ($arr[mid] < arr[mid + 1]$):**
        - The slope is increasing at $mid$.
        - Therefore, the peak $p$ lies strictly to the right of $mid$.
        - Contract search space:
          $$
          left \leftarrow mid + 1
          $$
  - Because $left$ and $right$ are initialized to $[1, n - 2]$, boundary conditions $0$ and $n - 1$ are safely avoided, ensuring $mid + 1$ is always a valid index.
- **Step-by-Step Worked Execution Trace on $arr = [0, 2, 1, 0]$ ($n = 4$):**
  - Initial search interval:
    $$
    left = 1, \quad right = n - 2 = 2
    $$
  - **Iteration 1:**
    - Current interval: $[left, right] = [1, 2]$.
    - Compute midpoint:
      $$
      mid = \left\lfloor \frac{1 + 2}{2} \right\rfloor = \mathbf{1}
      $$
    - Compare $arr[mid]$ with neighbor $arr[mid + 1]$:
      $$
      arr[1] = 2, \quad arr[2] = 1
      $$
      $$
      arr[1] > arr[2] \iff 2 > 1 \implies \mathbf{Descending\ Slope!}
      $$
    - The peak cannot be to the right of index 1.
    - Contract right boundary:
      $$
      right \leftarrow mid = \mathbf{1}
      $$
  - **Termination:**
    - Check loop condition:
      $$
      left < right \iff 1 < 1 \implies \mathbf{False}
      $$
    - Search interval collapsed to a single index:
      $$
      left == right == \mathbf{1}
      $$
    - Final Peak Index:
      $$
      ans = \mathbf{1}
      $$
- **Step-by-Step Worked Execution Trace on $arr = [0, 10, 5, 2]$ ($n = 4$):**
  - $left = 1, right = 2$.
  - $mid = 1$: $arr[1] = 10, arr[2] = 5 \implies 10 > 5 \implies right \leftarrow 1$.
  - Terminates with $ans = \mathbf{1}$.
- **Right-Leaning Mountain Trace ($arr = [0, 1, 2, 3, 2, 0], n = 6$):**
  - $left = 1, right = 4$.
  - $mid = 2$: $arr[2] = 2 < arr[3] = 3 \implies left \leftarrow 3$.
  - $mid = 3$: $arr[3] = 3 > arr[4] = 2 \implies right \leftarrow 3$.
  - Converges to $left = 3$ (value 3) in 2 steps.

This instance demonstrates unimodal optimization on 1D integer lattices via Fibonacci/bisection search, mathematically proves why strictly sign-definite first difference sequences define a monotone decision boundary, and derives $O(\log N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a mountain array $arr$:
Find the peak index $p$ in **$O(\log N)$ time**.

```text
arr = [ 0, 2, 1, 0 ]

Indices:
  Index 0: 0
  Index 1: 2 (PEAK!)
  Index 2: 1
  Index 3: 0

Slope at mid = 1:
  arr[1] = 2 > arr[2] = 1 -> descending!
  Peak must be at or left of 1 -> right = 1.
  Converges to index 1.

Result: 1
```

### The Invariant of the Slope Comparison
- Compare $arr[mid]$ with $arr[mid + 1]$:
  - If $arr[mid] > arr[mid + 1]$: we are on the descending slope; peak is at or left of $mid$ ($right = mid$).
  - If $arr[mid] < arr[mid + 1]$: we are on the ascending slope; peak is strictly right ($left = mid + 1$).
- Search space halves at every step.

---

## 2. Conceptual Foundation & Invariants

### 1. Monotone First Difference:
$$
\text{IsDescending}(k) \iff arr[k] > arr[k + 1]
$$
$$
k < p \implies \text{IsDescending}(k) = \text{False}, \quad k \ge p \implies \text{IsDescending}(k) = \text{True}
$$

### 2. Search Interval Invariant:
$$
p \in [left, right] \quad \text{at all times}
$$

> **Bisection of Unimodal Extrema.** A function $f: \{0, \dots, n-1\} \to \mathbb{R}$ is strictly unimodal if its discrete derivative $\Delta f(x) = f(x+1) - f(x)$ has a unique zero-crossing. Binary search on the boolean predicate $\Delta f(x) < 0$ locates the transition point in $\lfloor \log_2 n \rfloor$ comparisons.

---

## 3. Step-by-Step Worked Execution

We trace $arr = [0, 2, 1, 0]$:

---

### Step 1: Initial Bounds
- $left = 1, right = 2$.

---

### Step 2: Midpoint 1
- $mid = 1$.
- $arr[1] = 2, arr[2] = 1$.
- $2 > 1 \implies$ descending slope!
- $right \leftarrow 1$.

---

### Step 3: Termination
- $left == right == 1$.

---

### Step 4: Output
$$
\mathbf{1}
$$

---

## 4. Complete Execution Trace

| Iteration | Search Interval $[left, right]$ | Midpoint $mid$ | Pair Compared $(arr[mid], arr[mid+1])$ | Relation | Updated Boundary |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $[1, 2]$ | $1$ | $(2, 1)$ | $2 > 1$ (Descending) | $right \leftarrow 1$ |
| **Complete** | **$[1, 1]$** | — | — | **$left == right$** | **`Return 1`** |

---

## 5. Boundary Cases & Failure Modes

- **Minimal Mountain ($n = 3, [0, 1, 0]$):** $left = 1, right = 1 \implies$ loop terminates instantly $\implies ans = 1$.
- **Large Array ($N = 10^5$):** Converges in at most $\lceil \log_2 10^5 \rceil = 17$ iterations.
- **Peak at Far Left ($p = 1$):** Handled with $left$ starting at 1.
- **Peak at Far Right ($p = n - 2$):** Handled with $right$ ending at $n - 2$.

---

## 6. Traps & Common Anti-Patterns

- **Linear Scan ($O(N)$):** Scanning left-to-right until $arr[i] > arr[i+1]$ runs in $O(N)$ time and violates the explicit $O(\log N)$ requirement of the problem.
- **Including Endpoints ($left = 0, right = n - 1$):** At $mid = n - 1$, $mid + 1$ causes index-out-of-bounds. Since the peak cannot be at 0 or $n - 1$, bound search to $[1, n - 2]$.
- **Setting $right = mid - 1$ on Downhill:** If $arr[mid] > arr[mid + 1]$, $mid$ could be the actual peak! Setting $right = mid - 1$ would skip the peak. Use $right = mid$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Search range starts at $N - 2$ and is halved every iteration.
  - Total comparisons: $\lfloor \log_2 N \rfloor$.
  - Total Time: strictly logarithmic $\mathcal{O}(\log N)$ where $N \le 10^5 \implies \le 17$ steps. Completes in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
