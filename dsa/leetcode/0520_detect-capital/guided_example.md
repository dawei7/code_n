# Guided Example: Detect Capital

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "USA"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We define the usage of capitals in a word to be right when one of the following cases holds:

The objective is to compute `true` from `{"word": "USA"}` while avoiding redundant calculations and unnecessary overhead.

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

There are exactly three accepted capitalization patterns:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "USA"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- every letter is uppercase;
- every letter is lowercase;
- the first letter alone is uppercase.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Instead of checking those patterns with three separate scans, the solution summarizes the entire word by counting its uppercase letters.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "USA"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Inspect the first two characters:** For length at least two, their cases determine whether all later characters must be uppercase or lowercase. This also runs in $O(n)$ time but needs a separate one-character branch.
- **Three direct pattern scans:** Check all-uppercase, all-lowercase, and title-style forms separately. It remains $O(n)$ because three is constant, but repeats traversal logic.
- **Built-in whole-string methods:** `word.isupper()`, `word.islower()`, and `word.istitle()` can express the three cases compactly, though their exact language semantics should be understood.
- **Regular expression:** A full match against uppercase, lowercase, or first-capital patterns works, but introduces regex machinery for a simple linear property.
- **Exactly one capital in the middle:** `cnt == 1` alone is insufficient; checking `word[0]` rejects this invalid arrangement.
- **Several capitals but not all:** The count is between one and `n` and cannot satisfy an accepted signature.
- **Single lowercase letter:** Its uppercase count is zero, so it is valid.
- **Single uppercase letter:** Its uppercase count equals the length, so it is valid.
- **All-uppercase and one character:** More than one condition may describe it, but logical OR still produces the correct boolean result.
- **Nonempty guarantee:** It makes the direct first-character check safe.
- **English-letter guarantee:** It ensures every character is classified as either lowercase or uppercase; digits or punctuation would require more careful semantics.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `word`. The uppercase-count generator examines every character once. Each `isupper` test and boolean addition is constant work for the constrained English letters, so the running time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
