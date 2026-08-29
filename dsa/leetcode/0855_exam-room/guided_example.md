# Guided Example: Exam Room

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 10, "operations": [["seat"], ["seat"], ["seat"], ["seat"], ["leave", 4], ["seat"]]}`
- **Required output:** `[0, 9, 4, 2, null, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an exam room with `n` seats in a single row labeled from `0` to $n - 1$.

The objective is to compute `[0, 9, 4, 2, null, 5]` from `{"n": 10, "operations": [["seat"], ["seat"], ["seat"], ["seat"], ["leave", 4], ["seat"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent available choices as gaps between occupied boundaries

When some seats are occupied, every available seat lies in a gap between two occupied seats, or between a room boundary and the nearest occupied seat.

The solution represents one gap as tuple `(l,r)`:

- `l` and `r` are occupied seats bounding the gap;
- virtual boundary `-1` represents the space before seat 0;
- virtual boundary `n` represents the space after seat `n-1`.

The available seats in the gap are strictly between `l` and `r`.

Initially, no seat is occupied, so one interval `(-1,n)` represents the whole room.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 10, "operations": [["seat"], ["seat"], ["seat"], ["seat"], ["leave", 4], ["seat"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Best distance within a gap

Nested function `dist(x)` calculates the maximum closest-person distance obtainable from interval `(l,r)`.

For a leading interval `(-1,r)`, the best seat is 0 and its distance to the person at `r` is `r`. The formula `r-l-1` becomes `r`.

For a trailing interval `(l,n)`, the best seat is `n-1` and its distance is `n-l-1`, again `r-l-1`.

For an internal interval with occupied endpoints, the best seat is the lower midpoint:

$$
\left\lfloor\frac{l+r}{2}\right\rfloor,
$$

and its distance to the nearer endpoint is:

$$
\left\lfloor\frac{r-l}{2}\right\rfloor.
$$

The function returns `(r-l) >> 1` for this case.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep gaps ordered by the seating rule

`SortedList` uses key:

`(-dist(x), x[0])`.

Negating distance means a gap with larger achievable distance sorts earlier. If distances tie, smaller left boundary sorts earlier. Its selected seat is also smaller, so this enforces the required lowest-seat tie break.

`ts[0]` is therefore always the gap containing the next correct seat.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 9, 4, 2, null, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 10, "operations": [["seat"], ["seat"], ["seat"], ["seat"], ["leave", 4], ["seat"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 9, 4, 2, null, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Store occupied seats and scan every gap on `seat`:** Leaving is easy, but each seating call can take `O(q)` time.
- **Allocate an array of `n` seats:** Impossible when `n` is up to `10^9` and unnecessary for only `10^4` operations.
- **Priority queue with lazy deletion:** It can choose maximum gaps but needs stale-entry handling and neighbor maps. `SortedList` supports direct deletion.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q\log q)$. Let `q` be the number of operations performed so far. There are `O(q)` occupied boundaries and gaps.
- **Auxiliary Space Complexity:** $O(q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
