# Guided Example: Minimum Number of Moves to Make Palindrome

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aabb"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting only of lowercase English letters.

The objective is to compute `2` from `{"s": "aabb"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search from the right boundary inward

The loop examines `k` from `j` down to `i + 1`. The first equal character found is therefore the rightmost available partner for `cs[i]`.

If a match exists at `k`, the inner while-loop swaps it rightward one position at a time until it reaches `j`. This costs exactly `j - k` adjacent swaps.

Afterward, `cs[i] == cs[j]`, so those positions form a correct palindrome pair. The right pointer decreases, the left pointer later increases, and that fixed pair is never disturbed again.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aabb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why choose the rightmost matching occurrence

The left-boundary character must eventually be paired with an equal character at the right boundary unless it is the unique center character.

Among all matching occurrences in the active interval, the rightmost one requires the fewest swaps to reach `j`. Choosing an earlier equal occurrence would cross at least as many intervening characters.

Pairing the current leftmost occurrence with the rightmost available equal occurrence also avoids unnecessary crossings between equal-character pairs. An exchange argument can replace any optimal solution's farther-left partner with the rightmost partner without increasing swaps; the characters between them shift no more than before.

Thus the greedy pair can be fixed while preserving the existence of an optimal completion inside the remaining boundaries.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Realize displacement with actual adjacent swaps

The assignment

`cs[k], cs[k + 1] = cs[k + 1], cs[k]`

moves the chosen match one step right and shifts the crossed character one step left. Incrementing `k` repeats this until the match occupies `j`.

Each iteration corresponds to one allowed move, so increasing `ans` once per swap gives an exact cost rather than an abstract distance estimate.

The list mutation is important for later searches: all unpaired characters now appear in the relative order produced by those swaps.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aabb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Standard two-ended greedy:** Search for a match to the left character; if none exists, swap that character one step toward the center and retry. It is easier to visualize but may perform center moves explicitly rather than charging them at once.
- **Build a target palindrome then count inversions:** Choose a pairing and use a Fenwick tree to count adjacent swaps. This can improve asymptotic performance but makes correct duplicate pairing more involved.
- **Breadth-first search over strings:** It guarantees a minimum only for tiny inputs; the permutation state space is far too large for length 2000.
- **Already a palindrome:** Every boundary finds its match at `j`, so no swaps are added.
- **Length one:** The loop never runs and the answer is zero.
- **Even length:** Every character frequency is even, so each active left character finds a partner.
- **Odd length:** Exactly one odd-frequency character may require the center shortcut.
- **Repeated equal characters:** Searching from the right chooses the match with minimum boundary displacement.
- **Match already at right boundary:** The bubbling loop performs zero swaps before shrinking both sides.
- **No-match shortcut:** The source counts center movement but intentionally leaves the list unchanged outside the future active left boundary.
- **Palindrome feasibility guarantee:** It rules out two different unmatched character types, which the shortcut would not handle.
- **Adjacent-swap accounting:** Each physical bubble increments `ans` once, exactly matching the allowed operation.
- **Input preservation:** The immutable string remains unchanged; mutations occur in the copied list `cs`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the string length. For each left boundary, the backward search may scan $O(n)$ positions, and bubbling a match may also perform $O(n)$ swaps. Across at most $O(n)$ boundary iterations, total time is $O(n^2)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
