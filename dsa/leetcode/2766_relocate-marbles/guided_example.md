# Guided Example: Relocate Marbles

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 6, 7, 8], "moveFrom": [1, 7, 2], "moveTo": [2, 9, 5]}`
- **Required output:** `[5, 6, 8, 9]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` representing the initial positions of some marbles. You are also given two **0-indexed **integer arrays `moveFrom` and `moveTo` of **equal** length.

The objective is to compute `[5, 6, 8, 9]` from `{"nums": [1, 6, 7, 8], "moveFrom": [1, 7, 2], "moveTo": [2, 9, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track occupied positions, not individual marbles

The output asks only which positions are occupied after all moves. It does not ask how many marbles occupy each position. That distinction allows the exact solution to represent the entire state with a set of coordinates.

`pos = set(nums)` removes duplicate initial coordinates. If several marbles start at position 3, the set stores 3 once, which is sufficient to answer whether position 3 is occupied. The number of marbles at that coordinate never affects future decisions because each operation moves all marbles from its source together.

This is the main compression: potentially many physical marbles at the same coordinate have identical movement histories until they merge with others, and the required result treats any positive count identically.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 6, 7, 8], "moveFrom": [1, 7, 2], "moveTo": [2, 9, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Simulate one move as a set transfer

The paired loops `for f, t in zip(moveFrom, moveTo)` process operations in their given chronological order. For each source `f` and destination `t`:

1. `pos.remove(f)` marks the source unoccupied.
2. `pos.add(t)` marks the destination occupied.

The contract guarantees that at least one marble is at `f` when the operation is applied. Therefore `f` must be present in the set, and `remove` will not raise an error on valid input.

If `t` is already occupied, adding it again changes nothing. That is exactly right: the moved marbles join the marbles already there, but the output still needs only one copy of the coordinate.

If `f == t`, removal temporarily clears the coordinate and addition immediately restores it. The net occupied set is unchanged, matching the fact that moving all marbles from a position to the same position has no observable effect.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The paired loops `for f, t in zip(moveFrom, moveTo)` process... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why multiplicities can never become relevant later

It may seem dangerous to forget counts because a later operation could move marbles away again. However, every later move also transfers all marbles at its source. Whether one marble or a thousand occupy that coordinate, after that move the source is empty and the destination is occupied. The transition on occupied positions is identical:

$$
P' = (P \setminus \{f\}) \cup \{t\}.
$$

There is no operation that moves only one marble, tests a count, or splits the marbles at a coordinate across destinations. Therefore counts have no influence on any future occupied-set transition.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[5, 6, 8, 9]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 6, 7, 8], "moveFrom": [1, 7, 2], "moveTo": [2, 9, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[5, 6, 8, 9]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency map of marble counts:** It can simul:** - **Frequency map of marble counts:** It can simulate exact quantities, but counts are never queried and every move transfers the complete source count. A set contains all information needed for the output and future transitions.
- **Move every marble individually:** This repeats work for duplicates and can become much more expensive when many marbles share a coordinate.
- **Maintain a sorted set throughout:** It supports ordered output but makes each update logarithmic. Hash updates plus one final sort are simpler and match the exact code.
- **Sort after every move:** Intermediate order is irrelevant, so repeated sorting wastes work.
- **Destination already occupied:** `add` is idempotent; the two marble groups merge into one occupied coordinate.
- **Source equals destination:** Remove followed by add restores the same set.
- **Duplicate initial positions:** `set(nums)` intentionally collapses them because occupation is Boolean.
- **Later move uses an earlier destination:** Sequential processing preserves that dependency exactly.
- **Large or negative coordinate considerations:** The given coordinates are positive up to `10^9`, and hashing avoids allocating an array indexed by coordinate.
- **Guaranteed occupied source:** `remove` is appropriate because invalid absence need not be handled; `discard` would silently hide a broken precondition.
- **Equal move-array lengths:** `zip` covers every operation under the contract. Unequal arrays would be truncated, but that input is excluded.
- **Final set has one coordinate:** Sorting returns a one-element list, including after many merges.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + m + k \log k)$. Let `n` be `nums.length`, `m` be the number of moves, and `k` be the number of final occupied positions. Building `set(nums)` takes `O(n)` expected time. Every move performs one hash-set removal and one insertion, each `O(1)` expected, for `O(m)` expected simulation time. Sorting the final `k` distinct coordinates costs `O(k log k)`. Total expected time is
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
