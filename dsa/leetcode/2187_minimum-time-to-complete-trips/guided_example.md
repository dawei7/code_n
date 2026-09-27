# Guided Example: Minimum Time to Complete Trips

We analyze and trace the monotonic capacity bisection algorithm on a representative bus fleet scheduling instance, demonstrating how monotonicity of the aggregate completed-trip function over elapsed time reduces optimal duration scheduling to binary search over an upper-bounded time horizon in $O(n \log(\min(\text{time}) \cdot \text{totalTrips}))$ time.

- **Input:** `time = [1, 2, 3]`, `totalTrips = 5`
- **Output:** `3`

This instance demonstrates concurrent rate aggregation, monotone step function evaluation, upper-bound feasibility capping, and binary search range contraction.

---

## 1. Problem Overview & Representative Instance

We are given an integer array `time` where `time[i]` denotes the duration needed for bus $i$ to complete one round trip.
- Each bus operates independently and concurrently, starting a new trip immediately after completing the previous one.
- We are given an integer `totalTrips` denoting the required aggregate number of completed trips across all buses.
- We must find the **minimum elapsed time** $T$ at which the total number of completed trips across all buses is at least `totalTrips`.

In our representative instance:
- Three buses with durations `time = [1, 2, 3]`. Target `totalTrips = 5`.
- At time $T = 1$:
  - Bus 0: $\lfloor 1 / 1 \rfloor = 1$ trip.
  - Bus 1: $\lfloor 1 / 2 \rfloor = 0$ trips.
  - Bus 2: $\lfloor 1 / 3 \rfloor = 0$ trips.
  - Total: $1 + 0 + 0 = 1 < 5$.
- At time $T = 2$:
  - Bus 0: $\lfloor 2 / 1 \rfloor = 2$ trips.
  - Bus 1: $\lfloor 2 / 2 \rfloor = 1$ trip.
  - Bus 2: $\lfloor 2 / 3 \rfloor = 0$ trips.
  - Total: $2 + 1 + 0 = 3 < 5$.
- At time $T = 3$:
  - Bus 0: $\lfloor 3 / 1 \rfloor = 3$ trips.
  - Bus 1: $\lfloor 3 / 2 \rfloor = 1$ trip.
  - Bus 2: $\lfloor 3 / 3 \rfloor = 1$ trip.
  - Total: $3 + 1 + 1 = 5 \ge 5$ (Requirement satisfied!).
- Minimum required time is $3$.

---

## 2. Mathematical & Algorithmic Principles

### The Aggregate Trip Capacity Function

For any elapsed time $T \ge 0$, bus $i$ completes trips only at integer multiples of $\text{time}[i]$.
The number of full trips completed by bus $i$ by time $T$ is the floor quotient:
$$\text{trips}_i(T) = \left\lfloor \frac{T}{\text{time}[i]} \right\rfloor$$
The aggregate completed-trip capacity function across all $n$ buses is:
$$f(T) = \sum_{v \in \text{time}} \left\lfloor \frac{T}{v} \right\rfloor$$

### Monotonicity & Bisection

Because the floor function $x \mapsto \lfloor x / v \rfloor$ is non-decreasing for $v > 0$, the sum of these non-decreasing functions is also strictly non-decreasing:
$$T_1 \le T_2 \implies f(T_1) \le f(T_2)$$

This property guarantees that the boolean feasibility predicate:
$$P(T) = (f(T) \ge \text{totalTrips})$$
is monotonic:
$$P(T) = \begin{cases} \text{False} & \text{for } T < T^* \\ \text{True} & \text{for } T \ge T^* \end{cases}$$
The optimal time $T^*$ is the unique boundary point where $P(T)$ switches from False to True.

### Deriving the Search Horizon Bounds

1. **Lower Bound ($L$):**
   At time $T = 0$, $f(0) = 0 < \text{totalTrips}$. Since all trip times are $\ge 1$, the earliest possible non-zero time is $L = 1$.
2. **Feasible Upper Bound ($R$):**
   Consider the single fastest bus with duration $v_{\min} = \min(\text{time})$.
   Even if all other buses were decommissioned, this fastest bus alone would complete `totalTrips` trips in time:
   $$R = v_{\min} \times \text{totalTrips}$$
   Because the fleet working together can only complete trips faster than a single bus, the true optimal time satisfies $T^* \le R$.

| Variable / Parameter | Mathematical Formula | Algorithmic Role |
|---|---|---|
| Fleet Durations | $\text{time}[0 \dots n-1]$ | Individual bus cycle lengths |
| Required Target | $\text{totalTrips}$ | Aggregate completion quota |
| Capacity Function $f(T)$ | $\sum \lfloor T / v \rfloor$ | Total trips achieved by time $T$ |
| Feasible Upper Bound $R$ | $\min(\text{time}) \cdot \text{totalTrips}$ | Safe right endpoint for binary search |
| Probe Time $M$ | $\lfloor (L + R) / 2 \rfloor$ | Current midpoint being evaluated |

```mermaid
accTitle: Monotonic Capacity Binary Search
accDescr: Flowchart illustrating binary search over time horizon [L, R] using floor division summation.
flowchart TD
    Init["Initialize L = 1, R = min(time) * totalTrips"] --> Loop{"Is L < R?"}
    Loop -- "No (L == R)" --> Terminate["Optimal Time Found: Return L"]
    Loop -- "Yes" --> Mid["Compute M = L + (R - L) // 2"]
    Mid --> Eval["Calculate f(M) = sum(M // v for v in time)"]
    Eval --> Check{"f(M) >= totalTrips?"}
    Check -- "Yes (Sufficient trips)" --> ShrinkR["R = M: Solution in left half"]
    Check -- "No (Insufficient trips)" --> ShrinkL["L = M + 1: Must increase time"]
    ShrinkR & ShrinkL --> Loop
```

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `time = [1, 2, 3]` and `totalTrips = 5`.

### Step 1: Initial Bounds
- Fastest bus: $v_{\min} = \min(1, 2, 3) = 1$.
- Upper bound: $R = 1 \times 5 = 5$.
- Lower bound: $L = 1$.
- Search range: $[1, 5]$.

### Step 2: Binary Search Iteration 1
- Current interval: $[L, R] = [1, 5]$.
- Midpoint: $M = \lfloor (1 + 5) / 2 \rfloor = 3$.
- Evaluate capacity $f(3)$:
  - Bus with duration $1$: $\lfloor 3 / 1 \rfloor = 3$ trips.
  - Bus with duration $2$: $\lfloor 3 / 2 \rfloor = 1$ trip.
  - Bus with duration $3$: $\lfloor 3 / 3 \rfloor = 1$ trip.
  - Total trips: $f(3) = 3 + 1 + 1 = 5$.
- Feasibility check: $5 \ge 5$ (Sufficient!).
- Since $f(3)$ satisfies the quota, the optimal time is at most $3$.
- Shrink upper bound: $R = M = 3$.

### Step 3: Binary Search Iteration 2
- Current interval: $[L, R] = [1, 3]$.
- Midpoint: $M = \lfloor (1 + 3) / 2 \rfloor = 2$.
- Evaluate capacity $f(2)$:
  - Bus with duration $1$: $\lfloor 2 / 1 \rfloor = 2$ trips.
  - Bus with duration $2$: $\lfloor 2 / 2 \rfloor = 1$ trip.
  - Bus with duration $3$: $\lfloor 2 / 3 \rfloor = 0$ trips.
  - Total trips: $f(2) = 2 + 1 + 0 = 3$.
- Feasibility check: $3 < 5$ (Insufficient!).
- Time $2$ is strictly too small.
- Shrink lower bound: $L = M + 1 = 2 + 1 = 3$.

### Step 4: Convergence
- Current interval: $L = 3, R = 3$.
- Interval has collapsed to a single point ($L = R = 3$).
- The algorithm terminates and returns $L = 3$.

---

## 4. Comprehensive State Trace

The sequence of binary search probe points and bus capacities is documented below:

| Iteration | Search Interval $[L, R]$ | Midpoint Probe $M$ | Bus $0$ ($\lfloor M/1 \rfloor$) | Bus $1$ ($\lfloor M/2 \rfloor$) | Bus $2$ ($\lfloor M/3 \rfloor$) | Total Trips $f(M)$ | Feasible ($f(M) \ge 5$)? | Next Action |
|---|---|---|---|---|---|---|---|---|
| 1 | $[1, 5]$ | 3 | 3 | 1 | 1 | 5 | **Yes** ($5 \ge 5$) | $R \leftarrow 3$ |
| 2 | $[1, 3]$ | 2 | 2 | 1 | 0 | 3 | No ($3 < 5$) | $L \leftarrow 3$ |
| Halt | $[3, 3]$ | — | — | — | — | — | — | **Return 3** |

### Fleet Progress Across Integer Time Points

| Elapsed Time $T$ | Bus 1 Progress (`time = 1`) | Bus 2 Progress (`time = 2`) | Bus 3 Progress (`time = 3`) | Aggregate Trips $f(T)$ | Quota Met? |
|---|---|---|---|---|---|
| 1 | 1 | 0 | 0 | 1 | No |
| 2 | 2 | 1 | 0 | 3 | No |
| **3** | **3** | **1** | **1** | **5** | **Optimal Threshold Met** |
| 4 | 4 | 2 | 1 | 7 | Exceeds Quota |
| 5 | 5 | 2 | 1 | 8 | Exceeds Quota |

---

## 5. Algorithmic Correctness & Soundness

### Invariant Preservation
At each step of the binary search:
1. $T^*$ is guaranteed to lie in the range $[L, R]$.
2. $f(L - 1) < \text{totalTrips}$ (any time strictly less than $L$ is provably infeasible).
3. $f(R) \ge \text{totalTrips}$ (time $R$ is confirmed feasible).

When $M$ is evaluated:
- If $f(M) \ge \text{totalTrips}$, $M$ is feasible, so $T^* \le M$. Setting $R = M$ maintains invariant 3.
- If $f(M) < \text{totalTrips}$, $M$ and all times $\le M$ are infeasible, so $T^* \ge M + 1$. Setting $L = M + 1$ maintains invariant 2.
Because the interval length $R - L$ strictly decreases by at least a factor of two on each iteration, the loop terminates with $L = R = T^*$, proving mathematical soundness and exactness.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **64-Bit Integer Overflow in Upper Bound:**
   - When $\min(\text{time}) = 10^7$ and $\text{totalTrips} = 10^7$:
     $$R = 10^7 \times 10^7 = 10^{14}$$
   - This value exceeds the maximum signed 32-bit integer ($2^{31} - 1 \approx 2.14 \times 10^9$).
   - The bounds $L, R, M$ and arithmetic sums must use 64-bit integer types (`long long` in C++, `long` in Java).
2. **Single Bus ($n = 1$):**
   - E.g., `time = [2], totalTrips = 1`.
   - Upper bound is $2 \times 1 = 2$. Returns $2$.
3. **All Buses Identical:**
   - E.g., `time = [5, 5], totalTrips = 3`.
   - At $T = 5$, trips $= 1 + 1 = 2 < 3$. At $T = 10$, trips $= 2 + 2 = 4 \ge 3$. Returns $10$.

### Anti-Patterns to Avoid
- **Simulating Second-by-Second:** Incrementing $T = 1, 2, 3, \dots$ until $f(T) \ge \text{totalTrips}$ takes $O(T^* \cdot n)$ time. When $T^* = 10^{14}$, simulation would require billions of years. Binary search converges in at most $47$ iterations.
- **Floating-Point Division in Binary Search:** Computing $\sum T / v$ using floating-point math introduces rounding errors for large $T$. Floor integer division (`T // v`) is exact.

---

## 7. Complexity Analysis

- **Time Complexity:** $O(n \log(\min(\text{time}) \cdot \text{totalTrips}))$. The search space spans $[1, U]$ where $U \le 10^{14}$. The number of binary search iterations is $\lceil \log_2(10^{14}) \rceil \approx 47$. Each iteration evaluates $f(M)$ by summing over all $n$ buses in $O(n)$ time. For $n = 10^5$, total operations are at most $47 \times 10^5 \approx 4.7 \times 10^6$, executing in under $0.1$ seconds.
- **Auxiliary Space Complexity:** $O(1)$. Binary search updates scalar integer variables in place, requiring zero dynamic memory allocation.