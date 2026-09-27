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

---

## 5. Algorithmic Correctness

**Soundness.** Let the knight be at room $(r, c)$. To reach the princess alive via room $(r', c')$, the knight must enter $(r', c')$ with at least $DP[r', c']$ health. After interacting with room $(r, c)$, the knight's health is $\text{HP} + \text{dungeon}[r][c]$. Thus, $\text{HP} + \text{dungeon}[r][c] \ge DP[r', c']$, meaning $\text{HP} \ge DP[r', c'] - \text{dungeon}[r][c]$. Clamping with $\max(1, \dots)$ ensures the knight is alive upon entering $(r, c)$.

**Completeness.** Since the recurrence considers both valid moves (Right and Down) and takes the minimum, no viable escape path with lower initial health can exist.

---

## 6. Traps This Instance Exposes

- **Trying Forward DP:** In forward DP, high HP gains later cannot compensate for dying earlier. Trying to track both `min_hp_needed` and `current_hp` forward requires an intractable multi-objective state space. Backward DP completely resolves this.
- **Forgetting $\max(1, \dots)$ Clamping:** If a room gives massive healing (e.g. $+30$), $\text{needed} - \text{val} = 6 - 30 = -24$. Entering with $-24$ HP means the knight is dead! Health cannot drop to $\le 0$, so entry health must always be at least $1$.
- **Sentinel Padding:** Initializing a DP table of size $(M+1) \times (N+1)$ with $\infty$, and setting $DP[M][N-1] = DP[M-1][N] = 1$, allows unified processing of edges without boundary if-statements.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M$ is the number of rows and $N$ is the number of columns in `dungeon`. Each cell is computed in $O(1)$ arithmetic operations.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory when optimizing 2D DP to a single rolling row, or $O(M \cdot N)$ for the full matrix.