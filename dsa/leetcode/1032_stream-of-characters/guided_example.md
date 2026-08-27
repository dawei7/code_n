# Guided Example: Stream of Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["a"], "queries": ["a", "b", "a"]}`
- **Required output:** `[true, false, true]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings `words`.

The objective is to compute `[true, false, true]` from `{"words": ["a"], "queries": ["a", "b", "a"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A query asks about suffixes ending now

After each new letter arrives, every candidate answer must end at that newest letter. The uncertainty is only how far backward the candidate suffix begins.

Searching every word forward would require trying many different suffix starting positions. Reversing the viewpoint removes that branching. If a word is stored backward, then reading the stream from newest character to oldest follows a single path from the trie's root.

For example, word `"cd"` is inserted as `"dc"`. When the stream ends in `"...cd"`, searching its characters backward reads `d` and then `c`, exactly the stored trie path. A suffix match in forward order becomes a prefix match in reversed order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["a"], "queries": ["a", "b", "a"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Trie node structure

Each `Trie` node has `children`, a list of 26 possible next nodes, and `is_end`, which marks whether some complete reversed word ends there.

For lowercase character `c`, `ord(c) - ord('a')` maps `a` through `z` to indices zero through 25. A fixed child array avoids hash lookups and is safe because both words and query letters are guaranteed lowercase English letters.

The constructor inserts every word. In `insert`, `w[::-1]` visits its letters from last to first. A missing child node is created; an existing child is reused, allowing words with common suffixes in normal order to share trie prefixes after reversal.

After the final reversed character, `node.is_end = true` records a complete word. Reinserting a duplicate word simply follows the same path and sets the same flag again.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Each `Trie` node has `children`, a list of 26 possible next ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Store arriving letters

`StreamChecker` keeps all received letters in `cs`. Every call to `query` appends the new letter before searching, ensuring the current suffix includes that letter.

Only a bounded recent suffix can match. The maximum word length is 200, and a suffix longer than every word cannot be equal to a word. The exact code passes `cs[-limit:]` with `limit = 201`. This creates a list containing at most the most recent 201 characters.

Using 201 rather than 200 is harmless. Every trie path representing a word ends by depth 200 at the latest. If a terminal node is reached, search returns true immediately before an extra older character matters. If no terminal is reached within 200 steps, no dictionary word matches; the possible 201st step cannot create a word longer than the allowed maximum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[true, false, true]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["a"], "queries": ["a", "b", "a"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[true, false, true]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Forward trie with every suffix start:** Store :** - **Forward trie with every suffix start:** Store words normally and try searches from several recent positions after each query. This repeats work across candidate lengths; reversal turns them into one root-to-leaf scan.
- **Hash set of words:** Build every suffix of the recent stream and test membership. At most `W` suffixes exist, but materializing them can cost `O(W^2)` characters per query.
- **Aho-Corasick automaton:** Failure links can process each new character incrementally and report suffix matches efficiently. It offers stronger streaming performance but is substantially more complex than a reversed trie for `W <= 200`.
- **Store a bounded deque:** Keeping only the latest `W` characters is sufficient and changes persistent stream history from `O(Q)` to `O(W)`.
- **One-character word:** The first child reached during search is terminal, so any query with that letter returns true immediately.
- **A word that is a suffix of another word:** The shorter word's terminal appears before the longer path ends. Early return correctly accepts the shorter suffix.
- **Duplicate words:** Reinsertion reuses nodes and leaves the same terminal flag true; behavior is unchanged.
- **Shared normal suffixes:** Words such as `"cd"` and `"ad"` share root edge `d` in the reversed trie, saving nodes.
- **Stream shorter than every word:** The slice contains the entire stream, and search returns false unless a complete shorter word actually ends along its path.
- **Stream much longer than 200:** Only recent characters can participate in a matching word. Older history is ignored by search even though the exact list retains it.
- **Why 201 is safe:** It is one larger than the maximum word length, but no valid trie terminal requires that extra character and successful search returns before it.
- **Missing first edge:** If no word ends in the newest letter, search rejects after one step because every valid suffix must end there.
- **Lowercase contract:** Array indexing assumes characters from `a` through `z`. Other characters could produce invalid indices and are outside the source domain.
- **Nonempty words:** No terminal is placed at the trie root, matching the requirement that the reported suffix and every input word are nonempty.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S + QW)$. Let `S` be the total number of characters across all input words, `W` the maximum word length, and `Q` the number of query calls.
- **Auxiliary Space Complexity:** $O(S+W)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
