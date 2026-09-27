# Guided Example: K-th Symbol in Grammar

We trace the step-by-step Thue-Morse substitution morphism ($0 \to 01, \; 1 \to 10$), binary prefix self-similarity ($Row_n = Row_{n-1} \cdot \overline{Row_{n-1}}$), divide-and-conquer half-interval branching ($k \le 2^{n-2}$ vs $k > 2^{n-2}$), recursive bit-flip reduction ($\oplus 1$), and closed-form Hamming weight parity equivalence ($\text{popcount}(k - 1) \bmod 2$) on representative grammar rows:

- **Input:** $n = 2, \quad k = 2$
- **Required output:** `1`
  - Grammar production rules:
    - Row 1 begins with a single symbol: `0`.
    - Every subsequent row is formed by replacing each symbol in the previous row:
      $$
      0 \implies 01
      $$
      $$
      1 \implies 10
      $$
    - The first few rows are:
      - Row 1: `0`
      - Row 2: `01`
      - Row 3: `0110`
      - Row 4: `01101001`
    - Objective: Find the $k$-th symbol (1-indexed) in Row $n$.
    - For $n = 2, k = 2$:
      - Row 2 is `01`.
      - Index 1 is `0`, Index 2 is `1`.
      - The 2nd symbol is **`1`**.
- **Thue-Morse Halving & Inversion Invariant:**
  - **The Prefix-Complement Decomposition:**
    - Notice the structural relationship of Row $n$ (having length $2^{n - 1}$):
      1. **Left Half ($1 \dots 2^{n - 2}$):** Identical copy of Row $n - 1$.
      2. **Right Half ($2^{n - 2} + 1 \dots 2^{n - 1}$):** Bitwise complement (NOT) of Row $n - 1$.
      $$
      Row_n = Row_{n - 1} \;||\; \overline{Row_{n - 1}}
      $$
  - **Divide-and-Conquer Recurrence:**
    - Let $mid = 2^{n - 2} = 1 \ll (n - 2)$ be the midpoint of Row $n$.
    - Base Case: When $n = 1$, the symbol is always `0`.
    - If $k \le mid$: The $k$-th symbol lies in the left half, so it equals the $k$-th symbol of Row $n - 1$:
      $$
      f(n, k) = f(n - 1, k)
      $$
    - If $k > mid$: The $k$-th symbol lies in the right half, so it is the **inverted complement** of the corresponding symbol in the left half:
      $$
      f(n, k) = f(n - 1, \; k - mid) \oplus 1
      $$
  - **Closed-Form Parity Property:**
    - The number of bit inversions between the root and position $k$ equals the number of `1` bits in the binary representation of $k - 1$:
      $$
      f(n, k) = \text{popcount}(k - 1) \pmod 2
      $$
- **Step-by-Step Worked Execution Trace on $n = 4, k = 5$:**
  - We trace a deeper example to showcase recursive descent: Row 4, 5th symbol.
  - **Level 1 ($n = 4, k = 5$):**
    - Midpoint: $mid = 2^{4 - 2} = 2^2 = \mathbf{4}$.
    - Test position:
      $$
      k > mid \iff 5 > 4 \implies \mathbf{Right\ Half\ (Bit\ Inversion!)}
      $$
    - Map to previous row:
      $$
      k' \leftarrow k - mid = 5 - 4 = \mathbf{1}
      $$
    - Recurrence:
      $$
      f(4, 5) = f(3, 1) \oplus 1
      $$
  - **Level 2 ($n = 3, k = 1$):**
    - Midpoint: $mid = 2^{3 - 2} = 2^1 = \mathbf{2}$.
    - Test position:
      $$
      k \le mid \iff 1 \le 2 \implies \mathbf{Left\ Half\ (Direct\ Copy)}
      $$
    - Recurrence:
      $$
      f(3, 1) = f(2, 1)
      $$
  - **Level 3 ($n = 2, k = 1$):**
    - Midpoint: $mid = 2^{2 - 2} = 2^0 = \mathbf{1}$.
    - Test position:
      $$
      k \le mid \iff 1 \le 1 \implies \mathbf{Left\ Half\ (Direct\ Copy)}
      $$
    - Recurrence:
      $$
      f(2, 1) = f(1, 1)
      $$
  - **Level 4 (Base Case $n = 1, k = 1$):**
    - Base case reached:
      $$
      f(1, 1) = \mathbf{0}
      $$
  - **Unwind and Flip:**
    - $f(2, 1) = 0$
    - $f(3, 1) = 0$
    - $f(4, 5) = f(3, 1) \oplus 1 = 0 \oplus 1 = \mathbf{1}$
  - **Verification via Bit Parity:**
    - Zero-indexed position: $k - 1 = 5 - 1 = 4 = (100)_2$.
    - Population count: $\text{popcount}(4) = 1$.
    - Parity: $1 \pmod 2 = \mathbf{1}$.
    - Exact match!
- **Trace on Sample 3 ($n = 2, k = 2$):**
  - $mid = 2^{2 - 2} = 1$.
  - $k = 2 > 1 \implies f(2, 2) = f(1, 2 - 1) \oplus 1 = f(1, 1) \oplus 1 = 0 \oplus 1 = \mathbf{1}$.
- **First Element of Any Row ($k = 1$):**
  - Always in the left half at every level.
  - Never inverted $\implies$ always **`0`**.

This instance demonstrates substitution dynamical systems (Thue-Morse sequence) and logarithmic binary search reduction, mathematically proves why binary reflected Gray code parity computes the $k$-th grammar symbol in $O(1)$ bitwise operations, and derives $O(N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given $n$ rows where Row 1 is `0`, and each subsequent row replaces `0 -> 01` and `1 -> 10`:
Find the $k$-th symbol in Row $n$.

```text
Row 1: 0
Row 2: 0 1
Row 3: 0 1 1 0
Row 4: 0 1 1 0 1 0 0 1

n = 2, k = 2:
  Row 2 is "01". The 2nd symbol is 1.

Result: 1
```

### The Invariant of the Complementary Second Half
- The first half of Row $n$ is an exact copy of Row $n - 1$.
- The second half of Row $n$ is the **bitwise complement** of Row $n - 1$.
- If $k \le 2^{n-2}$, recurse directly on $(n-1, k)$.
- If $k > 2^{n-2}$, recurse on $(n-1, k - 2^{n-2})$ and **flip the result** ($\oplus 1$).

---

## 2. Conceptual Foundation & Invariants

### 1. Recursive Halving Recurrence:
Let $mid = 2^{n - 2}$:
$$
f(n, k) = \begin{cases}
0 & n = 1 \\
f(n - 1, k) & k \le mid \\
f(n - 1, k - mid) \oplus 1 & k > mid
\end{cases}
$$

### 2. Thue-Morse Parity Theorem:
$$
f(n, k) = \text{popcount}(k - 1) \bmod 2
$$

> **Thue-Morse Fixed Point Invariant.** The infinite word generated by the substitution $0 \mapsto 01, 1 \mapsto 10$ is the unique fixed point of the Morse-Hedlund morphism, whose $m$-th letter (0-indexed) is the sum of digits of $m$ in base 2 modulo 2.

---

## 3. Step-by-Step Worked Execution

We trace $n = 2, k = 2$:

---

### Step 1: Midpoint
- $mid = 2^{2 - 2} = 1$.

---

### Step 2: Compare $k$ with $mid$
- $k = 2 > 1 \implies$ Second half.
- Flip required: $f(1, 2 - 1) \oplus 1 = f(1, 1) \oplus 1$.

---

### Step 3: Base Case
- $f(1, 1) = 0$.
- $0 \oplus 1 = \mathbf{1}$.

---

### Step 4: Output
$$
\mathbf{1}
$$

---

## 4. Complete Execution Trace

| Recursion Step | Row $n$ | Target Column $k$ | Midpoint $mid = 2^{n-2}$ | Half Region | Inversion Applied? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $2$ | $2$ | $1$ | Right ($k > 1$) | Yes ($\oplus 1$) |
| **$2$ (Base)** | **$1$** | **$1$** | **—** | **Base Case** | **Returns `0`** |
| **Final** | — | — | — | — | **$0 \oplus 1 = \mathbf{1}$** |

---

## 5. Boundary Cases & Failure Modes

- **Root Element ($n = 1, k = 1$):** Base case $\implies$ returns 0.
- **First Position in Any Row ($k = 1$):** Never enters the right half $\implies$ always 0.
- **Last Position in Row $n$ ($k = 2^{n - 1}$):** Enters the right half at every single step $\implies (n - 1) \bmod 2$.
- **Large Values of $N$ ($N = 30$):** Total length is $2^{29} \approx 5.3 \times 10^8$. Generating rows as strings causes Out of Memory. Recursion only takes $N$ steps ($\le 30$).

---

## 6. Traps & Common Anti-Patterns

- **Generating the Full String:** Constructing the $N$-th row explicitly consumes exponential memory ($O(2^N)$), instantly crashing when $N = 30$. You must compute the single target character mathematically without generating previous rows.
- **1-Indexed to 0-Indexed Bit Shifts:** In 1-indexed arithmetic, $mid = 2^{n - 2} = 1 \ll (n - 2)$. Ensure the bit shift exponent is $n - 2$, not $n - 1$.
- **Off-By-One on Popcount Formulation:** The 0-indexed position is $k - 1$, so the bit parity is `(k - 1).bit_count() % 2`, not `k.bit_count() % 2`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Each recursive call reduces $n$ by 1: $\mathcal{O}(N)$ calls.
  - Or via bitwise popcount: $\mathcal{O}(1)$ machine instruction.
  - Total Time: $\mathcal{O}(N)$ (or $\mathcal{O}(1)$) where $N \le 30$. Completes in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ call stack space for recursion (or $\mathcal{O}(1)$ iterative/bitwise).
