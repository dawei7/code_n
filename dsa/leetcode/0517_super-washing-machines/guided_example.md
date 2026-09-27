# Guided Example: Super Washing Machines

We trace the step-by-step total dress conservation and divisibility check ($S \pmod n == 0$), target equilibrium calculation ($k = S / n$), signed net surplus deviation ($x_i = machines[i] - k$), prefix flow cut aggregation ($s_i = \sum x$), single-machine simultaneous output rate bottleneck ($x_i$), and maximum boundary load derivation on representative washing machine arrays:

- **Input:** $machines = [1, 0, 5]$
- **Required output:** `3`
  - Array length: $n = 3$ machines in a line.
  - Initial load: Machine 0 has $1$ dress, Machine 1 has $0$ dresses, Machine 2 has $5$ dresses.
  - Operation rules: In each move, any machine can pass at most one dress to an adjacent neighbor (left or right). Multiple machines can move dresses simultaneously.
- **Equilibrium & Flow Analysis:**
  - Total dresses:
    $$
    S = 1 + 0 + 5 = \mathbf{6}
    $$
  - Target per machine:
    $$
    k = \frac{S}{n} = \frac{6}{3} = \mathbf{2}
    $$
    $6 \pmod 3 = 0 \implies$ Feasible! Every machine must finish with exactly $2$ dresses.
- **Prefix Flow & Machine Bottleneck Trace:**
  - Track running prefix net flow $s$ and answer $ans$:
  - **Machine 0 (Has 1, Needs 2):**
    - Deviation: $x_0 = 1 - 2 = \mathbf{-1}$ (Deficit of 1 dress)
    - Cumulative flow crossing boundary $0 \mid 1$:
      $$
      s_0 = -1
      $$
      Machine 0 must receive a net total of $1$ dress from its right neighbor.
    - Moves required at this boundary: $|s_0| = |-1| = 1$.
    - Bottleneck: $ans = \max(ans, \; |s_0|, \; x_0) = \max(0, 1, -1) = \mathbf{1}$.
  - **Machine 1 (Has 0, Needs 2):**
    - Deviation: $x_1 = 0 - 2 = \mathbf{-2}$ (Deficit of 2 dresses)
    - Cumulative flow crossing boundary $1 \mid 2$:
      $$
      s_1 = s_0 + x_1 = -1 + (-2) = \mathbf{-3}
      $$
      Machines $\{0, 1\}$ together have a net deficit of $3$ dresses. Exactly $3$ dresses must cross the boundary between Machine 1 and Machine 2!
    - Moves required across cut $1 \mid 2$: $|s_1| = |-3| = \mathbf{3}$.
    - Bottleneck: $ans = \max(1, \; |s_1|, \; x_1) = \max(1, 3, -2) = \mathbf{3}$.
  - **Machine 2 (Has 5, Needs 2):**
    - Deviation: $x_2 = 5 - 2 = \mathbf{+3}$ (Surplus of 3 dresses)
    - Cumulative flow at end of line:
      $$
      s_2 = s_1 + x_2 = -3 + 3 = \mathbf{0}
      $$
    - Outgoing transfer constraint: Machine 2 must send out $3$ surplus dresses. Since a machine can only send out at most $1$ dress per move, sending $3$ dresses requires at least $x_2 = \mathbf{3}$ moves!
    - Bottleneck: $ans = \max(3, \; |s_2|, \; x_2) = \max(3, 0, 3) = \mathbf{3}$.
  - Global minimum moves: **`3`**.
- **Move-by-Move Physical Simulation ($[1, 0, 5]$):**
  - Initial: $[1, 0, 5]$
  - Move 1: Machine 2 passes 1 dress left $\implies [1, 1, 4]$
  - Move 2: Machine 1 passes 1 dress left, Machine 2 passes 1 dress left $\implies [2, 1, 3]$
  - Move 3: Machine 2 passes 1 dress left $\implies [2, 2, 2]$ (Balanced in 3 moves!).
- **Dual Outgoing Bottleneck Instance ($machines = [0, 3, 0]$):**
  - Target $k = 1$. Center machine has surplus $x_1 = 3 - 1 = 2$.
  - Center machine must send 1 dress left AND 1 dress right.
  - Because it can only send ONE dress per round (cannot send left and right in the same move), it takes $x_1 = \mathbf{2}$ moves.
- **Indivisible Dresses Instance ($machines = [0, 2]$):**
  - Total $2$, $n = 2$, but if $machines = [1, 2]$, sum $3 \pmod 2 = 1 \ne 0 \implies \mathbf{-1}$.

This instance demonstrates cut-capacity flow duality in 1D transport networks, mathematically proves why $\max(|s_i|, x_i)$ characterizes the exact minimax scheduling lower bound, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $machines$ where $machines[i]$ is the number of dresses in the $i$-th machine:
In each move, you can pick any subset of machines, and each chosen machine can pass **at most one dress** to an adjacent neighbor.
Find the **minimum number of moves** to make all washing machines contain an equal number of dresses.
If it is impossible, return `-1`.

```text
Machines: [ 1,  0,  5 ]
Total = 6, n = 3 -> Target per machine = 6 / 3 = 2

Net Balance Needed:
  M0: 1 - 2 = -1 (Needs 1 dress)
  M1: 0 - 2 = -2 (Needs 2 dresses)
  M2: 5 - 2 = +3 (Must export 3 dresses)

Net Cut Crossing:
  Between M1 and M2:
    Left side {M0, M1} needs total (-1) + (-2) = -3 dresses.
    All 3 dresses must cross the M1-M2 boundary!
    Since at most 1 dress crosses per move -> Minimum 3 moves required.

Result: 3 moves
```

### The Two Physical Bottlenecks
Why does $\max(|s_i|, x_i)$ give the exact minimum number of moves?
1. **The Boundary Cut Capacity ($|s_i|$):**
   Consider the cut separating machines $0 \dots i$ from machines $i+1 \dots n-1$.
   The net number of dresses that must pass across this cut is $s_i = \sum_{j=0}^i (machines[j] - k)$.
   Because at most ONE dress can cross this boundary in any single move, at least $|s_i|$ moves are strictly required.
2. **The Machine Output Rate ($x_i$):**
   A machine with a large surplus $x_i = machines[i] - k > 0$ needs to offload $x_i$ dresses.
   Even if it needs to send dresses in opposite directions (some to the left, some to the right), **a machine can only send at most one dress per turn**.
   Therefore, an individual machine requires at least $x_i$ moves to offload its surplus.
Because both bottlenecks are independent physical limits, the answer is the supremum: $\max(|s_i|, x_i)$.

---

## 2. Conceptual Foundation & Invariants

### 1. Conservation and Feasibility:
Let $S = \sum_{i=0}^{n-1} machines[i]$:
- If $S \pmod n \ne 0$:
  Dresses cannot be divided evenly among integer machines $\implies$ Return $-1$.
- Target equilibrium level:
  $$
  k = \frac{S}{n}
  $$

### 2. Single-Pass Bottleneck Accumulation:
Iterate $x \in machines$:
1. Local net balance:
   $$
   x \leftarrow x - k
   $$
2. Cumulative flow across boundary:
   $$
   s \leftarrow s + x
   $$
3. Update peak bottleneck:
   $$
   ans \leftarrow \max(ans, \; |s|, \; x)
   $$
Note that only positive $x$ (surplus) limits the single-machine output; negative $x$ (deficit) does not restrict reception because a machine can receive dresses from both sides simultaneously.

> **Minimax Flow Invariant.** Any schedule requires at least $\max(|s_i|)$ moves to transport dresses across every spatial cut and at least $\max(x_i)$ moves to drain the most overloaded machine.

---

## 3. Step-by-Step Worked Execution

We trace $machines = [1, 0, 5]$ ($n = 3, S = 6, k = 2$):

---

### Step 1: Initialize
- $ans = 0, \; s = 0$.

---

### Step 2: Traverse Machines

1. **Machine 0 ($machines[0] = 1$):**
   - Deviation: $x = 1 - 2 = -1$.
   - Prefix sum: $s \leftarrow 0 + (-1) = -1$.
   - Boundary load: $|s| = 1$.
   - Output rate: $x = -1$.
   - $ans = \max(0, 1, -1) = \mathbf{1}$.

2. **Machine 1 ($machines[1] = 0$):**
   - Deviation: $x = 0 - 2 = -2$.
   - Prefix sum: $s \leftarrow -1 + (-2) = -3$.
   - Boundary load: $|s| = 3$.
   - Output rate: $x = -2$.
   - $ans = \max(1, 3, -2) = \mathbf{3}$.

3. **Machine 2 ($machines[2] = 5$):**
   - Deviation: $x = 5 - 2 = 3$.
   - Prefix sum: $s \leftarrow -3 + 3 = 0$.
   - Boundary load: $|s| = 0$.
   - Output rate: $x = 3$.
   - $ans = \max(3, 0, 3) = \mathbf{3}$.

---

### Step 3: Final Output
$$
ans = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Machine Index $i$ | Initial Dresses | Net Surplus $x = val - k$ | Prefix Flow $s$ | Boundary Cut $\lvert s \rvert$ | Output Bottleneck $x$ | Running Max $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | $1$ | $-1$ | $-1$ | $1$ | $-1$ | $1$ |
| **$1$** | $0$ | $-2$ | $-3$ | **$3$** | $-2$ | **$3$** |
| **$2$** | $5$ | $+3$ | $0$ | $0$ | **$3$** | **$3$** |
| **Result** | — | — | — | — | — | **$3$** |

### Trace on Center Surplus Input $[0, 3, 0]$ ($k = 1$):
| Machine Index $i$ | Initial Dresses | Net Surplus $x$ | Prefix Flow $s$ | Boundary Cut $\lvert s \rvert$ | Output Bottleneck $x$ | Running Max $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$** | $0$ | $-1$ | $-1$ | $1$ | $-1$ | $1$ |
| **$1$** | $3$ | $+2$ | $+1$ | $1$ | **$2$** | **$2$** |
| **$2$** | $0$ | $-1$ | $0$ | $0$ | $-1$ | **$2$** |

---

## 5. Boundary Cases & Failure Modes

- **Infeasible Divisibility ($\sum machines \pmod n \ne 0$):** Immediately returns $\mathbf{-1}$.
- **Already Balanced ($[2, 2, 2]$):** All deviations $x = 0 \implies ans = \mathbf{0}$.
- **Single Machine ($[10]$):** Always balanced $\implies ans = \mathbf{0}$.
- **All Dresses in One Corner ($[0, 0, 0, 4]$):** Target $1$. $s$ reaches $-3 \implies 3$ moves to shift dresses across boundaries.

---

## 6. Traps & Common Anti-Patterns

- **Simulating the Dresses Step-by-Step:** Trying to greedily simulate dresses moving left and right with array mutations takes $O(N \cdot \text{moves})$ and suffers from state oscillations. Prefix mathematical analysis calculates the answer directly in $O(N)$ time.
- **Using $|x|$ Instead of $x$ for the Machine Bottleneck:** If a machine has deficit $x = -5$, it can receive from both its left neighbor and right neighbor simultaneously. A deficit does NOT bottleneck at 5 moves; only a *positive surplus* $x > 0$ is constrained by the 1-dress-per-turn export limit.
- **Missing the Boundary Cut Bottleneck:** Relying only on $\max(x_i)$ fails when many small deficits accumulate on one side (e.g. $[1, 0, 5]$, where $\max(x) = 3$ happens to match $|s|$, but for $[0, 0, 0, 4]$ the cut load is $3$ while $x = 3$).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Summing the array takes $O(N)$ time.
  - A single linear loop over $N$ machines computes prefix sums and running maximums in $O(1)$ per machine.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space using scalar accumulators.
