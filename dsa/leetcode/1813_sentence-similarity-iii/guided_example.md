# Guided Example: Sentence Similarity III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sentence1": "My name is Haley", "sentence2": "My Haley"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `sentence1` and `sentence2`, each representing a **sentence** composed of words. A sentence is a list of **words** that are separated by a **single** space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

The objective is to compute `true` from `{"sentence1": "My name is Haley", "sentence2": "My Haley"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Insertion can create only one unmatched middle block

To make a shorter sentence equal to a longer one by inserting one arbitrary sentence, the shorter sentence's words must appear in two pieces:

- some number of its words match the beginning of the longer sentence;
- all remaining words match the end of the longer sentence.

Anything present only in the longer sentence lies between those two pieces and is exactly the inserted sentence. The inserted piece may also be at the beginning, at the end, or empty.

This means similarity is a prefix-plus-suffix coverage problem at word boundaries, not a substring or character-edit problem.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sentence1": "My name is Haley", "sentence2": "My Haley"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Always treat `words1` as the longer list

The solution splits both input strings into word arrays. Because the source guarantees single spaces and no leading or trailing spaces, `split()` recovers exactly the sentence words.

If the first list has fewer words than the second, the method swaps the local arrays and their lengths. After that:

$$
m=\lvert\texttt{words1}\rvert\geq n=\lvert\texttt{words2}\rvert.
$$

Only the shorter sentence could need an insertion to become the longer one. Normalizing their roles avoids duplicate case logic.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count the longest matching prefix

Pointer `i` begins at zero. While `i < n` and `words1[i] == words2[i]`, it advances.

After the loop, the first `i` words of the shorter sentence match the longer sentence's first `i` words. Either all shorter words matched or the next prefix words differ.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sentence1": "My name is Haley", "sentence2": "My Haley"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Deque popping:** Remove matching words from both fronts, then both backs, and accept if the shorter deque empties. It expresses the same invariant with deque storage.
- **Character prefix/suffix matching:** It can split words illegally and is incorrect without careful space-boundary checks.
- **Search for the shorter sentence as a contiguous substring:** The shorter words may be separated by the inserted middle, so contiguity is not required.
- **Dynamic programming edit distance:** It solves a much broader problem and permits operations that this task forbids.
- **Identical sentences:** Prefix matching covers every word, so the result is true with an empty insertion.
- **Insertion at the beginning:** Prefix length can be zero while the suffix covers all shorter words.
- **Insertion at the end:** Suffix length can be zero while the prefix covers all shorter words.
- **Insertion in the middle:** Positive prefix and suffix counts jointly cover the shorter sentence.
- **One-word shorter sentence:** It must match either the first or last word of the longer sentence, unless lengths are equal.
- **Case sensitivity:** Word comparison preserves uppercase and lowercase distinctions.
- **Overlapping prefix and suffix:** It is harmless and deliberately handled by `i + j >= n`.
- **Longer-role swap:** Similarity is symmetric, so swapping local arrays does not change the answer.
- **Single-space guarantee:** `split()` returns the intended word sequence without empty tokens.
- **No leading or trailing spaces:** There are no phantom boundary words to handle.
- **One insertion only:** Two separate unmatched longer regions cannot both be inserted, which the coverage condition rejects.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M+N)$. Let $M$ and $N$ be the character lengths of the two input sentences. Splitting scans and stores their characters in $O(M+N)$ time and space.
- **Auxiliary Space Complexity:** $O(n + m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
