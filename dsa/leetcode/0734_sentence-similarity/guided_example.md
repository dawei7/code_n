# Guided Example: Sentence Similarity

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sentence1": ["great"], "sentence2": ["great"], "similarPairs": []}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We can represent a sentence as an array of words, for example, the sentence `"I am happy with leetcode"` can be represented as `arr = ["I","am",happy","with","leetcode"]`.

The objective is to compute `true` from `{"sentence1": ["great"], "sentence2": ["great"], "similarPairs": []}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Similarity is position-by-position and direct

Two sentences can be similar only if they have the same number of words. Once lengths match, every word at index `i` in the first sentence must be compatible with the word at the same index in the second.

There are exactly two ways a word pair passes:

- The two words are identical, because every word is similar to itself.
- The two distinct words appear as one of the explicitly supplied similar pairs, in either orientation.

The relation is not transitive in this problem. If `a` is paired with `b` and `b` is paired with `c`, that does not establish similarity between `a` and `c`. This is why the exact solution stores direct pair membership rather than building connected components.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sentence1": ["great"], "sentence2": ["great"], "similarPairs": []}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reject unequal sentence lengths before pairing words

The first check compares the two lengths. If they differ, the sentences are immediately dissimilar.

This is not merely a performance shortcut. Python’s `zip` stops when the shorter input ends. Without the explicit length check, all positions of the shorter sentence might pass and extra words in the longer sentence would never be examined, causing a false positive.

After equal lengths are established, `zip(sentence1, sentence2)` produces every corresponding pair exactly once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first check compares the two lengths.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Store declared pairs in a hash set

The set comprehension

`s = {(x, y) for x, y in similarPairs}`

turns each two-word declaration into a tuple that can be tested with expected constant-time hash lookup.

The solution stores only the orientation provided by the input. During validation it tests both `(x, y)` and `(y, x)`. That makes similarity symmetric without doubling the stored set.

For example, if the declaration is `["drama", "acting"]`, the sentence position `("acting", "drama")` still succeeds through the reverse lookup.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sentence1": ["great"], "sentence2": ["great"], "similarPairs": []}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Map each word to a set of direct neighbors:** :** - **Map each word to a set of direct neighbors:** Insert both directions and test `y in neighbors[x]`. This also gives expected linear construction and checking, but stores two directed entries per pair. The tuple set is more compact.
- **- **Linear scan of `similarPairs` for every positi:** - **Linear scan of `similarPairs` for every position:** It avoids preprocessing but can take `O(np)` time because the same pair list is searched repeatedly.
- **- **Union-find or graph traversal:** These incorre:** - **Union-find or graph traversal:** These incorrectly impose transitivity. They belong to Sentence Similarity II, not this direct-relation problem.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + p)$. Let `n` be the common sentence length when lengths match and `p` the number of declared pairs.
- **Auxiliary Space Complexity:** $O(p)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
