# Guided Example: Word Search II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"board": [["a", "b"], ["c", "d"]], "words": ["ef", "ace"]}`
- **Required output:** `[]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `m x n` `board` of characters and a list of strings `words`, return *all words on the board*.

The objective is to compute `[]` from `{"board": [["a", "b"], ["c", "d"]], "words": ["ef", "ace"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why searching each word independently repeats too much work

A direct strategy would run a separate board backtracking search for every word.
That is correct, but many dictionary words can share beginnings. Searching
`oath`, `oat`, and `oak` independently rediscovers the same paths for `o` and
`oa` three times. With up to $3 \cdot 10^4$ candidate words, that repeated work
is the central obstacle.

The exact solution combines every candidate in one trie. A trie node represents
a dictionary prefix, and each child edge adds one lowercase letter. During a
board walk, the algorithm advances through the board and trie together. The
moment the current board letters are not a prefix of any candidate, the trie
has no matching child and the search stops. This prefix pruning prevents the
backtracking from exploring paths that cannot produce an answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"board": [["a", "b"], ["c", "d"]], "words": ["ef", "ace"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build one trie containing all candidate words

Each `Trie` node has a 26-position `children` array and an integer `ref`.
Positions 0 through 25 correspond to `a` through `z`. A missing child is
`null`. The root represents the empty prefix.

To insert a word, `tree.insert(w, i)` starts at the root, converts each
character with `ord(c) - ord('a')`, creates a missing child when necessary,
and moves down that edge. At the final node, it stores `i` in `ref`. That
integer is the word's index in the original `words` list. The sentinel `-1`
means that no still-unreported candidate ends at this node.

Storing the index has two advantages. The DFS does not need to build a path
string during recursion, and when it reaches an ending it can recover the exact
candidate with `words[node.ref]`. Different words with shared prefixes reuse
the same initial nodes. If one word is a prefix of another, its endpoint can
have a nonnegative `ref` and also have children, so both words remain
representable.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Start a trie-guided search from every board cell

Any cell can be the first letter of a valid word, so `findWords` calls
`dfs(tree, i, j)` for every board coordinate. It does not precheck whether the
root has that letter; the first lines of `dfs` perform the same test. If the
corresponding trie child is absent, the call returns immediately after constant
work.

Inside `dfs(node, i, j)`, `node` represents the trie prefix matched before
using board cell `(i, j)`. The method converts `board[i][j]` to a child index.
If `node.children[idx]` is absent, appending this board letter would no longer
match any candidate prefix, so the entire branch is impossible. Otherwise it
moves `node` to that child. After the move, the trie depth agrees with the
number of board cells used in the current path.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"board": [["a", "b"], ["c", "d"]], "words": ["ef", "ace"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Run board DFS once per word:** This avoids a trie but repeats shared-prefix exploration for many candidates. Its cost grows with both the number of words and the board search space, which is especially poor when the dictionary is large.
- **Hash set plus prefix set:** Store complete words and every valid prefix, build the current path string during DFS, and stop when it is not in the prefix set. It recreates trie-like information with duplicated strings and extra path construction.
- **Delete exhausted trie branches:** After reporting a terminal word, recursively remove nodes that have no terminal reference and no children. The editorial uses this optimization to reduce later searches; it can be faster but requires careful parent bookkeeping and is absent from the exact source.
- **Separate visited matrix:** It preserves the board without temporary mutation but needs $O(mn)$ extra space or repeated allocation. In-place marking is safe because `'#'` is outside the lowercase board alphabet and every call restores its cell.
- **A word found along several paths:** Clearing `ref` after the first discovery ensures it appears only once in `ans`, even though later DFS calls can still traverse the same trie endpoint.
- **One word prefixes another:** Reporting the shorter word clears only its own reference. Its child edges remain available, allowing the longer word to be found in the same or a later traversal.
- **A board with one cell:** Each DFS either matches a one-letter trie endpoint or stops. There are no in-bounds neighbors, so longer candidates cannot be reported.
- **A one-letter candidate:** It is reported immediately after the DFS advances from the root to that letter's node; neighbor exploration may still continue for longer candidates sharing that prefix.
- **Repeated board letters:** Position, not character value, determines reuse. Different cells containing the same letter may both appear in one path, while the same coordinate cannot be revisited before restoration.
- **Duplicate candidate words:** The contract says `words` is unique. If duplicates were supplied, later insertion would overwrite the endpoint reference with the last index, and the result would still contain only one equal string because the reference is cleared after discovery.
- **No candidate begins with a cell's letter:** The outer loop still calls DFS, but its first child test returns immediately. No marking or neighbor exploration occurs.
- **No matches anywhere:** No endpoint reference is reached, `ans` stays empty, and all temporary board marks are restored normally.
- **Output order:** The nested board scan, neighbor offset order, and trie paths determine discovery order. The contract allows any order, so no sorting step is necessary.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T)$. Let $m$ and $n$ be the board dimensions, $L$ the maximum candidate length,
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
