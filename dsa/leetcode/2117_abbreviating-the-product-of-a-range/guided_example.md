# Guided Example: Abbreviating the Product of a Range

We trace the step-by-step execution of the optimal logarithmic mantissa and modular factorization approach on a representative problem instance:

- **Range:** $[left, right] = [1, 16]$
- **Expected Output:** `"20922...89888e3"`

This instance illustrates the dual separation of leading and trailing digits, the exact counting and cancellation of factor pairs $(2, 5)$ responsible for trailing zeros, and the formatting transition when the normalized product exceeds ten digits.

---

## 1. Problem Overview & Representative Instance

Given two positive integers $left$ and $right$, we consider the inclusive product:

$$P = \prod_{i=left}^{right} i$$

Let $C$ denote the count of trailing decimal zeros in $P$. We divide out all trailing zeros to obtain the normalized product $P' = P / 10^C$.
- If $P'$ contains strictly more than $10$ decimal digits, we represent it as `<first_5>...<last_5>e<C>`, where `<first_5>` denotes the first $5$ significant digits of $P'$ and `<last_5>` denotes its last $5$ digits (preserving leading zeros in the suffix if needed).
- If $P'$ contains $10$ or fewer digits, we represent it directly as `<P'>e<C>`.

For our representative instance $[1, 16]$:
- The full factorial product is $16! = 20{,}922{,}789{,}888{,}000$.
- The number of trailing zeros is $C = 3$, since $16!$ is divisible by $10^3$ but not $10^4$.
- Dividing by $10^3$ yields the normalized product $P' = 20{,}922{,}789{,}888$.
- The normalized value has $11$ digits ($11 > 10$), requiring abbreviation:
  - First $5$ digits: $20922$
  - Last $5$ digits: $89888$
  - Trailing zeros exponent: $e3$
- The final formatted string is `"20922...89888e3"`.

---

## 2. Mathematical & Algorithmic Principles

### Trailing Zeros and Prime Valuation
A decimal zero at the end of an integer corresponds directly to a factor of $10 = 2 \times 5$. By Legendre's formula / prime valuation $\nu_p(x)$:

$$C = \min\left(\sum_{i=left}^{right} \nu_2(i), \sum_{i=left}^{right} \nu_5(i)\right)$$

Because $2 \le 5$, multiples of $2$ are strictly more frequent than multiples of $5$ across any interval starting at $1$ (and virtually all intervals), making $\nu_5$ the typical limiting factor.

### Logarithmic Mantissa for Leading Digits
Directly computing large products causes integer overflow or quadratic-time large-integer arithmetic. Instead, we use base-10 logarithms:

$$\log_{10}(P) = \sum_{i=left}^{right} \log_{10}(i)$$

Removing $C$ trailing zeros scales the product by $10^{-C}$, which translates in log-space to:

$$L = \log_{10}(P') = \log_{10}(P) - C = \left(\sum_{i=left}^{right} \log_{10}(i)\right) - C$$

The integer part $\lfloor L \rfloor$ yields the order of magnitude:
- Total digits in $P'$ is $D = \lfloor L \rfloor + 1$.
- The fractional part $\{L\} = L - \lfloor L \rfloor$ represents the normalized mantissa in $[0, 1)$.
- The leading $5$ digits correspond to $\lfloor 10^{\{L\} + 4} \rfloor$.

### Modular Residue for Trailing Digits
To extract the last $5$ digits of $P'$ without evaluating the massive integer, we track the product modulo $10^5$ (or modulo $10^{10}$ to detect whether abbreviation is required). For each factor $i \in [left, right]$:
1. We divide out factors of $2$ as long as remaining required factor-2 cancellations exist ($c_2 > 0$).
2. We divide out factors of $5$ as long as remaining required factor-5 cancellations exist ($c_5 > 0$).
3. The stripped number is multiplied into a running modular accumulator modulo $10^{10}$.

| Computation Pillar | Mathematical Tool | Output Target |
|---|---|---|
| Trailing Zero Count $C$ | Prime factorization $\nu_2, \nu_5$ | Exponent $C$ |
| Leading 5 Digits | $\lfloor 10^{\{L\} + 4} \rfloor$ where $L = \sum \log_{10}(i) - C$ | Prefix string |
| Trailing 5 Digits | Residue modulo $10^5$ after cancelling $2^C \times 5^C$ | Suffix string |
| Total Digit Count $D$ | $\lfloor L \rfloor + 1$ or direct threshold check | Format switch ($D > 10$) |

---

## 3. Step-by-Step Walkthrough with Intermediate State

### Phase 1: Counting Prime Factors $(2, 5)$
We inspect each integer $i \in [1, 16]$:
- Factors of $5$ occur at:
  - $i = 5 \implies \nu_5(5) = 1$
  - $i = 10 \implies \nu_5(10) = 1$
  - $i = 15 \implies \nu_5(15) = 1$
  - Total factor-5 count: $\sum \nu_5 = 1 + 1 + 1 = 3$.
- Factors of $2$ occur at all even integers:
  - $2, 4, 6, 8, 10, 12, 14, 16 \implies \nu_2 = 1 + 2 + 1 + 3 + 1 + 2 + 1 + 4 = 15$.
- Trailing zeros:

$$C = \min(15, 3) = 3$$

### Phase 2: Logarithmic Accumulation for Leading Digits
We sum $\log_{10}(i)$ for $i = 1, \dots, 16$:

$$\sum_{i=1}^{16} \log_{10}(i) \approx 13.32061993$$

Subtracting the exponent $C = 3$:

$$L = 13.32061993 - 3 = 10.32061993$$

From $L$:
- Total digits: $D = \lfloor 10.32061993 \rfloor + 1 = 10 + 1 = 11$.
- Because $11 > 10$, the normalized product requires abbreviation.
- Fractional mantissa: $\{L\} = 0.32061993$.
- Leading significant digits:

$$\text{first\_5} = \lfloor 10^{0.32061993 + 4} \rfloor = \lfloor 10^{4.32061993} \rfloor = \lfloor 20922.789888 \rfloor = 20922$$

### Phase 3: Modular Accumulation for Trailing Digits
We initialize remaining factor allowances to remove: $rem_2 = 3$, $rem_5 = 3$.
We maintain running product $M$ modulo $10^{10}$:
- Numbers $1, 2, 3, 4$:
  - $i=2$: removes one factor of 2 ($rem_2 \to 2$).
  - $i=4$: removes two factors of 2 ($rem_2 \to 0$).
- Number $5$: removes one factor of 5 ($rem_5 \to 2$).
- Number $10$: $10 = 2 \times 5$; removes one factor of 5 ($rem_5 \to 1$). Factor of 2 remains since $rem_2 = 0$.
- Number $15$: removes one factor of 5 ($rem_5 \to 0$).
- All 3 factors of 2 and all 3 factors of 5 have been cancelled!
- The remaining product across all terms modulo $10^{10}$ yields $M = 20{,}922{,}789{,}888$.
- The last 5 digits are:

$$\text{last\_5} = M \pmod{10^5} = 20{,}922{,}789{,}888 \pmod{100000} = 89888$$

### Phase 4: Final String Assembly
Combining the components:
- Prefix: `"20922"`
- Ellipsis: `"..."`
- Suffix: `"89888"`
- Exponent: `"e3"`
Output: `"20922...89888e3"`.

---

## 4. Comprehensive State Trace

The table below traces factor cancellation and modular state across the interval integers:

| Integer $i$ | $\nu_2(i)$ | $\nu_5(i)$ | Factors 2 Removed | Factors 5 Removed | Remaining Value Multiplied | Running $M \pmod{10^5}$ |
|---|---|---|---|---|---|---|
| $1$ | $0$ | $0$ | $0$ | $0$ | $1$ | $1$ |
| $2$ | $1$ | $0$ | $1$ | $0$ | $1$ | $1$ |
| $3$ | $0$ | $0$ | $0$ | $0$ | $3$ | $3$ |
| $4$ | $2$ | $0$ | $2$ | $0$ | $1$ | $3$ |
| $5$ | $0$ | $1$ | $0$ | $1$ | $1$ | $3$ |
| $6$ | $1$ | $0$ | $0$ | $0$ | $6$ | $18$ |
| $7$ | $0$ | $0$ | $0$ | $0$ | $7$ | $126$ |
| $8$ | $3$ | $0$ | $0$ | $0$ | $8$ | $1008$ |
| $9$ | $0$ | $0$ | $0$ | $0$ | $9$ | $9072$ |
| $10$ | $1$ | $1$ | $0$ | $1$ | $2$ | $18144$ |
| $11$ | $0$ | $0$ | $0$ | $0$ | $11$ | $99584$ |
| $12$ | $2$ | $0$ | $0$ | $0$ | $12$ | $95008$ |
| $13$ | $0$ | $0$ | $0$ | $0$ | $13$ | $35104$ |
| $14$ | $1$ | $0$ | $0$ | $0$ | $14$ | $91456$ |
| $15$ | $0$ | $1$ | $0$ | $1$ | $3$ | $74368$ |
| $16$ | $4$ | $0$ | $0$ | $0$ | $16$ | $89888$ |

The modular suffix is verified as $89888$, matching the exact lower digits.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Trailing zeros are determined strictly by prime factors $2$ and $5$. Because multiplication is commutative and associative, dividing out exactly $C$ factors of $2$ and $C$ factors of $5$ during the product accumulation is mathematically equivalent to dividing the total product by $10^C$. The ring homomorphism $(a \cdot b) \bmod m = ((a \bmod m) \cdot (b \bmod m)) \bmod m$ guarantees that evaluating the suffix modulo $10^5$ preserves the exact lowest $5$ digits. Similarly, continuity of logarithms guarantees that $\sum \log_{10}(x) - C$ yields the exact order of magnitude and leading decimal digits within floating-point precision bounds.

**Completeness.** All integers in $[left, right]$ are visited. The total digit threshold $D \le 10$ is checked deterministically, ensuring that small ranges (e.g. $[1, 4] \to \text{"24e0"}$) are returned unabbreviated without ellipses, while large ranges exceeding 10 digits are formatted with leading digits, ellipsis, and zero-padded trailing digits.

---

## 6. Edge Cases & Anti-Patterns

- **Small Products ($D \le 10$):** If the normalized product is $\le 10^{10}$, no abbreviation occurs and the exact integer is formatted directly with `e<C>`.
- **Leading Zeros in Suffix:** If the last 5 digits evaluate to $42$, they must be formatted with leading zeros as `"00042"`.
- **Zero Trailing Zeros ($C = 0$):** When the range contains no multiples of 5, $C = 0$ and the suffix format appends `"e0"`.
- **Anti-Pattern — Arbitrary Precision BigInt Multiplication:** Calculating the raw product of a range like $[1, 10000]$ produces a number with tens of thousands of digits, resulting in quadratic time $\mathcal{O}(N^2)$ and massive memory consumption. The logarithmic and modular decoupling keeps runtime strictly $\mathcal{O}(N)$ and auxiliary memory $\mathcal{O}(1)$.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \log(\max(\text{val})))$, where $N = right - left + 1$. Factoring out powers of 2 and 5 takes logarithmic steps per integer, and computing $\log_{10}$ is an $\mathcal{O}(1)$ floating-point operation.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$. The algorithm only maintains scalar counters for prime valuations, logarithmic sums, and modular accumulators.
