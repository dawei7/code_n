# Guided Example: Words Within Two Edits of Dictionary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"queries": ["word", "note", "ants", "wood"], "dictionary": ["wood", "joke", "moat"]}`
- **Required output:** `["word", "note", "wood"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two string arrays, `queries` and `dictionary`. All words in each array comprise of lowercase English letters and have the same length.

The objective is to compute `["word", "note", "wood"]` from `{"queries": ["word", "note", "ants", "wood"], "dictionary": ["wood", "joke", "moat"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: An edit count is a positional mismatch count

All query and dictionary words have the same length. Changing one character affects exactly one position, so the minimum edits needed to transform query `s` into dictionary word `t` is their Hamming distance: the number of indices where their characters differ.

No insertion, deletion, or reordering is allowed. If there are at most two mismatching positions, changing those query characters makes the words equal. If there are three or more, two edits cannot suffice.

The exact comparison

`sum(a != b for a, b in zip(s, t)) < 3`

computes that mismatch count. Each character comparison produces `true` for a mismatch and `false` for a match; Python sums them as 1 and 0. Testing less than 3 is equivalent to at most two.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"queries": ["word", "note", "ants", "wood"], "dictionary": ["wood", "joke", "moat"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Try dictionary words until one witness is found

The outer loop preserves the order of `queries`. For one query `s`, the inner loop compares it with each dictionary word `t`. As soon as one distance is at most two, the method appends the original query string to `ans` and executes `break`.

Only one dictionary witness is required. Breaking prevents the same query from being appended again if it is close to several dictionary words.

If every dictionary comparison has at least three mismatches, the inner loop ends normally and the query is not appended. The next query is processed independently.

For `"word"` and dictionary word `"wood"`, only the third position differs, so the sum is one and `"word"` is included. For `"note"` and `"joke"`, positions zero and two differ, giving two. For `"ants"`, every dictionary candidate in the example has more than two mismatches, so it is omitted.

An exact dictionary match has distance zero and is valid because “a maximum of two edits” includes performing no edits.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `zip` covers the complete words

`zip(s,t)` stops at the shorter input, which could hide trailing differences for unequal lengths. The contract guarantees every word in both arrays has the same length `n`, so every position is paired exactly once. The implementation relies on that guarantee.


If a query is appended, some dictionary word produced fewer than three positional mismatches. Editing exactly those mismatching characters transforms the query into that dictionary word using zero, one, or two edits, so the inclusion is valid.

If a query is not appended, every dictionary word differs in at least three positions. Each allowed edit can repair at most one of those positions, so no sequence of two edits can make the query equal any dictionary word. Exclusion is therefore valid.

Because queries are considered in their original order and appends happen only in that loop, the returned list retains the required order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["word", "note", "wood"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"queries": ["word", "note", "ants", "wood"], "dictionary": ["wood", "joke", "moat"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["word", "note", "wood"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Manual mismatch counter:** Increment on differing characters and break immediately at three. This matches the manifest wording and improves comparisons that differ early while preserving the same worst-case bound.
- **Trie search with mismatch budget:** Traverse dictionary characters while allowing at most two mismatched edges. It may share work among dictionary words but is more complex for arrays limited to 100 words.
- **Precompute wildcard patterns:** Generate forms with up to two wildcard positions. The number of combinations grows quadratically with word length and requires careful collision handling.
- **Exact match:** Zero edits is within the maximum and must be included.
- **Several matching dictionary words:** The query is appended once because the inner loop breaks after the first witness.
- **Duplicate queries:** Each occurrence is processed and returned in its original position if valid.
- **Duplicate dictionary words:** They do not affect correctness; the first matching occurrence stops the scan.
- **Word length one or two:** Every pair differs in at most the word length, so length-one words always qualify and length-two words qualify against any dictionary word.
- **Equal-length guarantee:** It makes `zip` a complete positional comparison rather than a truncating one.
- **Metadata nuance:** The source short-circuits across dictionary words after success, but it does not stop a single mismatch sum at three.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(QDn)$. Let $Q$ be the number of queries, $D$ the number of dictionary words, and $n$ the common word length. In the worst case, every query is compared with every dictionary word, and each exact `sum` comparison visits all $n$ positions. Time is $O(QDn)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
