# Guided Example: Longest Word in Dictionary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["w", "wo", "wor", "worl", "world"]}`
- **Required output:** `"world"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `words` representing an English Dictionary, return *the longest word in* `words` *that can be built one character at a time by other words in* `words`.

The objective is to compute `"world"` from `{"words": ["w", "wo", "wor", "worl", "world"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate “built one character at a time” into a prefix condition

A word is eligible only if every prefix obtained while spelling it is also present in the dictionary. For a candidate such as `apple`, the required words are `a`, `ap`, `app`, `appl`, and `apple`. Merely finding the character path in some data structure is not enough; each point along that path must correspond to a complete dictionary word.

The exact solution represents all dictionary words in a trie. A trie shares nodes among words with common prefixes. Each node owns 26 child positions, one for every lowercase English letter, and an `is_end` flag indicating that the path from the root through that node is a complete inserted word.

This distinction between “path exists” and “word ends here” is fundamental. After inserting `apple`, nodes for `a`, `ap`, `app`, and `appl` all exist, but none of those shorter strings should count as dictionary words unless it was independently inserted and its node was marked `is_end`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["w", "wo", "wor", "worl", "world"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Building the trie

For each input word, `insert` starts at the root and processes its characters from left to right. The letter’s numeric child index is `ord(c) - ord("a")`. If that child does not exist, a new trie node is created. The traversal then moves to that child.

After the final character, `node.is_end = true` records that the complete word belongs to the dictionary. Inserting all words before testing any candidate makes eligibility independent of input order. A longer word may appear before one of its required prefixes in `words`, but the later search still sees the fully built dictionary.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How `search` checks every required prefix

The search begins at the root and follows the candidate’s characters. At each character it performs two checks:

1. The required child must exist. If it does not, even the character path is absent, so the candidate fails.
2. Immediately after moving to the child, that node’s `is_end` flag must be true. If it is false, the prefix ending at this character was never supplied as a complete word, so the candidate fails.

Because the second check occurs after every character, it checks every nonempty prefix, including the candidate itself. A successful search therefore means exactly that the word can be assembled one character at a time using dictionary words.

The full-word check may seem redundant because every candidate came from `words` and was inserted. It is still consistent and keeps `search`’s contract self-contained: success means every visited prefix, including the last, is a complete word.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"world"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["w", "wo", "wor", "worl", "world"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"world"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Hash set of words:** Put every word into a set, then test each candidate’s prefixes with set membership. This is simpler and also efficient, though constructing or slicing every prefix may add character-copying cost in Python. The trie represents prefix boundaries directly.
- **Sort by length and lexicographic order:** After sorting, maintain a set of buildable words and accept a word when its immediate prefix without the last character is buildable. If shorter words are processed first, that single-prefix fact is enough by induction. This approach is concise but pays sorting cost and depends on careful ordering.
- **Trie depth-first traversal:** One can traverse only through child nodes whose `is_end` flag is true and track the deepest reachable word. Visiting children in alphabetical order can handle the tie rule. The exact solution instead searches the original words, which keeps result construction simple.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let `S` be the sum of the lengths of all input words.
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
