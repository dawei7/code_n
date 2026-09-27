# Guided Example: Minimize Max Distance to Gas Station

We trace the step-by-step continuous monotonic binary search over real-valued distance penalties ($D$), adjacent highway gap measurement ($\Delta = b - a$), discrete station allocation feasibility testing ($\sum \lfloor \Delta / D \rfloor \le k$), high-precision bisection refinement ($\text{tolerance} \le 10^{-6}$), and optimal fuel station distribution on representative coordinate configurations:

- **Input:**
  - Station coordinates: $stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]$
  - Available new stations: $k = 9$
- **Required output:**
  $$
  0.5
  $$
  - Gas station placement rules:
    - You are given $N$ existing gas stations along a straight highway in sorted order.
    - You must add $k$ additional gas stations anywhere along the line (real-valued positions allowed).
    - Let $penalty$ be the **maximum distance between adjacent stations** after placing all $k$ new stations.
    - Objective: Find the **minimum possible value** of $penalty$.
    - Solutions within $10^{-6}$ of the exact answer are accepted.
    - For $[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]$:
      - There are 9 original adjacent intervals, each of length $\Delta = 1$.
      - We have $k = 9$ new stations available.
      - Greedily placing exactly 1 new station at the midpoint of each interval ($1.5, 2.5, 3.5, \dots, 9.5$) splits every gap in half.
      - New distance between every adjacent pair of stations is:
        $$
        \frac{1}{1 + 1} = 0.5
        $$
      - No adjacent distance exceeds $0.5$.
      - Minimal penalty is **0.5**.
- **Continuous Monotonicity & Allocation Invariant:**
  - **Station Requirement for Distance $D$:**
    - Consider an existing highway segment between stations $a$ and $b$ with gap length $\Delta = b - a$.
    - To ensure that no sub-segment exceeds length $D$, the interval must be partitioned into at least:
      $$
      pieces = \left\lceil \frac{\Delta}{D} \right\rceil
      $$
    - The number of interior stations needed to create this many pieces is:
      $$
      needed = pieces - 1 = \left\lfloor \frac{\Delta}{D} \right\rfloor
      $$
  - **The Feasibility Predicate ($check(D)$):**
    - A penalty threshold $D$ is achievable with $\le k$ stations if and only if:
      $$
      \sum_{i=0}^{N - 2} \left\lfloor \frac{stations[i + 1] - stations[i]}{D} \right\rfloor \le k
      $$
  - **Monotonic Bisection:**
    - If $check(D)$ is `true`, $D$ is feasible, and an even smaller distance might also be achievable $\implies right \leftarrow D$.
    - If $check(D)$ is `false`, more than $k$ stations are required $\implies D$ is too restrictive $\implies left \leftarrow D$.
    - Bisection over $[0, 10^8]$ converges to $10^{-6}$ accuracy in $\approx 50$ iterations.
- **Step-by-Step Worked Execution Trace on $stations = [1, \dots, 10], k = 9$:**
  - Existing stations: 10 stations, 9 intervals of length $\Delta_i = 1$.
  - Target: $k = 9$ stations.
  - Search range: $[left, right] = [0.0, 10^8]$.
  - **Iteration Round 1 (Testing Coarse Guess $D = 1.0$):**
    - For each of the 9 intervals ($\Delta = 1$):
      $$
      needed_i = \lfloor 1 / 1.0 \rfloor \text{ wait, when } \Delta = D, \text{ pieces } = 1 \implies needed = 0
      $$
      - In integer truncation with epsilon, $1 / 1.0 = 1$ piece $\implies 0$ stations added.
      - Total stations needed: $0 \le 9 \implies \mathbf{Feasible!}$
      - Shrink right boundary: $right \leftarrow 1.0$.
  - **Iteration Round 2 (Testing Candidate $D = 0.4$):**
    - For each interval ($\Delta = 1$):
      $$
      \lfloor 1 / 0.4 \rfloor = \lfloor 2.5 \rfloor = \mathbf{2} \text{ stations per interval}
      $$
    - Total stations needed:
      $$
      9 \text{ intervals} \times 2 = 18 \text{ stations}
      $$
    - Compare with budget: $18 > 9 \implies \mathbf{Infeasible!} \quad (k = 9 \text{ is insufficient})$.
    - Expand left boundary: $left \leftarrow 0.4$.
  - **Iteration Round 3 (Testing Candidate $D = 0.5$):**
    - For each interval ($\Delta = 1$):
      - We want sub-segments of length $\le 0.5$.
      - Number of pieces required: $1 / 0.5 = 2$ pieces.
      - Interior stations per interval:
        $$
        2 - 1 = \mathbf{1} \text{ station}
        $$
    - Total stations needed:
      $$
      9 \times 1 = \mathbf{9} \text{ stations}
      $$
    - Compare with budget: $9 \le 9 \implies \mathbf{Feasible!}$
    - Shrink right boundary: $right \leftarrow 0.5$.
  - **Convergence:**
    - Any $D < 0.5$ requires at least 2 stations per interval ($18 > 9$).
    - $D = 0.5$ requires exactly 9 stations.
    - Continuous binary search locks onto:
      $$
      ans = \mathbf{0.5}
      $$
- **Single Dominant Gap Trace ($stations = [23, 24, 36, 39, 46, 56, 57, 65, 84, 98], k = 1$):**
  - Gaps: $1, 12, 3, 7, 10, 1, 8, 19, 14$.
  - Largest gap is $19$ (between 65 and 84).
  - Second largest gap is $14$ (between 84 and 98).
  - With $k = 1$, we split the gap of 19 into two pieces of length $19 / 2 = 9.5$.
  - The largest remaining gap is now $14$.
  - Result: **14.0**.
- **Tied Maximum Gaps Trace ($stations = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54], k = 2$):**
  - 9 gaps of length 6.
  - Adding 2 stations splits only 2 of the 9 gaps.
  - The remaining 7 gaps are still of length 6.
  - Penalty remains **6.0**.

This instance demonstrates real-valued binary search on minimax objective functions and discrete allocation predicate testing, mathematically proves why monotonicity of floor quotients guarantees unique convergence to the infimum penalty, and derives $O(N \log(W / \epsilon))$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given highway gas station coordinates $stations$ and $k$ new stations to place:
Find the **minimum possible maximum distance** between adjacent stations.
Answers within $10^{-6}$ are accepted.

```text
stations = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], k = 9

9 intervals of length 1.
We have 9 new stations -> place 1 in each interval:
  Each interval is cut in half: 1 / 2 = 0.5.

Result: 0.5
```

### The Invariant of the Binary Search Predicate
- Monotonicity: Larger allowed maximum distance $D$ requires fewer stations.
- For an interval of length $\Delta$, the number of stations needed to make all sub-segments $\le D$ is $\lfloor \Delta / D \rfloor$.
- Binary search on $D \in [0, 10^8]$ until $right - left \le 10^{-6}$.

---

## 2. Conceptual Foundation & Invariants

### 1. Station Requirement per Gap:
$$
\text{stations\_needed}(\Delta, D) = \left\lfloor \frac{\Delta}{D} \right\rfloor
$$

### 2. Feasibility Condition:
$$
check(D) = \left( \sum_{i=0}^{N-2} \left\lfloor \frac{stations[i+1] - stations[i]}{D} \right\rfloor \le k \right)
$$
$$
\text{if } check(mid) \implies right \leftarrow mid \quad \text{else } left \leftarrow mid
$$

> **Convex Relaxation Minimax Invariant.** The continuous station allocation problem $\min_D \max_i \Delta_i / (m_i + 1)$ subject to $\sum m_i \le k$ has a monotone, quasi-convex level-set structure, whose sub-level sets are exactly certified by the discrete count test $\sum \lfloor \Delta_i / D \rfloor \le k$.

---

## 3. Step-by-Step Worked Execution

We trace $stations = [1, \dots, 10], k = 9$:

---

### Step 1: Interval Lengths
- 9 intervals of length 1.

---

### Step 2: Test $D = 0.4$
- Each interval needs $\lfloor 1 / 0.4 \rfloor = 2$ stations.
- Total $= 9 \times 2 = 18 > 9 \implies$ Infeasible ($D$ too small).

---

### Step 3: Test $D = 0.5$
- Each interval needs $\lfloor 1 / 0.5 \rfloor = 1$ station (since $1 / 0.5 = 2$ pieces $\implies 1$ cut).
- Total $= 9 \times 1 = 9 \le 9 \implies$ Feasible.

---

### Step 4: Output
$$
ans = \mathbf{0.5}
$$

---

## 4. Complete Execution Trace

| Tested Threshold $D$ | Stations Needed per Gap $\Delta = 1$ | Total Stations Across 9 Gaps | Feasible? ($\le 9$) | Bisection Action |
|:---:|:---:|:---:|:---:|:---:|
| $1.0$ | $0$ | $0$ | Yes ($0 \le 9$) | $right \leftarrow 1.0$ |
| $0.4$ | $2$ | $18$ | No ($18 > 9$) | $left \leftarrow 0.4$ |
| **$0.5$** | **$1$** | **$9$** | **Yes ($9 \le 9$)** | **$right \leftarrow 0.5$** |
| **Final** | — | — | — | **Result: `0.5`** |

---

## 5. Boundary Cases & Failure Modes

- **Single New Station ($k = 1$):** Halves the single largest gap; if the second largest gap is greater, the second largest gap becomes the new maximum.
- **Tied Large Gaps:** Adding stations to some tied gaps leaves the remaining un-augmented gaps at original size.
- **Large Coordinates ($10^8$):** Floating-point binary search handles large initial ranges cleanly with $right = 10^8$.
- **High $k$ Allocation ($k = 10^6$):** Sub-divisions become very fine; $\approx 50$ iterations guarantee $10^{-6}$ precision.

---

## 6. Traps & Common Anti-Patterns

- **Using a Max-Heap / Priority Queue:** A greedy max-heap splitting the largest gap one by one runs in $O(k \log N)$. When $k = 10^6$, this TLEs immediately! Continuous binary search takes only $\approx 50 \times N$ operations regardless of how large $k$ is.
- **Floating-Point Precision Issues:** Using a fixed number of iterations (e.g. 60 or 70 iterations) or `right - left > 1e-6` guarantees convergence without infinite loops.
- **Formula for Cuts:** Be careful with integer conversion: $\lfloor \Delta / D \rfloor$ counts interior cuts directly when $\Delta / D$ is an integer boundary.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initial interval size $W = 10^8$. To reach precision $\epsilon = 10^{-6}$, number of binary search iterations is $\log_2(10^8 / 10^{-6}) = \log_2(10^{14}) \approx 47$ iterations.
  - Each check takes $\mathcal{O}(N)$ where $N \le 2000$.
  - Total Time: $\approx 47 \times 2000 \approx 9.4 \times 10^4$ operations. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
