# Guided Example: Print Zero Even Odd

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1}`
- **Required output:** `"01"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a function `printNumber` that can be called with an integer parameter and prints it to the console.

The objective is to compute `"01"` from `{"n": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model the next allowed callback with three permits

The required sequence alternates zero with the integers one through `n`:

`0, 1, 0, 2, 0, 3, ...`.

Three threads own different callback types, so a semaphore for each role represents whether that role may print.

`z` starts with one permit, allowing zero to begin. `o` and `e` start at zero, forcing both number threads to wait. At every later moment, the thread that just printed releases exactly the role that should run next.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The zero thread chooses odd or even

The zero loop has `n` iterations, one for every integer that must follow a zero. It first acquires `z`, consuming the only zero permit, and calls `printNumber(0)`.

Loop index `i` is zero-based, while the next actual integer is `i + 1`. When `i` is even, `i + 1` is odd, so the code releases `o`. When `i` is odd, the next number is even, so it releases `e`.

The release occurs only after the zero callback returns. Therefore, the chosen number cannot print before its preceding zero has completed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The zero loop has `n` iterations, one for every integer that... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The odd and even threads print disjoint sequences

The odd loop visits one, three, five, and so on through `n`. Before each value, it acquires `o`. Only the zero iteration immediately preceding that odd value can supply the permit.

After printing, odd releases `z`, allowing the next zero.

The even loop is symmetric: it visits two, four, six, and so on, waits on `e`, prints its current value, and returns permission to zero.

Because the loops generate their own values, neither number thread needs a shared counter. Their ranges are disjoint and together contain every integer from one through `n` exactly once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"01"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"01"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Condition variable with next-role state:** Sto:** - **Condition variable with next-role state:** Store whether zero, odd, or even should run and notify after each callback. It is flexible but requires guarded wait loops.
- **Locks as gates:** Three one-use handoff locks can implement the same cycle, though semaphores express repeatable permits naturally.
- **Busy-wait flags:** Polling wastes CPU and still requires synchronization for visibility.
- **One shared number counter:** Zero could inspect a shared next integer and wake parity accordingly. The separate ranges here avoid extra shared mutation.
- **`n = 1`:** Zero prints, releases odd, odd prints one, and all loops finish.
- **Even `n`:** The final number callback belongs to the even thread.
- **Odd `n`:** The final number callback belongs to the odd thread.
- **Number thread starts first:** It blocks safely until zero releases its permit.
- **Zero scheduled repeatedly:** It cannot pass its next acquire without a number handoff.
- **Wrong parity thread scheduled:** Its semaphore remains zero, so it cannot print out of turn.
- **Release after callback:** Moving a release before printing would permit overlap and break the completed-output order.
- **Leftover final zero permit:** No zero-loop iteration remains, so it creates no extra output.
- **Callback exception:** Normal completion is assumed for progress.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. There are $n$ zero callbacks and $n$ number callbacks. Every callback is surrounded by a constant number of semaphore operations, so total algorithmic work is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
