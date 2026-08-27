# Guided Example: Add Bold Tag in String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abcxyz123", "words": ["abc", "123"]}`
- **Required output:** `"<b>abc</b>xyz<b>123</b>"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and an array of strings `words`.

The objective is to compute `"<b>abc</b>xyz<b>123</b>"` from `{"s": "abcxyz123", "words": ["abc", "123"]}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate matching from formatting.** The output rule sounds like a string-editing task, but inserting tags while searching is awkward. A newly found word may overlap a region already tagged, or it may touch that region exactly at the next character. The exact solution therefore performs three clean phases:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abcxyz123", "words": ["abc", "123"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

1. build a trie from all dictionary words;
2. discover every matched interval in `s`;
3. merge the intervals and construct the tagged string.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | 1.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

This separation ensures that overlap decisions are based on positions in the unchanged source string.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"<b>abc</b>xyz<b>123</b>"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abcxyz123", "words": ["abc", "123"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"<b>abc</b>xyz<b>123</b>"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Boolean coverage array:** Find each word occur:** - **Boolean coverage array:** Find each word occurrence and mark every covered source index. A final boundary scan inserts tags. This is conceptually simple, but repeated substring searches and repeated marking can be expensive.
- **Aho-Corasick automaton:** Add failure links to the trie so all patterns are matched in one left-to-right scan. This is the standard way to approach $O(N+D+M)$ matching without restarting from every index.
- **Track only the farthest covered end:** While scanning starts, retain the furthest endpoint reached by any match and emit maximal regions directly. This can avoid storing every `[start, end]` pair, but the ordering and emission logic must remain careful.
- **Empty `words`:** The trie has no outgoing path, `pairs` stays empty, and the original string is returned unchanged.
- **No matches:** The same early return avoids adding any tags.
- **Overlapping matches:** Intervals such as `[0, 1]` and `[1, 2]` merge because there is no gap.
- **Consecutive matches:** Intervals such as `[0, 1]` and `[2, 3]` also merge because `ed + 1 < a` is false.
- **Contained matches:** If `[0, 5]` is followed by `[1, 2]`, `max(ed, b)` preserves endpoint 5 rather than shrinking the bold region.
- **Match at the first or last character:** Python slices naturally handle empty prefix or suffix slices, so no special tag branch is needed.
- **Several words sharing a prefix:** Terminal flags at multiple trie depths ensure every complete word is recorded while traversal continues toward longer words.
- **Characters outside ASCII:** The 128-child array would be indexed out of range for sufficiently large code points. The input restriction to English letters and digits is therefore part of the implementation's safety argument.
- **Large numbers of matches:** `pairs` can consume significant memory even though the final bold union may contain only one interval. A streaming farthest-end design is preferable when constraints are much larger.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. Let $N=\lvert\texttt{s}\rvert$, let $D$ be the sum of dictionary-word lengths, let $L$ be the maximum dictionary-word length, and let $M$ be the number of matched word occurrences recorded in `pairs`.
- **Auxiliary Space Complexity:** $O(N + D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
