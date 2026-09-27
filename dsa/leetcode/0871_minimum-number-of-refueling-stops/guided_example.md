# Guided Example: Minimum Number of Refueling Stops

We trace the step-by-step retroactive refueling greedy strategy, max-heap fuel capacity tracking, fuel-to-distance conversion ($1\text{ liter} = 1\text{ mile}$), deficit replenishment, and minimum stop count minimization on representative highway journeys:

- **Input:**
  $$
  target = 100, \quad startFuel = 10, \quad stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
  $$
- **Required output:** `2`
  - Journey dynamics & refueling constraints:
    - Journey starts at position $0$ with initial fuel $startFuel = 10$.
    - Destination is at position $target = 100$.
    - The car consumes $1$ liter of fuel for every $1$ mile traveled.
    - Along the way, there are $4$ gas stations at positions $[10, 20, 30, 60]$ offering $[60, 30, 30, 40]$ liters of fuel.
    - The car has an **infinite fuel capacity**: any acquired fuel can be stored indefinitely.
    - Objective: Find the **minimum number of refueling stops** needed to reach $target$, or return $-1$ if impossible.
    - For this instance:
      - Stop 1: Refuel at station at mile $10$ ($+60$ liters).
      - Stop 2: Refuel at station at mile $60$ ($+40$ liters).
      - Total fuel acquired: $10 + 60 + 40 = 110 \ge 100$.
      - Exactly $2$ stops required!
      - Result: **`2`**.
- **The Retroactive Refueling Invariant (Lazy Greed):**
  - **The Infinite Tank Equivalence:**
    - Because the fuel tank has infinite capacity, stopping at a station and refueling immediately is functionally identical to storing that station's fuel in a "reserve voucher" and redeeming it later whenever needed.
    - Therefore, the car should **drive forward as far as possible without stopping**.
  - **Greedy Deficit Replenishment:**
    - When the car's current fuel drops below zero upon attempting to reach the next position, the car has run dry.
    - To fix this deficit with the **fewest possible stops**, which past station should the car have stopped at?
    - The station with the **largest fuel capacity** among all stations passed so far!
    - We store the fuel amounts of all passed stations in a **max-heap**.
    - Whenever $fuel < 0$, we pop the maximum available fuel from the heap, add it to our reserves, and increment the stop counter $ans \leftarrow ans + 1$.
    - If the heap empties while fuel remains negative, even stopping at every single passed station is insufficient to cover the gap $\implies$ return $-1$.

---

## 1. Instance & Teaching Goal

Given $target = 100$, starting fuel $10$, and stations at $10, 20, 30, 60$:
Trace the fuel balance and max-heap across miles $0 \to 100$.

```text
Mile 0 -> 10:  Uses 10 fuel. Fuel = 0. Pass Station (10, 60) -> Heap: [60]
Mile 10 -> 20: Uses 10 fuel. Fuel = -10 (Deficit!).
               Retroactive refuel: Pop 60 -> Fuel = 50. (Stop 1)
               Pass Station (20, 30) -> Heap: [30]
Mile 20 -> 30: Uses 10 fuel. Fuel = 40. Pass Station (30, 30) -> Heap: [30, 30]
Mile 30 -> 60: Uses 30 fuel. Fuel = 10. Pass Station (60, 40) -> Heap: [40, 30, 30]
Mile 60 -> 100: Uses 40 fuel. Fuel = -30 (Deficit!).
                Retroactive refuel: Pop 40 -> Fuel = 10. (Stop 2)
                Target 100 reached!

Total Stops = 2
```

The teaching goal is to justify why deferred greedy selection on a max-heap guarantees minimum stops compared to dynamic programming.

---

## 2. Conceptual Foundation & Invariants

### 1. Distance Leg Transition:
Let $(pos_k, fuel_k)$ be station $k$, with destination treated as $(target, 0)$.
For leg from $pos_{k-1}$ to $pos_k$:
$$
dist = pos_k - pos_{k-1}
$$
$$
startFuel \leftarrow startFuel - dist
$$

### 2. Deficit Resolution Loop:
$$
\text{While } startFuel < 0 \land \text{heap} \ne \emptyset:
$$
$$
startFuel \leftarrow startFuel + \text{heap}.\text{pop\_max}()
$$
$$
ans \leftarrow ans + 1
$$
$$
\text{If } startFuel < 0 \land \text{heap} == \emptyset \implies \text{return } -1
$$

---

## 3. Step-by-Step Worked Execution

We trace with stations $[(10, 60), (20, 30), (30, 30), (60, 40), (100, 0)]$:
Initialize: $ans = 0, pre = 0, startFuel = 10, H = [\,]$.

---

### Step 1: Advance to Station 1 ($pos = 10, fuel = 60$)
- Leg distance: $dist = 10 - 0 = 10$.
- Fuel consumed: $startFuel \leftarrow 10 - 10 = 0$.
- Fuel is non-negative ($0 \ge 0$). No refueling needed.
- Add station's fuel to reserve pool: $H = [60]$.
- Update checkpoint: $pre \leftarrow 10$.

---

### Step 2: Advance to Station 2 ($pos = 20, fuel = 30$)
- Leg distance: $dist = 20 - 10 = 10$.
- Fuel consumed: $startFuel \leftarrow 0 - 10 = -10$.
- **Deficit Detected ($startFuel = -10 < 0$)!**
- Resolve deficit using max passed fuel:
  - Pop $\max(H) = 60$.
  - Replenish: $startFuel \leftarrow -10 + 60 = 50$.
  - Increment stops: $ans \leftarrow 0 + 1 = \mathbf{1}$.
- Fuel is now positive ($50 \ge 0$).
- Add station's fuel to reserve pool: $H = [30]$.
- Update checkpoint: $pre \leftarrow 20$.

---

### Step 3: Advance to Station 3 ($pos = 30, fuel = 30$)
- Leg distance: $dist = 30 - 20 = 10$.
- Fuel consumed: $startFuel \leftarrow 50 - 10 = 40$.
- Fuel is non-negative ($40 \ge 0$).
- Add station's fuel to reserve pool: $H = [30, 30]$.
- Update checkpoint: $pre \leftarrow 30$.

---

### Step 4: Advance to Station 4 ($pos = 60, fuel = 40$)
- Leg distance: $dist = 60 - 30 = 30$.
- Fuel consumed: $startFuel \leftarrow 40 - 30 = 10$.
- Fuel is non-negative ($10 \ge 0$).
- Add station's fuel to reserve pool: $H = [40, 30, 30]$.
- Update checkpoint: $pre \leftarrow 60$.

---

### Step 5: Advance to Final Destination ($pos = 100, fuel = 0$)
- Leg distance: $dist = 100 - 60 = 40$.
- Fuel consumed: $startFuel \leftarrow 10 - 40 = -30$.
- **Deficit Detected ($startFuel = -30 < 0$)!**
- Resolve deficit:
  - Pop $\max(H) = 40$.
  - Replenish: $startFuel \leftarrow -30 + 40 = 10$.
  - Increment stops: $ans \leftarrow 1 + 1 = \mathbf{2}$.
- Fuel is non-negative ($10 \ge 0$).
- Destination reached!

---

### Termination:
Destination $100$ reached with $10$ liters remaining.
- **Return: `2`**.

---

## 4. Complete Execution Trace

| Segment | Destination Mile | Leg Distance | Fuel Before Replenish | Deficit? | Refuel Action Taken | Effective Fuel | Max-Heap State | Total Stops $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| $0 \to 1$ | $10$ | $10$ | $10 - 10 = 0$ | No | None | $0$ | $[60]$ | $0$ |
| $1 \to 2$ | $20$ | $10$ | $0 - 10 = -10$ | **Yes** | **Pop $60$ (Stop 1)** | **$50$** | $[30]$ | **`1`** |
| $2 \to 3$ | $30$ | $10$ | $50 - 10 = 40$ | No | None | $40$ | $[30, 30]$ | $1$ |
| $3 \to 4$ | $60$ | $30$ | $40 - 30 = 10$ | No | None | $10$ | $[40, 30, 30]$ | $1$ |
| **$4 \to \text{Dest}$** | **$100$** | **$40$** | **$10 - 40 = -30$** | **Yes** | **Pop $40$ (Stop 2)** | **$10$** | $[30, 30]$ | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **$startFuel \ge target$:** Car reaches target without stopping at any station $\implies$ returns $0$.
- **First Station Beyond Reach ($startFuel < stations[0][0]$):** Heap is empty when deficit occurs $\implies$ returns $-1$.
- **Total Combined Fuel Less Than Target:** Sum of $startFuel$ and all station fuel $< target \implies$ heap eventually empties while $startFuel < 0 \implies$ returns $-1$.

---

## 6. Traps & Common Anti-Patterns

- **Dynamic Programming on Continuous Mile Values:** Attempting $DP[mile]$ is impossible because $target \le 10^9$.
- **2D DP Over Stations $\mathcal{O}(N^2)$:** While $DP[i][j]$ (max distance using $j$ stops among first $i$ stations) is polynomial, it requires $\mathcal{O}(N^2)$ time and space. The greedy max-heap approach solves the problem in $\mathcal{O}(N \log N)$ time and $\mathcal{O}(N)$ space.
- **Prematurely Refueling at Weak Stations:** Stopping at a station with 10 liters when a 60-liter station was available forces additional unnecessary stops.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Iterating through $N$ stations: $\mathcal{O}(N)$.
  - Each station fuel amount is pushed to the max-heap once and popped at most once: $\mathcal{O}(N \log N)$.
  - Total Time: $\mathcal{O}(N \log N)$, completing in $< 5$ ms for $N \le 500$.
- **Auxiliary Space Complexity:**
  - Priority queue stores at most $N$ elements: $\mathcal{O}(N)$ space.
