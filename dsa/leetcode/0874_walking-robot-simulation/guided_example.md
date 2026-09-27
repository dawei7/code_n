# Guided Example: Walking Robot Simulation

We trace the step-by-step 2D Cartesian heading updates, modular rotational arithmetic, unit step discrete simulation, obstacle collision halting, and maximum squared Euclidean distance tracking on representative robotic navigation paths:

- **Input:**
  $$
  commands = [4, -1, 4, -2, 4], \quad obstacles = [[2, 4]]
  $$
- **Required output:** `65`
  - Robot simulation rules:
    - The robot starts at origin $(0, 0)$ facing **North** ($+y$ direction).
    - Commands:
      - `-2`: Turn left $90^\circ$.
      - `-1`: Turn right $90^\circ$.
      - $1 \le c \le 9$: Move forward $c$ units step by step.
    - If the robot encounters an obstacle in its path, it halts before the obstacle and stays in its current cell for that command.
    - Objective: Return the **maximum Euclidean distance squared** ($x^2 + y^2$) from the origin reached at any point during the entire journey.
    - For $commands = [4, -1, 4, -2, 4]$ and obstacle at $(2, 4)$:
      - Cmd 1 (`4` North): $(0, 0) \to (0, 4)$. Dist sq: $0^2 + 4^2 = 16$.
      - Cmd 2 (`-1` Turn Right): Faces East.
      - Cmd 3 (`4` East): Moves to $(1, 4)$. Next cell $(2, 4)$ is an **obstacle**! Halts at $(1, 4)$. Dist sq: $1^2 + 4^2 = 17$.
      - Cmd 4 (`-2` Turn Left): Faces North.
      - Cmd 5 (`4` North): Moves 4 steps from $(1, 4) \to (1, 8)$. Dist sq: $1^2 + 8^2 = 1 + 64 = \mathbf{65}$.
      - Maximum squared distance reached: **`65`**.
- **The Stepwise Collision & Rotational Invariant:**
  - **Modular Direction Ring:**
    - The 4 cardinal directions are indexed $k \in \{0, 1, 2, 3\}$:
      $$
      0: \text{North } (0, 1), \quad 1: \text{East } (1, 0), \quad 2: \text{South } (0, -1), \quad 3: \text{West } (-1, 0)
      $$
    - Turning right ($+90^\circ$ clockwise):
      $$
      k \leftarrow (k + 1) \pmod 4
      $$
    - Turning left ($-90^\circ$ counter-clockwise):
      $$
      k \leftarrow (k + 3) \pmod 4
      $$
  - **Unit-Step Collision Evaluation:**
    - An obstacle prevents jumping over it. Therefore, moving $c$ steps must be evaluated **one unit at a time**.
    - For each step, candidate $(nx, ny) = (x + dx, y + dy)$.
    - If $(nx, ny) \in \text{obstacles}$, break out of the loop immediately; the robot stays at $(x, y)$.
    - Otherwise, update $(x, y) \leftarrow (nx, ny)$ and update running maximum $ans \leftarrow \max(ans, x^2 + y^2)$.

---

## 1. Instance & Teaching Goal

Given $commands = [4, -1, 4, -2, 4]$ and an obstacle at $(2, 4)$, simulate the path and capture the peak distance squared.

```text
Y-Axis
 8 |          [Finish (1, 8)] -> dist^2 = 1^2 + 8^2 = 65 (MAX!)
 7 |             ^
 6 |             |
 5 |             |
 4 |    (0, 4) ->(1, 4)  [X (2, 4) Obstacle blocks East movement!]
 3 |       ^
 2 |       |
 1 |       |
 0 |   [Start (0, 0)]
---+----------------------------- X-Axis
       0         1         2
```

The teaching goal is to show how unit-step discretization prevents obstacle tunneling while maintaining peak metric tracking across all intermediate points.

---

## 2. Conceptual Foundation & Invariants

### 1. Directional Vectors:
$$
\text{dirs} = [(0, 1), (1, 0), (0, -1), (-1, 0)]
$$

### 2. State Vector:
State is represented as $(x, y, k) \in \mathbb{Z} \times \mathbb{Z} \times \mathbb{Z}_4$.
Metric maintained:
$$
\text{metric}(x, y) = x^2 + y^2
$$
$$
ans \leftarrow \max(ans, x^2 + y^2)
$$

---

## 3. Step-by-Step Worked Execution

Obstacle set: $S = \{(2, 4)\}$.
Initialize: $(x, y) = (0, 0)$, $k = 0$ (North), $ans = 0$.

---

### Step 1: Command `4` (Move 4 units North)
- Direction vector: $(0, 1)$.
- Unit steps:
  - Step 1: $(0, 1) \notin S \implies (x, y) = (0, 1), ans = \max(0, 1) = 1$.
  - Step 2: $(0, 2) \notin S \implies (x, y) = (0, 2), ans = \max(1, 4) = 4$.
  - Step 3: $(0, 3) \notin S \implies (x, y) = (0, 3), ans = \max(4, 9) = 9$.
  - Step 4: $(0, 4) \notin S \implies (x, y) = (0, 4), ans = \max(9, 16) = \mathbf{16}$.

---

### Step 2: Command `-1` (Turn Right $90^\circ$)
- Update heading:
  $$
  k \leftarrow (0 + 1) \pmod 4 = 1 \quad (\text{East})
  $$
- Direction vector: $(1, 0)$.
- Coordinates remain $(0, 4)$.

---

### Step 3: Command `4` (Move 4 units East)
- Direction vector: $(1, 0)$.
- Unit steps:
  - Step 1: $(0 + 1, 4) = (1, 4) \notin S \implies (x, y) = (1, 4)$.
    - $dist^2 = 1^2 + 4^2 = 1 + 16 = 17 \implies ans = \max(16, 17) = \mathbf{17}$.
  - Step 2: $(1 + 1, 4) = (2, 4)$.
    - Check obstacle: $(2, 4) \in S \implies$ **Collision Detected!**
    - Abort remaining steps of this command.
    - Robot remains at $(1, 4)$.

---

### Step 4: Command `-2` (Turn Left $90^\circ$)
- Update heading:
  $$
  k \leftarrow (1 + 3) \pmod 4 = 4 \pmod 4 = 0 \quad (\text{North})
  $$
- Direction vector: $(0, 1)$.
- Coordinates remain $(1, 4)$.

---

### Step 5: Command `4` (Move 4 units North)
- Direction vector: $(0, 1)$.
- Unit steps from $(1, 4)$:
  - Step 1: $(1, 5) \notin S \implies (1, 5)$, $dist^2 = 1 + 25 = 26$.
  - Step 2: $(1, 6) \notin S \implies (1, 6)$, $dist^2 = 1 + 36 = 37$.
  - Step 3: $(1, 7) \notin S \implies (1, 7)$, $dist^2 = 1 + 49 = 50$.
  - Step 4: $(1, 8) \notin S \implies (1, 8)$, $dist^2 = 1 + 64 = \mathbf{65}$.
- Update maximum: $ans = \max(17, 65) = \mathbf{65}$.

---

### Termination:
All commands processed.
- **Maximum distance squared:** **`65`**.

---

## 4. Complete Execution Trace

| Command Index | Command Value | Action Description | Facing Heading | Robot Position $(x, y)$ | Obstacle Struck? | Current $x^2 + y^2$ | Running Max $ans$ |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| Start | — | Initial state | North ($0$) | $(0, 0)$ | — | $0$ | $0$ |
| $1$ | `4` | Move 4 North | North ($0$) | $(0, 4)$ | No | $16$ | $16$ |
| $2$ | `-1` | Turn Right | East ($1$) | $(0, 4)$ | No | $16$ | $16$ |
| $3$ | `4` | Move East (halts at $(1, 4)$) | East ($1$) | $(1, 4)$ | **Yes at $(2, 4)$** | $17$ | $17$ |
| $4$ | `-2` | Turn Left | North ($0$) | $(1, 4)$ | No | $17$ | $17$ |
| **$5$** | **`4`** | **Move 4 North** | **North ($0$)** | **$(1, 8)$** | **No** | **$65$** | **`65`** |

---

## 5. Boundary Cases & Failure Modes

- **Unobstructed Straight Line ($[4, -1, 3]$):** Moves $4$ North, $3$ East $\implies (3, 4)$, dist sq $= 3^2 + 4^2 = 25$.
- **Blocked at First Step:** Obstacle at $(0, 1)$ with command `5` North $\implies$ robot cannot take even 1 step, stays at $(0, 0)$.
- **Negative Coordinates:** Moving South or West produces negative coordinates; squaring handles signs naturally ($(-3)^2 = 9$).
- **Maximum Commands ($10^4$) with Max Steps ($9$):** At most $9 \times 10^4$ unit steps evaluated.

---

## 6. Traps & Common Anti-Patterns

- **Checking Only Final Position of Each Command:** If a robot steps far away and then walks back towards the origin, checking only end-of-command coordinates misses the peak intermediate distance.
- **Array Linear Search for Obstacles:** Searching an array of $K$ obstacles on every single step takes $\mathcal{O}(C \cdot K)$ time ($9 \times 10^4 \times 10^4 \approx 9 \times 10^8$ operations), causing TLE. Pre-populating a hash set provides $\mathcal{O}(1)$ obstacle queries.
- **Floating-Point Square Root:** Calculating $\sqrt{x^2 + y^2}$ causes precision loss and slow floating-point arithmetic; the problem asks strictly for the integer squared distance.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Obstacle hash set construction: $\mathcal{O}(K)$ where $K$ is the number of obstacles ($K \le 10^4$).
  - Simulating $C$ commands: at most $9 \times C$ unit steps ($C \le 10^4$).
  - Each unit step performs an $\mathcal{O}(1)$ hash set lookup.
  - Total Time: strictly $\mathcal{O}(K + C)$, running in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - Hash set storing $K$ coordinate pairs: $\mathcal{O}(K)$ space.
