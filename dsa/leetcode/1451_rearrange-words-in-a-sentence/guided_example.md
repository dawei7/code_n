# Guided Example: Rearrange Words in a Sentence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"text": "Leetcode is cool"}`
- **Required output:** `"Is cool leetcode"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a sentence `text` (A *sentence* is a string of space-separated words) in the following format:

The objective is to compute `"Is cool leetcode"` from `{"text": "Leetcode is cool"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Normalize the original capitalization before sorting.** The sentence format capitalizes only its first letter; all later letters are lowercase. Once words are rearranged, the original first word may move away from the front. If its capital letter were left unchanged, the output could contain an uppercase letter in the middle.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"text": "Leetcode is cool"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The code first splits `text` into `words`, then applies `words[0] = words[0].lower()`. Because the original format guarantees that all other words are already lowercase, this makes every word lowercase before rearrangement. Case therefore has no lingering connection to the word's old position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`text.split()` separates the sentence into word strings. The contract uses exactly one space between words, but calling `split` without an explicit delimiter also safely handles ordinary whitespace and does not retain separator strings. The result is a mutable list, allowing the code to normalize and sort in place.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"Is cool leetcode"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"text": "Leetcode is cool"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"Is cool leetcode"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Attach original indices:** Sort pairs by length and then original index. This explicitly enforces tie order and works even with an unstable sorting algorithm, but Python's stable sort makes the indices redundant.
- **Bucket words by length:** Append each word to a bucket keyed by its length, then concatenate buckets from shortest to longest. This preserves tie order and can run in `O(N + W + L)` where `L` is the maximum length, but it uses a more specialized structure.
- **Sort by length and word text:** A key such as `(len(word), word)` is wrong because it alphabetizes equal-length words instead of preserving their original order.
- **Unstable sort by length:** In a language whose sort is not stable, equal-length words could be rearranged incorrectly. Add original indices or use stable buckets in that environment.
- **One-word sentence:** Splitting gives one word, sorting changes nothing, and the word is returned with its first letter capitalized.
- **Original first word moves later:** Lowercasing it before sorting prevents an uppercase letter from appearing in the middle of the result.
- **A later word becomes first:** `title` gives it the one required initial capital after sorting.
- **Several equal-length words:** Stability retains their complete original relative order, including duplicates.
- **Duplicate words:** They are separate list elements and are all preserved. A set or dictionary keyed only by word would incorrectly collapse them.
- **Already increasing lengths:** Sorting retains that length order; ties also remain stable. Capitalization is still normalized for the possibly unchanged first word.
- **All words the same length:** Stable sorting leaves the word sequence unchanged, and only sentence capitalization is normalized.
- **Single spaces:** `join` guarantees exactly one separator in the returned sentence, matching the format.
- **No leading or trailing spaces:** `join` adds separators only between words, so none are introduced at the ends.
- **Lowercase word guarantee:** `title` is safe for the new first word because the input contains ordinary lowercase-letter words. More complicated punctuation or apostrophes could make title casing affect multiple segments, but such text is outside the contract.
- **Length versus byte count:** Python `len` counts characters in the given strings. The input is constrained to the expected letter format, so this directly represents word length.
- **Empty input outside the contract:** Accessing `words[0]` would fail. The stated sentence constraints guarantee at least one word, so no empty-case branch is needed.
- **Very long sentence:** The sort dominates by word count while splitting and joining remain linear in characters, consistent with `O(N + W log W)`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + W log W)$. Let `N` be the total number of characters in `text` and `W` the number of words. Splitting and lowercasing copy or process `O(N)` characters. Computing length keys requires `O(W)` calls to `len`, which is constant time for Python strings.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
