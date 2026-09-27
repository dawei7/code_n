# Guided Example: Fibonacci Number

We trace the step-by-step linear recurrence relation ($F(n) = F(n-1) + F(n-2)$), initial condition grounding ($F(0) = 0, F(1) = 1$), two-variable rolling register transitions ($a \leftarrow b, \; b \leftarrow a + b$), exponential recursion avoidance, and constant-space sequence evolution on representative index queries:

- **Input:** $n = 5$
- **Required output:** `5`
  - Canonical recurrence definition:
    $$
    F(0) = 0, \quad F(1) = 1
    $$
    $$
    F(n) = F(n - 1) + F(n - 2) \quad \text{for } n \ge 2
    $$
- **Rolling register state execution trace:**
  - Initialize two memory registers:
    $$
    a = F(0) = 0, \quad b = F(1) = 1
    $$
  - At each step, $a$ stores $F(k)$ and $b$ stores $F(k + 1)$.
  - **Step 1 ($k = 0 \to 1$):**
    - State before: $a = 0, \; b = 1$
    - Simultaneous update:
      $$
      a \leftarrow b = \mathbf{1}, \quad b \leftarrow a + b = 0 + 1 = \mathbf{1}
      $$
    - State after: $a = F(1) = 1, \; b = F(2) = 1$
  - **Step 2 ($k = 1 \to 2$):**
    - State before: $a = 1, \; b = 1$
    - Simultaneous update:
      $$
      a \leftarrow b = \mathbf{1}, \quad b \leftarrow a + b = 1 + 1 = \mathbf{2}
      $$
    - State after: $a = F(2) = 1, \; b = F(3) = 2$
  - **Step 3 ($k = 2 \to 3$):**
    - State before: $a = 1, \; b = 2$
    - Simultaneous update:
      $$
      a \leftarrow b = \mathbf{2}, \quad b \leftarrow a + b = 1 + 2 = \mathbf{3}
      $$
    - State after: $a = F(3) = 2, \; b = F(4) = 3$
  - **Step 4 ($k = 3 \to 4$):**
    - State before: $a = 2, \; b = 3$
    - Simultaneous update:
      $$
      a \leftarrow b = \mathbf{3}, \quad b \leftarrow a + b = 2 + 3 = \mathbf{5}
      $$
    - State after: $a = F(4) = 3, \; b = F(5) = 5$
  - **Step 5 ($k = 4 \to 5$):**
    - State before: $a = 3, \; b = 5$
    - Simultaneous update:
      $$
      a \leftarrow b = \mathbf{5}, \quad b \leftarrow a + b = 3 + 5 = \mathbf{8}
      $$
    - State after: $a = F(5) = 5, \; b = F(6) = 8$
  - Loop completes $n = 5$ transitions.
  - Return register $a$:
    $$
    F(5) = \mathbf{5}
    $$
- **Base Case $n = 0$:**
  - Loop runs $0$ times $\implies$ returns initial $a = \mathbf{0}$
- **Base Case $n = 1$:**
  - Loop runs $1$ time $\implies a \leftarrow b = \mathbf{1}$
- **Higher Value Instance ($n = 8$):**
  - Sequence continues: $F(6) = 8, F(7) = 13, F(8) = 21 \implies \mathbf{21}$

This instance demonstrates linear state roll-forward dynamic programming, mathematically proves why tracking only the two most recent terms eliminates the need for an $O(N)$ memoization array, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n$:
Calculate $F(n)$, the $n$-th Fibonacci number:
$$
F(0) = 0, \quad F(1) = 1, \quad F(n) = F(n-1) + F(n-2)
$$

```text
Fibonacci Number Sequence:
  F(0) = 0
  F(1) = 1
  F(2) = 0 + 1 = 1
  F(3) = 1 + 1 = 2
  F(4) = 1 + 2 = 3
  F(5) = 2 + 3 = 5
  F(6) = 3 + 5 = 8
  F(7) = 5 + 8 = 13
  F(8) = 8 + 13 = 21

Result for n = 5: 5
```

### Avoiding the $O(2^N)$ Exponential Branching Trap
A naive recursive implementation:
$$
\text{fib}(n) = \text{fib}(n-1) + \text{fib}(n-2)
$$
generates a binary recursion tree of depth $n$ with $2^n$ redundant calls (e.g. $\text{fib}(2)$ is recalculated hundreds of times).
By computing bottom-up from $0$ to $n$:
Each Fibonacci number is computed once in $O(1)$ addition operations.
Because each term depends only on the immediate two preceding terms, **we only need two integer variables** to store the moving window.

---

## 2. Conceptual Foundation & Invariants

### 1. Rolling Register State Machine:
Let state at iteration $k$ be $(a_k, b_k)$:
- Invariant: $a_k = F(k)$ and $b_k = F(k + 1)$.
- Initialization ($k = 0$):
  $$
  a_0 = 0, \quad b_0 = 1
  $$
- Transition to $k + 1$:
  $$
  \begin{aligned}
  a_{k+1} &= b_k = F(k + 1) \\
  b_{k+1} &= a_k + b_k = F(k) + F(k + 1) = F(k + 2)
  \end{aligned}
  $$
- After $n$ iterations, $a_n = F(n)$.

> **Inductive Invariant.** At the beginning of iteration $k$, register $a$ holds $F(k)$ and register $b$ holds $F(k+1)$, ensuring exact alignment with the canonical Fibonacci recurrence.

---

## 3. Step-by-Step Worked Execution

We trace $n = 5$:

---

### Step 1: Initialize Registers
$$
a = 0, \quad b = 1
$$

---

### Step 2: Perform $n = 5$ Iterations

1. **Iteration 1:**
   $$
   a_{new} = 1, \quad b_{new} = 0 + 1 = 1 \implies (a, b) = (1, 1)
   $$
2. **Iteration 2:**
   $$
   a_{new} = 1, \quad b_{new} = 1 + 1 = 2 \implies (a, b) = (1, 2)
   $$
3. **Iteration 3:**
   $$
   a_{new} = 2, \quad b_{new} = 1 + 2 = 3 \implies (a, b) = (2, 3)
   $$
4. **Iteration 4:**
   $$
   a_{new} = 3, \quad b_{new} = 2 + 3 = 5 \implies (a, b) = (3, 5)
   $$
5. **Iteration 5:**
   $$
   a_{new} = 5, \quad b_{new} = 3 + 5 = 8 \implies (a, b) = (5, 8)
   $$

---

### Step 3: Return Output
Value in $a$ after 5 steps:
$$
\mathbf{5}
$$

---

## 4. Complete Execution Trace

| Iteration Step | Previous $a$ ($F(k)$) | Previous $b$ ($F(k+1)$) | Addition $a + b$ | New $a = b$ | New $b = a_{prev} + b_{prev}$ | Represented Fibonacci Term |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init ($k=0$)** | — | — | — | $0$ | $1$ | $F(0) = 0$ |
| **$1$ ($k=1$)** | $0$ | $1$ | $0 + 1 = 1$ | $1$ | $1$ | $F(1) = 1$ |
| **$2$ ($k=2$)** | $1$ | $1$ | $1 + 1 = 2$ | $1$ | $2$ | $F(2) = 1$ |
| **$3$ ($k=3$)** | $1$ | $2$ | $1 + 2 = 3$ | $2$ | $3$ | $F(3) = 2$ |
| **$4$ ($k=4$)** | $2$ | $3$ | $2 + 3 = 5$ | $3$ | $5$ | $F(4) = 3$ |
| **$5$ ($k=5$)** | $3$ | $5$ | $3 + 5 = 8$ | **$5$** | $8$ | **$F(5) = 5$** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 0$:** Range loop executes 0 times $\implies$ returns initial $a = \mathbf{0}$.
- **$n = 1$:** Range loop executes 1 time $\implies a \leftarrow b = \mathbf{1}$.
- **$n = 2$:** Range loop executes 2 times $\implies a = \mathbf{1}$.
- **Maximum Bound ($n = 30$):** $F(30) = 832,040$, fits easily inside standard 32-bit signed integers.

---

## 6. Traps & Common Anti-Patterns

- **Sequential Overwrite Bug:** Writing `a = b` followed by `b = a + b` in languages without simultaneous assignment overwrites $a$ before using its old value, effectively computing $b = b + b$. Using a temporary variable `temp = a + b; a = b; b = temp;` is required in C/Java.
- **Unmemoized Recursion:** Calling `fib(n-1) + fib(n-2)` takes $O(2^n)$ time, timing out for $n \ge 35$.
- **Off-by-One in Iteration Count:** Looping $n - 1$ times or returning $b$ instead of $a$ shifts the sequence indices by 1. Returning $a$ after $n$ iterations guarantees returning $F(n)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The loop performs exactly $n$ iterations.
  - Each iteration performs one integer addition and assignment in $O(1)$ time.
  - Total Time: $\mathcal{O}(N)$. For $n = 30$, takes $< 1$ microsecond.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space using two scalar registers $a$ and $b$.