# Guided Example: Nth Digit

We trace the step-by-step digit-length bucket reduction ($k \times 9 \cdot 10^{k-1}$ digits per length class $k$), exact number pinpointing ($num = 10^{k-1} + \lfloor (n-1)/k \rfloor$), intra-number digit extraction ($idx = (n-1) \bmod k$), and logarithmic convergence on representative digit positions:

- **Input:** $n = 11$
- **Required output:** `0`
  - Concatenated sequence: `123456789101112...`
  - Step 1 (Bucket reduction):
    - Length $k = 1$: numbers $1 \dots 9$, capacity $1 \times 9 = 9$ digits
    - $9 < 11 \implies$ Subtract: $n \leftarrow 11 - 9 = 2$, advance to $k = 2$
  - Step 2 (Length $k = 2$ evaluation):
    - Length $k = 2$: numbers $10 \dots 99$, capacity $2 \times 90 = 180$ digits
    - $180 \ge 2 \implies$ The target digit lies in length class $k = 2$
  - Step 3 (Pinpoint host number):
    - Base number for 2 digits: $10^{2-1} = 10$
    - Offset: $\lfloor (2 - 1) / 2 \rfloor = 0$
    - Host number: $num = 10 + 0 = \mathbf{10}$
  - Step 4 (Extract digit within host):
    - Intra-number index: $idx = (2 - 1) \bmod 2 = 1$
    - Digits of $10$: index $0$ is `'1'`, index $1$ is `'0'`
  - Target digit: $\mathbf{0}$
- **Single-Digit Input:** $n = 3 \implies k = 1, num = 3, idx = 0 \implies 3$
- **Boundary Across Tens and Hundreds:** $n = 190 \implies n - 9 - 180 = 1 \implies num = 100, idx = 0 \implies 1$
- **Maximum Bound:** $n = 2^{31} - 1 \approx 2 \times 10^9 \implies k \le 10$, solves in $\le 10$ iterations

This instance demonstrates decomposing semi-infinite combinatorial sequences by digit-length cardinality buckets, mathematically proves the quotient-remainder mapping from continuous indices to discrete decimal digits, and achieves $O(\log_{10} N)$ runtime and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an integer $n = 11$:
Find the $n^{\text{th}}$ digit (1-indexed) of the infinite sequence formed by writing all positive integers in order:
$$
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, \dots
$$

```text
Sequence Stream:  1 2 3 4 5 6 7 8 9 1 0 1 1 1 2 1 3 ...
1-based Index:    1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 ...
                                    0 1 2 3 4 5 6 7
                                      ^
                                 n = 11 -> Digit is '0'
```

### Bucket Cardinality by Digit Count
Instead of generating the string character by character ($O(N)$ time and memory):
- 1-digit numbers: $1 \dots 9 \implies 9$ numbers $\times 1$ digit $= 9$ digits.
- 2-digit numbers: $10 \dots 99 \implies 90$ numbers $\times 2$ digits $= 180$ digits.
- 3-digit numbers: $100 \dots 999 \implies 900$ numbers $\times 3$ digits $= 2700$ digits.
- In general, numbers with $k$ digits span $[10^{k-1}, 10^k - 1]$, contributing exactly:
  $$
  \text{Digits}(k) = k \times 9 \times 10^{k-1}
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. Stage 1: Find the Digit-Length Class $k$
Start with $k = 1, cnt = 9$:
While $n > k \times cnt$:
- Deduct the total digits contributed by all $k$-digit numbers:
  $$
  n \leftarrow n - k \times cnt
  $$
- Advance to the next length class:
  $$
  k \leftarrow k + 1, \quad cnt \leftarrow cnt \times 10
  $$

### 2. Stage 2: Pinpoint the Host Number $num$
The remaining $n$ is now 1-indexed within the $k$-digit class:
- The first $k$-digit number is $10^{k-1}$.
- Each number consumes exactly $k$ digits.
- The host number containing the $n^{\text{th}}$ digit is:
  $$
  num = 10^{k-1} + \left\lfloor \frac{n - 1}{k} \right\rfloor
  $$

### 3. Stage 3: Extract the Specific Digit
- The 0-based index of the target digit within $num$'s string representation is:
  $$
  idx = (n - 1) \bmod k
  $$
- The answer is the $idx^{\text{th}}$ digit of $num$.

> **Invariant.** After the while loop, the target digit is guaranteed to reside inside a $k$-digit number at 0-based character offset $(n - 1) \bmod k$ of $num = 10^{k-1} + \lfloor (n-1)/k \rfloor$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 11$:
Initial: $k = 1, cnt = 9$.

---

### Step 1: Bucket Reduction for $k = 1$
- 1-digit number capacity:
  $$
  k \times cnt = 1 \times 9 = 9
  $$
- Compare: $9 < 11$ (**True**).
- Subtract 1-digit capacity:
  $$
  n \leftarrow 11 - 9 = \mathbf{2}
  $$
- Scale to $k = 2$:
  $$
  k \leftarrow 1 + 1 = \mathbf{2}, \quad cnt \leftarrow 9 \times 10 = \mathbf{90}
  $$

---

### Step 2: Bucket Check for $k = 2$
- 2-digit number capacity:
  $$
  k \times cnt = 2 \times 90 = 180
  $$
- Compare: $180 < 2$ (**False**).
- Target lies within length class $k = 2$.
- While loop terminates.

---

### Step 3: Compute Host Number
- Base 2-digit integer: $10^{k-1} = 10^{2-1} = 10$.
- Remaining offset: $n - 1 = 2 - 1 = 1$.
- Number offset:
  $$
  \left\lfloor \frac{n - 1}{k} \right\rfloor = \left\lfloor \frac{1}{2} \right\rfloor = 0
  $$
- Host integer:
  $$
  num = 10 + 0 = \mathbf{10}
  $$

---

### Step 4: Extract Digit Index
- Intra-number offset:
  $$
  idx = (n - 1) \bmod k = 1 \bmod 2 = \mathbf{1}
  $$
- Convert $num = 10$ to characters:
  - Position 0: `'1'`
  - Position 1: `'0'`
- Result:
  $$
  \mathbf{0}
  $$

---

## 4. Complete Execution Trace

```text
n = 11
k=1, cnt=9  -> k * cnt = 9 < 11 -> n = 11 - 9 = 2, k = 2, cnt = 90
k=2, cnt=90 -> k * cnt = 180 >= 2 -> Loop exits

num = 10^(2-1) + (2 - 1) // 2 = 10 + 0 = 10
idx = (2 - 1) % 2 = 1
str(10)[1] = '0'

Output: 0
```

| Phase | Variable $k$ | Capacity $k \times cnt$ | Remaining $n$ | Condition $k \times cnt < n$ | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---|
| Init | 1 | $1 \times 9 = 9$ | 11 | $9 < 11$ (True) | $n \leftarrow 11 - 9 = 2$, $k \leftarrow 2$ |
| Loop Check | 2 | $2 \times 90 = 180$ | 2 | $180 < 2$ (False) | Loop terminates |
| Host Pinpoint | 2 | - | 2 | - | $num = 10 + 0 = \mathbf{10}$ |
| **Digit Extract**| **2** | - | **2** | - | **$idx = 1 \implies \text{str}(10)[1] = \mathbf{0}$** |

---

### Cross-Boundary Trace ($n = 190$)

```text
n = 190
k = 1: n = 190 - 9 = 181, k = 2
k = 2: n = 181 - 180 = 1, k = 3
k = 3: capacity 2700 >= 1 -> Loop terminates

num = 100 + (1 - 1) // 3 = 100
idx = (1 - 1) % 3 = 0
str(100)[0] = '1' -> Output: 1
```

---

## 5. Algorithmic Correctness

**Soundness.** All integers are partitioned into disjoint contiguous blocks based on digit length $k$. Subtracting block capacities $k \times 9 \cdot 10^{k-1}$ shifts the coordinate frame so that $n$ accurately reflects the position within the block of $k$-digit numbers. Within that block, numbers increment sequentially by 1 every $k$ digits, making $\lfloor (n - 1) / k \rfloor$ the exact integer offset and $(n - 1) \bmod k$ the exact digit offset.

**Completeness.** Since $k \times 9 \cdot 10^{k-1}$ grows exponentially, $n$ will fall within a finite bucket for any 32-bit integer $n \le 2^{31} - 1$ (where $k \le 10$). The formula covers all $n \ge 1$ without edge-case gaps.

---

## 6. Traps This Instance Exposes

- **0-based vs 1-based Offsets:** The input $n$ is 1-indexed. Failing to use $(n - 1)$ in the integer division $\lfloor (n - 1) / k \rfloor$ causes off-by-one errors on boundary numbers (e.g. at the last digit of a number).
- **String Concatenation Memory Limit:** Constructing a sequence string up to length $n = 10^9$ exceeds typical memory limits ($1 \text{ GB}$). Mathematical bucket deduction solves it using negligible space.
- **Power of 10 Overflow:** For $k \le 10$, $10^{k-1}$ and capacities fit comfortably within standard 64-bit integer registers.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log_{10} N)$, where $N = n$.
  - The while loop iterates once per digit-length class $k$.
  - For $N \le 2 \times 10^9$, $k \le 10$, so the loop runs at most 10 times.
  - Final string conversion and indexing takes $O(k) \le 10$ operations.
  - Total runtime is strictly logarithmic $O(\log_{10} N)$, executing in under $0.001$ ms.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory, using only scalar registers $k$, $cnt$, $num$, and $idx$.
