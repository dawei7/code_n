# Guided Example: Game of Life

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]}`
- **Required output:** `[[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

According to <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">Wikipedia's article</a>: "The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The objective is to compute `[[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]` from `{"board": [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: The in-place difficulty is simultaneous state change

Every cell's next state must be computed from the same original generation. If the algorithm changed a live cell directly from 1 to 0 and then processed its neighbor, that neighbor would incorrectly see the new dead state rather than the original live state. A full copy solves this, but the follow-up asks for constant extra space.

The exact source temporarily encodes both old and new state in the board cell itself. During the first pass, original-state information remains recoverable even after a cell has been assigned its next state. A second pass converts temporary markers back to ordinary zeros and ones.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the four stored states

The source uses this transition encoding:

| Original state | Next state | Value during first pass |
|---:|---:|---:|
| dead 0 | dead 0 | `0` |
| dead 0 | live 1 | `-1` |
| live 1 | live 1 | `1` |
| live 1 | dead 0 | `2` |

The sign separates original state:

- positive temporary values, `1` and `2`, were originally live;
- nonpositive values, `0` and `-1`, were originally dead.

The exact numeric marker also remembers the next state. Marker `2` means a live cell must become dead, while marker `-1` means a dead cell must become live. Unchanged cells keep their ordinary value.

This encoding is the reverse of another common convention that uses `-1` for live-to-dead and `2` for dead-to-live. What matters is consistency. The protected source counts `> 0` as originally live, so its marker meanings are exactly those in the table above.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source uses this transition encoding:

| Original state ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count original live neighbors even after earlier updates

For each cell `(i, j)`, the source examines row coordinates from `i - 1` through `i + 1` and column coordinates from `j - 1` through `j + 1`. Out-of-bounds coordinates are skipped. This square contains the eight neighbors and the cell itself.

A candidate location contributes one when `board[x][y] > 0`. Original live cells still have value 1 if they survive or 2 if they were processed earlier and will die. Both count as live in the original generation. A newly born cell has marker `-1`, which is not positive, so later cells correctly still regard it as originally dead.

Thus scan order cannot contaminate neighbor counts: temporary transitions preserve exactly the old-state classification needed by every later calculation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Copy the board:** Read every old state from a :** - **Copy the board:** Read every old state from a full copy and write new states into the original. It is straightforward and $O(mn)$ time but requires $O(mn)$ additional space.
- **Bit encoding:** Store the old state in one bit and the new state in another, then shift every cell. This is another clean $O(1)$-space technique; the signed-marker source uses comparison and explicit cleanup instead.
- **Different marker convention:** Using `-1` for live-to-dead and `2` for dead-to-live works only if old liveness is tested with `abs(value) == 1`. Mixing that rule with this source's `> 0` test would be incorrect.
- **Corner cell:** Only three neighbor coordinates are in bounds; all others are skipped.
- **Edge non-corner cell:** It has at most five legal neighbors, handled by the same bounds checks.
- **Single-cell dead board:** It has zero live neighbors, remains zero, and needs no marker.
- **Single-cell live board:** Self-count cancellation leaves zero neighbors, so under-population marks it 2 and cleanup makes it dead.
- **All dead cells:** No cell has three live neighbors, so the board remains all zero.
- **Birth beside processed deaths:** Death markers remain positive and count as originally live, so the birth calculation is still based on the old generation.
- **Survival rule:** A live cell with exactly two or three neighbors stays 1; no explicit assignment is necessary.
- **Infinite sparse board:** Store coordinates of live cells in a set and count neighbor occurrences around them, rather than materializing infinitely many dead cells. This changes the representation and uses space proportional to the active region.
- **Huge board stored externally:** Because one row's update depends only on itself and adjacent rows, a streaming design can retain a small rolling window of rows, though writing results requires careful separation from unread original data.
- **Rectangular dimensions:** Separate `m` and `n` bounds support all legal non-square boards.
- **Original binary constraint:** The marker logic assumes first-pass unprocessed cells begin only as 0 or 1. Other initial values would collide with the temporary-state interpretation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let the board have $m$ rows and $n$ columns. The first pass visits every cell and examines a fixed 3-by-3 neighborhood of nine candidate coordinates. Nine is constant, so this pass takes $O(mn)$ time. The cleanup pass also takes $O(mn)$ time, leaving total time $O(mn)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
