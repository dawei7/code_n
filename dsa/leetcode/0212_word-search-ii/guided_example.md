# Guided Example: Word Search II

We trace the step-by-step multi-word Trie construction, simultaneous board-and-trie backtracking DFS, and prefix pruning on representative 2D letter grids:

- **Input:**
  $$
  \text{board} = \begin{bmatrix}
  \text{'o'} & \text{'a'} & \text{'a'} & \text{'n'} \\
  \text{'e'} & \text{'t'} & \text{'a'} & \text{'e'} \\
  \text{'i'} & \text{'h'} & \text{'k'} & \text{'r'} \\
  \text{'i'} & \text{'f'} & \text{'l'} & \text{'v'}
  \end{bmatrix}, \quad \text{words} = [\text{"oath"}, \text{"pea"}, \text{"eat"}, \text{"rain"}]
  $$
- **Required output:** `["eat", "oath"]` (or `["oath", "eat"]`)
- **No Matches Instance:** $\text{board} = \begin{bmatrix} \text{'a'} & \text{'b'} \\ \text{'c'} & \text{'d'} \end{bmatrix}, \quad \text{words} = [\text{"ef"}, \text{"ace"}] \implies []$
- **Single Cell Board Instance:** $\text{board} = [[\text{'a'}]], \quad \text{words} = [\text{"a"}] \implies [\text{"a"}]$
- **Repeated Cell Reuse Block:** Word cannot reuse the same coordinate within the same path.

This instance demonstrates combining Trie data structures with grid graph DFS backtracking, explains why running individual Word Search I searches across $W$ words causes TLE, details in-place cell marking (`'#'`), implements duplicate match suppression (`node.word = None`), and analyzes execution complexity in $O(M \cdot N \cdot 4 \cdot 3^{L-1})$ time.

---

## 1. Instance & Teaching Goal

Given a $4 \times 4$ character board and a dictionary of $W = 4$ candidate words:
$$
\text{words} = [\text{"oath"}, \text{"pea"}, \text{"eat"}, \text{"rain"}]
$$
Find all words in the dictionary that can be formed by sequentially adjacent orthogonal steps on the board, without reusing any grid cell more than once per word.

Tracing the successful candidates:
1. `"oath"`: Starts at $(0, 0)$ (`'o'`) $\to (0, 1)$ (`'a'`) $\to (1, 1)$ (`'t'`) $\to (2, 1)$ (`'h'`). All 4 cells are adjacent. **Found.**
2. `"eat"`: Starts at $(1, 0)$ (`'e'`) $\to (0, 0)$ (`'o'` fails, but $(1, 1)$ is `'t'`, $(2, 0)$ is `'a'`) $\implies (1, 0)$ (`'e'`) $\to (2, 0)$ (`'a'` fails, $(2, 0)$ is `'i'`), $(1, 3)$ (`'e'`) $\to (0, 3)$ (`'n'`), $(1, 0)$ (`'e'`) $\to (0, 0)$ (`'o'`) $\dots$
   Examine cell $(1, 0)$ (`'e'`) $\to (0, 0)$ (`'o'`), or $(1, 3)$ (`'e'`) $\to (1, 2)$ (`'a'`) $\to (1, 1)$ (`'t'`)!
   Path: $(1, 3)$ (`'e'`) $\to (1, 2)$ (`'a'`) $\to (1, 1)$ (`'t'`). **Found.**
3. `"pea"`: Letter `'p'` does not exist anywhere on the board. **Not found.**
4. `"rain"`: Letter `'r'` exists at $(2, 3)$, but its neighbors are `'e'`, `'k'`, `'v'`. None is `'a'`. **Not found.**
Output: `["oath", "eat"]`.

### Why Individual Searches Fail
Running the standard LeetCode 79 DFS independently for each word in `words` takes $O(W \cdot M \cdot N \cdot 4^L)$ time. With up to $30,000$ words, this causes severe TLE.
The **Trie + DFS Backtracking** algorithm reverses the perspective:
- Insert all $W$ words into a single Trie.
- Traverse the board once. At each step, let the Trie guide the search.
- If the current sequence of board letters does not exist in the Trie, prune the entire search branch immediately!

---

## 2. Conceptual Foundation & Invariants

### Trie Architecture for Multi-Word Search
Each Trie node stores:
- `children`: map or array of outgoing character edges.
- `word`: stores the complete string reference if a word terminates at this node (otherwise `None`).

### Backtracking DFS with Prefix Pruning:
For each cell $(r, c)$ in the $M \times N$ board:
If $\text{board}[r][c] \in \text{root.children}$:
  Invoke $\text{backtrack}(r, c, \text{root.children}[\text{board}[r][c]])$.

#### The `backtrack(r, c, node)` Procedure:
1. **Match Discovery:**
   If `node.word is not None`:
   - Add `node.word` to output list `result`.
   - Set `node.word = None` to prevent adding the same word multiple times if found along different paths!
2. **Mark Visited (In-Place):**
   $$
   \text{temp} = \text{board}[r][c], \quad \text{board}[r][c] = \text{'\#'}
   $$
3. **4-Directional Exploration:**
   For $(dr, dc) \in \{(-1, 0), (1, 0), (0, -1), (0, 1)\}$:
   - $nr = r + dr, \quad nc = c + dc$.
   - If in bounds and $\text{board}[nr][nc] \in \text{node.children}$:
     $$
     \text{backtrack}(nr, nc, \text{node.children}[\text{board}[nr][nc]])
     $$
4. **Unmark (Backtrack):**
   $$
   \text{board}[r][c] = \text{temp}
   $$

> **Invariant.** During backtracking at cell $(r, c)$, `node` represents the exact Trie node corresponding to the sequence of characters on the current board path. If `node.children` contains no match for neighbor $(nr, nc)$, that subtree is pruned in $O(1)$ time.

---

## 3. Step-by-Step Worked Execution

We trace the search for `words = ["oath", "pea", "eat", "rain"]`:

### Step 0: Trie Construction
- Insert `"oath"`: `root -> 'o' -> 'a' -> 't' -> 'h'` (`word = "oath"`).
- Insert `"pea"`: `root -> 'p' -> 'e' -> 'a'` (`word = "pea"`).
- Insert `"eat"`: `root -> 'e' -> 'a' -> 't'` (`word = "eat"`).
- Insert `"rain"`: `root -> 'r' -> 'a' -> 'i' -> 'n'` (`word = "rain"`).

| Trie node | Path from the root | `word` stored there | Outgoing edges | Board cells that can reach it |
|:---|:---|:---|:---|:---|
| Node(o) | `o` | none | `a` | $(0,0)$ |
| Node(oa) | `o → a` | none | `t` | $(0,1)$, entered from $(0,0)$ |
| Node(oat) | `o → a → t` | none | `h` | $(1,1)$, entered from $(0,1)$ |
| Node(oath) | `o → a → t → h` | `"oath"` | none | $(2,1)$, entered from $(1,1)$ |
| Node(e) | `e` | none | `a` | $(1,0)$ and $(1,3)$ |
| Node(ea) | `e → a` | none | `t` | $(1,2)$, entered from $(1,3)$ |
| Node(eat) | `e → a → t` | `"eat"` | none | $(1,1)$, entered from $(1,2)$ |
| Node(r) | `r` | none | `a` | $(2,3)$ only |
| Node(p), Node(pe), Node(pea) | `p`, `p → e`, `p → e → a` | `"pea"` at the deepest of the three | `e`, then `a`, then none | none: no board cell holds `'p'`, so this whole subtree is unreachable |

Two facts in that table decide the whole run. First, the stored word sits at the *end* of a path, so a board path that stops one letter early is not a match. Second, a subtree with no entry point on the board costs nothing: the root test rejects its first letter everywhere.

---

### Step 1: Scan Cell $(0, 0)$ (`'o'`)
- Character `'o'` exists in `root.children`!
- Call `backtrack(0, 0, Node(o))`:
  - Mark $\text{board}[0][0] = \text{'\#'}$.
  - Neighbors of $(0, 0)$:
    - $(0, 1)$ contains `'a'`. Is `'a' \in \text{Node(o).children}`? **Yes!**
    - Call `backtrack(0, 1, Node(oa))`:
      - Mark $\text{board}[0][1] = \text{'\#'}$.
      - Neighbors of $(0, 1)$:
        - $(0, 2)$ contains `'a'`. Is `'a' \in \text{Node(oa).children}`? No (`Node(oa)` only has child `'t'`). Pruned!
        - $(1, 1)$ contains `'t'`. Is `'t' \in \text{Node(oa).children}`? **Yes!**
        - Call `backtrack(1, 1, Node(oat))`:
          - Mark $\text{board}[1][1] = \text{'\#'}$.
          - Neighbors of $(1, 1)$:
            - $(2, 1)$ contains `'h'`. Is `'h' \in \text{Node(oat).children}`? **Yes!**
            - Call `backtrack(2, 1, Node(oath))`:
              - `Node(oath).word == "oath"`!
              - **Add `"oath"` to result!**
              - Set `Node(oath).word = None`.
              - Unmark $(2, 1) \to \text{'h'}$.
          - Unmark $(1, 1) \to \text{'t'}$.
      - Unmark $(0, 1) \to \text{'a'}$.
  - Unmark $(0, 0) \to \text{'o'}$.

Result so far: `["oath"]`.

---

### Step 2: Scan Cell $(1, 3)$ (`'e'`)
- Character `'e'` exists in `root.children`!
- Call `backtrack(1, 3, Node(e))`:
  - Mark $\text{board}[1][3] = \text{'\#'}$.
  - Neighbors of $(1, 3)$:
    - $(1, 2)$ contains `'a'`. Is `'a' \in \text{Node(e).children}`? **Yes!**
    - Call `backtrack(1, 2, Node(ea))`:
      - Mark $\text{board}[1][2] = \text{'\#'}$.
      - Neighbors of $(1, 2)$:
        - $(1, 1)$ contains `'t'`. Is `'t' \in \text{Node(ea).children}`? **Yes!**
        - Call `backtrack(1, 1, Node(eat))`:
          - `Node(eat).word == "eat"`!
          - **Add `"eat"` to result!**
          - Set `Node(eat).word = None`.
          - Unmark $(1, 1) \to \text{'t'}$.
      - Unmark $(1, 2) \to \text{'a'}$.
  - Unmark $(1, 3) \to \text{'e'}$.

Result so far: `["oath", "eat"]`.

---

### Step 3: Remaining Grid Scans
- All other cells either have no matching character in `root.children` (e.g. `'i'`, `'k'`, `'f'`, `'l'`, `'v'`) or their paths terminate with no further Trie children.
- Final output: `["oath", "eat"]`.

The outer loop still touches all $16$ board cells, so it is worth seeing exactly how each one is disposed of:

| Letter | Cells holding it | Present among the root's edges? | Cells that open a search | What that search achieves |
|:---|:---|:---|:---:|:---|
| `'o'` | 1: $(0,0)$ | yes | 1 | The path `o → a → t → h` reaches a node holding `"oath"`, so the word is emitted |
| `'e'` | 2: $(1,0)$, $(1,3)$ | yes | 2 | $(1,0)$ is pruned after a single step, because Node(e) has only the `'a'` edge and its neighbors hold `'o'`, `'i'`, `'t'`; $(1,3)$ yields `"eat"` |
| `'r'` | 1: $(2,3)$ | yes | 1 | Pruned after a single step: Node(r) has only the `'a'` edge, and the neighbors hold `'e'`, `'v'`, `'k'` |
| `'a'` | 3: $(0,1)$, $(0,2)$, $(1,2)$ | no | 0 | The root test fails in constant time, so these three cells never open a search |
| `'n'`, `'t'`, `'i'`, `'h'`, `'k'`, `'f'`, `'l'`, `'v'` | 9 in total | no | 0 | The same constant-time rejection; in particular `'p'` never appears at all, so `"pea"` is eliminated without any traversal |

Only $4$ of the $16$ cells survive the first comparison, and only $2$ of those produce a word. That ratio is the entire reason the trie is built first: the dictionary, not the board, decides where a search may begin.

---

## 4. Complete Execution Trace

```text
Trie Root: contains 'o', 'p', 'e', 'r'

Cell (0,0) = 'o':
  -> (0,1) = 'a' (matches 'o'->'a')
    -> (1,1) = 't' (matches 'o'->'a'->'t')
      -> (2,1) = 'h' (matches 'o'->'a'->'t'->'h'*) -> FOUND "oath"

Cell (1,3) = 'e':
  -> (1,2) = 'a' (matches 'e'->'a')
    -> (1,1) = 't' (matches 'e'->'a'->'t'*) -> FOUND "eat"

All other paths pruned.
Final Output: ["oath", "eat"]
```

| Board Cell Start | Character | Matched Trie Path | Adjacent Neighbors Explored | Matched Terminal Word | Added to Results |
|:---:|:---:|:---|:---|:---:|:---|
| $(0, 0)$ | `'o'` | `o -> a -> t -> h` | $(0,1) \to (1,1) \to (2,1)$ | `"oath"` | **`"oath"`** |
| $(1, 0)$ | `'e'` | `e -> (no 'a' neighbor)` | $(0,0), (2,0), (1,1)$ | None | - |
| **$(1, 3)$** | **`'e'`** | **`e -> a -> t`** | **$(1,2) \to (1,1)$** | **`"eat"`** | **`"eat"`** |
| $(2, 3)$ | `'r'` | `r -> (no 'a' neighbor)` | $(1,3), (3,3), (2,2)$ | None | - |

### Decision Trace Inside the Two Successful Backtracking Runs

| Search | Depth | Cell entered | Letter | Trie node reached | Decisive neighbor checks | What this frame does |
|:---|:---:|:---:|:---:|:---|:---|:---|
| `"oath"` | 0 | $(0,0)$ | `'o'` | Node(o) | $(1,0)$ = `'e'` rejected, since the only edge is `'a'`; $(0,1)$ = `'a'` accepted | Masks $(0,0)$ and descends to depth 1 |
| `"oath"` | 1 | $(0,1)$ | `'a'` | Node(oa) | $(0,0)$ is already masked, so it is skipped before any letter test; $(0,2)$ = `'a'` rejected, since the only edge is `'t'`; $(1,1)$ = `'t'` accepted | Masks $(0,1)$ and descends to depth 2 |
| `"oath"` | 2 | $(1,1)$ | `'t'` | Node(oat) | $(1,0)$ = `'e'` and $(1,2)$ = `'a'` rejected, since the only edge is `'h'`; $(2,1)$ = `'h'` accepted | Masks $(1,1)$ and descends to depth 3 |
| `"oath"` | 3 | $(2,1)$ | `'h'` | Node(oath) | The node stores `"oath"` | Emits `"oath"`, clears the stored word, then unwinds and restores `'h'`, `'t'`, `'a'`, `'o'` |
| `"eat"` | 0 | $(1,3)$ | `'e'` | Node(e) | $(1,2)$ = `'a'` accepted; $(0,3)$ = `'n'` and $(2,3)$ = `'r'` rejected | Masks $(1,3)$ and descends to depth 1 |
| `"eat"` | 1 | $(1,2)$ | `'a'` | Node(ea) | $(1,1)$ = `'t'` accepted; $(0,2)$ = `'a'` and $(2,2)$ = `'k'` rejected | Masks $(1,2)$ and descends to depth 2 |
| `"eat"` | 2 | $(1,1)$ | `'t'` | Node(eat) | The node stores `"eat"` | Emits `"eat"`, clears the stored word, then unwinds and restores `'t'`, `'a'`, `'e'` |

Three details in this trace carry the correctness of the method. A masked cell is skipped *before* its letter is inspected, which is what forbids reusing a coordinate inside one word. A rejection is always caused by a missing edge at the current trie node, never by a letter's absence from the dictionary as a whole: `'a'` is rejected at Node(oa) even though `'a'` opens the search at $(0,1)$. And each emission clears the node's stored word, so the second successful path would not be able to append `"oath"` again.

---

## 5. Algorithmic Correctness

**Soundness.** A word is added to `result` if and only if a sequence of sequentially adjacent cells on the board forms the exact sequence of letters stored in the Trie. The in-place marker `'#'` prevents any cell from being visited more than once in the same path. Setting `node.word = None` guarantees that duplicate instances of the same word along different paths are never emitted twice.

**Completeness.** Every cell $(r, c)$ is considered as a potential starting point. Because the Trie contains all dictionary words, any word capable of being formed on the board will be reached and extracted.

---

## 6. Traps This Instance Exposes

- **Duplicate Words in Result:** If `"oath"` can be formed via two distinct paths on the board, searching both paths would append `"oath"` twice. Setting `node.word = None` upon the first discovery prevents duplicate additions without requiring an expensive set conversion.
- **Trie Pruning Optimization:** After a leaf node's word is found, if that node has no children, it can be pruned from the parent's `children` map. This prevents future board searches from exploring already-completed branches.
- **Forgetting to Restore Board Cell:** Failing to restore `board[r][c] = temp` during backtracking permanently leaves `'#'` on the board, breaking subsequent searches from other cells.

### Alternative Approaches and Their Tradeoffs

| Approach | Work at each board position | Prefix pruning | Time | Failure mode or tradeoff |
|:---|:---|:---|:---|:---|
| Trie plus board DFS (used above) | One trie-node descent per entered cell | Constant-time array lookup per neighbor | $O(\sum L)$ construction plus $O(M \cdot N \cdot 4 \cdot 3^{L-1})$ search | Baseline; correctness depends on the in-place `'#'` marker being restored on every exit |
| Independent depth-first search per dictionary word | A full walk from every start cell for every word | None: each word pays for its own walk even when no other word shares its prefix | $O(W \cdot M \cdot N \cdot 4^L)$ | The intended slow solution; with tens of thousands of words it exceeds the time limit |
| Hash set of words plus a hash set of all prefixes | One hashed growing string per entered cell | Pruning power equal to the trie's | $O(M \cdot N \cdot 4^L \cdot L)$ | Correct, but every step rehashes a longer prefix instead of following one array edge, adding a factor of $L$ |
| Trie plus leaf pruning | Same as the trie DFS, with exhausted leaves detached | Constant-time lookup, and dead branches vanish | Same asymptotic bound with a smaller constant | Mutates the trie during the search, so a second board needs the trie rebuilt first |
| Aho–Corasick automaton over the dictionary | One amortized constant-time transition per character | Failure links handle mismatches | Linear in the number of board paths examined — which is still exponential | The automaton is linear in a *text*, but a grid offers exponentially many simple paths, so it removes no asymptotic work here |

The trie is chosen because the board supplies the paths and the dictionary only needs to answer one question per step: does this node have an edge labeled with the neighbor's letter? Answering that in constant time is the strongest pruning available, and it also explains why the asymptotics are governed by $3^{L-1}$ rather than by the dictionary size $W$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Trie Construction: $O(\sum L)$, where $\sum L$ is the total number of characters across all words in `words`.
  - Board Search: $O(M \cdot N \cdot 4 \cdot 3^{L-1})$, where $M \times N$ is board size, $L$ is the maximum word length (at most 10), and each cell has at most 3 branching choices after the first step.
- **Auxiliary Space Complexity:** $O(\sum L)$ memory for the Trie, plus $O(L)$ recursion call stack memory during backtracking.
