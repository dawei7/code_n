# Guided Example: Lexicographically Smallest Palindromic Permutation Greater Than Target

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "baba", "target": "abba"}`
- **Required output:** `"baab"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `target`, each of length `n`, consisting of lowercase English letters.

The objective is to compute `"baab"` from `{"s": "baba", "target": "abba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A palindrome is determined by its first half and optional middle

Count every letter in `s`. A palindromic permutation can exist only when at most one character has odd frequency. Every character away from the center must be paired with an identical mirrored character, while an odd-length palindrome may place one unpaired character in the middle.

The source gathers all odd-frequency letter indices. If there are more than one, it returns `""`. Parity of the total length guarantees that the remaining cases are consistent: an even total has zero odd counts, and an odd total has exactly one.

The middle character is the unique odd letter when present. Each first-half count is `frequency[c] // 2`. Once a first half `half` is chosen, the complete palindrome is forced:

`half + middle + half[::-1]`.

Therefore the search only needs to construct the lexicographically smallest feasible first half that leads to a full palindrome strictly greater than `target`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "baba", "target": "abba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Match the target's first half as long as possible

The list `remaining` stores unused first-half letter counts, and `matched` stores indices already chosen equal to `target`. Starting at position zero, the algorithm consumes `target[position]` whenever that half-letter remains available.

Matching is preferable to choosing a larger letter immediately because a longer equal prefix is lexicographically smaller than any candidate that becomes greater earlier. Choosing a smaller letter would make the entire palindrome smaller at the first difference and could never be repaired by mirrored characters later.

The forward scan stops when the next target letter is unavailable or the entire first half has been matched.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The list `remaining` stores unused first-half letter counts,... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle the case where the first half matches completely

If all half positions match, the source builds the forced palindrome and compares the entire string with `target`. This comparison is necessary because when the first halves are identical, the middle or mirrored second half can decide the ordering.

If that palindrome is already strictly greater, it is optimal: no palindrome can have a smaller first half without becoming smaller than the target, and this one uses the exact target half.

If it is equal or smaller, the algorithm must change some position in the first half to a larger letter. It moves `position` back to the final half index and begins backtracking.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"baab"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "baba", "target": "abba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"baab"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate palindromic permutations:** Even hal:** - **Enumerate palindromic permutations:** Even halving the permutation space remains factorial. Frequency-guided pivot construction jumps directly to the smallest successor.
- **Find a next permutation of an arbitrary half:** Sorting the half and repeatedly advancing can traverse many permutations. Matching and backtracking locate the successor relative to `target` directly.
- **Ignore odd frequencies:** More than one odd count makes mirrored pairing impossible, so this feasibility check must precede construction.
- **Compare only the first half:** When halves match, the middle and mirrored portion can determine whether the palindrome is greater; the source correctly compares the full palindrome.
- **Choose an earlier pivot first:** It produces a larger result than a feasible later pivot.
- **Choose a larger-than-necessary replacement:** For a fixed pivot, that immediately worsens the answer. Ascending scanning finds the smallest.
- **Leave the suffix unsorted:** Once the pivot guarantees strict greaterness, ascending suffix order minimizes the result.
- **Even length:** There is no middle character, and every frequency must be even.
- **Odd length:** The unique odd-frequency letter is forced into the center.
- **Length one:** The sole letter is the only palindrome; it is returned only when strictly greater than the one-character target.
- **Exact equality with target:** Equality fails the strict condition and triggers backtracking.
- **Restoring counts:** Every popped match must return to `remaining` or later pivots would search an incomplete multiset.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the string length. Frequency counting, matching, suffix construction, mirroring, and final concatenation each take $O(n)$ time. Backtracking visits at most `n/2` positions, and each replacement search scans 26 letters, a fixed alphabet, so it is $O(n)$. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
