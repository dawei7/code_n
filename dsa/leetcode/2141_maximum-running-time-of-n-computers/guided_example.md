# Guided Example: Maximum Running Time of N Computers

We analyze and execute the monotonic bisection algorithm for simultaneous power scheduling on a representative problem instance, establishing how the bounded-contribution capacity constraint governs multi-machine concurrency.

- **Input:** `n = 2`, `batteries = [3, 3, 3]`
- **Output:** `4`

This instance illustrates fractional battery rotation, the physical constraint capping per-battery contribution at duration $T$, and the monotonic predicate certifying feasibility.

---

## 1. Problem Overview & Representative Instance

We are given $n$ identical computers and an array of $m$ batteries, where battery $i$ has an energy capacity of $\text{batteries}[i]$ minutes. All $n$ computers must run simultaneously. At any moment:
- Each computer may hold at most one battery.
- Each battery can power at most one computer at a time.
- Batteries may be swapped instantaneously between computers without downtime.
- Discharged batteries cannot be recharged.

The goal is to determine the maximum duration $T$ (in whole minutes) during which all $n$ computers can run concurrently without interruption.

In our representative instance:
- Number of computers: $n = 2$.
- Batteries: $[3, 3, 3]$ (three batteries of $3$ minutes each).
- Total available energy: $3 + 3 + 3 = 9$ minutes.

If batteries could be merged into a single fluid reservoir, $2$ computers could run for at most $\lfloor 9 / 2 \rfloor = 4$ minutes. We must prove whether discrete battery allocation allows achieving this theoretical upper bound of $T = 4$.

---

## 2. Mathematical & Algorithmic Principles

### The Single-Machine Saturation Cap

Consider an operating window of duration $T$. During this time, each of the $n$ computers requires $T$ minutes of energy, demanding a cumulative energy requirement of:
$$\text{Requirement}(T) = n \cdot T$$

Can a battery with capacity $B_i > T$ contribute its full capacity $B_i$ to meeting this requirement?
- No. Because a battery can be inserted into at most one computer at any point in time, it can operate for at most $T$ minutes during a session of length $T$.
- Any surplus capacity $B_i - T$ cannot be utilized concurrently.
- Therefore, the effective energy contributed by battery $i$ towards a duration of $T$ is bounded:
$$\text{Contribution}(B_i, T) = \min(B_i, T)$$

Summing across all $m$ batteries gives the total usable energy for duration $T$:
$$\text{UsableEnergy}(T) = \sum_{i=1}^{m} \min(B_i, T)$$

### Feasibility Predicate

By the Birkhoff-von Neumann theorem on doubly stochastic matrices (or max-flow min-cut duality on task-machine bipartite scheduling networks), a valid collision-free assignment of batteries to computers over continuous time $T$ exists if and only if the total usable energy meets the cumulative requirement:
$$\text{Feasible}(T) \iff \sum_{i=1}^{m} \min(B_i, T) \ge n \cdot T$$

### Monotonicity & Binary Search

Let $f(T) = \sum_{i=1}^m \min(B_i, T) - n \cdot T$. 
- If $T$ is feasible, any duration $T' \le T$ is also feasible because shorter durations require strictly less total energy and never decrease the usable portion of any battery.
- If $T$ is infeasible, any $T' > T$ is also infeasible.

This monotonic step profile enables binary search over the domain $[L, R]$:
- Lower bound: $L = 0$ (trivially feasible).
- Upper bound: $R = \lfloor (\sum B_i) / n \rfloor$, the absolute physical ceiling if all energy were pooled.

| Component | Definition / Formula | Concrete Role in Instance ($n = 2$) |
|---|---|---|
| Target Duration $T$ | Candidate simultaneous runtime | Value tested for feasibility |
| Capped Contribution | $\min(B_i, T)$ | Usable energy from battery $i$ over $T$ minutes |
| Total Usable Energy | $\sum_{i=1}^m \min(B_i, T)$ | Sum of usable energy across all batteries |
| Required Energy | $n \cdot T$ | Total energy required to power $n$ computers |
| Feasibility Condition | $\sum \min(B_i, T) \ge n \cdot T$ | Test determining whether interval shifts right or left |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We execute binary search on the representative instance $n = 2$, $\text{batteries} = [3, 3, 3]$.

```
Batteries:  [3, 3, 3],  n = 2
Total Energy = 9
Upper Bound R = floor(9 / 2) = 4
Search Space for T: [1, 4]
```

### Step 1: Initialize Search Interval
- Total battery energy: $3 + 3 + 3 = 9$.
- $L = 1$.
- $R = \lfloor 9 / 2 \rfloor = 4$.
- Current search interval: $[1, 4]$.

### Step 2: Probe Midpoint $T = 2$
- Midpoint: $T = 1 + \lfloor(4 - 1)/2\rfloor = 2$.
- Evaluate battery contributions for $T = 2$:
  - Battery 0 ($B_0 = 3$): $\min(3, 2) = 2$.
  - Battery 1 ($B_1 = 3$): $\min(3, 2) = 2$.
  - Battery 2 ($B_2 = 3$): $\min(3, 2) = 2$.
- Total usable energy: $2 + 2 + 2 = 6$.
- Energy required: $n \cdot T = 2 \cdot 2 = 4$.
- Feasibility check: $6 \ge 4$ is true.
- Conclusion: $T = 2$ is feasible. Record best answer $4 \ge 2$, advance lower bound: $L = 2 + 1 = 3$.
- New search interval: $[3, 4]$.

### Step 3: Probe Midpoint $T = 3$
- Midpoint: $T = 3 + \lfloor(4 - 3)/2\rfloor = 3$.
- Evaluate battery contributions for $T = 3$:
  - Battery 0 ($B_0 = 3$): $\min(3, 3) = 3$.
  - Battery 1 ($B_1 = 3$): $\min(3, 3) = 3$.
  - Battery 2 ($B_2 = 3$): $\min(3, 3) = 3$.
- Total usable energy: $3 + 3 + 3 = 9$.
- Energy required: $n \cdot T = 2 \cdot 3 = 6$.
- Feasibility check: $9 \ge 6$ is true.
- Conclusion: $T = 3$ is feasible. Record best answer $3$, advance lower bound: $L = 3 + 1 = 4$.
- New search interval: $[4, 4]$.

### Step 4: Probe Midpoint $T = 4$
- Midpoint: $T = 4$.
- Evaluate battery contributions for $T = 4$:
  - Battery 0 ($B_0 = 3$): $\min(3, 4) = 3$.
  - Battery 1 ($B_1 = 3$): $\min(3, 4) = 3$.
  - Battery 2 ($B_2 = 3$): $\min(3, 4) = 3$.
- Total usable energy: $3 + 3 + 3 = 9$.
- Energy required: $n \cdot T = 2 \cdot 4 = 8$.
- Feasibility check: $9 \ge 8$ is true.
- Conclusion: $T = 4$ is feasible. Record best answer $4$, advance lower bound: $L = 4 + 1 = 5$.
- Search interval $[5, 4]$ is empty ($L > R$). Bisection terminates.

The maximum concurrent runtime is $4$.

---

## 4. Comprehensive State Trace

The table below catalogs each iteration of the bisection search:

| Iteration | Search Range $[L, R]$ | Probe $T$ | Individual Capped Energies | $\sum \min(B_i, T)$ | Required $n \cdot T$ | Feasible? | Next Action |
|---|---|---|---|---|---|---|---|
| Initial | $[1, 4]$ | - | - | - | - | - | Compute mid |
| 1 | $[1, 4]$ | $2$ | $[2, 2, 2]$ | $6$ | $4$ | Yes ($6 \ge 4$) | Set $L = 3$ |
| 2 | $[3, 4]$ | $3$ | $[3, 3, 3]$ | $9$ | $6$ | Yes ($9 \ge 6$) | Set $L = 4$ |
| 3 | $[4, 4]$ | $4$ | $[3, 3, 3]$ | $9$ | $8$ | Yes ($9 \ge 8$) | Set $L = 5$ |
| Conclude | $[5, 4]$ | - | Terminated | - | - | - | Return $4$ |

### Physical Schedule Verification for $T = 4$

To demonstrate how three $3$-minute batteries run two computers for $4$ minutes:
- Minutes $0$ to $2$: Computer 1 runs on Battery 0 ($2$ min used, $1$ left); Computer 2 runs on Battery 1 ($2$ min used, $1$ left).
- Minutes $2$ to $3$: Computer 1 runs on Battery 0 ($1$ min used, discharged); Computer 2 runs on Battery 2 ($1$ min used, $2$ left).
- Minutes $3$ to $4$: Computer 1 runs on Battery 1 ($1$ min used, discharged); Computer 2 runs on Battery 2 ($1$ min used, $1$ left).
- Both computers run continuously for $4$ full minutes with zero idle gap.

---

## 5. Algorithmic Correctness & Soundness

### Sufficiency of the Bounded Sum Criterion
The feasibility condition $\sum_{i=1}^m \min(B_i, T) \ge n \cdot T$ is both necessary and sufficient:
1. **Necessity:** No single battery can supply more than $1$ unit of energy per unit time. Over an interval of length $T$, its maximum possible output is $T$, regardless of total capacity. Thus total energy cannot exceed $\sum \min(B_i, T)$. Since $n$ computers require $n \cdot T$ total energy, $\sum \min(B_i, T) \ge n \cdot T$ is strictly required.
2. **Sufficiency:** If $\sum \min(B_i, T) \ge n \cdot T$, batteries can be ordered along a circular timeline of length $T$ with capacity strips wrapped across $n$ computer tracks. Because each battery strip has length at most $\min(B_i, T) \le T$, no battery ever wraps around to overlap with itself at the same time point. Hence, no collision occurs.

### Invariant Preservation
At each step of the binary search, all durations $t < L$ are known to be feasible, and all durations $t > R$ are known to be infeasible. When $L > R$, the highest confirmed value is $R$, which is the unique global maximum.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Number of Computers Equals Number of Batteries ($m = n$):** No swapping can assist a weaker battery. The runtime is strictly limited by the weakest battery: $\min(B_0, B_1, \dots, B_{n-1})$. The bisection naturally clamps at this minimum.
2. **One Huge Battery Dominates:** For example, $n = 2$ and $\text{batteries} = [1, 1, 100]$. The single large battery cannot power both computers at once. Its contribution is capped at $\min(100, T) = T$. The usable energy is $1 + 1 + T$, which must satisfy $2 + T \ge 2T \implies T \le 2$. The answer is correctly $2$.
3. **Large Total Energy Exceeding 32-bit Integers:** With $m \le 10^5$ and $B_i \le 10^9$, total energy can reach $10^{14}$. Search bounds and summation accumulators must use 64-bit integer types to prevent arithmetic overflow.

### Common Anti-Patterns
- **Uncapped Sum Division ($\lfloor \sum B_i / n \rfloor$):** Simply dividing total energy by $n$ fails whenever a few outlier batteries exceed the average, as surplus power cannot be duplicated across computers simultaneously.
- **Simulation of Swaps:** Attempting to discretely simulate fractional swaps second by second creates an intractable state space. The mathematical feasibility reduction collapses the entire simulation to a single algebraic inequality check per probe.
- **Greedy Static Pairing:** Assigning fixed batteries to fixed computers misses the power of rotational time-sharing.

---

## 7. Complexity Analysis

### Time Complexity
- Let $m$ be the number of batteries, and let $S = \sum_{i=1}^m B_i$ be the total energy.
- The binary search interval is $[1, \lfloor S / n \rfloor]$.
- The width of the search domain is at most $S / n \le 10^{14} / 1 = 10^{14}$.
- The number of bisection probes is $\log_2(10^{14}) \approx 47$.
- Each probe evaluates the summation $\sum_{i=1}^m \min(B_i, T)$, which takes $O(m)$ time.
- Total time complexity is $O(m \cdot \log(\sum B_i / n))$, taking under $25$ milliseconds for $10^5$ batteries.

### Auxiliary Space Complexity
- The binary search and predicate evaluation maintain scalar variables ($L$, $R$, $T$, and sum accumulators).
- No auxiliary arrays or recursive stacks are allocated.
- Total auxiliary space complexity is $O(1)$.