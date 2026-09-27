# Guided Example: Sqrt(x)

We trace the step-by-step execution of monotonic bisection search and Newton's method on representative integer instances:

- **Non-Square Integer:** $x = 8 \implies 2$ (since $\lfloor \sqrt{8} \rfloor = \lfloor 2.8284 \dots \rfloor = 2$)
- **Perfect Square:** $x = 4 \implies 2$
- **Boundary Base Case:** $x = 0 \implies 0$

This instance demonstrates binary search over a discrete monotonic mathematical domain ($m \mapsto m^2$), preventing 32-bit integer overflow via division ($M \le x / M$), and integer floor convergence.

---

## 1. Instance & Teaching Goal

Given a non-negative integer $x = 8$, compute and return the square root of $x$ rounded down to the nearest integer ($\lfloor \sqrt{x} \rfloor$). The built-in exponent function or operator (such as `pow(x, 0.5)` or `x ** 0.5`) must not be used.

For $x = 8$:
- $2^2 = 4 \le 8$
- $3^2 = 9 > 8$
The largest integer whose square does not exceed $8$ is $2$.

A linear scan from $1$ upward takes $O(\sqrt{x})$ time, which requires over $46{,}340$ operations when $x \approx 2^{31} - 1$. Because $f(m) = m^2$ is strictly monotonically increasing for $m \ge 0$, binary search determines $\lfloor \sqrt{x} \rfloor$ in $O(\log x)$ time (at most $\approx 31$ iterations).

---

## 2. Conceptual Foundation & Invariants

### Monotonic Bisection Predicate
Let $x \ge 1$. The integer square root must lie within range $[1, x]$ (or $[1, \lfloor x / 2 \rfloor]$ for $x \ge 4$).
At midpoint $M = L + \lfloor (R - L) / 2 \rfloor$:
- If $M \times M == x$: exact square root discovered. Return $M$.
- If $M \times M < x$: $M$ is a valid candidate for the integer floor. Record $\text{ans} \leftarrow M$, and search right:
  $$
  L \leftarrow M + 1
  $$
- If $M \times M > x$: $M$ is strictly too large. Eliminate right half:
  $$
  R \leftarrow M - 1
  $$

### Avoiding Integer Overflow
In 32-bit typed systems, computing $M \times M$ when $M \approx 2^{16}$ overflows the 32-bit signed integer limit ($2^{31}-1 = 2{,}147{,}483{,}647$).
Using division:
$$
M \le \lfloor x / M \rfloor
$$
is mathematically equivalent to $M^2 \le x$ while remaining entirely within 32-bit arithmetic.

> **Invariant.** Throughout the search, $\text{ans}^2 \le x$, and any value strictly greater than $R$ satisfies value$^2 > x$. When $L > R$, $R$ is identical to $\text{ans}$.

---

## 3. Step-by-Step Worked Execution

We trace $x = 8$:

### Initialization
- Edge case: $x < 2$ returns $x$ directly.
- Search bounds: $L = 1, R = \lfloor 8 / 2 \rfloor = 4$.
- Recorded candidate: $\text{ans} = 1$.

---

### Step 1 ($L = 1, R = 4$)
- Midpoint: $M = 1 + \lfloor (4 - 1) / 2 \rfloor = 2$.
- Square evaluation: $M^2 = 2 \times 2 = 4$.
- Compare: $4 \le 8$. Candidate valid!
- Update: $\text{ans} \leftarrow 2$.
- Shift search right: $L \leftarrow M + 1 = 3$.
- Active interval: $[3, 4]$.

---

### Step 2 ($L = 3, R = 4$)
- Midpoint: $M = 3 + \lfloor (4 - 3) / 2 \rfloor = 3$.
- Square evaluation: $M^2 = 3 \times 3 = 9$.
- Compare: $9 > 8$. Too large!
- Shift search left: $R \leftarrow M - 1 = 2$.
- Active interval: $[3, 2]$.

---

### Step 3: Termination
- Boundary cross: $L = 3 > R = 2$.
- Loop terminates.
- Emitted output: $\text{ans} = 2$ (or returning $R = 2$).

---

## 4. Complete Execution Trace

| Iteration | Left $L$ | Right $R$ | Midpoint $M$ | $M^2$ | $M^2 \le 8$? | Recorded $\text{ans}$ | Boundary Adjustment |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 1 | 4 | 2 | 4 | **Yes ($4 \le 8$)** | **2** | Search right: $L \leftarrow 3$ |
| 2 | 3 | 4 | 3 | 9 | No ($9 > 8$) | 2 | Search left: $R \leftarrow 2$ |
| Terminal | 3 | **2** | - | - | $L > R$ | **2** | **Exit with $R = 2$** |

### Newton-Raphson Alternative Trace ($x = 8$)
Starting from $r_0 = 8$:
$$
r_{k+1} = \left\lfloor \frac{1}{2} \left( r_k + \frac{x}{r_k} \right) \right\rfloor
$$
- $r_1 = \lfloor \frac{1}{2}(8 + 8/8) \rfloor = \lfloor \frac{9}{2} \rfloor = 4$
- $r_2 = \lfloor \frac{1}{2}(4 + 8/4) \rfloor = \lfloor \frac{6}{2} \rfloor = 3$
- $r_3 = \lfloor \frac{1}{2}(3 + 8/3) \rfloor = \lfloor \frac{5}{2} \rfloor = 2$
- $r_4 = \lfloor \frac{1}{2}(2 + 8/2) \rfloor = \lfloor \frac{6}{2} \rfloor = 3 > 2 \implies$ Halt at $2$!

The same four iterations written as a table show why halting on the first non-decreasing step is safe:

| Iteration $k$ | $r_k$ | $x / r_k$ | $\frac{1}{2}\left(r_k + x/r_k\right)$ | $r_{k+1} = \lfloor \cdot \rfloor$ | Still decreasing? |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 8 | 1 | $4.5$ | 4 | yes |
| 1 | 4 | 2 | $3$ | 3 | yes |
| 2 | 3 | $8/3 \approx 2.667$ | $17/6 \approx 2.833$ | 2 | yes |
| 3 | 2 | 4 | $3$ | 3 | **no — sequence turns upward** |

For $x > 0$ and $r_k \ge 1$, the arithmetic mean $\frac{1}{2}(r_k + x/r_k)$ is at least $\sqrt{x}$ by the AM–GM inequality, so the iteration can only descend toward $\sqrt{x}$ and then oscillate in the pair $\{2, 3\}$ here. That is why the answer is taken as the last value before the increase, namely $r_3 = 2$.

---

## 5. Algorithmic Correctness

**Soundness.** Because $M^2$ increases strictly monotonically with $M > 0$, any $M$ satisfying $M^2 > x$ guarantees that all integers $k \ge M$ also satisfy $k^2 > x$. Thus, eliminating the right half upon $M^2 > x$ discards only strictly impossible candidates.

**Completeness.** The search interval $[L, R]$ halves in size each iteration. When $L > R$, the boundary pointer $R$ sits at the exact mathematical threshold $\max \{m \in \mathbb{Z} \mid m^2 \le x\}$.

---

## 6. Traps This Instance Exposes

- **Integer Multiplication Overflow:** Writing `M * M <= x` causes overflow when $M \ge 46341$ in 32-bit signed integers. Writing `M <= x // M` or using 64-bit arithmetic avoids overflow.
- **Base Case $x = 0$ and $x = 1$:** When $x = 0$, $L = 1$ would fail division by zero. Handling $x < 2$ returning $x$ upfront ensures division is never called with $M = 0$.
- **Returning $L$ vs Returning $R$:** When the loop exits with $L > R$, $L$ is the first value whose square exceeds $x$, while $R$ is the greatest value whose square is $\le x$. Returning $R$ (or the recorded candidate $\text{ans}$) is required.

The bracket $[\,m^2 \le x < (m+1)^2\,]$ pins the answer for every boundary in the case set:

| Instance | $x$ | $\lfloor \sqrt{x} \rfloor$ | $m^2$ | $(m+1)^2$ | Why the guard or predicate settles it |
|:---|:---:|:---:|:---:|:---:|:---|
| Zero boundary | 0 | 0 | 0 | 1 | The $x < 2$ guard returns $x$ directly, so no midpoint of $0$ is ever used as a divisor. |
| One boundary | 1 | 1 | 1 | 4 | Same guard; the interval $[1, 1]$ would otherwise be reached with $L = 1, R = 1$. |
| Perfect square | 4 | 2 | 4 | 9 | The predicate confirms $M^2 = x$ exactly rather than merely bounding it. |
| Floor case (main trace) | 8 | 2 | 4 | 9 | $2.8284\dots$ truncates to $2$; $9 > 8$ eliminates every $m \ge 3$. |
| Near 32-bit maximum | 2147395599 | 46339 | 2147302921 | 2147395600 | The successor already exceeds $x$ by $1$, and early midpoints are far above $46341$, so the division test is what keeps 32-bit arithmetic safe. |

Row 5 is the one that justifies the division form: a midpoint such as $\lfloor (x+1)/2 \rfloor$ would square far beyond $2^{31} - 1 = 2147483647$, whereas comparing $M$ against $\lfloor x / M \rfloor$ stays inside the same 32-bit range for every midpoint.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log x)$. The search interval has size $x / 2$, which is halved at each step, taking at most $\approx 31$ iterations for any 32-bit non-negative integer.
- **Auxiliary Space Complexity:** $O(1)$. Memory consumption is strictly constant.
