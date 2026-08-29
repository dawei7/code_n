# Guided Example: Long Pressed Name

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"name": "alex", "typed": "aaleex"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Your friend is typing his `name` into a keyboard. Sometimes, when typing a character `c`, the key might get *long pressed*, and the character will be typed 1 or more times.

The objective is to compute `true` from `{"name": "alex", "typed": "aaleex"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

Long pressing can increase the number of consecutive copies of a character, but it cannot change the order of distinct character runs, remove a required occurrence, or introduce a new run character. The exact solution compares `name` and `typed` one run at a time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"name": "alex", "typed": "aaleex"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

A run is a maximal consecutive block of the same character. For example, `alex` has runs `a`, `l`, `e`, `x`, while `aaleex` has `aa`, `l`, `ee`, `x`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Pointers `i` and `j` mark the beginnings of the next unprocessed runs in `name` and `typed`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"name": "alex", "typed": "aaleex"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Character-by-character greedy pointer:** Match name characters directly and allow typed repeats of the previous matched character. This also works but needs careful handling of leading and trailing extras.
- **Materialize run-length arrays:** Compare character/count pairs after grouping. It is conceptually clear but uses $O(m+t)$ extra space.
- **Only compare character sets:** Sets lose order and multiplicity and are insufficient.
- **Typed shorter than name:** It cannot contain enough required presses and eventually fails a run length or exhaustion test.
- **No long presses:** Identical strings pass with equal run lengths.
- **Every run extended:** All typed counts may be larger and still pass.
- **Extra final run:** Joint exhaustion rejects it.
- **Missing final run:** Joint exhaustion rejects it.
- **Same total length but different run structure:** A character mismatch rejects it even if counts coincidentally sum equally.
- **Single-character name:** Typed must contain only that character and at least one copy.
- **Repeated intended character:** The typed run must be at least the full required multiplicity.
- **Lowercase contract:** Direct character equality has no case or locale complication.
- **Run order:** Long pressing cannot reorder runs; advancing both pointers together enforces identical order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m+t)$. Let $m=\lvert\texttt{name}\rvert$ and $t=\lvert\texttt{typed}\rvert$. Each pointer and its run-end helper moves only forward; every character is examined a constant number of times.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
