# Guided Example: Unique Morse Code Words

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["gin", "zen", "gig", "msg"]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

The objective is to compute `2` from `{"words": ["gin", "zen", "gig", "msg"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Map each lowercase letter by its alphabet index

The list `codes` contains the 26 Morse encodings in alphabetical order:

- index zero is the code for `a`;
- index one is the code for `b`;
- continuing through index 25 for `z`.

For lowercase character `c`, the expression:

`ord(c) - ord('a')`

converts it to the corresponding zero-based alphabet index.

The input contract guarantees lowercase English letters, so every computed index is within the table.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["gin", "zen", "gig", "msg"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Transform one word by concatenation

For each character of a word, the inner list comprehension retrieves its Morse fragment:

`codes[ord(c) - ord('a')]`.

`''.join(...)` concatenates those fragments without separators.

This matches the definition exactly. A word's transformation is not a list of per-letter codes and does not include spaces or punctuation between them.

For `"cab"`, the fragments are `"-.-."`, `".-"`, and `"-..."`. Joining them produces `"-.-..--..."`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why transformation boundaries do not need preservation

Different letter sequences may concatenate to the same dots-and-dashes string because no separator identifies where one letter code ends and the next begins.

That is intentional. The problem defines uniqueness by the final concatenated transformation, not by the original word or the sequence of fragments.

The algorithm therefore stores only the joined string. If two different words produce the same joined value, the set treats them as one transformation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["gin", "zen", "gig", "msg"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dictionary letter mapping:** Map characters directly to strings. It is readable but the array plus alphabet offset is simpler for a dense lowercase alphabet.
- **Store tuples of fragments:** Incorrect for this definition because two different fragment boundaries may yield the same concatenated transformation.
- **Sort all transformations:** Sorting then counting changes works but costs $O(W\log W)$ comparisons after the same encoding work.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$. Let $C$ be the sum of all input word lengths. Each source character causes one constant-time table lookup and contributes a Morse fragment of length at most four. Constructing all transformations therefore writes $O(C)$ symbols.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
