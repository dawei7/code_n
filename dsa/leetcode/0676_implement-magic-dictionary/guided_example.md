# Guided Example: Implement Magic Dictionary

We trace the step-by-step prefix tree (Trie) dictionary indexing, depth-first search with exact-edit budget tracking ($diff \in \{0, 1\}$), exact-match branch delegation ($c == w[i] \implies diff$ preserved), single-character substitution branch exploration ($c \ne w[i] \implies diff \leftarrow 1$), exact-1-edit termination validation ($diff == 1 \land node.is\_end$), length mismatch pruning, and identity rejection on representative query words:

- **Input:**
  - Build dictionary: $dictionary = [\text{"hello"}, \; \text{"leetcode"}]$
  - Query sequence:
    ```text
    search("hello");     // return False (exact match has 0 edits, no 1-edit neighbor exists)
    search("hhllo");     // return True  (change index 1 'h' -> 'e' to match "hello")
    search("hell");      // return False (length mismatch, 4 != 5)
    search("leetcoded"); // return False (length mismatch, 9 != 8)
    ```
- **Required outputs:** `[false, true, false, false]`
  - Magic Dictionary contract:
    - You must determine if you can change **exactly one character** in $searchWord$ to form a word present in the dictionary.
    - Crucial boundary condition: An exact match with 0 character changes is **invalid**. The edit distance must equal **strictly 1**.
- **Trie Traversal & Edit Budget Invariant:**
  - **Trie Indexing:**
    - Store all dictionary words in a standard prefix tree (Trie).
    - Mark terminal nodes with $is\_end = \mathbf{True}$.
  - **The Edit Budget State ($diff \in \{0, 1\}$):**
    - Perform a depth-first search $dfs(i, \; node, \; diff)$:
      - $i$: Current character index in $searchWord$ ($0 \le i \le |w|$).
      - $node$: Current node in the Trie.
      - $diff$: Number of character substitutions consumed so far ($0$ or $1$).
  - **Branch Transitions at Step $i$:**
    1. **Matching Character ($c == w[i]$):**
       - If $w[i]$ exists in $node.children$:
         - Traverse down matching child with unchanged edit budget:
           $$
           dfs(i + 1, \; node.children[w[i]], \; diff)
           $$
    2. **Character Substitution ($c \ne w[i]$):**
       - If the edit budget has not yet been used ($diff == 0$):
         - For any child branch $c \in node.children$ where $c \ne w[i]$:
           - Traverse down with budget consumed ($diff \leftarrow 1$):
             $$
             dfs(i + 1, \; node.children[c], \; \mathbf{1})
             $$
  - **Termination Acceptance Criteria:**
    - When all characters in $searchWord$ are traversed ($i == |w|$):
      $$
      \text{Accept} \iff (diff == 1) \quad \land \quad (node.is\_end == \mathbf{True})
      $$
    - If $diff == 0$, exactly zero edits were made $\implies$ **Rejected**.
- **Step-by-Step Worked Execution Trace:**
  - **Dictionary Population:**
    - Insert `"hello"`: `root -> 'h' -> 'e' -> 'l' -> 'l' -> 'o'` ($is\_end = True$).
    - Insert `"leetcode"`: `root -> 'l' -> 'e' -> ... -> 'e'` ($is\_end = True$).
  - **Query 1: `search("hello")`:**
    - We test if changing **exactly 1 character** in `"hello"` can match any dictionary word.
    - **Path 1 (Match All 5 Characters, $diff = 0$):**
      - Traces `root -> 'h' -> 'e' -> 'l' -> 'l' -> 'o'`.
      - At index 5: $node.is\_end = True$, but $diff = 0$!
      - Rejected because 0 edits were made (the problem requires changing exactly 1 character).
    - **Path 2 (Substitute 1 Character, $diff = 1$):**
      - At index 0 ($w[0] = \text{'h'}$): Try other child $c = \text{'l'}$ ($diff = 1$).
        - Next chars of `"hello"` are `"ello"`.
        - Child branch from `'l'` has `'e' -> 'e' -> 't'`, which does not match `"ello"`.
      - At index 1 ($w[1] = \text{'e'}$): Trie node under `'h'` only has child `'e'`. No other child exists.
      - At index 2 ($w[2] = \text{'l'}$): Only child `'l'`.
      - At index 3 ($w[3] = \text{'l'}$): Only child `'l'`.
      - At index 4 ($w[4] = \text{'o'}$): Only child `'o'`.
    - No substitution produces a valid dictionary word.
    - Return **`false`**.
  - **Query 2: `search("hhllo")`:**
    - Search string: `"hhllo"`.
    - **Step $i = 0$ ($w[0] = \text{'h'}$):**
      - Match child `'h'` ($diff = 0$).
      - Advance to node `'h'`.
    - **Step $i = 1$ ($w[1] = \text{'h'}$):**
      - Inspect children of node `'h'`: only child is `'e'`.
      - Since $w[1] = \text{'h'} \ne \text{'e'}$ and $diff = 0$, we perform a **substitution**!
      - Consume edit: $diff \leftarrow 1$.
      - Advance to child node `'e'`.
    - **Step $i = 2$ ($w[2] = \text{'l'}$):**
      - Match child `'l'` under `'e'` ($diff = 1$).
    - **Step $i = 3$ ($w[3] = \text{'l'}$):**
      - Match child `'l'` under `'l'` ($diff = 1$).
    - **Step $i = 4$ ($w[4] = \text{'o'}$):**
      - Match child `'o'` under second `'l'` ($diff = 1$).
    - **Termination Check ($i = 5$):**
      - Current node is terminal `'o'` ($node.is\_end == True$).
      - Edit count: $diff == \mathbf{1}$.
      - Both conditions satisfied:
        $$
        diff == 1 \quad \land \quad node.is\_end \implies \mathbf{True!}
        $$
      - Changing index 1 `'h'` to `'e'` forms `"hello"`.
    - Return **`true`**.
  - **Query 3: `search("hell")`:**
    - Search word has length $4$.
    - In the Trie, the node reached at length 4 is `'l'` (second `'l'` of `"hello"`), which has $is\_end = False$.
    - Return **`false`**.
  - **Query 4: `search("leetcoded")`:**
    - Length is $9$. Trie path for `"leetcode"` terminates at length $8$.
    - Child `'d'` does not exist under terminal `'e'`.
    - Return **`false`**.

This instance demonstrates branch-and-bound Hamming distance verification over prefix trees, mathematically proves why strict exact-1-edit requirements reject identical zero-distance string queries, and derives $O(\Sigma \cdot L)$ search time and $O(N \cdot L)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a dictionary:
Implement a Magic Dictionary that checks if changing **exactly 1 character** in `searchWord` produces a word in the dictionary.

```text
Dictionary: ["hello", "leetcode"]

1. search("hello"):
   Identical to "hello" (0 changes).
   No other word in dictionary is 1 change away.
   Returns FALSE! (Must change EXACTLY ONE character).

2. search("hhllo"):
   Change index 1 'h' -> 'e' produces "hello".
   Returns TRUE!

3. search("hell"):
   Length 4 != 5. Cannot match by 1 replacement.
   Returns FALSE!
```

### The Invariant of the Exact Hamming Distance $d = 1$
- A query is valid if and only if there exists a dictionary word $W$ with length $|W| = |searchWord|$ such that their Hamming distance is strictly 1:
  $$
  d_H(searchWord, \; W) = 1
  $$
- Words of different lengths or words with distance 0 or $\ge 2$ are rejected.

---

## 2. Conceptual Foundation & Invariants

### 1. The Branching DFS Recurrence:
At index $i$ and Trie node $u$ with difference budget $diff \in \{0, 1\}$:
$$
\text{If } w[i] \in u.children \implies \text{test } dfs(i + 1, \; u.children[w[i]], \; diff)
$$
$$
\text{If } diff == 0 \implies \forall c \in u.children \setminus \{w[i]\}: \text{test } dfs(i + 1, \; u.children[c], \; 1)
$$

### 2. Termination Predicate:
At $i == |w|$:
$$
\text{Accept} \iff (diff == 1 \land u.is\_end)
$$

> **Hamming Sphere-1 Boundary Invariant.** A word $w$ is accepted if and only if the intersection of the radius-1 Hamming sphere $S_1(w)$ and the language $\mathcal{L}(\text{Trie})$ is non-empty.

---

## 3. Step-by-Step Worked Execution

We trace $searchWord = \text{"hhllo"}$ against Trie holding `"hello"`:

---

### Step 1: $i = 0$ ($'h'$)
- Match child `'h'`. $diff = 0$.

---

### Step 2: $i = 1$ ($'h'$)
- Child `'h'` does not exist.
- Child `'e'` exists $\ne \text{'h'}$.
- Substitute `'h'` to `'e'`. $diff \leftarrow 1$.

---

### Step 3: $i = 2, 3, 4$ ($'l', 'l', 'o'$)
- Match `'l'`, `'l'`, `'o'` with $diff = 1$.

---

### Step 4: End of Word ($i = 5$)
- At terminal node `'o'`.
- $diff == 1$ and $is\_end == True \implies \mathbf{true}$.

---

## 4. Complete Execution Trace

| Query Word | Character Traversal Path | Edits Consumed $diff$ | Reached Terminal? | Exact-1 Acceptance | Output |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `"hello"` | `'h' \to 'e' \to 'l' \to 'l' \to 'o'` | $0$ (Exact match) | Yes | **Rejected ($diff \ne 1$)** | **`false`** |
| **`"hhllo"`** | **`'h' \to 'e'(\text{sub}) \to 'l' \to 'l' \to 'o'`** | **`1`** | **Yes** | **Accepted ($diff == 1$)** | **`true`** |
| `"hell"` | `'h' \to 'e' \to 'l' \to 'l'` | $0$ | No (Not terminal) | Rejected | **`false`** |
| `"leetcoded"` | Length 9 | — | Dead end at 8 | Rejected | **`false`** |

---

## 5. Boundary Cases & Failure Modes

- **Single-Letter Dictionary ($["a"], searchWord = "b"$):** $1$ edit from `'b'` to `'a'` $\implies$ `true`.
- **Single-Letter Identical ($["a"], searchWord = "a"$):** $0$ edits $\implies$ `false`.
- **Length Mismatch:** Fails immediately when path length differs.
- **Alphabet Size 26:** At most 25 substitution branches explored at each character position.

---

## 6. Traps & Common Anti-Patterns

- **Accepting Exact Matches:** Thinking that because `"hello"` is in the dictionary, `search("hello")` should return `true`. You MUST modify a character!
- **Allowing Multiple Edits:** If two characters differ, the second difference must be rejected.
- **Modifying the Query String Explicitly ($26 \times L$ searches):** Generating all mutated strings takes $26 \times L$ lookups; Trie DFS pruning explores only existing branches.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `buildDict`: $\mathcal{O}(\sum L)$ to construct the Trie.
  - `search(w)`:
    - At most one substitution branch is taken ($diff = 0 \to 1$).
    - Branching explores at most $26$ children at one position, then follows exact matches.
    - Total Time per search: $\mathcal{O}(26 \cdot L)$ where $L$ is word length. For $L \le 100$, executes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\Sigma \cdot \sum L)$ for the Trie nodes.
