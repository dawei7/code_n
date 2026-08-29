# Guided Example: Implement Stack using Queues

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": [["push", 1], ["push", 2], ["top"], ["pop"], ["empty"]]}`
- **Required output:** `[2, 2, false]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

The objective is to compute `[2, 2, false]` from `{"operations": [["push", 1], ["push", 2], ["top"], ["pop"], ["empty"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Make the queue front behave like the stack top

A stack removes the most recently pushed element, while a queue removes the
earliest enqueued element. The exact solution reconciles these opposite orders
by doing the reordering during `push`. Between public operations, queue `q1`
stores every stack element from logical top to logical bottom, in front-to-back
queue order. Queue `q2` is empty and serves as temporary storage for the next
push.

For a logical stack whose top-to-bottom order is `[c, b, a]`, `q1` has front
`c`, followed by `b`, then `a`. With that representation, both `pop` and `top`
can use the queue's front directly in constant time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": [["push", 1], ["push", 2], ["top"], ["pop"], ["empty"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Push the new value before all older values

Suppose `q1` already contains the existing stack in top-to-bottom order. A new
value `x` must become the new top, so the desired new queue order is `x`
followed by all of `q1`'s old contents.

`push` first appends `x` to the back of the empty `q2`. Because it is currently
the only element, it is also at `q2`'s front. The method then repeatedly removes
the front of `q1` with `popleft()` and appends that value to the back of `q2`.
The old elements leave `q1` in their existing top-to-bottom order, so appending
them preserves that relative order behind `x`.

After the transfer, `q2` has exactly the desired sequence and `q1` is empty.
The simultaneous assignment `q1, q2 = q2, q1` swaps the
deque objects. The newly ordered deque becomes the permanent `q1`, and the
emptied old deque becomes scratch `q2` for the next call. Swapping references
avoids copying elements back a second time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace several pushes

Initially both queues are empty. Pushing 1 appends it to `q2`; there is nothing
to transfer, and the swap leaves `q1 = [1]` and `q2 = []`.

Pushing 2 starts with `q2 = [2]`. Moving the one old element appends 1, giving
`q2 = [2, 1]`. After the swap, the front of `q1` is 2, which is the correct
stack top.

Pushing 3 starts with `q2 = [3]` and transfers 2 followed by 1. The resulting
`q1 = [3, 2, 1]` directly represents last-in-first-out order. A pop removes 3,
the next top is 2, and no further reorganization is necessary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 2, false]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": [["push", 1], ["push", 2], ["top"], ["pop"], ["empty"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 2, false]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One-queue rotation:** Append `x` to the only queue, then move each older front element to the back so `x` rotates to the front. It satisfies the follow-up, has the same $O(n)$ push and $O(1)$ pop behavior, and matches the manifest summary rather than the exact source.
- **Cheap push, expensive pop with two queues:** Always append to the main queue in $O(1)$; for pop, transfer all but its last element to the second queue. It shifts the linear cost to removals and may be preferable when pushes greatly outnumber pops.
- **Ordinary list as a stack:** Python could append and pop at the same end in amortized $O(1)$ time, but that would evade the requirement to implement the behavior using queue operations.
- **First push:** With no old values to transfer, the new element becomes the front after a constant-time swap.
- **Pop down to empty:** Removing the sole element leaves `q1` empty and `q2` already empty, so `empty()` returns true.
- **Alternating push and pop:** Every push reorders only the current stack contents; every pop immediately removes the new front. The representation does not depend on batching operations.
- **Repeated values:** Position determines stack order. Equal integers remain separate deque entries and are popped once per push.
- **Maximum operation count:** At most 100 calls are made, but the complexity reasoning remains valid for larger sequences.
- **Invalid empty access:** The reference guarantees it does not occur. A reusable production class might raise a documented exception or return a sentinel, but adding that behavior is outside this contract.
- **Queue-operation restriction:** The implementation uses append-to-back, remove-from-front, front peek, size, and emptiness only. The reference swap exchanges queue identities and does not violate FIFO access.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of elements already in the stack before an operation.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
