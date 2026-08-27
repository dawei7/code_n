# Guided Example: Reverse Only Letters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "ab-cd"}`
- **Required output:** `"dc-ba"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, reverse the string according to the following rules:

The objective is to compute `"dc-ba"` from `{"s": "ab-cd"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Find the next movable character on each side.

- While `cs[i]` is not alphabetic, increment `i`. Those characters stay untouched in their original positions.
- While `cs[j]` is not alphabetic, decrement `j`.

Both inner loops include `i < j` so indices do not cross or leave the valid range.

When both pointers identify letters and `i < j`, swap them. Then move both pointers inward. Repeating pairs the first letter with the last letter, the second letter with the second-to-last letter, and so on.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "ab-cd"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Invariant Preservation

Ensure every candidate decision satisfies the required constraints.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Ensure every candidate decision satisfies the required const... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"dc-ba"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "ab-cd"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"dc-ba"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Stack of letters:** Extract all letters, then :** - **Stack of letters:** Extract all letters, then scan original positions and pop replacements for letter slots. It is also $O(n)$ time and space but stores a separate letter collection.
- **Reverse extracted letters and rebuild:** This is clear and equivalent, with $O(n)$ extra storage.
- **Reverse the entire string:** It moves punctuation and digits, violating fixed positions.
- **Swap without skipping both sides:** A letter could exchange with a non-letter and move a fixed character.
- **No letters:** Both pointers only skip; the original string is returned unchanged.
- **All letters:** The method becomes ordinary in-place list reversal.
- **One letter:** It remains at its position.
- **Odd number of letters:** The central extracted letter remains unchanged.
- **Adjacent punctuation:** Inner loops skip any number of consecutive fixed characters.
- **Uppercase and lowercase:** Both are alphabetic and participate in the same reversal sequence; case stays attached to each character.
- **Digits and symbols:** They are non-alphabetic and remain fixed.
- **ASCII contract:** Makes Python `isalpha` behavior align with English-letter semantics.
- **Immutable input:** A list is required for swaps; joining produces a new string rather than altering `s`.
- **Pointers meet on punctuation:** No swap occurs, and that fixed character remains untouched.
- **Pointers meet on a letter:** It is the middle letter of the extracted sequence and correctly stays where it is.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. Each pointer moves only inward and visits each position at most once.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
