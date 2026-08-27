# Guided Example: Calculate Score After Performing Instructions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"instructions": ["jump", "add", "add"], "values": [3, 1, 1]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two arrays, `instructions` and `values`, both of size `n`.

The objective is to compute `0` from `{"instructions": ["jump", "add", "add"], "values": [3, 1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: There is only one execution path

At any in-bounds instruction index `i`, the next state is completely determined:

- `"add"` changes the score by `values[i]` and moves to `i + 1`;
- `"jump"` leaves the score unchanged and moves to `i + values[i]`.

There is no choice, branching search, or optimization decision. The correct method is to simulate this one path until one of the two stopping conditions occurs.

The only complication is that jumps can move backward or stay in place, so execution may enter a cycle. The process must stop before executing an index for a second time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"instructions": ["jump", "add", "add"], "values": [3, 1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track whether each instruction has already executed

The source allocates:

`vis = [false] * n`.

`vis[i]` means instruction index `i` has already been executed. A boolean array is appropriate because valid indices are the dense range zero through `n - 1`.

The loop condition is:

`0 <= i < n and not vis[i]`.

Python evaluates the left side first and short-circuits. Thus `vis[i]` is accessed only when `i` is in bounds. The loop stops safely for both a negative jump target and a target at or beyond `n`.

It also stops when `vis[i]` is already true. Since the body is not entered, the revisited instruction is not executed again, exactly matching the specification.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source allocates:

`vis = [false] * n`.

`vis[i]` means ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark before applying the instruction

At the start of each loop body, the source performs:

`vis[i] = true`.

Only then does it update the score or instruction pointer. Marking before movement is important for a self-jump. If `instructions[0] = "jump"` and `values[0] = 0`, execution stays at index zero. On the next condition check, `vis[0]` is true, so the process ends. If marking were delayed until after reaching a different index, this case could loop forever.

More generally, every executed index is recorded before any transition that may eventually return to it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"instructions": ["jump", "add", "add"], "values": [3, 1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Hash set of visited indices:** This matches th:** - **Hash set of visited indices:** This matches the manifest wording and can store only reached indices. A boolean list is faster and simpler for the dense known index range, though it always allocates `O(n)` space.
- **Floyd cycle detection:** Two pointers could detect cycles with constant memory, but score accumulation and the rule to stop at the first repeated execution make bookkeeping more awkward. The direct visited array is clearer.
- **Recursive simulation:** It risks recursion-depth failure for a path of length `10^5` and provides no benefit over the loop.
- **Execute before checking visited:** That would incorrectly apply a revisited add instruction one extra time. The loop condition must reject the index first.
- **Mark after moving:** A zero jump could repeat forever. Mark the current instruction before computing its successor.
- **Jump to n:** Index `n` is out of bounds, so execution stops without indexing either input array there.
- **Jump below zero:** Negative indices must be treated as out of bounds rather than Python-style indexing from the end; the explicit `0 <= i` condition prevents accidental negative indexing.
- **Zero jump:** The current index becomes the next attempted index, is recognized as visited, and is not executed twice.
- **Backward cycle of several indices:** Every member executes once; the first attempted repeat ends the process.
- **Negative add value:** It decreases `ans` and then moves to the next index. Scores need not be nonnegative.
- **Add at the last index:** The value is included, then `i` becomes `n` and the process stops.
- **First instruction exits immediately:** A jump outside the array returns the initial score zero after executing only that jump.
- **Instruction string test:** Checking the first letter is safe only because the contract restricts values to `"add"` and `"jump"`.
- **Equal array lengths:** The source takes `n = len(values)` and indexes `instructions` with the same `i`. Correctness relies on the guaranteed equal sizes.
- **No mutation:** The source changes neither input array; all execution state lives in `i`, `ans`, and `vis`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the instruction count. Each valid index enters the loop at most once because it is marked on entry and any revisit stops before the body. Every iteration performs constant work: a few comparisons, one boolean assignment, one instruction check, and one arithmetic transition. Total time is `O(n)` in the worst case.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
