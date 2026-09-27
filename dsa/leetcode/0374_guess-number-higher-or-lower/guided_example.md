# Guided Example: Guess Number Higher or Lower

We trace the step-by-step interactive binary search interval contraction ($[L, R] = [1, n]$), ternary feedback query processing (`guess(mid) \in \{-1, 0, 1\}`), midpoint calculation ($M = L + \lfloor(R-L)/2\rfloor$), and target discovery on representative guessing game instances:

- **Input:** $n = 10, \quad pick = 6$
- **Required output:** $6$
  - Initial active interval: $[1, 10]$
  - Probe 1: Midpoint $M = 1 + \lfloor(10 - 1)/2\rfloor = 5$
    - Call `guess(5)` $\implies 1$ (Target $pick > 5$, guess is too low)
    - Discard lower half: $L \leftarrow 5 + 1 = 6$
    - Narrowed range: $[6, 10]$
  - Probe 2: Midpoint $M = 6 + \lfloor(10 - 6)/2\rfloor = 8$
    - Call `guess(8)` $\implies -1$ (Target $pick < 8$, guess is too high)
    - Discard upper half: $R \leftarrow 8 - 1 = 7$
    - Narrowed range: $[6, 7]$
  - Probe 3: Midpoint $M = 6 + \lfloor(7 - 6)/2\rfloor = 6$
    - Call `guess(6)` $\implies 0$ (Exact match found!)
    - Return target: $\mathbf{6}$
- **Immediate First-Probe Match:** $n = 1, pick = 1 \implies M = 1$, `guess(1) == 0` in 1 call
- **Upper Limit Constraint:** $n = 2^{31} - 1 \implies$ converges in $\le 31$ queries

This instance demonstrates interactive binary search against an external black-box comparator, mathematically proves why $M = L + \lfloor(R-L)/2\rfloor$ prevents integer overflow while halving the candidate space on each query, and achieves $O(\log N)$ query complexity and $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given an upper limit $n = 10$ and an unknown secret number $pick = 6$ chosen from $[1, 10]$:
Determine the secret number by calling the interactive API `guess(num)`:
- `guess(num) == -1`: Your guess is higher than the picked number ($num > pick$).
- `guess(num) == 1`: Your guess is lower than the picked number ($num < pick$).
- `guess(num) == 0`: Your guess equals the picked number ($num == pick$).

```text
Game Space: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Secret Pick = 6

Query 1: guess(5) -> returns  1 (Too low! Pick is in [6..10])
Query 2: guess(8) -> returns -1 (Too high! Pick is in [6..7])
Query 3: guess(6) -> returns  0 (CORRECT! Match found)

Total Queries: 3 (Much faster than linear scan of 10)
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Monotonic Feedback Sequence
The response function $g(x) = \text{guess}(x)$ satisfies:
- For all $x < pick$: $g(x) = 1$
- For $x = pick$: $g(x) = 0$
- For all $x > pick$: $g(x) = -1$
Negating the output, $-g(x) = -\text{guess}(x)$, yields a monotonically non-decreasing function:
$$
-g(x) \in [-1, \dots, -1, \quad 0, \quad 1, \dots, 1]
$$
This monotonicity guarantees that binary search will converge deterministically to $pick$.

### 2. Iterative Bisection Protocol:
Initialize $L = 1, R = n$.
While $L \le R$:
1. Midpoint computation:
   $$
   M = L + \left\lfloor \frac{R - L}{2} \right\rfloor
   $$
2. API probe:
   $$
   res = \text{guess}(M)
   $$
3. Tri-state branch:
   - If $res == 0$: return $M$ (Target found).
   - If $res == 1$: secret is strictly greater than $M \implies L \leftarrow M + 1$.
   - If $res == -1$: secret is strictly less than $M \implies R \leftarrow M - 1$.

> **Invariant.** The secret number $pick$ is guaranteed to lie within the inclusive interval $[L, R]$ at the start of every iteration.

---

## 3. Step-by-Step Worked Execution

We trace $n = 10, pick = 6$:

---

### Step 1: Probe 1 (Window $[1, 10]$)
- Range: $L = 1, R = 10$.
- Compute midpoint:
  $$
  M = 1 + \left\lfloor \frac{10 - 1}{2} \right\rfloor = 1 + 4 = \mathbf{5}
  $$
- Call API:
  $$
  res = \text{guess}(5) \implies \mathbf{1} \quad (5 < pick)
  $$
- Update lower bound:
  $$
  L \leftarrow 5 + 1 = \mathbf{6}
  $$
- Next active interval: $[6, 10]$.

---

### Step 2: Probe 2 (Window $[6, 10]$)
- Range: $L = 6, R = 10$.
- Compute midpoint:
  $$
  M = 6 + \left\lfloor \frac{10 - 6}{2} \right\rfloor = 6 + 2 = \mathbf{8}
  $$
- Call API:
  $$
  res = \text{guess}(8) \implies \mathbf{-1} \quad (8 > pick)
  $$
- Update upper bound:
  $$
  R \leftarrow 8 - 1 = \mathbf{7}
  $$
- Next active interval: $[6, 7]$.

---

### Step 3: Probe 3 (Window $[6, 7]$)
- Range: $L = 6, R = 7$.
- Compute midpoint:
  $$
  M = 6 + \left\lfloor \frac{7 - 6}{2} \right\rfloor = 6 + 0 = \mathbf{6}
  $$
- Call API:
  $$
  res = \text{guess}(6) \implies \mathbf{0} \quad (6 == pick)
  $$
- Exact target identified!
- Immediate return:
  $$
  \mathbf{6}
  $$

---

## 4. Complete Execution Trace

```text
n = 10, pick = 6

Iteration 1:
  Interval = [1, 10], Midpoint M = 5
  guess(5) = 1 (Too low) -> L = 6

Iteration 2:
  Interval = [6, 10], Midpoint M = 8
  guess(8) = -1 (Too high) -> R = 7

Iteration 3:
  Interval = [6, 7], Midpoint M = 6
  guess(6) = 0 (Match!) -> Return 6
```

| Iteration | Search Range $[L, R]$ | Midpoint Probe $M$ | Return of `guess(M)` | Semantic Meaning | Action Taken | Next Range |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $[1, 10]$ | 5 | $1$ | $5 < pick$ | $L \leftarrow 5 + 1 = 6$ | $[6, 10]$ |
| 2 | $[6, 10]$ | 8 | $-1$ | $8 > pick$ | $R \leftarrow 8 - 1 = 7$ | $[6, 7]$ |
| **3** | **$[6, 7]$** | **6** | **$0$** | **$6 == pick$** | **Target verified!** | **`6` (Output)** |

---

## 5. Algorithmic Correctness

**Soundness.** If `guess(M) == 0`, $M$ is mathematically confirmed by the oracle to equal $pick$. When `guess(M) == 1`, $M < pick$, so $pick \ge M + 1$; discarding all values $\le M$ cannot eliminate the target. When `guess(M) == -1`, $M > pick$, so $pick \le M - 1$; discarding all values $\ge M$ cannot eliminate the target. Thus, the search invariant is maintained unconditionally.

**Completeness.** Each comparison strictly reduces the range size: $|R' - L' + 1| \le \lfloor |R - L + 1| / 2 \rfloor$. The algorithm terminates in at most $\lfloor \log_2 n \rfloor + 1$ queries, guaranteed to encounter the unique matching midpoint.

---

## 6. Traps This Instance Exposes

- **API Sign Inversion Confusion:** `guess(num) == -1` means the guess is *higher* than $pick$ (so $pick$ is smaller, decrement $R$). A common mistake is interpreting $-1$ as "guess was too small".
- **32-Bit Integer Midpoint Overflow:** When $L + R > 2^{31} - 1$, writing `(L + R) // 2` causes integer overflow in fixed-width languages (Java, C++). Writing `L + (R - L) // 2` is universally overflow-safe.
- **Off-By-One Boundary Contraction:** Omitting the $\pm 1$ adjustment (e.g. setting $L = M$ or $R = M$) can cause infinite loops when $L$ and $R$ differ by 1.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$ API calls. The search domain of size $N$ is halved at every step. For $N = 2^{31} - 1$, at most $31$ API calls are made.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space, storing only scalar integer pointers $L, R, M$.