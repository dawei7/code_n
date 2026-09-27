# Guided Example: Valid Perfect Square

We trace the step-by-step monotonic interval bisection ($[L, R] = [1, num]$), quadratic midpoint probing ($M^2$ vs $num$), boundary contraction, and integer square verification ($L^2 == num$) on representative numerical instances:

- **Input:** $num = 16$
- **Required output:** `true`
  - Search range: $[1, 16]$
  - Iteration 1: $M = 1 + \lfloor(16 - 1)/2\rfloor = 8 \implies 8^2 = 64 > 16 \implies$ eliminate right half, $R = 7$
  - Iteration 2: $M = 1 + \lfloor(7 - 1)/2\rfloor = 4 \implies 4^2 = 16 == 16 \implies \mathbf{\text{Match found!}}$
  - Result: `true`
- **Non-Square Counterexample:** $num = 14$
  - Search narrows between $3^2 = 9 < 14$ and $4^2 = 16 > 14$
  - No integer root exists $\implies \text{false}$
- **Unit Base Case:** $num = 1 \implies 1^2 = 1 \implies \text{true}$
- **Upper Constraint Bound:** $num = 2^{31} - 1 \approx 2.14 \times 10^9 \implies$ binary search converges in at most $31$ steps

This instance demonstrates logarithmic range reduction on monotonically increasing integer polynomials ($f(x) = x^2$), proves why integer bisection avoids floating-point precision hazards without using `sqrt`, and establishes $O(\log N)$ time and $O(1)$ space complexity.

---

## 1. Instance & Teaching Goal

Given a positive integer $num = 16$:
Determine whether $num$ is a **perfect square** (i.e. there exists an integer $x \ge 1$ such that $x^2 = num$) without using built-in library functions like `sqrt`:

```text
Search Space: Integers x in [1, 16]
Function: f(x) = x^2 (Strictly Monotonically Increasing)

Probe 1: x = 8 -> 8^2 = 64 > 16  (x is too large! R = 7)
Probe 2: x = 4 -> 4^2 = 16 == 16 (Exact match! Return true)
```

### Why Linear Search ($O(\sqrt{N})$) is Suboptimal
- Incrementing $x = 1, 2, 3 \dots$ until $x^2 \ge num$ requires up to $\sqrt{2^{31}-1} \approx 46,340$ operations.
- Because $f(x) = x^2$ is strictly increasing for $x > 0$, binary search halves the interval on every step, converging in $\le \log_2(2^{31}) \approx 31$ iterations ($O(\log N)$).

---

## 2. Conceptual Foundation & Invariants

### 1. Bisection Framework
Initialize interval boundaries:
$$
L = 1, \quad R = num
$$
While $L \le R$:
1. Calculate integer midpoint:
   $$
   M = L + \left\lfloor \frac{R - L}{2} \right\rfloor
   $$
2. Evaluate quadratic square:
   $$
   P = M \times M
   $$
3. Branch according to order:
   - If $P == num$: return **`True`** (Perfect square confirmed).
   - If $P < num$: discard left half $\implies L \leftarrow M + 1$.
   - If $P > num$: discard right half $\implies R \leftarrow M - 1$.
4. If $L > R$, no integer square root exists $\implies$ return **`False`**.

### 2. Functional Bisection Equivalent
Using `bisect_left` on `range(1, num + 1)` with key $x \mapsto x^2$:
$$
l = \text{bisect\_left}(\dots) + 1
$$
$$
\text{return } l \times l == num
$$

> **Invariant.** If an integer $x$ exists such that $x^2 = num$, it is strictly guaranteed to lie within the current search window $[L, R]$.

---

## 3. Step-by-Step Worked Execution

We trace $num = 16$:

---

### Step 1: Initial Bounds Setup
- Range: $L = 1, R = 16$.
- Compute midpoint:
  $$
  M = 1 + \left\lfloor \frac{16 - 1}{2} \right\rfloor = 1 + 7 = \mathbf{8}
  $$
- Evaluate square:
  $$
  P = 8^2 = \mathbf{64}
  $$
- Compare: $64 > 16$. Midpoint is strictly too large.
- Contract upper bound:
  $$
  R \leftarrow 8 - 1 = \mathbf{7}
  $$
- New active range: $[1, 7]$.

---

### Step 2: Second Bisection Step
- Range: $L = 1, R = 7$.
- Compute midpoint:
  $$
  M = 1 + \left\lfloor \frac{7 - 1}{2} \right\rfloor = 1 + 3 = \mathbf{4}
  $$
- Evaluate square:
  $$
  P = 4^2 = \mathbf{16}
  $$
- Compare:
  $$
  P == num \iff 16 == 16 \implies \mathbf{\text{True}}
  $$
- Perfect square verified with integer root $x = 4$!
- Return: **`true`**.

---

## 4. Complete Execution Trace

```text
num = 16
Initial: L = 1, R = 16

Iteration 1:
  L = 1, R = 16 -> M = 8
  M^2 = 64 > 16 -> eliminate [8, 16] -> R = 7

Iteration 2:
  L = 1, R = 7  -> M = 4
  M^2 = 16 == 16 -> EXACT SQUARE FOUND! -> Return True
```

| Iteration | Search Window $[L, R]$ | Midpoint $M$ | Evaluated Square $M^2$ | Comparison vs $num = 16$ | Action Taken | Next Window |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $[1, 16]$ | 8 | 64 | $64 > 16$ | $R \leftarrow 8 - 1 = 7$ | $[1, 7]$ |
| **2** | **$[1, 7]$** | **4** | **16** | **$16 == 16$** | **Exact match found!** | **`true` (Output)** |

---

### Comparison: Non-Square Trace ($num = 14$)

```text
num = 14, L = 1, R = 14
Iter 1: M = 7 -> 7^2 = 49 > 14 -> R = 6
Iter 2: M = 3 -> 3^2 =  9 < 14 -> L = 4
Iter 3: M = 5 -> 5^2 = 25 > 14 -> R = 4
Iter 4: M = 4 -> 4^2 = 16 > 14 -> R = 3
L = 4 > R = 3 -> Terminate -> Return False
```

| Iteration | Window $[L, R]$ | Midpoint $M$ | $M^2$ | vs $14$ | Action Taken | Next Window |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $[1, 14]$ | 7 | 49 | $> 14$ | $R \leftarrow 6$ | $[1, 6]$ |
| 2 | $[1, 6]$ | 3 | 9 | $< 14$ | $L \leftarrow 4$ | $[4, 6]$ |
| 3 | $[4, 6]$ | 5 | 25 | $> 14$ | $R \leftarrow 4$ | $[4, 4]$ |
| 4 | $[4, 4]$ | 4 | 16 | $> 14$ | $R \leftarrow 3$ | $[4, 3]$ |
| **Exit** | $[4, 3]$ | - | - | $L > R$ | **No integer root** | **`false`** |

---

## 5. Algorithmic Correctness

**Soundness.** If $M^2 == num$, then $M$ is an integer whose square is $num$, satisfying the exact definition of a perfect square. Because $f(x) = x^2$ is strictly increasing on $x > 0$, any $x \ge M$ will have $x^2 > M^2 > num$, so discarding $[M, R]$ when $M^2 > num$ cannot eliminate any potential root. Likewise, discarding $[L, M]$ when $M^2 < num$ is mathematically sound.

**Completeness.** At each step, the search interval size is halved: $|R - L + 1| \to \lfloor |R - L + 1| / 2 \rfloor$. The loop terminates in at most $\lceil \log_2(num) \rceil + 1$ iterations. If an integer root exists in $[1, num]$, it is guaranteed to be probed.

---

## 6. Traps This Instance Exposes

- **Integer Overflow in 32-bit Languages:** In C++ or Java, computing `M * M` when $M = 2^{30}$ causes 32-bit signed integer overflow. Casting to 64-bit integer (`long long`) or testing `M > num / M` prevents overflow. (Python handles arbitrary-precision integers automatically).
- **Floating-Point Precision Loss:** Relying on `int(sqrt(num)) ** 2 == num` can fail on large 64-bit integers due to IEEE 754 double precision rounding errors. Integer binary search is exact.
- **Midpoint Formula Overflow:** Writing `(L + R) // 2` can overflow in fixed-width arithmetic. Writing `L + (R - L) // 2` is universally safe.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$, where $N = num$. The search space is bounded by $num \le 2^{31} - 1$. Each iteration performs $O(1)$ arithmetic operations, executing at most $\approx 31$ iterations.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, storing only scalar boundary integers.