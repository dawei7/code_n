# Guided Example: Time Taken to Cross the Door

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arrival": [0, 1, 1, 2, 4], "state": [0, 1, 0, 0, 1]}`
- **Required output:** `[0, 3, 1, 2, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` persons numbered from `0` to $n - 1$ and a door. Each person can enter or exit through the door once, taking one second.

The objective is to compute `[0, 3, 1, 2, 4]` from `{"arrival": [0, 1, 1, 2, 4], "state": [0, 1, 0, 0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain one FIFO queue per direction

`q[0]` stores arrived people waiting to enter, and `q[1]` stores arrived people waiting to exit.

People are considered in increasing original index `i`. Because `arrival` is nondecreasing, appending them to their direction queue preserves arrival order and index order. Popping from the left therefore selects the smallest-index waiting person within that direction.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arrival": [0, 1, 1, 2, 4], "state": [0, 1, 0, 0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Interpret `st` as the preferred direction

`st=0` means entering has priority when both queues are non-empty. `st=1` means exiting has priority.

Before time zero, the door was not used in the previous second, so exiting should win an initial tie. The source initializes `st=1`.

After someone crosses, `st` remains or becomes that person's direction. If both directions compete in the next consecutive second, the previous direction wins as required.

If a second passes with nobody using the door, `st` resets to one, representing the rule that exiting wins after an idle previous second.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Add everyone who has arrived by current time

At the start of second `t`, the inner loop enqueues all still-unprocessed people with `arrival[i]<=t`.

Using `<=` rather than equality is robust when time advances through earlier idle iterations: anyone who arrived before or at current time must now be waiting.

The input order and monotonically increasing `i` ensure each person is enqueued exactly once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 3, 1, 2, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arrival": [0, 1, 1, 2, 4], "state": [0, 1, 0, 0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 3, 1, 2, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Jump over idle gaps:** Set `t` to the next arrival when both queues are empty; this removes dependence on the arrival-time bound.
- **Simultaneous arrivals:** Enqueue all before choosing, then apply direction and index priorities.
- **Initial tie:** Exit wins because the door was previously unused.
- **Consecutive same-direction use:** That direction retains priority.
- **Idle previous second:** Reset preference to exit.
- **Only one queue:** Its direction crosses regardless of prior preference.
- **Same direction tie:** FIFO order yields the smallest person index.
- **Arrival while others wait:** The new person joins the appropriate queue's tail.
- **One person per second:** Only one pop occurs per outer iteration.
- **Manifest mismatch:** This code advances idle seconds individually rather than jumping.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each person is appended once and popped once, for $O(n)$ queue operations. The loop can also execute idle seconds, but arrival times are bounded by `n`, so there are $O(n)$ such time steps. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
