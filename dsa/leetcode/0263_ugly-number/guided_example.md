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

### Exponent Table: One Row per Input

Every input is decided by the same three numbers the loops produce — the
exponents $a, b, c$ and the residual $R$ in $n = 2^a \cdot 3^b \cdot 5^c \cdot R$.
Writing them out for several inputs shows that the verdict depends on $R$ alone,
never on which allowed primes happened to appear.

| $n$ | $a$ (exponent of 2) | $b$ (exponent of 3) | $c$ (exponent of 5) | Residual $R$ | Reconstruction of $n$ | Verdict |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 6 | 1 | 1 | 0 | 1 | $2^1 \cdot 3^1 = 6$ | `true` |
| 30 | 1 | 1 | 1 | 1 | $2 \cdot 3 \cdot 5 = 30$ | `true` |
| 60 | 2 | 1 | 1 | 1 | $2^2 \cdot 3 \cdot 5 = 60$ | `true` |
| 45 | 0 | 2 | 1 | 1 | $3^2 \cdot 5 = 45$ | `true` |
| 1 | 0 | 0 | 0 | 1 | the empty product, with no prime factor at all | `true` |
| 14 | 1 | 0 | 0 | 7 | $2 \cdot 7 = 14$ | `false` |
| 98 | 1 | 0 | 0 | 49 | $2 \cdot 7^2 = 98$ | `false` |
| 210 | 1 | 1 | 1 | 7 | $2 \cdot 3 \cdot 5 \cdot 7 = 210$ | `false` |
| 2147483647 | 0 | 0 | 0 | 2147483647 | no allowed prime divides it, so nothing is stripped | `false` |

Three rows carry the teaching load. Row four shows an input with $a = 0$: a
number with no factor of 2 at all still passes, because the loops are permitted
to run zero times. Row seven ends with the composite residual $49$, proving the
terminal test is the equality $R = 1$ and not a primality check — a residual that
is composite fails for the same reason a prime one does. Row eight keeps allowed
and disallowed factors together ($210 = 2 \cdot 3 \cdot 5 \cdot 7$); stripping
removes exactly the allowed part and leaves $7$ untouched, which is what makes
the residual a faithful witness of everything the loops could not remove.

---

## 5. Algorithmic Correctness

**Soundness.** Every division replaces $n$ with $n / p$ where $p \in \{2, 3, 5\}$. By unique factorization, if $n$ eventually reaches $1$, the original number was of the form $2^a 3^b 5^c$, which is the exact mathematical definition of an ugly number.

**Completeness.** Since division by 2, 3, and 5 strictly reduces $n$ when divisible and does not alter any prime factors other than 2, 3, and 5, any number containing an extraneous prime factor $q \ge 7$ will retain $q$, ending at $R \ge 7 > 1$ and returning `false`.

---

## 6. Traps This Instance Exposes

- **Infinite Loop on Zero:** For $n = 0$, $0 \pmod 2 == 0$ and $0 // 2 == 0$. Without `if n <= 0: return False`, the code hangs in an infinite loop.
- **Negative Numbers:** $-6 = -1 \times 2 \times 3$. Mathematically, $-1$ is a unit, not an ugly prime. The problem explicitly defines ugly numbers as **positive** integers.
- **Trial Division by All Primes:** Running trial division through all primes up to $\sqrt{n}$ costs $O(\sqrt{n})$ time. Since only 2, 3, and 5 are allowed, dividing strictly by $\{2, 3, 5\}$ requires at most $\log_2 n$ operations.

### Boundary Map of the Guard and the Terminal Test

Each row below isolates one boundary value and states what the guard contributes
versus what the arithmetic alone would do. The negative rows are the interesting
ones: the arithmetic happens to return `false` for them too, but only by
accident, so the guard is doing definitional work rather than arithmetic work.

| Input | Does $n \ge 1$ hold? | Stripping behavior | Terminal residual | Verdict | What the boundary teaches |
|:---:|:---:|:---|:---:|:---:|:---|
| 0 | No | A loop on 0 never advances, since $0 \bmod 2 = 0$ and $0 // 2 = 0$ | Never reached | `false` | Here the guard is a termination proof: without it the method does not halt at all |
| -6 | No | $-6 \bmod 2 = 0$, so stripping would run and end at residual $-1$ | Never reached (guard) | `false` | $-1$ is a unit, not a prime factor; ugly numbers live in $\mathbb{Z}^{+}$, so the guard encodes the definition |
| -14 | No | The same halving chain would end at residual $-7$ | Never reached (guard) | `false` | Dividing a negative by allowed primes keeps it negative, so no negative input can ever reduce to 1 |
| 1 | Yes | All three loops are skipped because no prime divides 1 | $R = 1$ | `true` | The empty product is the base case, and $1 = 2^0 3^0 5^0$ |
| $2^{30} = 1073741824$ | Yes | 30 successive divisions by 2, the largest count any legal 32-bit input can force | $R = 1$ | `true` | The work bound is real and reached: no input in range needs a 31st division |
| $2^{31} - 1 = 2147483647$ | Yes | No loop body executes at all | $R = 2147483647$ | `false` | An odd non-multiple of 3 or 5 leaves the entire input as residual |
| $49 = 7^2$ | Yes | No loop body executes at all | $R = 49$ | `false` | The terminal test is $R = 1$; a composite residual is rejected exactly like a prime one |
| $98 = 2 \cdot 7^2$ | Yes | One division by 2 | $R = 49$ | `false` | Removing the allowed factor exposes the disallowed part without altering it |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$, where $n$ is the input integer. Each successful division by 2, 3, or 5 reduces $n$ by at least half ($n \leftarrow \lfloor n/2 \rfloor$). The maximum number of divisions is bounded by $\log_2 n \le 31$ operations for any 32-bit integer, executing in nanoseconds.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. Only loop variables are stored.

### Alternatives and Their Costs

The problem asks a membership question about one integer, and the alternatives
differ mainly in how much more than that they compute.

| Strategy | Mechanism | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| Strip the three allowed primes | Divide out every factor of 2, 3, and 5, then test whether the residual is 1 | $O(\log n)$ | $O(1)$ | The direct method; it still needs the non-positive guard to terminate on $n = 0$ |
| Recursive stripping | Accept when $n = 1$, otherwise recurse on $n // p$ for any allowed prime $p$ dividing $n$ | $O(\log n)$ | $O(\log n)$ call stack | Same verdicts, but up to 30 nested frames replace three loops |
| Enumerate all ugly numbers up to $n$ | Build the closure of $\{1\}$ under multiplication by 2, 3, and 5 and test membership | $O(u \log u)$ where $u$ is how many ugly numbers lie in range | $O(u)$ | There are 1691 ugly numbers below $2^{31}$, so this answers a far harder question than asked |
| Full trial division up to $\sqrt{n}$ | Test every candidate divisor from 2 upward | $O(\sqrt{n})$ | $O(1)$ | About 46340 candidate divisors at the 32-bit limit replace at most 30 divisions |
| Sieve of smallest prime factors | Precompute a factor table for every integer up to $n$ | $O(n \log \log n)$ | $O(n)$ | Infeasible near $2^{31}$ and again solves a much larger problem |

The chosen method is the first row. It exploits the constraint that the allowed
prime set has only three elements: each division by 2, 3, or 5 shrinks the value
by at least a factor of 2, so at most $\log_2 n$ divisions occur, and the
residual test turns a factorization question into a single equality.
