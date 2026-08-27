# Guided Example: Replace Words

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"dictionary": ["a", "b", "c"], "sentence": "aadsfasf absbs bbab cadsfafs"}`
- **Required output:** `"a a b c"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In English, we have a concept called **root**, which can be followed by some other word to form another longer word - let's call this word **derivative**. For example, when the **root** `"help"` is followed by the word `"ful"`, we can form a derivative `"helpful"`.

The objective is to compute `"a a b c"` from `{"dictionary": ["a", "b", "c"], "sentence": "aadsfasf absbs bbab cadsfafs"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The replacement relation is a prefix relation

A dictionary root can replace a sentence word only when the root appears at the very beginning of that word. For example, `"cat"` can replace `"cattle"`, but it cannot replace a word merely because `"cat"` occurs in the middle.

When several roots match, the shortest one must win. This means a search should examine a word from left to right and stop at the first dictionary root it completes.

A trie is designed for exactly this operation. It stores common prefixes once and lets the search consume one character at a time without repeatedly constructing and hashing every possible prefix.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"dictionary": ["a", "b", "c"], "sentence": "aadsfasf absbs bbab cadsfafs"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What one trie node means

The root trie node represents the empty prefix. Following an edge labeled with a letter extends that prefix by one character. A path from the root therefore spells a dictionary prefix.

Each node contains:

- `children`, an array of 26 child references for lowercase English letters;
- `is_end`, which says whether the path ending at this node is a complete dictionary root.

The array index for character `c` is `ord(c) - ord("a")`. Thus `a` maps to zero, `b` to one, and `z` to twenty-five. The source guarantees lowercase letters, so every dictionary and sentence-word character maps to a valid slot.

It is important to distinguish “this prefix exists” from “this prefix is a root.” A node may exist only because it is on the path to a longer dictionary word. `is_end` records when stopping at that node is legally allowed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The root trie node represents the empty prefix.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Insert every dictionary root

Insertion starts at the trie root and processes the letters of a dictionary word in order. For each letter:

1. Compute its child index.
2. Create a child node if that edge does not exist.
3. Move to the child.

After the last letter, mark `is_end = true`.

If several roots share a prefix, they reuse the same initial nodes. For dictionary roots `"cat"` and `"car"`, the `c` and `a` nodes are shared, then the paths branch. If one root is a prefix of another, such as `"a"` and `"apple"`, the node for `a` is terminal and still has descendants.

Inserting the same root more than once simply sets the same Boolean to true again. Duplicate dictionary entries, if present, do not alter replacement behavior.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"a a b c"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"dictionary": ["a", "b", "c"], "sentence": "aadsfasf absbs bbab cadsfafs"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"a a b c"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Hash set of roots:** Put all roots in a set an:** - **Hash set of roots:** Put all roots in a set and test every prefix of each word from shortest to longest. The logic is simple, but Python slicing constructs progressively longer strings, which can make processing one long word quadratic in its length.
- **- **Sort roots by length and test each against eac:** - **Sort roots by length and test each against each word:** This guarantees that the first match is shortest but may compare many unrelated roots for every word, performing much more work than following one trie path.
- **- **Dictionary child maps:** A hash map per trie n:** - **Dictionary child maps:** A hash map per trie node stores only existing edges and may use less space for sparse nodes. The 26-slot array offers direct indexing and predictable behavior for the fixed alphabet.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D + S)$. Let `D` be the total number of characters across all dictionary roots and `S` be the number of characters in the input sentence.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
