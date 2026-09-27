# Guided Example: Prime Number of Set Bits in Binary Representation

We trace the step-by-step Hamming weight population count evaluation ($\text{popcount}(i)$), 20-bit integer upper bound constraint analysis ($right \le 10^6 < 2^{20}$), small prime lookup set construction ($\mathcal{P}_{<20} = \{2, 3, 5, 7, 11, 13, 17, 19\}$), bitwise cardinality predicate testing, and inclusive range summation over representative numerical sequences:

- **Input:** $left = 6, \quad right = 10$
- **Required output:** `4`
  - Counting criteria:
    - For each integer $x \in [left, right]$:
      - Express $x$ in base-2 binary representation.
      - Count the number of set bits (bits equal to `1`), denoted by $\text{popcount}(x)$.
      - Determine whether $\text{popcount}(x)$ is a **prime number** (greater than 1 with no positive divisors other than 1 and itself).
    - Objective: Return the total count of numbers in $[left, right]$ whose set bit count is prime.
    - Note on 1: The integer 1 is **not** a prime number.
    - For the range $[6, 10]$:
      - $x = 6$: Binary `110` $\implies 2$ set bits. 2 is prime $\implies$ **Counted**.
      - $x = 7$: Binary `111` $\implies 3$ set bits. 3 is prime $\implies$ **Counted**.
      - $x = 8$: Binary `1000` $\implies 1$ set bit. 1 is not prime $\implies$ Discarded.
      - $x = 9$: Binary `1001` $\implies 2$ set bits. 2 is prime $\implies$ **Counted**.
      - $x = 10$: Binary `1010` $\implies 2$ set bits. 2 is prime $\implies$ **Counted**.
      - Total matching integers: $1 + 1 + 0 + 1 + 1 = \mathbf{4}$.
- **Bounded Bitness & Static Prime Set Invariant:**
  - **Upper Bound on Bit Count:**
    - The problem constraints specify $right \le 10^6$.
    - Since $2^{19} = 524{,}288 < 10^6 < 2^{20} = 1{,}048{,}576$:
      - Any integer $x \le 10^6$ can have at most **19 set bits**!
      - Thus, $\text{popcount}(x) \in [0, 19]$.
  - **The Complete Prime Target Set ($\mathcal{P}$):**
    - The prime numbers strictly less than 20 are completely enumerated as:
      $$
      \mathcal{P} = \{ 2, \; 3, \; 5, \; 7, \; 11, \; 13, \; 17, \; 19 \}
      $$
    - Testing primality requires only checking if $\text{popcount}(x) \in \mathcal{P}$, which runs in $\mathcal{O}(1)$ time using a hash set or bitmask!
  - **Range Summation:**
    $$
    ans = \sum_{x = left}^{right} \mathbf{1}_{[\text{popcount}(x) \in \mathcal{P}]}
    $$
- **Step-by-Step Worked Execution Trace on Range $[6, 10]$:**
  - Define prime predicate set: $\mathcal{P} = \{2, 3, 5, 7, 11, 13, 17, 19\}$.
  - Initialize counter: $ans = 0$.
  - **Integer $x = 6$:**
    - Binary representation:
      $$
      6 = 4 + 2 = (110)_2
      $$
    - Population count:
      $$
      \text{popcount}(6) = \mathbf{2}
      $$
    - Set membership: $2 \in \mathcal{P} \implies \mathbf{Prime!}$
    - Increment: $ans \leftarrow 0 + 1 = \mathbf{1}$.
  - **Integer $x = 7$:**
    - Binary representation:
      $$
      7 = 4 + 2 + 1 = (111)_2
      $$
    - Population count:
      $$
      \text{popcount}(7) = \mathbf{3}
      $$
    - Set membership: $3 \in \mathcal{P} \implies \mathbf{Prime!}$
    - Increment: $ans \leftarrow 1 + 1 = \mathbf{2}$.
  - **Integer $x = 8$:**
    - Binary representation:
      $$
      8 = 2^3 = (1000)_2
      $$
    - Population count:
      $$
      \text{popcount}(8) = \mathbf{1}
      $$
    - Set membership: $1 \notin \mathcal{P} \implies \mathbf{Not\ Prime.}$
    - Counter unchanged: $ans = 2$.
  - **Integer $x = 9$:**
    - Binary representation:
      $$
      9 = 8 + 1 = (1001)_2
      $$
    - Population count:
      $$
      \text{popcount}(9) = \mathbf{2}
      $$
    - Set membership: $2 \in \mathcal{P} \implies \mathbf{Prime!}$
    - Increment: $ans \leftarrow 2 + 1 = \mathbf{3}$.
  - **Integer $x = 10$:**
    - Binary representation:
      $$
      10 = 8 + 2 = (1010)_2
      $$
    - Population count:
      $$
      \text{popcount}(10) = \mathbf{2}
      $$
    - Set membership: $2 \in \mathcal{P} \implies \mathbf{Prime!}$
    - Increment: $ans \leftarrow 3 + 1 = \mathbf{4}$.
  - **Termination:**
    - Reached $right = 10$.
    - Final result:
      $$
      ans = \mathbf{4}
      $$
- **Range $[10, 15]$ Trace:**
  - $10$ (`1010`): $2 \implies$ Yes
  - $11$ (`1011`): $3 \implies$ Yes
  - $12$ (`1100`): $2 \implies$ Yes
  - $13$ (`1101`): $3 \implies$ Yes
  - $14$ (`1110`): $3 \implies$ Yes
  - $15$ (`1111`): $4 \implies$ No (4 is composite)
  - Total: 5.
- **Power of Two Boundary ($x = 1, 2, 4, 8$):**
  - All powers of two have $\text{popcount}(x) = 1$.
  - Since 1 is not prime, all powers of two evaluate to **0**.

This instance demonstrates finite Hamming weight projection and static sieve reduction over bounded integer domains, mathematically proves why $\lceil \log_2(\max R) \rceil \le 20$ bounds the prime candidate domain to 8 static elements, and derives $O(R - L + 1)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given $[left, right]$:
Count how many numbers have a **prime number of 1s** in their binary representation.

```text
Range: [ 6, 10 ]

6  = 110  -> 2 bits -> PRIME
7  = 111  -> 3 bits -> PRIME
8  = 1000 -> 1 bit  -> NOT prime (1 is not prime!)
9  = 1001 -> 2 bits -> PRIME
10 = 1010 -> 2 bits -> PRIME

4 numbers have a prime number of set bits!
Result: 4
```

### The Invariant of the Finite Prime Set
- Since $right \le 10^6 < 2^{20}$, any number has at most 19 set bits.
- The primes $\le 19$ are strictly $\{2, 3, 5, 7, 11, 13, 17, 19\}$.
- Population count lookup against this static set runs in strictly $O(1)$ time per integer.

---

## 2. Conceptual Foundation & Invariants

### 1. Bounded Prime Set:
$$
\mathcal{P} = \{2, 3, 5, 7, 11, 13, 17, 19\}
$$

### 2. Indicator Aggregation:
$$
ans = \sum_{x = left}^{right} [\text{popcount}(x) \in \mathcal{P}]
$$

> **Hamming Projection Invariant.** The bit count map $w_H: [left, right] \to \{0, \dots, 19\}$ projects into a finite co-domain, where membership in the prime fiber bundle $w_H^{-1}(\mathcal{P})$ is decidable in $O(1)$ machine instructions via CPU popcount.

---

## 3. Step-by-Step Worked Execution

We trace $[6, 10]$:

---

### Step 1: Evaluate Numbers
- $6 \to 2$ set bits $\in \mathcal{P} \implies$ Yes.
- $7 \to 3$ set bits $\in \mathcal{P} \implies$ Yes.
- $8 \to 1$ set bit $\notin \mathcal{P} \implies$ No.
- $9 \to 2$ set bits $\in \mathcal{P} \implies$ Yes.
- $10 \to 2$ set bits $\in \mathcal{P} \implies$ Yes.

---

### Step 2: Sum
- $1 + 1 + 0 + 1 + 1 = \mathbf{4}$.

---

### Step 3: Output
$$
\mathbf{4}
$$

---

## 4. Complete Execution Trace

| Integer $x$ | Binary Form | Set Bit Count $\text{popcount}(x)$ | Prime? ($\in \mathcal{P}$) | Cumulative Total |
|:---:|:---:|:---:|:---:|:---:|
| $6$ | `110` | $2$ | Yes | $1$ |
| $7$ | `111` | $3$ | Yes | $2$ |
| $8$ | `1000` | $1$ | No (1 is not prime) | $2$ |
| $9$ | `1001` | $2$ | Yes | $3$ |
| **$10$** | **`1010`** | **$2$** | **Yes** | **`4`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Number Range ($[6, 6]$):** Returns 1.
- **Number with 1 Set Bit (Powers of 2):** 1 is not prime $\implies$ discarded.
- **Upper Limit ($10^6$):** $10^6 = (11110100001001000000)_2$ has 7 set bits (prime) $\implies$ properly detected.
- **Numbers with 4 Set Bits ($15 = 1111$):** 4 is composite $\implies$ discarded.

---

## 6. Traps & Common Anti-Patterns

- **Treating 1 as Prime:** 1 is neither prime nor composite. Including 1 in the prime set causes false positives on all powers of 2.
- **Dynamic Primality Testing on Every Number:** Running trial division to check if the bit count is prime is unnecessary overhead. Pre-defining the 8 possible primes $\le 19$ enables $O(1)$ set lookup.
- **String Conversion for Bit Counting:** Converting numbers to binary strings `bin(x).count('1')` is much slower than using built-in integer bit count `x.bit_count()` or bitwise operations.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Loop runs $N = right - left + 1$ iterations ($N \le 10^4$).
  - For each number, `bit_count()` and set lookup take $\mathcal{O}(1)$ time.
  - Total Time: strictly linear in range $\mathcal{O}(N)$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ memory for the static prime set containing 8 integers.
