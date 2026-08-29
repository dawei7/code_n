# Guided Example: Implement Queue using Stacks

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["empty", "push", "pop", "empty"], "values": [null, 7, null, null]}`
- **Required output:** `[true, null, 7, true]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

The objective is to compute `[true, null, 7, true]` from `{"operations": ["empty", "push", "pop", "empty"], "values": [null, 7, null, null]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Two reversals reconcile stack order with queue order

A queue must return the oldest element, but a stack exposes the newest element.
The exact solution separates queued values into two phases:

- `stk1` is the incoming stack. Every `push` appends the newest value here.
- `stk2` is the outgoing stack. Its top, `stk2[-1]`, is the oldest value still
  in the queue and therefore the queue front.

Values enter `stk1` in arrival order, with the newest on top. When `stk2` needs
values, repeatedly popping `stk1` and appending to `stk2` reverses that order.
The value that arrived earliest was at the bottom of `stk1`, so it moves last
and ends on top of `stk2`, ready to leave first.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["empty", "push", "pop", "empty"], "values": [null, 7, null, null]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Push never performs a transfer

`push(x)` simply executes `stk1.append(x)`. This is a standard push-to-top
stack operation and takes constant time. The method does not try to place `x`
directly behind values already in `stk2`; the division between stacks already
encodes the needed chronology.

If `stk2` contains elements, all of them were pushed before every value still
in `stk1`. They must therefore be popped first. New pushes can accumulate in
`stk1` without disturbing the established front order in `stk2`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Transfer only when the outgoing stack is empty

Both `pop` and `peek` call `move`. That helper first checks `if not stk2`.
Only when no already-reversed values remain does it move every element from
`stk1` to `stk2`.

Avoiding a transfer while `stk2` is nonempty is essential. Suppose older values
are already waiting in `stk2` and newer pushes are in `stk1`. Moving those new
values onto `stk2` would place them above the older front and violate FIFO
order. Waiting until `stk2` empties ensures one complete older batch is served
before the next batch is reversed.

After a transfer, `stk1` is empty. The oldest value in that batch is at
`stk2[-1]`, the next-oldest is directly below it in pop order, and the newest is
at the bottom. Repeated pops naturally produce arrival order without further
movement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[true, null, 7, true]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["empty", "push", "pop", "empty"], "values": [null, 7, null, null]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[true, null, 7, true]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Expensive push, cheap pop:** Move all existing values around every new value so one stack's top is always the queue front. Pop becomes worst-case $O(1)$, but each push costs $O(n)$ and a long push sequence becomes quadratic.
- **One stack plus recursion:** Temporarily pop values recursively to reach the oldest element, then restore newer ones. It uses call-stack space, repeats work across removals, and is less efficient than two persistent phases.
- **Ordinary deque:** It directly supports queue operations in constant time, but using it would avoid the exercise's two-stack constraint.
- **First pop after many pushes:** This is the expensive operation that transfers the whole incoming batch, but later pops from that batch are constant time.
- **Peek before pop:** A transfer performed by `peek` is useful preparation, not wasted work; the following `pop` reuses the outgoing order.
- **Push while `stk2` is nonempty:** The new value waits in `stk1` because every outgoing value is older and must leave first.
- **Pop the last outgoing value while incoming values wait:** That pop returns the correct older value. The next `pop` or `peek` triggers transfer of the waiting newer batch.
- **Repeated values:** Stack positions preserve arrival order even when values are equal; each pushed occurrence is stored and removed separately.
- **Valid-access guarantee:** Empty `pop` and `peek` do not occur. A production queue might raise an explicit exception, but the challenge requires no additional policy.
- **Stack-operation restriction:** Python list `append`, `pop`, `[-1]`, and truth testing correspond to push, pop, top, and empty checks. No bottom or interior element is accessed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. `push` and `empty` take $O(1)$ time. A particular `pop` or `peek` can take
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
