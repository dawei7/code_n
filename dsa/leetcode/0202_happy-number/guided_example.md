# Guided Example: Happy Number

We trace the step-by-step digit square-sum mapping, Pigeonhole bounded descent, and Floyd's cycle detection on representative happy and cyclic integers:

- **Input:** $n = 19$
- **Required output:** `true` ($19 \to 82 \to 68 \to 100 \to 1$)
- **Unhappy Cycle Instance:** $n = 2 \implies \text{false}$ (Enters the classic 8-node cycle $4 \to 16 \to 37 \to 58 \to 89 \to 145 \to 42 \to 20 \to 4$)
- **Trivial Unit Instance:** $n = 1 \implies \text{true}$
- **Power of Ten Instance:** $n = 1000 \implies \text{true}$ ($1^2 + 0^2 + 0^2 + 0^2 = 1$)

This instance demonstrates functional iteration $f(n) = \sum d_i^2$, mathematically proves why digit square-sums strictly contract all large integers into a finite domain ($\le 243$), compares hash set cycle detection with Floyd's Tortoise and Hare pointers, and runs in $O(\log N)$ time with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a positive integer $n = 19$:
Define the successor function $f(n)$ as the sum of the squares of its decimal digits:
$$
f(n) = \sum_{i=1}^{k} d_i^2
$$
Iteratively apply $f(n)$ to generate the trajectory starting at $19$:
1. $n = 19 \implies f(19) = 1^2 + 9^2 = 1 + 81 = \mathbf{82}$
2. $n = 82 \implies f(82) = 8^2 + 2^2 = 64 + 4 = \mathbf{68}$
3. $n = 68 \implies f(68) = 6^2 + 8^2 = 36 + 64 = \mathbf{100}$
4. $n = 100 \implies f(100) = 1^2 + 0^2 + 0^2 = \mathbf{1}$
Because the trajectory terminates at $1$, $19$ is a **happy number** (`true`).

Now contrast this with an unhappy number like $n = 2$:
$$
2 \to 4 \to 16 \to 37 \to 58 \to 89 \to 145 \to 42 \to 20 \to \mathbf{4}
$$
The value $4$ repeats, trapping the sequence in an infinite periodic cycle $\{4, 16, 37, 58, 89, 145, 42, 20\}$ that never hits $1$. Thus, $2$ is unhappy (`false`).

---

## 2. Conceptual Foundation & Invariants

### Mathematical Boundedness Proof
Why does the sequence never diverge to infinity?
Consider an integer $n$ with $k$ digits, so $n \ge 10^{k-1}$.
The maximum possible sum of digit squares occurs when all digits are $9$:
$$
f(n) \le 81 \cdot k
$$
For $k \ge 4$ (i.e. $n \ge 1000$):
- If $k = 4$ ($n \le 9999$): $f(n) \le 4 \times 81 = 324 < 1000$.
- If $k = 10$: $f(n) \le 10 \times 81 = 810 \ll 10^9$.
For any number with 4 or more digits, $f(n) < n$. The sequence is strictly contracting until $n \le 243$!
Because the state space is restricted to $[1, 243]$, by the **Pigeonhole Principle**, any trajectory must either reach the absorbing state $1$ or repeat a state within at most $243$ iterations.

### Cycle Detection Protocols:
1. **Method A (Hash Set):**
   Store visited numbers in `seen = set()`. If $n == 1$, return `true`. If $n \in \text{seen}$, a cycle is detected; return `false`.
2. **Method B (Floyd's Tortoise and Hare, $O(1)$ Space):**
   Advance `slow` by 1 step ($f(\text{slow})$) and `fast` by 2 steps ($f(f(\text{fast}))$).
   If `fast == 1`, return `true`. If `slow == fast`, a cycle is detected; return `false`.

> **Invariant.** At each step, either the value of $n$ reaches the fixed point $1$, or Floyd's pointers reduce the distance around the periodic cycle until $\text{slow} = \text{fast}$.

---

## 3. Step-by-Step Worked Execution

We trace the trajectory of $n = 19$:

### Iteration 0:
- Current $n = 19$.
- $n \ne 1$, not in `seen`.
- Add to `seen`: $\text{seen} = \{19\}$.
- Digits: $1, 9$.
- $f(19) = 1^2 + 9^2 = 1 + 81 = 82$.

---

### Iteration 1:
- Current $n = 82$.
- $n \ne 1$, not in `seen`.
- Add to `seen`: $\text{seen} = \{19, 82\}$.
- Digits: $8, 2$.
- $f(82) = 8^2 + 2^2 = 64 + 4 = 68$.

---

### Iteration 2:
- Current $n = 68$.
- $n \ne 1$, not in `seen`.
- Add to `seen`: $\text{seen} = \{19, 82, 68\}$.
- Digits: $6, 8$.
- $f(68) = 6^2 + 8^2 = 36 + 64 = 100$.

---

### Iteration 3:
- Current $n = 100$.
- $n \ne 1$, not in `seen`.
- Add to `seen`: $\text{seen} = \{19, 82, 68, 100\}$.
- Digits: $1, 0, 0$.
- $f(100) = 1^2 + 0^2 + 0^2 = 1$.

---

### Iteration 4 (Terminal State):
- Current $n = 1$.
- Loop condition $n == 1$ met!
- Return `true`.

---

## 4. Complete Execution Trace

```text
n = 19:
  19  -> 1^2 + 9^2 =  82  (Add 19 to seen)
  82  -> 8^2 + 2^2 =  68  (Add 82 to seen)
  68  -> 6^2 + 8^2 = 100  (Add 68 to seen)
  100 -> 1^2 + 0^2 + 0^2 = 1 (Add 100 to seen)
  1   -> Reached 1! -> Return True

n = 2 (Unhappy Contrast):
  2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (Cycle detected! -> Return False)
```

| Iteration Step | Current $n$ | Extracted Digits | Sum of Squares Calculation | Successor $f(n)$ | Seen Set State | Status |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| 0 | 19 | $[1, 9]$ | $1^2 + 9^2 = 1 + 81$ | 82 | $\{19\}$ | Active |
| 1 | 82 | $[8, 2]$ | $8^2 + 2^2 = 64 + 4$ | 68 | $\{19, 82\}$ | Active |
| 2 | 68 | $[6, 8]$ | $6^2 + 8^2 = 36 + 64$ | 100 | $\{19, 82, 68\}$ | Active |
| 3 | 100 | $[1, 0, 0]$ | $1^2 + 0^2 + 0^2 = 1 + 0 + 0$ | 1 | $\{19, 82, 68, 100\}$ | Active |
| **4** | **1** | - | - | - | - | **Happy $\implies \text{true}$** |

---

## 5. Algorithmic Correctness

**Soundness.** A number is happy by definition if repeated digit-square summation reaches 1. Once 1 is reached, $f(1) = 1^2 = 1$, forming a permanent stable fixed point. If 1 is reached, the method outputs `true`. If a value is seen twice before reaching 1, the sequence has entered a periodic cycle excluding 1, guaranteeing it will never reach 1 and correctly returning `false`.

**Completeness.** Since the mapping contracts any integer into a finite set $\le 243$, every positive integer reaches either 1 or an unhappy cycle in a finite number of steps.

---

## 6. Traps This Instance Exposes

- **Infinite While Loop:** Without cycle detection (`seen` set or Floyd's pointers), an unhappy number like $2$ loops forever, causing a Time Limit Exceeded error.
- **String Conversion Overhead:** Using `sum(int(d)**2 for d in str(n))` creates string objects and lists at every step. Extracting digits via `n % 10` and `n //= 10` is significantly faster and uses zero heap memory.
- **Cycle Numbers:** Number theory proves that in base 10, all unhappy numbers enter the unique cycle $\{4, 16, 37, 58, 89, 145, 42, 20\}$. Checking `if n == 4: return False` is an alternative $O(1)$ space optimization.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$ to process the digits of the initial input $n$. Once the number drops below $243$, the trajectory length is at most a constant number of steps (at most 20 iterations). Thus, total runtime is $O(\log n)$.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory using Floyd's two-pointer algorithm; $O(1)$ memory using a hash set (since at most 243 integers can ever be inserted).
