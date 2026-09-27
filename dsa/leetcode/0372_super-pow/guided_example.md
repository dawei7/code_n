# Guided Example: Super Pow

We trace the step-by-step place-value decimal exponent decomposition ($B = \sum d_i \cdot 10^i$), reverse digit streaming (`b[::-1]`), modular place-base upgrading ($a \leftarrow a^{10} \pmod{1337}$), and accumulator multiplication on representative large exponent arrays:

- **Input:** $a = 2, \quad b = [1, 0]$
- **Required output:** $1024$
  - Exponent digits: $b = [1, 0] \implies B = 10$
  - Target value: $2^{10} \pmod{1337} = 1024 \pmod{1337} = \mathbf{1024}$
  - Reverse place-value traversal (`b[::-1] = [0, 1]`):
    - Units place ($e = 0$):
      - Term: $2^0 \pmod{1337} = 1$
      - Cumulative answer: $ans = 1 \times 1 = 1$
      - Upgrade base to tens place: $a \leftarrow 2^{10} \pmod{1337} = 1024$
    - Tens place ($e = 1$):
      - Term: $1024^1 \pmod{1337} = 1024$
      - Cumulative answer: $ans = 1 \times 1024 = \mathbf{1024}$
      - Upgrade base: $a \leftarrow 1024^{10} \pmod{1337}$
  - Final result: $\mathbf{1024}$
- **Single-Digit Base Case:** $a = 2, b = [3] \implies 2^3 = 8$
- **Identity Base:** $a = 1, b = [4, 3, 3, 8, 5, 2] \implies 1^{433852} = 1$
- **Large Modulo Wraparound:** $a = 2147483647, b = [2, 0, 0] \implies$ intermediate bases reduced modulo $1337$ prevent integer overflow

This instance demonstrates modular exponentiation over arbitrary-length decimal arrays, mathematically proves why factoring $a^B = \prod (a^{10^i})^{d_i}$ reduces array exponentiation to $O(D)$ bounded modular multiplications, and eliminates the need to instantiate giant integer values.

---

## 1. Instance & Teaching Goal

Given an integer $a = 2$ and an extremely large positive integer exponent $b = [1, 0]$ represented as an array of decimal digits:
Compute $a^b \pmod{1337}$:
$$
2^{10} \pmod{1337} = 1024 \pmod{1337} = 1024
$$

```text
Decimal Expansion of Exponent b = [1, 0]:
  Value B = 1 * 10^1 + 0 * 10^0 = 10

Exponent Product Property:
  a^B = a^(d_1 * 10^1 + d_0 * 10^0)
      = (a^(10^0))^d_0  *  (a^(10^1))^d_1

For a = 2, b = [1, 0]:
  Units place (d_0 = 0): (2^1)^0   = 1
  Tens place  (d_1 = 1): (2^10)^1  = 1024

Product: 1 * 1024 = 1024 (mod 1337)
```

### Eliminating BigInteger Construction
In many languages (and in hardware), an array of 2,000 digits cannot be parsed into a standard 64-bit integer.
- By treating $b$ as a polynomial in base 10:
  $$
  B = d_0 + 10 \cdot d_1 + 100 \cdot d_2 + \dots
  $$
- We process digits from right to left (least significant to most significant):
  - In each step, multiply $ans$ by $(a_{\text{current}})^{d_i} \pmod{1337}$.
  - Then update the base for the next higher decimal place: $a_{\text{current}} \leftarrow (a_{\text{current}})^{10} \pmod{1337}$.
- Every intermediate number is kept strictly below $1337$, executing entirely in bounded arithmetic.

---

## 2. Conceptual Foundation & Invariants

### 1. State Variables:
- `mod = 1337`: The fixed modulus.
- `ans = 1`: The cumulative product accumulator.
- `a`: Current base corresponding to $a^{10^p} \pmod{1337}$ at decimal place $p$.

### 2. Transition Protocol for each digit $e \in b[::-1]$:
1. Multiply accumulated answer by the contribution of digit $e$:
   $$
   ans \leftarrow \big(ans \times (a^e \bmod mod)\big) \bmod mod
   $$
2. Upgrade base for the next decimal place (power of 10):
   $$
   a \leftarrow (a^{10} \bmod mod)
   $$

### 3. Modulo Multiplicative Homomorphism:
$$
(X \times Y) \pmod M = \big((X \bmod M) \times (Y \bmod M)\big) \pmod M
$$
This ensures that reducing modulo $1337$ after every step produces the exact same remainder as reducing at the end.

> **Invariant.** After processing the first $k$ digits from the right, `ans` is congruent to $a$ raised to the integer formed by the lowest $k$ digits of $b$, and `a` holds $a^{10^k} \pmod{1337}$.

---

## 3. Step-by-Step Worked Execution

We trace $a = 2, b = [1, 0]$ with $mod = 1337$:
Initial state: $ans = 1, a = 2$.
Reversed digits: $b[::-1] = [0, 1]$.

---

### Step 1: Units Place ($e = 0$)
- Read least significant digit: $e = 0$.
- Compute digit term:
  $$
  \text{term} = 2^0 \pmod{1337} = \mathbf{1}
  $$
- Accumulate:
  $$
  ans \leftarrow (1 \times 1) \pmod{1337} = \mathbf{1}
  $$
- Upgrade base for tens place:
  $$
  a \leftarrow 2^{10} \pmod{1337} = 1024 \pmod{1337} = \mathbf{1024}
  $$
- State after units place: $ans = 1, a = 1024$.

---

### Step 2: Tens Place ($e = 1$)
- Read next digit: $e = 1$.
- Compute digit term:
  $$
  \text{term} = 1024^1 \pmod{1337} = \mathbf{1024}
  $$
- Accumulate:
  $$
  ans \leftarrow (1 \times 1024) \pmod{1337} = \mathbf{1024}
  $$
- Upgrade base for hundreds place:
  $$
  a \leftarrow 1024^{10} \pmod{1337}
  $$
- Exponent array exhausted! While loop terminates.

---

### Step 3: Final Output
Cumulative remainder:
$$
\mathbf{1024}
$$

---

## 4. Complete Execution Trace

```text
a = 2, b = [1, 0] (mod 1337)
Reversed digits: [0, 1]

Iteration 1 (e = 0):
  term = pow(2, 0, 1337) = 1
  ans  = (1 * 1) % 1337  = 1
  a    = pow(2, 10, 1337) = 1024

Iteration 2 (e = 1):
  term = pow(1024, 1, 1337) = 1024
  ans  = (1 * 1024) % 1337  = 1024
  a    = pow(1024, 10, 1337)

Final Result: 1024
```

| Iteration | Exponent Digit $e$ | Decimal Place Value | Current Base $a$ | Digit Term $a^e \pmod{1337}$ | Updated Accumulator `ans` | Next Base $a^{10} \pmod{1337}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Init | - | - | 2 | - | 1 | - |
| 1 | 0 | Units ($10^0$) | 2 | $2^0 = 1$ | $1 \times 1 = \mathbf{1}$ | $2^{10} = \mathbf{1024}$ |
| **2** | **1** | **Tens ($10^1$)** | **1024** | **$1024^1 = 1024$** | **$1 \times 1024 = \mathbf{1024}$** | **$1024^{10} \pmod{1337}$** |
| **Exit** | - | - | - | - | **`1024` (Final)** | - |

---

## 5. Algorithmic Correctness

**Soundness.** Any non-negative integer $B$ with decimal digits $[d_{k-1}, \dots, d_0]$ equals $\sum_{i=0}^{k-1} d_i \cdot 10^i$. By exponent arithmetic, $a^B = \prod_{i=0}^{k-1} (a^{10^i})^{d_i}$. At iteration $i$, the variable $a$ holds $a^{10^i} \pmod{mod}$. Raising $a$ to power $d_i$ and multiplying into `ans` directly computes that factor. By the ring properties of $\mathbb{Z} / 1337\mathbb{Z}$, performing modular reductions at each multiplication preserves the exact algebraic result.

**Completeness.** Every digit in $b$ is processed from least to most significant. Because $d_i \in [0, 9]$, each digit exponentiation `pow(a, e, mod)` performs at most $\approx 4$ multiplications (via binary exponentiation), ensuring no precision is lost and every place value is incorporated.

---

## 6. Traps This Instance Exposes

- **Base Greater Than Modulo:** The input base $a$ can be up to $2^{31} - 1$, which is much larger than $1337$. Python's `pow(a, e, mod)` automatically reduces $a \pmod{1337}$ internally before exponentiating, preventing large arithmetic overhead.
- **Digit Value Zero ($e = 0$):** When a digit is 0 (as in $b = [1, 0]$), $a^0 = 1$, so `ans` remains unchanged. The base $a$ must still be upgraded via $a \leftarrow a^{10} \pmod{1337}$ to correctly advance to the next decimal power.
- **Left-to-Right Horner Alternative:** Digits can also be processed left to right via Horner's scheme: $ans = (ans^{10} \times a^d) \pmod{mod}$. Both schemes are $O(D)$ and mathematically equivalent.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$, where $D = \text{len}(b)$ is the number of decimal digits in the exponent.
  - The loop runs $D$ times.
  - In each iteration, `pow(a, e, 1337)` takes $O(\log 9) = O(1)$ multiplications because $e \le 9$.
  - Upgrading base `pow(a, 10, 1337)` takes $O(\log 10) = O(1)$ multiplications.
  - Total runtime is strictly linear in the number of digits $O(D)$, easily handling $D \le 2000$.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary space, as all operations are modular scalar updates.
