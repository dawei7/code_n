# Guided Example: Truncate Sentence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "Hello how are you Contestant", "k": 4}`
- **Required output:** `"Hello how are you"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **sentence** is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of **only** uppercase and lowercase English letters (no punctuation).

The objective is to compute `"Hello how are you"` from `{"s": "Hello how are you Contestant", "k": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat the sentence as words, not as arbitrary characters

The required result consists of the first $k$ complete words with exactly one space between adjacent words. The protected solution performs three direct transformations:

1. `s.split()` converts the sentence into a list of words;
2. `[:k]` keeps its first $k$ entries;
3. `' '.join(...)` reconstructs those words as a sentence.

The input format guarantees that words are already separated by one space with no leading or trailing spaces. Therefore splitting loses no meaningful formatting and returns exactly the semantic word sequence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "Hello how are you Contestant", "k": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How `split()` identifies the words

Calling `split()` without an explicit separator treats runs of whitespace as separators and omits empty tokens. On valid input there is exactly one ordinary space between words, so the result is simply the list described by the problem.

For `"Hello how are you Contestant"`, the list is:

`["Hello", "how", "are", "you", "Contestant"]`.

No punctuation handling is needed because every word contains only English letters.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why slicing produces exactly the required prefix

Python slice `words[:k]` includes indices zero through $k-1$ and excludes index $k$. Those are precisely the first $k$ words.

The constraint guarantees $1\leq k\leq$ the number of words. Thus the slice is nonempty and never needs special handling for a request beyond the sentence.

Slicing also does not modify the original word list; it creates a new list containing references to the selected words.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"Hello how are you"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "Hello how are you Contestant", "k": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"Hello how are you"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan for the `k`th space:** Return the prefix ending before that separator, using less temporary word-list storage.
- **Build words manually:** It duplicates behavior already provided reliably by `split` and `join`.
- **Character-count truncation:** It is incorrect because words have different lengths and may be cut in the middle.
- **Regular expression tokenization:** It adds machinery without improving the guaranteed simple format.
- **`k = 1`:** The slice keeps only the first word, and join adds no spaces.
- **`k` equals total words:** The complete sentence is reconstructed unchanged.
- **One-word sentence:** The only valid `k` is one, so the same word is returned.
- **Mixed letter case:** Words are preserved exactly; no normalization occurs.
- **Single-space guarantee:** Tokenization matches the source boundaries exactly.
- **No leading spaces:** The output naturally begins with the first letter.
- **No trailing spaces:** `join` never appends one.
- **No punctuation:** There is no ambiguity about punctuation attached to a word.
- **Valid `k` range:** No error or padding behavior for excessive `k` is required.
- **Input immutability:** Strings are immutable, and the method produces a new result.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the character length of `s`. Splitting scans all $n$ characters and creates word strings/list entries. Slicing copies at most all word references, and joining writes at most $n$ output characters. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
