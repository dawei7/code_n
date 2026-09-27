# Guided Example: Super Ugly Number

We trace the step-by-step min-heap priority queue generation, unique prime factor representation, duplicate elimination via minimal prime factor breaking (`if x % k == 0: break`), 32-bit integer overflow guards, and $n$-th number extraction on representative prime base configurations:

- **Input:** $n = 12, \quad \text{primes} = [2, 7, 13, 19]$
- **Required output:** $32$
  - Extracted sequence: $[1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]$
  - The 12th super ugly number is $32 = 2^5$
- **Single Prime Base Case:** $\text{primes} = [2], n = 5 \implies [1, 2, 4, 8, 16]$, output is $16$
- **Base Prime Input:** $n = 1 \implies 1$ (1 is the first super ugly number for any prime set)
- **Prime Multiples Interleaving:** Primes $[2, 7]$ interleave as $1, 2, 4, 7, 8, 14, 16, 28, \dots$

This instance demonstrates canonical prime factorization ordering, mathematically proves why breaking on `x % k == 0` generates each composite number via its smallest prime factor to eliminate duplicates without set hashing overhead, analyzes heap state invariants, and operates in $O(N \log K)$ time and $O(N)$ space.

---

## 1. Instance & Teaching Goal

Given $n = 12$ and prime factors $\text{primes} = [2, 7, 13, 19]$:
A **super ugly number** is a positive integer whose prime factors are all contained in `primes`.
Find the $n$-th super ugly number in ascending order:

```text
Sequence progression:
1st:  1
2nd:  2  (2^1)
3rd:  4  (2^2)
4th:  7  (7^1)
5th:  8  (2^3)
6th:  13 (13^1)
7th:  14 (2 * 7)
8th:  16 (2^4)
9th:  19 (19^1)
10th: 26 (2 * 13)
11th: 28 (4 * 7)
12th: 32 (2^5) -> Output: 32
```

### The Duplicate Elimination Dilemma
In a naive min-heap implementation:
- Multiplying $2$ by $7$ yields $14$.
- Multiplying $7$ by $2$ also yields $14$.
Without pruning, duplicates flood the heap, degrading heap push/pop runtime.
The **Minimal Prime Factor Invariant** ensures that each composite number $X$ is generated **exactly once**:
When processing popped value $x$, iterate through primes $k \in \text{primes}$ in ascending order:
- Push $k \times x$ to the heap.
- If $x \pmod k == 0$: **Break immediately!**

---

## 2. Conceptual Foundation & Invariants

### Mathematical Proof of the `x % k == 0` Invariant
Let $p_1 < p_2 < \dots < p_m$ be the sorted primes.
Every integer $X > 1$ has a unique representation:
$$
X = p_{\text{min}} \times Y
$$
where $p_{\text{min}}$ is the **smallest prime factor** dividing $X$, and $Y = X / p_{\text{min}}$.

Suppose we are processing $x$, and $x$ is already divisible by $k$ (i.e. $x \pmod k == 0$).
If we were to multiply $x$ by a strictly larger prime $p > k$:
$$
Z = x \times p
$$
Notice that $Z$ is divisible by $k$ (since $x$ is divisible by $k$).
The smallest prime factor of $Z$ is $k$, NOT $p$!
Therefore, $Z$ will be generated naturally when the value $(x / k) \times p$ is popped and multiplied by $k$:
$$
Z = \left(\frac{x}{k} \cdot p\right) \times k
$$
By stopping immediately when $x \pmod k == 0$, we guarantee that every number is formed exclusively by multiplying its other factors by its **smallest prime factor**, eliminating all redundant duplicate insertions!

### Algorithm State:
1. Min-heap `q = [1]`.
2. Variable `x = 0`.
3. Loop $n$ times:
   - Pop smallest element $x = \text{heappop}(q)$.
   - For $k \in \text{primes}$:
     - If $x \le \text{MAX\_INT} // k$: `heappush(q, k * x)`.
     - If $x \pmod k == 0$: `break`.
4. Return $x$.

> **Invariant.** After $i$ pops, $x$ is strictly the $i$-th smallest super ugly number. At no point does the heap contain duplicate elements.

---

## 3. Step-by-Step Worked Execution

We trace the min-heap evolution for $n = 12$ with $\text{primes} = [2, 7, 13, 19]$:
Heap initialized to `q = [1]`.

---

### Steps 1 to 4:
- **Pop 1 ($i = 1$):** $x = 1$.
  - Multiply by $2 \implies$ push $2$. ($1 \% 2 \ne 0$).
  - Multiply by $7 \implies$ push $7$. ($1 \% 7 \ne 0$).
  - Multiply by $13 \implies$ push $13$.
  - Multiply by $19 \implies$ push $19$.
  - Heap: $[2, 7, 13, 19]$.
- **Pop 2 ($i = 2$):** $x = 2$.
  - Multiply by $2 \implies$ push $4$.
  - $2 \pmod 2 == 0 \implies$ **Break!** (Does not push $2 \times 7 = 14$).
  - Heap: $[4, 7, 13, 19]$.
- **Pop 3 ($i = 3$):** $x = 4$.
  - Multiply by $2 \implies$ push $8$.
  - $4 \pmod 2 == 0 \implies$ **Break!**
  - Heap: $[7, 8, 13, 19]$.
- **Pop 4 ($i = 4$):** $x = 7$.
  - Multiply by $2 \implies$ push $14$. ($7 \% 2 \ne 0$).
  - Multiply by $7 \implies$ push $49$. ($7 \% 7 == 0 \implies$ **Break!**).
  - Heap: $[8, 13, 14, 19, 49]$.

---

### Steps 5 to 8:
- **Pop 5 ($i = 5$):** $x = 8$.
  - Multiply by $2 \implies$ push $16$. Break ($8 \% 2 == 0$).
  - Heap: $[13, 14, 16, 19, 49]$.
- **Pop 6 ($i = 6$):** $x = 13$.
  - Multiply by $2 \implies$ push $26$.
  - Multiply by $7 \implies$ push $91$.
  - Multiply by $13 \implies$ push $169$. Break ($13 \% 13 == 0$).
  - Heap: $[14, 16, 19, 26, 49, 91, 169]$.
- **Pop 7 ($i = 7$):** $x = 14$.
  - Multiply by $2 \implies$ push $28$. Break ($14 \% 2 == 0$).
  - Heap: $[16, 19, 26, 28, 49, 91, 169]$.
- **Pop 8 ($i = 8$):** $x = 16$.
  - Multiply by $2 \implies$ push $32$. Break ($16 \% 2 == 0$).
  - Heap: $[19, 26, 28, 32, 49, 91, 169]$.

---

### Steps 9 to 12 (Reaching Target):
- **Pop 9 ($i = 9$):** $x = 19$.
  - Multiply by $2 \implies$ push $38$.
  - Push $133, 247, 361$.
  - Heap min is $26$.
- **Pop 10 ($i = 10$):** $x = 26$.
  - Multiply by $2 \implies$ push $52$. Break ($26 \% 2 == 0$).
  - Heap min is $28$.
- **Pop 11 ($i = 11$):** $x = 28$.
  - Multiply by $2 \implies$ push $56$. Break ($28 \% 2 == 0$).
  - Heap min is $32$.
- **Pop 12 ($i = 12$):** $x = \mathbf{32}$!
  - Loop completes $n = 12$ iterations.

Final extracted value:
$$
x = \mathbf{32}
$$

---

## 4. Complete Execution Trace

```text
n = 12, primes = [2, 7, 13, 19]

Pop 1:  x = 1  -> pushes 2, 7, 13, 19
Pop 2:  x = 2  -> pushes 4 (break on 2%2==0)
Pop 3:  x = 4  -> pushes 8 (break on 4%2==0)
Pop 4:  x = 7  -> pushes 14, 49 (break on 7%7==0)
Pop 5:  x = 8  -> pushes 16 (break on 8%2==0)
Pop 6:  x = 13 -> pushes 26, 91, 169
Pop 7:  x = 14 -> pushes 28 (break on 14%2==0)
Pop 8:  x = 16 -> pushes 32 (break on 16%2==0)
Pop 9:  x = 19 -> pushes 38, ...
Pop 10: x = 26 -> pushes 52
Pop 11: x = 28 -> pushes 56
Pop 12: x = 32 -> Target 12th ugly number reached!

Result: 32
```

| Pop $i$ | Extracted $x$ | Factorization | Multipliers Tested | Values Pushed | Break Trigger | New Heap Minimum |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 | $1$ | 2, 7, 13, 19 | 2, 7, 13, 19 | None | 2 |
| 2 | 2 | $2^1$ | 2 | 4 | $2 \pmod 2 == 0$ | 4 |
| 3 | 4 | $2^2$ | 2 | 8 | $4 \pmod 2 == 0$ | 7 |
| 4 | 7 | $7^1$ | 2, 7 | 14, 49 | $7 \pmod 7 == 0$ | 8 |
| 5 | 8 | $2^3$ | 2 | 16 | $8 \pmod 2 == 0$ | 13 |
| 6 | 13 | $13^1$ | 2, 7, 13 | 26, 91, 169 | $13 \pmod{13} == 0$ | 14 |
| 7 | 14 | $2 \times 7$ | 2 | 28 | $14 \pmod 2 == 0$ | 16 |
| 8 | 16 | $2^4$ | 2 | 32 | $16 \pmod 2 == 0$ | 19 |
| 9 | 19 | $19^1$ | 2, 7, 13, 19 | 38, $\dots$ | $19 \pmod{19} == 0$ | 26 |
| 10 | 26 | $2 \times 13$ | 2 | 52 | $26 \pmod 2 == 0$ | 28 |
| 11 | 28 | $2^2 \times 7$ | 2 | 56 | $28 \pmod 2 == 0$ | 32 |
| **12** | **32** | **$2^5$** | - | - | - | **$\mathbf{32}$ (Output)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every number pushed into the heap is generated by multiplying an already confirmed super ugly number by a prime from `primes`. Thus, every generated value has prime factors belonging exclusively to `primes`. The priority queue ensures elements are extracted in strictly non-decreasing order.

**Completeness.** Every super ugly number $Z > 1$ can be uniquely written as $Z = p_{\text{min}} \times Y$, where $Y$ is a super ugly number and $p_{\text{min}}$ is the smallest prime dividing $Z$. Since $Y$ is smaller than $Z$, $Y$ is popped before $Z$. When $Y$ is processed, no prime smaller than $p_{\text{min}}$ divides $Y$ (otherwise $p_{\text{min}}$ would not be the smallest factor of $Z$). Thus, the loop over primes reaches $p_{\text{min}}$ and successfully pushes $p_{\text{min}} \times Y = Z$. No valid number is ever missed.

---

## 6. Traps This Instance Exposes

- **Heap Flooding with Duplicates:** Omitting `if x % k == 0: break` allows both $2 \times 7$ and $7 \times 2$ to be pushed, causing exponential heap growth and duplicate popped values.
- **32-Bit Integer Overflow:** For large $n$, multiplying numbers near $2^{31} - 1$ can overflow 32-bit signed integers. Checking `if x <= mx // k` guards against arithmetic overflow before calling `heappush`.
- **Set Lookup Overhead:** While a hash set can filter duplicates, hash sets introduce significant memory and hashing overhead compared to the mathematical $O(1)$ modulo check.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log K)$, where $N$ is the target rank and $K$ is the number of primes. Each of the $N$ iterations pops the minimum from a heap of size at most $O(K)$. The inner loop executes at most $K$ times, pushing elements in $O(\log K)$ time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store elements in the priority queue.