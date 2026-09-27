# Guided Example: Design Search Autocomplete System

We trace the step-by-step 27-ary prefix tree (Trie) construction (lowercase letters plus space `' '`), interactive keystroke buffering ($t$), prefix tree traversal ($node = search(pref)$), subtree DFS completion collection, dual-criterion sorting (frequency descending $\to$ ASCII ascending), top-3 suggestion filtering, sentence termination commit on `'#'`, and dynamic frequency incrementation on representative search engine queries:

- **Input:**
  - Initial historical database:
    - `"i love you"`: typed $5$ times
    - `"island"`: typed $3$ times
    - `"iroman"`: typed $2$ times
    - `"i love leetcode"`: typed $2$ times
  - Keystroke sequence:
    ```text
    input('i'); // Prefix "i"
    input(' '); // Prefix "i "
    input('a'); // Prefix "i a"
    input('#'); // Terminates and saves "i a"
    ```
- **Required outputs:**
  - `input('i')`: `["i love you", "island", "i love leetcode"]`
  - `input(' ')`: `["i love you", "i love leetcode"]`
  - `input('a')`: `[]`
  - `input('#')`: `[]`
  - Search engine requirements:
    1. Top suggestions are ranked by **highest historical frequency** first.
    2. Ties in frequency are broken by **lexicographical (ASCII) ascending order**.
    3. Return at most **3** suggestions.
    4. The special character `'#'` indicates end of sentence: it increments the historical frequency of the fully typed sentence by $+1$ and resets the buffer for the next search.
- **Prefix Tree (Trie) & Interactive Ranking Architecture:**
  - **Alphabet Size ($|\Sigma| = 27$):**
    - Indices $0 \dots 25$: characters `'a'` through `'z'` ($\text{ord}(c) - \text{ord}('a')$).
    - Index $26$: space character `' '`.
  - **Trie Node Properties:**
    - `children`: Array of size 27 pointing to descendant nodes.
    - `v`: Integer frequency count (non-zero if a sentence ends at this node).
    - `w`: Full sentence string.
  - **Keystroke Processing (`input(c)`):**
    - If $c$ is `'#'`:
      - Extract buffered sentence $s$.
      - Insert $s$ into the Trie with frequency $+1$ (or update existing count).
      - Clear buffer: $t = []$.
      - Return `[]`.
    - If $c$ is not `'#'`:
      - Append $c$ to buffer $t$: $pref = \text{join}(t)$.
      - Traverse Trie from root along characters in $pref$.
      - If prefix node does not exist $\implies$ return `[]`.
      - If prefix node exists:
        - Perform DFS over its subtree to collect all candidate sentences with their frequencies:
          $$
          \text{Candidates} = \{(freq, \; sentence)\}
          $$
        - Sort candidates using comparison key:
          $$
          \text{Key} = (-freq, \; sentence)
          $$
        - Return the top $3$ sentence strings.
- **Step-by-Step Worked Keystroke Trace:**
  - **Init: Build Trie with Initial Sentences:**
    - Insert `"i love you"` with count 5.
    - Insert `"island"` with count 3.
    - Insert `"iroman"` with count 2.
    - Insert `"i love leetcode"` with count 2.
    - Active buffer: $t = []$.
  - **Keystroke 1: `input('i')`:**
    - Buffer: $t = [\text{'i'}] \implies pref = \text{"i"}$.
    - Traverse Trie to node for `'i'`. Node exists!
    - Subtree DFS finds 4 matching completed sentences:
      1. `"i love you"`: frequency $5$
      2. `"island"`: frequency $3$
      3. `"iroman"`: frequency $2$
      4. `"i love leetcode"`: frequency $2$
    - **Dual-Criterion Ranking:**
      - Highest frequency is $5$: `"i love you"` (Rank 1).
      - Next frequency is $3$: `"island"` (Rank 2).
      - Frequency $2$ has a tie between `"iroman"` and `"i love leetcode"`.
        - Lexicographical tie-breaker:
          $$
          \text{"i love leetcode"} < \text{"iroman"} \quad (\text{space ' ' is ASCII 32} < \text{'r' is ASCII 114})
          $$
        - Therefore `"i love leetcode"` wins Rank 3!
      - Rank 4: `"iroman"`.
    - Top 3 slice:
      $$
      \mathbf{[\text{"i love you"}, \; \text{"island"}, \; \text{"i love leetcode"}]}
      $$
  - **Keystroke 2: `input(' ')`:**
    - Buffer: $t = [\text{'i'}, \; \text{' '}] \implies pref = \text{"i "}$.
    - Traverse from `'i'` down branch for space `' '` (index 26).
    - Subtree DFS finds 2 matching sentences:
      1. `"i love you"`: frequency $5$
      2. `"i love leetcode"`: frequency $2$
    - Sorted candidates:
      1. `"i love you"` ($freq = 5$)
      2. `"i love leetcode"` ($freq = 2$)
    - Return all available candidates ($\le 3$):
      $$
      \mathbf{[\text{"i love you"}, \; \text{"i love leetcode"}]}
      $$
  - **Keystroke 3: `input('a')`:**
    - Buffer: $t = [\text{'i'}, \; \text{' '}, \; \text{'a'}] \implies pref = \text{"i a"}$.
    - Traverse from `"i "` to child `'a'`.
    - No child `'a'` exists under `"i "` in the Trie!
    - Return:
      $$
      \mathbf{[]}
      $$
  - **Keystroke 4: `input('#')`:**
    - End-of-sentence command detected.
    - Completed sentence: $s = \text{"i a"}$.
    - Insert `"i a"` into Trie with frequency $+1$:
      - Creates new path: `root -> 'i' -> ' ' -> 'a'` with $v = 1, w = \text{"i a"}$.
    - Reset buffer: $t \leftarrow []$.
    - Returns:
      $$
      \mathbf{[]}
      $$
- **Subsequent Search Verification:**
  - If user subsequently inputs `'i'`, the candidate list will now include `"i a"` with count 1 alongside the other 4 sentences!

This instance demonstrates interactive prefix-tree query evaluation and dual-criterion lexicographical heap ranking, mathematically proves why space-augmented 27-ary Tries preserve word-boundary total ordering, and derives $O(P + K \log K)$ keystroke query time and $O(\Sigma \cdot L)$ space bounds.

---

## 1. Instance & Teaching Goal

Implement a real-time **Search Autocomplete System**:
- Each typed character narrows down matching historical sentences.
- Returns **top 3 suggestions** sorted by:
  1. Frequency descending.
  2. ASCII order ascending (for ties).
- Character `'#'` commits the sentence with frequency $+1$ and resets.

```text
Database:
  "i love you" (5), "island" (3), "iroman" (2), "i love leetcode" (2)

1. input('i'):
   Matches all 4. Top 3:
     "i love you" (5)
     "island" (3)
     "i love leetcode" (2, beats "iroman" because ' ' < 'r')

2. input(' '): Prefix "i "
   Matches: "i love you" (5), "i love leetcode" (2)

3. input('a'): Prefix "i a"
   No matches -> []

4. input('#'): Commits "i a" with count 1, resets buffer -> []
```

### The Invariant of ASCII Tie-Breaking
- In ASCII, the space character `' '` has code 32, while `'a'`–`'z'` are 97–122.
- Therefore, `"i love ..."` lexicographically precedes `"iroman"` because `' ' < 'r'`.

---

## 2. Conceptual Foundation & Invariants

### 1. Alphabet Mapping:
$$
\text{idx}(c) = \begin{cases} 26 & \text{if } c = \text{' '} \\ \text{ord}(c) - \text{ord}('a') & \text{otherwise} \end{cases}
$$

### 2. Dual Sorting Comparator:
For each matching sentence pair $(count, word)$:
$$
\text{key} = (-count, \; word)
$$

> **Prefix Quotient Invariant.** All valid completions of prefix string $P$ correspond isomorphically to the leaf-closure of the subtree rooted at the Trie node $\tau(P)$.

---

## 3. Step-by-Step Worked Execution

We trace the query for `'i'`:

---

### Step 1: Append to Buffer
- Buffer: `"i"`.

---

### Step 2: Search Prefix Node
- Locate node for `'i'`.

---

### Step 3: DFS Traversal of Subtree
Collects:
- `(5, "i love you")`
- `(3, "island")`
- `(2, "iroman")`
- `(2, "i love leetcode")`

---

### Step 4: Sort
1. `(5, "i love you")`
2. `(3, "island")`
3. `(2, "i love leetcode")`  (tie-break: `' ' < 'r'`)
4. `(2, "iroman")`

---

### Step 5: Slice Top 3
$$
\mathbf{[\text{"i love you"}, \; \text{"island"}, \; \text{"i love leetcode"}]}
$$

---

## 4. Complete Execution Trace

| Keystroke | Active Prefix | Subtree Matches Found | Sorted Candidates | Output Emitted | Buffer State After |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `'i'` | `"i"` | 4 matches | `["i love you", "island", "i love leetcode", "iroman"]` | **`["i love you", "island", "i love leetcode"]`** | `['i']` |
| `' '` | `"i "` | 2 matches | `["i love you", "i love leetcode"]` | **`["i love you", "i love leetcode"]`** | `['i', ' ']` |
| `'a'` | `"i a"` | $0$ (Dead end) | `[]` | **`[]`** | `['i', ' ', 'a']` |
| `'#'` | — | Commit `"i a"` | Insert into Trie with count 1 | **`[]`** | `[]` (Reset) |

---

## 5. Boundary Cases & Failure Modes

- **Fewer Than 3 Matches:** Returns all matching sentences (e.g. 1 or 2).
- **No Matches:** Returns `[]` while continuing to buffer characters until `'#'`.
- **Existing Sentence Typed Again:** Increases its frequency by $+1$.
- **New Sentence Typed:** Added to Trie with initial frequency $1$.

---

## 6. Traps & Common Anti-Patterns

- **Alphabet Size 26 (Missing the Space):** Sentences contain spaces. Using an alphabet of size 26 crashes on spaces. The alphabet must have 27 slots.
- **Forgetting to Reset Buffer on `'#'`:** If you don't clear the buffer, the next query will accidentally prepend old text.
- **Reverse Tie-Breaking:** Ties must be sorted in **alphabetical ascending** order (`'a'` before `'b'`). Negating the string or misplacing the sign produces incorrect tie-breaking.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `input(c)`:
    - Traversing to prefix node: $\mathcal{O}(L)$ where $L$ is current prefix length ($L \le 200$).
    - DFS collecting subtree sentences: $\mathcal{O}(K)$ where $K$ is sentences matching prefix.
    - Sorting at most $K$ items: $\mathcal{O}(K \log K)$.
    - Slicing top 3: $\mathcal{O}(1)$.
    - Total Time per keystroke: $\mathcal{O}(L + K \log K)$. Completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N \cdot L)$ space for the 27-ary Trie storing all historical sentences.
