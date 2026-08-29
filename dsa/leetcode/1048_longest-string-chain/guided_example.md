# Guided Example: Longest String Chain

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["a", "b", "ba", "bca", "bda", "bdca"]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of `words` where each word consists of lowercase English letters.

The objective is to compute `4` from `{"words": ["a", "b", "ba", "bca", "bda", "bdca"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the chain into a length-ordered dynamic program

Every predecessor is exactly one character shorter than its successor. Chain lengths therefore increase by one at every step.

The input's original order is irrelevant, so the code sorts `words` by string length. Once a word at index `i` is processed, every possible predecessor must already appear somewhere before it. This turns the predecessor relation into an acyclic left-to-right dependency.

Let `dp[i]` be the maximum chain length whose final word is `words[i]`. Every word alone forms a chain of length one, so the array begins with ones.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["a", "b", "ba", "bca", "bda", "bdca"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Test whether one word is a predecessor

The helper `check(w1, w2)` first requires `len(w2) - len(w1) == 1`. Inserting exactly one character must increase length by exactly one. Equal lengths, a larger gap, or reversed lengths fail immediately.

Two pointers then scan the strings:

- `i` points to the next unmatched character of shorter `w1`.
- `j` scans longer `w2`.
- `cnt` counts characters skipped from `w2`.

If `w1[i] == w2[j]`, both sequences can use that character, so `i` advances. In every iteration `j` advances because the current longer-word character has been consumed either as a match or as the inserted extra character.

If the characters differ, the only legal explanation is that `w2[j]` is the one inserted character. The code increments `cnt` but leaves `i` in place, allowing the next longer-word character to try matching the same shorter-word character.

At the end, `cnt < 2` requires at most one internal mismatch, and `i == len(w1)` requires every character of the shorter word to have matched in order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why an insertion at the end needs no mismatch

Suppose `w1 = "abc"` and `w2 = "abcd"`. The loop matches `a`, `b`, and `c`. Then `i` reaches the end of `w1` and the loop stops before examining final `d`.

`cnt` remains zero, but the one-character length difference already proves there is exactly one unconsumed longer-word character. The return condition accepts, correctly treating `d` as the insertion.

The same logic handles an insertion at the beginning or middle through one counted mismatch.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["a", "b", "ba", "bca", "bda", "bdca"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Delete-one-character predecessor map:** For each length-sorted word, generate all `L` deletion strings and look up their best chains. This reaches the manifest's `O(W \log W + WL^2)` time and avoids all word pairs.
- **Top-down memoized deletion:** Store all words in a set, recursively delete one character, and memoize the best chain from each word. It has similar deletion-generation complexity.
- **Build an explicit graph:** Add an edge for every predecessor relation and find the longest DAG path. The pairwise DP already performs this implicitly without storing edges.
- **Insertion at the beginning:** The first mismatch is skipped in `w2`, after which matching continues.
- **Insertion in the middle:** Exactly one mismatch is skipped while `i` waits for its character.
- **Insertion at the end:** The loop can finish with zero counted mismatches because the one extra trailing character remains, and the length difference guarantees it.
- **Two mismatches:** `cnt` reaches at least two and the helper rejects, even if lengths differ by one.
- **Reordered characters:** Pointer monotonicity prevents acceptance.
- **Same-length words:** They fail the length check immediately and cannot extend a chain.
- **Single input word:** `res` remains one, the correct trivial chain length.
- **Duplicate words:** Equal strings cannot be predecessor-successor pairs because their lengths are equal; duplicates do not artificially extend a chain.
- **Several predecessors:** `max` chooses the one carrying the longest earlier chain.
- **Input mutation:** Sorting changes the order of `words`. A caller needing original order must sort a copy.
- **Extra DP slot:** The exact array has length `n + 1` although indices zero through `n - 1` are used. The spare entry is harmless.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(W \log W + W^2L)$. Let `W` be the number of words and `L` the maximum word length. Sorting takes `O(W \log W)` comparisons.
- **Auxiliary Space Complexity:** $O(W)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
