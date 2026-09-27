# Guided Example: 24 Game

We trace the step-by-step recursive contraction of multiset numbers ($4 \to 3 \to 2 \to 1$), binary arithmetic operator branching (`+`, `-`, `*`, `/`), real-valued floating-point division precision ($\epsilon = 10^{-6}$), division-by-zero avoidance, pair selection permutations ($i \ne j$), and successful expression tree synthesis on representative 4-card hands:

- **Input:** $cards = [4, 1, 8, 7]$
- **Required output:** `true`
  - Rules of the 24 Game:
    - You must use all 4 cards exactly once.
    - Allowed binary operators: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
    - Arbitrary parentheses may group operations in any legal order.
    - Division is real-number division (e.g. $4 / (1 - 2/3) = 12$), not integer truncation.
    - Unary negation is disallowed (cannot do $-4$).
    - Objective: Determine if any valid grouping and assignment of operators evaluates to **24**.
    - For $[4, 1, 8, 7]$:
      $$
      (8 - 4) \times (7 - 1) = 4 \times 6 = \mathbf{24}
      $$
- **Recursive Multiset Contraction & Full Binary Tree Invariant:**
  - **The Pair Contraction Principle:**
    - Any mathematical expression evaluating 4 numbers using binary operators corresponds to a full binary tree with 4 leaves and 3 internal operation nodes.
    - In each contraction step:
      1. Pick any two distinct numbers $nums[i]$ and $nums[j]$ from the current set of size $n$ ($n \in \{4, 3, 2\}$).
      2. Combine them using one of the valid operations to form a single new number $v$:
         $$
         v \in \left\{ a + b, \; a - b, \; a \times b, \; \frac{a}{b} \ (b \ne 0) \right\}
         $$
      3. The remaining $n - 2$ numbers plus the newly formed $v$ constitute a smaller multiset of size $n - 1$.
    - Repeating this 3 times contracts the multiset from size $4 \to 3 \to 2 \to 1$.
  - **Base Decision Condition ($n = 1$):**
    - Due to real division creating floating-point approximations, we test equality within a floating-point tolerance $\epsilon = 10^{-6}$:
      $$
      |nums[0] - 24.0| < 10^{-6} \implies \mathbf{True!}
      $$
- **Step-by-Step Worked Execution Trace on $[4, 1, 8, 7]$:**
  - Initial multiset: $\{4.0, \; 1.0, \; 8.0, \; 7.0\}$ (size $n = 4$).
  - **Level 1 Search ($n = 4 \to n = 3$):**
    - Consider pair selection: pick $a = 8.0$ and $b = 4.0$.
    - Unused elements: $\{1.0, \; 7.0\}$.
    - Test subtraction operator:
      $$
      v_1 = a - b = 8.0 - 4.0 = \mathbf{4.0}
      $$
    - Contracted multiset:
      $$
      \{1.0, \; 7.0, \; \mathbf{4.0}\} \quad (n = 3)
      $$
  - **Level 2 Search ($n = 3 \to n = 2$):**
    - Consider pair selection from $\{1.0, 7.0, 4.0\}$: pick $a = 7.0$ and $b = 1.0$.
    - Unused element: $\{4.0\}$.
    - Test subtraction operator:
      $$
      v_2 = a - b = 7.0 - 1.0 = \mathbf{6.0}
      $$
    - Contracted multiset:
      $$
      \{4.0, \; \mathbf{6.0}\} \quad (n = 2)
      $$
  - **Level 3 Search ($n = 2 \to n = 1$):**
    - Only two numbers remain: $a = 4.0$ and $b = 6.0$.
    - Test multiplication operator:
      $$
      v_3 = a \times b = 4.0 \times 6.0 = \mathbf{24.0}
      $$
    - Contracted multiset:
      $$
      \{\mathbf{24.0}\} \quad (n = 1)
      $$
  - **Level 4 Base Verification ($n = 1$):**
    - Remaining value: $24.0$.
    - Evaluate target distance:
      $$
      |24.0 - 24.0| = 0.0 < 10^{-6} \implies \mathbf{Target\ 24\ Reached!}
      $$
    - Unwind recursion immediately with **`true`**.
- **The Fractional Division Subtlety ($[3, 3, 8, 8]$):**
  - Integer operations fail to produce 24 on this hand.
  - However, using rational fraction division:
    - Step 1: $8 / 3 \approx 2.666667$.
    - Step 2: $3 - (8 / 3) = 1/3 \approx 0.333333$.
    - Step 3: $8 / (1/3) = \mathbf{24.0}$!
    - The floating-point tolerance check correctly accepts this valid solution.
- **Unsolvable Hand ($[1, 2, 1, 2]$):**
  - All combinations of pairs and operators yield maximum reachable values around $6$ or small fractions.
  - Exhaustive search of all tree shapes explores all combinations and concludes with **`false`**.

This instance demonstrates backtrack search over binary expression tree topologies and non-associative operator permutations, mathematically proves why pair contraction covers all bracket structures, and derives $O(1)$ fixed bounded search space and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given 4 numbers between 1 and 9:
Using operations `+`, `-`, `*`, `/` and parentheses, determine if you can **evaluate to 24**.

```text
cards = [ 4, 1, 8, 7 ]

Solution expression:
  (8 - 4) * (7 - 1) = 4 * 6 = 24

Evaluation path:
  Level 1 (4 -> 3): combine 8 and 4 with '-' -> [ 4, 1, 7 ]
  Level 2 (3 -> 2): combine 7 and 1 with '-' -> [ 4, 6 ]
  Level 3 (2 -> 1): combine 4 and 6 with '*' -> [ 24 ]

Target reached! Return true.
```

### The Invariant of Expression Tree Equivalence
- Every parenthesization of 4 numbers corresponds to a full binary tree with 4 leaves.
- Repeatedly picking 2 numbers, applying an operator, and replacing them with the result generates **all possible parenthesizations and operator placements**.

---

## 2. Conceptual Foundation & Invariants

### 1. Pair Reduction Step ($N \to N - 1$):
Given list $nums$ of length $n$:
For each distinct pair $(i, j)$:
$$
nxt = [nums[k] \mid k \ne i, k \ne j]
$$
For each $op \in \{+, -, \times, /\ (\text{if } nums[j] \ne 0)\}$:
$$
\text{Recurse on: } nxt \cup \{nums[i] \circ nums[j]\}
$$

### 2. Floating-Point Tolerance Check:
At $n == 1$:
$$
\text{Success} \iff |nums[0] - 24| < 10^{-6}
$$

> **Dyadic Multiset Contraction Invariant.** Any algebraic expression over an abelian monoid with division and subtraction generated by $k$ leaves is isomorphic to a path in the configuration graph of multiset contractions $\mathcal{M}_k \to \mathcal{M}_{k-1} \dots \to \mathcal{M}_1$.

---

## 3. Step-by-Step Worked Execution

We trace $[4, 1, 8, 7]$:

---

### Step 1: Pair $(8, 4)$
- Operator `-`: $8 - 4 = 4$.
- New multiset: $\{1, 7, 4\}$.

---

### Step 2: Pair $(7, 1)$
- Operator `-`: $7 - 1 = 6$.
- New multiset: $\{4, 6\}$.

---

### Step 3: Pair $(4, 6)$
- Operator `*`: $4 \times 6 = 24$.
- New multiset: $\{24\}$.

---

### Step 4: Base Check
- $|24 - 24| < 10^{-6} \implies \mathbf{true}$.

---

## 4. Complete Execution Trace

| Level | Current Numbers | Pair Picked $(a, b)$ | Operator Applied | Resulting Value | Next Number Multiset |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ ($n = 4$) | $\{4, 1, 8, 7\}$ | $(8, 4)$ | Subtraction (`-`) | $8 - 4 = \mathbf{4}$ | $\{1, 7, 4\}$ |
| $2$ ($n = 3$) | $\{1, 7, 4\}$ | $(7, 1)$ | Subtraction (`-`) | $7 - 1 = \mathbf{6}$ | $\{4, 6\}$ |
| $3$ ($n = 2$) | $\{4, 6\}$ | $(4, 6)$ | Multiplication (`*`) | $4 \times 6 = \mathbf{24}$ | $\{\mathbf{24}\}$ |
| **$4$ ($n = 1$)** | **`{24}`** | — | — | **$\lvert 24 - 24 \rvert = 0 < 10^{-6}$** | **Target Met: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Division by Zero ($nums[j] == 0$):** Must explicitly guard against dividing by zero (`if nums[j] == 0: continue`).
- **Precision Tolerance:** Using integer division `//` fails on hands like $[3, 3, 8, 8] \implies 8 / (3 - 8/3) = 24$. Floating-point division with $\epsilon = 10^{-6}$ is mandatory.
- **Non-Commutative Operations (`-`, `/`):** Order matters ($a - b \ne b - a$ and $a / b \ne b / a$). Testing both ordered pairs $(i, j)$ and $(j, i)$ naturally explores both directions.

---

## 6. Traps & Common Anti-Patterns

- **Only Testing Linear Expressions:** Assuming expressions are of the form $((a \circ b) \circ c) \circ d$ misses balanced tree expressions like $(a \circ b) \circ (c \circ d)$ (such as $(8-4) \times (7-1)$!). The recursive multiset reduction covers both tree shapes automatically.
- **Using Integer Division:** Integer division truncates $8 / 3$ to $2$, causing solvable hands like $[3, 3, 8, 8]$ to falsely fail.
- **Unary Minus:** Expressions cannot prepend a minus sign like $-(4 - 28)$; every operator must be binary between two existing operands.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Step 1: $\binom{4}{2} \times 2 = 12$ ordered pairs $\times 4$ operators $= 48$ branches.
  - Step 2: $\binom{3}{2} \times 2 = 6$ ordered pairs $\times 4$ operators $= 24$ branches.
  - Step 3: $2$ ordered pairs $\times 4$ operators $= 8$ branches.
  - Total states: $48 \times 24 \times 8 = 9216$ worst-case evaluations.
  - Total Time: strictly constant $\mathcal{O}(1)$ time. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - Maximum recursion depth is $4 \implies \mathcal{O}(1)$ stack space.
