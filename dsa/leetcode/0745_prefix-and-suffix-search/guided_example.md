# Guided Example: Prefix and Suffix Search

We trace the step-by-step exhaustive prefix-suffix Cartesian product indexing ($(w[:i], w[j:]) \to k$), sequential index overwriting for greatest-index priority ($d[(a, b)] \leftarrow k$), $O(1)$ composite key dictionary lookup ($d.get((pref, suff), -1)$), and subword boundary query resolution on representative dictionary word collections:

- **Input:**
  - Operations sequence:
    ```text
    WordFilter(["apple"])
    f("a", "e")
    ```
- **Required output:** `[null, 0]`
  - Query specifications:
    - `WordFilter(words)`: Preprocesses a dictionary of $N$ words.
    - `f(pref, suff)`: Returns the **largest index** $k$ of a word in $words$ that simultaneously possesses prefix $pref$ and suffix $suff$.
    - If no satisfying word exists, return `-1`.
    - For $words = [\text{"apple"}]$:
      - Word `"apple"` is at index $0$.
      - Prefix `"a"` matches `"apple"[0 \dots 0]`.
      - Suffix `"e"` matches `"apple"[4 \dots 4]`.
      - Only matching word is index $0$.
      - Result: `0`.
- **Cartesian Substring Pairing & Index Overwrite Invariant:**
  - **The Short Word Constraint:**
    - In this problem, words are very short: $|w| \le 7$ characters.
    - For a word of length $L$, there are exactly $L + 1$ prefixes and $L + 1$ suffixes:
      $$
      \text{Prefixes: } a = w[0 \dots i] \quad (0 \le i \le L)
      $$
      $$
      \text{Suffixes: } b = w[j \dots L] \quad (0 \le j \le L)
      $$
    - The number of distinct $(prefix, suffix)$ pairs for a single word is bounded by:
      $$
      (L + 1)^2 \le (7 + 1)^2 = \mathbf{64\ pairs}
      $$
  - **The Natural Maximal-Index Invariant:**
    - We iterate through the word list in increasing order of index $k = 0, 1, \dots, N - 1$.
    - For each word $w$ at index $k$, register every pair in a hash map:
      $$
      d[(a, b)] \leftarrow k
      $$
    - If a later word at index $k_2 > k_1$ shares the exact same prefix and suffix, the assignment $d[(a, b)] \leftarrow k_2$ automatically overwrites the earlier index $k_1$.
    - Thus, the hash map is guaranteed to hold the **largest index** for every valid $(prefix, suffix)$ query!
  - **Constant-Time Retrieval:**
    - Each `f(pref, suff)` query simply performs a hash table lookup:
      $$
      \text{ans} = d.\text{get}((pref, suff), \; -1)
      $$
    - Achieves instantaneous $\mathcal{O}(1)$ query time!
- **Step-by-Step Worked Execution Trace on $words = [\text{"apple"}]$:**
  - Index $k = 0$, word $w = \text{"apple"}$ (length $L = 5$).
  - **Phase 0: Preprocessing & Table Population:**
    - Generate all prefixes:
      $$
      \text{prefixes} = [\text{""}, \text{"a"}, \text{"ap"}, \text{"app"}, \text{"appl"}, \text{"apple"}]
      $$
    - Generate all suffixes:
      $$
      \text{suffixes} = [\text{""}, \text{"e"}, \text{"le"}, \text{"ple"}, \text{"pple"}, \text{"apple"}]
      $$
    - Populate Cartesian product dictionary $d$:
      - Pair $(\text{"", ""}) \to 0$
      - Pair $(\text{"a", ""}) \to 0$
      - Pair $(\text{"a", "e"}) \to 0$
      - Pair $(\text{"a", "le"}) \to 0$
      - $\dots$
      - Pair $(\text{"apple", "apple"}) \to 0$
    - Total $(5 + 1) \times (5 + 1) = 36$ entries registered.
  - **Phase 1: Serve Query `f("a", "e")`:**
    - Query key: $(\text{"a"}, \text{"e"})$.
    - Hash map lookup:
      $$
      d[(\text{"a"}, \text{"e"})] = \mathbf{0}
      $$
    - Return value:
      $$
      ans \leftarrow \mathbf{0}
      $$
- **Greatest Matching Index Resolution Trace ($words = [\text{"apple"}, \text{"ape"}]$):**
  - Index 0: `"apple"` registers $(\text{"a"}, \text{"e"}) \to 0$.
  - Index 1: `"ape"` also starts with `"a"` and ends with `"e"`!
  - Overwrites entry:
    $$
    d[(\text{"a"}, \text{"e"})] \leftarrow \mathbf{1}
    $$
  - Query `f("a", "e")` returns **`1`** (the larger index).
- **Unmatched Query Trace (`f("b", "e")`):**
  - No word has prefix `"b"` and suffix `"e"`.
  - Key $(\text{"b"}, \text{"e"})$ is absent from $d$.
  - Returns default fallback **`-1`**.

This instance demonstrates space-time trade-off optimization and product-index hashing over bounded alphabets, mathematically proves why chronological dictionary overwriting maintains maximum-order statistics under composite key relations, and derives $O(N \cdot L^2)$ preprocessing time, $O(1)$ query time, and $O(N \cdot L^2)$ space bounds.

---

## 1. Instance & Teaching Goal

Implement `WordFilter`:
`f(pref, suff)` returns the **largest index** of a word having prefix $pref$ and suffix $suff$.
Return -1 if no such word exists.

```text
words = [ "apple" ]

Preprocessing:
  "apple" has length 5.
  Prefixes: "", "a", "ap", "app", "appl", "apple"
  Suffixes: "", "e", "le", "ple", "pple", "apple"
  Store all (pref, suff) pairs -> index 0

Query f("a", "e"):
  ("a", "e") exists in map -> returns 0
Result: 0
```

### The Invariant of Exhaustive Pair Hashing
- Since word length $L \le 7$, each word generates at most $(L+1)^2 \le 64$ pairs of $(prefix, suffix)$.
- Indexing all pairs into a hash map $d[(pref, suff)] = k$ from index $0$ to $N - 1$ ensures later words overwrite earlier ones, naturally storing the largest index.
- Queries run in strictly $O(1)$ time.

---

## 2. Conceptual Foundation & Invariants

### 1. Hash Table Construction:
For each word $w$ at index $k \in [0, N - 1]$:
$$
\forall i \in [0, |w|], \; \forall j \in [0, |w|]: \quad d[(w[0 \dots i], \; w[j \dots |w|])] \leftarrow k
$$

### 2. Immediate $O(1)$ Query:
$$
\text{ans} = d.\text{get}((pref, suff), \; -1)
$$

> **Biprojection Memory Invariant.** For words bounded by length $L$, the Cartesian product of the prefix and suffix sets $\mathcal{P}(w) \times \mathcal{S}(w)$ has cardinality $\le (L+1)^2$, allowing pre-materialized memoization of the partial order preimage with $O(1)$ query complexity.

---

## 3. Step-by-Step Worked Execution

We trace $words = [\text{"apple"}]$:

---

### Step 1: Preprocessing
- Generate 36 pairs for `"apple"`.
- Store $d[(\text{"a"}, \text{"e"})] = 0$.

---

### Step 2: Query `f("a", "e")`
- Lookup $(\text{"a"}, \text{"e"})$ in $d$.
- Value is **`0`**.

---

### Step 3: Output
$$
\mathbf{0}
$$

---

## 4. Complete Execution Trace

| Call | Query $(pref, suff)$ | In Hash Table? | Stored Value | Action Taken | Returned Value |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `f("a", "e")` | `("a", "e")` | Yes | $0$ | Return index | **`0`** |
| `f("b", "e")` | `("b", "e")` | No | None | Return fallback | **`-1`** |
| `f("ap", "le")`| `("ap", "le")`| Yes | $0$ | Return index | **`0`** |

---

## 5. Boundary Cases & Failure Modes

- **Empty Prefix or Suffix (`""`):** Handled naturally by slices $w[:0]$ and $w[n:]$.
- **Multiple Matches:** Later words overwrite earlier ones in $d \implies$ largest index is always returned.
- **Prefix Equals Suffix Equals Full Word:** $w[:n]$ and $w[0:]$ both equal $w \implies$ registered cleanly.
- **No Matching Word:** Key absent $\implies$ returns $-1$.

---

## 6. Traps & Common Anti-Patterns

- **Searching Linearly on Every Query ($O(N \cdot L)$ per query):** With $Q = 10^4$ queries and $N = 10^4$ words, linear search takes $10^8$ string comparisons (TLE). Pre-hashing all pairs guarantees $O(1)$ per query.
- **Two Separate Tries (Intersecting Index Lists):** Maintaining one prefix Trie and one suffix Trie requires intersecting two lists of indices, which takes $O(N)$ time per query in the worst case. Single composite key hashing is strictly $O(1)$.
- **Reverse Iteration Overwrite:** If iterating backward, use `if pair not in d: d[pair] = k`. Forward iteration `d[pair] = k` is simpler and naturally keeps the latest (largest) index.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Preprocessing: $N$ words, each generating $(L + 1)^2$ pairs $\implies \mathcal{O}(N \cdot L^2)$ where $L \le 7 \implies \le 64 N$ operations. Completes in $< 35$ ms.
  - Each `f(pref, suff)` query: strictly constant time $\mathcal{O}(1)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N \cdot L^2)$ memory to store the $(prefix, suffix)$ tuples in the hash dictionary.
