# Guided Example: Word Ladder II

We trace the step-by-step level-synchronized BFS predecessor DAG construction and backtracking path reconstruction on representative word ladder instances:

- **Input:** `beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot", "dot", "dog", "lot", "log", "cog"]`
- **Required output:** `[["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]`
- **Missing Destination Trap:** `beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot", "dot", "dog", "lot", "log"]` $\implies []$ (`endWord` must exist in `wordList`)

This instance demonstrates level-synchronized word removal (allowing sibling parents to discover the same child before retirement), building a Directed Acyclic Graph (DAG) of shortest predecessor edges, halting BFS immediately upon completing the first tier containing `endWord`, and DFS backtracking to emit all minimal transformation sequences.

---

## 1. Instance & Teaching Goal

Given two words `beginWord = "hit"` and `endWord = "cog"`, and a dictionary `wordList = ["hot", "dot", "dog", "lot", "log", "cog"]`:
A transformation sequence changes exactly one character at a time such that every intermediate word exists in `wordList`.
Find **all** shortest transformation sequences.

In this instance, two equally short 5-word paths exist:
1. $\text{hit} \to \text{hot} \to \mathbf{dot} \to \mathbf{dog} \to \text{cog}$
2. $\text{hit} \to \text{hot} \to \mathbf{lot} \to \mathbf{log} \to \text{cog}$

A naive BFS storing full path lists in the queue causes exponential memory explosion and Time Limit Exceeded (TLE).
The optimal two-phase architecture:
1. **Phase 1 (Breadth-First Search):** Traverses the state space level-by-level to determine shortest distances and build a compact Predecessor Map (`parents[v] = [u1, u2, ...]`). Crucially, words discovered at depth $d$ are only retired from the dictionary after depth $d$ completes, preserving parallel convergence.
2. **Phase 2 (Depth-First Backtracking):** Walks backward from `endWord` to `beginWord` along the constructed predecessor DAG, assembling all valid minimal paths without searching dead ends.

---

## 2. Conceptual Foundation & Invariants

### Level-Synchronized BFS & Predecessor Map Protocol
Let `words` be a hash set of words in `wordList`.
If `endWord` $\notin$ `words`: return `[]`.
Initialize `curr_level = {beginWord}` and `parents = defaultdict(list)`.

While `curr_level` is non-empty and `endWord` not reached:
1. **Remove Active Level from Dictionary:**
   $$
   \text{words.difference\_update}(\text{curr\_level})
   $$
   This prevents cycles while still allowing multiple words in `curr_level` to link to the same child in `next_level`.
2. **Expand Neighbors:**
   For each word $u \in \text{curr\_level}$:
   - Generate all 1-character mutations $v$:
     For each index $i$ and character $c \in \text{'a'} \dots \text{'z'}$:
     $$
     v = u[:i] + c + u[i+1:]
     $$
   - If $v \in \text{words}$:
     - $\text{parents}[v].\text{append}(u)$
     - Add $v$ to `next_level`.
3. **Check Destination:**
   If `endWord` $\in$ `next_level`:
   - Set `found = True`.
   - Halt BFS after committing `parents` (do not advance to depth $d+1$).
4. **Advance Level:**
   $\text{curr\_level} \leftarrow \text{next\_level}$.

### Phase 2: DFS Path Reconstruction
Define $\text{backtrack}(\text{word})$:
- If $\text{word} == \text{beginWord}$: return `[[beginWord]]`.
- For each $p \in \text{parents}[\text{word}]$:
  - For each path in $\text{backtrack}(p)$:
    - Return $\text{path} + [\text{word}]$.

> **Invariant.** For every entry $p \in \text{parents}[v]$, the length of the shortest path from `beginWord` to $p$ is strictly $1$ less than that to $v$.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on `beginWord = "hit"`, `endWord = "cog"`:
Initial `words = {"hot", "dot", "dog", "lot", "log", "cog"}`.

### Level 0: `curr_level = {"hit"}`
- Retire `curr_level`: `words.discard("hit")`.
- Neighbors of `"hit"`:
  - Mutate index 1 (`'i'` $\to$ `'o'`): `"hot"` $\in$ `words`.
  - Link: $\text{parents}[\text{"hot"}].\text{append}(\text{"hit"})$.
- `next_level = {"hot"}`.
- Advance: `curr_level = {"hot"}`.

---

### Level 1: `curr_level = {"hot"}`
- Retire `curr_level`: `words.remove("hot")`.
- Active dictionary: `{"dot", "dog", "lot", "log", "cog"}`.
- Neighbors of `"hot"`:
  - Mutate index 0 (`'h'` $\to$ `'d'`): `"dot"` $\in$ `words`.
    - $\text{parents}[\text{"dot"}].\text{append}(\text{"hot"})$.
  - Mutate index 0 (`'h'` $\to$ `'l'`): `"lot"` $\in$ `words`.
    - $\text{parents}[\text{"lot"}].\text{append}(\text{"hot"})$.
- `next_level = {"dot", "lot"}`.
- Advance: `curr_level = {"dot", "lot"}`.

---

### Level 2: `curr_level = {"dot", "lot"}`
- Retire `curr_level`: `words.difference_update({"dot", "lot"})`.
- Active dictionary: `{"dog", "log", "cog"}`.
- Neighbors of `"dot"`:
  - Mutate index 2 (`'t'` $\to$ `'g'`): `"dog"` $\in$ `words`.
  - $\text{parents}[\text{"dog"}].\text{append}(\text{"dot"})$.
- Neighbors of `"lot"`:
  - Mutate index 2 (`'t'` $\to$ `'g'`): `"log"` $\in$ `words`.
  - $\text{parents}[\text{"log"}].\text{append}(\text{"lot"})$.
- `next_level = {"dog", "log"}`.
- Advance: `curr_level = {"dog", "log"}`.

---

### Level 3: `curr_level = {"dog", "log"}`
- Retire `curr_level`: `words.difference_update({"dog", "log"})`.
- Active dictionary: `{"cog"}`.
- Neighbors of `"dog"`:
  - Mutate index 0 (`'d'` $\to$ `'c'`): `"cog"` $\in$ `words`.
  - $\text{parents}[\text{"cog"}].\text{append}(\text{"dog"})$.
- Neighbors of `"log"`:
  - Mutate index 0 (`'l'` $\to$ `'c'`): `"cog"` $\in$ `words`.
  - $\text{parents}[\text{"cog"}].\text{append}(\text{"log"})$.
  *(Notice: "cog" receives two parents from the same tier!)*
- `endWord = "cog"` is in `next_level`!
- Set `found = True`. BFS halts!

---

### Phase 2: Backtracking from `"cog"`
- $\text{parents}[\text{"cog"}] = [\text{"dog"}, \text{"log"}]$:
  - Branch 1 through `"dog"`:
    - $\text{parents}[\text{"dog"}] = [\text{"dot"}]$
    - $\text{parents}[\text{"dot"}] = [\text{"hot"}]$
    - $\text{parents}[\text{"hot"}] = [\text{"hit"}]$
    - Reconstruct: `["hit", "hot", "dot", "dog", "cog"]`.
  - Branch 2 through `"log"`:
    - $\text{parents}[\text{"log"}] = [\text{"lot"}]$
    - $\text{parents}[\text{"lot"}] = [\text{"hot"}]$
    - $\text{parents}[\text{"hot"}] = [\text{"hit"}]$
    - Reconstruct: `["hit", "hot", "lot", "log", "cog"]`.

Output: `[["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]`.

---

## 4. Complete Execution Trace

### Predecessor DAG Construction Graph

```text
Level 0:                "hit"
                          |
Level 1:                "hot"
                       /     \
Level 2:            "dot"   "lot"
                      |       |
Level 3:            "dog"   "log"
                       \     /
Level 4:                "cog"
```

| BFS Level $d$ | Frontier `curr_level` | Words Retired from Dict | Discovered Successors | Added Predecessor Edges | Destination Found? |
|:---:|:---|:---|:---|:---|:---:|
| 0 | `["hit"]` | `{"hit"}` | `"hot"` | $\text{parents}[\text{"hot"}] = [\text{"hit"}]$ | No |
| 1 | `["hot"]` | `{"hot"}` | `"dot"`, `"lot"` | $\text{parents}[\text{"dot"}] = [\text{"hot"}]$, $\text{parents}[\text{"lot"}] = [\text{"hot"}]$ | No |
| 2 | `["dot", "lot"]` | `{"dot", "lot"}` | `"dog"`, `"log"` | $\text{parents}[\text{"dog"}] = [\text{"dot"}]$, $\text{parents}[\text{"log"}] = [\text{"lot"}]$ | No |
| **3** | **`["dog", "log"]`** | **`{"dog", "log"}`** | **`"cog"`** | **$\text{parents}[\text{"cog"}] = [\text{"dog"}, \text{"log"}]$** | **Yes (`"cog"`)** |
| 4 | - | - | - | **Halt BFS** | - |

### Hamming Distance Versus Discovered Depth

The number of differing positions between a word and `"hit"` is only a lower bound on its ladder length, because every intermediate word must itself appear in the dictionary.

| Dictionary word | Hamming distance from `"hit"` | Discovered at BFS depth $d$ | Why the two numbers coincide or differ |
|:---|:---:|:---:|:---|
| `"hot"` | 1 | 1 | They coincide: one substitution at index 1 turns `'i'` into `'o'`. |
| `"dot"` | 2 | 2 | They coincide because `"hot"` sits on the shortest route; index 0 then changes from `'h'` to `'d'`. |
| `"lot"` | 2 | 2 | The same predecessor `"hot"` reaches `"lot"` through the alternative index-0 substitution. |
| `"dog"` | 3 | 3 | `'d'` and `'o'` are already in place, so only index 2 must change from `'t'` to `'g'`. |
| `"log"` | 3 | 3 | The mirror case: index 0 became `'l'` at depth $2$ and only index 2 changes to `'g'` at depth $3$. |
| `"cog"` | 3 | 4 | The bound of 3 is unreachable: no dictionary word is one substitution from `"cog"` *and* one from `"hot"`, so the ladder must detour through a fourth word. |

---

## 5. Algorithmic Correctness

**Soundness.** BFS discovers nodes in strict order of edge distance from `beginWord`. Any path constructed by following predecessor edges from `endWord` backward to `beginWord` consists solely of edges $(u, v)$ where $\text{dist}(u) = \text{dist}(v) - 1$. Therefore, every reconstructed sequence is strictly a shortest path.

**Completeness.** By deferring the removal of visited words until after each tier completes, all parallel paths reaching the same node at the same minimal depth are preserved in `parents`. Halting once `endWord` is detected prevents exploring sub-optimal longer paths.

---

## 6. Traps This Instance Exposes

- **Immediate Word Removal (The Parallel Parent Erasure Bug):** If `"cog"` is removed from `words` the instant `"dog"` discovers it, then `"log"` will not find `"cog"` in `words`, missing the second valid shortest path `["hit", "hot", "lot", "log", "cog"]`. Words must be removed level-by-level, not neighbor-by-neighbor.
- **Storing Full Paths in BFS Queues (Memory Explosion TLE):** Storing full paths `[["hit", "hot", ...], ...]` inside the queue duplicates sub-paths combinatorially. Separating BFS into parent graph construction followed by DFS path extraction runs an order of magnitude faster.
- **Missing `endWord` Check:** If `endWord` $\notin$ `wordList`, return `[]` immediately before running any search.

### Boundary and Degenerate Instances

| Instance | Input condition | Expected output | Why the algorithm produces it |
|:---|:---|:---|:---|
| `beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot", "dot", "dog", "lot", "log", "cog"]` | Two dictionary routes of equal length converge on `"cog"` | The two 5-word ladders | `"dog"` and `"log"` both record `"cog"` as a successor in the same tier, so the predecessor map stores both parents and backtracking emits both sequences. |
| The same words without `"cog"` in `wordList` | `endWord` is absent from the dictionary | `[]` | The membership guard rejects the request before the first expansion, so no level is ever built. |
| `beginWord = "a"`, `endWord = "c"`, `wordList = ["a", "b", "c"]` | Length-$1$ words; the target is one substitution away | `[["a", "c"]]` | Among the $L \times 26 = 26$ candidate mutations of `"a"`, the string `"c"` itself is present, so `"c"` enters the frontier at depth $1$ and the search halts; the longer `"a" → "b" → "c"` route is never emitted. |
| `beginWord = "red"`, `endWord = "tax"`, `wordList = ["ted", "tex", "rex", "tad", "den", "pee", "tax"]` | Three routes of the same length converge | The three 4-word ladders | `"tex"` is discovered from both `"ted"` and `"rex"` at depth $2$, so its predecessor set has two entries, and `"tax"` is discovered at depth $3$ from both `"tad"` and `"tex"`. |
| `beginWord = "abc"`, `endWord = "xyz"`, `wordList = ["xbc", "xya", "ayz", "xyz"]` | `endWord` is in the dictionary but unreachable | `[]` | The only listed neighbour of `"abc"` is `"xbc"`, and no single substitution of `"xbc"` lands on `"xya"`, `"ayz"`, or `"xyz"`, so the next frontier is empty and the search ends without a destination. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot L \cdot 26 + K \cdot L)$, where $N$ is the number of words, $L$ is word length ($L \le 10$), and $K$ is the number of shortest paths. Each word generates $L \times 26$ candidates, evaluated against a hash set in $O(L)$ time.
- **Auxiliary Space Complexity:** $O(N \cdot L)$ to store the dictionary, the predecessor map, and the queue frontiers.
