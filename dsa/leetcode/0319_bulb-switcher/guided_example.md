# Guided Example: Bulb Switcher

We trace the step-by-step mathematical reduction from round-by-round toggle simulation to divisor parity analysis, prove why perfect squares have an odd number of factors, and extract the count of active bulbs via integer square root $\lfloor \sqrt{n} \rfloor$ on representative instances:

- **Input:** $n = 10$
- **Required output:** $3$ (Bulbs at positions $1, 4, 9$ remain ON; all other bulbs finish OFF)
- **Large Bound Instance:** $n = 10^9 \implies \lfloor \sqrt{10^9} \rfloor = 31622$
- **Small Bound Instances:**
  - $n = 0 \implies 0$ (No bulbs exist)
  - $n = 1 \implies 1$ (Bulb 1 toggled in round 1, remains ON)
  - $n = 3 \implies 1$ (Bulb 1 ON, Bulb 2 OFF, Bulb 3 OFF)
  - $n = 4 \implies 2$ (Bulbs 1 and 4 remain ON)

This instance demonstrates mathematical symmetry and number-theoretic reduction, proves why divisors pair up as $(d, k/d)$ unless $d = \sqrt{k}$, demonstrates why simulating $O(N \log N)$ rounds causes Time Limit Exceeded when $n = 10^9$, and achieves $O(1)$ constant time and auxiliary space.

---

## 1. Instance & Teaching Goal

There are $n = 10$ bulbs numbered $1$ to $10$, initially all **OFF**.
You perform $10$ rounds of switching:
- Round 1: Toggle every 1st bulb (multiples of 1: all bulbs turned ON).
- Round 2: Toggle every 2nd bulb (multiples of 2: 2, 4, 6, 8, 10 turned OFF).
- Round 3: Toggle every 3rd bulb (multiples of 3: 3, 6, 9 toggled).
- $\dots$
- Round $i$: Toggle every $i$-th bulb.
- Round 10: Toggle the 10th bulb.

Find how many bulbs remain **ON** after all $10$ rounds:

```text
Round-by-Round Bulb States (n = 10):
Bulb:    1    2    3    4    5    6    7    8    9    10
Init:   OFF  OFF  OFF  OFF  OFF  OFF  OFF  OFF  OFF  OFF
Rnd 1:  ON   ON   ON   ON   ON   ON   ON   ON   ON   ON
Rnd 2:  ON   OFF  ON   OFF  ON   OFF  ON   OFF  ON   OFF
Rnd 3:  ON   OFF  OFF  OFF  ON   ON   ON   OFF  OFF  OFF
Rnd 4:  ON   OFF  OFF  ON   ON   ON   ON   OFF  OFF  OFF
Rnd 5:  ON   OFF  OFF  ON   OFF  ON   ON   OFF  OFF  ON
Rnd 6:  ON   OFF  OFF  ON   OFF  OFF  ON   OFF  OFF  ON
Rnd 7:  ON   OFF  OFF  ON   OFF  OFF  OFF  OFF  OFF  ON
Rnd 8:  ON   OFF  OFF  ON   OFF  OFF  OFF  ON   OFF  ON
Rnd 9:  ON   OFF  OFF  ON   OFF  OFF  OFF  ON   ON   ON
Rnd 10: ON   OFF  OFF  ON   OFF  OFF  OFF  ON   ON   OFF

Final ON bulbs: {1, 4, 9} -> Exactly 3 bulbs!
```

### The Infeasibility of Direct Simulation
- Simulating $n$ rounds requires $\sum_{i=1}^n \frac{n}{i} = n \ln n$ toggles.
- For $n = 10^9$, $n \ln n \approx 2.07 \times 10^{10}$ operations and $1$ GB of memory, causing immediate memory and time limits.
- Instead, analyze each bulb's behavior **independently** via its divisors!

---

## 2. Conceptual Foundation & Invariants

### 1. Toggle Condition Equals Divisor Count
Bulb $k$ is toggled in round $d$ if and only if $d$ divides $k$.
Therefore:
$$
\text{Total Toggles}(k) = \text{number of positive divisors of } k
$$
Because the bulb begins in the **OFF** state:
- An **even** number of toggles leaves the bulb **OFF** ($\text{OFF} \to \text{ON} \to \dots \to \text{OFF}$).
- An **odd** number of toggles leaves the bulb **ON** ($\text{OFF} \to \text{ON} \to \dots \to \text{ON}$).

### 2. Divisor Symmetry and Perfect Squares
For any integer $k$, its positive divisors naturally pair up:
$$
(d, \; k / d)
$$
- For example, if $k = 12$, the pairs are $(1, 12), (2, 6), (3, 4)$.
  All pairs consist of two distinct integers, so the total number of divisors is even ($6$).
- A divisor pairs with itself if and only if:
  $$
  d = \frac{k}{d} \iff d^2 = k
  $$
  This condition holds **if and only if $k$ is a perfect square**!
- If $k$ is a perfect square (e.g. $k = 9$):
  Divisors are $1, 3, 9$. The pairs are $(1, 9)$ and the self-paired $(3, 3)$.
  The divisor count is strictly **odd** ($3$ divisors).

### 3. The Closed-Form Formula
Only bulbs at positions that are **perfect squares** ($1^2, 2^2, 3^2, \dots$) remain ON.
The number of perfect squares $\le n$ is given by:
$$
\text{Result} = \lfloor \sqrt{n} \rfloor
$$

> **Invariant.** Bulb $k$ finishes ON if and only if $k$ is a perfect square. The total count of active bulbs in $[1, n]$ is identically $\lfloor \sqrt{n} \rfloor$.

---

## 3. Step-by-Step Worked Execution

We trace the divisor parity analysis on $n = 10$:

---

### Step 1: Enumerate Divisors for Each Bulb $k \in [1, 10]$

1. **Bulb 1:**
   - Divisors: $\{1\}$.
   - Count: $1$ (Odd).
   - Final state: **ON** ($1 = 1^2$).
2. **Bulb 2:**
   - Divisors: $\{1, 2\}$. Pairs: $(1, 2)$.
   - Count: $2$ (Even).
   - Final state: **OFF**.
3. **Bulb 3:**
   - Divisors: $\{1, 3\}$. Pairs: $(1, 3)$.
   - Count: $2$ (Even).
   - Final state: **OFF**.
4. **Bulb 4:**
   - Divisors: $\{1, 2, 4\}$. Pairs: $(1, 4), (2, 2)$.
   - Count: $3$ (Odd).
   - Final state: **ON** ($4 = 2^2$).
5. **Bulb 5:**
   - Divisors: $\{1, 5\}$. Pairs: $(1, 5)$.
   - Count: $2$ (Even).
   - Final state: **OFF**.
6. **Bulb 6:**
   - Divisors: $\{1, 2, 3, 6\}$. Pairs: $(1, 6), (2, 3)$.
   - Count: $4$ (Even).
   - Final state: **OFF**.
7. **Bulb 7:**
   - Divisors: $\{1, 7\}$. Pairs: $(1, 7)$.
   - Count: $2$ (Even).
   - Final state: **OFF**.
8. **Bulb 8:**
   - Divisors: $\{1, 2, 4, 8\}$. Pairs: $(1, 8), (2, 4)$.
   - Count: $4$ (Even).
   - Final state: **OFF**.
9. **Bulb 9:**
   - Divisors: $\{1, 3, 9\}$. Pairs: $(1, 9), (3, 3)$.
   - Count: $3$ (Odd).
   - Final state: **ON** ($9 = 3^2$).
10. **Bulb 10:**
    - Divisors: $\{1, 2, 5, 10\}$. Pairs: $(1, 10), (2, 5)$.
    - Count: $4$ (Even).
    - Final state: **OFF**.

---

### Step 2: Perfect Square Counting
The bulbs that remain ON are:
$$
\{1, 4, 9\} = \{1^2, 2^2, 3^2\}
$$
Count of perfect squares $\le 10$:
$$
\lfloor \sqrt{10} \rfloor = \lfloor 3.162277 \dots \rfloor = \mathbf{3}
$$

---

## 4. Complete Execution Trace

```text
n = 10

Divisor Parity:
  Bulb 1:  divisors {1}          -> count = 1 (ODD)  -> ON  [1^2]
  Bulb 2:  divisors {1, 2}       -> count = 2 (EVEN) -> OFF
  Bulb 3:  divisors {1, 3}       -> count = 2 (EVEN) -> OFF
  Bulb 4:  divisors {1, 2, 4}    -> count = 3 (ODD)  -> ON  [2^2]
  Bulb 5:  divisors {1, 5}       -> count = 2 (EVEN) -> OFF
  Bulb 6:  divisors {1, 2, 3, 6} -> count = 4 (EVEN) -> OFF
  Bulb 7:  divisors {1, 7}       -> count = 2 (EVEN) -> OFF
  Bulb 8:  divisors {1, 2, 4, 8} -> count = 4 (EVEN) -> OFF
  Bulb 9:  divisors {1, 3, 9}    -> count = 3 (ODD)  -> ON  [3^2]
  Bulb 10: divisors {1, 2, 5, 10}-> count = 4 (EVEN) -> OFF

Square Root Evaluation:
  int(sqrt(10)) = int(3.1622) = 3

Result: 3
```

| Bulb Position $k$ | Positive Divisors | Divisor Pairs | Total Toggles | Parity | Final State | Perfect Square? |
|:---:|:---|:---|:---:|:---:|:---:|:---:|
| **1** | $\{1\}$ | $(1, 1)$ | 1 | **Odd** | **ON** | **Yes ($1^2$)** |
| 2 | $\{1, 2\}$ | $(1, 2)$ | 2 | Even | OFF | No |
| 3 | $\{1, 3\}$ | $(1, 3)$ | 2 | Even | OFF | No |
| **4** | $\{1, 2, 4\}$ | $(1, 4), (2, 2)$ | 3 | **Odd** | **ON** | **Yes ($2^2$)** |
| 5 | $\{1, 5\}$ | $(1, 5)$ | 2 | Even | OFF | No |
| 6 | $\{1, 2, 3, 6\}$ | $(1, 6), (2, 3)$ | 4 | Even | OFF | No |
| 7 | $\{1, 7\}$ | $(1, 7)$ | 2 | Even | OFF | No |
| 8 | $\{1, 2, 4, 8\}$ | $(1, 8), (2, 4)$ | 4 | Even | OFF | No |
| **9** | $\{1, 3, 9\}$ | $(1, 9), (3, 3)$ | 3 | **Odd** | **ON** | **Yes ($3^2$)** |
| 10 | $\{1, 2, 5, 10\}$ | $(1, 10), (2, 5)$ | 4 | Even | OFF | No |

---

## 5. Algorithmic Correctness

**Soundness.** A bulb toggles once for every positive divisor $d \le n$. Because $d \le k \le n$, every divisor of $k$ is visited in some round. Since divisors pair up into distinct integers unless $d = \sqrt{k}$, non-square integers always have an even number of divisors and end OFF. Perfect squares have an odd number of divisors and end ON.

**Completeness.** The set of perfect squares $\le n$ is exactly $\{1^2, 2^2, \dots, m^2\}$ where $m^2 \le n < (m + 1)^2$. By definition, $m = \lfloor \sqrt{n} \rfloor$. Thus, `int(sqrt(n))` accounts for every single surviving bulb without omission.

---

## 6. Traps This Instance Exposes

- **Attempting Simulation for Large $n$:** With $n = 10^9$, any loop executing $n$ or $\sqrt{n}$ times will either run out of memory or time out. Recognizing the mathematical reduction to $\lfloor \sqrt{n} \rfloor$ yields $O(1)$ computation.
- **Floating-Point Imprecision:** For $n = 10^9$, standard IEEE-754 double precision floats have 53 bits of mantissa, which can represent integers up to $9 \times 10^{15}$ exactly. $\sqrt{10^9} \approx 31622.7766$, and casting to `int` safely returns $31622$.
- **Base Case $n = 0$:** If $n = 0$, $\lfloor \sqrt{0} \rfloor = 0$, correctly returning $0$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time. The implementation computes $\lfloor \sqrt{n} \rfloor$ via a single hardware square root instruction.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory using zero additional data structures.
