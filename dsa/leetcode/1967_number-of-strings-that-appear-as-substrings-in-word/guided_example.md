# Guided Example: Number of Strings That Appear as Substrings in Word

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"patterns": ["a", "abc", "bc", "d"], "word": "abc"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `patterns` and a string `word`, return *the **number** of strings in *`patterns`* that exist as a **substring** in *`word`.

The objective is to compute `3` from `{"patterns": ["a", "abc", "bc", "d"], "word": "abc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Test each pattern independently

The result counts entries in `patterns`, not distinct pattern values. The exact solution iterates conceptually through every pattern with the generator `p in word for p in patterns`.

Python's substring membership operator returns true when `p` occurs as a contiguous sequence anywhere inside `word`. It does not accept a subsequence with gaps and does not require the match to begin at index zero.

`sum` treats each true result as one and each false result as zero. Thus every array entry contributes one exactly when it is a substring.

For patterns `["a", "abc", "bc", "d"]` and word `"abc"`, the first three membership tests are true and the last false, giving three.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"patterns": ["a", "abc", "bc", "d"], "word": "abc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why duplicate patterns count repeatedly

The generator iterates list entries rather than converting `patterns` to a set. If `["a","a","a"]` is checked against `"ab"`, all three independent membership operations are true and sum to three, matching the example.

Deduplicating would solve a different question: the number of distinct pattern strings that occur.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The generator iterates list entries rather than converting `... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What the built-in search means

For a pattern of length $P$ and word length $W$, membership searches possible contiguous start positions. A match succeeds only if all $P$ characters align consecutively. Python implements this search inside its string runtime; the source does not implement KMP, a trie, or a multi-pattern automaton.

This is important when explaining the exact algorithm. The one-line form is concise because it delegates matching, not because all patterns are searched in one combined pass.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"patterns": ["a", "abc", "bc", "d"], "word": "abc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **KMP per pattern:** Build a prefix table for ea:** - **KMP per pattern:** Build a prefix table for each pattern and search in $O(W+P_i)$ time, with $O(P_i)$ temporary space.
- **Aho-Corasick automaton:** Search many patterns together after trie/failure-link preprocessing. Duplicate multiplicities must be preserved separately.
- **Enumerate word substrings into a set:** Then membership is fast, but there are $O(W^2)$ substrings and substantial storage.
- **Duplicate pattern entries:** Each occurrence is tested and counted independently.
- **Pattern equals word:** Membership is true.
- **Pattern longer than word:** It cannot be a substring and contributes zero.
- **One-character pattern:** It counts when that character occurs at least once, regardless of how many occurrences word contains.
- **Repeated occurrence in word:** A pattern contributes only one for its array entry; the number of match positions is irrelevant.
- **Overlapping matches:** They still make one membership Boolean true and do not add multiple times.
- **Substring versus subsequence:** Characters must be adjacent; gaps are not allowed.
- **Empty patterns:** The contract excludes them, avoiding Python's always-true empty-string membership behavior.
- **No preprocessing reuse:** Identical patterns trigger repeated membership searches in the exact code, even though caching could reduce work.
- **Short-circuit per pattern:** Membership may stop at its first match, improving practical time without changing the worst-case bound.
- **List-entry counting:** The generator preserves original multiplicity and order, although only the final count is returned.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T+PM)$. Let $Q$ be the number of patterns, $W$ the word length, and $P_i$ the length of pattern $i$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
