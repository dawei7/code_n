# Guided Example: Minimum Lights to Illuminate a Road

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"lights": [0, 0, 0, 0]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `lights` of length `n`, representing positions 0 through $n - 1$ on a road.

The objective is to compute `2` from `{"lights": [0, 0, 0, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Representing existing coverage as interval updates

For an existing bulb at position `i` with positive radius `v`, the covered interval is

$$
\left[\max(0,i-v),\min(n-1,i+v)\right].
$$

Marking every position of every interval separately could take quadratic time when many bulbs have large radii. A difference array records an entire inclusive interval using only two constant-time changes.

The source creates `d` with `n` zeros. For interval `[l,r]`, it performs:



The positive change says that one more coverage interval begins at `l`. The negative change immediately after `r` says that this interval stops contributing. If `r=n-1`, there is no in-array position at which to subtract, so the second update is omitted.

Positions with `lights[i] == 0` contain no working bulb and create no interval.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"lights": [0, 0, 0, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recovering visibility with a prefix sum

During the final left-to-right scan, `s` is the running prefix sum of `d`. At position `p`, `s` equals the number of existing illumination intervals containing `p`:

- if `s>0`, at least one existing bulb illuminates the position;
- if `s=0`, the position is currently invisible.

The exact count above zero is unimportant; overlapping bulbs do not make a position “more than visible.” Still, using counts rather than booleans allows interval starts and ends to combine correctly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Turning invisible positions into runs

The variable `cnt` stores the length of the current consecutive invisible run. Whenever `s==0`, the source increments `cnt`. When a visible position is reached, the current run has ended, so its required bulbs are added to `ans` and `cnt` is reset.

After the loop, a final addition handles an invisible run that reaches the road's last position.

This delayed processing is useful because a new radius-one bulb can cover neighboring invisible positions together. Counting each invisible position independently would overestimate the answer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"lights": [0, 0, 0, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Mark every covered cell directly:** Looping through every existing interval is straightforward but can take `O(n^2)` time when many bulbs each illuminate most of the road. Difference updates reduce each interval to constant work.
- **Store merged intervals:** Sorting and merging existing coverage intervals can also reveal gaps, but bulb centers are already indexed along the road. The difference array obtains the same gap information in linear time without sorting.
- **Greedily place bulbs while scanning:** One can place a new bulb as far right as possible whenever the first uncovered position is encountered. That also leads to the same per-run count, but the source only needs the count and expresses it directly as `\lceil L/3\rceil`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of road positions. The first loop examines each entry of `lights` once and performs at most two constant-time difference-array updates. The second loop scans all `n` difference values once. Total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
