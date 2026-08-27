# Guided Example: Palindromic Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abc"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return *the number of **palindromic substrings** in it*.

The objective is to compute `3` from `{"s": "abc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count occurrences, not distinct text values

The task asks how many substrings are palindromes. Two equal strings at different index ranges count as two substrings because their positions differ. The algorithm therefore counts every palindromic interval when it discovers it; it does not put palindrome text into a set.

A palindrome reads the same from both directions. Starting at its middle, characters occur in matching pairs at equal distances to the left and right. This symmetry suggests choosing every possible center and expanding outward while the characters match.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: There are two kinds of centers

An odd-length palindrome has one character at its center. For example, `"racecar"` is centered on `e`. An even-length palindrome has its center between two adjacent characters. For example, `"abba"` is centered between the two `b` characters.

For a string of length `n`, there are:

- `n` single-character centers;
- `n - 1` gaps between adjacent characters.

That gives `2n - 1` possible centers in total. Every nonempty palindrome has exactly one of them.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An odd-length palindrome has one character at its center.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How one loop index represents both center types

The exact solution loops with `k` from zero through `2 * n - 2`. It converts `k` into initial left and right indices:

`i = k // 2`

`j = (k + 1) // 2`

When `k` is even, both formulas produce the same index. For example, `k = 4` gives `i = 2` and `j = 2`. This represents the odd-length center at character two.

When `k` is odd, `j` is exactly one greater than `i`. For example, `k = 3` gives `i = 1` and `j = 2`. This represents the even-length center between characters one and two.

As `k` increases, these formulas alternate between a character center and the following gap. They enumerate every valid center exactly once without needing two separate loops.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Dynamic programming table:** Record whether `s:** - **Dynamic programming table:** Record whether `s[i:j + 1]` is a palindrome using matching endpoints and the state for the inner interval. It takes `O(N^2)` time and `O(N^2)` space, while center expansion reaches the same time with constant extra space.
- **- **Check every substring independently:** There a:** - **Check every substring independently:** There are quadratically many substrings, and scanning each one for symmetry adds another linear factor, producing `O(N^3)` time.
- **- **Manacher's algorithm:** It reuses symmetry inf:** - **Manacher's algorithm:** It reuses symmetry information between nearby centers and can count palindromes in `O(N)` time. It is asymptotically faster but substantially more intricate; center expansion is the intended clear optimal variant for the package's stated `O(N^2)` bound.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Let `N` be the string length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
