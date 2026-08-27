# Guided Example: Average Height of Buildings in Each Segment

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"buildings": [[1, 4, 2], [3, 9, 4]]}`
- **Required output:** `[[1, 3, 2], [3, 4, 3], [4, 9, 4]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A perfectly straight street is represented by a number line. The street has building(s) on it and is represented by a 2D integer array `buildings`, where $\text{buildings}[i] = [\text{start}_{i}, \text{end}_{i}, \text{height}_{i}]$. This means that there is a building with $\text{height}_{i}$ in the **half-closed segment** $[\text{start}_{i}, \text{end}_{i})$.

The objective is to compute `[[1, 3, 2], [3, 4, 3], [4, 9, 4]]` from `{"buildings": [[1, 4, 2], [3, 9, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Record changes only at endpoints

Between consecutive building endpoints, the set of active buildings is constant. Its count and sum of heights are constant, so the integer average is constant.

For building `[start,end,height]`, the source records:

- count change +1 at start and -1 at end in `cnt`;
- height-sum change +height at start and -height at end in `d`.

This is a difference-map sweep line. It avoids visiting every coordinate up to $10^8$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"buildings": [[1, 4, 2], [3, 9, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain the active aggregate

`m` is the number of buildings active immediately to the right of the last processed endpoint, and `s` is their total height. `last` is that endpoint.

When the loop reaches next coordinate `k`, the values of `s` and `m` describe interval `[last,k)`. The source emits that interval before applying events at `k`.

This order matches half-open semantics: a building ending at `k` is still active throughout the interval leading up to `k`, while a building starting at `k` becomes active only to its right.

If one building ends exactly where another begins, the interval before the coordinate is emitted using the old building. Then both endpoint deltas are applied together, removing the old height and adding the new one for the following interval. There is no zero-width segment at the shared coordinate, and no moment when both buildings are incorrectly counted over a positive-length interval.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `m` is the number of buildings active immediately to the rig... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Skip uncovered gaps

If `m==0`, no building covers `[last,k)`, so the source emits nothing. It still updates `last=k` after processing events.

This retained gap boundary later prevents equal-average occupied regions on opposite sides of an empty gap from being merged.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 3, 2], [3, 4, 3], [4, 9, 4]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"buildings": [[1, 4, 2], [3, 9, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 3, 2], [3, 4, 3], [4, 9, 4]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Coordinate-by-coordinate simulation:** Impossi:** - **Coordinate-by-coordinate simulation:** Impossible when endpoints reach $10^8$; only event coordinates matter.
- **Store active heights in a multiset:** Unnecessary because only their sum and count determine the average.
- **Sort explicit start/end events:** Equivalent to difference maps but must combine simultaneous events before describing the next interval.
- **Several events at one coordinate:** Dictionary accumulation applies their net effect together.
- **No active building:** Omit the interval from output.
- **Equal averages across an endpoint:** Merge when segments are contiguous.
- **Equal averages across an empty gap:** Do not merge; the endpoint-contiguity check prevents it.
- **Half-open boundary:** Emit the preceding interval before applying current deltas.
- **Single building:** Produces its original interval and height.
- **Complete overlap:** Sum heights and divide by active count.
- **Integer division:** `s // m` implements the specified truncation for positive heights.
- **Any output order:** The source returns sorted street order, which is valid.
- **Input preservation:** It builds event maps without sorting or modifying `buildings`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B\log B)$. Let $B$ be the number of buildings and $E\le2B$ the number of distinct endpoints. Recording events takes $O(B)$ expected time. Sorting endpoints costs $O(E\log E)=O(B\log B)$, and the sweep is linear.
- **Auxiliary Space Complexity:** $O(B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
