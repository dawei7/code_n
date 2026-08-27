# Guided Example: Longest Word With All Prefixes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["k", "ki", "kir", "kira", "kiran"]}`
- **Required output:** `"kiran"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `words`, find the **longest** string in `words` such that **every prefix** of it is also in `words`.

The objective is to compute `"kiran"` from `{"words": ["k", "ki", "kir", "kira", "kiran"]}` while avoiding redundant calculations and unnecessary overhead.

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

**Store every complete word in a trie.** A trie shares nodes among common prefixes. Following characters from the root traces a prefix, while `is_end` distinguishes a prefix that is itself present as a complete word from one that exists only because a longer word uses it.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["k", "ki", "kir", "kira", "kiran"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Each `Trie` node contains a 26-slot child array and one Boolean. `__slots__` prevents a per-instance attribute dictionary, reducing overhead across potentially many nodes.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Each `Trie` node contains a 26-slot child array and one Bool... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Insert all words before checking candidates.** `insert` begins at the root and maps each lowercase character to index `ord(c) - ord("a")`. A missing child is created; an existing child is reused. After the final character, `node.is_end = true` records that the full word occurs in `words`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"kiran"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["k", "ki", "kir", "kira", "kiran"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"kiran"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort plus valid-word set:** Process words in l:** - **Sort plus valid-word set:** Process words in lexicographic order and accept a word when its immediate prefix is already valid. It is simpler but includes sorting cost.
- **Check every prefix in a hash set:** Straightforward slicing can repeat character copying and lead to quadratic work per long word.
- **One-letter word:** Its only nonempty prefix is itself, which is marked after insertion, so it is valid.
- **Missing immediate prefix:** Search fails at that prefix node even if longer structural trie nodes exist.
- **Missing shorter prefix:** Every depth is checked, so an earlier gap cannot be hidden by later complete words.
- **Several longest valid words:** The lexicographically smallest replaces or blocks larger ties regardless of input order.
- **No valid word:** This can happen when no one-letter starting prefix exists; the empty answer is returned.
- **Duplicate input words:** Insertion simply marks the same node again and does not affect correctness.
- **Existing-path assumption:** `search` omits a null-child guard only because every searched word was inserted first.
- **Short-circuit optimization:** Noncompetitive lengths or ties are not searched because they cannot change `ans`.
- **Fixed lowercase alphabet:** Direct 26-slot arrays trade memory for constant child access.
- **Input order:** Insert-all-first design makes prefix validation independent of order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let `S` be the sum of all word lengths. Insertion visits each input character once, taking `O(S)` time. Each word can be searched at most once, and total searched character length is at most `S`, so validation is `O(S)`. Lexicographic tie comparisons can inspect word characters, but under the total-length input bound the intended overall accounting remains linear in corpus size for trie work.
- **Auxiliary Space Complexity:** $O(26S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
