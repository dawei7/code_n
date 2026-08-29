# Guided Example: Find Words Containing Character

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["leet", "code"], "x": "e"}`
- **Required output:** `[0, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array of strings `words` and a character `x`.

The objective is to compute `[0, 1]` from `{"words": ["leet", "code"], "x": "e"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What `enumerate` provides

`enumerate(words)` yields each original zero-based index `i` together with its word `w`. This avoids a separate counter and ensures returned indices refer to positions in the input list, not positions in a sorted or filtered copy.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["leet", "code"], "x": "e"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What membership means

For a string `w`, expression `x in w` is true if at least one character equals `x`. Python scans characters until it finds a match or reaches the end.

The list comprehension appends `i` only when this Boolean is true. It does not append an index multiple times when the target appears several times in one word, because membership produces a single Boolean per word.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the result is exact

Take any returned index $i$. It passed `x in words[i]`, so the indexed word contains the target and belongs in the answer.

Conversely, if word $i$ contains `x`, membership finds an occurrence and the comprehension includes $i$. Thus no qualifying index is missed.

Every input word is enumerated once, so these two directions prove the returned list contains exactly the requested set.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["leet", "code"], "x": "e"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Nested explicit loops:** Scan characters manually and break at the first match. It has the same complexity but more bookkeeping.
- **Convert each word to a set:** Membership then becomes fast, but constructing sets costs $O(S)$ time and $O(S)$ extra space for a single target query.
- **Use `w.count(x)`:** Correctly detects positivity but scans the full word even after an early match; `in` can short-circuit.
- **Target appears many times:** Return the word's index once, not once per occurrence.
- **No word contains the target:** Every membership check fails and the result is an empty list.
- **Every word contains it:** The result contains all indices in increasing order.
- **One-character word:** Membership is one direct character comparison.
- **Target at the first character:** Python may finish that word's membership check immediately.
- **Duplicate words:** They occupy different input indices and each qualifying index is returned.
- **Output order:** Increasing order is produced naturally even though any order is accepted.
- **Lowercase guarantee:** No case folding or normalization is needed.
- **Required output space:** The manifest's $O(1)$ space should be read as auxiliary space excluding the returned list.
- **Why no character index is needed:** The task asks only whether a word contains `x`, not where its first or every occurrence lies. Membership deliberately discards location after finding a match.
- **Short-circuit does not change correctness:** Stopping at the first occurrence is safe because later occurrences cannot cause the same word index to be added again or change a Boolean true back to false.
- **Empty words are excluded:** Every word has at least one character, but the same membership expression would safely reject an empty string if the domain changed.
- **Index stability:** The source neither sorts nor mutates `words`, so `i` always denotes the original array position expected by the result contract.
- **Total-character bound is precise:** A word with no target requires all its characters inspected, while one beginning with the target may take one comparison. $O(S)$ states the worst case across these variable stopping points.
- **Why a regular expression is excessive:** Pattern construction and matching add machinery without improving the linear lower bound for a single literal lowercase character.
- **List comprehension allocation:** Result capacity grows only for matching words; nonmatching words do not create placeholder entries.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Define
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
