# Guided Example: Maximum Profit of Operating a Centennial Wheel

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"customers": [8, 3], "boardingCost": 5, "runningCost": 6}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are the operator of a Centennial Wheel that has **four gondolas**, and each gondola has room for **up** **to** **four people**. You have the ability to rotate the gondolas **counterclockwise**, which costs you `runningCost` dollars.

The objective is to compute `3` from `{"customers": [8, 3], "boardingCost": 5, "runningCost": 6}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Evaluate the profit after every possible paid service rotation

Choosing when to stop means choosing a prefix of paid wheel rotations. The solution simulates those rotations in chronological order and records the earliest prefix with the largest positive cumulative profit.

Its state variables are:

- `i`: the number of rotations already performed and the index of the next arrival entry;
- `wait`: customers who have arrived but have not yet boarded;
- `t`: cumulative profit after `i` paid rotations;
- `mx`: highest positive-or-zero profit seen so far;
- `ans`: earliest rotation count at which a strictly positive record profit was achieved.

`ans` starts at negative one and `mx` starts at zero. Therefore, a non-positive profit never becomes an accepted operating plan.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"customers": [8, 3], "boardingCost": 5, "runningCost": 6}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the loop condition includes arrivals and backlog

The loop continues while:

`wait or i < len(customers)`.

If arrival entries remain, the operator must simulate the corresponding rotations to evaluate plans that serve those future customers. This includes arrival entries equal to zero: reaching a later arrival time still requires the intervening paid rotation described by the schedule.

After the final arrival, customers may remain in the queue because only four can board per rotation. `wait` keeps the loop running until that backlog is exhausted.

Once both conditions are false, there are no future customers and nobody waiting. Another paid rotation would board zero customers and subtract `runningCost`, so it cannot improve profit. Ending the simulation is safe.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Arrival happens before boarding

At the start of an iteration, the source adds:

`customers[i] if i < len(customers) else 0`

to `wait`. This follows the timing rule that `customers[i]` arrive just before the corresponding rotation. After the arrival list is exhausted, the conditional contributes zero while backlog rotations continue.

The next calculation is:

`up = wait if wait < 4 else 4`.

This is `min(wait, 4)` written as a conditional expression. It boards every waiting customer when fewer than four are present, or exactly the gondola capacity when at least four are waiting.

The rule says customers cannot be kept waiting when room exists, so the operator has no choice to board fewer people in hopes of changing later timing. `wait -= up` leaves exactly the unboarded queue.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"customers": [8, 3], "boardingCost": 5, "runningCost": 6}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Queue individual customer objects:** Only the waiting count affects boarding and profit. Storing each person wastes $O(A)$ space.
- **Stop simulation at the final arrival index:** This can miss profitable rotations that serve customers still waiting after arrivals end.
- **Simulate gondola positions:** Capacity at the boarding gondola and free safety rotations after stopping make occupant positions irrelevant to profit.
- **Update on `t >= mx`:** This would replace an earlier optimal rotation count with a later tie, violating the minimum-rotations requirement.
- **Initialize the best profit below zero:** That could accept a negative plan even though operating zero rotations yields profit zero and the required answer is `-1` when no positive plan exists.
- **Zero arrivals between future arrivals:** The scheduled rotation still incurs cost if the operator continues toward later customer batches, and the simulation includes it.
- **No positive profit:** `t` never exceeds initial `mx = 0`, so `ans` remains `-1`.
- **Profit becomes positive and later declines:** The record remains at the earlier profitable prefix.
- **Profit later exceeds the record:** `ans` updates to that rotation because the true maximum has improved.
- **Later tie with the maximum:** Strict comparison preserves the earlier rotation count.
- **Fewer than four waiting:** Every waiting customer boards because unused capacity cannot be withheld.
- **More than four waiting:** Exactly four board and the remainder stays for later rotations.
- **Backlog after final arrival:** The `wait` part of the loop condition continues service until it is empty, evaluating all useful prefixes.
- **No backlog and no future arrivals:** The loop stops because further paid rotations have negative incremental profit `-runningCost`.
- **Free rotations after stopping:** They safely unload onboard customers but do not alter the recorded paid-service profit or rotation choice requested by the problem.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $N$ be the number of arrival entries and let $A$ be the total number of arriving customers.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
