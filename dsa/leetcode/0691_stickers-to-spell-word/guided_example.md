# Guided Example: Stickers to Spell Word

We trace the step-by-step target character bitmask indexing ($mask \in [0, 2^{|target|}-1]$), breadth-first search (BFS) layer exploration, multiset letter consumption per sticker ($cnt[c] -= 1$), state transition mask composition ($nxt = cur \mid 2^i$), duplicate state pruning ($vis[nxt]$), and minimum sticker count derivation on representative multiset spelling targets:

- **Input:**
  - Stickers available: $stickers = [\text{"with"}, \; \text{"example"}, \; \text{"science"}]$
  - Target word: $target = \text{"thehat"}$
- **Required output:** `3`
  - Spelling mechanics:
    - You may cut individual letters out of any sticker.
    - Each sticker can be chosen repeatedly with an infinite supply.
    - Objective: Assemble the exact character multiset of $target$ using the **minimum number of stickers**.
    - For $target = \text{"thehat"}$:
      - Character breakdown: two `'t'`, two `'h'`, one `'e'`, one `'a'`.
      - Using `"with"` gives: `'t'`, `'h'`.
      - Using `"with"` again gives: `'t'`, `'h'`.
      - Using `"example"` gives: `'e'`, `'a'`.
      - Together, these 3 stickers furnish all required letters: $\{\text{'t'}, \text{'h'}, \text{'t'}, \text{'h'}, \text{'e'}, \text{'a'}\}$.
      - Minimum stickers needed is **3**.
- **Bitmask State Space & Breadth-First Search Invariant:**
  - **The Bitmask Target Encoding:**
    - Let $N = |target| \le 15$.
    - Represent which characters of $target$ have been spelled out using an $N$-bit mask:
      $$
      mask = \sum_{i: target[i] \text{ is covered}} 2^i
      $$
    - Initial state: $mask = 0$ (no characters spelled, 0 stickers used).
    - Goal state: $mask = 2^N - 1$ (all $N$ characters covered).
  - **Shortest Path BFS on Unweighted Graph:**
    - Each transition uses **exactly 1 sticker**, which corresponds to an edge of weight 1 in the state graph.
    - Breadth-First Search (BFS) explores states layer-by-layer: the first time the full mask $2^N - 1$ is dequeued, the current layer index $ans$ is guaranteed to be the **absolute minimum number of stickers**.
  - **Sticker Transition Computation ($cur \to nxt$):**
    - For a candidate sticker $s$ with character frequency table $cnt$:
      - Initialize $nxt = cur$.
      - Iterate over all indices $i \in [0, N - 1]$ of $target$:
        - If bit $i$ is not yet set ($(cur \gg i) \& 1 == 0$) AND $cnt[target[i]] > 0$:
          - Use one copy of this letter: $cnt[target[i]] \leftarrow cnt[target[i]] - 1$.
          - Mark position $i$ as covered: $nxt \leftarrow nxt \mid 2^i$.
      - If $nxt$ has not been visited before ($vis[nxt] == False$):
        - Mark $vis[nxt] = True$ and enqueue $nxt$.
- **Step-by-Step Worked Execution Trace on $target = \text{"thehat"}$ ($N = 6$):**
  - Positions:
    - Index 0: `'t'`
    - Index 1: `'h'`
    - Index 2: `'e'`
    - Index 3: `'h'`
    - Index 4: `'a'`
    - Index 5: `'t'`
  - Full target mask: $2^6 - 1 = 63 = 111111_2$.
  - BFS Queue starts with $mask = 0$, layer $ans = 0$.
  - **Layer 0 (0 Stickers Used):**
    - Dequeue $cur = 0$ ($000000_2$).
    - **Apply Sticker `"with"` (letters: `'w', 'i', 't', 'h'`):**
      - Index 0 (`'t'`): consumes `'t'`, sets bit 0 $\implies nxt = 000001_2$.
      - Index 1 (`'h'`): consumes `'h'`, sets bit 1 $\implies nxt = 000011_2$.
      - Index 3 (`'h'`): no `'h'` left in `"with"`.
      - Index 5 (`'t'`): no `'t'` left in `"with"`.
      - Resulting mask: $nxt = 000011_2 = \mathbf{3}$ (spells $target[0 \dots 1] = \text{"th"}$).
      - Enqueue $3$ into Layer 1.
    - **Apply Sticker `"example"` (letters: `'e', 'x', 'a', 'm', 'p', 'l', 'e'`):**
      - Index 2 (`'e'`): consumes `'e'`, sets bit 2.
      - Index 4 (`'a'`): consumes `'a'`, sets bit 4.
      - Resulting mask: $nxt = 010100_2 = \mathbf{20}$ (spells $target[2, 4] = \text{"ea"}$).
      - Enqueue $20$ into Layer 1.
    - **Apply Sticker `"science"` (letters: `'s', 'c', 'i', 'e', 'n', 'c', 'e'`):**
      - Index 2 (`'e'`): consumes `'e'`, sets bit 2.
      - Resulting mask: $nxt = 000100_2 = 4$.
      - Enqueue $4$ into Layer 1.
  - **Layer 1 (1 Sticker Used):**
    - $ans \leftarrow 1$.
    - Process mask $3$ ($000011_2$, holding `"th"`):
      - Applying `"example"` covers `'e'` (bit 2) and `'a'` (bit 4):
        $$
        nxt = 000011_2 \mid 010100_2 = 010111_2 = \mathbf{23} \quad (\text{"the.a."})
        $$
        Enqueue $23$ into Layer 2.
      - Applying `"with"` covers remaining `'t'` (bit 5) and `'h'` (bit 3):
        $$
        nxt = 000011_2 \mid 101000_2 = 101011_2 = \mathbf{43} \quad (\text{"th.ht"})
        $$
        Enqueue $43$ into Layer 2.
    - Process mask $20$ ($010100_2$, holding `"ea"`):
      - Applying `"with"` covers `'t'` (bit 0) and `'h'` (bit 1):
        $$
        nxt = 010100_2 \mid 000011_2 = 010111_2 = \mathbf{23} \quad (\text{already visited})
        $$
  - **Layer 2 (2 Stickers Used):**
    - $ans \leftarrow 2$.
    - Process mask $23$ ($010111_2$, covered: indices $0, 1, 2, 4$, letters: `'t', 'h', 'e', 'a'`):
      - Missing characters: index 3 (`'h'`) and index 5 (`'t'`).
      - Apply sticker `"with"`:
        - Contains `'t'` and `'h'`!
        - Index 3 (`'h'`): covers bit 3!
        - Index 5 (`'t'`): covers bit 5!
        - New mask:
          $$
          nxt = 010111_2 \mid 101000_2 = 111111_2 = \mathbf{63} \quad \mathbf{(Goal\ Reached!)}
          $$
        - Enqueue $63$ into Layer 3.
  - **Layer 3 (3 Stickers Used):**
    - $ans \leftarrow 3$.
    - Dequeue $cur = 63 = 2^6 - 1$:
      - Goal check: $cur == (1 \ll N) - 1 \implies \mathbf{Complete!}$
      - Return current layer count:
        $$
        ans = \mathbf{3}
        $$
- **Missing Required Letter ($stickers = [\text{"notice"}, \text{"possible"}], target = \text{"basic"}$):**
  - Character `'a'` does not appear in any sticker.
  - BFS exhausts all reachable masks without ever reaching $2^N - 1$.
  - Returns **`-1`**.

This instance demonstrates state space reduction via positional bitmask projection and breadth-first search shortest path extraction on hypercube state graphs, mathematically proves why level-synchronous queue traversal minimizes sticker consumption, and derives $O(S \cdot N \cdot 2^N)$ runtime and $O(2^N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a list of stickers (infinite copies) and a target word:
Find the **minimum number of stickers** needed to cut out letters to spell the target.
If impossible, return $-1$.

```text
stickers = ["with", "example", "science"], target = "thehat"

Target characters: 't', 'h', 'e', 'h', 'a', 't' (length 6)

Layer 0 -> start at empty mask: 000000 (0 stickers)
Layer 1 -> use "with"    -> covers "th...." (mask 000011)
Layer 2 -> use "example" -> covers "the.a." (mask 010111)
Layer 3 -> use "with"    -> covers "..h..t" (mask 111111 -> ALL COVERED!)

Total stickers = 3
Result: 3
```

### The Invariant of BFS on Bitmasks
- Representing each character position of $target$ as a bit in a mask transforms the problem into finding the shortest path from $0$ to $2^N - 1$ in an unweighted directed graph.
- BFS level expansion guarantees that the first time $2^N - 1$ is reached, the number of stickers used is globally minimal.

---

## 2. Conceptual Foundation & Invariants

### 1. Bitmask Encoding:
$$
N = |target| \le 15
$$
$$
mask \in [0, \; 2^N - 1]
$$
Goal: reach $2^N - 1$.

### 2. Transition Operation:
For mask $cur$ and sticker $s$:
$$
nxt = cur \mid \left( \bigcup_{i: (cur \gg i) \& 1 == 0 \land cnt[target[i]] > 0} 2^i \right)
$$
If $vis[nxt] == False \implies vis[nxt] \leftarrow True, \; q.append(nxt)$.

> **Hypercube Reachability Invariant.** The collection of letter choices induces a directed acyclic transit network on the boolean lattice $\{0, 1\}^N$, where BFS exploration discovers the unweighted geodesic from $\mathbf{0}$ to $\mathbf{1}$ in minimum edge hops.

---

## 3. Step-by-Step Worked Execution

We trace $target = \text{"thehat"}$:

---

### Step 1: Layer 0
- Queue: `[0]`.

---

### Step 2: Layer 1
- From 0 with `"with"`: covers bits 0, 1 $\implies mask = 3$ (`"th"`).
- From 0 with `"example"`: covers bits 2, 4 $\implies mask = 20$ (`"ea"`).

---

### Step 3: Layer 2
- From mask 3 with `"example"`: covers bits 2, 4 $\implies mask = 23$ (`"thea"`).

---

### Step 4: Layer 3
- From mask 23 with `"with"`: covers remaining bits 3, 5 $\implies mask = 63$ (`"thehat"`).
- Full mask reached at Layer 3.
- Return **`3`**.

---

## 4. Complete Execution Trace

| BFS Layer | Current Mask $cur$ | Letters Covered | Sticker Applied | Target Letters Consumed | Next Mask $nxt$ | Goal Reached? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $0$ ($000000_2$) | None | `"with"` | `'t'` (0), `'h'` (1) | $3$ ($000011_2$) | No |
| $0$ | $0$ | None | `"example"` | `'e'` (2), `'a'` (4) | $20$ ($010100_2$) | No |
| $1$ | $3$ ($000011_2$) | `"th"` | `"example"` | `'e'` (2), `'a'` (4) | $23$ ($010111_2$) | No |
| **$2$** | **$23$ ($010111_2$)** | **`"thea"`** | **`"with"`** | **`'h'` (3), `'t'` (5)** | **$63$ ($111111_2$)** | **`Yes (Layer 3)`** |

---

## 5. Boundary Cases & Failure Modes

- **Impossible Target:** Missing any letter present in $target \implies$ BFS queue empties $\implies$ returns $-1$.
- **Single Sticker Contains Entire Target:** Reaches $2^N - 1$ on Layer 1 $\implies 1$.
- **Target with All Identical Letters ($target = \text{"aaaa"}$):** Frequency counter correctly decrements letter counts per sticker.
- **Max Target Length $N = 15$:** State space size $2^{15} = 32768$ states, traversed in milliseconds.

---

## 6. Traps & Common Anti-Patterns

- **A* / Dijkstra with Heuristics:** Unweighted transitions make standard level-by-level BFS strictly optimal and simpler without priority queue overhead.
- **Ignoring Duplicate Letters in Target:** Using set intersection fails to account for duplicate characters (e.g. two `'t'`s require two `'t'`s). Frequency counting $cnt[c] -= 1$ correctly tracks distinct occurrences.
- **DFS Without Memoization:** Naive recursion branches exponentially, causing severe Time Limit Exceeded.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Total states in bitmask: at most $2^N$.
  - For each state, iterate through $S$ stickers.
  - For each sticker, scan $N$ characters of target.
  - Total Time: $\mathcal{O}(S \cdot N \cdot 2^N)$. For $N = 15, S = 50$, executes $\approx 2.4 \times 10^7$ operations in $< 50$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(2^N)$ space for the visited boolean array and BFS queue.
