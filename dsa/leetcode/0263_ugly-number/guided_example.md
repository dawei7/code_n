# Guided Example: Ugly Number

We trace the step-by-step non-positive boundary guard, prime factor trial division by $\{2, 3, 5\}$, and fundamental theorem of arithmetic residual verification on representative integer instances:

- **Input:** $n = 6$
- **Required output:** `true` ($6 = 2 \times 3$; prime factors are exclusively in $\{2, 3, 5\}$)
- **Prime Factor 7 Violation:** $n = 14 \implies \text{false}$ ($14 = 2 \times 7$; residual $7 \ne 1$)
- **Identity Unit Instance:** $n = 1 \implies \text{true}$ ($1 = 2^0 \cdot 3^0 \cdot 5^0$; no prime factors exist)
- **Zero Boundary Instance:** $n = 0 \implies \text{false}$ (Non-positive; prevents division-by-zero infinite loop)
- **Negative Integer Instance:** $n = -6 \implies \text{false}$ (Ugly numbers are defined strictly over $\mathbb{Z}^+$)

This instance demonstrates prime factorization reduction, explains why dividing out all powers of 2, 3, and 5 reduces any ugly number to 1, details the non-positive early guard, and guarantees $O(\log n)$ logarithmic runtime with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an integer $n = 6$, determine whether it is an **ugly number** (a positive integer whose prime factors are limited to $2, 3,$ and $5$):
```text
Prime factorization of 6: 2 * 3
Allowed prime set: {2, 3, 5}
All prime factors are in {2, 3, 5} -> Output: True
```

Contrast with $n = 14$:
$$
14 = 2 \times 7
$$
The prime factor $7 \notin \{2, 3, 5\}$, so $14$ is **not ugly** (`false`).

By the Fundamental Theorem of Arithmetic, any positive integer $n$ can be uniquely factored as:
$$
n = 2^a \cdot 3^b \cdot 5^c \cdot R
$$
where $R$ is not divisible by 2, 3, or 5.
If we repeatedly divide $n$ by 2, 3, and 5 until divisibility ceases, $n$ becomes $R$.
The number is ugly **if and only if $R = 1$**.

---

## 2. Conceptual Foundation & Invariants

### 1. Non-Positive Boundary Guard
By definition, ugly numbers are **strictly positive integers** ($n \ge 1$):
- If $n \le 0$, return `false` immediately.
*(Crucial: If $n = 0$, $0 \pmod 2 = 0$ and $0 // 2 = 0$. Without an early guard, a division loop on 0 would run indefinitely!)*.

### 2. Systematic Prime Stripping Protocol
For each allowed prime $p \in [2, 3, 5]$:
While $n \pmod p == 0$:
$$
n \leftarrow n // p
$$

### 3. Residual Evaluation
After exhausting all divisions by $2, 3,$ and $5$:
- If $n == 1$: All prime factors were in $\{2, 3, 5\}$. Return `true`.
- If $n > 1$: The residual contains some other prime factor ($7, 11, 13, \dots$). Return `false`.

> **Invariant.** At any step of the division loop, the current $n$ is an integer preserving all prime factors of the original input other than the removed powers of 2, 3, and 5.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $n = 6$:

### Step 1: Boundary Guard
- Check: $n \le 0 \iff 6 \le 0$ (**False**).
- Proceeds to factor stripping.

---

### Step 2: Strip Prime Factor 2
- Check: $6 \pmod 2 == 0$ (**True**).
- Divide: $n \leftarrow 6 // 2 = \mathbf{3}$.
- Check: $3 \pmod 2 == 0$ (**False**).
- Factor 2 fully stripped.

---

### Step 3: Strip Prime Factor 3
- Check: $3 \pmod 3 == 0$ (**True**).
- Divide: $n \leftarrow 3 // 3 = \mathbf{1}$.
- Check: $1 \pmod 3 == 0$ (**False**).
- Factor 3 fully stripped.

---

### Step 4: Strip Prime Factor 5
- Check: $1 \pmod 5 == 0$ (**False**).
- Factor 5 loop does not run.

---

### Step 5: Terminal Residual Check
- Residual: $n = 1$.
- Check $n == 1 \implies 1 == 1$ (**True**).
- **Return `true`!**

---

## 4. Complete Execution Trace

```text
n = 6
Check n > 0 -> 6 > 0 (Pass)

Prime 2: 6 % 2 == 0 -> n = 6 // 2 = 3
         3 % 2 != 0 -> done with 2
Prime 3: 3 % 3 == 0 -> n = 3 // 3 = 1
         1 % 3 != 0 -> done with 3
Prime 5: 1 % 5 != 0 -> done with 5

Final n == 1 -> Return True
```

| Step | Divisor Tested ($p$) | Pre-Division $n$ | Divisible ($n \pmod p == 0$)? | Post-Division $n$ | Residual State |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | Setup | 6 | - | 6 | Positive integer verified |
| **1** | 2 | 6 | **Yes ($6 = 2 \times 3$)** | **3** | Power $2^1$ removed |
| **2** | 3 | 3 | **Yes ($3 = 3 \times 1$)** | **1** | Power $3^1$ removed |
| 3 | 5 | 1 | No ($1 \pmod 5 = 1$) | 1 | No factor of 5 |
| **End** | Check $n == 1$ | 1 | - | - | **`true` (Ugly)** |

### Contrast: Non-Ugly Number Trace ($n = 14$)
- Strip 2: $14 \pmod 2 == 0 \implies n \leftarrow 7$.
- Strip 3: $7 \pmod 3 \ne 0$.
- Strip 5: $7 \pmod 5 \ne 0$.
- Residual: $n = 7 \ne 1$.
- **Returns `false`!**

---

## 5. Algorithmic Correctness

**Soundness.** Every division replaces $n$ with $n / p$ where $p \in \{2, 3, 5\}$. By unique factorization, if $n$ eventually reaches $1$, the original number was of the form $2^a 3^b 5^c$, which is the exact mathematical definition of an ugly number.

**Completeness.** Since division by 2, 3, and 5 strictly reduces $n$ when divisible and does not alter any prime factors other than 2, 3, and 5, any number containing an extraneous prime factor $q \ge 7$ will retain $q$, ending at $R \ge 7 > 1$ and returning `false`.

---

## 6. Traps This Instance Exposes

- **Infinite Loop on Zero:** For $n = 0$, $0 \pmod 2 == 0$ and $0 // 2 == 0$. Without `if n <= 0: return False`, the code hangs in an infinite loop.
- **Negative Numbers:** $-6 = -1 \times 2 \times 3$. Mathematically, $-1$ is a unit, not an ugly prime. The problem explicitly defines ugly numbers as **positive** integers.
- **Trial Division by All Primes:** Running trial division through all primes up to $\sqrt{n}$ costs $O(\sqrt{n})$ time. Since only 2, 3, and 5 are allowed, dividing strictly by $\{2, 3, 5\}$ requires at most $\log_2 n$ operations.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$, where $n$ is the input integer. Each successful division by 2, 3, or 5 reduces $n$ by at least half ($n \leftarrow \lfloor n/2 \rfloor$). The maximum number of divisions is bounded by $\log_2 n \le 31$ operations for any 32-bit integer, executing in nanoseconds.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. Only loop variables are stored.
