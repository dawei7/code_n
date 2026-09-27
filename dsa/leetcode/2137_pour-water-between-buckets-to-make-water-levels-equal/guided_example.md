# Guided Example: Pour Water Between Buckets to Make Water Levels Equal

We trace the step-by-step execution of the continuous binary search and conservation with dissipation approach on a representative problem instance:

- **Initial Water Volumes (`buckets`):** `[1, 2, 7]`
- **Pouring Loss Percentage (`loss`):** $80\%$
- **Expected Output:** $2.0$

This instance demonstrates how fractional dissipation during transfer introduces an asymmetric efficiency factor between water donors and water recipients, proving why testing target height feasibility forms a strictly monotonic predicate resolvable via continuous bisection.

---

## 1. Problem Overview & Representative Instance

We have an array of $n$ buckets, where $\text{buckets}[i]$ represents the initial volume of water in bucket $i$. We wish to pour water between buckets until every bucket contains the exact same volume $v$. Whenever we pour $x$ units of water from one bucket to another, $\text{loss}\%$ is spilled, meaning the receiving bucket receives only:

$$x \times \left(1 - \frac{\text{loss}}{100}\right) \text{ units of water}$$

Our objective is to determine the maximum possible equal water level $v$ attainable across all buckets within an absolute error tolerance of $10^{-5}$.

Consider our representative instance:
`buckets = [1, 2, 7], loss = 80`
- Transfer efficiency: $\eta = 1 - \frac{80}{100} = 0.20$ (only $20\%$ of poured water arrives).
- If we target level $v = 2.0$:
  - Bucket $2$ has initial volume $7$, providing a surplus of $7 - 2 = 5$ units.
  - Pouring all $5$ surplus units delivers $5 \times 0.20 = 1.0$ unit.
  - Bucket $0$ has initial volume $1$, requiring a deficit of $2 - 1 = 1.0$ unit.
  - Bucket $1$ is already at volume $2$, requiring $0$ units.
  - The delivered $1.0$ unit exactly covers Bucket $0$'s deficit, achieving an equal volume of $2.0$ across all three buckets.

---

## 2. Mathematical & Algorithmic Principles

### Conservation Under Dissipation
Let $v$ be a hypothetical uniform water level. The buckets naturally partition into two sets:
1. **Donor Buckets ($\text{buckets}[i] > v$):** Buckets exceeding level $v$ can donate their excess volume:

$$\text{Surplus}(v) = \sum_{\text{buckets}[i] > v} (\text{buckets}[i] - v)$$

   Accounting for transmission loss, the total volume successfully delivered to other buckets is:

$$\text{Delivered}(v) = \text{Surplus}(v) \times \left(1 - \frac{\text{loss}}{100}\right)$$

2. **Recipient Buckets ($\text{buckets}[i] < v$):** Buckets below level $v$ require an influx of water to reach $v$:

$$\text{Deficit}(v) = \sum_{\text{buckets}[i] < v} (v - \text{buckets}[i])$$

### Monotonicity of the Feasibility Predicate
A uniform water level $v$ is physically achievable if and only if the delivered surplus equals or exceeds the total required deficit:

$$\mathcal{P}(v) = \left( \text{Delivered}(v) \ge \text{Deficit}(v) \right)$$

As $v$ increases:
- Each term in $\text{Surplus}(v)$ decreases, so $\text{Delivered}(v)$ is monotonically non-increasing.
- Each term in $\text{Deficit}(v)$ increases, so $\text{Deficit}(v)$ is monotonically non-decreasing.
Consequently, $\mathcal{P}(v)$ exhibits a single crossover threshold: it is `true` for all $v \le v^*$ and `false` for all $v > v^*$. This monotonicity permits binary search over continuous real values in $[0, \max(\text{buckets})]$.

| Concept | Mathematical Formula | Physical Meaning |
|---|---|---|
| Transfer Efficiency ($\eta$) | $1 - \frac{\text{loss}}{100}$ | Fraction of poured volume that reaches destination |
| Aggregate Surplus | $\sum \max(0, \text{buckets}[i] - v)$ | Total excess water extractable from donor buckets |
| Delivered Volume | $\eta \times \text{Surplus}(v)$ | Net water available to fill deficient buckets |
| Aggregate Deficit | $\sum \max(0, v - \text{buckets}[i])$ | Total water needed to lift lower buckets to $v$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Efficiency factor: $\eta = 1 - 0.80 = 0.20$.
Initial interval: $L = 0.0, R = 7.0$ (the maximum bucket capacity).

### Iteration 1: Probe $M = (0.0 + 7.0) / 2 = 3.5$
- Bucket 0 ($1$): Deficit $= 3.5 - 1.0 = 2.5$.
- Bucket 1 ($2$): Deficit $= 3.5 - 2.0 = 1.5$.
- Bucket 2 ($7$): Surplus $= 7.0 - 3.5 = 3.5$.
- Total Deficit $= 2.5 + 1.5 = 4.0$.
- Delivered Surplus $= 3.5 \times 0.20 = 0.70$.
- Check: $0.70 \ge 4.0$ is False. Water is insufficient.
- Action: Contract upper bound $R \leftarrow 3.5$. New interval: $[0.0, 3.5]$.

### Iteration 2: Probe $M = (0.0 + 3.5) / 2 = 1.75$
- Bucket 0 ($1$): Deficit $= 1.75 - 1.0 = 0.75$.
- Bucket 1 ($2$): Surplus $= 2.0 - 1.75 = 0.25$.
- Bucket 2 ($7$): Surplus $= 7.0 - 1.75 = 5.25$.
- Total Deficit $= 0.75$.
- Delivered Surplus $= (0.25 + 5.25) \times 0.20 = 5.50 \times 0.20 = 1.10$.
- Check: $1.10 \ge 0.75$ is True. Water is more than sufficient.
- Action: Contract lower bound $L \leftarrow 1.75$. New interval: $[1.75, 3.5]$.

### Iteration 3: Probe $M = (1.75 + 3.5) / 2 = 2.625$
- Bucket 0 ($1$): Deficit $= 2.625 - 1.0 = 1.625$.
- Bucket 1 ($2$): Deficit $= 2.625 - 2.0 = 0.625$.
- Bucket 2 ($7$): Surplus $= 7.0 - 2.625 = 4.375$.
- Total Deficit $= 1.625 + 0.625 = 2.25$.
- Delivered Surplus $= 4.375 \times 0.20 = 0.875$.
- Check: $0.875 \ge 2.25$ is False.
- Action: Contract upper bound $R \leftarrow 2.625$. New interval: $[1.75, 2.625]$.

### Subsequent Convergence to $v = 2.0$
As iterations proceed, the interval rapidly contracts around $2.0$:
- At $v = 2.0$:
  - Deficit $= (2.0 - 1.0) = 1.0$.
  - Surplus $= (7.0 - 2.0) = 5.0$.
  - Delivered $= 5.0 \times 0.20 = 1.0$.
  - Delivered $=$ Deficit ($1.0 = 1.0$).
The algorithm converges to $v = 2.00000$ within the required precision tolerance.

---

## 4. Comprehensive State Trace

The evaluation metrics across bisection probes are summarized below:

| Iteration | Lower Bound $L$ | Upper Bound $R$ | Midpoint Probe $M$ | Aggregate Surplus | Delivered Volume ($\eta \times \text{Surplus}$) | Total Deficit | Feasible? | Next Search Interval |
|---|---|---|---|---|---|---|---|---|
| $1$ | $0.000$ | $7.000$ | $3.500$ | $3.500$ | $0.700$ | $4.000$ | False | $[0.000, 3.500]$ |
| $2$ | $0.000$ | $3.500$ | $1.750$ | $5.500$ | $1.100$ | $0.750$ | True | $[1.750, 3.500]$ |
| $3$ | $1.750$ | $3.500$ | $2.625$ | $4.375$ | $0.875$ | $2.250$ | False | $[1.750, 2.625]$ |
| $4$ | $1.750$ | $2.625$ | $2.1875$ | $4.8125$ | $0.9625$ | $1.375$ | False | $[1.750, 2.1875]$ |
| $5$ | $1.750$ | $2.1875$ | $1.96875$ | $5.0625$ | $1.0125$ | $0.96875$ | True | $[1.96875, 2.1875]$ |
| $\infty$ | $2.000$ | $2.000$ | $2.000$ | $5.000$ | $1.000$ | $1.000$ | True | Converged at $2.0$ |

Final converged water level: $2.0$.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** For any target water level $v$, the water transferred out of donor buckets cannot exceed $\text{Surplus}(v)$. Because physics dictates that each unit transferred loses $\text{loss}\%$, the total volume arriving at destination buckets is strictly bounded above by $(1 - \frac{\text{loss}}{100})\text{Surplus}(v)$. If this arriving volume is at least $\text{Deficit}(v)$, water can be apportioned among all recipient buckets to bring each of them to level $v$.

**Completeness.** The function $f(v) = \text{Delivered}(v) - \text{Deficit}(v)$ is continuous, strictly decreasing, positive at $v = 0$ (assuming $\sum \text{buckets} > 0$), and negative at $v = \max(\text{buckets})$. By the Intermediate Value Theorem, a unique root $v^*$ exists where $f(v^*) = 0$. Binary search on the continuous domain bisects the interval by half on each iteration, reducing interval width to $(R_0 - L_0) \cdot 2^{-K}$. After $K = 80$ iterations, the interval width is under $10^{-20}$, guaranteeing convergence to within the requested $10^{-5}$ precision.

---

## 6. Edge Cases & Anti-Patterns

- **Zero Loss ($\text{loss} = 0$):** Water is conserved perfectly. The target level is simply the arithmetic mean $\frac{1}{n}\sum \text{buckets}[i]$.
- **Complete Loss ($\text{loss} = 100$):** No water can be transferred. The maximum equal level that can be guaranteed without transferring is the minimum bucket volume $\min(\text{buckets})$.
- **All Buckets Already Equal:** The initial spread is $0$, and the binary search immediately converges to the uniform volume.
- **Anti-Pattern — Floating-Point Equality While-Loops:** Using `while (R - L > eps)` can run into precision issues with float representations if `eps` is chosen too small. Performing a fixed number of bisection steps (e.g. 80 iterations) guarantees predictable termination and extreme precision.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n \cdot K)$, where $n$ is the number of buckets and $K \approx 80$ is the number of bisection iterations. In each iteration, we scan the $n$ buckets once to compute surplus and deficit in $\mathcal{O}(n)$ time. Total time is $\mathcal{O}(80n) = \mathcal{O}(n)$.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$. The algorithm requires only scalar floating-point variables for the search bounds, midpoints, and running sums.