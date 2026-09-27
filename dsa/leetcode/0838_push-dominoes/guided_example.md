# Guided Example: Push Dominoes

We trace the step-by-step multi-source breadth-first search wavefront propagation, simultaneous physical force balance resolution, discrete arrival timestamp synchronization ($time[j] == t + 1$), opposing force cancellation ($|force[i]| > 1 \implies \text{upright '.'}$), and final steady-state equilibrium string assembly on representative domino chains:

- **Input:**
  $$
  dominoes = \text{"RR.L"}
  $$
- **Required output:**
  $$
  \text{"RR.L"}
  $$
  - Domino dynamics and physical laws:
    - We have $n$ dominoes positioned along a 1D line at integer indices $0 \dots n - 1$.
    - At timestep $t = 0$, some dominoes are pushed left (`'L'`) or right (`'R'`), while others start standing vertically (`'.'`).
    - **Wave Propagation Rule:**
      - A domino falling right pushes its immediate right neighbor ($i + 1$) after 1 second.
      - A domino falling left pushes its immediate left neighbor ($i - 1$) after 1 second.
    - **Balanced Equilibrium Rule:**
      - If a standing domino is pushed from both the left (by an `'R'` wave) and the right (by an `'L'` wave) at the **exact same timestep**, the opposing forces cancel out perfectly.
      - The domino remains upright (`'.'`) and propagates no further force in either direction.
    - For $dominoes = \text{"RR.L"}$ ($n = 4$):
      - Domino 0: pushed right (`'R'`).
      - Domino 1: pushed right (`'R'`).
      - Domino 3: pushed left (`'L'`).
      - Domino 2: starts upright (`'.'`).
      - At $t = 1$:
        - Domino 1 pushes Domino 2 to the right (`'R'`).
        - Domino 3 pushes Domino 2 to the left (`'L'`).
        - Domino 2 experiences simultaneous opposing forces: $\{ \text{'R'}, \text{'L'} \}$.
        - Forces balance! Domino 2 remains upright: `'.'`.
      - Final stable configuration: `"RR.L"`.
- **Multi-Source BFS & Collision Resolution Invariant:**
  - **The Wavefront Timestamp Grid:**
    - Maintain two tracking structures across the 1D lattice:
      1. $time[i] \in \{-1, 0, 1, \dots\}$: The earliest second at which a falling wavefront reaches domino $i$.
      2. $force[i] \subseteq \{\text{'L'}, \text{'R'}\}$: The list of directional forces acting on domino $i$ at its arrival time.
  - **Queue Initialization ($t = 0$):**
    - For each initial non-empty domino $i$ ($dominoes[i] \ne \text{'.'}$):
      - Enqueue $i$.
      - Set $time[i] = 0$.
      - Record initial force: $force[i] = [dominoes[i]]$.
  - **State Transition & Neighbor Propagation:**
    - Dequeue domino $i$:
      - **Equilibrium Check:**
        - If $|force[i]| > 1$ (both `'L'` and `'R'` reached simultaneously):
          - Domino remains standing: $ans[i] \leftarrow \text{'.'}$.
          - It exerts **zero force** on adjacent dominoes (propagation halts at $i$).
        - If $|force[i]| == 1$ (unbalanced single force $f$):
          - Domino falls: $ans[i] \leftarrow f$.
          - Determine adjacent target index:
            $$
            j = \begin{cases} i - 1 & f = \text{'L'} \\ i + 1 & f = \text{'R'} \end{cases}
            $$
          - If $j$ is in bounds ($0 \le j < n$):
            - **First arrival at $j$ ($time[j] == -1$):**
              - Enqueue $j$.
              - Set $time[j] \leftarrow time[i] + 1$.
              - Add force: $force[j].\text{append}(f)$.
            - **Simultaneous arrival at $j$ ($time[j] == time[i] + 1$):**
              - Add opposing force: $force[j].\text{append}(f)$.
              - The opposing force will balance out when $j$ is popped!
- **Step-by-Step Worked Execution Trace on $dominoes = \text{"RR.L"}$ ($n = 4$):**
  - Initialize:
    - $time = [-1, -1, -1, -1]$
    - $force = \{\}$
    - $ans = [\text{'.'}, \text{'.'}, \text{'.'}, \text{'.'}]]$
    - Queue $q = [0, 1, 3]$
    - At $t = 0$:
      - Domino 0: $time[0] = 0, force[0] = [\text{'R'}]$
      - Domino 1: $time[1] = 0, force[1] = [\text{'R'}]$
      - Domino 3: $time[3] = 0, force[3] = [\text{'L'}]$
  - **Timestep 0 Processing:**
    - **Pop Domino 0:**
      - $|force[0]| = 1 \implies ans[0] = \mathbf{\text{'R'}}.$
      - Target neighbor $j = 0 + 1 = 1$.
      - $time[1] = 0 \ne 0 + 1 \implies$ Domino 1 is already active at $t = 0$! No force applied.
    - **Pop Domino 1:**
      - $|force[1]| = 1 \implies ans[1] = \mathbf{\text{'R'}}.$
      - Target neighbor $j = 1 + 1 = 2$.
      - $time[2] == -1 \implies \mathbf{First\ Arrival\ at\ Domino\ 2!}$
      - Enqueue 2: $q.\text{append}(2)$.
      - $time[2] \leftarrow 0 + 1 = \mathbf{1}$.
      - $force[2] \leftarrow [\text{'R'}]$.
    - **Pop Domino 3:**
      - $|force[3]| = 1 \implies ans[3] = \mathbf{\text{'L'}}.$
      - Target neighbor $j = 3 - 1 = 2$.
      - Inspect neighbor 2: $time[2] == 1 == 0 + 1 \implies \mathbf{Simultaneous\ Collision!}$
      - $force[2].\text{append}(\text{'L'})$.
      - Domino 2 now has forces:
        $$
        force[2] = [\text{'R'}, \; \text{'L'}]
        $$
  - **Timestep 1 Processing:**
    - **Pop Domino 2:**
      - Inspect forces: $force[2] = [\text{'R'}, \text{'L'}]$.
      - Count forces: $|force[2]| = 2 > 1 \implies \mathbf{Balanced\ Forces!}$
      - Forces cancel out: Domino 2 remains standing:
        $$
        ans[2] = \mathbf{\text{'.'}}
        $$
      - No further propagation occurs from Domino 2!
    - Queue $q$ is now empty.
  - **Assembled Steady-State String:**
    $$
    ans = \mathbf{\text{"RR.L"}}
    $$
- **Step-by-Step Worked Execution Trace on Mixed Domino Chain ($dominoes = \text{".L.R...LR..L.."}$):**
  - Dominoes at indices 1 ('L'), 3 ('R'), 7 ('L'), 8 ('R'), 11 ('L') pushed initially.
  - Index 0: pushed left by index 1 at $t = 1 \implies \text{'L'}$.
  - Gap between 3 ('R') and 7 ('L'):
    - Indices $4, 5, 6$.
    - $t = 1$: index 4 gets 'R', index 6 gets 'L'.
    - $t = 2$: both reach index 5 simultaneously $\implies$ index 5 gets both 'R' and 'L' $\implies$ stays `'.'`.
    - Segment becomes `"RR.LL"`.
  - Gap between 8 ('R') and 11 ('L'):
    - Indices $9, 10$ (even length 2).
    - $t = 1$: index 9 gets 'R', index 10 gets 'L'.
    - Both fall without collision $\implies \text{"RRLL"}$.
  - Tail indices $12, 13$: never reached $\implies \text{".."}$.
  - Final string: `"LL.RR.LLRRLL.."`.

This instance demonstrates discrete wavefront propagation in cellular automata and kinematic shock-wave neutralization, mathematically proves why level-synchronized multi-source BFS captures exact simultaneous contact dynamics without floating-point simulation, and derives $O(N)$ runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a string of dominoes:
`'L'` pushes left, `'R'` pushes right, `'.'` stands upright.
Opposing forces arriving at the exact same time **cancel out**, leaving the domino upright (`'.'`).
Find the final state.

```text
dominoes = "RR.L"

At t = 0: 0('R'), 1('R'), 3('L')
At t = 1:
  Domino 1 pushes Domino 2 right ('R').
  Domino 3 pushes Domino 2 left ('L').
  Domino 2 receives BOTH 'R' and 'L' simultaneously!
  Forces balance -> Domino 2 stays '.'

Result: "RR.L"
```

### The Invariant of Simultaneous Wavefront Arrival
- Multi-source BFS with arrival timestamps.
- If only one force arrives at domino $i$, it falls in that direction and pushes its neighbor at $t + 1$.
- If both `'R'` and `'L'` arrive at the exact same second, forces cancel: the domino stays upright `'.'` and halts propagation.

---

## 2. Conceptual Foundation & Invariants

### 1. Wavefront Kinematics:
$$
\text{pos}(R, t) = x_0 + t, \quad \text{pos}(L, t) = x_0 - t
$$

### 2. Force Superposition Principle:
$$
ans[i] = \begin{cases}
f & force[i] = [f] \\
\text{'.'} & |force[i]| \ne 1
\end{cases}
$$

> **Cellular Automaton Shock Invariant.** In a 1D discrete excitable medium with constant wave speed $c = 1$, head-on collisions of opposing fronts annihilate or create stationary solitary neutral boundaries depending on the parity of the spatial separation: odd separations leave a single invariant neutral node, while even separations form a sharp shock interface.

---

## 3. Step-by-Step Worked Execution

We trace $dominoes = \text{"RR.L"}$:

---

### Step 1: Queue Initial State
- $q = [0, 1, 3]$ at $t = 0$.
- $force[0] = [\text{'R'}], force[1] = [\text{'R'}], force[3] = [\text{'L'}]$.

---

### Step 2: Process $t = 0$
- Domino 1 pushes right $\to$ reaches 2 at $t = 1$ with `'R'`.
- Domino 3 pushes left $\to$ reaches 2 at $t = 1$ with `'L'`.
- $force[2] = [\text{'R'}, \text{'L'}]$.

---

### Step 3: Process $t = 1$ (Domino 2)
- $|force[2]| = 2 > 1 \implies$ balance!
- $ans[2] = \mathbf{\text{'.'}}$.
- No further push.

---

### Step 4: Output
$$
\mathbf{\text{"RR.L"}}
$$

---

## 4. Complete Execution Trace

| Queue Step | Domino $i$ | Forces Received | $\lvert force[i] \rvert$ | Final State $ans[i]$ | Propagation Action |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $t = 0$ | $0$ | $[\text{'R'}]$ | $1$ | `'R'` | None (1 occupied) |
| $t = 0$ | $1$ | $[\text{'R'}]$ | $1$ | `'R'` | Pushes 2 at $t = 1$ with `'R'` |
| $t = 0$ | $3$ | $[\text{'L'}]$ | $1$ | `'L'` | Pushes 2 at $t = 1$ with `'L'` |
| **$t = 1$** | **$2$** | **$[\text{'R'}, \text{'L'}]$** | **$2$** | **`'.'` (Balanced)** | **None (Halts)** |
| **Final** | — | — | — | — | **`"RR.L"`** |

---

## 5. Boundary Cases & Failure Modes

- **All Standing ($dominoes = \text{"...."}$):** Queue is empty initially $\implies$ all remain `'.'`.
- **Opposing Forces with Even Gap ($"R..L"$):** $t = 1$ reaches indices $1$ ('R') and $2$ ('L'). At $t = 2$, each attempts to push the other, but both are already visited at $t = 1 \implies \text{"RRLL"}$.
- **Opposing Forces with Odd Gap ($"R...L"$):** $t = 1$ sets $1$ ('R') and $3$ ('L'). At $t = 2$, both hit index $2$ simultaneously $\implies \text{"RR.LL"}$.
- **Unidirectional Cascade ($"R....."$):** Dominoes fall sequentially to the right end $\implies \text{"RRRRRR"}$.

---

## 6. Traps & Common Anti-Patterns

- **Step-by-Step Full String Mutation ($O(N^2)$):** Simulating second-by-second by rescanning the entire string takes quadratic time. Multi-source BFS visits each domino at most twice, achieving strictly $O(N)$ runtime.
- **Overwriting a Balanced Force:** If domino $j$ receives `'R'` and then `'L'` in the same timestep, do not overwrite `'R'`; collect both in a list and resolve after the timestep completes.
- **Propagating from a Balanced Domino:** A balanced domino does NOT push its neighbors; only unbalanced dominoes with $|force| == 1$ continue propagation.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Each domino is enqueued at most once when first reached.
  - At each step, a constant number of neighbors ($\le 2$) are evaluated.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 10^5$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for the BFS queue, `time` array, and `force` dictionary.
