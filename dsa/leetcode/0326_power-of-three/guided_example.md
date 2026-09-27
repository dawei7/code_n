# Guided Example: Power of Three

We trace the step-by-step iterative division by 3, remainder verification (`if n % 3: return False`), boundary condition handling ($n \le 2$), and terminal equality check ($n == 1$) on representative integer instances:

- **Input:** $n = 27$
- **Required output:** `true`
  - Successive division steps: $27 \to 9 \to 3 \to 1$
  - Each division has remainder $0$
  - Loop terminates at $n = 1$, matching $1 == 1 \implies \text{true}$ ($27 = 3^3$)
- **Composite Non-Power Instance:** $n = 45$:
  - $45 // 3 = 15$ ($45 \pmod 3 = 0$)
  - $15 // 3 = 5$ ($15 \pmod 3 = 0$)
  - At $n = 5$: $5 \pmod 3 = 2 \ne 0 \implies$ immediately returns `false` ($45 = 3^2 \times 5$, not a pure power)
- **Zero Base Case:** $n = 0 \implies 0 > 2$ is false, returns $0 == 1 \implies \text{false}$
- **Negative Integer Base Case:** $n = -3 \implies -3 > 2$ is false, returns $-3 == 1 \implies \text{false}$
- **Unit Power Base Case:** $n = 1 \implies 1 > 2$ is false, returns $1 == 1 \implies \text{true}$ ($3^0 = 1$)
- **Maximum 32-Bit Power of Three:** $n = 3^{19} = 1162261467 \implies \text{true}$

This instance demonstrates prime factorization verification, explains why loop condition `n > 2` cleanly handles negative values, zero, and one without dedicated branch ladders, proves why floor division preserves exactness once divisibility is verified, and analyzes $O(\log_3 N)$ logarithmic time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $n = 27$:
Determine if there exists an integer exponent $x$ such that $n = 3^x$.

```text
Powers of 3 progression:
3^0 = 1
3^1 = 3
3^2 = 9
3^3 = 27
3^4 = 81
...

Testing n = 27:
27 / 3 = 9 (rem 0)
 9 / 3 = 3 (rem 0)
 3 / 3 = 1 (rem 0)
Reached 1! -> Valid Power of 3 (True)
```

### Mathematical Invariants of Powers of Three
1. **Uniqueness of Prime Factorization:** Any positive integer $n$ is a power of three if and only if its only prime factor is $3$ ($n = 3^k$ for integer $k \ge 0$).
2. **Peeling Factors:** If $n > 1$ is a power of three, $n \pmod 3$ must be $0$, and $n / 3$ must also be a power of three.
3. **Termination Target:** Continually dividing by $3$ must terminate at exactly $1$ ($3^0$).

---

## 2. Conceptual Foundation & Invariants

### The `while n > 2` State Invariant
Why loop while `n > 2` instead of `n > 0`?
- For $n \le 2$:
  - If $n = 1$: $3^0 = 1$, which is a valid power of three.
  - If $n = 2$: $2$ is not divisible by $3$, so it is false.
  - If $n = 0$: $0$ is not a power of three.
  - If $n < 0$: Negative numbers cannot be formed from positive base $3$.
By terminating the loop when $n \le 2$, we can simply check `return n == 1` at the end!
This simultaneously validates $n = 1$ and rejects $n \in \{2, 0, -1, -2, \dots\}$.

### Iteration Protocol:
While $n > 2$:
1. If $n \pmod 3 \ne 0$:
   Return `False` (Contains prime factors other than 3).
2. $n \leftarrow n // 3$.
Return $n == 1$.

> **Invariant.** At the start of each iteration, all factors of 3 removed so far were exact. If $n$ was a power of 3, the current $n$ remains a power of 3.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $n = 27$:

---

### Step 1: Initial Evaluation
- Current $n = 27$.
- Check loop condition: $27 > 2$ (**True**).
- Divisibility check: $27 \pmod 3 = 0$.
  - Divisible! No foreign prime factors detected.
- Integer division:
  $$
  n \leftarrow 27 // 3 = \mathbf{9}
  $$

---

### Step 2: Second Iteration
- Current $n = 9$.
- Check loop condition: $9 > 2$ (**True**).
- Divisibility check: $9 \pmod 3 = 0$.
  - Divisible!
- Integer division:
  $$
  n \leftarrow 9 // 3 = \mathbf{3}
  $$

---

### Step 3: Third Iteration
- Current $n = 3$.
- Check loop condition: $3 > 2$ (**True**).
- Divisibility check: $3 \pmod 3 = 0$.
  - Divisible!
- Integer division:
  $$
  n \leftarrow 3 // 3 = \mathbf{1}
  $$

---

### Step 4: Terminal Check
- Current $n = 1$.
- Check loop condition: $1 > 2$ (**False**).
- Loop terminates.
- Evaluate return condition:
  $$
  n == 1 \iff 1 == 1 \implies \mathbf{\text{True}}
  $$

---

## 4. Complete Execution Trace

```text
n = 27
Iter 1: 27 > 2 -> 27 % 3 == 0 -> n = 27 // 3 = 9
Iter 2:  9 > 2 ->  9 % 3 == 0 -> n =  9 // 3 = 3
Iter 3:  3 > 2 ->  3 % 3 == 0 -> n =  3 // 3 = 1
End loop: n = 1 -> return 1 == 1 -> True

n = 45
Iter 1: 45 > 2 -> 45 % 3 == 0 -> n = 45 // 3 = 15
Iter 2: 15 > 2 -> 15 % 3 == 0 -> n = 15 // 3 = 5
Iter 3:  5 > 2 ->  5 % 3 == 2 != 0 -> return False!
```

| Iteration | Current $n$ | Condition $n > 2$ | Modulo Test $n \pmod 3$ | Remainder Zero? | Division Update $n //= 3$ | New $n$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 27 | True ($27 > 2$) | $27 \pmod 3 = 0$ | Yes | $27 // 3$ | 9 |
| 2 | 9 | True ($9 > 2$) | $9 \pmod 3 = 0$ | Yes | $9 // 3$ | 3 |
| 3 | 3 | True ($3 > 2$) | $3 \pmod 3 = 0$ | Yes | $3 // 3$ | 1 |
| **Exit** | **1** | **False ($1 \le 2$)** | - | - | - | **$1 == 1 \implies \text{True}$** |

---

## 5. Algorithmic Correctness

**Soundness.** If $n$ is a power of three ($n = 3^k$), each division yields $3^{k-1}$ with zero remainder until $k = 0$, reaching $n = 1$. If $n$ contains any prime factor $p \ne 3$ (e.g. $n = 45 = 3^2 \cdot 5$), dividing out threes eventually produces a quotient not divisible by 3 (such as $5$), causing $n \pmod 3 \ne 0$ to return `False`.

**Completeness.** Nonpositive numbers ($n \le 0$) and $n = 2$ bypass the loop entirely because $n \le 2$. The final check $n == 1$ evaluates to `False` for all of them. The unique case $n = 1 = 3^0$ also bypasses the loop and returns `1 == 1` (`True`). All integers are correctly classified.

---

## 6. Traps This Instance Exposes

- **Floating-Point Logarithm Errors:** Checking `log(n, 3).is_integer()` fails due to floating-point roundoff (e.g. $\log_3(243) = 4.999999999999999$ or $\log_3(45)$ rounding issues). Exact integer arithmetic is mandatory.
- **Infinite Loop with Zero:** Checking `while n % 3 == 0: n //= 3` creates an infinite loop when $n = 0$ because $0 \pmod 3 = 0$ and $0 // 3 = 0$. The condition `n > 2` avoids this trap.
- **Negative Exponents:** Although $3^{-1} = 1/3$ is mathematically a power of three, the input is restricted to integer type, where only nonnegative integer powers are represented.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log_3 N)$. For positive $n$, each iteration reduces $n$ by a factor of 3. The loop runs at most $\lfloor \log_3 N \rfloor$ times (at most 20 iterations for 32-bit signed integers). For $n \le 2$, runtime is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory using zero additional variables.
