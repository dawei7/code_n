# Guided Example: Check If a Word Occurs As a Prefix of Any Word in a Sentence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sentence": "i love eating burger", "searchWord": "burg"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a `sentence` that consists of some words separated by a **single space**, and a `searchWord`, check if `searchWord` is a prefix of any word in `sentence`.

The objective is to compute `4` from `{"sentence": "i love eating burger", "searchWord": "burg"}` while avoiding redundant calculations and unnecessary overhead.

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

**Turn the sentence into words in original order.** `sentence.split()` produces a list of its words from left to right. The input guarantees single spaces and lowercase letters, so tokenization is straightforward. Calling `split` without an explicit delimiter also ignores surrounding or repeated whitespace, although that extra tolerance is not needed by the contract.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sentence": "i love eating burger", "searchWord": "burg"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The code passes this list to `enumerate(..., 1)`. The second argument makes the first produced index one rather than Python's usual zero. Each loop iteration therefore receives exactly the word position required by the problem and the corresponding word `s`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Use the language's exact prefix operation.** `s.startswith(searchWord)` is true when the first characters of `s` equal all of `searchWord`. It also returns false when `searchWord` is longer than `s`, so there is no need for a separate length check or slicing boundary logic.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sentence": "i love eating burger", "searchWord": "burg"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Manual character scan:** Walk the original sentence, identify each word start, and compare `searchWord` without creating word strings. This achieves the manifest's `O(N)` time and `O(1)` auxiliary space.
- **Explicit split list variable:** Assign `words = sentence.split()` before looping. It behaves exactly like the inline stored expression and can be easier to inspect, with the same linear allocation.
- **Prefix slicing:** Compare `s[:len(searchWord)]` with `searchWord`. It is correct but allocates a substring for each checked word.
- **Regular expression:** A word-boundary pattern can locate a prefix, but translating its character position back to a one-based word index adds complexity for this simple scan.
- **Trie:** Building a prefix tree can help answer many prefix queries against the same sentence. For one query it uses unnecessary `O(N)` construction and storage.
- **Search as an arbitrary substring:** Using `searchWord in s` is wrong because occurrences away from the first character are not prefixes.
- **Several matching words:** Immediate return gives the minimum one-based index.
- **Whole-word equality:** A word starts with itself, so it is a valid match.
- **Search word longer than a word:** `startswith` returns false safely.
- **First word matches:** `enumerate` begins at one, so the function returns one without examining later words.
- **Last word matches:** Earlier failures do not prevent reaching it, and its correct one-based position is returned.
- **No match:** Exhausting the loop produces `-1`.
- **One-word sentence:** The single prefix test decides between one and `-1`.
- **Repeated words:** Each occurrence has its own position. The first matching occurrence wins.
- **Lowercase guarantee:** Direct comparison is correct; converting case could change a problem with case-sensitive semantics and is unnecessary.
- **Single-space guarantee:** `split` preserves word order and produces no empty tokens. Its broader whitespace behavior does not affect valid inputs.
- **Empty search word outside the contract:** Every string starts with the empty string, but the input guarantees at least one search character.
- **Memory accounting:** The generator-like `enumerate` is constant-space, but the underlying split list is not. Include that list when analyzing this exact source.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the number of characters in `sentence` and `M` the length of `searchWord`. Splitting the sentence takes `O(N)` time and creates words with `O(N)` total characters.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
