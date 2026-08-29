# Guided Example: Exclusive Time of Functions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2, "logs": ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]}`
- **Required output:** `[3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

On a **single-threaded** CPU, we execute a program containing `n` functions. Each function has a unique ID between 0 and $n - 1$.

The objective is to compute `[3, 4]` from `{"n": 2, "logs": ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Trace the first sample.

- `0:start:0` pushes 0 and sets `pre = 0`.
- `1:start:2` credits function 0 with `2 - 0 = 2` units, covering times 0 and 1. It pushes 1 and sets `pre = 2`.
- `1:end:5` credits function 1 with `5 - 2 + 1 = 4` units, covering 2 through 5. It pops 1 and sets `pre = 6`.
- `0:end:6` credits resumed function 0 with `6 - 6 + 1 = 1` unit.

Totals are 3 for function 0 and 4 for function 1.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2, "logs": ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Invariant Preservation

Ensure every candidate decision satisfies the required constraints.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2, "logs": ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Store start times in stack frames:** Push each function with its effective start and subtract child durations on return. It works but needs more per-frame bookkeeping than the global segment boundary.
- **Event-by-event segment accounting:** The exact approach is preferable because each interval is credited immediately to the current stack top.
- **Start and end at the same timestamp:** The call executes for one unit; `cur - pre + 1` correctly returns 1.
- **Nested calls:** The parent is credited before the child starts and again only after the child ends, so child time is excluded.
- **Recursive calls:** Duplicate IDs on the stack are valid and their separate intervals accumulate into one answer entry.
- **Adjacent events:** Setting `pre = cur + 1` after an end prevents the inclusive end unit from being counted again.
- **Top-level gaps:** Valid program logs describe execution periods; when the stack is empty, no function receives time before the next start.
- **Well-formed nesting:** The algorithm trusts that every end corresponds to the current stack top, as guaranteed by call-stack logs.
- **Inclusive end timestamp:** Omitting `+ 1` is the most common off-by-one error and undercounts every completed call.
- **Large timestamps:** Only differences matter; the algorithm does not iterate through individual time units.
- **Functions never called:** Their initialized answer entries remain zero.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L$ be the number of log entries and $D$ the maximum active call depth. Each log is split, parsed, and processed once. Each start pushes one ID, and its matching end pops it once. Total time is $O(L)$.
- **Auxiliary Space Complexity:** $O(n+D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
