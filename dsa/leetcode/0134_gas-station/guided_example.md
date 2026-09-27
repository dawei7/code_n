# Guided Example: Gas Station

We trace the step-by-step single-pass greedy deficit reset and global feasibility summation on representative circular route instances:

- **Input:** $\text{gas} = [1, 2, 3, 4, 5]$, $\text{cost} = [3, 4, 5, 1, 2]$
- **Required output:** $3$ (Station 3 is the unique valid starting index)
- **Infeasible Base:** $\text{gas} = [2, 3, 4]$, $\text{cost} = [3, 4, 3] \implies -1$ ($\sum \text{gas} < \sum \text{cost}$)

This instance demonstrates net fuel gain transformation ($\Delta_i = \text{gas}[i] - \text{cost}[i]$), proves why a deficit at station $K$ invalidates all starting points between current start and $K$, explains the global invariant ($\sum \Delta \ge 0 \iff$ a valid circular start exists), and executes in $O(N)$ linear time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

There are $n = 5$ gas stations along a circular route. At station $i$, you receive $\text{gas}[i]$ and expend $\text{cost}[i]$ to travel to station $i + 1$:
$$
\text{gas} = [1, 2, 3, 4, 5], \quad \text{cost} = [3, 4, 5, 1, 2]
$$
Calculate the net fuel balance delta $\Delta_i = \text{gas}[i] - \text{cost}[i]$ for each station:
- Station 0: $1 - 3 = -2$
- Station 1: $2 - 4 = -2$
- Station 2: $3 - 5 = -2$
- Station 3: $4 - 1 = +3$
- Station 4: $5 - 2 = +3$

Total net fuel:
$$
\sum_{i=0}^4 \Delta_i = (-2) + (-2) + (-2) + 3 + 3 = 0 \ge 0
$$
Because the total fuel is non-negative, a complete circular circuit is guaranteed to exist.
Simulating from Station 3:
- Leave 3: Tank $= +3$. Reach 4.
- At 4: Tank $= 3 + 3 = 6$. Reach 0.
- At 0: Tank $= 6 - 2 = 4$. Reach 1.
- At 1: Tank $= 4 - 2 = 2$. Reach 2.
- At 2: Tank $= 2 - 2 = 0$. Reach 3.
Complete circuit achieved! Returns $3$.

A naive simulation tests all $N$ starting points for up to $N$ steps, taking $O(N^2)$ time.
The greedy reset theorem proves that whenever a tank dips below zero at station $K$, no station between the current start and $K$ can possibly complete the circuit, allowing the start pointer to jump directly to $K + 1$ in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### The Deficit Jump Theorem
Suppose we start at station $A$ and reach station $K$ ($K \ge A$), but the tank runs dry at leg $K$ ($\text{curr\_tank} < 0$).
Could any intermediate station $B$ ($A \le B \le K$) be a valid starting point?
**Proof by contradiction:**
Because we reached $B$ starting from $A$ with an empty tank, the fuel remaining at $B$ was non-negative ($\text{fuel}_B \ge 0$).
If starting at $A$ with surplus fuel at $B$ failed to traverse past $K$, then starting at $B$ with strictly **zero** initial fuel will run dry even sooner (at or before $K$).
Therefore, **every station from $A$ to $K$ is disqualified simultaneously**.
The next candidate start must be at least $K + 1$.

### Greedy Single-Pass Protocol
Maintain:
- $\text{total\_tank} = 0$: Tracks $\sum_{i=0}^{N-1} (\text{gas}[i] - \text{cost}[i])$.
- $\text{curr\_tank} = 0$: Running fuel balance since candidate `start`.
- $\text{start} = 0$: Candidate starting station index.

For $i$ from $0$ to $N - 1$:
1. Let $\Delta = \text{gas}[i] - \text{cost}[i]$.
2. $\text{total\_tank} \leftarrow \text{total\_tank} + \Delta$.
3. $\text{curr\_tank} \leftarrow \text{curr\_tank} + \Delta$.
4. If $\text{curr\_tank} < 0$:
   - Deficit encountered! Disqualify all stations $\text{start} \dots i$.
   - $\text{start} \leftarrow i + 1$
   - $\text{curr\_tank} \leftarrow 0$

**Final Decision:**
If $\text{total\_tank} < 0$: return $-1$ (insufficient total fuel).
Else: return $\text{start}$.

> **Invariant.** If $\text{total\_tank} \ge 0$, the candidate index `start` reached at the end of the loop is mathematically guaranteed to complete the entire circular tour without ever dropping below zero.

---

## 3. Step-by-Step Worked Execution

We trace the single-pass greedy scan on $\text{gas} = [1, 2, 3, 4, 5]$ and $\text{cost} = [3, 4, 5, 1, 2]$:

### Initialization
- $\text{total\_tank} = 0$
- $\text{curr\_tank} = 0$
- $\text{start} = 0$

---

### Step 1: Station $i = 0$ ($1 - 3 = -2$)
- $\Delta = -2$.
- $\text{total\_tank} = 0 - 2 = -2$.
- $\text{curr\_tank} = 0 - 2 = -2$.
- $\text{curr\_tank} < 0 \implies$ Deficit at station 0!
  - Disqualify Station 0.
  - Reset: $\text{start} \leftarrow 0 + 1 = \mathbf{1}$.
  - Reset: $\text{curr\_tank} \leftarrow 0$.

---

### Step 2: Station $i = 1$ ($2 - 4 = -2$)
- $\Delta = -2$.
- $\text{total\_tank} = -2 - 2 = -4$.
- $\text{curr\_tank} = 0 - 2 = -2$.
- $\text{curr\_tank} < 0 \implies$ Deficit at station 1!
  - Disqualify Station 1.
  - Reset: $\text{start} \leftarrow 1 + 1 = \mathbf{2}$.
  - Reset: $\text{curr\_tank} \leftarrow 0$.

---

### Step 3: Station $i = 2$ ($3 - 5 = -2$)
- $\Delta = -2$.
- $\text{total\_tank} = -4 - 2 = -6$.
- $\text{curr\_tank} = 0 - 2 = -2$.
- $\text{curr\_tank} < 0 \implies$ Deficit at station 2!
  - Disqualify Station 2.
  - Reset: $\text{start} \leftarrow 2 + 1 = \mathbf{3}$.
  - Reset: $\text{curr\_tank} \leftarrow 0$.

---

### Step 4: Station $i = 3$ ($4 - 1 = +3$)
- $\Delta = +3$.
- $\text{total\_tank} = -6 + 3 = -3$.
- $\text{curr\_tank} = 0 + 3 = 3$.
- $\text{curr\_tank} \ge 0 \implies$ Station 3 remains candidate start.

---

### Step 5: Station $i = 4$ ($5 - 2 = +3$)
- $\Delta = +3$.
- $\text{total\_tank} = -3 + 3 = \mathbf{0}$.
- $\text{curr\_tank} = 3 + 3 = 6$.
- $\text{curr\_tank} \ge 0 \implies$ Station 3 remains candidate start.

---

### Circuit Validation
Loop completes:
- Total fuel balance: $\text{total\_tank} = 0 \ge 0$.
- Candidate starting station is $\text{start} = \mathbf{3}$.

Result: Station $3$ successfully completes the circuit.

---

## 4. Complete Execution Trace

```text
Stations:       0      1      2      3      4
Gas - Cost:    -2     -2     -2     +3     +3
curr_tank:     -2     -2     -2     +3     +6
Action:       RESET  RESET  RESET   KEEP   KEEP
start ptr:      1      2      3      3      3  => START = 3
total_tank:     0 (>= 0 -> Feasible)
```

| Station $i$ | $\text{gas}[i]$ | $\text{cost}[i]$ | Net $\Delta_i$ | $\text{curr\_tank}$ Before Reset | Deficit Occurs? | Updated $\text{start}$ | Cumulative $\text{total\_tank}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 3 | $-2$ | $-2$ | **Yes** | 1 | $-2$ |
| 1 | 2 | 4 | $-2$ | $-2$ | **Yes** | 2 | $-4$ |
| 2 | 3 | 5 | $-2$ | $-2$ | **Yes** | 3 | $-6$ |
| 3 | 4 | 1 | $+3$ | $+3$ | No | 3 | $-3$ |
| 4 | 5 | 2 | $+3$ | $+6$ | No | **3** | **0 (Feasible)** |

The pointer value alone is not yet a proof, so the resulting tour is walked once at the level of individual legs. The tank starts empty at the candidate station, and each row credits the fuel of the departure station before charging the leg:

| Leg | Depart from $i$ | $\text{gas}[i]$ | $\text{cost}[i]$ | Tank on arrival at $(i + 1) \bmod 5$ | Dropped below zero? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 3 | 4 | 1 | $0 + 4 - 1 = 3$ | No |
| 2 | 4 | 5 | 2 | $3 + 5 - 2 = 6$ | No |
| 3 | 0 | 1 | 3 | $6 + 1 - 3 = 4$ | No |
| 4 | 1 | 2 | 4 | $4 + 2 - 4 = 2$ | No |
| 5 | 2 | 3 | 5 | $2 + 3 - 5 = 0$ | No, the tank is exactly empty on returning to station 3 |

The smallest arrival value is $0$, reached only on the final leg, and it is reached exactly when the car is back at the candidate station. That is the sharp boundary the reset rule respects: the tank is allowed to be exactly empty at a station, and a reset is triggered only by a strictly negative value.

---

## 5. Algorithmic Correctness

**Soundness.** If the sum of all net gains is non-negative ($\sum \Delta \ge 0$), then the sum of losses is compensated by the sum of surpluses. Because $\text{curr\_tank} \ge 0$ across the entire suffix $[\text{start} \dots N-1]$, and the accumulated deficit across prefix $[0 \dots \text{start}-1]$ is at most the total surplus, the car has sufficient remaining fuel upon wrapping around from $N-1$ to $0$ to traverse the prefix back to `start`.

**Completeness.** Every time `curr_tank` falls below zero at step $i$, the Deficit Jump Theorem proves that no index in the range $[\text{old\_start} \dots i]$ can be valid. Hence, candidate discarding is strictly sound and complete.

---

## 6. Traps This Instance Exposes

- **Simulating the Wraparound Twice ($O(N^2)$ Trap):** There is no need to run a second circular simulation once the loop finishes! If $\text{total\_tank} \ge 0$, mathematical induction proves that `start` is guaranteed to succeed.
- **Total Gas Insufficiency:** If $\sum \text{gas} < \sum \text{cost}$, no starting station anywhere on the circle can succeed because the net energy of the closed loop is strictly negative. Checking `if total_tank < 0: return -1` immediately catches this.
- **Zero Balance Transitions:** Running with `curr_tank == 0` is allowed; fuel is empty, but the car does not stall. The deficit reset is triggered strictly on `curr_tank < 0`.

The authored cases show both sides of the final decision, including the one where a surviving candidate is still overruled:

| Authored case | Net sequence $\Delta_i$ | $\sum_i \Delta_i$ | Candidate `start` after the pass | Returned | What decides the row |
|:---|:---|:---:|:---:|:---:|:---|
| `sample-1` | $[-2, -2, -2, +3, +3]$ | $0$ | 3 | 3 | Three resets consume stations 0, 1 and 2; the surviving suffix then carries the tour |
| `sample-2` | $[-1, -1, +1]$ | $-1$ | 2 | $-1$ | A candidate index does survive, but the global guard overrides it because the closed loop is net negative |
| `trial-single-station` | $[+1]$ | $+1$ | 0 | 0 | The single leg earns more than it spends, so no reset ever fires |
| `trial-late-start` | $[+1, -3, +1, -2, +3]$ | $0$ | 4 | 4 | Resets at stations 1 and 3 discard indices 0 through 3, leaving only the final suffix |

The second row is the reason the guard is not optional: the deficit resets leave `start = 2`, yet no station can complete a cycle whose total net fuel is $-1$, and reporting that index would be wrong.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of gas stations. The array is traversed once in a single forward pass, performing $O(1)$ scalar updates per station.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, utilizing only three scalar counters (`total_tank`, `curr_tank`, `start`).

Three strategies agree on every authored case, but only two of them are linear:

| Strategy | Work performed | Time | Auxiliary space | Behavior on `sample-2` |
|:---|:---|:---:|:---:|:---|
| Simulate every candidate start | Up to $N$ legs are walked for each of the $N$ starts | $O(N^2)$ | $O(1)$ | Returns $-1$ only after all three candidate starts have failed |
| Single-pass greedy with deficit resets | One forward pass over the net sequence | $O(N)$ | $O(1)$ | Resets at stations 0 and 1, then the global guard returns $-1$ |
| Two-pointer window grown leftwards | A window absorbs a station on its left whenever its own balance turns negative | $O(N)$ | $O(1)$ | Also returns $-1$, because the final window balance is still negative |

The first row is the honest baseline: it is only correct because it retries after every failure. The greedy rows reach the same index in one pass because a failure at station $K$ retires a whole contiguous block of candidates at once.

---
