# Guided Example: Word Ladder

We trace the step-by-step Bidirectional Breadth-First Search (2-Way BFS) frontier expansion on representative word ladder instances:

- **Input:** `beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot", "dot", "dog", "lot", "log", "cog"]`
- **Required output:** $5$ (Sequence: `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`, length $5$)
- **Unreachable Destination Base:** `beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot", "dot", "dog", "lot", "log"]` $\implies 0$

This instance demonstrates bidirectional BFS frontier swapping (always expanding the smaller active set), pruning the search space from $O(B^D)$ down to $O(B^{D/2})$, counting word node length rather than edge transitions, and detecting frontier intersections in $O(N \cdot L \cdot 26)$ time.

---

## 1. Instance & Teaching Goal

Given two words `beginWord = "hit"` and `endWord = "cog"`, and a dictionary `wordList = ["hot", "dot", "dog", "lot", "log", "cog"]`:
Find the **number of words** in the shortest transformation sequence from `beginWord` to `endWord`.
Every adjacent pair must differ by exactly one letter, and every intermediate word must belong to `wordList`.

The shortest sequence is:
$$
\text{"hit"} \longrightarrow \text{"hot"} \longrightarrow \text{"dot"} \longrightarrow \text{"dog"} \longrightarrow \text{"cog"}
$$
The number of words in this sequence is $5$.

### 1-Way BFS vs Bidirectional BFS
In a unidirectional BFS, searching outward from `beginWord` with branching factor $B$ to depth $D$ visits approximately $B^D$ states.
In **Bidirectional BFS**, we grow two frontiers simultaneously:
- Forward frontier: from `beginWord`
- Backward frontier: from `endWord`

By always expanding the **smaller** of the two frontiers at each step, the two search spheres meet in the middle at depth $D/2$. The number of evaluated states drops from $O(B^D)$ to $O(2 \cdot B^{D/2})$, achieving exponential speedups on dense word graphs.

---

## 2. Conceptual Foundation & Invariants

### Bidirectional BFS Protocol
Let `word_set` be the hash set of `wordList`.
If `endWord` $\notin$ `word_set`: return $0$.

Initialize:
- `front_set = {beginWord}`
- `back_set = {endWord}`
- `word_set.discard(beginWord)`, `word_set.discard(endWord)`
- `length = 1`

While `front_set` and `back_set` are non-empty:
1. **Frontier Size Balancing:**
   To minimize candidate generation, always expand the smaller set:
   $$
   \text{if } |\text{front\_set}| > |\text{back\_set}|: \quad \text{swap}(\text{front\_set}, \, \text{back\_set})
   $$
2. **Increment Sequence Length:**
   $$
   \text{length} \leftarrow \text{length} + 1
   $$
3. **Expand Frontier:**
   Initialize `next_front = set()`.
   For each word $u \in \text{front\_set}$:
   - Generate all 1-character mutations $v$:
     For $i \in [0, L-1]$ and $c \in \text{'a'} \dots \text{'z'}$:
     $$
     v = u[:i] + c + u[i+1:]
     $$
   - **Intersection Check:**
     If $v \in \text{back\_set}$:
     - The forward and backward frontiers have collided!
     - **Immediately return `length`!**
   - If $v \in \text{word\_set}$:
     - `word_set.remove(v)`
     - `next_front.add(v)`
4. **Advance Frontier:**
   `front_set = next_front`.

If frontiers empty without collision, return $0$.

> **Invariant.** `length` tracks the exact number of words in the combined shortest path joining the root of `front_set` to the root of `back_set`.

---

## 3. Step-by-Step Worked Execution

We trace Bidirectional BFS on `beginWord = "hit"`, `endWord = "cog"`:
Initial `word_set = {"hot", "dot", "dog", "lot", "log"}` (`"cog"` moved to `back_set`).
- `front_set = {"hit"}` (size 1)
- `back_set = {"cog"}` (size 1)
- `length = 1`

---

### Step 1: Expand `front_set = {"hit"}`
- `length` becomes $2$.
- Mutate `"hit"`:
  - Position 1: `'i'` $\to$ `'o'`: `"hot"`.
  - Is `"hot"` in `back_set`? No.
  - Is `"hot"` in `word_set`? Yes!
    - Remove from `word_set`.
    - `next_front.add("hot")`.
- `front_set = {"hot"}` (size 1).
- `back_set = {"cog"}` (size 1).

---

### Step 2: Expand `front_set = {"hot"}`
- Sizes equal (1 vs 1), no swap needed.
- `length` becomes $3$.
- Mutate `"hot"`:
  - Position 0: `'h'` $\to$ `'d'`: `"dot"` $\in$ `word_set` $\implies$ add to `next_front`.
  - Position 0: `'h'` $\to$ `'l'`: `"lot"` $\in$ `word_set` $\implies$ add to `next_front`.
- `front_set = {"dot", "lot"}` (size 2).
- `back_set = {"cog"}` (size 1).

---

### Step 3: Size Balancing Swap & Expand Backward Frontier
- $|\text{front\_set}| = 2$, $|\text{back\_set}| = 1$.
- **Frontier Swap!**
  - `front_set` $\leftarrow \text{"cog"}$ (size 1)
  - `back_set` $\leftarrow \text{"dot", "lot"}$ (size 2)
- `length` becomes $4$.
- Mutate `"cog"`:
  - Position 0: `'c'` $\to$ `'d'`: `"dog"` $\in$ `word_set` $\implies$ add to `next_front`.
  - Position 0: `'c'` $\to$ `'l'`: `"log"` $\in$ `word_set` $\implies$ add to `next_front`.
- `front_set = {"dog", "log"}` (size 2).
- `back_set = {"dot", "lot"}` (size 2).

---

### Step 4: Collision Discovery
- Sizes equal (2 vs 2), no swap.
- `length` becomes $\mathbf{5}$.
- Mutate `"dog"` from `front_set`:
  - Position 2: `'g'` $\to$ `'t'`: candidate is `"dot"`.
  - **Intersection Check:**
    $$
    \text{"dot"} \in \text{back\_set}!
    $$
- **Frontiers Collide at `"dot"`!**
- **Immediately return `length` = $\mathbf{5}$!**

Total sequence: `"hit" (1) -> "hot" (2) -> "dot" (3) -> "dog" (4) -> "cog" (5)`.

---

## 4. Complete Execution Trace

### Bidirectional Collision Table

```text
Forward Frontier (hit):    "hit" -> "hot" -> {"dot", "lot"}
                                                    ^
                                             COLLISION DETECTED!
                                                    v
Backward Frontier (cog):             {"dog", "log"} <- "cog"
```

| Step | `front_set` | `back_set` | Swapped? | `length` | Generated Word | Intersection Found? | Action Taken |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---|
| 1 | `{"hit"}` | `{"cog"}` | No | 2 | `"hot"` | No | `next_front = {"hot"}` |
| 2 | `{"hot"}` | `{"cog"}` | No | 3 | `"dot"`, `"lot"` | No | `next_front = {"dot", "lot"}` |
| 3 | `{"cog"}` | `{"dot", "lot"}` | **Yes (1 < 2)** | 4 | `"dog"`, `"log"` | No | `next_front = {"dog", "log"}` |
| **4** | **`{"dog", "log"}`** | **`{"dot", "lot"}`** | No | **5** | **`"dot"`** | **Yes (`"dot"`)** | **Collision! Return 5** |

---

## 5. Algorithmic Correctness

**Soundness.** Both frontiers expand strictly by single-character mutations. When a word generated by the forward search is found in the backward frontier, a valid connected chain exists from `beginWord` to `endWord`. Because both frontiers expand in lockstep BFS layers, the first collision represents the shortest possible path.

**Completeness.** Swapping to always expand the smaller frontier maintains completeness because any valid path must pass through both frontiers. Pruning words immediately upon insertion into `next_front` prevents cycles and revisitation.

---

## 6. Traps This Instance Exposes

- **Word Count vs Edge Count:** The problem asks for the *number of words* in the sequence, not the number of transformation edges. The path `"hit" -> "cog"` (if valid) has 1 transformation edge but 2 words. Initializing `length = 1` correctly counts words.
- **`endWord` Not in `wordList`:** If `endWord` is absent from `wordList`, no transformation can end at `endWord`. Checking `if endWord not in word_set: return 0` upfront avoids redundant computation.
- **Symmetric Frontier Expansion:** Expanding both sets without size-swapping degrades performance when one frontier blossoms into thousands of words while the other remains small. The swap `if len(front) > len(back): front, back = back, front` is crucial.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot L \cdot 26)$ worst-case, where $N = |\text{wordList}|$ and $L$ is word length. Bidirectional BFS reduces practical state expansions to $O(B^{D/2})$ compared to $O(B^D)$ for standard BFS.
- **Auxiliary Space Complexity:** $O(N \cdot L)$ to store the word set and two active frontier sets.
