# Guided Example: Print in Order

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3]}`
- **Required output:** `"firstsecondthird"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Suppose we have a class:

The objective is to compute `"firstsecondthird"` from `{"nums": [1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn ordering requirements into two closed gates

Three threads may begin in any scheduler order, but the callbacks must complete in the sequence first, second, third. There are two dependencies:

- `second` must wait until `first` has finished printing.
- `third` must wait until `second` has finished printing.

The class represents these dependencies with locks `l2` and `l3`. Both are acquired during construction, before worker methods run, so both later stages begin behind closed gates.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Let the first stage run immediately

`first` does not acquire a gate. Regardless of when its thread is scheduled, it can call `printFirst`.

Only after that callback returns does it call `l2.release()`. This placement is essential. Releasing before the callback would allow the second thread to print while the first callback had not completed, breaking the required output order.

Releasing `l2` opens exactly the gate on which `second` waits.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `first` does not acquire a gate.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Block the second stage until first completes

`second` begins with `l2.acquire()`. Because the constructor already holds that lock, a second thread scheduled too early blocks rather than printing.

After `first` releases the lock, the acquire succeeds. The second callback runs, and only after it returns does `second` release `l3`. This establishes the next happens-before relationship.

The method does not release `l2` afterward. Each of the three methods is called exactly once, so that gate has no future consumer and does not need to be reusable.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"firstsecondthird"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"firstsecondthird"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Semaphores:** Initialize the second and third :** - **Semaphores:** Initialize the second and third stage permits to zero, then release them in sequence. This expresses the same two gates and does not rely on lock ownership semantics.
- **Events:** One event can signal completion of first and another completion of second. Events are readable for one-way, one-use notifications.
- **Condition variable with stage counter:** Wait until a shared stage reaches the required number, update it, and notify. It is more general but more code for three fixed stages.
- **Busy waiting on flags:** Repeatedly checking shared booleans wastes CPU and still needs memory-visibility synchronization.
- **Calling methods in apparent input order:** Incorrect because operating-system scheduling, not input presentation, determines actual execution.
- **Third starts first:** It blocks on `l3` until both preceding callbacks finish.
- **Second starts first:** It blocks on `l2` until first finishes.
- **First starts last:** The other two wait safely; once first runs, the gates open in sequence.
- **Release after callback:** Moving either release before its print callback would permit overlapping or reversed output.
- **Exactly one call per method:** The locks are one-use gates and are not reset for repeated cycles.
- **Callback exception:** It can prevent the next release and cause a wait; the contract assumes normal callbacks.
- **No final unlock:** Nothing follows third, so leaving `l3` acquired after the successful wait is harmless.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The repository classifies this package as bounded concurrency: exactly three calls and all six launch permutations form a fixed legal domain. Each method performs one callback and at most one acquire or release, so total algorithmic work is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
