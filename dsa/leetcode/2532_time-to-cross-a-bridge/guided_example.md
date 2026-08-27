# Guided Example: Time to Cross a Bridge

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1, "k": 3, "time": [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `k` workers who want to move `n` boxes from the right (old) warehouse to the left (new) warehouse. You are given the two integers `n` and `k`, and a 2D integer array `time` of size `k x 4` where $\text{time}[i] = [\text{right}_{i}, \text{pick}_{i}, \text{left}_{i}, \text{put}_{i}]$.

The objective is to compute `6` from `{"n": 1, "k": 3, "time": [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model workers in four off-bridge states

At any moment, a worker is in exactly one of these collections:

- `wait_in_left`: ready on the left to cross right and fetch a box;
- `work_in_right`: picking up a box, unavailable until a completion time;
- `wait_in_right`: ready on the right with a box and waiting to cross left;
- `work_in_left`: putting down a returned box, unavailable until completion.

The bridge itself is simulated by advancing current time `cur` whenever one chosen worker crosses. Since crossings are never simultaneous, no separate bridge-occupancy structure is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1, "k": 3, "time": [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Turn worker indices into efficiency ranks

The code sorts `time` by `right_i+left_i` in ascending order. Python's sort is stable, so equal crossing sums remain in original worker-index order.

After sorting:

- a larger sorted index has a larger crossing sum, or the same sum and a larger original index;
- therefore, a larger sorted index means a less efficient worker under the problem's exact ordering.

The simulation can use these sorted indices as efficiency ranks. It does not need original IDs because the answer asks only for elapsed time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The code sorts `time` by `right_i+left_i` in ascending order... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Waiting heaps choose the least efficient worker

Python heaps return the smallest key. Waiting heaps store `-i`, so the most negative key corresponds to the largest sorted index and hence the least efficient waiting worker.

All workers begin on the left, and indices 0 through `k-1` are inserted into `wait_in_left`.

There are separate waiting heaps per side because right-side workers always receive bridge priority over left-side workers.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1, "k": 3, "time": [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Minute-by-minute simulation:** It wastes time :** - **Minute-by-minute simulation:** It wastes time across long pick or put intervals; completion heaps allow jumps.
- **One waiting heap:** It cannot enforce unconditional right-side priority cleanly.
- **Efficiency ties:** Stable sorting preserves original index order, so larger sorted rank remains less efficient.
- **Several simultaneous completions:** Release all before choosing the least efficient waiter.
- **No boxes left to dispatch:** Do not send another left worker even if one waits.
- **Final box:** Return after its left crossing without waiting for put time.
- **One worker:** The same worker cycles through all four stages for every box.
- **Right-side priority:** It is checked before left dispatch whenever both wait.
- **Idle bridge:** Advance to the earliest work completion.
- **Input mutation:** Sorting reorders worker rows into efficiency rank order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log k)$. Sorting `k` workers costs $O(k\log k)$. Each dispatched box causes one left-to-right and one right-to-left crossing. Workers enter and leave work heaps a constant number of times per carried box, and every heap operation costs $O(\log k)$.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
