# Guided Example: Implement Trie (Prefix Tree)

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": [["search", "bat"], ["startsWith", "b"]]}`
- **Required output:** `[false, false]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A <a href="https://en.wikipedia.org/wiki/Trie" target="_blank">**trie**</a> (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

The objective is to compute `[false, false]` from `{"operations": [["search", "bat"], ["startsWith", "b"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What the data structure must remember

The class receives operations over time, so this is not a problem where one
answer is computed from one input and then discarded. Every call to `insert`
changes the state that later calls to `search` and `startsWith` observe. The
essential distinction is between a complete stored word and a path that merely
exists because it is the beginning of a longer word. After inserting `apple`,
the letters of `app` are present in the structure, which makes
`startsWith("app")` true, but `search("app")` must remain false until `app`
itself is inserted.

A trie represents that distinction naturally. Its root stands for the empty
prefix. Following one edge labelled with a character extends the represented
prefix by that character. Thus, along the route for `apple`, successive nodes
represent `a`, `ap`, `app`, `appl`, and `apple`. Words with a common beginning
share the same initial nodes. Inserting `application` after `apple`, for
example, reuses the nodes for `a`, `ap`, and `app`; only the remainder needs a
different route.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": [["search", "bat"], ["startsWith", "b"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: One `Trie` object is also one trie node

The exact optimal implementation does not define a separate `TrieNode` class.
Every instance of `Trie` is a node, and the object constructed by `Trie()` is
the root node. Each node owns two fields:

- `children` is a list of exactly 26 positions. Position 0 represents `a`,
  position 1 represents `b`, and so on through position 25 for `z`. A `null`
  entry means that no inserted word continues through that letter from this
  node. A non-`null` entry points to another `Trie` instance.
- `is_end` records whether at least one inserted word ends at this exact node.
  It says nothing about whether the node has children. A node can be both a
  word ending and the start of longer stored words.

The fixed array is justified by the contract that every word and prefix uses
only lowercase English letters. For a character `c`, the expression
`ord(c) - ord('a')` converts it into the required index from 0 through 25.
This conversion is constant time, and direct indexing avoids searching among
the outgoing edges.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Inserting a word

`insert` begins with `node = self`, so traversal starts at the root. For each
character `c` in the word, it computes the corresponding child index. If that
child position is empty, this is the first inserted word that needs this exact
prefix, so the method creates a new `Trie` object and stores it there. Whether
the child was newly created or already existed, traversal then moves to that
child. Reusing an existing child is what makes common prefixes share storage.

Only after all characters have been consumed does the method set
`node.is_end = true`. That timing is crucial. Setting the flag on intermediate
nodes would incorrectly turn every prefix into a complete word. Conversely,
failing to set it at the final node would make the path discoverable by
`startsWith` but invisible to exact `search`.

Consider inserting `apple` into an empty trie. The method creates five nodes,
one for each successive prefix, and marks only the `apple` node as an ending.
Inserting `app` afterward walks through three already-existing nodes and marks
the `app` node. It neither deletes the two later nodes nor creates duplicates.
Consequently, both words remain stored. Inserting `apple` again simply follows
the same path and assigns `true` to a flag that is already true, so duplicate
insertion is harmless and needs no special case.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[false, false]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": [["search", "bat"], ["startsWith", "b"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[false, false]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Hash-map children:** Store only existing outgoing edges in a dictionary. This can save memory for sparse nodes and support larger alphabets, but dictionary entries have more per-edge overhead and lookups rely on expected constant-time hashing; the exact solution instead exploits the guaranteed 26-letter alphabet with direct array access.
- **Hash set of complete words:** Exact `search` is expected $O(L)$, but answering `startsWith` by scanning stored words can be far more expensive. Storing every prefix in a second set restores fast prefix checks while duplicating substantial string data.
- **Sorted set or balanced search tree:** Lexicographic ordering can locate the first candidate near a prefix, but operations generally introduce an $O(\log W)$ factor for $W$ stored words and compare strings. The trie makes work depend directly on the queried length.
- **Compressed trie or radix tree:** Collapsing single-child chains into string-labelled edges can reduce node overhead. It adds substring comparison and edge-splitting logic, which is unnecessary for the required operations and fixed constraints.
- **A word that extends an existing word:** Inserting `apple` after `app` follows the existing `app` path, leaves its ending flag true, and creates only the missing `l` and `e` nodes. Both exact searches remain true.
- **A word that is an existing word's prefix:** Inserting `app` after `apple` creates no nodes; it marks the already-present `app` endpoint. This is precisely why path existence and `is_end` must be separate facts.
- **Absent character in the middle:** `_search_prefix` returns `null` as soon as a required child is missing. Later characters cannot repair a broken root-to-node path, so early termination is both safe and efficient.
- **Duplicate insertion:** The same path is reused and the final boolean remains true. The structure models membership rather than insertion frequency, which is exactly what the contract asks.
- **Maximum-length strings and many calls:** Iterative traversal avoids recursion depth problems even when a string has length 2000. Shared prefixes can greatly reduce created nodes, while completely different suffixes correctly receive separate branches.
- **Lowercase-only precondition:** The index formula is valid because the reference contract excludes uppercase letters, punctuation, and other characters. Supporting a broader alphabet would require validation or a different child representation; silently feeding such input to this implementation would violate its contract.
- **Empty strings:** Public inputs are guaranteed nonempty. Internally, `_search_prefix("")` would return the root, making `startsWith("")` true and `search("")` depend on the root's flag, but those behaviors are outside the required input domain and need no special branch.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L$ be the length of the word or prefix supplied to one operation. Each
- **Auxiliary Space Complexity:** $O(T)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
