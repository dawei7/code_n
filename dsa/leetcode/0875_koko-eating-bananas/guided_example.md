# Guided Example: Koko Eating Bananas

We trace the step-by-step monotonicity proof on eating speed, discrete ceiling hour accumulation $\lceil \text{pile} / k \rceil$, binary search interval bisection, feasibility predicates, and minimal speed derivation on representative banana pile distributions:

- **Input:**
  $$
  piles = [3, 6, 7, 11], \quad h = 8
  $$
- **Required output:** `4`
  - Banana eating protocol & constraints:
    - There are $N = 4$ piles of bananas with counts $[3, 6, 7, 11]$.
    - Guards will return in $h = 8$ hours.
    - Koko chooses an integer eating speed $k$ (bananas per hour).
    - Each hour, Koko chooses a pile and eats up to $k$ bananas from it.
    - If the pile has fewer than $k$ bananas, she eats all of them and does **not** eat from any other pile during that hour.
    - Therefore, the hours required to consume a pile of size $x$ at speed $k$ is:
      $$
      \text{hours}(x, k) = \lceil \frac{x}{k} \rceil = \lfloor \frac{x + k - 1}{k} \rfloor
      $$
    - Total hours needed to finish all piles:
      $$
      T(k) = \sum_{x \in piles} \lceil \frac{x}{k} \rceil
      $$
    - Objective: Find the **minimum integer speed $k$** such that $T(k) \le h$.
    - For $piles = [3, 6, 7, 11]$ and $h = 8$:
      - At $k = 3$: $\lceil 3/3 \rceil + \lceil 6/3 \rceil + \lceil 7/3 \rceil + \lceil 11/3 \rceil = 1 + 2 + 3 + 4 = 10 > 8$ (Too slow!).
      - At $k = 4$: $\lceil 3/4 \rceil + \lceil 6/4 \rceil + \lceil 7/4 \rceil + \lceil 11/4 \rceil = 1 + 2 + 2 + 3 = 8 \le 8$ (Feasible!).
      - Minimum speed: **`4`**.
- **Monotonicity & Bisection on the Answer Invariant:**
  - **The Monotone Feasibility Lemma:**
    - The ceiling function $\lceil x / k \rceil$ is monotonically non-increasing with respect to $k$:
      $$
      k_1 < k_2 \implies \lceil \frac{x}{k_1} \rceil \ge \lceil \frac{x}{k_2} \rceil \implies T(k_1) \ge T(k_2)
      $$
    - Therefore, the predicate $P(k) = (T(k) \le h)$ is monotonic:
      $$
      [\text{False}, \text{False}, \dots, \text{False}, \mathbf{True}, \text{True}, \dots, \text{True}]
      $$
    - The problem reduces to finding the first index where $P(k)$ switches from False to True.
  - **Search Space Bounds:**
    - Minimum possible speed: $k = 1$ (eating at least 1 banana per hour).
    - Maximum needed speed: $k = \max(piles) = 11$ (eating an entire pile in at most 1 hour, requiring exactly $N \le h$ hours).
    - We binary search within range $[1, \max(piles)]$.

---

## 1. Instance & Teaching Goal

Given $piles = [3, 6, 7, 11]$ and $h = 8$, find the minimal integer speed $k \in [1, 11]$ that finishes all bananas within $8$ hours.

```text
Speed k:    1    2    3    [4]   5    6   ...  11
Total Time: 27   15   10    8    8    6   ...   4
Time <= 8?: No   No   No   YES  YES  YES  ...  YES
                            ^
                     Smallest Speed = 4
```

The teaching goal is to justify how the step-function behavior of integer ceiling operations preserves global monotonicity, permitting logarithmic bisection.

---

## 2. Conceptual Foundation & Invariants

### 1. Pile Duration Formula:
$$
\text{cost}(x, k) = \lfloor \frac{x + k - 1}{k} \rfloor
$$

### 2. Feasibility Predicate:
$$
\text{feasible}(k) \iff \sum_{x \in piles} \lfloor \frac{x + k - 1}{k} \rfloor \le h
$$

### 3. Binary Search Invariant:
Maintain interval $[left, right]$ such that:
- For all $k < left$, $\text{feasible}(k) == \mathbf{false}$.
- For all $k \ge right$, $\text{feasible}(k) == \mathbf{true}$.
Convergence occurs when $left == right$.

---

## 3. Step-by-Step Worked Execution

We trace $piles = [3, 6, 7, 11], h = 8$:
Search space: $left = 1, right = \max(piles) = 11$.

---

### Step 1: Bisection 1 ($left = 1, right = 11$)
- Midpoint candidate speed:
  $$
  mid = \lfloor \frac{1 + 11}{2} \rfloor = 6
  $$
- Evaluate hours at speed $k = 6$:
  - Pile $3$: $\lceil 3/6 \rceil = 1$
  - Pile $6$: $\lceil 6/6 \rceil = 1$
  - Pile $7$: $\lceil 7/6 \rceil = 2$
  - Pile $11$: $\lceil 11/6 \rceil = 2$
  - Total hours: $1 + 1 + 2 + 2 = 6$.
- Feasibility check: $6 \le h = 8 \implies \mathbf{Feasible!}$
- Since $k = 6$ works, the minimal speed could be $6$ or smaller:
  $$
  right \leftarrow mid = 6
  $$

---

### Step 2: Bisection 2 ($left = 1, right = 6$)
- Midpoint candidate speed:
  $$
  mid = \lfloor \frac{1 + 6}{2} \rfloor = 3
  $$
- Evaluate hours at speed $k = 3$:
  - Pile $3$: $\lceil 3/3 \rceil = 1$
  - Pile $6$: $\lceil 6/3 \rceil = 2$
  - Pile $7$: $\lceil 7/3 \rceil = 3$
  - Pile $11$: $\lceil 11/3 \rceil = 4$
  - Total hours: $1 + 2 + 3 + 4 = 10$.
- Feasibility check: $10 > h = 8 \implies \mathbf{Too\ Slow!}$
- Speed $3$ is insufficient; minimal speed must be strictly greater:
  $$
  left \leftarrow mid + 1 = 4
  $$

---

### Step 3: Bisection 3 ($left = 4, right = 6$)
- Midpoint candidate speed:
  $$
  mid = \lfloor \frac{4 + 6}{2} \rfloor = 5
  $$
- Evaluate hours at speed $k = 5$:
  - Pile $3$: $\lceil 3/5 \rceil = 1$
  - Pile $6$: $\lceil 6/5 \rceil = 2$
  - Pile $7$: $\lceil 7/5 \rceil = 2$
  - Pile $11$: $\lceil 11/5 \rceil = 3$
  - Total hours: $1 + 2 + 2 + 3 = 8$.
- Feasibility check: $8 \le 8 \implies \mathbf{Feasible!}$
- Shrink upper bound:
  $$
  right \leftarrow mid = 5
  $$

---

### Step 4: Bisection 4 ($left = 4, right = 5$)
- Midpoint candidate speed:
  $$
  mid = \lfloor \frac{4 + 5}{2} \rfloor = 4
  $$
- Evaluate hours at speed $k = 4$:
  - Pile $3$: $\lceil 3/4 \rceil = 1$
  - Pile $6$: $\lceil 6/4 \rceil = 2$
  - Pile $7$: $\lceil 7/4 \rceil = 2$
  - Pile $11$: $\lceil 11/4 \rceil = 3$
  - Total hours: $1 + 2 + 2 + 3 = 8$.
- Feasibility check: $8 \le 8 \implies \mathbf{Feasible!}$
- Shrink upper bound:
  $$
  right \leftarrow mid = 4
  $$

---

### Termination:
$left == right == 4$.
Search space collapsed.
- **Minimum eating speed:** **`4`**.

---

## 4. Complete Execution Trace

| Iteration | Search Range $[left, right]$ | Candidate Speed $mid$ | Hours Calculation $(\sum \lceil x / mid \rceil)$ | Total Hours | Condition $(\le 8)$ | Decision | Next Range |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| $1$ | $[1, 11]$ | $6$ | $1 + 1 + 2 + 2$ | $6$ | Feasible | $right \leftarrow 6$ | $[1, 6]$ |
| $2$ | $[1, 6]$ | $3$ | $1 + 2 + 3 + 4$ | $10$ | **Too Slow** | $left \leftarrow 4$ | $[4, 6]$ |
| $3$ | $[4, 6]$ | $5$ | $1 + 2 + 2 + 3$ | $8$ | Feasible | $right \leftarrow 5$ | $[4, 5]$ |
| **$4$** | **$[4, 5]$** | **$4$** | **$1 + 2 + 2 + 3$** | **$8$** | **Feasible** | **$right \leftarrow 4$** | **$[4, 4]$** |

---

## 5. Boundary Cases & Failure Modes

- **$h == \text{len}(piles)$ (e.g. 5 piles, 5 hours):** Koko must eat each entire pile in exactly 1 hour. Speed must be $\max(piles)$.
- **Very Large $h$ ($h \gg \sum piles$):** Speed $k = 1$ suffices, taking $\sum piles \le h$ hours.
- **Large Pile Sizes ($piles[i] \le 10^9$):** Bisection range $[1, 10^9]$ takes only $\lceil \log_2(10^9) \rceil \approx 30$ iterations.
- **Integer Division Overhead:** Using `(x + k - 1) // k` avoids floating-point roundoff errors inherent to `math.ceil(x / k)`.

---

## 6. Traps & Common Anti-Patterns

- **Linear Search from $k = 1$:** Incrementing speed $k = 1, 2, 3 \dots$ takes $\mathcal{O}(M \cdot N)$ where $M = \max(piles) = 10^9$. This causes an immediate Time Limit Exceeded. Binary search reduces $10^9$ checks to 30.
- **Upper Bound Miscalculation:** Setting upper bound to $\sum piles$ is unnecessarily large and risks overflow; Koko can never consume more than one pile per hour, so speed beyond $\max(piles)$ provides zero reduction in total hours.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding maximum pile size $M = \max(piles)$: $\mathcal{O}(N)$.
  - Binary search interval $[1, M]$ has $\log_2 M$ levels.
  - In each level, checking feasibility takes $\mathcal{O}(N)$ arithmetic operations.
  - Total Time: $\mathcal{O}(N \log M)$, taking $< 15$ ms for $N = 10^4$ and $M = 10^9$.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ space using fixed scalar registers ($left, right, mid$).
