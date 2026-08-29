# Guided Example: Occurrences After Bigram

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"text": "alice is a good girl she is a good student", "first": "a", "second": "good"}`
- **Required output:** `["girl", "student"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `first` and `second`, consider occurrences in some text of the form `"first second third"`, where `second` comes immediately after `first`, and `third` comes immediately after `second`.

The objective is to compute `["girl", "student"]` from `{"text": "alice is a good girl she is a good student", "first": "a", "second": "good"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert the text into a word sequence

The relationship in the problem is about consecutive words, not arbitrary character positions. The solution begins:



`split` without an explicit delimiter separates on whitespace and returns the words in their original order. The contract guarantees single spaces with no leading or trailing spaces, so this produces exactly the intended tokens.

For:



the list is:



Once tokenized, an occurrence of `"first second third"` is simply three adjacent list elements.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"text": "alice is a good girl she is a good student", "first": "a", "second": "good"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Examine every complete three-word window

The loop is:



`i` is the index of a possible `first` word. A complete triple needs positions `i`, `i + 1`, and `i + 2`.

The largest legal start is `len(words) - 3`. Python's range stops before its endpoint, so `range(len(words) - 2)` produces exactly starts zero through `len(words) - 3`.

If the text contains fewer than three words, the range is empty. No complete pattern can exist, so returning an empty answer is correct.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Unpack the current triple

The exact code uses:



The half-open slice begins at `i` and stops before `i + 3`, producing exactly three words. The loop bounds guarantee that the slice always has length three, so tuple-style unpacking into `a`, `b`, and `c` is safe.

These variables correspond to the pattern roles:

- `a` is the possible `first`.
- `b` is the possible `second`.
- `c` is the word to report if the first two match.

Creating a fixed three-element slice costs constant time and space per iteration.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["girl", "student"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"text": "alice is a good girl she is a good student", "first": "a", "second": "good"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["girl", "student"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Direct indexed comparison:** Compare `words[i]` and `words[i + 1]` and append `words[i + 2]`. This avoids the temporary three-element slice but has the same complexity.
- **Streaming three-word window:** Tokenize lazily and retain only the previous two words. This can reduce auxiliary storage apart from the output, though ordinary `split` is simpler.
- **Regular expression:** A regex can find patterns, but overlapping matches and word boundaries require care and make it less transparent.
- **Fewer than three words:** No loop iteration occurs and the result is empty.
- **No matching bigram:** Nothing is appended.
- **Match at the beginning:** Start index zero is included.
- **Match ending at the final word:** The last legal start is included by the range.
- **Overlapping matches:** Advancing by one preserves them.
- **Repeated third word:** The list keeps one copy per occurrence rather than deduplicating.
- **First equals second:** The two adjacent positions are still checked independently and correctly.
- **Third equals first or second:** There is no restriction on the reported word.
- **Single-space guarantee:** `split` also tolerates broader whitespace, but the source contract is already clean.
- **Input preservation:** Strings are immutable; the method creates a separate token list.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the number of characters in `text` and `W` the number of words.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
