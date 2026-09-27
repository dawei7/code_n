# Guided Example: Longest Mountain in Array

We trace the step-by-step unimodal mountain subarray characterization, forward strictly increasing prefix length tracking ($f[i]$), backward strictly decreasing suffix length tracking ($g[i]$), peak vertex qualification ($f[i] > 1 \land g[i] > 1$), span combination ($f[i] + g[i] - 1$), and maximum mountain subarray length derivation on representative numeric arrays:

- **Input:**
  $$
  arr = [2, 1, 4, 7, 3, 2, 5]
  $$
- **Required output:** `5`
  - Mountain subarray criteria:
    - A subarray $arr[L \dots R]$ is defined as a **mountain** if and only if:
      1. Its length is at least 3 ($R - L + 1 \ge 3$).
      2. There exists a peak index $p \in (L, R)$ such that:
         - The subarray strictly increases from $L$ up to $p$:
           $$
           arr[L] < arr[L+1] < \dots < arr[p]
           $$
         - The subarray strictly decreases from $p$ down to $R$:
           $$
           arr[p] > arr[p+1] > \dots > arr[R]
           $$
    - Objective: Find the maximum length of any mountain subarray in $arr$ (return 0 if none exists).
    - For $arr = [2, 1, 4, 7, 3, 2, 5]$:
      - Subarray $[1, 4, 7, 3, 2]$ (from index 1 to 5):
        - Strictly increases: $1 < 4 < 7$ (length 3).
        - Peak at index 3 (value 7).
        - Strictly decreases: $7 > 3 > 2$ (length 3).
        - Total mountain elements: $5$ ($[1, 4, 7, 3, 2]$).
      - Maximum mountain length: **`5`**.
- **Bidirectional Dynamic Programming Invariant:**
  - **Uphill and Downhill Decomposition:**
    - Any mountain of length $L$ centered at peak $p$ is the union of:
      1. A strictly increasing sequence ending at $p$ (uphill slope of length $f[p]$).
      2. A strictly decreasing sequence starting at $p$ (downhill slope of length $g[p]$).
    - Because the peak $p$ is shared by both slopes, the total number of elements in the mountain is:
      $$
      \text{length}(p) = f[p] + g[p] - 1
      $$
  - **The Peak Validity Requirement:**
    - A valid peak **must have non-trivial slopes on both sides**:
      - It must have an ascending climb: $f[p] > 1$.
      - It must have a descending descent: $g[p] > 1$.
    - A monotonic sequence (purely increasing or purely decreasing) has $f[p] = 1$ or $g[p] = 1$ and cannot be a mountain.
  - **Two-Pass Recurrence:**
    - **Forward Pass ($i = 1 \dots n - 1$):**
      $$
      f[i] = \begin{cases} f[i - 1] + 1 & arr[i] > arr[i - 1] \\ 1 & arr[i] \le arr[i - 1] \end{cases}
      $$
    - **Backward Pass ($i = n - 2 \dots 0$):**
      $$
      g[i] = \begin{cases} g[i + 1] + 1 & arr[i] > arr[i + 1] \\ 1 & arr[i] \le arr[i + 1] \end{cases}
      $$
- **Step-by-Step Worked Execution Trace on $arr = [2, 1, 4, 7, 3, 2, 5]$ ($n = 7$):**
  - Initialize DP arrays: $f = [1, 1, 1, 1, 1, 1, 1], g = [1, 1, 1, 1, 1, 1, 1]$.
  - **Pass 1: Forward Increasing Runs ($f$):**
    - $i = 0$ ($val = 2$): base $f[0] = 1$.
    - $i = 1$ ($val = 1$): $1 \le 2 \implies f[1] = 1$.
    - $i = 2$ ($val = 4$): $4 > 1 \implies f[2] = f[1] + 1 = 1 + 1 = \mathbf{2}$.
    - $i = 3$ ($val = 7$): $7 > 4 \implies f[3] = f[2] + 1 = 2 + 1 = \mathbf{3}$.
    - $i = 4$ ($val = 3$): $3 \le 7 \implies f[4] = 1$.
    - $i = 5$ ($val = 2$): $2 \le 3 \implies f[5] = 1$.
    - $i = 6$ ($val = 5$): $5 > 2 \implies f[6] = f[5] + 1 = 1 + 1 = \mathbf{2}$.
    - Forward vector:
      $$
      f = [1, \; 1, \; 2, \; 3, \; 1, \; 1, \; 2]
      $$
  - **Pass 2: Backward Decreasing Runs ($g$) and Peak Testing:**
    - Initialize $ans = 0$.
    - $i = 6$ ($val = 5$): base $g[6] = 1$.
    - $i = 5$ ($val = 2$): $2 \le 5 \implies g[5] = 1$.
    - $i = 4$ ($val = 3$): $3 > 2 \implies g[4] = g[5] + 1 = 1 + 1 = \mathbf{2}$.
      - Peak test: $f[4] = 1 \implies$ no left climb (not a peak).
    - $i = 3$ ($val = 7$): $7 > 3 \implies g[3] = g[4] + 1 = 2 + 1 = \mathbf{3}$.
      - Peak test: $f[3] = 3 > 1$ and $g[3] = 3 > 1 \implies \mathbf{Valid\ Peak!}$
      - Combined mountain length:
        $$
        f[3] + g[3] - 1 = 3 + 3 - 1 = \mathbf{5}
        $$
      - Update: $ans \leftarrow \max(0, 5) = \mathbf{5}$.
    - $i = 2$ ($val = 4$): $4 \le 7 \implies g[2] = 1$.
    - $i = 1$ ($val = 1$): $1 \le 4 \implies g[1] = 1$.
    - $i = 0$ ($val = 2$): $2 > 1 \implies g[0] = g[1] + 1 = 1 + 1 = \mathbf{2}$.
      - $f[0] = 1 \implies$ not a peak.
  - **Global Maximum:**
    $$
    ans = \mathbf{5}
    $$
- **Flat Array Trace ($arr = [2, 2, 2]$):**
  - Strict inequalities $arr[i] > arr[i \pm 1]$ never hold.
  - All $f[i] = 1, g[i] = 1 \implies$ no peak $\implies ans = \mathbf{0}$.
- **Monotonic Ascending Array ($arr = [1, 2, 3, 4]$):**
  - $f = [1, 2, 3, 4]$, but all $g[i] = 1$ (no descent exists).
  - Condition $g[i] > 1$ fails for every element $\implies ans = \mathbf{0}$.
- **Plateau Peak ($arr = [1, 3, 3, 1]$):**
  - $arr[1] == arr[2] = 3$ violates strict inequality.
  - Cannot form a single sharp peak $\implies ans = \mathbf{0}$.

This instance demonstrates unimodal sequence decomposition and coordinate slope analysis on discrete real sequences, mathematically proves why factoring unimodal intervals into independent monotonic cones isolates peak candidates in linear time, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given integer array $arr$:
A mountain subarray has length $\ge 3$, strictly increases to a peak $p$, then strictly decreases.
Find the **longest mountain length**.

```text
arr = [ 2, 1, 4, 7, 3, 2, 5 ]

Mountain around peak 7 (index 3):
  Climb:   1 < 4 < 7  (length 3)
  Descent: 7 > 3 > 2  (length 3)
  Total length = 3 + 3 - 1 = 5

Subarray: [ 1, 4, 7, 3, 2 ]
Result: 5
```

### The Invariant of Peak Slope Integration
- $f[i]$: length of strictly increasing run ending at $i$.
- $g[i]$: length of strictly decreasing run starting at $i$.
- Peak condition: $f[i] > 1$ AND $g[i] > 1$.
- Total span: $f[i] + g[i] - 1$.

---

## 2. Conceptual Foundation & Invariants

### 1. Unimodal Mountain Specification:
$$
\text{Mountain}(L, p, R) \iff (L < p < R) \;\land\; (\forall i \in [L, p-1]: arr[i] < arr[i+1]) \;\land\; (\forall i \in [p, R-1]: arr[i] > arr[i+1])
$$

### 2. Bidirectional Recurrence:
$$
f[i] = (f[i - 1] + 1) \cdot \mathbb{I}[arr[i] > arr[i - 1]] + 1 \cdot \mathbb{I}[arr[i] \le arr[i - 1]]
$$
$$
g[i] = (g[i + 1] + 1) \cdot \mathbb{I}[arr[i] > arr[i + 1]] + 1 \cdot \mathbb{I}[arr[i] \le arr[i + 1]]
$$
$$
ans = \max_{i: f[i] > 1 \land g[i] > 1} (f[i] + g[i] - 1) \cup \{0\}
$$

> **Unimodality Decomposition Invariant.** A discrete sequence is unimodal if and only if its forward first difference sequence transitions from strictly positive to strictly negative at most once. The length of a maximal unimodal interval centered at local maximum $p$ equals the sum of the positive and negative variation run-lengths minus 1.

---

## 3. Step-by-Step Worked Execution

We trace $arr = [2, 1, 4, 7, 3, 2, 5]$:

---

### Step 1: Forward Pass ($f$)
- $f = [1, 1, 2, 3, 1, 1, 2]$.

---

### Step 2: Backward Pass ($g$)
- $g = [2, 1, 1, 3, 2, 1, 1]$.

---

### Step 3: Test Peaks
- Index 3 (value 7):
  - $f[3] = 3 > 1$ and $g[3] = 3 > 1$.
  - Length: $3 + 3 - 1 = \mathbf{5}$.

---

### Step 4: Output
$$
\mathbf{5}
$$

---

## 4. Complete Execution Trace

| Index $i$ | Value $arr[i]$ | Increasing Run $f[i]$ | Decreasing Run $g[i]$ | Valid Peak? ($f > 1 \land g > 1$) | Mountain Span $f + g - 1$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $2$ | $1$ | $2$ | No ($f = 1$) | — |
| $1$ | $1$ | $1$ | $1$ | No | — |
| $2$ | $4$ | $2$ | $1$ | No ($g = 1$) | — |
| **$3$** | **$7$** | **$3$** | **$3$** | **Yes** | **$3 + 3 - 1 = \mathbf{5}$** |
| $4$ | $3$ | $1$ | $2$ | No ($f = 1$) | — |
| $5$ | $2$ | $1$ | $1$ | No | — |
| **$6$** | **$5$** | **$2$** | **$1$** | **No ($g = 1$)** | — |
| **Max** | — | — | — | — | **`5`** |

---

## 5. Boundary Cases & Failure Modes

- **Purely Increasing Array ($[1, 2, 3]$):** No descent ($g[i] = 1$ everywhere) $\implies 0$.
- **Purely Decreasing Array ($[3, 2, 1]$):** No climb ($f[i] = 1$ everywhere) $\implies 0$.
- **Equal Consecutive Elements ($[1, 2, 2, 1]$):** Flat peak violates strict inequality $\implies 0$.
- **Small Array ($N < 3$):** Cannot form mountain of length $\ge 3 \implies 0$.

---

## 6. Traps & Common Anti-Patterns

- **Allowing Flat Tops ($arr[i] == arr[i+1]$):** Mountains require **strictly** increasing and **strictly** decreasing segments. Equal elements immediately reset the run length to 1.
- **Forgetting the Peak Qualification ($f[i] > 1 \land g[i] > 1$):** Summing $f[i] + g[i] - 1$ without checking both $> 1$ will falsely count monotonic endpoints as mountains.
- **Double-Counting the Peak:** The peak is included in both $f[i]$ and $g[i]$; remember to subtract 1 ($f[i] + g[i] - 1$).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Forward pass: $\mathcal{O}(N)$.
  - Backward pass: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 10^4$. Completes in $< 0.5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for the $f$ and $g$ run-length arrays.
