# Guided Example: Car Fleet

We trace the step-by-step single-lane traffic kinematic constraints, car position sorting in descending proximity to target, unobstructed destination arrival time calculation ($t = \frac{target - pos}{spd}$), lead vehicle bottleneck domination ($t \le pre \implies \text{merge}$), new fleet creation thresholds ($t > pre$), and total car fleet count derivation on representative traffic streams:

- **Input:**
  $$
  target = 12, \quad position = [10, 8, 0, 5, 3], \quad speed = [2, 4, 1, 1, 3]
  $$
- **Required output:** `3`
  - Single-lane roadway dynamics:
    - Cars drive towards a common finish line at coordinate $target$.
    - The road is strictly single-lane: **cars can never pass each other**.
    - If a faster car catches up to a slower car ahead, it must decelerate to match the leader's speed and merges into the leader's **car fleet**.
    - If a car catches up exactly at the finish line $target$, they arrive as a single fleet.
    - Objective: Calculate the total number of distinct car fleets that cross the finish line.
    - For the 5 cars on road to target 12:
      - Car at 10 (speed 2): reaches target in $\frac{12 - 10}{2} = \mathbf{1.0\ hour}$.
      - Car at 8 (speed 4): reaches target in $\frac{12 - 8}{4} = \mathbf{1.0\ hour}$.
        - Catches up to the car at 10 right at the destination $\implies$ merges into **Fleet 1**.
      - Car at 5 (speed 1): reaches target in $\frac{12 - 5}{1} = \mathbf{7.0\ hours}$.
        - Too slow to catch Fleet 1 (takes 7 hours vs 1 hour) $\implies$ starts **Fleet 2**.
      - Car at 3 (speed 3): reaches target in $\frac{12 - 3}{3} = \mathbf{3.0\ hours}$.
        - Unobstructed time (3h) is faster than Fleet 2 (7h) $\implies$ catches up to Car 5 $\implies$ merges into **Fleet 2**.
      - Car at 0 (speed 1): reaches target in $\frac{12 - 0}{1} = \mathbf{12.0\ hours}$.
        - Slower than Fleet 2 (12h vs 7h) $\implies$ starts **Fleet 3**.
      - Resulting fleet count: **`3`**.
- **Descending Position Order & Bottleneck Arrival Time Invariant:**
  - **The Precedence Hierarchy:**
    - A car at position $p_1$ can only ever be obstructed by cars ahead of it ($p_2 > p_1$).
    - Cars behind $p_1$ can never slow down or obstruct car $p_1$.
    - Therefore, by sorting all cars in **descending order of starting position** (closest to the destination first), we process each car's bottleneck from front to back without any backward dependencies!
  - **The Unobstructed Arrival Time Metric:**
    - For a car at position $pos$ with speed $spd$:
      $$
      t = \frac{target - pos}{spd}
      $$
  - **The Merge Condition:**
    - Let $pre$ be the arrival time of the fleet immediately ahead.
    - **Case 1 ($t \le pre$):**
      - The trailing car arrives at the destination in less than or equal to the time taken by the leader ahead.
      - Because the trailing car cannot pass, it catches up before or at the finish line.
      - It joins the leader's fleet, adopting the leader's arrival time.
      - Fleet count remains unchanged.
    - **Case 2 ($t > pre$):**
      - The trailing car takes strictly longer to reach the destination than the fleet ahead.
      - The leader ahead will have already reached the finish line before this trailing car can ever catch up.
      - Therefore, this car **can never merge with the fleet ahead**.
      - It forms a **brand new fleet**, becoming the new bottleneck:
        $$
        ans \leftarrow ans + 1, \quad pre \leftarrow t
        $$
- **Step-by-Step Worked Execution Trace on the 5-Car Road:**
  - Destination: $target = 12$.
  - Pair and sort cars by position descending:
    1. Car A: $pos = 10, spd = 2$
    2. Car B: $pos = 8, spd = 4$
    3. Car C: $pos = 5, spd = 1$
    4. Car D: $pos = 3, spd = 3$
    5. Car E: $pos = 0, spd = 1$
  - Initialize state: $ans = 0, pre = 0.0$.
  - **Process Car A ($pos = 10, spd = 2$):**
    - Unobstructed arrival time:
      $$
      t = \frac{12 - 10}{2} = \frac{2}{2} = \mathbf{1.0}
      $$
    - Comparison: $t = 1.0 > pre = 0.0 \implies \mathbf{New\ Fleet\ 1\ Formed!}$
    - Update: $ans \leftarrow 0 + 1 = \mathbf{1}, pre \leftarrow \mathbf{1.0}$.
  - **Process Car B ($pos = 8, spd = 4$):**
    - Unobstructed arrival time:
      $$
      t = \frac{12 - 8}{4} = \frac{4}{4} = \mathbf{1.0}
      $$
    - Comparison: $t = 1.0 \le pre = 1.0 \implies \mathbf{Catches\ Up\ at\ Destination!}$
    - Action: Merges into Fleet 1. $ans$ and $pre$ remain unchanged ($ans = 1, pre = 1.0$).
  - **Process Car C ($pos = 5, spd = 1$):**
    - Unobstructed arrival time:
      $$
      t = \frac{12 - 5}{1} = \frac{7}{1} = \mathbf{7.0}
      $$
    - Comparison: $t = 7.0 > pre = 1.0 \implies \mathbf{Too\ Slow\ to\ Catch\ Fleet\ 1!}$
    - Action: Forms a new fleet (Fleet 2).
    - Update: $ans \leftarrow 1 + 1 = \mathbf{2}, pre \leftarrow \mathbf{7.0}$.
  - **Process Car D ($pos = 3, spd = 3$):**
    - Unobstructed arrival time:
      $$
      t = \frac{12 - 3}{3} = \frac{9}{3} = \mathbf{3.0}
      $$
    - Comparison: $t = 3.0 \le pre = 7.0 \implies \mathbf{Catches\ Up\ to\ Fleet\ 2!}$
    - Action: Merges into Fleet 2. $ans$ and $pre$ remain unchanged ($ans = 2, pre = 7.0$).
  - **Process Car E ($pos = 0, spd = 1$):**
    - Unobstructed arrival time:
      $$
      t = \frac{12 - 0}{1} = \frac{12}{1} = \mathbf{12.0}
      $$
    - Comparison: $t = 12.0 > pre = 7.0 \implies \mathbf{Too\ Slow\ to\ Catch\ Fleet\ 2!}$
    - Action: Forms a new fleet (Fleet 3).
    - Update: $ans \leftarrow 2 + 1 = \mathbf{3}, pre \leftarrow \mathbf{12.0}$.
  - **All Cars Processed:**
    $$
    ans = \mathbf{3}
    $$
- **Single Car Road ($target = 10, position = [3], speed = [3]$):**
  - Only 1 car $\implies$ forms exactly 1 fleet $\implies ans = \mathbf{1}$.
- **All Cars Merge into Single Fleet ($target = 100, position = [0, 2, 4], speed = [4, 2, 1]$):**
  - Pos 4 (spd 1): $t = (100 - 4)/1 = 96$.
  - Pos 2 (spd 2): $t = (100 - 2)/2 = 49 \le 96 \implies$ merges.
  - Pos 0 (spd 4): $t = (100 - 0)/4 = 25 \le 96 \implies$ merges.
  - Total fleets: $\mathbf{1}$.

This instance demonstrates monotone sorting and 1D particle aggregation under non-penetration velocity limits, mathematically proves why processing particles in reverse spatial order eliminates transitive merge propagation graphs, and derives $O(N \log N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given car starting positions, speeds, and a finish line at $target$:
Cars cannot pass; faster cars merge into slower cars ahead.
Find the **number of car fleets** at the finish line.

```text
target = 12
Cars sorted closest to target first:
  Pos 10 (spd 2): time = (12 - 10) / 2 = 1.0  -> Fleet 1 (pre = 1.0)
  Pos 8  (spd 4): time = (12 - 8)  / 4 = 1.0  -> merges into Fleet 1!
  Pos 5  (spd 1): time = (12 - 5)  / 1 = 7.0  -> Fleet 2 (pre = 7.0)
  Pos 3  (spd 3): time = (12 - 3)  / 3 = 3.0  -> merges into Fleet 2!
  Pos 0  (spd 1): time = (12 - 0)  / 1 = 12.0 -> Fleet 3 (pre = 12.0)

Total fleets = 3
Result: 3
```

### The Invariant of the Front-to-Back Bottleneck
- Sort cars by position descending (closest to target first).
- Calculate arrival time $t = (target - pos) / speed$.
- If $t \le pre$: catches up to the fleet ahead $\implies$ merges.
- If $t > pre$: cannot catch up $\implies$ creates a new fleet and sets new bottleneck $pre = t$.

---

## 2. Conceptual Foundation & Invariants

### 1. Unobstructed Arrival Time:
$$
T_i = \frac{target - position_i}{speed_i}
$$

### 2. Monotonic Fleet Formation Rule:
Sorting such that $position_{(1)} > position_{(2)} > \dots > position_{(n)}$:
$$
\text{Fleet}((k)) = \begin{cases}
\text{Fleet}((k - 1)) & T_{(k)} \le \max_{j < k} T_{(j)} \\
\text{New Fleet} & T_{(k)} > \max_{j < k} T_{(j)}
\end{cases}
$$
$$
ans = \sum_{k=1}^n \mathbb{I}\left[ T_{(k)} > \max_{j < k} T_{(j)} \right]
$$

> **Sticky Collision Particle Invariant.** In a 1D pressureless gas with inelastic sticking collisions and a terminal absorbing barrier at $target$, the number of clusters reaching the boundary equals the number of strict running maxima in the arrival time sequence ordered by initial position.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Sort by Position Descending
- $10, 8, 5, 3, 0$.

---

### Step 2: Car at 10
- $t = 2 / 2 = 1.0 \implies$ Fleet 1. $pre = 1.0$.

---

### Step 3: Car at 8
- $t = 4 / 4 = 1.0 \le 1.0 \implies$ merge into Fleet 1.

---

### Step 4: Car at 5
- $t = 7 / 1 = 7.0 > 1.0 \implies$ Fleet 2. $pre = 7.0$.

---

### Step 5: Car at 3
- $t = 9 / 3 = 3.0 \le 7.0 \implies$ merge into Fleet 2.

---

### Step 6: Car at 0
- $t = 12 / 1 = 12.0 > 7.0 \implies$ Fleet 3. $pre = 12.0$.

---

### Step 7: Output
$$
\mathbf{3}
$$

---

## 4. Complete Execution Trace

| Car Rank | Initial Position | Speed | Unobstructed Time $t$ | Bottleneck $pre$ | Action Taken | Total Fleets $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $10$ | $2$ | $1.0$ | $0.0$ | **Start Fleet 1** | $1$ |
| $2$ | $8$ | $4$ | $1.0$ | $1.0$ | Merge with Fleet 1 | $1$ |
| $3$ | $5$ | $1$ | $7.0$ | $1.0$ | **Start Fleet 2** | $2$ |
| $4$ | $3$ | $3$ | $3.0$ | $7.0$ | Merge with Fleet 2 | $2$ |
| **$5$** | **$0$** | **$1$** | **$12.0$** | **$7.0$** | **Start Fleet 3** | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Car ($n = 1$):** Always 1 fleet.
- **Identical Arrival Times ($1.0$ and $1.0$):** $t \le pre$ correctly merges cars reaching the line simultaneously.
- **Cars Start Far Apart with High Speeds:** The sorting guarantees that faster cars behind are evaluated against the leader ahead.
- **All Cars Form Separate Fleets:** Decreasing speeds ensure no car catches up $\implies N$ fleets.

---

## 6. Traps & Common Anti-Patterns

- **Sorting Ascending (Smallest Position First):** Processing from back to front requires dynamic lookahead into what happens ahead; sorting descending (closest to target first) makes the decision purely local and greedy.
- **Simulating Real-Time Positions Over Timesteps:** Trying to step forward second-by-second is continuous and causes TLE / floating-point rounding errors. Arrival time math solves the problem analytically.
- **Integer Division on Arrival Times:** Arrival times can be fractional (e.g. $7/3 = 2.33$ vs $5/2 = 2.5$). Always use floating-point division `/` rather than integer floor `//`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting indices by position: $\mathcal{O}(N \log N)$ where $N \le 10^5$.
  - Single pass through sorted array: $\mathcal{O}(N)$.
  - Total Time: strictly $\mathcal{O}(N \log N)$. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory to store sorted indices.
