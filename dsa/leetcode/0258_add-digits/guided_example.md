# Guided Example: Add Digits

We trace the step-by-step decimal place-value congruence modulo 9, digital root cycle extraction, and constant-time shift formula on representative integer instances:

- **Input:** $\text{num} = 38$
- **Required output:** $2$ (Step 1: $3 + 8 = 11$; Step 2: $1 + 1 = 2$)
- **Multiple of 9 Instance:** $\text{num} = 18 \implies 9$ (Digit sum $1 + 8 = 9$; positive multiple of 9 produces 9, not 0)
- **Zero Base Case:** $\text{num} = 0 \implies 0$ (The only integer with digital root 0)
- **Single Digit Identity:** $\text{num} = 7 \implies 7$ (Already a single digit)
- **Large Integer Instance:** $\text{num} = 9999 \implies 9$ ($9 \times 4 = 36 \to 3 + 6 = 9$)

This instance demonstrates modular arithmetic and digital roots in base 10, proves why decimal digit summation preserves invariance modulo 9 ($10^k \equiv 1^k \equiv 1 \pmod 9$), solves the problem in strictly $O(1)$ time and $O(1)$ auxiliary space without any loops or recursion, and explains the $(n - 1) \pmod 9 + 1$ index-shift identity.

---

## 1. Instance & Teaching Goal

Given an integer $\text{num} = 38$, repeatedly sum its digits until a single digit remains:
```text
Iteration 1: 38 -> 3 + 8 = 11
Iteration 2: 11 -> 1 + 1 = 2
Output: 2
```

While an iterative simulation repeatedly extracting digits with `% 10` and `// 10` takes $O(\log_{10} N)$ time, the follow-up asks for an **$O(1)$ constant-time, loop-free** solution.
Number theory establishes that the repeated sum of digits of a decimal number is its **digital root**, which is periodic modulo 9:
$$
\text{dr}(n) = \begin{cases}
0, & \text{if } n = 0 \\
9, & \text{if } n > 0 \text{ and } n \equiv 0 \pmod 9 \\
n \pmod 9, & \text{if } n \not\equiv 0 \pmod 9
\end{cases}
$$
This piecewise function can be expressed in a single closed form:
$$
\text{dr}(n) = 1 + (n - 1) \pmod 9 \quad (\text{for } n > 0)
$$

---

## 2. Conceptual Foundation & Invariants

### The Modulo 9 Invariance Proof
Any positive integer $n$ can be written in decimal notation:
$$
n = d_k 10^k + d_{k-1} 10^{k-1} + \dots + d_1 10^1 + d_0 10^0 = \sum_{i=0}^k d_i 10^i
$$
Observe the base-10 modular identity:
$$
10 \equiv 1 \pmod 9 \implies 10^i \equiv 1^i \equiv 1 \pmod 9 \quad \text{for all } i \ge 0
$$
Substituting into the decimal expansion:
$$
n \equiv \sum_{i=0}^k d_i (1) \equiv \sum_{i=0}^k d_i \pmod 9
$$
**A number and the sum of its decimal digits leave the exact same remainder when divided by 9.**
Because each iterative reduction preserves congruence modulo 9, the final single-digit result $R \in [1, 9]$ must satisfy:
$$
R \equiv n \pmod 9
$$

### The Shift Trick: Why $(n - 1) \pmod 9 + 1$?
In standard integer modulo arithmetic:
$n \pmod 9$ produces remainders in $\{0, 1, 2, \dots, 8\}$.
However, for any positive integer $n > 0$, the digital root must lie in $\{1, 2, \dots, 9\}$.
If $n$ is a multiple of 9 (e.g. $18$), $18 \pmod 9 = 0$, but its digital root is $1 + 8 = 9$!
To map the residue cycle $\{0, 1, \dots, 8\}$ to $\{9, 1, \dots, 8\}$ without branching:
1. Subtract $1$: maps $n \in [1, 9]$ to $[0, 8]$.
2. Take modulo $9$: $(n - 1) \pmod 9$ yields the correct offset in $[0, 8]$.
3. Add $1$ back: shifts the range back to $[1, 9]$!

> **Invariant.** For any positive integer $n$, $(n - 1) \pmod 9 + 1$ is mathematically identical to the terminal single-digit sum.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{num} = 38$:

### Step 1: Zero Guard
- Check: $\text{num} == 0 \implies 38 == 0$ (False).
- Proceeds to closed-form digital root formula.

---

### Step 2: Offset Subtraction
- Subtract $1$:
  $$
  38 - 1 = \mathbf{37}
  $$

---

### Step 3: Modulo 9 Reduction
- Divide $37$ by $9$:
  $$
  37 = 4 \times 9 + 1 \implies 37 \pmod 9 = \mathbf{1}
  $$

---

### Step 4: Re-Add Unit Offset
- Add $1$:
  $$
  1 + 1 = \mathbf{2}
  $$

---

### Verification via Iterative Simulation
- Pass 1: $38 \to 3 + 8 = 11$.
- Pass 2: $11 \to 1 + 1 = 2$.
- Both methods yield $\mathbf{2}$!

---

## 4. Complete Execution Trace

```text
num = 38

Formula: (38 - 1) % 9 + 1
       = 37 % 9 + 1
       = 1 + 1
       = 2

Result: 2
```

| Input $n$ | Zero Guard | Shifted ($n - 1$) | Residue Modulo 9 | Restored Value ($+ 1$) | Iterative Verification |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | Return 0 | - | - | **0** | $0 \to 0$ |
| 1 | Pass | 0 | 0 | **1** | $1 \to 1$ |
| 7 | Pass | 6 | 6 | **7** | $7 \to 7$ |
| 9 | Pass | 8 | 8 | **9** | $9 \to 9$ |
| 18 | Pass | 17 | 8 | **9** | $18 \to 1 + 8 = 9$ |
| **38** | **Pass** | **37** | **1** | **2** | **$38 \to 11 \to 2$** |
| 9999 | Pass | 9998 | 8 | **9** | $36 \to 9$ |

The rows above evaluate the closed form directly. The next table walks the same
instances from the opposite direction, recording what the literal repeated
digit-sum reduction actually produces round by round, so every formula entry can
be cross-checked against the simulation it is meant to replace.

| Instance $n$ | Round 1 result | Round 2 result | Round 3 result | Reduction rounds | Digital root |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | — | — | — | 0 | **0** |
| 7 | — | — | — | 0 | **7** |
| 18 | 9 | — | — | 1 | **9** |
| 38 | 11 | 2 | — | 2 | **2** |
| 9999 | 36 | 9 | — | 2 | **9** |
| 2147483647 | 46 | 10 | 1 | 3 | **1** |

Two facts fall out of this trace. First, a multiple of 9 such as $9999$ needs
the same two rounds as $38$ but lands on $9$ rather than on $0$, because the
digit sum of a positive multiple of 9 is again a positive multiple of 9 and the
smallest such single digit is $9$. Second, the number of rounds is bounded by
the digit count: for $n \le 2^{31} - 1$ there are at most $10$ digits, so the
first round yields at most $90$, the second at most $18$, and the third at most
$9$. Three rounds therefore always suffice on the stated input domain, which is
why the reference case $2147483647$ terminates at $1$ after the chain
$2147483647 \to 46 \to 10 \to 1$.

---

## 5. Algorithmic Correctness

**Soundness.** Since $10 \equiv 1 \pmod 9$, the digit-sum map $S(n) = \sum d_i$ satisfies $S(n) \equiv n \pmod 9$. By mathematical induction, repeated applications $S(S(\dots S(n)))$ preserve $n \pmod 9$. Since the terminal value $R$ is a single digit, $R \in [0, 9]$. If $n > 0$, every digit sum of positive digits is $\ge 1$, so $R \in [1, 9]$. There is exactly one integer in $[1, 9]$ congruent to $n \pmod 9$, which the formula $(n - 1) \pmod 9 + 1$ uniquely calculates.

**Completeness.** Zero is correctly handled by the initial branch, and every positive 32-bit integer is covered by the closed-form arithmetic expression without truncation or overflow.

---

## 6. Traps This Instance Exposes

- **Failing the Zero Case in the Compact Formula:** Evaluating $(0 - 1) \pmod 9 + 1$: in Python, `(-1) % 9` is $8$, so $8 + 1 = 9$ (Incorrect! The digital root of 0 is 0). Thus, `if num == 0: return 0` is mandatory before applying the formula.
- **The Multiple-of-9 Remainder Trap:** Writing `num % 9` directly produces `0` for $18, 27, 36, \dots$. The answer for positive multiples of 9 is $9$, not $0$. The $(n - 1) \pmod 9 + 1$ shift cleanly solves this edge case.
- **Base Dependency:** This formula works because decimal numbers are in base 10 ($10 - 1 = 9$). For an arbitrary base $b$, the digital root is evaluated modulo $(b - 1)$.

### Boundary Map of the Residue Collision

The trap is not a single unlucky input; it is one residue class of size
$\lfloor n / 9 \rfloor$. The table below separates the instances where the
unshifted residue already agrees with the root from the ones where it does not,
and shows the shift repairing exactly those cases.

| Instance $n$ | Unshifted `num % 9` | Correct digital root | Agreement | Shifted evaluation `(num - 1) % 9 + 1` |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | Agrees, but only because the guard intercepts it first | $8 + 1 = 9$, so the guard is mandatory |
| 1 | 1 | 1 | Agrees; the residue set is anchored here | $0 + 1 = 1$ |
| 7 | 7 | 7 | Agrees | $6 + 1 = 7$ |
| 9 | 0 | 9 | Disagrees by $-9$ | $8 + 1 = 9$ |
| 18 | 0 | 9 | Disagrees by $-9$ | $8 + 1 = 9$ |
| 38 | 2 | 2 | Agrees | $1 + 1 = 2$ |
| 9999 | 0 | 9 | Disagrees by $-9$ | $8 + 1 = 9$ |
| 2147483647 | 1 | 1 | Agrees | $0 + 1 = 1$ |

Only the residue $0$ is ambiguous, and it is ambiguous for two different
reasons. For $n = 0$ the true root is $0$, so no formula built from residues
alone can recover it; the guard must run first. For every positive multiple of
$9$ the true root is $9$, and the shift resolves it uniformly, because
$(n - 1) \bmod 9$ sends the residue $0$ to $8$ and leaves every other residue
untouched. Removing the ambiguity at one end while preserving it nowhere else is
the entire content of the $(n - 1) \bmod 9 + 1$ identity.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time. A single branch check followed by one subtraction, one modulo operation, and one addition. No loops, recursion, or string conversions are executed.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory.

### Alternatives and Their Actual Costs

The constant bound is not an accident of the closed form; it is the point of the
follow-up. Each alternative below reaches the correct root but pays for
information the residue class already contains.

| Approach | Mechanism | Time | Auxiliary space | Failure mode or tradeoff |
|:---|:---|:---:|:---:|:---|
| Closed-form digital root | One subtraction, one modulo by 9, one addition | $O(1)$ | $O(1)$ | Silent wrong answer on $n = 0$ if the guard is dropped, and it is specific to base 10 |
| Digit-extraction loop | Repeatedly take the last digit and divide the running value down, then restart on the partial sum | $O(\log_{10} n)$ for the first round; at most three rounds on the stated domain | $O(1)$ | Correct and readable, but the follow-up asks for the loop to be removed, and the round count is only bounded by the digit count |
| Decimal string reduction | Render the value as text, sum its character values per round, and repeat on the running total | $O(d)$ per round where $d$ is the digit count | $O(d)$ | Allocates and reparses strings for a value that is already available arithmetically; worst initial cost of the three |
| Unshifted `num % 9` | Return the raw residue | $O(1)$ | $O(1)$ | Returns $0$ for $9, 18, 9999, \dots$ where the root is $9$, and cannot represent $0$ separately from those cases |

The closed form wins because the digit-sum map and the identity map differ by an
exact multiple of $9$, so the entire infinite sequence of reductions collapses
to one residue computation. No intermediate partial sum has to be materialised,
which is what keeps the auxiliary space constant rather than proportional to the
digit count.

$$\text{total work} = \Theta(1), \qquad \text{auxiliary space} = \Theta(1)$$
