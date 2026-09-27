# Guided Example: Count Primes

We trace the step-by-step Sieve of Eratosthenes boolean state elimination, composite factor marking from $p^2$, and prime counting on representative integer bounds:

- **Input:** $n = 10$
- **Required output:** $4$ (Primes strictly less than 10 are $2, 3, 5, 7$)
- **Prime Upper Bound Instance:** $n = 7 \implies 3$ (Primes are $2, 3, 5$; $7$ is excluded by strict inequality $< n$)
- **Base Boundary Instances:**
  - $n = 0 \implies 0$
  - $n = 1 \implies 0$
  - $n = 2 \implies 0$ (No primes strictly less than 2)
  - $n = 3 \implies 1$ (Prime 2)

This instance demonstrates the classical Sieve of Eratosthenes, proves why composite marking starts at $p^2$ rather than $2p$, details the Mertens-Landau harmonic prime sum divergence ($\sum 1/p \approx \ln \ln n$), and operates in $O(N \log \log N)$ time with $O(N)$ space.

---

## 1. Instance & Teaching Goal

Given an integer $n = 10$:
Count the number of prime numbers strictly less than $n$ (in the interval $[2, n-1]$).
Listing integers in $[2, 9]$:
- $2$: Prime
- $3$: Prime
- $4$: Composite ($2 \times 2$)
- $5$: Prime
- $6$: Composite ($2 \times 3$)
- $7$: Prime
- $8$: Composite ($2 \times 4$)
- $9$: Composite ($3 \times 3$)
Total primes: $\{2, 3, 5, 7\} \implies \mathbf{4}$.

Individual primality testing using trial division takes $O(\sqrt{x})$ per number, yielding $O(N \sqrt{N})$ total time, which times out when $n = 5 \times 10^6$.
The **Sieve of Eratosthenes** computes all primes in the range in bulk:
- Start with all numbers assumed prime.
- As each prime $p$ is discovered, mark all its multiples as composite.
- By starting composite marking at $p^2$, all redundant duplicate visits from smaller factors are eliminated.

---

## 2. Conceptual Foundation & Invariants

### The Sieve Protocol
Let $A$ be a boolean array of size $n$, where $A[i] = \text{True}$ indicates that integer $i$ is currently candidate prime:
1. **Base Initialization:**
   If $n \le 2$, return $0$.
   Initialize $A[0] = A[1] = \text{False}$, and $A[2 \dots n-1] = \text{True}$.
2. **Composite Filtering (Outer Loop $p \le \sqrt{n-1}$):**
   For $p = 2, 3, \dots, \lfloor \sqrt{n-1} \rfloor$:
   - If $A[p] == \text{True}$:
     $p$ has no factors strictly between $1$ and $p$, so $p$ is prime.
     Mark all multiples of $p$ starting from $p^2$ as composite:
     $$
     \text{for } m = p^2, p^2 + p, p^2 + 2p, \dots < n: \quad A[m] \leftarrow \text{False}
     $$
3. **Prime Count Aggregation:**
   $$
   \text{return } \sum_{i=2}^{n-1} A[i]
   $$

### Why Mark Multiples Starting from $p^2$?
Any composite number $c < p^2$ that has $p$ as a factor must have the form:
$$
c = k \cdot p \quad \text{where } k < p
$$
Because $k < p$, $k$ possesses at least one prime factor $q \le k < p$.
Therefore, $c$ has already been marked composite during the earlier sieve pass for prime $q$!
Starting at $p^2$ avoids re-marking smaller composites.

> **Invariant.** Before starting iteration $p$, for every integer $x < p^2$, $A[x] = \text{True}$ if and only if $x$ is prime.

---

## 3. Step-by-Step Worked Execution

We trace the sieve for $n = 10$ ($N = 10$, indices $0 \dots 9$):

### Step 0: Initial State
$$
A = [\text{F}, \text{F}, \text{T}, \text{T}, \text{T}, \text{T}, \text{T}, \text{T}, \text{T}, \text{T}]
$$
Indices: $0, 1$ are $\text{False}$; $2 \dots 9$ are $\text{True}$.
Outer loop bound: $p \le \lfloor \sqrt{9} \rfloor = 3$.

---

### Step 1: Prime $p = 2$
- $A[2] = \text{True} \implies \mathbf{2 \text{ is prime!}}$
- Mark multiples starting from $p^2 = 2^2 = \mathbf{4}$, stepping by $2$:
  - $m = 4$: $A[4] \leftarrow \text{False}$.
  - $m = 6$: $A[6] \leftarrow \text{False}$.
  - $m = 8$: $A[8] \leftarrow \text{False}$.
- Array state:
  $$
  A = [\text{F}, \text{F}, \mathbf{T}, \mathbf{T}, \mathbf{F}, \text{T}, \mathbf{F}, \text{T}, \mathbf{F}, \text{T}]
  $$

---

### Step 2: Prime $p = 3$
- $A[3] = \text{True} \implies \mathbf{3 \text{ is prime!}}$
- Mark multiples starting from $p^2 = 3^2 = \mathbf{9}$, stepping by $3$:
  - $m = 9$: $A[9] \leftarrow \text{False}$.
- Array state:
  $$
  A = [\text{F}, \text{F}, \mathbf{T}, \mathbf{T}, \mathbf{F}, \mathbf{T}, \mathbf{F}, \mathbf{T}, \mathbf{F}, \mathbf{F}]
  $$

---

### Step 3: Loop Termination ($p > \sqrt{9}$)
- Sieve loop bound reached ($p > 3$).
- Remaining unmarked numbers $\ge 4$ (specifically $5$ and $7$) are certified prime!

---

### Step 4: Final Count
Sum remaining `True` values across $A[2 \dots 9]$:
- $A[2] = \text{True}$
- $A[3] = \text{True}$
- $A[5] = \text{True}$
- $A[7] = \text{True}$

Total prime count: $\mathbf{4}$.

---

## 4. Complete Execution Trace

```text
Initial Array (size 10):
Idx: 0  1  2  3  4  5  6  7  8  9
Val: F  F  T  T  T  T  T  T  T  T

p = 2: Mark multiples starting at 2*2=4, step 2 (4, 6, 8)
Val: F  F  T  T  F  T  F  T  F  T

p = 3: Mark multiples starting at 3*3=9, step 3 (9)
Val: F  F  T  T  F  T  F  T  F  F

Outer loop finishes (p <= sqrt(10)).
True indices: 2, 3, 5, 7 -> Count = 4
```

| Pass | Tested Prime $p$ | Starting Multiple $p^2$ | Multiples Marked Composite | Updated Boolean Array $A[2 \dots 9]$ |
|:---:|:---:|:---:|:---|:---|
| Init | - | - | $0, 1$ set to False | `[T, T, T, T, T, T, T, T]` |
| **1** | **$p = 2$** | **$4$** | **$4, 6, 8$** | `[T, T, F, T, F, T, F, T]` |
| **2** | **$p = 3$** | **$9$** | **$9$** | `[T, T, F, T, F, T, F, F]` |
| End | $p > \sqrt{9}$ | - | Sieve complete | **Count of `True` = $4$** |

---

## 5. Algorithmic Correctness

**Soundness.** Any number $m$ marked False is of the form $k \cdot p$ with $k \ge 2$, meaning it has a non-trivial factor $p > 1$ and is composite. No prime number is ever marked False.

**Completeness.** Every composite number $c < n$ has a prime factor $p \le \sqrt{c} < \sqrt{n}$. When the sieve reaches this prime factor $p$, $c$ is marked False because $c \ge p^2$ and $c$ is a multiple of $p$. Thus, every composite is eliminated.

---

## 6. Traps This Instance Exposes

- **Strict Inequality `< n`:** The problem asks for primes *strictly less than* $n$. If $n = 7$, $7$ itself is prime but must not be counted (result is $3$, for primes $2, 3, 5$). Allocating an array of size $n$ guarantees that index $n$ is never included.
- **Starting at $2p$ Instead of $p^2$:** Marking from $2p$ is correct but wastes significant time re-marking even numbers ($4, 6, 8, \dots$) during later prime passes. Starting at $p^2$ avoids this overhead.
- **Base Cases $n \le 2$:** If $n = 0, 1, 2$, there are no primes strictly less than $n$. Guarding with `if n <= 2: return 0` avoids negative range indexing.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log \log N)$. Summing the work done across all primes $p \le \sqrt{N}$:
  $$
  \sum_{p \le N} \frac{N}{p} = N \sum_{p \le N} \frac{1}{p} \approx N \ln(\ln N)
  $$
  By Mertens' second theorem, the harmonic sum of primes diverges as $\ln \ln N$, making the runtime nearly linear.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space for the boolean sieve array.
