# Guided Example: Perfect Number

We trace the step-by-step proper divisor definition ($\sum d = num, \; d < num$), square-root paired factor trial division ($i \le \sqrt{num}$), duplicate factor square handling ($i \ne num // i$), edge-case unit handling ($num = 1$), and aliquot sum equality verification on representative positive integers:

- **Input:** $num = 28$
- **Required output:** `true`
  - Definition: A positive integer $num$ is a **perfect number** if the sum of all its positive proper divisors (divisors strictly less than $num$) equals $num$ itself:
    $$
    \sum_{d \mid num, \; d < num} d = num
    $$
- **Square-root trial division execution trace:**
  - Exclude base case $num = 1$ (1 has no proper divisors $\implies$ sum is $0$).
  - Initialize divisor sum: $s = 1$ (1 is a proper divisor of every $num > 1$)
  - Search range for divisor pairs: $i \in [2, \lfloor\sqrt{28}\rfloor] = [2, 5]$
  - **Iteration 1 ($i = 2$):**
    - Divisibility check: $28 \pmod 2 = 0$ (Pass)
    - Paired factor:
      $$
      \text{pair} = 28 / 2 = \mathbf{14}
      $$
    - Since $i (2) \ne \text{pair} (14)$, add both factors:
      $$
      s \leftarrow 1 + 2 + 14 = \mathbf{17}
      $$
  - **Iteration 2 ($i = 3$):**
    - $28 \pmod 3 = 1 \ne 0 \implies$ Skip.
  - **Iteration 3 ($i = 4$):**
    - Divisibility check: $28 \pmod 4 = 0$ (Pass)
    - Paired factor:
      $$
      \text{pair} = 28 / 4 = \mathbf{7}
      $$
    - Since $4 \ne 7$, add both factors:
      $$
      s \leftarrow 17 + 4 + 7 = \mathbf{28}
      $$
  - **Iteration 4 ($i = 5$):**
    - $5 \times 5 = 25 \le 28$. $28 \pmod 5 = 3 \ne 0 \implies$ Skip.
  - Next $i = 6 > \lfloor\sqrt{28}\rfloor \implies$ Division loop terminates.
  - **Proper Divisor Sum:**
    $$
    s = 1 + 2 + 14 + 4 + 7 = \mathbf{28}
    $$
  - Compare with original number:
    $$
    s == num \iff 28 == 28 \quad (\mathbf{True})
    $$
  - Return **`true`**.
- **Prime Number Instance ($num = 7$):**
  - Only proper divisor is $1$. $s = 1 \ne 7 \implies \mathbf{false}$
- **Unit Instance ($num = 1$):**
  - Proper divisors strictly less than 1 are empty $\implies s = 0 \ne 1 \implies \mathbf{false}$
- **Non-Perfect Composite ($num = 6$ vs $num = 12$):**
  - For $num = 6$: divisors $\{1, 2, 3\} \implies 1 + 2 + 3 = 6 \implies \mathbf{true}$
  - For $num = 12$: divisors $\{1, 2, 3, 4, 6\} \implies 16 \ne 12 \implies \mathbf{false}$

This instance demonstrates mathematical factor pairing around $\sqrt{N}$, mathematically proves why testing up to $\sqrt{N}$ discovers all proper divisors, and derives $O(\sqrt{N})$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer $num$:
A **perfect number** is a positive integer that is equal to the sum of its positive divisors, excluding the number itself (its **proper divisors**).
Return `true` if $num$ is a perfect number, and `false` otherwise.

```text
Evaluating num = 28:
  Divisors of 28:         1,  2,  4,  7,  14,  28
  Proper Divisors (< 28): 1,  2,  4,  7,  14

  Sum = 1 + 2 + 4 + 7 + 14 = 28 == num

28 is a Perfect Number -> true!
```

### The Factor Symmetry Theorem
Every divisor $d$ of $num$ has a unique complementary partner:
$$
d' = \frac{num}{d}
$$
- If $d \le \sqrt{num}$, then $d' \ge \sqrt{num}$.
- By checking integers $i$ from $2$ up to $\lfloor\sqrt{num}\rfloor$:
  Whenever $num \pmod i == 0$, we find **both** $i$ and its partner $num // i$ simultaneously in $O(1)$ operations!
- This reduces the divisor search from $O(N)$ down to $O(\sqrt{N})$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Proper Divisor Sum Algorithm:
1. Special case: If $num == 1$, return `False` (1 has no positive integer strictly less than itself).
2. Initialize sum with the universal proper divisor:
   $$
   s = 1
   $$
3. Loop $i = 2, 3, \dots$ while $i \le \lfloor num / i \rfloor$:
   - If $num \pmod i == 0$:
     $$
     s \leftarrow s + i
     $$
     If $i \ne num // i$ (not a perfect square root):
     $$
     s \leftarrow s + \frac{num}{i}
     $$
4. Check if $s == num$.

### 2. Perfect Square Safeguard:
For square numbers like $num = 16$:
At $i = 4$, $16 / 4 = 4$.
The condition `if i != num // i` prevents adding $4$ twice to the divisor sum.

> **Proper Divisor Invariant.** At all times, every integer $d$ added to $s$ satisfies $d \mid num$ and $1 \le d < num$, ensuring the final sum is the exact aliquot sum $\sigma_1(num) - num$.

---

## 3. Step-by-Step Worked Execution

We trace $num = 28$:

---

### Step 1: Base Case & Setup
- $num = 28 \ne 1$.
- Initialize $s = 1, \; i = 2$.

---

### Step 2: Factor Pairing Loop ($i \le 28 // i$)

1. **Iteration $i = 2$ ($2 \le 14$):**
   - $28 \pmod 2 = 0$ (Divisor found!).
   - Add factor $2$: $s \leftarrow 1 + 2 = 3$.
   - Partner factor: $28 / 2 = 14$.
   - Since $2 \ne 14$: add partner:
     $$
     s \leftarrow 3 + 14 = \mathbf{17}
     $$
   - Advance $i \leftarrow 3$.

2. **Iteration $i = 3$ ($3 \le 9$):**
   - $28 \pmod 3 = 1 \ne 0$.
   - Advance $i \leftarrow 4$.

3. **Iteration $i = 4$ ($4 \le 7$):**
   - $28 \pmod 4 = 0$ (Divisor found!).
   - Add factor $4$: $s \leftarrow 17 + 4 = 21$.
   - Partner factor: $28 / 4 = 7$.
   - Since $4 \ne 7$: add partner:
     $$
     s \leftarrow 21 + 7 = \mathbf{28}
     $$
   - Advance $i \leftarrow 5$.

4. **Iteration $i = 5$ ($5 \le 5$):**
   - $28 \pmod 5 = 3 \ne 0$.
   - Advance $i \leftarrow 6$.

5. **Loop Termination:**
   - $i = 6 > 28 // 6 (4) \implies$ Loop halts.

---

### Step 3: Equality Test
$$
s == num \iff 28 == 28 \implies \mathbf{True}
$$

---

## 4. Complete Execution Trace

| Divisor Candidate $i$ | Divisibility $num \pmod i$ | Paired Divisor $num // i$ | Equal Factors? | Divisors Added | Cumulative Sum $s$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init** | — | — | — | $1$ | $1$ |
| **$2$** | $28 \pmod 2 = 0$ | $14$ | No ($2 \ne 14$) | $2 + 14 = 16$ | $1 + 16 = \mathbf{17}$ |
| **$3$** | $28 \pmod 3 = 1$ | — | — | None | $17$ |
| **$4$** | $28 \pmod 4 = 0$ | $7$ | No ($4 \ne 7$) | $4 + 7 = 11$ | $17 + 11 = \mathbf{28}$ |
| **$5$** | $28 \pmod 5 = 3$ | — | — | None | $28$ |
| **Final** | — | — | — | — | **$s = 28 == num \implies \text{true}$** |

---

## 5. Boundary Cases & Failure Modes

- **$num = 1$:** 1 has no proper divisors strictly less than 1 $\implies \mathbf{false}$.
- **Prime Numbers ($num = 13$):** No factors in $[2, \sqrt{13}] \implies s = 1 \ne 13 \implies \mathbf{false}$.
- **First Known Perfect Numbers:**
  - $6 \implies 1 + 2 + 3 = 6$ (**true**)
  - $28 \implies 1 + 2 + 4 + 7 + 14 = 28$ (**true**)
  - $496 \implies 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = 496$ (**true**)
  - $8128$ (**true**)
- **Negative or Zero Numbers:** Perfect numbers are defined strictly over positive integers.

---

## 6. Traps & Common Anti-Patterns

- **Scanning All Numbers Up to $N$ ($O(N)$):** For $num = 10^8$, looping from $1$ to $N$ takes $10^8$ operations, causing Time Limit Exceeded. Bounding the loop at $\sqrt{num}$ takes only $10^4$ operations.
- **Double-Counting the Square Root ($i^2 == num$):** For $num = 16$, $4 \times 4 = 16$. If you add both $i$ and $num // i$ without checking $i \ne num // i$, 4 is added twice, yielding an incorrect sum.
- **Adding $num$ to the Sum:** A proper divisor must be *strictly less* than $num$. Starting $s = 0$ and checking up to $num$ would include $num$ itself, requiring subtracting it back out. Starting with $s = 1$ avoids including $num$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The loop terminates when $i > \lfloor\sqrt{num}\rfloor$.
  - Number of iterations is strictly bounded by $\sqrt{num}$.
  - Total Time: $\mathcal{O}(\sqrt{num})$. For $num \le 10^8$, $\sqrt{10^8} = 10^4$ operations, completing in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ using scalar integer accumulators.
