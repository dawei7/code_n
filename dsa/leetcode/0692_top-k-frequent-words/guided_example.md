# Guided Example: Top K Frequent Words

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["i", "love", "leetcode", "i", "love", "coding"], "k": 2}`
- **Required output:** `["i", "love"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `words` and an integer `k`, return *the *`k`* most frequent strings*.

The objective is to compute `["i", "love"]` from `{"words": ["i", "love", "leetcode", "i", "love", "coding"], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Counting occurrences

`cnt = Counter(words)`

builds a mapping from each distinct word to the number of times it occurs in the input.

For example, with

`["i", "love", "leetcode", "i", "love", "coding"]`,

the mapping contains frequencies two for `"i"` and `"love"` and one for `"leetcode"` and `"coding"`.

The source guarantees that `k` is at most the number of unique words, so the mapping contains enough entries for the requested result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["i", "love", "leetcode", "i", "love", "coding"], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Turning two ordering rules into one sort key

The expression

`sorted(cnt, key=lambda x: (-cnt[x], x))`

iterates over the dictionary's keys, so each element `x` being sorted is a unique word.

Its key is a two-item tuple:

`(-cnt[x], x)`.

Python sorts tuples lexicographically: it compares the first components, and only if those are equal does it compare the second components.

Ordinary numeric sorting is ascending. Negating the frequency reverses that dimension:

- frequency `5` becomes key component `-5`;
- frequency `3` becomes `-3`;
- because `-5 < -3`, the frequency-five word appears first.

If two frequencies are equal, their negative components are equal, so tuple comparison moves to the word itself. Python's normal string ordering puts the lexicographically smaller lowercase word first, exactly matching the tie rule.

This key avoids writing a custom comparator. It also defines a complete deterministic order for every pair of distinct words.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why sorting the Counter directly works

Iterating over a dictionary-like `Counter` produces its keys, not its `(word, frequency)` pairs. Therefore, `sorted(cnt, ...)` returns a list of words.

The key function can still read each frequency through `cnt[x]`. There is no need to call `cnt.keys()` explicitly, and no need to remove frequencies from the sorted output afterward.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["i", "love"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["i", "love", "leetcode", "i", "love", "coding"], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["i", "love"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Size-`k` min-heap:** Keep only the best `k` unique words while scanning the frequency map. This can achieve `O(N + U\log k)` heap work, but the heap's “worst retained word” ordering must reverse the lexicographical tie rule carefully, and the final `k` words still need output ordering.
- **Max-heap of all unique words:** Heapify keys based on negative frequency and word, then pop `k` times. This uses `O(U)` space and takes `O(U + k\log U)` after counting.
- **Frequency buckets plus tries:** Bucket words by count and enumerate each bucket lexicographically through a trie. With bounded word length, this can approach linear time but has much larger constants and implementation complexity.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log K)$. Let:
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
