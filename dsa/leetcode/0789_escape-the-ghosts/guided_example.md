# Guided Example: Escape the Ghosts

We trace the step-by-step 2D grid Manhattan distance metric ($L_1$), simultaneous movement dynamics, player-to-target shortest path calculation ($|tx| + |ty|$), ghost-to-target interception bounds ($|tx - x| + |ty - y|$), Triangle Inequality interception theorem (target camping dominance), and strict escape feasibility verification on representative coordinate game boards:

- **Input:**
  - Ghosts: $ghosts = [[1, 0], \; [0, 3]]$
  - Destination: $target = [0, 1]$
  - Player starts at: $(0, 0)$
- **Required output:** `true`
  - Pac-Man grid pursuit mechanics:
    - Player starts at the origin $(0, 0)$ and moves 1 step per turn in any cardinal direction to reach $target = (tx, ty)$.
    - Each ghost starts at its initial coordinate and can also move 1 step per turn.
    - Moves occur simultaneously.
    - If a ghost occupies the same cell as the player at any point in time (including at the target), the player is captured.
    - Objective: Return `true` if the player can reach $target$ without being captured, or `false` otherwise.
    - For $ghosts = [[1, 0], [0, 3]], target = [0, 1]$:
      - Player distance from $(0, 0)$ to $(0, 1)$:
        $$
        d_{\text{player}} = |0 - 0| + |1 - 0| = 1 \text{ step}
        $$
      - Ghost 1 at $(1, 0)$ distance to $(0, 1)$:
        $$
        d_{G1} = |0 - 1| + |1 - 0| = 1 + 1 = 2 \text{ steps}
        $$
      - Ghost 2 at $(0, 3)$ distance to $(0, 1)$:
        $$
        d_{G2} = |0 - 0| + |1 - 3| = 0 + 2 = 2 \text{ steps}
        $$
      - The player arrives at $(0, 1)$ in 1 turn.
      - Neither ghost can arrive before turn 2.
      - Player escapes safely $\implies$ return **`true`**.
- **The Target Camping Dominance Theorem ($L_1$ Metric Invariant):**
  - **Player Shortest Path:**
    - On a 2D integer lattice, the minimum number of turns for the player to reach $target$ is the Manhattan ($L_1$) distance:
      $$
      d_{\text{player}} = |tx| + |ty|
      $$
  - **Ghost Interception Capability:**
    - Suppose a ghost at $(x, y)$ can intercept the player at some intermediate cell $P$ at time $t$.
    - Then the ghost could alternatively just march directly to $target$!
    - By the Triangle Inequality in the Manhattan metric:
      $$
      \text{dist}(ghost, target) \le \text{dist}(ghost, P) + \text{dist}(P, target)
      $$
    - Because the player's path is optimal, $\text{dist}(P, target) = d_{\text{player}} - t$.
    - Thus, if a ghost can intercept the player at $P$, it can reach $target$ in at most $t + (d_{\text{player}} - t) = d_{\text{player}}$ steps!
    - In other words: **A ghost can intercept the player somewhere if and only if it can reach the target at or before the player**:
      $$
      d_{\text{ghost}} \le d_{\text{player}}
      $$
  - **Safe Escape Condition:**
    - The player escapes if and only if **every ghost** is strictly further from the target than the player:
      $$
      \forall (x, y) \in ghosts: \quad |tx - x| + |ty - y| > |tx| + |ty|
      $$
    - No complicated graph search or chase simulation is needed!
- **Step-by-Step Worked Execution Trace on $ghosts = [[1, 0], [0, 3]], target = [0, 1]$:**
  - Target coordinates: $(tx, ty) = (0, 1)$.
  - **Step 1: Calculate Player Minimal Time:**
    $$
    d_{\text{player}} = |tx - 0| + |ty - 0| = |0| + |1| = \mathbf{1} \text{ turn}
    $$
  - **Step 2: Evaluate Ghost 1 at $(1, 0)$:**
    - Compute Manhattan distance to target $(0, 1)$:
      $$
      d_{G1} = |0 - 1| + |1 - 0| = 1 + 1 = \mathbf{2} \text{ turns}
      $$
    - Test condition:
      $$
      d_{G1} > d_{\text{player}} \iff 2 > 1 \implies \mathbf{Safe\ from\ Ghost\ 1!}
      $$
  - **Step 3: Evaluate Ghost 2 at $(0, 3)$:**
    - Compute Manhattan distance to target $(0, 1)$:
      $$
      d_{G2} = |0 - 0| + |1 - 3| = 0 + 2 = \mathbf{2} \text{ turns}
      $$
    - Test condition:
      $$
      d_{G2} > d_{\text{player}} \iff 2 > 1 \implies \mathbf{Safe\ from\ Ghost\ 2!}
      $$
  - **Step 4: Formulate Global Decision:**
    - Both ghosts require strictly more turns ($2 > 1$) than the player to reach $target$.
    - The player takes 1 step north to $(0, 1)$ on turn 1 and wins immediately.
    - Result:
      $$
      ans = \mathbf{true}
      $$
- **Ghost Interception Failure Trace ($ghosts = [[1, 0]], target = [2, 0]$):**
  - Player distance to $(2, 0)$: $|2| + |0| = 2$ turns.
  - Ghost distance from $(1, 0)$ to $(2, 0)$: $|2 - 1| + |0 - 0| = 1$ turn.
  - Ghost reaches $(2, 0)$ in 1 turn, waits there, and captures the player on turn 2.
  - Condition $d_{\text{ghost}} > d_{\text{player}} \iff 1 > 2$ fails!
  - Returns **`false`**.
- **Tied Arrival Trace ($d_{\text{ghost}} == d_{\text{player}}$):**
  - If a ghost arrives at the target at the exact same turn as the player, it captures the player on arrival.
  - Strict inequality ($>$) is required $\implies$ returns **`false`**.

This instance demonstrates differential game pursuit-evasion on $L_1$ metric spaces and geodesic dominance reduction, mathematically proves why the Triangle Inequality collapses trajectory interception into destination arrival time comparisons, and derives $O(G)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given player at $(0, 0)$, $target$, and a list of $ghosts$:
Can the player reach $target$ before any ghost captures them?

```text
Player starts at (0, 0).
Target: (0, 1) -> Player distance = |0| + |1| = 1 step.

Ghosts:
  Ghost 1 at (1, 0): dist to target = |0 - 1| + |1 - 0| = 2 steps
  Ghost 2 at (0, 3): dist to target = |0 - 0| + |1 - 3| = 2 steps

Player arrives in 1 step.
Both ghosts need 2 steps.
Player escapes!
Result: true
```

### The Invariant of the Target Camping Dominance
- By the Manhattan Triangle Inequality, if a ghost can intercept the player anywhere along their route, it can also reach the target at or before the player.
- Therefore, the player can escape if and only if **every ghost is strictly further from the target than the player**:
  $$|tx - x| + |ty - y| > |tx| + |ty|$$

---

## 2. Conceptual Foundation & Invariants

### 1. Manhattan Metric Distances:
$$
d_{\text{player}} = |tx| + |ty|
$$
$$
d_{\text{ghost}}(x, y) = |tx - x| + |ty - y|
$$

### 2. Universal Escape Predicate:
$$
\text{canEscape} \iff \forall (x, y) \in ghosts: \quad d_{\text{ghost}}(x, y) > d_{\text{player}}
$$

> **Geodesic Interception Domination Invariant.** In the normed vector space $(\mathbb{R}^2, \|\cdot\|_1)$, the intersection of reachable cones $B_1(ghost, t) \cap B_1(origin, t)$ along any optimal geodesic to $target$ is non-empty only if $\|ghost - target\|_1 \le \|target\|_1$.

---

## 3. Step-by-Step Worked Execution

We trace $ghosts = [[1, 0], [0, 3]], target = [0, 1]$:

---

### Step 1: Player Distance
- $d_{\text{player}} = |0| + |1| = 1$.

---

### Step 2: Ghost 1 $(1, 0)$
- $d_1 = |0 - 1| + |1 - 0| = 1 + 1 = 2 > 1$ (Safe).

---

### Step 3: Ghost 2 $(0, 3)$
- $d_2 = |0 - 0| + |1 - 3| = 0 + 2 = 2 > 1$ (Safe).

---

### Step 4: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| Entity | Position | Distance to Target $(0, 1)$ | Condition $d > d_{\text{player}}$? | Safe? |
|:---:|:---:|:---:|:---:|:---:|
| Player | $(0, 0)$ | $1$ (Benchmark) | — | — |
| Ghost 1 | $(1, 0)$ | $2$ | $2 > 1$ | Yes |
| **Ghost 2** | **$(0, 3)$** | **$2$** | **$2 > 1$** | **Yes** |
| **Final** | — | — | — | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Ghost Closer Than Player ($[1, 0]$ vs $[2, 0]$):** Ghost needs 1 step, player needs 2 $\implies$ returns `false`.
- **Tied Distance ($d_{\text{ghost}} == d_{\text{player}}$):** Ghost reaches target at same time, capturing player $\implies$ returns `false`.
- **Ghost Starts on Target:** Ghost distance 0 $\le d_{\text{player}} \implies$ returns `false`.
- **Target at Origin ($[0, 0]$):** Player distance 0 $\implies$ returns `true` (unless ghost also at origin).

---

## 6. Traps & Common Anti-Patterns

- **Attempting Minimax / Game Tree Search:** A full game search with multiple ghosts on a continuous grid is intractable and exponential. The problem reduces completely to a static distance inequality!
- **Simulating Paths Step-by-Step:** Checking if player can dodge ghosts step-by-step is unnecessary; if $d_{\text{ghost}} > d_{\text{player}}$, the player simply walks straight to the target without dodging.
- **Using Euclidean Distance ($\sqrt{\Delta x^2 + \Delta y^2}$):** Moves are restricted to grid cardinal directions (horizontal/vertical), requiring the Manhattan metric $|\Delta x| + |\Delta y|$, not Euclidean.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass over the $G$ ghosts, evaluating arithmetic Manhattan distance for each: $\mathcal{O}(G)$.
  - Total Time: strictly linear in ghost count $\mathcal{O}(G)$ where $G \le 100$. Completes in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
