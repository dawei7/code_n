# Guided Example: Smallest Good Base

We trace the step-by-step geometric series polynomial representation ($n = \sum_{i=0}^m k^i$), inverse monotonicity between degree $m$ and base $k$, maximum degree bound ($m \le \lfloor\log_2(n)\rfloor$), binary search for base $k$ at fixed degree, and guaranteed fallback to $n - 1$ on representative integers:

- **Input:** $n = \text{"13"}$
- **Required output:** `"3"`
  - Numeric value: $n = 13$
  - Definition: Base $k \ge 2$ is a good base if $n$ in base $k$ consists entirely of `1`s:
    $$
    n = 1 + k + k^2 + \dots + k^m
    $$
  - Inverse relationship:
    To minimize the base $k$, we must **maximize the polynomial length $m$** (since $k^m \approx n$).
  - Maximum degree bound:
    Since $k \ge 2$, $2^m \le n \implies m \le \lfloor\log_2(13)\rfloor = 3$.
- **Degree search trace ($m$ from $3$ down to $2$):**
  - **Test $m = 3$ (Four 1s: $1 + k + k^2 + k^3 = 13$):**
    - Smallest base $k = 2$: $1 + 2 + 4 + 8 = 15 > 13$
    - Since $15 > 13$, no integer base $k \ge 2$ can satisfy $m = 3$.
  - **Test $m = 2$ (Three 1s: $1 + k + k^2 = 13$):**
    - Quadratic equation: $k^2 + k - 12 = 0 \implies (k - 3)(k + 4) = 0$
    - Binary search on $k \in [2, 12]$:
      - At $k = 3$:
        $$
        1 + 3 + 3^2 = 1 + 3 + 9 = \mathbf{13} == n
        $$
    - Exact match found!
    - In base 3: $13_{10} = 111_3$.
    - Since $m = 2$ is the maximal degree yielding a valid integer base, $k = \mathbf{3}$ is unconditionally the **smallest good base**.
- **Five-Digit Instance ($n = \text{"4681"}$):**
  - $m = 4$:
    $$
    1 + k + k^2 + k^3 + k^4 = 4681 \implies k = 8 \quad (1 + 8 + 64 + 512 + 4096 = 4681)
    $$
    In base 8: $4681 = 11111_8 \implies \mathbf{\text{"8"}}$
- **Fallback Instance ($n = 10^{18}$):**
  - No integer base fits degrees $m \ge 2 \implies$ Falls back to $m = 1$, where $n = 1 + k \implies k = \mathbf{n - 1}$ (in base $n-1$, $n = 11_{n-1}$).

This instance demonstrates geometric polynomial inversion and monotonic search spaces, mathematically proves why maximizing degree $m$ minimizes base $k$, and derives $O(\log^2 n)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n$ represented as a string:
A base $k \ge 2$ is called a **good base** of $n$ if the representation of $n$ in base $k$ consists entirely of `'1'`s.
Return the **smallest good base** of $n$.

```text
The Geometric Series Equation:
  If n consists of (m + 1) ones in base k:
    n = 1 + k + k^2 + k^3 + ... + k^m

For n = 13:
  m = 1 (two 1s):   1 + k = 13          -> k = 12  (Base 12: "11")
  m = 2 (three 1s): 1 + k + k^2 = 13    -> k = 3   (Base 3:  "111")
  m = 3 (four 1s):  1 + k + k^2 + k^3 = 13 -> No integer solution (k=2 gives 15 > 13)

Smallest base k is 3!
```

### The Inversion Duality ($k$ vs $m$)
- Notice the fundamental inverse relationship:
  $$
  n \approx k^m \implies k \approx n^{1/m}
  $$
- Larger degree $m$ forces the base $k$ to be smaller!
- Therefore, to find the **smallest base $k$**, we simply search for the **largest possible degree $m$** that admits an exact integer solution for $k$.

---

## 2. Conceptual Foundation & Invariants

### 1. Bounding the Degree $m$:
Since the smallest possible base is $k = 2$:
$$
2^m \le n \implies m \le \lfloor\log_2(n)\rfloor
$$
For $n \le 10^{18}$, $\log_2(10^{18}) \approx 59.8$.
Thus, $m$ is strictly bounded by $60$. There are only about 60 possible degrees to test!

### 2. Monotonic Binary Search for Fixed $m$:
For a fixed degree $m \in [2, 60]$, the polynomial function:
$$
f(k) = 1 + k + k^2 + \dots + k^m
$$
is strictly monotonically increasing with respect to $k \ge 2$.
- Because $f(k)$ is strictly monotonic, we can use binary search to test whether an integer $k$ exists such that $f(k) == n$.
- Search range for $k$:
  $$
  l = 2, \quad r = \lfloor n^{1/m} \rfloor \le n - 1
  $$
- If $f(mid) \ge n$, search left half: $r \leftarrow mid$.
- Otherwise, search right half: $l \leftarrow mid + 1$.
- After convergence, check if $f(l) == n$.

### 3. Early Termination Guarantee:
By iterating $m$ in **descending order** (from $60$ down to $2$):
The **first** degree $m$ that yields an exact integer match $f(k) == n$ is guaranteed to have the largest $m$, and consequently the **globally smallest base $k$**!

> **Degree-Base Invariant.** For any $m_1 > m_2 \ge 1$, if $n = \sum_{i=0}^{m_1} k_1^i = \sum_{i=0}^{m_2} k_2^i$, then $k_1 < k_2$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 13$:

---

### Step 1: Determine Degree Search Range
$$
m_{max} = \lfloor\log_2(13)\rfloor = 3
$$
We test degrees $m \in [3, 2]$ in descending order.

---

### Step 2: Test Degree $m = 3$ ($1 + k + k^2 + k^3 = 13$)
- Binary search range for $k$: $[2, 12]$.
- At $k = 2$:
  $$
  1 + 2 + 4 + 8 = 15 > 13
  $$
- Since $f(2) = 15 > 13$, and $f(k)$ is strictly increasing, no integer $k \ge 2$ can satisfy the equation for $m = 3$.

---

### Step 3: Test Degree $m = 2$ ($1 + k + k^2 = 13$)
- Binary search range for $k$: $[2, 12]$.
  - Try $mid = 7$:
    $$
    1 + 7 + 49 = 57 > 13 \implies r \leftarrow 7
    $$
  - Try $mid = 4$:
    $$
    1 + 4 + 16 = 21 > 13 \implies r \leftarrow 4
    $$
  - Try $mid = 3$:
    $$
    1 + 3 + 9 = 13 == 13 \implies r \leftarrow 3
    $$
  - Search converges to $l = 3$.
- Validation:
  $$
  cal(3, 2) = 1 + 3 + 9 = \mathbf{13} == n
  $$
- Exact match found at $k = 3$!

---

### Step 4: Halt and Return
Because $m = 2$ is the maximum successful degree, $k = 3$ is the global minimum.
Return **`"3"`**.

---

## 4. Complete Execution Trace

| Tested Degree $m$ | Ones Count ($m + 1$) | Polynomial Equation | Binary Search on Base $k$ | Calculated Value $f(k)$ | Target $n$ | Valid? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **$3$** | $4$ ones | $1 + k + k^2 + k^3$ | $k = 2$ | $15$ | $13$ | Exceeds $13$ (No base) |
| **$2$** | $3$ ones | $1 + k + k^2$ | $k = 3$ | **$13$** | $13$ | **Match Found: $k = 3$** |
| **Conclusion** | — | — | — | — | — | **Return `"3"`** |

---

## 5. Boundary Cases & Failure Modes

- **Prime Numbers ($n = 13$):** May have good bases (e.g. $k = 3$).
- **No Non-Trivial Base ($n = 2$):** $m = 1 \implies k = 2 - 1 = \mathbf{1}$ (invalid since $k \ge 2$). In fact, for $n = 3$, $m = 1 \implies k = 2$ ($3 = 11_2$).
- **Large Prime Numbers ($n = 31$):** $1 + 2 + 4 + 8 + 16 = 31 \implies k = 2$ ($m = 4$).
- **Fallback Base ($n - 1$):** If no degree $m \ge 2$ yields an exact integer match, $m = 1$ always works: $n = 1 + k \implies k = n - 1$. The representation is always `"11"` in base $n - 1$.

---

## 6. Traps & Common Anti-Patterns

- **Searching Base $k$ Upwards From 2:** Directly scanning $k = 2, 3, \dots, 10^{18}$ takes $O(n)$ time, which will run for millions of years on $n = 10^{18}$. Searching over the tiny degree space $m \in [2, 60]$ takes microsecond time.
- **64-Bit Integer Overflow During Polynomial Evaluation:** Computing $k^m$ can exceed $2^{63} - 1$ when $k$ is large. In Python, integers have arbitrary precision, avoiding overflow; in C++, guarding multiplication with `if (p > (n - s) / k) break` prevents overflow exceptions.
- **Not Testing in Descending Order of $m$:** Iterating $m$ from 2 upwards finds the *largest* base first (e.g. $k = 12$ for $n = 13$) instead of the *smallest* base ($k = 3$). Descending order from 60 down to 2 guarantees immediate return of the global minimum base.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The degree loop runs at most $\log_2(n) \le 60$ iterations.
  - In each iteration, binary search over $k \in [2, n]$ takes $\log_2(n) \le 60$ steps.
  - Evaluating polynomial of degree $m$ takes $m \le 60$ operations.
  - Total Time: $\mathcal{O}(\log^3 n)$. For $n = 10^{18}$, $(60)^3 \approx 2 \times 10^5$ operations, completing in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ space using scalar numeric registers.