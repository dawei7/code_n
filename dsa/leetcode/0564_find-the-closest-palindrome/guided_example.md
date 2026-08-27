# Guided Example: Find the Closest Palindrome

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": "123"}`
- **Required output:** `"121"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `n` representing an integer, return *the closest integer (not including itself), which is a palindrome*. If there is a tie, return ***the smaller one***.

The objective is to compute `"121"` from `{"n": "123"}` while avoiding redundant calculations and unnecessary overhead.

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

The nearest palindrome does not require searching outward integer by integer. For a number with `l` digits, any nearby palindrome is determined almost completely by a prefix of length `ceil(l/2)`: mirror that prefix to form the remaining digits.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": "123"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution creates a small candidate set, removes the input itself, and chooses the candidate with smallest absolute difference, breaking ties toward the smaller integer.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution creates a small candidate set, removes the inpu... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Include candidates that change digit length.** The set begins with:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"121"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": "123"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"121"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Search outward one integer at a time:** The ne:** - **Search outward one integer at a time:** The nearest palindrome can be far away, making this needlessly slow.
- **Generate every palindrome of the digit length:** There are exponentially many prefixes; only three nearby ones matter.
- **Mirror only the unchanged prefix:** It fails around values where the nearest palindrome requires a middle carry or borrow.
- **Omit digit-length boundaries:** Inputs near powers of ten or all-nines values can be answered incorrectly.
- **Input already palindrome:** It is explicitly removed, so the next closest palindrome is chosen.
- **Power of ten:** The lower all-nines candidate is essential.
- **All nines:** The upper `10^l + 1` candidate is essential.
- **One digit:** Zero and neighboring one-digit palindromes are compared normally.
- **Odd length:** The middle prefix digit is not mirrored twice.
- **Even length:** The complete half is mirrored.
- **Equal distances:** The smaller candidate wins.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $d$ be the number of digits. Extracting and parsing the prefix, mirroring a constant number of candidates, and formatting the result each process $O(d)$ digits. Time is $O(d)$.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
