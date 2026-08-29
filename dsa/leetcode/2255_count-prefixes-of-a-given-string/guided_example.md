# Guided Example: Count Prefixes of a Given String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["a", "b", "c", "ab", "bc", "abc"], "s": "abc"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string array `words` and a string `s`, where $\text{words}[i]$ and `s` comprise only of **lowercase English letters**.

The objective is to compute `3` from `{"words": ["a", "b", "c", "ab", "bc", "abc"], "s": "abc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Test the definition directly

A word `w` is a prefix of `s` when the first `len(w)` characters of `s` equal `w`. Python's `s.startswith(w)` performs exactly this test.

The solution evaluates that predicate for every occurrence in `words`:

`sum(s.startswith(w) for w in words)`.

The generator produces one Boolean per list position. Python treats `true` as one and `false` as zero when summing, so the result is the number of matching word occurrences.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["a", "b", "c", "ab", "bc", "abc"], "s": "abc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why duplicates are counted separately

The method iterates the list, not a set. If `"a"` appears twice and is a prefix, `startswith` returns true twice and the sum gains two.

This matches the problem's explicit requirement that repeated equal strings count each time. Deduplicating `words` would be incorrect.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What `startswith` checks

For a word of length `k`, the predicate conceptually compares:

`s[0:k] == w`.

It does not search later positions. A word occurring inside `s` but not at index zero returns false.

If `w` is longer than `s`, it cannot be a prefix and `startswith` returns false. No explicit length condition is needed.

If `w == s`, every character matches and it is a valid prefix. A prefix is allowed to be the whole target string.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["a", "b", "c", "ab", "bc", "abc"], "s": "abc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Slice the target manually:** `s[:len(w)] == w` is correct, but may allocate a substring; `startswith` expresses the intent directly.
- **Build a trie from words:** It adds nodes and setup for a single short target and is unnecessary here.
- **Convert words to a set:** It would lose duplicate occurrences that must be counted separately.
- **Use substring membership:** `w in s` accepts occurrences away from the beginning and is incorrect.
- **Use `s.endswith(w)`:** That tests the opposite boundary.
- **Word equals `s`:** It is a valid prefix and counts.
- **Word longer than `s`:** It returns false.
- **Repeated qualifying word:** Every occurrence contributes one.
- **Repeated non-prefix word:** Every occurrence contributes zero.
- **Mismatch at first character:** Comparison stops immediately and returns false.
- **Mismatch later:** A partially matching beginning is still not a prefix unless the entire word matches.
- **Single-character target:** Only matching one-character words can qualify because input words are nonempty.
- **Input ordering:** It does not affect the numeric count.
- **Lowercase guarantee:** No case folding or locale behavior is needed.
- **Many words sharing a long prefix:** Each is still checked independently because every list occurrence contributes separately.
- **Empty words:** The constraints exclude them, so the special convention that an empty string is a prefix never enters the method's inputs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
