# Guided Example: Word Squares

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["a"]}`
- **Required output:** `[["a"]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of **unique** strings `words`, return *all the ***<a href="https://en.wikipedia.org/wiki/Word_square" target="_blank">word squares</a>*** you can build from *`words`. The same word from `words` can be used **multiple times**. You can return the answer in **any order**.

The objective is to compute `[["a"]]` from `{"words": ["a"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build the square row by row from diagonal symmetry

All words have the same length $L$, so a completed word square contains exactly $L$ rows. The defining condition is

`square[row][col] == square[col][row]`

for every coordinate. Once the first `d` rows have been chosen, this symmetry forces the first `d` characters of row `d`. Specifically, its character at column `i` must equal the character at column `d` of the already chosen row `i`.

The required prefix for the next row is therefore constructed as

`pref = [v[idx] for v in t]`,

where `t` is the current list of rows and `idx = len(t)`. Joining it gives

`t[0][idx] + t[1][idx] + ... + t[idx - 1][idx]`.

Any word that does not begin with this prefix can never extend the partial square, regardless of later choices. Backtracking only over matching words prunes those impossible branches immediately.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["a"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store prefix candidates in the trie

Each trie node has 26 child slots, one for each lowercase letter, and a list `v` of input word indices. While inserting word index `i`, the code follows or creates the node for each successive character and appends `i` to that node's `v`.

Consequently, the node reached after prefix `p` stores exactly the indices of all words beginning with `p`. The list is attached at every prefix node rather than only at complete-word leaves, so a search need not traverse an entire subtree to collect candidates.

`search(w)` follows the characters of a requested prefix. If a child is absent, no input word has that prefix and it returns an empty list. Otherwise, after the final character it returns that node's candidate index list.

The trie shares nodes for common prefixes. For example, words beginning with `la` reuse the same `l` and `a` nodes, while their indices coexist in the relevant `v` lists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Explore all legal continuations

The outer loop tries every input word as the first row by calling `dfs([w])`. This is necessary because the first row has no forced nonempty prefix, and any word may begin a square.

At recursive depth `idx`, the required prefix is derived from all current rows and looked up in the trie. For every returned index `i`, the corresponding `words[i]` is appended, recursion continues, and then `t.pop()` removes the trial row before the next candidate is tried. This append/recurse/pop pattern restores the exact prior partial square and is the essence of backtracking.

The same input word may be used multiple times. The code intentionally has no `used` set, and trie candidates remain available at every depth. This matches the contract.

When `len(t) == L`, all rows have been chosen. `t[:]` copies the current list into `ans`; copying is essential because later backtracking mutates `t`. Storing `t` itself would make previously recorded results change as rows are popped and appended.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[["a"]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["a"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[["a"]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every sequence of `L` words:** This explores $N^L$ combinations and checks symmetry only afterward. Prefix pruning rejects impossible sequences as soon as their next forced prefix has no candidate.
- **Scan all words for each prefix:** Backtracking remains correct but each state pays $O(NL)$ to find candidates. The trie changes lookup to $O(L)$ plus iteration over actual matches.
- **Prefix hash table:** Map every prefix directly to word indices. It offers fast lookup and similar storage; the trie shares common prefix structure and matches the exact solution.
- **Forbid reusing a word:** A `used` set would violate the contract and lose valid squares such as those containing the same word in multiple rows.
- **Store a completed `t` without copying:** Later `pop` operations would corrupt the recorded answer. `t[:]` freezes the row list for that result.
- **Word length one:** Each input word alone is a valid one-row square. DFS receives a length-one list and records it immediately.
- **No word for a forced prefix:** Trie search returns `[]`, naturally terminating that branch.
- **Several words share a prefix:** Every stored index is explored, ensuring that all valid continuations and outputs are found.
- **Any output order:** Trie insertion and input iteration determine a stable order, but the contract does not require sorting results.
- **Unique input words:** This prevents duplicate dictionary entries from generating identical search branches, though different valid row sequences are all retained.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(NL)$. Let $N$ be the number of words, $L$ their common length, and $P$ the number of partial-square states actually explored by DFS, including completed states. Trie insertion visits $L$ characters for each word and appends one index at each depth, taking $O(NL)$ time.
- **Auxiliary Space Complexity:** $O(NL^2 + L^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
