# Guided Example: Minimum Swaps to Make Sequences Increasing

We trace the step-by-step parallel array strictly increasing invariant ($A[i] > A[i-1] \land B[i] > B[i-1]$), dual 2-state dynamic programming state machine ($a = \text{no swap}, \; b = \text{swap}$), self-increasing versus cross-increasing condition taxonomy, state transitions across parity branches, and minimum total swap convergence on representative integer sequence pairs:

- **Input:**
  $$
  nums1 = [1, 3, 5, 4], \quad nums2 = [1, 2, 3, 7]
  $$
- **Required output:** `1`
  - Array swap mechanics & strict monotonicity constraints:
    - You are given two arrays $nums1$ and $nums2$ of length $n$.
    - In one operation, you can swap $nums1[i]$ and $nums2[i]$ at the same index $i$.
    - Objective: Find the **minimum number of swaps** needed to make both arrays **strictly increasing**:
      $$
      nums1[0] < nums1[1] < \dots < nums1[n - 1]
      $$
      $$
      nums2[0] < nums2[1] < \dots < nums2[n - 1]
      $$
    - For $nums1 = [1, 3, 5, 4]$ and $nums2 = [1, 2, 3, 7]$:
      - Notice at index 3: $nums1[2] = 5$ while $nums1[3] = 4$ ($5 \not< 4$).
      - If we swap at index 3:
        - $nums1$ becomes $[1, 3, 5, 7]$ (strictly increasing!).
        - $nums2$ becomes $[1, 2, 3, 4]$ (strictly increasing!).
      - Both sequences are strictly increasing with only **1 swap**.
- **The Dual-State Markov Invariant ($a, b$):**
  - **State Definitions at Index $i$:**
    - Let $a$ be the minimum swaps to make prefix $0 \dots i$ valid such that we **do NOT swap** at index $i$.
    - Let $b$ be the minimum swaps to make prefix $0 \dots i$ valid such that we **DO swap** at index $i$.
  - **Base Case at Index $0$:**
    $$
    a = 0 \quad (\text{0 swaps}), \qquad b = 1 \quad (\text{1 swap at index 0})
    $$
  - **The Two Transition Conditions:**
    - At index $i \ge 1$, compare adjacent pairs:
      1. **Self-Increasing Condition ($C_{\text{self}}$):**
         $$
         nums1[i - 1] < nums1[i] \quad \text{and} \quad nums2[i - 1] < nums2[i]
         $$
      2. **Cross-Increasing Condition ($C_{\text{cross}}$):**
         $$
         nums1[i - 1] < nums2[i] \quad \text{and} \quad nums2[i - 1] < nums1[i]
         $$
  - **Branching Transition Rules:**
    - **Case 1 (Only $C_{\text{cross}}$ holds, not $C_{\text{self}}$):**
      - The unswapped pair is not increasing, so the swap decisions at $i - 1$ and $i$ **must differ**:
        $$
        a_{\text{new}} = b_{\text{old}}
        $$
        $$
        b_{\text{new}} = a_{\text{old}} + 1
        $$
    - **Case 2 (Only $C_{\text{self}}$ holds, not $C_{\text{cross}}$):**
      - Crossing is illegal, so the swap decisions at $i - 1$ and $i$ **must match** (either swap both or neither):
        $$
        a_{\text{new}} = a_{\text{old}}
        $$
        $$
        b_{\text{new}} = b_{\text{old}} + 1
        $$
    - **Case 3 (Both $C_{\text{self}}$ and $C_{\text{cross}}$ hold):**
      - Both choices are legal; take the minimum:
        $$
        a_{\text{new}} = \min(a_{\text{old}}, \; b_{\text{old}})
        $$
        $$
        b_{\text{new}} = \min(b_{\text{old}} + 1, \; a_{\text{old}} + 1)
        $$
- **Step-by-Step Worked Execution Trace on $nums1 = [1, 3, 5, 4], nums2 = [1, 2, 3, 7]$:**
  - Length $n = 4$.
  - **Index 0:**
    - $a = 0, \quad b = 1$.
  - **Index 1 (Pairs $(1, 3)$ and $(1, 2)$):**
    - $C_{\text{self}}$: $1 < 3$ and $1 < 2 \implies \mathbf{True.}$
    - $C_{\text{cross}}$: $1 < 2$ and $1 < 3 \implies \mathbf{True.}$
    - Case 3 (Both hold):
      $$
      a \leftarrow \min(a, b) = \min(0, 1) = \mathbf{0}
      $$
      $$
      b \leftarrow \min(b + 1, a + 1) = \min(1 + 1, 0 + 1) = \mathbf{1}
      $$
    - State after index 1: $a = 0, b = 1$.
  - **Index 2 (Pairs $(3, 5)$ and $(2, 3)$):**
    - $C_{\text{self}}$: $3 < 5$ and $2 < 3 \implies \mathbf{True.}$
    - $C_{\text{cross}}$: $3 < 3$ and $2 < 5 \implies \mathbf{False}$ *(3 is not strictly less than 3)*.
    - Case 2 (Only $C_{\text{self}}$ holds):
      - Must match swap status of index 1:
      $$
      a \leftarrow a = \mathbf{0}
      $$
      $$
      b \leftarrow b + 1 = 1 + 1 = \mathbf{2}
      $$
    - State after index 2: $a = 0, b = 2$.
  - **Index 3 (Pairs $(5, 4)$ and $(3, 7)$):**
    - $C_{\text{self}}$: $5 < 4$ and $3 < 7 \implies \mathbf{False}$ *(5 is not less than 4!)*.
    - $C_{\text{cross}}$: $5 < 7$ and $3 < 4 \implies \mathbf{True.}$
    - Case 1 (Only $C_{\text{cross}}$ holds):
      - Must invert swap status relative to index 2:
      $$
      a \leftarrow b_{\text{old}} = \mathbf{2}
      $$
      $$
      b \leftarrow a_{\text{old}} + 1 = 0 + 1 = \mathbf{1}
      $$
    - State after index 3: $a = 2, b = 1$.
  - **Termination:**
    - Array end reached.
    - Minimum total operations:
      $$
      ans = \min(a, b) = \min(2, 1) = \mathbf{1}
      $$
- **Swap First Pair Trace ($nums1 = [0, 3, 5, 8], nums2 = [2, 1, 4, 6]$):**
  - Swapping index 0 produces $[2, 3, 5, 8]$ and $[0, 1, 4, 6]$, resolving the inversions at lower cost than swapping multiple subsequent elements.
  - The DP state machine automatically propagates $b = 1$ forward to achieve optimal cost.
- **Identical Arrays Trace ($nums1 == nums2$):**
  - Swapping does not alter values $\implies ans = \mathbf{0}$.

This instance demonstrates 2-state forward dynamic programming over product posets and transition graph coupling, mathematically proves why memoryless local compatibility conditions determine global strict monotonicity, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given two arrays $nums1$ and $nums2$:
Find the **minimum swaps** at matching indices $i$ to make both arrays **strictly increasing**.

```text
nums1 = [ 1, 3, 5, 4 ]
nums2 = [ 1, 2, 3, 7 ]

Notice at index 3:
  nums1: 5 -> 4 (NOT increasing!)
  Swap index 3:
    nums1 becomes [ 1, 3, 5, 7 ] (strictly increasing!)
    nums2 becomes [ 1, 2, 3, 4 ] (strictly increasing!)

Minimum swaps = 1
Result: 1
```

### The Invariant of the 2-State Machine
At each index $i$, track two minimal costs:
- $a$: cost if we **do not swap** at index $i$.
- $b$: cost if we **do swap** at index $i$.
Depending on whether pairs are self-increasing ($A[i-1] < A[i]$) or cross-increasing ($A[i-1] < B[i]$), transitions couple or decouple $a$ and $b$.

---

## 2. Conceptual Foundation & Invariants

### 1. Compatibility Conditions:
$$
C_{\text{self}} \iff nums1[i - 1] < nums1[i] \;\land\; nums2[i - 1] < nums2[i]
$$
$$
C_{\text{cross}} \iff nums1[i - 1] < nums2[i] \;\land\; nums2[i - 1] < nums1[i]
$$

### 2. State Transition Recurrence:
$$
(a', b') = \begin{cases}
(b, a + 1) & \neg C_{\text{self}} \land C_{\text{cross}} \\
(a, b + 1) & C_{\text{self}} \land \neg C_{\text{cross}} \\
(\min(a, b), \min(b + 1, a + 1)) & C_{\text{self}} \land C_{\text{cross}}
\end{cases}
$$

> **Markov Decision Chain Invariant.** The strictly increasing constraint on the Cartesian product $\mathbb{R}^n \times \mathbb{R}^n$ under coordinate transposition factors into a two-state trellis diagram. Optimal paths through the trellis satisfy Bellman's principle of optimality with transition rank at most 2.

---

## 3. Step-by-Step Worked Execution

We trace $nums1 = [1, 3, 5, 4], nums2 = [1, 2, 3, 7]$:

---

### Step 1: Base Case ($i = 0$)
- $a = 0, b = 1$.

---

### Step 2: Index 1
- Both $C_{\text{self}}$ and $C_{\text{cross}}$ true $\implies a = \min(0, 1) = 0, b = \min(2, 1) = 1$.

---

### Step 3: Index 2
- Only $C_{\text{self}}$ true ($3 < 3$ fails cross) $\implies a = 0, b = 1 + 1 = 2$.

---

### Step 4: Index 3
- Only $C_{\text{cross}}$ true ($5 < 4$ fails self) $\implies a = b_{\text{old}} = 2, b = a_{\text{old}} + 1 = 1$.

---

### Step 5: Output
- $\min(2, 1) = \mathbf{1}$.

---

## 4. Complete Execution Trace

| Index $i$ | $nums1[i], nums2[i]$ | $C_{\text{self}}$ Valid? | $C_{\text{cross}}$ Valid? | Unswapped Cost $a$ | Swapped Cost $b$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $1, 1$ | — | — | $0$ | $1$ |
| $1$ | $3, 2$ | Yes ($1<3, 1<2$) | Yes ($1<2, 1<3$) | $0$ | $1$ |
| $2$ | $5, 3$ | Yes ($3<5, 2<3$) | No ($3 < 3$ false) | $0$ | $2$ |
| **$3$** | **$4, 7$** | **No ($5 < 4$ false)** | **Yes ($5<7, 3<4$)** | **$2$** | **`1`** |
| **Final** | — | — | — | — | **$\min(2, 1) = \mathbf{1}$** |

---

## 5. Boundary Cases & Failure Modes

- **Already Strictly Increasing ($[1, 2], [3, 4]$):** 0 swaps needed $\implies ans = 0$.
- **Swap Everything ($[2, 1], [1, 2]$):** Swapping index 0 resolves both $\implies ans = 1$.
- **Length 2 Array:** Minimal problem size, evaluates single transition.
- **Strict Inequality:** Numbers must be strictly increasing ($x < y$); equality $x == y$ triggers cross or self failure.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Swapping Based on Local Comparison:** Deciding to swap index $i$ without looking at future elements leads to dead ends where future indices cannot be satisfied. Dynamic programming considers all forward ripple effects.
- **Forgetting That Both Conditions Can Hold:** When both $C_{\text{self}}$ and $C_{\text{cross}}$ are true, you have complete freedom to choose whether to match or invert previous swap choices; take $\min(a, b)$.
- **O(N) Space Overhead:** Only the scalar variables $a$ and $b$ from the previous index are needed, keeping auxiliary memory strictly $O(1)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass from $i = 1$ to $n - 1$: $N - 1$ steps.
  - Constant-time scalar arithmetic per step: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 10^5$. Completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (two scalar state variables).