# Guided Example: Binary Number with Alternating Bits

We trace the step-by-step binary bitwise extraction ($curr = n \& 1$), adjacent bit equality comparison ($curr == prev$), bitwise right-shift progression ($n \leftarrow n \gg 1$), algebraic shift-XOR all-ones property ($n \oplus (n \gg 1) = 2^m - 1$), and boolean alternation validation on representative positive integers:

- **Input:** $n = 5$
- **Required output:** `true`
  - Alternating bits definition:
    - In the binary representation of $n$, no two adjacent bits may have the same value.
    - Every 0 must be flanked by 1s, and every 1 must be flanked by 0s.
    - Binary expansion of $n = 5$:
      $$
      5 = 101_2
      $$
    - Adjacent pairs:
      - Pair $(b_0, b_1) = (1, 0) \implies \text{different}$
      - Pair $(b_1, b_2) = (0, 1) \implies \text{different}$
    - Every adjacent bit pair alternates. Return **`true`**.
- **Bitwise Stream Extraction & Shift-XOR Invariant:**
  - **Sequential Least-Significant-Bit (LSB) Extraction:**
    - At each step, inspect the least significant bit:
      $$
      curr = n \ \& \ 1
      $$
    - If $curr$ matches the previous bit ($curr == prev$), an adjacent identical pair has been discovered $\implies$ return **`false`**.
    - Otherwise, update $prev \leftarrow curr$ and shift the integer right by one bit:
      $$
      n \leftarrow n \gg 1
      $$
    - If the number reduces to 0 without encountering equal adjacent bits, the bits alternate completely $\implies$ return **`true`**.
  - **The Shift-XOR All-Ones Property ($O(1)$ Formulation):**
    - If $n$ has alternating bits ($10101\dots_2$ or $1010\dots_2$):
      - Shifting $n$ right by 1 bit swaps the parity of every position.
      - Bitwise XOR between $n$ and $n \gg 1$ produces a solid sequence of $1$s:
        $$
        x = n \oplus (n \gg 1) = \underbrace{111\dots 1_2}_{m \text{ ones}} = 2^m - 1
        $$
      - Adding 1 flips all bits to zero with a single high carry: $x + 1 = 1000\dots 0_2$.
      - Bitwise AND evaluates to zero:
        $$
        x \ \& \ (x + 1) == 0
        $$
- **Step-by-Step Worked Execution Trace on $n = 5$ ($101_2$):**
  - Initial state:
    $$
    n = 5, \quad prev = -1
    $$
  - **Iteration 1 ($n = 5$):**
    - Binary value: $n = 101_2$.
    - Extract LSB:
      $$
      curr = 5 \ \& \ 1 = \mathbf{1}
      $$
    - Compare with previous bit:
      $$
      prev = -1 \ne curr = 1 \quad \mathbf{(Initial\ Bit\ Accepted)}
      $$
    - Update previous: $prev \leftarrow 1$.
    - Right shift:
      $$
      n \leftarrow 5 \gg 1 = \lfloor 5 / 2 \rfloor = \mathbf{2} \quad (10_2)
      $$
  - **Iteration 2 ($n = 2$):**
    - Binary value: $n = 10_2$.
    - Extract LSB:
      $$
      curr = 2 \ \& \ 1 = \mathbf{0}
      $$
    - Compare with previous bit:
      $$
      prev = 1 \ne curr = 0 \quad \mathbf{(Alternation\ Maintained!)}
      $$
    - Update previous: $prev \leftarrow 0$.
    - Right shift:
      $$
      n \leftarrow 2 \gg 1 = \lfloor 2 / 2 \rfloor = \mathbf{1} \quad (1_2)
      $$
  - **Iteration 3 ($n = 1$):**
    - Binary value: $n = 1_2$.
    - Extract LSB:
      $$
      curr = 1 \ \& \ 1 = \mathbf{1}
      $$
    - Compare with previous bit:
      $$
      prev = 0 \ne curr = 1 \quad \mathbf{(Alternation\ Maintained!)}
      $$
    - Update previous: $prev \leftarrow 1$.
    - Right shift:
      $$
      n \leftarrow 1 \gg 1 = \mathbf{0}
      $$
  - **Termination ($n = 0$):**
    - Integer completely processed with zero violations.
    - Return **`true`**.
- **Failure Trace on Consecutive Bits ($n = 7$, $111_2$):**
    - Iteration 1: $curr = 1, prev \leftarrow 1, n \leftarrow 3$.
    - Iteration 2: $curr = 3 \& 1 = \mathbf{1}$.
      - Compare: $curr = 1 == prev = 1 \implies \mathbf{Identical\ Adjacent\ Bits!}$
      - Immediate early termination $\implies$ Returns **`false`**.
- **Low-Bit Violation Trace ($n = 11$, $1011_2$):**
    - Iteration 1: $11 \& 1 = 1, prev \leftarrow 1, n \leftarrow 5$.
    - Iteration 2: $5 \& 1 = 1$.
      - Compare: $curr = 1 == prev = 1 \implies \mathbf{Identical\ Adjacent\ Bits!}$
      - Returns **`false`**.

This instance demonstrates binary radix digit extraction and bit-level regular language recognition, mathematically proves why shift-XOR transforms alternating binary words into Mersenne numbers, and derives $O(\log N)$ (or $O(1)$ algebraic) runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a positive integer $n$:
Determine if its binary representation has **strictly alternating bits** (no two adjacent bits are equal).

```text
n = 5 in binary: 1 0 1

Adjacent pairs:
  Bit 0 and Bit 1: 1 and 0 (different)
  Bit 1 and Bit 2: 0 and 1 (different)

Result: true
```

### The Invariant of Bit Alternation
- In an alternating binary string, each bit must strictly differ from its predecessor:
  $$
  b_i \ne b_{i+1} \quad \forall i
  $$
- This can be verified either by extracting bits one-by-one or checking if $x = n \oplus (n \gg 1)$ satisfies $x \& (x + 1) == 0$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Iterative Extraction Rule:
Initialize $prev = -1$.
While $n > 0$:
$$
curr = n \ \& \ 1
$$
$$
\text{If } curr == prev \implies \text{return } \mathbf{False}
$$
$$
prev \leftarrow curr, \quad n \leftarrow n \gg 1
$$
$$
\text{return } \mathbf{True}
$$

### 2. Algebraic Identity:
A number has alternating bits if and only if:
$$
(n \oplus (n \gg 1)) + 1 = 2^{\lfloor \log_2 n \rfloor + 1}
$$

> **Mersenne Projection Invariant.** The difference operator $\Delta b_i = b_i \oplus b_{i-1}$ maps the language of alternating binary words $(10)^*1$ or $(10)^*$ bijectively to the set of solid Mersenne blocks $\{2^k - 1 \mid k \in \mathbb{N}\}$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 5$ ($101_2$):

---

### Step 1: Bit 0
- $curr = 5 \& 1 = 1$.
- $prev = -1 \ne 1 \implies prev \leftarrow 1, n \leftarrow 2$.

---

### Step 2: Bit 1
- $curr = 2 \& 1 = 0$.
- $prev = 1 \ne 0 \implies prev \leftarrow 0, n \leftarrow 1$.

---

### Step 3: Bit 2
- $curr = 1 \& 1 = 1$.
- $prev = 0 \ne 1 \implies prev \leftarrow 1, n \leftarrow 0$.

---

### Step 4: Output
- Loop finishes $\implies \mathbf{true}$.

---

## 4. Complete Execution Trace

| Iteration | Remaining $n$ | Binary String | Extracted Bit $curr$ | Previous Bit $prev$ | Condition $curr == prev$? | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $5$ | `101` | $1$ | $-1$ | No | $prev \leftarrow 1, n \leftarrow 2$ |
| $2$ | $2$ | `10` | $0$ | $1$ | No | $prev \leftarrow 0, n \leftarrow 1$ |
| $3$ | $1$ | `1` | $1$ | $0$ | No | $prev \leftarrow 1, n \leftarrow 0$ |
| **End** | **$0$** | — | — | — | — | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **$n = 1$ ($1_2$):** Single bit, trivially alternating $\implies$ returns `true`.
- **$n = 2$ ($10_2$):** $1$ and $0 \implies$ returns `true`.
- **$n = 3$ ($11_2$):** $1$ and $1 \implies$ returns `false`.
- **Powers of Two ($n = 4$, $100_2$):** Contains consecutive zeros `00` $\implies$ returns `false`.

---

## 6. Traps & Common Anti-Patterns

- **Converting to String (`bin(n)`):** String conversion allocates character memory; bitwise operations run directly in CPU registers without allocation.
- **Off-By-One Initialization:** Initializing $prev$ to 0 causes false rejections when the first bit is 0. Use $-1$ as the empty sentinel.
- **Forgetting Right Shift:** Forgetting $n \gg= 1$ leads to an infinite loop.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Loop runs at most $\lfloor \log_2 n \rfloor + 1$ times.
  - Since $n \le 2^{31} - 1$, loop runs at most 31 iterations.
  - Each iteration performs $\mathcal{O}(1)$ bitwise operations.
  - Total Time: strictly $\mathcal{O}(\log n) \le 31$ operations, completing in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space (two integer variables $curr$ and $prev$).
