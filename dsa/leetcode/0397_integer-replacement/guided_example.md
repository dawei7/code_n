# Guided Example: Integer Replacement

We trace the step-by-step greedy bitwise reduction strategy ($n \gg 1$ for evens, lowest-2-bits test $(n \ \& \ 3) == 3$ for odds), trailing zero cascade maximization, special handling of boundary base case $n = 3$, and logarithmic convergence on representative integer instances:

- **Input:** $n = 7$
- **Required output:** $4$
  - Step 1: $n = 7 = 111_2$
    - Odd, ends in binary `11` ($n \ \& \ 3 == 3$) and $n \ne 3$
    - Greedy choice: $n \leftarrow 7 + 1 = \mathbf{8}$ (turns `111` into `1000`, creating 3 trailing zeros!)
    - Operations: $1$
  - Step 2: $n = 8 = 1000_2 \implies n \leftarrow 8 / 2 = \mathbf{4}$ (Operations: $2$)
  - Step 3: $n = 4 = 100_2 \implies n \leftarrow 4 / 2 = \mathbf{2}$ (Operations: $3$)
  - Step 4: $n = 2 = 10_2 \implies n \leftarrow 2 / 2 = \mathbf{1}$ (Operations: $4$)
  - Target $n = 1$ reached in $\mathbf{4}$ steps ($7 \to 8 \to 4 \to 2 \to 1$)
- **The $n = 3$ Exception:** $n = 3 = 11_2$
  - Even though $3 \ \& \ 3 == 3$, decrementing is strictly better:
    - $3 - 1 = 2 \to 1$ takes **2 steps**
    - $3 + 1 = 4 \to 2 \to 1$ takes **3 steps**
  - Exception rule correctly chooses $3 - 1 = 2$
- **Even Power of Two:** $n = 8 \implies 8 \to 4 \to 2 \to 1$ (3 steps)
- **Large Bound:** $n = 2^{31} - 1 \implies$ requires 32 bit-shift iterations in $O(\log n)$ time

This instance demonstrates bit-manipulation greedy invariants, mathematically proves why maximizing trailing zeros in binary minimizes total divisions and additions, contrasts $O(\log N)$ bitwise greed against exponential recursion, and operates in $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given a positive integer $n = 7$:
Apply the following operations to reduce $n$ to $1$ in the **minimum number of operations**:
1. If $n$ is even: $n \leftarrow n / 2$.
2. If $n$ is odd: choose either $n \leftarrow n + 1$ or $n \leftarrow n - 1$.

```text
Decision Tree for n = 7:
Option A (Add 1):      7 -> 8 -> 4 -> 2 -> 1  (4 operations)  <- OPTIMAL!
Option B (Subtract 1): 7 -> 6 -> 3 -> 2 -> 1  (4 operations, via 3-1)
                       7 -> 6 -> 3 -> 4 -> 2 -> 1 (5 operations, via 3+1)

For larger odd numbers like 15:
Option A: 15 -> 16 -> 8 -> 4 -> 2 -> 1  (5 operations)  <- OPTIMAL!
Option B: 15 -> 14 -> 7 -> 8 -> 4 -> 2 -> 1 (6 operations)
```

### Why Binary Bit Representation Explains the Greedy Choice
Division by 2 is a right bit-shift ($n \gg 1$). To reduce $n$ to 1 as fast as possible, we want to maximize the number of **trailing zeros** created after each step:
- If $n$ is even (`n & 1 == 0`): shift right immediately.
- If $n$ is odd (`n & 1 == 1`), look at its last two bits (`n & 3`):
  - **Case `n & 3 == 3` (Binary `...11`):**
    Adding $1$ carries over: `...011` $+ 1 =$ `...100`.
    This replaces two ones with **at least two trailing zeros**, enabling multiple successive divisions by 2!
  - **Case `n & 3 == 1` (Binary `...01`):**
    Subtracting $1$ clears the bit: `...001` $- 1 =$ `...000`.
    This produces at least two trailing zeros!
  - **The Sole Exception ($n = 3$):**
    Binary $3 = 11_2$. Here, $3 - 1 = 2 \to 1$ (2 steps), whereas $3 + 1 = 4 \to 2 \to 1$ (3 steps). Therefore, $n = 3$ must subtract 1.

---

## 2. Conceptual Foundation & Invariants

### 1. The Greedy Bitwise State Machine:
While $n > 1$:
1. **Even Branch:**
   If $(n \ \& \ 1) == 0$:
   $$
   n \leftarrow n \gg 1
   $$
2. **Odd Branch with Double Ones ($n \ \& \ 3 == 3$ and $n \ne 3$):**
   $$
   n \leftarrow n + 1
   $$
3. **Odd Branch Otherwise ($n == 3$ or $n \ \& \ 3 == 1$):**
   $$
   n \leftarrow n - 1
   $$
4. Increment step counter: $ans \leftarrow ans + 1$.

> **Invariant.** Every step maximizes the number of trailing zero bits available for subsequent divisions, minimizing total transitions without backtracking.

---

## 3. Step-by-Step Worked Execution

We trace $n = 7$:
Initial: $n = 7, ans = 0$.

---

### Step 1: $n = 7$
- Binary: $7 = 111_2$.
- Parity: $(7 \ \& \ 1) == 1$ (Odd).
- Lowest 2 bits: $7 \ \& \ 3 = 3$ (Binary ends in `11`).
- Since $n \ne 3$, apply $+1$:
  $$
  n \leftarrow 7 + 1 = \mathbf{8} \quad (1000_2)
  $$
- Operations: $ans \leftarrow 0 + 1 = \mathbf{1}$.

---

### Step 2: $n = 8$
- Binary: $8 = 1000_2$.
- Parity: Even $\implies n \leftarrow 8 \gg 1 = \mathbf{4}$.
- Operations: $ans \leftarrow 1 + 1 = \mathbf{2}$.

---

### Step 3: $n = 4$
- Binary: $4 = 100_2$.
- Parity: Even $\implies n \leftarrow 4 \gg 1 = \mathbf{2}$.
- Operations: $ans \leftarrow 2 + 1 = \mathbf{3}$.

---

### Step 4: $n = 2$
- Binary: $2 = 10_2$.
- Parity: Even $\implies n \leftarrow 2 \gg 1 = \mathbf{1}$.
- Operations: $ans \leftarrow 3 + 1 = \mathbf{4}$.

---

### Step 5: Termination
$n = 1$. Loop exits.
Return:
$$
ans = \mathbf{4}
$$

---

## 4. Complete Execution Trace

```text
n = 7
Step 1: n = 7 (111_2)  -> odd, n & 3 == 3, n != 3 -> n = 7 + 1 = 8 (1000_2) -> ans = 1
Step 2: n = 8 (1000_2) -> even                   -> n = 8 >> 1 = 4 (100_2)  -> ans = 2
Step 3: n = 4 (100_2)  -> even                   -> n = 4 >> 1 = 2 (10_2)   -> ans = 3
Step 4: n = 2 (10_2)   -> even                   -> n = 2 >> 1 = 1 (1_2)    -> ans = 4
Target n = 1 reached -> Return ans = 4
```

| Step | State $n$ | Binary Representation | Condition Checked | Action Selected | Next $n$ | Total Steps $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 7 | $111_2$ | $n \ \& \ 3 == 3 \land n \ne 3$ | $n \leftarrow n + 1$ | 8 | 1 |
| 2 | 8 | $1000_2$ | Even ($n \ \& \ 1 == 0$) | $n \leftarrow n \gg 1$ | 4 | 2 |
| 3 | 4 | $100_2$ | Even ($n \ \& \ 1 == 0$) | $n \leftarrow n \gg 1$ | 2 | 3 |
| **4** | **2** | **$10_2$** | **Even ($n \ \& \ 1 == 0$)** | **$n \leftarrow n \gg 1$** | **1** | **$\mathbf{4}$** |
| **Exit**| 1 | $1_2$ | $n == 1$ | Terminate | - | **`4` (Final)** |

---

### The $n = 3$ Special Case Comparison

```text
n = 3 (11_2):
If applying +1: 3 -> 4 -> 2 -> 1 (3 steps)
If applying -1: 3 -> 2 -> 1      (2 steps) -> OPTIMAL!

Handled by guard condition `n != 3`:
When n = 3, goes to `else: n -= 1`, choosing the 2-step path.
```

---

## 5. Algorithmic Correctness

**Soundness.** Every addition or subtraction on an odd number produces an even number. If an odd number has binary suffix `01`, subtracting 1 yields suffix `00` (divisible by 4), allowing at least two subsequent divisions; adding 1 yields suffix `10` (divisible only by 2). Conversely, if it has binary suffix `11`, adding 1 produces a carry cascade resulting in suffix `00` (divisible by 4 or higher powers of 2). Because dividing by 2 strictly reduces the bit-length of $n$ while additions and subtractions only alter the lowest bits, this greedy choice is provably optimal for all $n > 3$.

**Completeness.** In each iteration, $n$ decreases either by half (for even $n$) or by 1 (for $n = 3$) or transforms into a multiple of 4 (for other odd $n$, which immediately halves twice). The sequence is strictly monotonically decreasing over every 2-step window, guaranteeing rapid convergence to 1.

---

## 6. Traps This Instance Exposes

- **Exponential Recursion TLE:** A naive recursion `min(solve(n+1), solve(n-1)) + 1` exhibits $O(2^d)$ branching without memoization and exceeds Python recursion limits for $n \approx 10^9$.
- **The $n = 3$ Exception:** Blindly checking `n & 3 == 3` causes $n = 3$ to transition to 4 (taking 3 steps total), missing the 2-step path $3 \to 2 \to 1$.
- **32-Bit Overflow ($n = 2^{31} - 1$):** When $n = 2147483647$, $n + 1 = 2147483648$, which overflows signed 32-bit integers in C++/Java. Python automatically uses arbitrary-precision integers, handling this without overflow.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$, where $N = n$.
  - At every odd step, the operation creates at least two trailing zeros, followed immediately by at least two divisions by 2.
  - The number of bits in $n$ is $\lfloor \log_2 N \rfloor + 1$.
  - Total iterations cannot exceed $2 \log_2 N$. For $N = 2^{31} - 1$, the loop terminates in $\le 32$ iterations ($< 0.001$ ms).
- **Auxiliary Space Complexity:** $O(1)$ constant memory, requiring only scalar variables `n` and `ans`.