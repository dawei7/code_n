# Guided Example: Snake in Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "commands": ["RIGHT", "DOWN"]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a snake in an `n x n` matrix `grid` and can move in **four possible directions**. Each cell in the `grid` is identified by the position: $\text{grid}[i][j] = (i * n) + j$.

The objective is to compute `3` from `{"n": 2, "commands": ["RIGHT", "DOWN"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

Cell identifiers use row-major order. A cell at row $r$ and column $c$ has identifier

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "commands": ["RIGHT", "DOWN"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

The snake starts at identifier zero, which corresponds to coordinates `(0,0)`. The solution tracks its row in `x` and column in `y` while executing every command, then applies the row-major formula once at the end.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Each legal command changes exactly one coordinate by one:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "commands": ["RIGHT", "DOWN"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Track the identifier directly:** Add minus $n$, plus $n$, minus one, or plus one for up, down, left, and right. This uses one scalar and exactly matches the manifest summary, with the same $O(c)$ time and $O(1)$ space.
- **Direction dictionary:** Map each complete command to a coordinate pair or identifier delta. This can make the transition table data-driven, though four match cases are already clear.
- **Simulate an actual matrix:** Allocating cell values or marking visited locations is unnecessary because only the final position matters.
- **Count commands by direction:** Summing the number of ups, downs, lefts, and rights also yields the final coordinates under legal input. Sequential processing is simpler and remains linear.
- **Returning to the start:** Opposite commands cancel. If final `x` and `y` are both zero, the returned identifier is zero regardless of the path taken.
- **Moves along a boundary:** They are handled like any other moves. The guarantee excludes only commands that would cross the boundary.
- **One command:** The corresponding single coordinate update is encoded directly.
- **Repeated commands:** Each occurrence represents another unit move and is processed independently.
- **First-character dispatch:** It is safe only because the four legal command strings have distinct initial letters. If new commands with shared initials were added, full-string matching would be necessary.
- **Illegal command:** No match case would run, effectively treating it as no movement. The contract guarantees this situation never occurs; the source does not validate or raise an error.
- **Illegal out-of-bounds path:** The exact code would allow negative or oversized coordinates and return an invalid identifier. Correctness is scoped to the explicit boundary guarantee.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(c)$. Let $c$ be the number of commands. The loop examines each command once and performs one constant-time coordinate update, giving $O(c)$ time. Accessing `c[0]` is constant time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
