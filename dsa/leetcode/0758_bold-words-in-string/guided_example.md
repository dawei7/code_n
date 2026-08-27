# Guided Example: Bold Words in String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["ab", "bc"], "s": "aabcd"}`
- **Required output:** `"a<b>abc</b>d"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of keywords `words` and a string `s`, make all appearances of all keywords $\text{words}[i]$ in `s` bold. Any letters between `<b>` and `</b>` tags become bold.

The objective is to compute `"a<b>abc</b>d"` from `{"words": ["ab", "bc"], "s": "aabcd"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate matching, merging, and formatting

The minimum-tag result is easiest to produce in three stages:

1. Find every substring occurrence of every keyword.
2. Merge overlapping or directly adjacent matched ranges.
3. Insert one tag pair around each merged range.

The exact solution uses a trie for efficient prefix matching from every position in `s`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["ab", "bc"], "s": "aabcd"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the keyword trie

Each trie node has child slots indexed by character code and an `is_end` flag. Inserting a word follows or creates one child per character, then marks the final node.

Shared keyword prefixes share trie paths. For example, `"ab"` and `"abc"` reuse the nodes for `a` and `b`, with ending flags at two depths.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Each trie node has child slots indexed by character code and... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find all keyword occurrences

For every possible start index `i` in `s`, traversal begins at the trie root and moves `j` to the right.

If the needed child does not exist, no longer substring starting at `i` can match a keyword, so the loop breaks. Whenever the reached node has `is_end = true`, range `[i, j]` is a complete keyword occurrence and is appended to `pairs`.

Continuing after an ending node is important because a longer keyword may share that prefix.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"a<b>abc</b>d"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["ab", "bc"], "s": "aabcd"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"a<b>abc</b>d"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Boolean coverage array:** Mark every character:** - **Boolean coverage array:** Mark every character covered by any direct keyword search, then emit tags at true-run boundaries. This is simple but may repeat substring searches.
- **- **Aho-Corasick automaton:** Finds all keyword oc:** - **Aho-Corasick automaton:** Finds all keyword occurrences in linear text-plus-match time, but its failure links are unnecessary for the small limits.
- **- **Do not merge adjacent ranges:** That produces :** - **Do not merge adjacent ranges:** That produces extra tags and violates the minimum-tag requirement.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(p + nL)$. Let `p` be the total keyword characters, `n` the source length, and `L` the maximum keyword length. Trie construction is `O(p)`. Each starting position follows at most `L` trie edges before failing or exhausting a longest word, so matching is `O(nL)`.
- **Auxiliary Space Complexity:** $O(p + nL)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
