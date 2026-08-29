# Guided Example: Put Boxes Into the Warehouse I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"boxes": [4, 3, 4, 1], "warehouse": [5, 3, 3, 4, 1]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two arrays of positive integers, `boxes` and `warehouse`, representing the heights of some boxes of unit width and the heights of `n` rooms in a warehouse respectively. The warehouse's rooms are labelled from `0` to $n - 1$ from left to right where $\text{warehouse}[i]$ (0-indexed) is the height of the $i^{\text{th}}$ room.

The objective is to compute `3` from `{"boxes": [4, 3, 4, 1], "warehouse": [5, 3, 3, 4, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace room height with reachable height

A box enters only from the left. Even if a room is tall, a shorter earlier room can block a tall box from ever reaching it.

For room `i`, the maximum box height that can reach it is therefore the minimum physical height among rooms zero through `i`.

The source stores these entrance bottlenecks in `left`:

`left[i] = min(left[i - 1], warehouse[i])`.

`left[0]` is the first room's height. Each later value is no greater than its predecessor, so `left` is non-increasing from left to right.

A box fits in final room `i` exactly when its height is at most `left[i]`. Once these effective capacities are known, the physical passage rule no longer needs to be simulated.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"boxes": [4, 3, 4, 1], "warehouse": [5, 3, 3, 4, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort boxes from shortest to tallest

The source sorts `boxes` in ascending order. Pointer `i` identifies the shortest box not yet placed.

Smaller boxes are the most flexible: every room that accepts a taller box also accepts a shorter one. Trying the shortest remaining box first prevents a tall box from consuming a room that might be the only option for some smaller-box arrangement deeper inside.

The sort happens in place, so the supplied `boxes` list is permanently reordered.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Fill rooms from deepest to shallowest

Pointer `j` starts at `n - 1`, the rightmost room. If the current shortest box fits effective capacity `left[j]`, the algorithm places it there, advances to the next box, and moves `j` one room left.

Placing a chosen box as deep as possible is safe. A deep room is harder to reach because it inherits every earlier bottleneck. Using it for a box that fits leaves the shallower, weakly larger capacities available for later taller boxes.

If `left[j] < boxes[i]`, the current box cannot reach room `j`. The source moves `j` left until it finds a room with enough effective height or runs out of rooms.

Because `left` becomes weakly larger as `j` moves left, this search progresses toward increasingly permissive rooms.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"boxes": [4, 3, 4, 1], "warehouse": [5, 3, 3, 4, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Modify warehouse in place:** Replace every height by its prefix minimum and avoid the separate `left` array, if input mutation is allowed.
- **Largest-box left-to-right greedy:** Sort descending, discard boxes too tall for each current room, and place the largest that fits. It is an equivalent strategy.
- **Simulate pushing each box:** It repeatedly rechecks bottlenecks and obscures the effective-capacity reduction.
- **First room is shortest:** Every effective capacity equals that height, so only boxes no taller than it can enter.
- **Warehouse widens later:** A later tall room remains limited by the narrowest earlier room.
- **More boxes than rooms:** At most one box per room, and the pointer stops after all rooms are consumed.
- **More rooms than boxes:** The loop stops after every box is placed.
- **Smallest box too tall:** No remaining box can fit any remaining room.
- **Equal heights:** Sorting and comparisons handle duplicate box or room heights normally.
- **Exact fit:** `left[j] == boxes[i]` is allowed.
- **Unit width and no stacking:** They justify treating every room as one placement slot.
- **Input mutation:** Sorting changes box order, while the separate prefix array leaves warehouse heights unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B\log B+W)$. Let $B$ be box count and $W$ room count. Computing prefix minima costs $O(W)$. Sorting boxes costs $O(B\log B)$.
- **Auxiliary Space Complexity:** $O(B+W)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
