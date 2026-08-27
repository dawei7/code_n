# Guided Example: The Latest Time to Catch a Bus

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"buses": [10, 20], "passengers": [2, 17, 18, 19], "capacity": 2}`
- **Required output:** `16`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `buses` of length `n`, where $\text{buses}[i]$ represents the departure time of the $$i^{\text{th}}$$ bus. You are also given a **0-indexed** integer array `passengers` of length `m`, where $\text{passengers}[j]$ represents the arrival time of the $$j^{\text{th}}$$ passenger. All bus departure times are unique. All passenger arrival times are unique.

The objective is to compute `16` from `{"buses": [10, 20], "passengers": [2, 17, 18, 19], "capacity": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort all events into chronological order

Passengers board in order of arrival, and buses depart in order of time. The input arrays are not sorted, so the method first sorts both in ascending order.

The pointer `j` is the index of the earliest passenger who has not boarded yet. For each bus departure `t`, `c` starts at `capacity` and the inner loop boards passengers while three conditions hold: a seat remains, a passenger remains, and that passenger arrived no later than `t`.

Advancing `j` after every boarding means passengers taken by earlier buses are never reconsidered. When the bus loop ends, the simulation exactly matches the schedule without the new traveler.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"buses": [10, 20], "passengers": [2, 17, 18, 19], "capacity": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Only the final bus determines the latest possible arrival

Any arrival that catches an earlier bus cannot be later than a feasible arrival for the last bus unless the later buses' seats are completely claimed by earlier-arriving passengers. The chronological simulation tells us the boundary at the final departure.

After the final bus:

- if `c > 0`, it has a spare seat after all eligible existing passengers board, so arriving at the final departure time itself is initially feasible;
- if `c == 0`, it is full, and the latest new traveler could enter its queue no later than the arrival time of the last passenger who obtained a seat.

The code first decrements `j` because during simulation it points one position after the last boarded passenger. Then it sets `ans` to `buses[-1]` for a nonfull final bus, or `passengers[j]` for a full one.

In the full case, matching the last boarded passenger's time is forbidden, so the later collision-removal loop immediately retreats below it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Any arrival that catches an earlier bus cannot be later than... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Retreat through occupied arrival times

The candidate cannot equal any existing passenger arrival, even if that passenger boarded an earlier bus. Because `passengers` is sorted, the relevant occupied times at or below the candidate appear immediately backward from `j`.

The loop condition `~j` is a compact Python test for `j != -1` in this controlled range. When `j >= 0`, `~j` is a nonzero negative integer and is truthy. When `j == -1`, `~j == 0` and the loop stops.

If `passengers[j] == ans`, the candidate is occupied. The method subtracts one from `ans` and moves `j` to the previous passenger. If that earlier passenger occupies the new candidate, it repeats. The final value is the greatest unoccupied integer time at or below the boarding boundary.

For a full last bus whose last boarded passenger arrives at 17, the initial candidate 17 collides and becomes 16. If another passenger arrived at 16, it becomes 15, continuing until a gap is found.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `16` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"buses": [10, 20], "passengers": [2, 17, 18, 19], "capacity": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `16` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Binary search an arrival time:** Simulate boar:** - **Binary search an arrival time:** Simulate boarding for each candidate and test feasibility. This repeats substantial work and is unnecessary once the final boarding boundary is known.
- **Use a set for collision checks:** Start from the boundary and decrement while the candidate is in a passenger set. This is correct with expected constant lookup but uses additional `O(p)` storage; the sorted backward pointer reuses ordering.
- **Simulate the new traveler explicitly at many times:** Only the boundary passenger and occupied-time gaps matter. Full schedule resimulation for every candidate is wasteful.
- **Final bus has spare capacity:** Its departure time is best unless an existing passenger has exactly that arrival, in which case retreat finds the next gap.
- **Final bus is full:** Start from its last boarded passenger's time, then retreat at least once because that time is occupied.
- **No passenger boards any bus:** After `j -= 1`, `j = -1` and the last bus has spare capacity. The collision loop safely skips, returning the last departure.
- **Consecutive occupied times:** The backward loop retreats through the entire consecutive block.
- **Passengers arriving after the last bus:** They never board and lie beyond pointer `j`. They cannot collide with a candidate at or before the last departure unless equal ordering made them eligible, so ignoring them is correct.
- **Capacity one:** Each bus boards at most the earliest waiting passenger; the same pointer simulation applies.
- **Many early passengers:** Earlier buses remove them from the queue, which is why simulating every bus before inspecting the last one is necessary.
- **Unique passenger times:** The source guarantee means one backward step handles one occupied time; duplicates would require different queue and collision handling.
- **Bitwise complement condition:** `~j` is correct only because `j` stops at `-1` and never needs values below it. An explicit `j >= 0` would be clearer.
- **Input mutation:** Both `buses` and `passengers` are sorted in place.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(b log b + p log p)$. Let `b` be the number of buses and `p` the number of passengers. Sorting costs `O(b \log b + p \log p)`. The boarding pointer advances at most `p` times across all buses, and the collision retreat also moves backward at most `p` times, so simulation is linear after sorting.
- **Auxiliary Space Complexity:** $O(b + p)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
