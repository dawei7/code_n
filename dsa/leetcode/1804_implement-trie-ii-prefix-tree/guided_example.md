# Guided Example: Implement Trie II (Prefix Tree)

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"], "arguments": [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]}`
- **Required output:** `[null, null, null, 2, 2, null, 1, 1, null, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A <a href="https://en.wikipedia.org/wiki/Trie" target="_blank">**trie**</a> (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

The objective is to compute `[null, null, null, 2, 2, null, 1, 1, null, 0]` from `{"operations": ["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"], "arguments": [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each node represents one prefix

A trie stores words by sharing their prefixes. The root represents the empty prefix. Following the child for `'a'` reaches the prefix `"a"`, then following `'p'` reaches `"ap"`, and so on.

Every node in the protected solution is another `Trie` object with three pieces of state:

- `children` is a fixed array of 26 child references, one for each lowercase letter;
- `v` counts how many stored word instances end exactly at this node;
- `pv` counts how many stored word instances pass through this node, meaning how many begin with the prefix represented by the node.

The two counters answer different questions. If the trie contains `"app"` and `"apple"`, the node for `"app"` has an exact-word count for `"app"`, while its prefix count includes both words.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"], "arguments": [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Map a character to one child slot

For lowercase character `c`, `ord(c) - ord('a')` produces an index from 0 through 25. This gives constant-time access to the appropriate child without hashing at every node.

The lowercase-only input contract is essential: it guarantees every character maps inside the array.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Insert one word instance

Insertion starts at the root. For each character, it computes the child index and creates a new `Trie` node if that link is absent. It then moves into that child and increments the child's `pv`.

Incrementing after the move means the node for every nonempty prefix of the word gains one prefix instance. The root's `pv` is never changed. Empty prefixes are not queried under the constraints, so no root prefix count is needed.

After the final character, `node.v += 1` records one additional exact occurrence of the full word. Inserting the same word twice walks the same nodes and increments the same counters twice; duplicates are intentionally preserved.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, null, 2, 2, null, 1, 1, null, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"], "arguments": [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, null, 2, 2, null, 1, 1, null, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dictionary children:** A hash map per node stores only present edges and may save sparse-node memory, but child lookup has hashing overhead.
- **Subtree counting on demand:** Traversing every descendant for a prefix query can be proportional to the entire stored dataset; `pv` makes the answer immediate after the path lookup.
- **Store a Boolean terminal flag:** It cannot represent duplicate word instances; integer `v` is required.
- **Physically prune on erase:** Nodes whose prefix count reaches zero can be unlinked, but the exact source deliberately retains them for simpler updates and possible reuse.
- **Insert duplicates:** Every occurrence increments both prefix and exact counts independently.
- **Word is a prefix of another:** Its node can have both a positive `v` and children leading to longer words.
- **Missing path:** `search` returns `null` and count methods return zero.
- **Existing path with zero exact count:** `countWordsEqualTo` returns zero even if longer words share the path.
- **Erasing one of several copies:** Counters decrease by one rather than resetting.
- **Guaranteed valid erase:** It permits traversal without defensive missing-child checks or negative-count protection.
- **Root prefix count:** It remains zero because empty prefixes are outside the input contract.
- **Maximum word length:** Iterative traversal avoids recursion-depth concerns for length 2000.
- **Lowercase alphabet:** It justifies fixed 26-way arrays and ordinal indexing.
- **Helper visibility:** `search` is an implementation helper; required public operations call it without changing trie state.
- **Object reuse:** Zero-count retained nodes can be populated again by later insertion.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L$ be the length of the word or prefix supplied to an operation. `insert`, `erase`, `search`, and both count methods traverse one child per character, so each operation takes $O(L)$ time.
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
