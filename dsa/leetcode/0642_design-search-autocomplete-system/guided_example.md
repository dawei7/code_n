# Guided Example: Design Search Autocomplete System

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["AutocompleteSystem", "input", "input", "input", "input"], "arguments": [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]}`
- **Required output:** `[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character `'#'`).

The objective is to compute `[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]` from `{"operations": ["AutocompleteSystem", "input", "input", "input", "input"], "arguments": [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate persistent sentence data from the current query

The system must remember all historical sentences and their hot degrees across calls. It must also remember the characters typed since the most recent terminator. The solution represents these two kinds of state separately:

- a trie stores sentences and accumulated frequencies permanently;
- the list `t` stores the current unfinished input one character at a time.

When an ordinary character arrives, it is appended to `t` and the whole current text becomes the prefix to search. When `#` arrives, the characters in `t` form a completed sentence. That sentence is inserted with an increment of one, `t` is reset to an empty list, and no suggestions are returned for the terminator.

Keeping `t` as a list makes appending one character efficient. The implementation joins it into a string when it needs to search or save the sentence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["AutocompleteSystem", "input", "input", "input", "input"], "arguments": [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the trie represents the alphabet

Every trie node owns an array of 27 child references. Indices zero through twenty-five represent lowercase `a` through `z`. Index twenty-six represents a space. The conversion is:

- `ord(c) - ord("a")` for a lowercase letter;
- twenty-six for a space.

An array gives direct child lookup without hashing. It is appropriate because the reference alphabet is fixed and small. A node represents the prefix spelled by the path from the root to that node; the root represents the empty prefix.

Only terminal nodes need sentence information. At the end of an inserted sentence:

- `v` stores its hot degree;
- `w` stores the complete sentence text.

Intermediate prefix nodes normally retain `v = 0` and an empty `w`. This lets the search traversal distinguish a complete historical sentence from a prefix that merely leads to longer sentences.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every trie node owns an array of 27 child references.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Insertion accumulates rather than replaces frequency

To insert sentence `w` with amount `t`, the trie walks or creates one edge for each character. At the terminal node, it performs `node.v += t` and saves the full sentence.

The addition is essential. The initialization data could conceptually contain an existing sentence count, and each later completed user input must raise that same sentence's hot degree by one. Replacing `v` would lose history. If the sentence is new, the default zero plus the increment creates its first count.

Storing the full sentence at the terminal node means a later traversal does not have to rebuild it from the path. That costs references to sentence strings but makes collection simple.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["AutocompleteSystem", "input", "input", "input", "input"], "arguments": [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Store the top three at every trie node:** Duri:** - **Store the top three at every trie node:** During insertion, update each prefix node's cached best sentences. A query can then return results after following the new character, avoiding subtree traversal and full sorting. This greatly improves frequent-query performance but makes insertions more complicated because a frequency change can alter rankings along every prefix.
- **- **Maintain a current trie pointer:** Ordinary ca:** - **Maintain a current trie pointer:** Ordinary calls can advance from the node reached by the previous character instead of joining and rescanning the whole prefix. Once a path becomes missing, a sentinel state can remain missing until `#`. This reduces prefix navigation to constant time per character, though it does not remove the subtree traversal and sorting cost.
- **- **Heap for the best three:** While traversing ma:** - **Heap for the best three:** While traversing matches, a size-three heap can avoid sorting all `H` results, reducing ranking work toward `O(H log 3)`. Tie ordering and the “worst of the kept three” comparison must be implemented carefully.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P + U + H log H)$. Let `C` be the total number of characters across the initial sentences. Building the trie follows or creates one node per character, so initialization takes `O(C)` time. In the worst case it creates `O(C)` trie nodes. Each node contains 27 child slots, a constant-sized array, so the structural space remains `O(C)` under a fixed alphabet. Full-sentence strings are also referenced at terminal nodes; the provided input strings supply those initial objects, while newly completed sentences add storage proportional to their lengths.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
