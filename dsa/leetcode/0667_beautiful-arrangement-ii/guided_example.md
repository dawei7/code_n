# Guided Example: Beautiful Arrangement II

We trace the step-by-step alternating zig-zag prefix construction ($1, n, 2, n-1, \dots$), distinct difference generation ($|a_{i+1} - a_i|$ spanning decreasing values), monotonic suffix stabilization (appending remaining numbers with uniform distance $1$), and exact $k$-difference permutation synthesis on representative integer ranges:

- **Input:** $n = 3, \quad k = 2$
- **Required output:** `[1, 3, 2]`
  - Mathematical problem statement:
    - Construct a permutation of integers from $1$ to $n$.
    - The sequence of adjacent absolute differences is:
      $$
      D = [|a_1 - a_2|, \; |a_2 - a_3|, \dots, |a_{n-1} - a_n|]
      $$
    - The set of distinct values in $D$ must have cardinality **exactly $k$**:
      $$
      |\text{distinct}(D)| = k
      $$
- **Zig-Zag Bipartition & Monotonic Suffix Invariant:**
  - **Generating $k - 1$ Distinct Large Differences:**
    - If you alternate between the smallest available number ($l$) and the largest available number ($r$), each bounce produces a unique difference:
      - Bounce 1: between $1$ and $n \implies |n - 1|$
      - Bounce 2: between $n$ and $2 \implies |n - 2|$
      - Bounce 3: between $2$ and $n - 1 \implies |n - 3|$
    - Each successive alternating step decrements the gap by exactly $1$, generating $k - 1$ unique differences:
      $$
      \{k, \; k - 1, \; k - 2, \dots, 2\}
      $$
  - **Stabilizing with Monotonic Fill (Difference $1$):**
    - Once $k$ elements have been placed in the zig-zag sequence, exactly $n - k$ numbers remain unplaced.
    - All remaining unplaced numbers form a contiguous numerical interval $[l, r]$.
    - By appending these remaining numbers in **strictly monotonic consecutive order** (either ascending $l \to r$ or descending $r \to l$ depending on parity):
      - Every adjacent pair in the suffix has difference:
        $$
        |x - (x \pm 1)| = \mathbf{1}
        $$
      - No new differences are introduced.
    - Total distinct differences across the entire array is **strictly $k$**!
- **Step-by-Step Worked Execution Trace on $n = 3, k = 2$:**
  - Available bounds:
    $$
    l = 1, \quad r = 3, \quad ans = []
    $$
  - **Phase 1: Build Alternating Prefix ($i = 0 \dots k - 1$):**
    - Range: $i \in [0, 1]$ ($k = 2$ steps).
    - **Step $i = 0$ (Even step $\implies$ take $l$):**
      - Append $l = 1$.
      - Advance left pointer: $l \leftarrow 1 + 1 = \mathbf{2}$.
      - $ans = [1]$.
    - **Step $i = 1$ (Odd step $\implies$ take $r$):**
      - Append $r = 3$.
      - Decrease right pointer: $r \leftarrow 3 - 1 = \mathbf{2}$.
      - $ans = [1, \; 3]$.
    - First difference formed:
      $$
      |1 - 3| = \mathbf{2}
      $$
  - **Phase 2: Monotonic Suffix Fill ($i = k \dots n - 1$):**
    - Remaining indices: $i = 2$.
    - Check parity of $k$:
      - $k = 2$ is **even**.
      - Because the last placed element was from the right pointer ($r = 3$), we continue placing from $r$ downwards to preserve order without gap jumps:
      - Append $r = 2$.
      - $r \leftarrow 2 - 1 = 1$.
      - $ans = [1, \; 3, \; \mathbf{2}]$.
    - Second difference formed:
      $$
      |3 - 2| = \mathbf{1}
      $$
  - **Step 3: Audit Output Permutation:**
    - Constructed array:
      $$
      ans = [\mathbf{1}, \; \mathbf{3}, \; \mathbf{2}]
      $$
    - Pairwise differences:
      - $|1 - 3| = 2$
      - $|3 - 2| = 1$
    - Distinct difference set:
      $$
      \{1, \; 2\} \implies \text{Count} = \mathbf{2} == k
      $$
    - Permutation is complete, valid, and contains exactly 2 distinct differences.
- **Minimum Difference Target ($n = 3, k = 1$):**
  - Prefix takes $l = 1$.
  - $k = 1$ is odd $\implies$ remaining elements appended ascending: $2, 3$.
  - Array: $[1, 2, 3]$.
  - Differences: $|1 - 2| = 1, |2 - 3| = 1 \implies \{1\}$ (Count $= 1$).
- **Maximum Difference Target ($n = 4, k = 3$):**
  - Alternating: $1, 4, 2, 3$.
  - Differences: $|1 - 4| = 3$, $|4 - 2| = 2$, $|2 - 3| = 1$.
  - Distinct: $\{3, 2, 1\}$ (Count $= 3$).

This instance demonstrates constructive combinatorial synthesis and two-pointer boundary alternating dynamics, mathematically proves why suffix monotonic closure prevents unintended difference collisions, and derives $O(N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given $n$ and $k$:
Construct a permutation of $1 \dots n$ whose adjacent differences have **exactly $k$ distinct values**.

```text
n = 3, k = 2

Construct:
  Phase 1 (Zig-Zag k elements):
    Step 0: pick l = 1 -> [ 1 ]
    Step 1: pick r = 3 -> [ 1, 3 ]   (difference |1-3| = 2)

  Phase 2 (Monotonic remaining):
    Step 2: pick remaining 2 -> [ 1, 3, 2 ] (difference |3-2| = 1)

Differences: [ 2, 1 ] -> exactly 2 distinct values!
Result: [ 1, 3, 2 ]
```

### The Invariant of the Controlled Difference Reservoir
- Alternating between $l$ and $r$ generates differences $k, k-1, k-2, \dots$ down to 2.
- Filling the remaining numbers monotonically adds difference 1 without creating any other differences.
- The total distinct differences is guaranteed to equal $k$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Two-Pointer Construction Protocol:
Initialize $l = 1, r = n$.
For $i = 0 \dots k - 1$:
- If $i$ is even: append $l$, $l \leftarrow l + 1$
- If $i$ is odd: append $r$, $r \leftarrow r - 1$

### 2. Suffix Monotonic Fill:
For $i = k \dots n - 1$:
- If $k$ is even: append $r$, $r \leftarrow r - 1$
- If $k$ is odd: append $l$, $l \leftarrow l + 1$

> **Combinatorial Difference Basis Invariant.** The alternating sequence $\{1, n, 2, n-1, \dots\}$ produces a strictly decreasing difference spectrum $D_j = n - j$, while the contiguous linear residual sequence contributes only difference $1$, forming a basis of size $k$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 3, k = 2$:

---

### Step 1: $i = 0$
- $l = 1, r = 3$.
- Append $l = 1$. $l \leftarrow 2$.
- $ans = [1]$.

---

### Step 2: $i = 1$
- Append $r = 3$. $r \leftarrow 2$.
- $ans = [1, 3]$.

---

### Step 3: $i = 2$ ($k = 2$ is even)
- Append $r = 2$.
- $ans = [1, 3, 2]$.

---

### Step 4: Verification
- Differences: $|1 - 3| = 2, |3 - 2| = 1$.
- Distinct differences: $\{1, 2\}$, size $= 2$.
- Return **`[1, 3, 2]`**.

---

## 4. Complete Execution Trace

| Position Placed | Pointer Used | Value Chosen | Array State After | Adjacent Difference Created | Distinct Differences So Far |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | Left ($l$) | $1$ | `[1]` | None (First element) | $\emptyset$ |
| $1$ | Right ($r$) | $3$ | `[1, 3]` | $\lvert 1 - 3 \rvert = \mathbf{2}$ | $\{2\}$ |
| **$2$** | **Residual Right ($r$)** | **$2$** | **`[1, 3, 2]`** | **$\lvert 3 - 2 \rvert = \mathbf{1}$** | **`{1, 2}` (Size 2)** |

---

## 5. Boundary Cases & Failure Modes

- **$k = 1$:** Entire array is monotonically increasing $[1, 2, 3 \dots n] \implies$ difference 1 only.
- **$k = n - 1$ (Maximum possible $k$):** Array alternates for all $n$ steps $\implies$ differences $\{n-1, n-2 \dots 1\}$.
- **Even vs Odd $k$:** Checking parity of $k$ determines whether the suffix must count upwards ($l \to r$) or downwards ($r \to l$).

---

## 6. Traps & Common Anti-Patterns

- **Wrong Suffix Direction:** If $k$ is even, the last element placed was from the right pointer $r$. Appending $l$ next creates a jump difference that can introduce a duplicate or unintended difference. The suffix direction must match the last alternating endpoint.
- **Permutation Invalidation (Reusing Numbers):** Using separate tracking variables for $l$ and $r$ guarantees every number from $1$ to $n$ is used exactly once.
- **Backtracking / Brute Force ($O(N!)$):** Generating all permutations causes Time Limit Exceeded; the constructive two-pointer approach builds the answer directly in $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single loop running from $0$ to $n - 1$: $\mathcal{O}(N)$.
  - Each step does $\mathcal{O}(1)$ pointer updates and appends.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 1$ ms for $N = 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the constructed output permutation.
