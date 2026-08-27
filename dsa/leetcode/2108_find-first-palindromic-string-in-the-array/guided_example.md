# Guided Example: Find First Palindromic String in the Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["abc", "car", "ada", "racecar", "cool"]}`
- **Required output:** `"ada"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `words`, return *the first **palindromic** string in the array*. If there is no such string, return *an **empty string** *`""`.

The objective is to compute `"ada"` from `{"words": ["abc", "car", "ada", "racecar", "cool"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Preserve array order and stop at the first match

The word “first” makes the input order essential. The source creates a generator that examines `words` from left to right:

`(w for w in words if w == w[::-1])`.

It yields only words that equal their reversed form. `next(..., "")` requests the first yielded word and uses the empty string as a default if the generator yields nothing.

Because `next` is lazy, later words are not checked after the first palindrome is found. This is important in an example containing both `"ada"` and the later `"racecar"`: the method returns `"ada"` immediately.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["abc", "car", "ada", "racecar", "cool"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why reversal tests palindromicity

`w[::-1]` is Python slicing with a step of -1, producing the characters of `w` in reverse order.

A string is palindromic exactly when its forward sequence equals its backward sequence. Therefore,

`w == w[::-1]`

is true if and only if `w` is a palindrome.

Odd-length strings naturally compare the center character with itself. Even-length strings have no unique center, but complete reversal still compares every mirrored pair. One-character strings always pass.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `w[::-1]` is Python slicing with a step of -1, producing the... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand the generator and default

The parenthesized expression is a generator, not a precomputed list. It requests one word, constructs and compares that word's reverse, then proceeds only if necessary.

`next(generator, "")` has two outcomes:

- if a palindromic word is yielded, return that original word;
- if the generator is exhausted, return `""`.

The returned value is `w` from the input, not the reversed copy. For a palindrome they have equal text, but returning the original makes the intent explicit.

The constraints say input words are nonempty, so the default empty string cannot be confused with a valid palindromic input word.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"ada"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["abc", "car", "ada", "racecar", "cool"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"ada"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two mirrored pointers:** Compare characters at:** - **Two mirrored pointers:** Compare characters at the two ends while moving inward. This realizes the manifest's constant-space claim and can stop a word check at its first mismatch.
- **Build a list of all palindromes:** It does unnecessary work and storage after the first match. The lazy generator stops immediately.
- **Sort the words:** This destroys the input-order meaning of “first” and is incorrect.
- **First word is palindromic:** Only one word is examined.
- **No palindrome:** Generator exhaustion returns the explicit empty-string default.
- **One-character word:** It equals its reverse and is always palindromic.
- **Even-length palindrome:** Complete reversal handles it without a special center case.
- **Repeated words:** The earliest palindromic occurrence is returned.
- **Nonempty word guarantee:** It keeps `""` reserved for the no-result case.
- **Reversed-copy allocation:** `w[::-1]` is concise but not constant-space.
- **Input preservation:** Strings and the array are only read.
- **Lazy evaluation:** Words after the first palindrome incur no time or reverse allocation.
- **Long non-palindromic word:** Its full reverse is still allocated before equality can reject it, which is why peak space depends on word length.
- **Return identity versus text:** The generator yields the original `w` value from `words`, not the temporary reverse.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
