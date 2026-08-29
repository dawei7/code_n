# Guided Example: Next Palindrome Using Same Digits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": "1221"}`
- **Required output:** `"2112"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a numeric string `num`, representing a very large **palindrome**.

The objective is to compute `"2112"` from `{"num": "1221"}` while avoiding redundant calculations and unnecessary overhead.

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

**A palindrome is determined by its first half.** In an even-length palindrome, the second half is the mirror of the first. In an odd-length palindrome, the center digit stays between those mirrored halves. Because the input is already a palindrome, its digit counts have the required pairing structure. Rearranging the first-half digits and mirroring them generates every palindrome possible from those pairs; for odd length, the unique unpaired center digit remains fixed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": "1221"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

For equal-length digit strings, numeric order is determined by the first position where they differ. That position lies in the first half before its mirrored partner. Therefore, ordering the possible palindromes is exactly the same as lexicographically ordering their first halves. The smallest larger palindrome is obtained by finding the next lexicographic permutation of the first half.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Operate on a mutable character list.** `nums = list(num)` copies the string into individual characters because Python strings cannot be modified in place. The nested helper receives the full list but sets its local `n = len(nums) // 2`. Inside that helper, `n` means the number of characters in the first half, not the full string length.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"2112"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": "1221"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"2112"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate every half permutation:** Sorting all possible palindromes is factorial and infeasible for 100,000 digits.
- **Frequency-based successor construction:** One can locate a pivot and rebuild the minimal suffix from digit counts, but the standard next-permutation reversal is simpler because the suffix is already ordered.
- **Even length:** Every digit belongs to a mirrored pair, and the entire palindrome is determined by the first half.
- **Odd length:** The middle digit is the only unpaired digit and remains unchanged.
- **Length one:** The half has no pivot, so no different palindrome exists and the method returns empty.
- **Length two palindrome:** Its first half has one character, so there is no alternative ordering.
- **Repeated digits:** The strict pivot and successor comparisons skip equal values and produce the next distinct permutation.
- **First half already nonincreasing:** It is the maximum arrangement, so no larger valid palindrome exists.
- **First half nondecreasing:** A next permutation exists unless every half digit is equal.
- **Leading zeros:** All candidates have equal length, so lexicographic comparison still matches their fixed-width digit-string order, though the local description does not separately define leading-zero inputs.
- **Input preservation:** Converting to a list creates a copy; the original string is immutable and unchanged.
- **Suffix slices:** The exact reversal syntax allocates temporary storage even though an in-place two-pointer reversal could avoid that extra slice.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the full string length. Finding the pivot scans at most half the string, finding the successor scans at most half, suffix reversal is linear in the half length, and mirroring plus joining are linear. Total running time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
