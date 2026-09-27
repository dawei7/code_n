# Guided Example: Longest Word in Dictionary

We trace the step-by-step prefix-tree (Trie) dictionary insertion, incremental prefix validity verification ($\forall k \le |w|, \; w[0 \dots k] \in \text{Words}$), continuous word-ending chain traversal ($\text{node.is\_end} == \text{true}$), dual-criteria optimization ($\max \text{length}$, then $\min \text{lexicographical}$), and candidate comparison on representative vocabulary collections:

- **Input:**
  $$
  words = [\text{"a"}, \; \text{"banana"}, \; \text{"app"}, \; \text{"appl"}, \; \text{"ap"}, \; \text{"apply"}, \; \text{"apple"}]
  $$
- **Required output:** `"apple"`
  - Problem objective:
    - Find the longest word in $words$ that can be built **one character at a time** by other words in $words$.
    - A word $w$ is valid if and only if every single one of its prefixes ($w[0 \dots 0], w[0 \dots 1], \dots, w[0 \dots |w|-1]$) exists in the dictionary.
    - Tie-breaking rules:
      1. Primary criterion: **Maximum string length**.
      2. Secondary criterion: **Smallest lexicographical order** (alphabetical order).
    - For the input:
      - `"banana"` cannot be built because prefix `"b"` is missing.
      - Candidate chain: `"a"` $\to$ `"ap"` $\to$ `"app"` $\to$ `"appl"` $\to$ `"apple"` (length 5).
      - Candidate chain: `"a"` $\to$ `"ap"` $\to$ `"app"` $\to$ `"appl"` $\to$ `"apply"` (length 5).
      - Both `"apple"` and `"apply"` have maximum length 5.
      - Lexicographical tie-breaker: $\text{"apple"} < \text{"apply"}$.
      - Winning word is `"apple"`.
- **Trie Prefix End-Mark & Chain Reachability Invariant:**
  - **The Trie Construction:**
    - Insert all words into a 26-ary prefix tree (Trie).
    - Each node represents a character, containing an `is_end` boolean flag indicating whether the string path from root to that node forms a complete word in $words$.
  - **The Incremental Prefix Invariant:**
    - A word $w = c_0 c_1 \dots c_{L-1}$ is valid if and only if during its root-to-leaf traversal, **every visited node along the path has `is_end == true`**:
      $$
      \text{valid}(w) \iff \bigwedge_{j=0}^{L-1} \text{node}_{c_j}.\text{is\_end} == \mathbf{true}
      $$
    - If even a single intermediate node has `is_end == false`, that prefix is absent from the dictionary, severing the incremental construction chain.
  - **Optimal Candidate Selection:**
    - Track current best word $ans$ (initialized to empty string `""`).
    - For each valid word $w$:
      $$
      \text{If } |w| > |ans| \ \lor \ (|w| == |ans| \ \land \ w < ans): \quad ans \leftarrow w
      $$
- **Step-by-Step Worked Execution Trace on the Vocabulary:**
  - **Phase 0: Build the Trie:**
    - Insert all 7 words into the Trie.
    - Nodes marked with `is_end = true`:
      - Path `a`: `is_end = true`
      - Path `a -> p`: `is_end = true`
      - Path `a -> p -> p`: `is_end = true`
      - Path `a -> p -> p -> l`: `is_end = true`
      - Path `a -> p -> p -> l -> e`: `is_end = true`
      - Path `a -> p -> p -> l -> y`: `is_end = true`
      - Path `b -> a -> n -> a -> n -> a`: `is_end = true` (at final `'a'`)
  - **Phase 1: Evaluate Each Candidate Word:**
    - **Candidate 1: `"a"` (length 1):**
      - Prefix `a`: `is_end = true`.
      - Valid! $|"a"| = 1 > |""| = 0 \implies ans = \mathbf{\text{"a"}}$.
    - **Candidate 2: `"banana"` (length 6):**
      - Inspect path: $b \to a \dots$
      - Node `'b'`: `is_end == false` (word `"b"` does not exist in $words$!).
      - Chain severed at length 1.
      - **Invalid!** Rejected.
    - **Candidate 3: `"app"` (length 3):**
      - Prefixes: `'a'` (true), `'ap'` (true), `'app'` (true).
      - Valid! $|"app"| = 3 > |"a"| = 1 \implies ans = \mathbf{\text{"app"}}$.
    - **Candidate 4: `"appl"` (length 4):**
      - Prefixes: `'a'`, `'ap'`, `'app'`, `'appl'` all have `is_end = true`.
      - Valid! $|"appl"| = 4 > |"app"| = 3 \implies ans = \mathbf{\text{"appl"}}$.
    - **Candidate 5: `"ap"` (length 2):**
      - Valid, but length $2 < 4$. No update.
    - **Candidate 6: `"apply"` (length 5):**
      - Prefixes: `'a'`, `'ap'`, `'app'`, `'appl'`, `'apply'` all have `is_end = true`.
      - Valid! Length $5 > 4 \implies ans = \mathbf{\text{"apply"}}$.
    - **Candidate 7: `"apple"` (length 5):**
      - Prefixes: `'a'`, `'ap'`, `'app'`, `'appl'`, `'apple'` all have `is_end = true`.
      - Valid! Length equals current maximum ($5 == 5$).
      - Compare lexicographical tie-breaker:
        $$
        \text{"apple"} < \text{"apply"} \implies \mathbf{Tie-Breaker\ Won!}
        $$
      - Update best word:
        $$
        ans \leftarrow \mathbf{\text{"apple"}}
        $$
  - **Step 2: Output:**
    $$
    ans = \mathbf{\text{"apple"}}
    $$
- **Single Connected Chain Trace ($words = [\text{"w"}, \text{"wo"}, \text{"wor"}, \text{"worl"}, \text{"world"}]$):**
  - Continuous single-branch progression.
  - Returns **`"world"`**.
- **No Build-able Words ($words = [\text{"apple"}, \text{"banana"}]$):**
  - Neither `"a"` nor `"b"` is present.
  - No word can be built from length 1.
  - Returns empty string `""`.

This instance demonstrates prefix tree (Trie) end-mark validation and multi-objective lexicographical optimization, mathematically proves why contiguous branch validity enforces strict inductive prefix construction, and derives $O(\sum |w|)$ execution time and $O(\sum |w|)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array of words:
Find the **longest word** that can be built one character at a time by other words in the dictionary.
Tie-break by **lexicographically smallest** word.

```text
words = [ "a", "banana", "app", "appl", "ap", "apply", "apple" ]

Validity check (all prefixes must exist):
  "banana": prefix "b" missing -> INVALID
  "apply":  "a", "ap", "app", "appl", "apply" all exist -> VALID (len 5)
  "apple":  "a", "ap", "app", "appl", "apple" all exist -> VALID (len 5)

Tie-break: "apple" < "apply" alphabetically!
Result: "apple"
```

### The Invariant of the Continuous Prefix Chain
- A word of length $L$ is valid if and only if all $L$ of its prefixes are valid dictionary words.
- In a Trie, this means every node along the word's path from root to leaf must have `is_end == True`.

---

## 2. Conceptual Foundation & Invariants

### 1. Incremental Validity Condition:
For word $w = c_0 c_1 \dots c_{L-1}$:
$$
\text{valid}(w) \iff \forall k \in [1, L]: \quad w[0 \dots k-1] \in words
$$

### 2. Selection Total Order:
A word $w_1$ dominates $w_2$ if:
$$
|w_1| > |w_2| \quad \lor \quad (|w_1| == |w_2| \land w_1 <_{lex} w_2)
$$

> **Prefix Tree Order-Ideal Invariant.** The collection of valid words forms a rooted sub-tree of the full Trie containing the root, isomorphic to the maximal connected downward-closed order ideal with respect to the string prefix order.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Insert into Trie
- All words inserted, `is_end` set at terminal nodes.

---

### Step 2: Test Words
- `"a"`: valid (len 1). $ans = \text{"a"}$.
- `"banana"`: 'b' has `is_end = False` $\implies$ invalid.
- `"app"`: valid (len 3). $ans = \text{"app"}$.
- `"appl"`: valid (len 4). $ans = \text{"appl"}$.
- `"apply"`: valid (len 5). $ans = \text{"apply"}$.
- `"apple"`: valid (len 5). $\text{"apple"} < \text{"apply"} \implies ans = \text{"apple"}$.

---

### Step 3: Output
$$
\mathbf{\text{"apple"}}
$$

---

## 4. Complete Execution Trace

| Word Evaluated | Prefix Validity Chain | Chain Fully Intact? | Word Length | Best Word $ans$ | Update Reason |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `"a"` | `[a: True]` | Yes | $1$ | `"a"` | First valid word |
| `"banana"` | `[b: False, ...]` | **No (Broken at 'b')**| $6$ | `"a"` | Missing prefix `"b"` |
| `"app"` | `[a, ap, app: True]` | Yes | $3$ | `"app"` | Longer length ($3 > 1$) |
| `"appl"` | `[a, ap, app, appl: True]`| Yes | $4$ | `"appl"` | Longer length ($4 > 3$) |
| `"apply"` | `[a, ap, app, appl, apply: True]`| Yes | $5$ | `"apply"` | Longer length ($5 > 4$) |
| **`"apple"`** | `[a, ap, app, appl, apple: True]`| **Yes** | **$5$** | **`"apple"`** | **Lexicographical tie-breaker (`"apple" < "apply"`)** |

---

## 5. Boundary Cases & Failure Modes

- **No Word of Length 1:** No word can ever start the chain $\implies$ returns empty string `""`.
- **All Words Form Single Chain:** Returns the longest word.
- **Multiple Distinct Branches:** Correctly chooses the branch with the longest length or alphabetically earlier leaf.
- **All Words Length 1 ($["z", "b", "a"]$):** All valid, length 1 $\implies$ returns `"a"`.

---

## 6. Traps & Common Anti-Patterns

- **Checking Only the Immediate Predecessor ($w[:-1]$):** Checking only that $w[:-1]$ exists does not guarantee $w[:-2]$ exists unless verified recursively or through an inductive table. A Trie search checks all prefixes simultaneously.
- **Inverted Lexicographical Comparison:** For equal lengths, the problem requires the **smallest** lexicographical word (`ans > w`). Do not pick the larger one.
- **Sorting Approach without Length Considerations:** Sorting words alphabetically first without checking lengths fails because shorter words like `"a"` precede `"apple"`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Inserting all words into the Trie: $\mathcal{O}(\sum |w|)$ where $\sum |w|$ is the total number of characters across all words.
  - Validating each word: $\mathcal{O}(|w|)$ steps along the Trie path.
  - Total Time: strictly linear $\mathcal{O}(\sum |w|)$. Completes in $< 10$ ms for $N = 1000, L = 30$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(26 \cdot \sum |w|)$ memory for the Trie node structure.
