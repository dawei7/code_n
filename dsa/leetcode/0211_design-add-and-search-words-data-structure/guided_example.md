# Guided Example: Design Add and Search Words Data Structure

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": [["search", "."], ["search", "a"]]}`
- **Required output:** `[false, false]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a data structure that supports adding new words and finding if a string matches any previously added string.

The objective is to compute `[false, false]` from `{"operations": [["search", "."], ["search", "a"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why ordinary membership storage is not enough

`addWord` stores literal lowercase words, but `search` accepts patterns in
which `.` can stand for any one lowercase letter. A hash set can answer an
ordinary exact lookup efficiently, yet a pattern such as `.ad` represents up
to 26 concrete strings. Generating all replacements and looking each one up
would repeat prefix work and scale poorly as the number of wildcards grows.

A trie stores words by their prefixes. Each edge consumes one character, so a
literal query follows one edge while a dot can branch to every existing edge
at that same depth. Crucially, it explores only prefixes that were actually
inserted rather than blindly constructing every theoretical replacement.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": [["search", "."], ["search", "a"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What one trie node records

The exact solution defines a small `Trie` node class. Every node contains a
26-element `children` list and an `is_end` boolean. Child position 0 represents
`a`, position 1 represents `b`, and position 25 represents `z`; `null` means
that no stored word continues through that letter. `is_end` distinguishes a
complete inserted word from a path that exists only as a prefix of a longer
word.

`WordDictionary` owns one root node in `trie`. The root represents the
empty prefix. If `bad`, `bake`, and `dad` have been inserted, the first two
words share the root's `b` child and the next `a` child, then diverge. The word
beginning with `d` uses another root child. Prefix sharing is the reason the
trie can avoid repeatedly storing and checking the same beginning.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Adding a word preserves all previously stored words

`addWord` begins at the root. For every character `c`, it computes
`ord(c) - ord('a')`, which is an index from 0 through 25 under the lowercase
input guarantee. If the corresponding child is absent, the method creates a
new `Trie` node there. It then moves into that child whether it was new or
already present.

After consuming the whole word, it sets `node.is_end = true`. The flag is set
only at the final node. If `bad` is inserted, the nodes for `b` and `ba` exist,
but neither becomes a stored word accidentally. Inserting `ba` later reuses
those nodes and marks the `ba` node without damaging the longer `bad` route.
Inserting an already stored word is idempotent: its path is reused and its
already-true endpoint flag remains true.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[false, false]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": [["search", "."], ["search", "a"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[false, false]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative frontier of nodes:** Keep every node that can match the current pattern prefix, replacing the frontier with matching literal children or all children for a dot. It avoids recursion and substring slices but can hold a broad set of nodes at once; it is the method described by the manifest summary, not by the exact source file.
- **Nested dictionaries with an end sentinel:** A map stores only present character edges and naturally supports sparse alphabets. It may save empty child slots but adds hashing and per-entry overhead; the fixed array exploits the lowercase-only contract.
- **Words grouped by length in hash sets:** Search only words of the pattern's length and compare characters with dot matching. It is simple, but a query can scan every stored word of that length, giving $O(NL)$ time for $N$ candidates.
- **No dots:** Search follows exactly one route and never recurses, so a missing character fails immediately and a complete route still requires `is_end` at its endpoint.
- **A dot at the first character:** The root's existing children are the complete set of possible first letters. Empty slots are skipped, so the search never explores letters absent from all stored words.
- **Consecutive dots:** Each recursive level consumes exactly one dot and one edge. A pattern such as `b..` therefore matches only three-letter words beginning with `b`, not shorter or longer words.
- **A prefix but not a word:** If the pattern is exhausted at an unmarked internal node, the helper returns false even if that node has children. Matching must consume an entire added word of the same length.
- **An added word that prefixes another:** Both can be represented by marking the shorter endpoint while retaining its children. Searches for either length consult the appropriate endpoint flag.
- **Duplicate additions:** Reusing a path and assigning `true` again does not create duplicate logical entries. The required structure records membership, not frequency.
- **Maximum input sizes:** Words have length at most 25 and queries contain at most two dots, keeping recursion shallow. Up to $10^4$ operations can still build many nodes, so sharing prefixes remains valuable.
- **Lowercase and dot preconditions:** `addWord` accepts only lowercase letters, and only search patterns may contain dots. The fixed-index calculation and wildcard branch assume those guarantees; other characters are outside the contract.
- **Input preservation:** The implementation reads each supplied string and creates slices during wildcard recursion, but strings are immutable and the caller's values are never changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L B^d)$. Let $L$ be the length of the added word or search pattern, let $d$ be the
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
