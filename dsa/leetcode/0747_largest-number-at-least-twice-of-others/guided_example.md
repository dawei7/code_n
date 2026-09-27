# Guided Example: Largest Number At Least Twice of Others

We trace the step-by-step single-pass maximum and runner-up tracking ($m_1, m_2$), runner-up dominance inequality evaluation ($m_1 \ge 2 m_2$), universal condition reduction via the maximum non-dominant element, original array index resolution ($idx$), and boundary cases on representative integer arrays:

- **Input:** $nums = [3, 6, 1, 0]$
- **Required output:** `1`
  - Dominance condition:
    - Identify the unique largest element $m_1$ in the array.
    - Check whether $m_1$ is **at least twice as large** as every other number $z$ in $nums$:
      $$
      m_1 \ge 2z \quad \forall z \ne m_1
      $$
    - If the condition is satisfied, return the **index** of $m_1$ in $nums$.
    - Otherwise, return `-1`.
    - For $[3, 6, 1, 0]$:
      - Array elements: $3, 6, 1, 0$.
      - Maximum element: $6$ (located at index 1).
      - Compare against all other elements:
        - $6 \ge 2 \times 3 = 6$ (holds!).
        - $6 \ge 2 \times 1 = 2$ (holds!).
        - $6 \ge 2 \times 0 = 0$ (holds!).
      - Since $6$ is at least twice every other number, return its index: **1**.
- **Runner-Up Reduction Invariant:**
  - **The Universal Quantifier Reduction:**
    - To verify that $m_1 \ge 2z$ for all $z \ne m_1$, we do not need to test every element individually.
    - Let $m_2$ be the **second largest element** (the runner-up).
    - By definition, $m_2 \ge z$ for all other elements $z \ne m_1$.
    - Therefore, the universal statement holds if and only if it holds for the runner-up:
      $$
      (\forall z \ne m_1: \; m_1 \ge 2z) \iff m_1 \ge 2m_2
      $$
  - **Single-Pass Tracking Protocol:**
    - Initialize $m_1 = -\infty, \; m_2 = -\infty, \; idx = -1$.
    - For each index $i$ and value $v = nums[i]$:
      - If $v > m_1$:
        - The old maximum is demoted to runner-up: $m_2 \leftarrow m_1$.
        - Update new maximum and index: $m_1 \leftarrow v, \; idx \leftarrow i$.
      - Else if $v > m_2$:
        - Update runner-up: $m_2 \leftarrow v$.
    - Decision:
      $$
      ans = \begin{cases} idx & \text{if } m_1 \ge 2m_2 \\ -1 & \text{otherwise} \end{cases}
      $$
- **Step-by-Step Worked Execution Trace on $nums = [3, 6, 1, 0]$:**
  - Initialize: $m_1 = -\infty, m_2 = -\infty, idx = -1$.
  - **Index $i = 0$ ($v = 3$):**
    - $3 > -\infty \implies$ Demote old $m_1$, promote 3:
      $$
      m_2 \leftarrow -\infty, \quad m_1 \leftarrow 3, \quad idx \leftarrow 0
      $$
  - **Index $i = 1$ ($v = 6$):**
    - $6 > 3 \implies$ Demote $3$ to runner-up, promote $6$:
      $$
      m_2 \leftarrow 3, \quad m_1 \leftarrow 6, \quad idx \leftarrow 1
      $$
  - **Index $i = 2$ ($v = 1$):**
    - $1 \le 6$ (not greater than $m_1$).
    - $1 \le 3$ (not greater than $m_2$).
    - No changes: $m_1 = 6, m_2 = 3, idx = 1$.
  - **Index $i = 3$ ($v = 0$):**
    - $0 \le 6$ and $0 \le 3$.
    - No changes.
  - **Dominance Evaluation:**
    - Largest element: $m_1 = \mathbf{6}$ at index $idx = \mathbf{1}$.
    - Runner-up element: $m_2 = \mathbf{3}$.
    - Evaluate test inequality:
      $$
      6 \ge 2 \times 3 \iff 6 \ge 6 \quad \mathbf{(Satisfied!)}
      $$
    - Result:
      $$
      ans = idx = \mathbf{1}
      $$
- **Non-Dominant Failure Trace ($nums = [1, 2, 3, 4]$):**
  - Maximum element: $m_1 = 4$ at index 3.
  - Runner-up element: $m_2 = 3$.
  - Evaluate test:
    $$
    4 \ge 2 \times 3 \iff 4 \ge 6 \quad \mathbf{(False!)}
    $$
    - Result: $ans = \mathbf{-1}$.
- **Single Element Array ($nums = [1]$):**
  - No second element exists ($m_2 = 0$ or $-\infty$).
  - Trivially satisfies dominance $\implies$ returns index **`0`**.
- **Array with Zeros ($nums = [0, 0, 3, 2]$):**
  - $m_1 = 3, m_2 = 2$.
  - $3 < 2 \times 2 = 4 \implies$ returns **`-1`**.

This instance demonstrates order-statistic reduction and single-pass scalar extremal tracking, mathematically proves why dominating the supremum over the complement set guarantees universal constraint satisfaction, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$:
Find the largest element $m_1$.
Return its index if $m_1 \ge 2z$ for all other elements $z$.
Otherwise, return -1.

```text
nums = [ 3, 6, 1, 0 ]

Largest element: 6 (at index 1)
Second largest element: 3

Test: 6 >= 2 * 3 = 6 (TRUE!)
Result: 1
```

### The Invariant of the Runner-Up Domination
- To verify that $m_1 \ge 2z$ for all elements, we only need to test against the **second largest element** $m_2$.
- If $m_1 \ge 2 m_2$, it is automatically $\ge 2z$ for all $z \le m_2$.
- Tracking $m_1$ and $m_2$ in a single pass solves the problem in $O(N)$ time with $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### 1. Extremal Equivalence:
$$
\big(\forall z \in nums \setminus \{m_1\}: \; m_1 \ge 2z\big) \iff m_1 \ge 2 \max_{z \ne m_1} z
$$

### 2. Decision Predicate:
$$
ans = \begin{cases} \text{index}(m_1) & \text{if } m_1 \ge 2m_2 \\ -1 & \text{otherwise} \end{cases}
$$

> **Supremum Dominance Invariant.** The cone inequality $x \ge 2y$ over a finite set $S$ with unique maximum $x = \max S$ holds uniformly across $S \setminus \{x\}$ if and only if it holds for the runner-up $y = \max (S \setminus \{x\})$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [3, 6, 1, 0]$:

---

### Step 1: Scan Elements
- $3 \implies m_1 = 3$.
- $6 \implies m_2 = 3, m_1 = 6$ (index 1).
- $1 \implies$ unchanged.
- $0 \implies$ unchanged.

---

### Step 2: Compare
- $m_1 = 6, m_2 = 3$.
- $6 \ge 2 \times 3 \implies 6 \ge 6$ (True).

---

### Step 3: Output
- Index of 6 is **`1`**.

---

## 4. Complete Execution Trace

| Element Scanned $v$ | Previous $m_1$ | Previous $m_2$ | Action Taken | Updated $m_1$ | Updated $m_2$ | Active Max Index |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $3$ | $-\infty$ | $-\infty$ | $3 > -\infty$ | $3$ | $-\infty$ | $0$ |
| $6$ | $3$ | $-\infty$ | $6 > 3 \implies$ Demote $3$ | $6$ | $3$ | $1$ |
| $1$ | $6$ | $3$ | $1 \le 3 \implies$ Ignore | $6$ | $3$ | $1$ |
| $0$ | $6$ | $3$ | $0 \le 3 \implies$ Ignore | $6$ | $3$ | $1$ |
| **Final Test** | — | — | **$6 \ge 2 \times 3$ (True)** | **$6$** | **$3$** | **Result: `1`** |

---

## 5. Boundary Cases & Failure Modes

- **Runner-Up Fails ($[1, 2, 3, 4]$):** $4 < 2 \times 3 = 6 \implies$ returns $-1$.
- **Tied Duplicate Maxima:** Problem guarantees the largest integer is unique.
- **Single Element Array ($[1]$):** $m_2$ is nonexistent $\implies$ returns 0.
- **All Zeros Except One ($[0, 0, 5, 0]$):** $5 \ge 2 \times 0 \implies$ returns index 2.

---

## 6. Traps & Common Anti-Patterns

- **Checking All Elements via Nested Loop ($O(N^2)$):** Iterating through all pairs is redundant. Testing only the second largest element $m_2$ guarantees validity in a single pass.
- **Sorting the Entire Array ($O(N \log N)$):** Sorting finds $m_1$ and $m_2$ but loses the original index of $m_1$ unless pairs `(val, idx)` are sorted. Single-pass linear scan preserves the original index with zero extra memory.
- **Integer Overflow in Multiplication:** In languages with fixed-width integers, $2 \times m_2$ can overflow if $m_2 > 2^{30}$. Use $m_1 / 2 \ge m_2$ or 64-bit integers.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single pass over $N$ elements tracking the two largest values: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 0.05$ ms for $N = 100$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (only scalar registers $m_1, m_2, idx$).
