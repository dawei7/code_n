# Guided Example: K Empty Slots

We trace the step-by-step day-by-day bulb illumination stream, prefix sum Fenwick tree (Binary Indexed Tree) activation tracking, boundary partner coordinate identification ($y = x \pm (k + 1)$), unlit intermediate interval query verification ($\text{query}(x-1) - \text{query}(y) == 0$), earliest satisfactory day reporting, and failure mode detection on representative bulb activation schedules:

- **Input:** $bulbs = [1, 3, 2], \quad k = 1$
- **Required output:** `2`
  - Problem rules:
    - $n$ light bulbs arranged in a line at positions $1, 2, \dots, n$, initially all turned **OFF**.
    - On day $i$ ($1$-indexed), bulb $bulbs[i-1]$ is turned **ON**.
    - Target condition: Find the **earliest day** on which there exist two turned-on bulbs at positions $x_1 < x_2$ such that:
      1. Exactly $k$ bulbs lie between them ($x_2 - x_1 - 1 = k \iff x_2 = x_1 + k + 1$).
      2. All $k$ intermediate bulbs are **still turned OFF**.
    - If no such configuration ever occurs, return $-1$.
- **Fenwick Tree & Interval Emptiness Invariant:**
  - **The Fixed-Distance Partner Invariant:**
    - When bulb $x$ turns on on day $i$, it can only form a valid pair with two specific fixed positions:
      - Left partner: $y = x - (k + 1)$
      - Right partner: $y = x + (k + 1)$
    - If a partner position $y$ is not yet lit ($vis[y] == False$), no pair is completed at this step.
  - **The Zero-Intermediate-Activity Check:**
    - If partner $y = x - k - 1$ is already lit:
      - The intervening bulbs occupy positions $y + 1, y + 2, \dots, x - 1$ (exactly $k$ positions).
      - All $k$ of these bulbs are turned OFF if and only if the sum of lit bulbs in range $[y + 1, \; x - 1]$ is **strictly zero**:
        $$
        \sum_{p = y + 1}^{x - 1} \text{lit}[p] = \text{query}(x - 1) - \text{query}(y) == 0
        $$
    - If this sum equals zero, we have found a valid configuration on day $i$! Because we iterate days in ascending order ($i = 1, 2, \dots$), the first time this condition is met is guaranteed to be the earliest day.
- **Step-by-Step Worked Execution Trace on $bulbs = [1, 3, 2], k = 1$ ($n = 3$):**
  - Setup: $n = 3$ bulbs, distance gap $k = 1 \implies$ required coordinate span is $k + 1 = 2$.
  - Initialize Fenwick tree and visited bit-array $vis = [False, False, False, False]$.
  - **Day 1 ($i = 1, \; x = bulbs[0] = 1$):**
    - Bulb 1 turns ON.
    - Update Fenwick tree at position $1$: $\text{update}(1, +1)$.
    - Record status: $vis[1] = True$.
    - Current bulb row state:
      $$
      [\mathbf{ON}, \; \text{OFF}, \; \text{OFF}]
      $$
    - Check left partner: $y = 1 - 2 = -1 \le 0$ (Out of bounds).
    - Check right partner: $y = 1 + 2 = 3$:
      - Is bulb 3 on? $vis[3] == False$.
      - Partner not yet lit.
    - Continue to Day 2.
  - **Day 2 ($i = 2, \; x = bulbs[1] = 3$):**
    - Bulb 3 turns ON.
    - Update Fenwick tree at position $3$: $\text{update}(3, +1)$.
    - Record status: $vis[3] = True$.
    - Current bulb row state:
      $$
      [\mathbf{ON}, \; \text{OFF}, \; \mathbf{ON}]
      $$
    - Check right partner: $y = 3 + 2 = 5 > 3$ (Out of bounds).
    - Check left partner:
      $$
      y = x - k - 1 = 3 - 1 - 1 = \mathbf{1}
      $$
      - Boundary check: $y = 1 > 0 \implies \mathbf{Valid\ Index}$.
      - Is left partner lit? $vis[1] == True \implies \mathbf{Yes!}$
      - Interval between 1 and 3: position $[2, 2]$ (length $= 3 - 1 - 1 = 1 == k$).
      - Query number of lit bulbs in $[2, 2]$:
        $$
        \text{query}(3 - 1) - \text{query}(1) = \text{query}(2) - \text{query}(1) = 1 - 1 = \mathbf{0}
        $$
      - The intermediate bulb at position 2 is **completely unlit**!
    - **Target Condition Satisfied:**
      - Bulbs 1 and 3 are ON.
      - Exactly $k = 1$ unlit bulb (bulb 2) lies between them.
      - Current day:
        $$
        ans = i = \mathbf{2}
        $$
      - Return **`2`** immediately.
- **Middle Bulb Interruption Failure Trace ($bulbs = [1, 2, 3], k = 1$):**
  - Day 1: Bulb 1 ON $\implies [\mathbf{ON}, \text{OFF}, \text{OFF}]$.
  - Day 2: Bulb 2 ON $\implies [\mathbf{ON}, \mathbf{ON}, \text{OFF}]$.
    - Bulb 2 has partners $0$ and $4$ (both out of bounds).
  - Day 3: Bulb 3 ON $\implies [\mathbf{ON}, \mathbf{ON}, \mathbf{ON}]$.
    - Bulb 3 checks left partner $y = 1$. Bulb 1 is ON.
    - But range query between 1 and 3 checks bulb 2: $\text{query}(2) - \text{query}(1) = 2 - 1 = \mathbf{1} \ne 0$.
    - Bulb 2 is already ON, so the gap of unlit bulbs is violated!
  - No valid day found $\implies$ Returns **`-1`**.

This instance demonstrates dynamic range-sum querying over evolving spatial point sets, mathematically proves why fixed-offset partner tests bound interval validations to $O(1)$ candidates per day, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a sequence of bulbs turning on each day:
Find the **earliest day** where two ON bulbs have **exactly $k$ OFF bulbs between them**.
If impossible, return $-1$.

```text
bulbs = [ 1, 3, 2 ], k = 1

Day 1: Bulb 1 turns ON  -> [ ON,  OFF, OFF ]
Day 2: Bulb 3 turns ON  -> [ ON,  OFF, ON  ]
                             ^     ^    ^
                             1    (1)   3

Bulbs 1 and 3 are ON, and between them is exactly k = 1 OFF bulb (Bulb 2)!
Condition satisfied on Day 2.
Result: 2
```

### The Invariant of the $k$-Gap
- Two bulbs at positions $x$ and $y$ have exactly $k$ bulbs between them if and only if:
  $$
  |x - y| = k + 1
  $$
- The condition holds on day $i$ if both $x$ and $y$ are lit, and the range sum of lit bulbs between $\min(x, y) + 1$ and $\max(x, y) - 1$ is strictly $0$.

---

## 2. Conceptual Foundation & Invariants

### 1. Left and Right Partner Probes:
When bulb $x$ turns on:
$$
\text{Left partner: } y_L = x - k - 1
$$
$$
\text{Right partner: } y_R = x + k + 1
$$

### 2. Range Emptiness Query via Fenwick Tree:
For left partner $y_L$:
$$
\text{Valid} \iff y_L > 0 \land vis[y_L] \land \left(\text{query}(x - 1) - \text{query}(y_L) == 0\right)
$$
For right partner $y_R$:
$$
\text{Valid} \iff y_R \le n \land vis[y_R] \land \left(\text{query}(y_R - 1) - \text{query}(x) == 0\right)
$$

> **Localized Discrete Interval Emptiness Invariant.** In an online insertion process, an interval $(y, x)$ of fixed length $k$ with lit endpoints contains zero active elements if and only if the cumulative counting function satisfies $F(x-1) - F(y) = 0$.

---

## 3. Step-by-Step Worked Execution

We trace $bulbs = [1, 3, 2], k = 1$:

---

### Step 1: Day 1 (Bulb 1)
- Turn on bulb 1.
- Partners: $y_L = -1$ (out), $y_R = 3$ (not yet lit).

---

### Step 2: Day 2 (Bulb 3)
- Turn on bulb 3.
- Check left partner $y_L = 3 - 2 = 1$.
- Bulb 1 is lit ($vis[1] = True$).
- Range query $[2, 2]$: $\text{query}(2) - \text{query}(1) = 1 - 1 = 0$.
- Zero bulbs in between are lit!
- Earliest day found: **`2`**.

---

## 4. Complete Execution Trace

| Day $i$ | Bulb Lit $x$ | Left Partner $y_L$ | Left Partner Lit? | Intermediate Lit Count | Right Partner $y_R$ | Right Partner Lit? | Match on Day? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $1$ | $-1$ | Invalid | — | $3$ | No ($vis[3] = \text{False}$) | No |
| **$2$** | **$3$** | **$1$** | **Yes ($vis[1] = \text{True}$)** | **$0$ (Empty)** | $5$ | Invalid | **Yes (Day 2)** |
| $3$ | $2$ | Skipped | — | — | — | — | — |

---

## 5. Boundary Cases & Failure Modes

- **$k = 0$ (Direct Neighbors):** Checks adjacent bulbs $x \pm 1$; empty count range $[x, x-1]$ has width 0.
- **$k \ge n$:** Distance exceeds row length $\implies$ returns $-1$.
- **Middle Bulb Lights Up First ($[2, 1, 3], k = 1$):** Day 1 lights bulb 2; when 1 and 3 light up later, bulb 2 is already ON $\implies$ query count is $1 \ne 0 \implies$ rejects.

---

## 6. Traps & Common Anti-Patterns

- **Scanning the Interval with a Linear Loop ($O(K)$):** Checking if all intermediate bulbs are OFF using a loop takes $O(K)$ time per day, resulting in $O(N \cdot K)$ worst-case time (TLE). A Fenwick tree queries in $O(\log N)$ time.
- **1-Indexed Fenwick Tree Offsets:** Carefully query $[y + 1, x - 1]$ as $\text{query}(x - 1) - \text{query}(y)$.
- **Sliding Window on Inverse Array ($O(N)$):** While an $O(N)$ sliding window on the `days` array also exists, the Fenwick tree approach directly models the online problem dynamics with high clarity.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - $N$ days of bulb activations.
  - Each day performs 1 point update and at most 2 range queries in a Fenwick tree of size $N$: $\mathcal{O}(\log N)$.
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 15$ ms for $N = 2 \times 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the Fenwick tree array and visited boolean array.
