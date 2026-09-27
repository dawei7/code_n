# Guided Example: Find the Derangement of an Array

We trace the step-by-step fixed-point avoidance combinatorial definition ($\forall i: \pi(i) \ne i$), cycle decomposition case analysis (2-cycle mutual transposition vs general permutation cycle), classical subfactorial recurrence ($D(n) = (n - 1) \cdot (D(n-1) + D(n-2))$), base case boundary anchoring ($D(1) = 0, D(2) = 1$), and modulo $10^9 + 7$ dynamic programming on representative array lengths:

- **Input:** $n = 3$
- **Required output:** `2`
  - Combinatorial definition:
    - A **derangement** (denoted $!n$ or $D(n)$) is a permutation $\pi$ of the set $\{1, 2, \dots, n\}$ such that **no element appears in its original index**:
      $$
      \forall i \in \{1, \dots, n\}: \quad \pi(i) \ne i
      $$
  - For $n = 3$, all $3! = 6$ permutations are:
    - `[1, 2, 3]`: 3 fixed points $\implies$ Invalid
    - `[1, 3, 2]`: 1 fixed point ($\pi(1) = 1$) $\implies$ Invalid
    - `[2, 1, 3]`: 1 fixed point ($\pi(3) = 3$) $\implies$ Invalid
    - `[3, 2, 1]`: 1 fixed point ($\pi(2) = 2$) $\implies$ Invalid
    - `[2, 3, 1]`: $0$ fixed points ($\pi(1)=2, \pi(2)=3, \pi(3)=1$) $\implies \mathbf{Valid!}$
    - `[3, 1, 2]`: $0$ fixed points ($\pi(1)=3, \pi(2)=1, \pi(3)=2$) $\implies \mathbf{Valid!}$
  - Exactly **$2$** valid derangements exist.
- **The Classical Derangement Recurrence Proof:**
  - Consider where the last element $n$ can be mapped.
  - Since $\pi(n) \ne n$, element $n$ can be placed in any of the remaining **$n - 1$ slots** $\{1, 2, \dots, n - 1\}$.
  - Suppose element $n$ is placed at position $k$ (where $k \in \{1, \dots, n-1\}$). There are $n - 1$ choices for $k$.
  - Now, examine the destination of element $k$ ($\pi(k)$):
    - **Case 1 (Mutual 2-Cycle Swap): $\pi(k) = n$**
      - Elements $n$ and $k$ swap positions: $\pi(n) = k$ and $\pi(k) = n$.
      - Neither element is in its original position.
      - The remaining $n - 2$ elements must form a valid derangement among themselves.
      - Number of ways:
        $$
        D(n - 2)
        $$
    - **Case 2 (General Cycle Extension): $\pi(k) \ne n$**
      - Element $k$ does **not** go to position $n$.
      - Here, element $k$ is forbidden from going to position $n$ (just as it was originally forbidden from going to position $k$).
      - This maps identically to a derangement problem on the $n - 1$ elements $\{1, \dots, n-1\}$ where each has exactly one forbidden destination.
      - Number of ways:
        $$
        D(n - 1)
        $$
  - **Combining Both Disjoint Cases:**
    - Since there are $n - 1$ choices for position $k$:
      $$
      D(n) = (n - 1) \cdot \left( D(n - 1) + D(n - 2) \right)
      $$
- **Step-by-Step Worked Execution Trace ($n = 3$):**
  - **Base Cases:**
    - $D(0) = 1$ (The empty set has 1 derangement vacuously).
    - $D(1) = 0$ (A single element has nowhere to move without staying at index 1).
    - Array initialization: $f = [1, 0, 0, 0]$ (indices $0 \dots 3$).
  - **Compute $i = 2$:**
    - Recurrence formula:
      $$
      D(2) = (2 - 1) \cdot (D(1) + D(0)) = 1 \cdot (0 + 1) = \mathbf{1}
      $$
    - Derangement: `[2, 1]`.
    - $f[2] = 1$.
  - **Compute $i = 3$:**
    - Recurrence formula:
      $$
      D(3) = (3 - 1) \cdot (D(2) + D(1))
      $$
    - Substitute $D(2) = 1$ and $D(1) = 0$:
      $$
      D(3) = 2 \cdot (1 + 0) = 2 \cdot 1 = \mathbf{2}
      $$
    - $f[3] = 2$.
  - **Step 4: Output:**
    $$
    ans = f[3] = \mathbf{2}
    $$
- **Larger Example ($n = 4$):**
  - $D(4) = (4 - 1) \cdot (D(3) + D(2)) = 3 \cdot (2 + 1) = 3 \cdot 3 = \mathbf{9}$.
- **Larger Example ($n = 5$):**
  - $D(5) = (5 - 1) \cdot (D(4) + D(3)) = 4 \cdot (9 + 2) = 4 \cdot 11 = \mathbf{44}$.
- **Asymptotic Ratio to Factorial:**
  - Notice the sequence $D(n) / n!$:
    - $D(1)/1! = 0$
    - $D(2)/2! = 1/2 = 0.5$
    - $D(3)/3! = 2/6 = 0.333$
    - $D(4)/4! = 9/24 = 0.375$
    - $D(5)/5! = 44/120 = 0.3667$
  - As $n \to \infty$, $D(n) / n! \to \frac{1}{e} \approx 0.367879$.

This instance demonstrates fixed-point exclusion combinatorics and subfactorial recurrence derivations, mathematically proves why partitioning by 2-cycle transpositions decouples recursive subproblem cardinality, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n$:
Find the number of **derangements** of $\{1, \dots, n\}$ modulo $10^9 + 7$.
A derangement has $\pi(i) \ne i$ for all $i$.

```text
n = 3:
  Valid derangements:
    [2, 3, 1]  (1->2, 2->3, 3->1)
    [3, 1, 2]  (1->3, 2->1, 3->2)

Total count = 2
```

### The Invariant of Subfactorial Recurrence
- Every derangement of $n$ elements either:
  1. Contains a 2-cycle involving element $n$ and some $k$ ($D(n-2)$ ways).
  2. Element $n$ is part of a larger cycle $\ge 3$ ($D(n-1)$ ways).
- Scaling by the $n - 1$ symmetric choices for partner $k$ yields:
  $$
  D(n) = (n - 1)(D(n - 1) + D(n - 2))
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. Recurrence Relations:
- Second-order linear recurrence:
  $$
  D(n) = (n - 1) \cdot (D(n - 1) + D(n - 2)) \pmod{10^9 + 7}
  $$
- First-order alternating recurrence:
  $$
  D(n) = n \cdot D(n - 1) + (-1)^n \pmod{10^9 + 7}
  $$

### 2. Base Cases:
$$
D(0) = 1, \quad D(1) = 0
$$

> **Fixed-Point Exclusion Invariant.** By the principle of inclusion-exclusion, $D(n) = n! \sum_{i=0}^n \frac{(-1)^i}{i!}$, whose integer discretization satisfies the homogeneous shift relation $D(n) - n D(n-1) = -(D(n-1) - (n-1)D(n-2))$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 3$:

---

### Step 1: Base Anchoring
- $f[0] = 1$.
- $f[1] = 0$.

---

### Step 2: Evaluate $i = 2$
$$
f[2] = (2 - 1) \cdot (f[1] + f[0]) = 1 \cdot (0 + 1) = \mathbf{1}
$$

---

### Step 3: Evaluate $i = 3$
$$
f[3] = (3 - 1) \cdot (f[2] + f[1]) = 2 \cdot (1 + 0) = \mathbf{2}
$$

---

### Step 4: Final Output
$$
\mathbf{2}
$$

---

## 4. Complete Execution Trace

| Index $i$ | Predecessor $f[i-1]$ | Second Predecessor $f[i-2]$ | Multiplier $i - 1$ | Sum $f[i-1] + f[i-2]$ | Computed $f[i]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | — | — | — | — | $1$ |
| $1$ | — | — | — | — | $0$ |
| $2$ | $0$ | $1$ | $1$ | $1$ | **$1$** |
| **$3$** | **$1$** | **$0$** | **$2$** | **$1$** | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$:** Single element has no other slot to occupy $\implies 0$.
- **$n = 2$:** Only swap `[2, 1]` $\implies 1$.
- **Large $n$ ($n = 10^6$):** Loop computes iteratively in $O(N)$ time with rolling variables, avoiding call stack overflow.
- **Modulo Handling:** Apply `% (10**9 + 7)` after multiplication at every step.

---

## 6. Traps & Common Anti-Patterns

- **Direct Factorial Inclusion-Exclusion ($O(N)$ with division):** Evaluating $n! \sum \frac{(-1)^i}{i!}$ modulo $10^9 + 7$ requires computing modular inverses, which is slower and more complex than simple integer addition and multiplication.
- **Naive Recursion Without Memoization ($O(2^N)$):** Computing $D(n) = (n-1)(D(n-1) + D(n-2))$ recursively without memoization explodes exponentially.
- **Off-by-One Base Case:** Setting $D(0) = 0$ instead of $D(0) = 1$ causes $D(2)$ to evaluate to $1 \cdot (0 + 0) = 0$, breaking the entire sequence.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single loop from $i = 2$ to $n$: exactly $n - 1$ iterations.
  - Each step involves one addition, one multiplication, and one modulo operation: $\mathcal{O}(1)$ time.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 10^6$, completes in $< 50$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ space if using two rolling variables ($prev, curr$), or $\mathcal{O}(N)$ for the DP array.
