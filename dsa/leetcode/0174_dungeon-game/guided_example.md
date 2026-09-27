# Guided Example: Dungeon Game

We trace the step-by-step backward dynamic programming recurrence from the princess room to the entrance on representative 2D grid instances:

- **Input:** $\text{dungeon} = \begin{bmatrix} -2 & -3 & 3 \\ -5 & -10 & 1 \\ 10 & 30 & -5 \end{bmatrix}$
- **Required output:** $7$ (Knight follows path $(0,0) \to (0,1) \to (0,2) \to (1,2) \to (2,2)$ starting with $7$ HP)
- **Single Room Negative Instance:** $\text{dungeon} = [[-10]] \implies 11$
- **Single Room Magic Orb Instance:** $\text{dungeon} = [[10]] \implies 1$ (Knight must start with at least $1$ HP)

This instance demonstrates why forward dynamic programming fails due to dual-objective coupling (minimum cumulative dip vs remaining health), proves why backward dynamic programming ($DP[r][c] = \max(1, \min(\text{next}) - \text{dungeon}[r][c])$) provides perfect optimal substructure, and operates in $O(M \cdot N)$ time and $O(N)$ space.

---

## 1. Instance & Teaching Goal

Given a $3 \times 3$ grid where negative numbers represent demon damage and positive numbers represent magic healing orbs:
$$
\text{dungeon} =
\begin{pmatrix}
-2 & -3 & 3 \\
-5 & -10 & 1 \\
10 & 30 & -5
\end{pmatrix}
$$
The knight starts at $(0, 0)$ and must reach the princess at $(2, 2)$, moving only **Right** or **Down**.
The knight dies immediately if health reaches $\le 0$ at any point.
Find the **minimum initial health** required at $(0, 0)$ to survive to the princess.

### Why Forward DP Fails
In forward DP from $(0, 0)$, a path with a low damage dip early might leave the knight with low current HP, while a path with higher early damage might leave the knight with high HP from a large magic orb.
Because future survival depends on *both* the historical minimum dip and current health, subproblems do not exhibit the principle of optimality in the forward direction.

### Why Backward DP Succeeds
Let $DP[r][c]$ be the **minimum health the knight MUST HAVE upon entering room $(r, c)$** to successfully complete the remaining journey to the princess.
- At any cell, the knight only needs to know the minimum HP required upon entering the adjacent next cells (Right $(r, c+1)$ or Down $(r+1, c)$).
- Moving to the cell requiring smaller entry health ($\min(DP[\text{Right}], DP[\text{Down}])$) is **always globally optimal**.
- Therefore, backward DP from $(m-1, n-1)$ back to $(0, 0)$ has strict optimal substructure!

---

## 2. Conceptual Foundation & Invariants

### Backward Recurrence Formulation
Let $M$ be rows, $N$ be columns.
At any room $(r, c)$:
Let $\text{needed\_next}$ be the minimum health required upon leaving room $(r, c)$ to enter the chosen next room:
$$
\text{needed\_next} =
\begin{cases}
1 & \text{if } (r, c) = (M-1, N-1) \quad (\text{princess room}) \\
DP[r][c+1] & \text{if } r = M-1 \quad (\text{bottom edge, must go Right}) \\
DP[r+1][c] & \text{if } c = N-1 \quad (\text{right edge, must go Down}) \\
\min(DP[r][c+1], \, DP[r+1][c]) & \text{otherwise}
\end{cases}
$$

The health upon entering room $(r, c)$ satisfies:
$$
\text{enter\_hp} + \text{dungeon}[r][c] \ge \text{needed\_next} \implies \text{enter\_hp} \ge \text{needed\_next} - \text{dungeon}[r][c]
$$
Because the knight must enter the room alive ($\text{enter\_hp} \ge 1$):
$$
DP[r][c] = \max(1, \, \text{needed\_next} - \text{dungeon}[r][c])
$$

> **Invariant.** $DP[r][c]$ is the strictly minimal positive integer health required when stepping into room $(r, c)$ such that there exists a valid sequence of Right/Down moves to $(M-1, N-1)$ where health remains $\ge 1$ at every step.

---

## 3. Step-by-Step Worked Execution

We compute the $3 \times 3$ DP table backwards from $(2, 2)$ to $(0, 0)$:

### Row 2 (Bottom Row, $r = 2$):
- **Cell $(2, 2)$ (Princess):**
  $\text{needed\_next} = 1$. Room value $= -5$.
  $$
  DP[2][2] = \max(1, \, 1 - (-5)) = \mathbf{6}
  $$
- **Cell $(2, 1)$:**
  Can only go Right to $(2, 2)$ where needed $= 6$. Room value $= 30$.
  $$
  DP[2][1] = \max(1, \, 6 - 30) = \max(1, -24) = \mathbf{1}
  $$
  *(Healing 30 HP means 1 HP is enough to leave with $\ge 6$ HP)*.
- **Cell $(2, 0)$:**
  Can only go Right to $(2, 1)$ where needed $= 1$. Room value $= 10$.
  $$
  DP[2][0] = \max(1, \, 1 - 10) = \mathbf{1}
  $$

---

### Row 1 (Middle Row, $r = 1$):
- **Cell $(1, 2)$ (Right Edge):**
  Can only go Down to $(2, 2)$ where needed $= 6$. Room value $= 1$.
  $$
  DP[1][2] = \max(1, \, 6 - 1) = \mathbf{5}
  $$
- **Cell $(1, 1)$:**
  Choices: Right to $(1, 2)$ (needs 5) or Down to $(2, 1)$ (needs 1).
  $\text{needed\_next} = \min(5, 1) = 1$. Room value $= -10$.
  $$
  DP[1][1] = \max(1, \, 1 - (-10)) = \mathbf{11}
  $$
- **Cell $(1, 0)$:**
  Choices: Right to $(1, 1)$ (needs 11) or Down to $(2, 0)$ (needs 1).
  $\text{needed\_next} = \min(11, 1) = 1$. Room value $= -5$.
  $$
  DP[1][0] = \max(1, \, 1 - (-5)) = \mathbf{6}
  $$

---

### Row 0 (Top Row, $r = 0$):
- **Cell $(0, 2)$ (Right Edge):**
  Can only go Down to $(1, 2)$ where needed $= 5$. Room value $= 3$.
  $$
  DP[0][2] = \max(1, \, 5 - 3) = \mathbf{2}
  $$
- **Cell $(0, 1)$:**
  Choices: Right to $(0, 2)$ (needs 2) or Down to $(1, 1)$ (needs 11).
  $\text{needed\_next} = \min(2, 11) = 2$. Room value $= -3$.
  $$
  DP[0][1] = \max(1, \, 2 - (-3)) = \mathbf{5}
  $$
- **Cell $(0, 0)$ (Entrance):**
  Choices: Right to $(0, 1)$ (needs 5) or Down to $(1, 0)$ (needs 6).
  $\text{needed\_next} = \min(5, 6) = 5$. Room value $= -2$.
  $$
  DP[0][0] = \max(1, \, 5 - (-2)) = \mathbf{7}
  $$

Required initial health at $(0, 0)$ is $\mathbf{7}$.

---

## 4. Complete Execution Trace

```text
Dungeon Grid:             DP Table (Minimum Entry HP Required):
[ -2,  -3,   3 ]          [ 7,   5,   2 ]
[ -5, -10,   1 ]   ==>    [ 6,  11,   5 ]
[ 10,  30,  -5 ]          [ 1,   1,   6 ]

Optimal Path: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)
Health Simulation (Start HP = 7):
  Enter (0,0): 7 - 2 = 5 HP
  Enter (0,1): 5 - 3 = 2 HP
  Enter (0,2): 2 + 3 = 5 HP
  Enter (1,2): 5 + 1 = 6 HP
  Enter (2,2): 6 - 5 = 1 HP -> Princess rescued!
```

| Cell $(r, c)$ | Room Value | Options (Right, Down) | $\text{needed\_next} = \min(R, D)$ | Formula $\max(1, \text{needed} - \text{val})$ | Computed $DP[r][c]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $(2, 2)$ | -5 | Princess Exit | 1 | $\max(1, 1 - (-5))$ | 6 |
| $(2, 1)$ | 30 | Right $(2, 2): 6$ | 6 | $\max(1, 6 - 30)$ | 1 |
| $(2, 0)$ | 10 | Right $(2, 1): 1$ | 1 | $\max(1, 1 - 10)$ | 1 |
| $(1, 2)$ | 1 | Down $(2, 2): 6$ | 6 | $\max(1, 6 - 1)$ | 5 |
| $(1, 1)$ | -10 | Right: 5, Down: 1 | 1 | $\max(1, 1 - (-10))$ | 11 |
| $(1, 0)$ | -5 | Right: 11, Down: 1 | 1 | $\max(1, 1 - (-5))$ | 6 |
| $(0, 2)$ | 3 | Down $(1, 2): 5$ | 5 | $\max(1, 5 - 3)$ | 2 |
| $(0, 1)$ | -3 | Right: 2, Down: 11 | 2 | $\max(1, 2 - (-3))$ | 5 |
| **$(0, 0)$** | **-2** | **Right: 5, Down: 6** | **5** | **$\max(1, 5 - (-2))$** | **7 (Result)** |

### Why Each Branch Was Accepted or Rejected

The table above records the winning branch's values. Reading it as an elimination argument shows that the answer $7$ is the result of two local rejections, not of an exhaustive path search:

| Decision point | Room value | Right branch demands | Down branch demands | Chosen | Why the rejected branch is strictly worse |
|:---:|:---:|:---:|:---:|:---|:---|
| $(0, 0)$ | -2 | $DP[0][1] = 5$ | $DP[1][0] = 6$ | Right | the Down route must absorb $5$ damage before reaching room $(1, 0)$, so it needs $6 + 2 = 8$ health at the entrance, more than the $7$ the winning route needs |
| $(0, 1)$ | -3 | $DP[0][2] = 2$ | $DP[1][1] = 11$ | Right | the Down branch hands the knight to the $-10$ room, whose entry requirement of $11$ is nine points above the Right branch |
| $(0, 2)$ | 3 | no Right move exists | $DP[1][2] = 5$ | Down, forced | the last column admits only Down, so no comparison is available or needed |
| $(1, 2)$ | 1 | no Right move exists | $DP[2][2] = 6$ | Down, forced | the same edge rule applies one row lower |
| $(2, 2)$ | -5 | princess room | princess room | stop | the recurrence seeds this cell with $\text{needed\_next} = 1$ and computes $\max(1, 1 - (-5)) = 6$ |

At $(0, 1)$ the knight rejects a branch that is *cheaper in the immediate sense* only after the comparison: the $-10$ room looks attractive because the Down move itself costs nothing, yet entering it alive demands $11$ health, which is the largest requirement anywhere in the grid. Backward DP converts that currently invisible future cost into a single number before the decision is made.

### Health Along the Winning Route

The DP table stores requirements, not the health the knight actually carries. Turning the requirements into an executed route is the real check that $7$ is feasible:

| Step | Room entered | Room value | Health on entry | Health after resolving the room | $DP$ value demanded here | What it means |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | $(0, 0)$ | -2 | 7 | 5 | 7 | the start is exactly the computed requirement, so no slack is spent or saved |
| 2 | $(0, 1)$ | -3 | 5 | 2 | 5 | this is the lowest health on the whole route: two points above death |
| 3 | $(0, 2)$ | 3 | 2 | 5 | 2 | the orb repairs three points before the knight turns downward |
| 4 | $(1, 2)$ | 1 | 5 | 6 | 5 | a further net gain keeps the knight away from the floor |
| 5 | $(2, 2)$ | -5 | 6 | 1 | 6 | the final demon leaves exactly one health: alive, never at or below zero |

Starting with $6$ instead is fatal on the same route: the health sequence becomes $4, 1, 4, 5, 0$, and the princess's room itself kills the knight at the last step. That is why the initial answer must be $7$ and not the value that merely reaches the princess's doorstep.

---

## 5. Algorithmic Correctness

**Soundness.** Let the knight be at room $(r, c)$. To reach the princess alive via room $(r', c')$, the knight must enter $(r', c')$ with at least $DP[r', c']$ health. After interacting with room $(r, c)$, the knight's health is $\text{HP} + \text{dungeon}[r][c]$. Thus, $\text{HP} + \text{dungeon}[r][c] \ge DP[r', c']$, meaning $\text{HP} \ge DP[r', c'] - \text{dungeon}[r][c]$. Clamping with $\max(1, \dots)$ ensures the knight is alive upon entering $(r, c)$.

**Completeness.** Since the recurrence considers both valid moves (Right and Down) and takes the minimum, no viable escape path with lower initial health can exist.

---

## 6. Traps This Instance Exposes

- **Trying Forward DP:** In forward DP, high HP gains later cannot compensate for dying earlier. Trying to track both `min_hp_needed` and `current_hp` forward requires an intractable multi-objective state space. Backward DP completely resolves this.
- **Forgetting $\max(1, \dots)$ Clamping:** If a room gives massive healing (e.g. $+30$), $\text{needed} - \text{val} = 6 - 30 = -24$. Entering with $-24$ HP means the knight is dead! Health cannot drop to $\le 0$, so entry health must always be at least $1$.
- **Sentinel Padding:** Initializing a DP table of size $(M+1) \times (N+1)$ with $\infty$, and setting $DP[M][N-1] = DP[M-1][N] = 1$, allows unified processing of edges without boundary if-statements.

### Boundary Grids the Same Recurrence Must Handle

The traced grid is generous: it contains a $+30$ orb and a route that avoids the deepest damage. The recurrence earns its keep on the degenerate grids, where the clamp and the edge rules decide everything:

| Grid | Shape | Required initial health | What the recurrence is actually doing |
|:---|:---|:---:|:---|
| `[[0]]` | one neutral room | 1 | $\text{needed\_next} = 1$ and the room changes nothing, so $\max(1, 1 - 0) = 1$ |
| `[[-3]]` | one damaging room | 4 | the knight absorbs three damage and must still be alive, so $\max(1, 1 - (-3)) = 4$ |
| `[[100]]` | one healing room | 1 | $1 - 100$ is negative and the clamp lifts it back to the floor of 1, since the knight cannot start below one health |
| `[[-10]]` | one severely damaging room | 11 | the ten points of damage plus the single point that must remain on arrival |
| `[[-1,-1],[-1,-1]]` | every route accumulates damage | 4 | both routes cross three damaging rooms, so the branch minimum is the same on either side and the answer is the sum of the damage plus 1 |
| `[[-3,-3,-3]]` | single row, no healing | 10 | with one forced chain of three rooms the recurrence degenerates to $1 + 3 + 3 + 3$; a single column behaves identically |

The last two rows are the ones that catch a careless implementation: with no healing anywhere, the clamp at 1 only matters at the princess's room, and every earlier cell's value is a running sum of future damage plus one. A solution that clamps too aggressively, or that treats the princess's room as free, understates these answers.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M$ is the number of rows and $N$ is the number of columns in `dungeon`. Each cell is computed in $O(1)$ arithmetic operations.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory when optimizing 2D DP to a single rolling row, or $O(M \cdot N)$ for the full matrix.