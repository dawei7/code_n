# Guided Example: Generate Fibonacci Sequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"callCount": 5}`
- **Required output:** `[0, 1, 1, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a generator function that returns a generator object which yields the **fibonacci sequence**.

The objective is to compute `[0, 1, 1, 2, 3]` from `{"callCount": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A generator produces values only when requested

Calling `fibGenerator()` returns a generator object. The function body does not run to completion and does not create a finite Fibonacci array.

Each call to `gen.next()` resumes execution until the next `yield`, returns that yielded value, and suspends the generator again with its local state preserved.

This lazy behavior is ideal for an infinite sequence: callers can request any finite prefix without computing unused future values.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"callCount": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store only the two values needed by the recurrence

The Fibonacci recurrence is:

$$
F_0=0,\qquad F_1=1,\qquad F_{r+2}=F_r+F_{r+1}.
$$

Variables `previous` and `current` hold two consecutive values. Initially:

$$
\texttt{previous}=F_0=0,\qquad
\texttt{current}=F_1=1.
$$

To produce the next sequence value, the generator yields `previous`. To advance the state, it replaces the pair with:

$$
(\texttt{current},\texttt{previous}+\texttt{current}).
$$

No earlier Fibonacci number is needed once the newest pair is known.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The Fibonacci recurrence is:

$$
F_0=0,\qquad F_1=1,\qquad F... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand suspension around `yield`

The loop body is:

1. `yield previous`;
2. update both variables.

On the first `next()` call, execution initializes the variables, enters the loop, and suspends at `yield previous` with value zero. The update has not happened yet.

On the second `next()` call, execution resumes immediately after that yield, updates the pair to $(1,1)$, loops, and yields one.

This resume-then-advance behavior continues for every call.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1, 1, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"callCount": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1, 1, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Precomputed array:** Simple for a fixed limit :** - **Precomputed array:** Simple for a fixed limit but uses $O(q)$ memory and is not naturally infinite.
- **Recursive Fibonacci:** Recomputes overlapping subproblems and can take exponential time per value.
- **Memoized recursion:** Avoids recomputation but stores all prior values, unnecessary for sequential generation.
- **Zero requested calls:** No sequence value is produced.
- **First two values:** Initialization must be zero and one in that order.
- **Simultaneous update:** It preserves both old values for the recurrence.
- **Multiple generators:** Each object retains independent state.
- **Infinite loop:** Safe because `yield` suspends on every iteration and the caller controls demand.
- **Large indices:** Ordinary Number precision eventually fails, though not within 50 calls.
- **Generator completion:** This implementation intentionally never returns `done: true` under continued requests.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Each resumed iteration performs one addition, one pair assignment, and one yield, so amortized time per produced Fibonacci value is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
