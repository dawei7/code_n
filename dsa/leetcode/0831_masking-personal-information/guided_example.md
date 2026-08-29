# Guided Example: Masking Personal Information

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "LeetCode@LeetCode.com"}`
- **Required output:** `"l*****e@leetcode.com"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a personal information string `s`, representing either an **email address** or a **phone number**. Return *the **masked** personal information using the below rules*.

The objective is to compute `"l*****e@leetcode.com"` from `{"s": "LeetCode@LeetCode.com"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First decide which of the two valid formats was supplied

The input is guaranteed to be either a valid email address or a valid phone number. A valid email begins with a letter because its name contains only letters. A valid phone number begins with either a digit or one of its permitted separation characters, never a letter.

The condition `s[0].isalpha()` therefore distinguishes the two formats without searching the entire string for `@`. Once the branch is known, the formats have different masking rules and can be handled independently.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "LeetCode@LeetCode.com"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Email: normalize the complete address first

The email branch performs `s = s.lower()`. This converts uppercase letters in both the name and domain to lowercase in one pass. Symbols such as `@` and `.` are unchanged.

The masked name must contain:

- its original first letter;
- exactly five asterisks, regardless of original name length;
- its original last letter.

Everything beginning with `@`, including the normalized domain, must then remain.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the suffix slice begins one character before `@`

`s.find('@')` returns the index of the one `@` symbol. The last character of the email name is located one position earlier. Therefore,

`s[s.find('@') - 1:]`

contains the name's last character, the `@` symbol, and the complete domain.

Prepending `s[0] + '*****'` yields:

`first-name-letter + five asterisks + last-name-letter + @ + domain`.

For `"LeetCode@LeetCode.com"`, lowercasing gives `"leetcode@leetcode.com"`. The first name letter is `l`, and the slice from one character before `@` is `"e@leetcode.com"`. The result is `"l*****e@leetcode.com"`.

For the minimum two-letter name `"ab"`, the first and last letters are still distinct positions. The rule does not preserve an empty middle; it always inserts five asterisks, producing `"a*****b"` before the domain.

The validity guarantee ensures the name has at least two letters, so the slice position before `@` is a valid name character.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"l*****e@leetcode.com"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "LeetCode@LeetCode.com"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"l*****e@leetcode.com"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Detect email by searching for `@`:** This is also correct under the input contract. Testing the first character avoids an extra conceptual format scan.
- **Regular expressions:** They can validate and capture parts, but validation is guaranteed and direct slicing/filtering is clearer.
- **Email name of length two:** It still receives exactly five asterisks between its first and last letters.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(s)`. In the email branch, lowercasing and suffix slicing each copy at most `O(n)` characters, and the returned string has `O(n)` length. Time and output space are `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
