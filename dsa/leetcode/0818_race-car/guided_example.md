# Guided Example: Race Car

We trace the step-by-step 1D kinematic motion simulation ($position \mathrel{+}= speed, \; speed \mathrel{*}= 2$), exponential displacement blocks ($2^k - 1$), reverse instruction mechanics ('R'), overshoot versus undershoot trajectory branching, dynamic programming state recurrence ($dp[i]$), and minimum instruction sequence length minimization on representative target coordinates:

- **Input:** $target = 6$
- **Required output:** `5`
  - Vehicle motion laws:
    - The car starts at position $0$ with speed $+1$.
    - **Instruction 'A' (Accelerate):**
      $$
      position \leftarrow position + speed
      $$
      $$
      speed \leftarrow speed \times 2
      $$
    - **Instruction 'R' (Reverse):**
      - If $speed > 0$: $speed \leftarrow -1$.
      - Otherwise: $speed \leftarrow +1$.
      - $position$ remains unchanged.
    - Objective: Find the **minimum length of instructions** to reach exactly $position = target$ with any speed.
    - For $target = 6$:
      - After 3 consecutive 'A's:
        - $t = 1$: pos = $0 + 1 = 1$, speed = $2$
        - $t = 2$: pos = $1 + 2 = 3$, speed = $4$
        - $t = 3$: pos = $3 + 4 = 7$, speed = $8$
      - At position $7$ (overshot target $6$ by $1$ unit):
        - Apply 'R': pos = $7$, speed = $-1$
      - Apply 'A':
        - pos = $7 + (-1) = \mathbf{6}$, speed = $-2$
      - Total instructions: `"AAARA"` (length **5**).
- **Exponential Block Sums & Trajectory Invariant:**
  - **The Power of 2 Invariant:**
    - Any sequence of $k$ consecutive 'A' accelerations from speed $\pm 1$ travels distance:
      $$
      D(k) = 1 + 2 + 4 + \dots + 2^{k - 1} = 2^k - 1
      $$
  - **Exact Power Target ($target = 2^k - 1$):**
    - If $target$ is exactly of the form $2^k - 1$, the optimal strategy is simply $k$ 'A's:
      $$
      dp[target] = k
      $$
  - **General Target Decomposition ($2^{k-1} - 1 < target < 2^k - 1$):**
    - Let $k = \text{bit\_length}(target)$. The target lies strictly between two powers-of-two milestones:
      1. **Overshoot Branch:**
         - Accelerate $k$ times to reach $2^k - 1 > target$ ($k$ instructions).
         - Reverse ('R') to point backwards ($1$ instruction).
         - The remaining distance to travel is $(2^k - 1 - target)$ from a fresh standstill speed of $-1$.
         - Cost:
           $$
           k + 1 + dp[2^k - 1 - target]
           $$
      2. **Undershoot Branch:**
         - Accelerate $k - 1$ times to reach $2^{k-1} - 1 < target$ ($k - 1$ instructions).
         - Reverse ('R') and drive backward for $j$ accelerations ($0 \le j < k - 1$):
           - Distance reversed: $2^j - 1$.
         - Reverse ('R') again to face forward at speed $+1$.
         - Total instructions spent on repositioning: $(k - 1) + 1 + j + 1 = k + j + 1$.
         - Net forward progress:
           $$
           (2^{k - 1} - 1) - (2^j - 1) = 2^{k - 1} - 2^j
           $$
         - Remaining forward distance to target:
           $$
           target - (2^{k - 1} - 2^j)
           $$
         - Total cost:
           $$
           (k - 1) + j + 2 + dp[target - (2^{k - 1} - 2^j)]
           $$
    - The optimal cost $dp[target]$ is the minimum across the overshoot branch and all valid undershoot branches $j \in [0, k - 2]$.
- **Step-by-Step Worked Execution Trace on $target = 6$:**
  - Distance $i = 6$:
    - $k = \text{bit\_length}(6) = \mathbf{3}$ *(since $2^2 - 1 = 3 < 6 < 7 = 2^3 - 1$)*.
  - **Precomputed Base Values:**
    - $dp[1] = 1$ (Instruction `"A"`, distance $2^1 - 1 = 1$).
    - $dp[2] = 4$ (Instructions `"A R A"`, reach 1, reverse, forward).
    - $dp[3] = 2$ (Instructions `"AA"`, distance $2^2 - 1 = 3$).
  - **Evaluating $dp[6]$:**
    - **Strategy 1 (Overshoot):**
      - Forward accelerations: $k = 3$ 'A's to reach $2^3 - 1 = 7$.
      - Reverse: 1 'R'.
      - Remaining distance: $7 - 6 = \mathbf{1}$.
      - Cost:
        $$
        k + 1 + dp[1] = 3 + 1 + 1 = \mathbf{5}
        $$
        *(Sequence: `"AAARA"`)*.
    - **Strategy 2 (Undershoot with $k - 1 = 2$ forward 'A's):**
      - Reach position $2^2 - 1 = 3$.
      - **Case $j = 0$ (Reverse and immediately reverse back without moving back):**
        - Move backward 0 'A's: distance reversed $2^0 - 1 = 0$.
        - Net forward progress: $3 - 0 = 3$.
        - Remaining distance: $6 - 3 = 3$.
        - Cost:
          $$
          (k - 1) + j + 2 + dp[3] = 2 + 0 + 2 + dp[3] = 4 + 2 = \mathbf{6}
          $$
          *(Sequence: `"AARRAA"`)*.
      - **Case $j = 1$ (Reverse and move back 1 'A'):**
        - Move backward 1 'A': distance reversed $2^1 - 1 = 1$.
        - Net forward progress: $3 - 1 = 2$.
        - Remaining distance: $6 - 2 = 4$.
        - $dp[4] = 5$ (from earlier DP step).
        - Cost:
          $$
          2 + 1 + 2 + dp[4] = 5 + 5 = \mathbf{10}
          $$
    - **Select Minimum Instruction Cost:**
      $$
      dp[6] = \min(5, \; 6, \; 10) = \mathbf{5}
      $$
- **Exact Power Target Trace ($target = 3$):**
  - $k = \text{bit\_length}(3) = 2$.
  - $3 == 2^2 - 1 \implies dp[3] = 2$ (`"AA"`).
- **Undershoot Optimal Trace ($target = 4$):**
  - Overshoot: $k = 3$ (reach 7), $7 - 4 = 3 \implies 3 + 1 + dp[3] = 4 + 2 = 6$ (`"AAARAA"`).
  - Undershoot $j = 0$: $k - 1 = 2$ (reach 3), reverse twice, need $4 - 3 = 1 \implies 2 + 0 + 2 + dp[1] = 4 + 1 = \mathbf{5}$ (`"AARRA"`).
  - Undershoot wins! Output is **`5`**.

This instance demonstrates discrete hybrid automata trajectory optimization and dyadic decomposition on discrete manifolds, mathematically proves why canonical optimal trajectories consist of at most one overshoot or a bounded backward realignment, and derives $O(T \log T)$ execution time and $O(T)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given target position $target$:
Vehicle accelerates ('A': $pos \mathrel{+}= spd, spd \mathrel{*}= 2$) or reverses ('R': $spd = -1$ or $+1$).
Find the **minimum instruction length** to land on $target$.

```text
target = 6

Strategy 1: Overshoot
  Accelerate 3 times: 'A', 'A', 'A' -> reaches 7 (speed 8)
  Reverse: 'R'                      -> position 7 (speed -1)
  Accelerate 1 time: 'A'            -> reaches 7 - 1 = 6!

Total instructions: "AAARA" -> length 5
Result: 5
```

### The Invariant of Dyadic Trajectory Optimization
- $k$ accelerations cover $2^k - 1$ distance.
- To reach $target$, we either:
  1. **Overshoot:** go to $2^k - 1 > target$, reverse, and solve subproblem for the remaining $2^k - 1 - target$.
  2. **Undershoot:** go to $2^{k-1} - 1 < target$, reverse, drive back $2^j - 1$, reverse forward, and solve subproblem for the remaining distance.

---

## 2. Conceptual Foundation & Invariants

### 1. Milestone Distances:
$$
D(k) = 2^k - 1
$$

### 2. Recurrence Relation:
For $k = \text{bit\_length}(i)$:
$$
dp[i] = \begin{cases}
k & i = 2^k - 1 \\
\min \begin{cases}
k + 1 + dp[2^k - 1 - i] \\
\min_{0 \le j < k - 1} \Big( (k - 1) + j + 2 + dp[i - (2^{k - 1} - 2^j)] \Big)
\end{cases} & \text{otherwise}
\end{cases}
$$

> **Dyadic Approximation Invariant.** The continuous optimal control problem on $\mathbb{R} \times \mathbb{R}$ with bang-bang acceleration contracts to a 1D discrete shortest path. An optimal trajectory reverses at most twice before reducing strictly to a smaller coordinate subproblem.

---

## 3. Step-by-Step Worked Execution

We trace $target = 6$:

---

### Step 1: Base Table
- $dp[1] = 1$ (`"A"`).
- $dp[2] = 4$ (`"A R A"`).
- $dp[3] = 2$ (`"AA"`).

---

### Step 2: Target 6 ($k = 3$)
- Overshoot to $7$: $3 + 1 + dp[7 - 6] = 4 + 1 = \mathbf{5}$.
- Undershoot $j = 0$ (reach 3, no back): $2 + 0 + 2 + dp[6 - 3] = 4 + 2 = 6$.
- Undershoot $j = 1$ (reach 3, back 1): $2 + 1 + 2 + dp[6 - 2] = 5 + dp[4] = 10$.

---

### Step 3: Output
- $\min(5, 6, 10) = \mathbf{5}$.

---

## 4. Complete Execution Trace

| Strategy Branch | Forward Accelerations | Turnaround $j$ | Repositioning Cost | Remaining Subproblem | Subproblem Cost | Total Branch Length |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Overshoot** | **$3$ ('A')** | — | **$3 + 1 = 4$** | **$dp[7 - 6] = dp[1]$** | **$1$** | **`5` (Min!)** |
| Undershoot $j=0$ | $2$ ('A') | $0$ | $2 + 0 + 2 = 4$ | $dp[6 - 3] = dp[3]$ | $2$ | $6$ |
| Undershoot $j=1$ | $2$ ('A') | $1$ | $2 + 1 + 2 = 5$ | $dp[6 - 2] = dp[4]$ | $5$ | $10$ |

---

## 5. Boundary Cases & Failure Modes

- **$target = 1$:** Single accelerate `"A"` $\implies 1$.
- **$target = 3$:** Double accelerate `"AA"` $\implies 2$.
- **$target = 7$:** Triple accelerate `"AAA"` $\implies 3$.
- **Large Target ($target = 10^4$):** $10^4 \times \log_2(10^4) \approx 1.4 \times 10^5$ operations; runs in $< 15$ ms.

---

## 6. Traps & Common Anti-Patterns

- **General BFS Queue Over State Space $(pos, speed)$:** A direct BFS exploring all pairs $(pos, speed)$ explores thousands of unguided states and risks TLE or memory exhaustion. 1D Dynamic Programming over target distances guarantees polynomial time.
- **Missing Undershoot Branches:** Only checking overshoot ignores optimal paths where undershooting and taking a tiny backward correction is faster (e.g. $target = 4$).
- **Allowing $j \ge k - 1$:** Reversing backward for more than $k - 1$ steps retreats farther than the starting point, which is strictly suboptimal.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Outer loop runs from $i = 1$ to $target$: $\mathcal{O}(T)$.
  - Inner loop explores at most $k = \log_2(i)$ undershoot choices: $\mathcal{O}(\log T)$.
  - Total Time: strictly $\mathcal{O}(T \log T)$ where $T \le 10^4 \implies \le 1.4 \times 10^5$ operations. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(T)$ memory to store the 1D DP array $dp$.