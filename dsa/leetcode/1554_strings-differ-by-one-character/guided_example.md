# Guided Example: Strings Differ by One Character

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"dict": ["abcd", "acbd", "aacd"]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a list of strings `dict` where all the strings are of the same length.

The objective is to compute `true` from `{"dict": ["abcd", "acbd", "aacd"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Remove one position to create a comparison signature

Two equal-length strings differ in exactly one position `i` if all characters except position `i` are equal and their characters at `i` are different.

The source replaces one character at a time with the marker `*`. For word `word` and index `i`, it builds:

`word[:i] + "*" + word[i + 1:]`.

This wildcard signature preserves the position of the removed character and every other character.

If two words produce the same signature, they agree at every non-wildcard position. Because the marker occurs at the same location in the identical signatures, the only position where they can differ is that wildcard position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"dict": ["abcd", "acbd", "aacd"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why distinct input strings make the collision exact

Matching signatures prove the two words differ in at most one character. They might have differed in zero characters if duplicate words were allowed.

The contract says all input strings are unique. Therefore, two different words cannot have the same removed character as well as the same remaining characters. A signature collision between processed words consequently proves their wildcard characters differ, giving Hamming distance exactly one.

This distinctness guarantee is an essential part of the proof, not merely a data-cleanliness detail.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Store signatures from earlier words

Set `s` contains every wildcard signature generated for words already processed, plus earlier positions of the current word.

For each new signature `t`, the source first tests membership. If it already exists, a qualifying pair has been found and the method returns true immediately.

Otherwise, it adds `t` and continues. If all word-position combinations finish without a collision, no two strings differ by exactly one character.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"dict": ["abcd", "acbd", "aacd"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Rolling hash per omitted position:** It can build signatures in $O(1)$ per position after preprocessing, realizing expected $O(Q\ell)$ time with collision safeguards.
- **Compare every pair of words:** Direct Hamming comparisons cost $O(Q^2\ell)$.
- **Sort wildcard signatures:** It can detect equal neighbors but requires materializing and sorting all signatures.
- **Duplicate words:** They would create collisions despite Hamming distance zero, but uniqueness excludes them.
- **One-character words:** Every word produces `"*"`; any two distinct one-letter words correctly differ by one.
- **One word only:** No signature can match one from another word, so the result is false.
- **Difference at first position:** Replacing index zero makes matching suffixes collide.
- **Difference at last position:** Replacing the final index makes matching prefixes collide.
- **Two differences:** Replacing one leaves the other mismatch, preventing collision.
- **Wildcard safety:** `*` is outside the lowercase input alphabet and cannot be confused with source data.
- **Equal lengths:** They ensure signatures align position by position and retain the same length.
- **Early return:** The first proven pair is sufficient; no pair identities need to be returned.
- **Hash-set behavior:** Membership is expected constant time after the signature is built, subject to normal hash-table assumptions.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Q\ell^2)$. Let $Q$ be word count and $\ell$ their common length. There are $Q\ell$ loop iterations.
- **Auxiliary Space Complexity:** $O(q\ell)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
