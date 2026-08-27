# Guided Example: Break a Palindrome

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"palindrome": "abccba"}`
- **Required output:** `"aaccba"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a palindromic string of lowercase English letters `palindrome`, replace **exactly one** character with any lowercase English letter so that the resulting string is **not** a palindrome and that it is the **lexicographically smallest** one possible.

The objective is to compute `"aaccba"` from `{"palindrome": "abccba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why length one is impossible

Every one-character string is a palindrome, regardless of which lowercase letter it contains. Changing its only character still leaves a one-character string.

Therefore, `n == 1` returns the empty string, as the contract requires when no valid replacement exists.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"palindrome": "abccba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why changing a non-`a` character to `a` is best

`a` is the smallest lowercase letter. At a position containing any other character, replacing it with `a` creates the smallest possible character at that position.

Lexicographic comparison is decided by the first differing position. Consequently, changing an earlier non-`a` character to `a` always beats changing a later position, even if the later replacement is also a decrease.

The loop begins at zero and advances while:

`i < n // 2 and s[i] == "a"`.

It stops at the first non-`a` character in the left half. If it finds one, `s[i] = "a"` performs the greatest lexicographic improvement at the earliest possible location.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `a` is the smallest lowercase letter.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why that change breaks the palindrome

The input is a palindrome, so `s[i]` originally equals its mirror `s[n - 1 - i]`. The loop restricts `i` to the first half, so the mirror is a different position.

Changing only `s[i]` to `a` while its original non-`a` mirror remains unchanged makes that pair unequal. The result is therefore not a palindrome.

The middle character of an odd-length palindrome is deliberately excluded by `i < n // 2`. Changing only the middle character would preserve symmetry and fail to break the palindrome.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"aaccba"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"palindrome": "abccba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"aaccba"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every replacement:** Generating all altern:** - **Try every replacement:** Generating all alternatives and comparing strings is correct but can take quadratic time.
- **Change a right-half non-`a` to `a`:** It breaks the palindrome but is lexicographically worse than changing its earlier left mirror.
- **Change the middle character:** In an odd-length palindrome, this preserves the palindrome and is invalid.
- **Length one:** No replacement can make it non-palindromic, so the answer is empty.
- **All `a` characters:** Change the final one to `b`.
- **Only the middle is non-`a`:** Ignore it and use the final-position fallback.
- **First character is non-`a`:** Changing it to `a` is immediately optimal.
- **Even length:** Every position has a distinct mirror, and the same first-half rule applies.
- **Exactly one replacement:** The fallback changes `a` to `b` rather than leaving the input unchanged.
- **Immutable input:** The list conversion enables one character assignment and explains the linear space bound.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. Converting the immutable string to a list takes $O(n)$ time and space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
