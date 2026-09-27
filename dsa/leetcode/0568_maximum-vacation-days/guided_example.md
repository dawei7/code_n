# Guided Example: Maximum Vacation Days

We trace the step-by-step weekly flight transition modeling ($flights[i][j] == 1$), city stay preservation ($f[k-1][j]$), reachability negative-infinity masking ($-\infty$), weekly vacation yield addition ($days[j][k-1]$), dynamic programming grid propagation, and global maximum vacation day optimization on representative flight networks:

- **Input:**
  $$
  flights = \begin{bmatrix}
  0 & 1 & 1 \\
  1 & 0 & 1 \\
  1 & 1 & 0
  \end{bmatrix}, \quad
  days = \begin{bmatrix}
  1 & 3 & 1 \\
  6 & 0 & 3 \\
  3 & 3 & 3
  \end{bmatrix}
  $$
- **Required output:** `12`
  - Problem specifications:
    - Number of cities: $n = 3$ (labeled $0, 1, 2$).
    - Number of weeks: $K = 3$ (weeks $1, 2, 3$).
    - Starting state: The employee begins at **City 0** on Monday morning of Week 1.
    - At the start of each week, the employee can choose to stay in their current city or take an available flight to another city.
    - Spending week $w$ in city $j$ grants $days[j][w]$ vacation days.
- **Dynamic Programming Formulation ($f[k][j]$):**
  - Let $f[k][j]$ denote the maximum cumulative vacation days gathered through week $k$ ending in city $j$.
  - **Base State (Week 0):**
    - The employee starts at City 0 with 0 vacation days:
      $$
      f[0][0] = 0, \quad f[0][1] = -\infty, \quad f[0][2] = -\infty
      $$
  - **Weekly Transition (from week $k - 1$ to week $k$):**
    - To spend week $k$ at city $j$, the employee could:
      1. Stay at city $j$ from week $k-1$: inherited score $f[k-1][j]$.
      2. Fly into city $j$ from another city $i$ (valid if $flights[i][j] == 1$): score $f[k-1][i]$.
    - Take the maximum across all reachable source cities:
      $$
      \text{best\_prev} = \max\left( f[k-1][j], \; \max_{i: flights[i][j]=1} f[k-1][i] \right)
      $$
    - Add the vacation days earned in city $j$ during week $k$:
      $$
      f[k][j] = \text{best\_prev} + days[j][k-1]
      $$
- **Execution trace over $K = 3$ weeks:**
  - **Week 1 ($k = 1$, evaluates $days[\dots][0] = [1, 6, 3]$):**
    - Candidate sources: Only City 0 is reachable ($f[0][0] = 0$).
    - **Ending at City 0:**
      - Stay at City 0: $0 + days[0][0] = 0 + 1 = \mathbf{1}$.
    - **Ending at City 1:**
      - Fly from City 0 ($flights[0][1] = 1$): $0 + days[1][0] = 0 + 6 = \mathbf{6}$.
    - **Ending at City 2:**
      - Fly from City 0 ($flights[0][2] = 1$): $0 + days[2][0] = 0 + 3 = \mathbf{3}$.
    - DP table after Week 1:
      $$
      f[1] = [1, \; \mathbf{6}, \; 3]
      $$
  - **Week 2 ($k = 2$, evaluates $days[\dots][1] = [3, 0, 3]$):**
    - Available from Week 1: City 0 ($1$), City 1 ($6$), City 2 ($3$).
    - **Ending at City 0:**
      - Stay at 0 ($1$), fly from 1 ($6$), fly from 2 ($3$).
      - Best entry: $\max(1, 6, 3) = 6$ (flying from City 1).
      - Vacation days: $6 + days[0][1] = 6 + 3 = \mathbf{9}$.
    - **Ending at City 1:**
      - Stay at 1 ($6$), fly from 0 ($1$), fly from 2 ($3$).
      - Best entry: $\max(6, 1, 3) = 6$.
      - Vacation days: $6 + days[1][1] = 6 + 0 = \mathbf{6}$.
    - **Ending at City 2:**
      - Stay at 2 ($3$), fly from 0 ($1$), fly from 1 ($6$).
      - Best entry: $\max(3, 1, 6) = 6$ (flying from City 1).
      - Vacation days: $6 + days[2][1] = 6 + 3 = \mathbf{9}$.
    - DP table after Week 2:
      $$
      f[2] = [\mathbf{9}, \; 6, \; \mathbf{9}]
      $$
  - **Week 3 ($k = 3$, evaluates $days[\dots][2] = [1, 3, 3]$):**
    - Available from Week 2: City 0 ($9$), City 1 ($6$), City 2 ($9$).
    - **Ending at City 0:**
      - Best arrival: $\max(f[2][0], f[2][1], f[2][2]) = \max(9, 6, 9) = 9$.
      - Vacation days: $9 + days[0][2] = 9 + 1 = \mathbf{10}$.
    - **Ending at City 1:**
      - Best arrival: $\max(9, 6, 9) = 9$ (flying from City 0 or City 2).
      - Vacation days: $9 + days[1][2] = 9 + 3 = \mathbf{12}$.
    - **Ending at City 2:**
      - Best arrival: $\max(9, 6, 9) = 9$ (staying at 2 or flying from 0).
      - Vacation days: $9 + days[2][2] = 9 + 3 = \mathbf{12}$.
    - DP table after Week 3:
      $$
      f[3] = [10, \; \mathbf{12}, \; \mathbf{12}]
      $$
  - All $K = 3$ weeks completed.
  - Global maximum vacation days:
    $$
    \max(10, 12, 12) = \mathbf{12}
    $$
- **Disconnected City Instance:**
  - If City 2 has no incoming flights from any reachable city, its state remains $-\infty$ for all weeks, preventing invalid teleportation.
- **Staying in the Same City Throughout:**
  - If all flight matrix values are 0, employee must stay in City 0 $\implies \sum_{w} days[0][w]$.

This instance demonstrates multistage decision process dynamic programming over time-expanded digraphs, mathematically proves why $-\infty$ initialization enforces reachability constraints from the initial node, and derives $O(K \cdot N^2)$ runtime and $O(K \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ adjacency matrix $flights$ and an $n \times K$ vacation matrix $days$:
You start at **City 0** on Week 1.
In each week, you can stay in your current city or fly to any connected city, earning that city's vacation days for that week.
Find the **maximum vacation days** you can take over all $K$ weeks.

```text
Cities: 0, 1, 2     Weeks: 1, 2, 3

Week 1: Fly 0 -> 1    (Earns days[1][0] = 6)
Week 2: Fly 1 -> 2    (Earns days[2][1] = 3)
Week 3: Stay in 2     (Earns days[2][2] = 3)

Total Vacation Days = 6 + 3 + 3 = 12
```

### Time-Expanded Digraph Principle
- The decision is staged across $K$ consecutive weeks.
- The state at week $k$ depends only on the city you ended up in at week $k - 1$.
- This forms a classic layered DAG (Directed Acyclic Graph) of size $K \times N$.
- Using dynamic programming:
  $$
  f[k][j] = \text{Max vacation days ending in city } j \text{ at week } k
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. Reachability Masking:
Initialize all states to $-\infty$, except the starting condition:
$$
f[0][0] = 0, \quad f[0][j] = -\infty \quad (\forall j \ne 0)
$$
This mathematically prevents using vacation days from a city that has not yet been legally reached.

### 2. The Recurrence Relation:
For week $k \in [1, K]$ and destination city $j \in [0, n - 1]$:
$$
f[k][j] = \max\left( f[k-1][j], \; \max_{i: flights[i][j]=1} f[k-1][i] \right) + days[j][k-1]
$$

### 3. Answer Extraction:
$$
\text{Ans} = \max_{j \in [0, n - 1]} f[K][j]
$$

> **Temporal Causality Invariant.** Because transitions occur only between week $k-1$ and week $k$, no flight can travel backwards in time, ensuring optimal substructure and acyclic progression.

---

## 3. Step-by-Step Worked Execution

We trace the $3 \times 3$ matrix over 3 weeks:

---

### Step 1: Base State ($k = 0$)
$$
f[0] = [0, \; -\infty, \; -\infty]
$$

---

### Step 2: Week 1
From City 0, we can reach City 0 (stay), City 1 (fly), City 2 (fly).
- $f[1][0] = 0 + 1 = \mathbf{1}$
- $f[1][1] = 0 + 6 = \mathbf{6}$
- $f[1][2] = 0 + 3 = \mathbf{3}$
State: $f[1] = [1, 6, 3]$.

---

### Step 3: Week 2
All 3 cities have flights to each other.
Maximum incoming score to any city is $\max(1, 6, 3) = \mathbf{6}$ (arriving from City 1).
- $f[2][0] = 6 + days[0][1] = 6 + 3 = \mathbf{9}$
- $f[2][1] = 6 + days[1][1] = 6 + 0 = \mathbf{6}$
- $f[2][2] = 6 + days[2][1] = 6 + 3 = \mathbf{9}$
State: $f[2] = [9, 6, 9]$.

---

### Step 4: Week 3
Maximum incoming score to any city is $\max(9, 6, 9) = \mathbf{9}$.
- $f[3][0] = 9 + days[0][2] = 9 + 1 = \mathbf{10}$
- $f[3][1] = 9 + days[1][2] = 9 + 3 = \mathbf{12}$
- $f[3][2] = 9 + days[2][2] = 9 + 3 = \mathbf{12}$
State: $f[3] = [10, 12, 12]$.

---

### Step 5: Global Maximum
$$
\max(10, 12, 12) = \mathbf{12}
$$

---

## 4. Complete Execution Trace

| Week $k$ | City 0 Best ($+days$) | City 1 Best ($+days$) | City 2 Best ($+days$) | Optimal Vector $f[k]$ |
|:---:|:---:|:---:|:---:|:---:|
| **$0$** | $0$ | $-\infty$ | $-\infty$ | `[0, -inf, -inf]` |
| **$1$** | $0 + 1 = 1$ | $0 + 6 = 6$ | $0 + 3 = 3$ | `[1, 6, 3]` |
| **$2$** | $6 + 3 = 9$ | $6 + 0 = 6$ | $6 + 3 = 9$ | `[9, 6, 9]` |
| **$3$** | $9 + 1 = 10$ | $9 + 3 = \mathbf{12}$ | $9 + 3 = \mathbf{12}$ | **`[10, 12, 12]`** |
| **Final** | — | — | — | **Result: $12$** |

---

## 5. Boundary Cases & Failure Modes

- **No Flights Available ($flights[i][j] = 0$ everywhere):** Employee is trapped in City 0 $\implies$ accumulates $\sum_{w} days[0][w]$.
- **Single City ($N = 1$):** Sum of all vacation days for City 0 across all $K$ weeks.
- **Single Week ($K = 1$):** Choose between staying at 0 or taking a single initial flight.
- **Unreachable Cities:** Initialized to $-\infty$ and cannot propagate scores until a flight from an active city arrives.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Selection per Week:** Choosing the city with the most vacation days in week $w$ may strand the employee in a city with poor connections or zero days in future weeks. DP evaluates the global path.
- **Forgetting that Staying is Always Free:** Even if $flights[i][i] == 0$ in the input, an employee is always allowed to remain in their current city.
- **Initializing Non-Start Cities to 0:** Setting $f[0][j] = 0$ for $j \ne 0$ allows the employee to start in any city, violating the contract that the employee must start at City 0.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The DP table has $(K + 1) \times N$ entries.
  - Computing each entry checks $N$ possible incoming cities: $O(N)$.
  - Total Time: $\mathcal{O}(K \cdot N^2)$. For $N = 100, K = 100$, $100 \times 100^2 = 10^6$ operations, completing in $< 25$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K \cdot N)$ space for the DP table (can be compressed to $O(N)$ with rolling arrays).
