# Guided Example: Short Encoding of Words

We trace the step-by-step word reference string encoding with hash delimiter (`'#'`), suffix absorption property ($w_1 \text{ is suffix of } w_2$), reversed word prefix tree (Trie) insertion ($w[::-1]$), leaf node depth summation ($\sum_{leaf} (\text{depth} + 1)$), and minimal reference string length optimization on representative word sets:

- **Input:**
  $$
  words = [\text{"time"}, \; \text{"me"}, \; \text{"bell"}]
  $$
- **Required output:** `10`
  - Reference string encoding rules:
    - A valid encoding consists of a single reference string $s$ where every encoded word ends with the delimiter character `'#'`.
    - Every word in $words$ must appear as a substring in $s$ that terminates immediately before one of the `'#'` characters.
    - Objective: Find the **minimum length** of the reference string $s$.
    - For $words = [\text{"time"}, \text{"me"}, \text{"bell"}]$:
      - Notice that `"me"` is an exact suffix of `"time"`.
      - If we construct the block `"time#"`, the substring starting at index 2 and ending at index 4 is `"me"`.
      - Thus, `"time#"` simultaneously encodes **both** `"time"` and `"me"` without extra characters!
      - The word `"bell"` does not share a suffix with `"time"`, so it requires its own block: `"bell#"`.
      - Concatenated reference string:
        $$
        s = \text{"time\#bell\#"}
        $$
      - Length of $s$: $5 + 5 = \mathbf{10}$.
- **Suffix Tree Absorption & Reversed Trie Invariant:**
  - **The Suffix Absorption Principle:**
    - A word $u$ can share the encoding of word $v$ if and only if $u$ is a **suffix** of $v$:
      $$
      u \text{ is a suffix of } v \iff v.\text{endswith}(u)
      $$
    - If $u$ is a suffix of $v$, the cost of encoding $u$ is $0$ once $v$ is encoded!
    - Therefore, only words that are **not suffixes of any other word** require independent blocks of length $|w| + 1$ (accounting for the trailing `'#'`).
  - **Reversed Trie Representation:**
    - Testing whether word $u$ is a suffix of word $v$ is equivalent to testing whether the reversed string $u^R = u[::-1]$ is a **prefix** of $v^R = v[::-1]$!
    - Insert the reversed forms of all words into a prefix tree (Trie):
      - `"time"` reversed is `"emit"`.
      - `"me"` reversed is `"em"`.
      - `"bell"` reversed is `"lleb"`.
    - In the Trie:
      - `"em"` is an internal prefix ancestor along the branch to `"emit"`.
      - Node `"m"` in `"em"` has a child `"i"` leading to `"emit"`.
      - Therefore, `"em"` is an **internal node**, while `"emit"` is a **leaf node**!
    - **Depth Summation Rule:**
      - Only **leaf nodes** in the reversed Trie represent maximal, non-absorbed words.
      - If a leaf node is at depth $d$ from the root (where depth is the word length):
        $$
        \text{encoded block length} = d + 1 \quad (\text{word characters} + \text{delimiter})
        $$
      - The total minimum encoding length is simply the sum of $(d + 1)$ across all leaf nodes in the Trie!
- **Step-by-Step Worked Execution Trace on $[\text{"time"}, \text{"me"}, \text{"bell"}]$:**
  - **Phase 0: Reverse Input Words:**
    - `"time"` $\to \mathbf{\text{"emit"}}$ (Length 4)
    - `"me"` $\to \mathbf{\text{"em"}}$ (Length 2)
    - `"bell"` $\to \mathbf{\text{"lleb"}}$ (Length 4)
  - **Phase 1: Build Reversed Prefix Trie:**
    - Initialize root node (depth 0).
    - **Insert `"emit"`:**
      - $\text{root} \xrightarrow{\text{'e'}} N_1 \xrightarrow{\text{'m'}} N_2 \xrightarrow{\text{'i'}} N_3 \xrightarrow{\text{'t'}} N_4$.
    - **Insert `"em"`:**
      - Trace $\text{root} \xrightarrow{\text{'e'}} N_1 \xrightarrow{\text{'m'}} N_2$.
      - Node $N_2$ already exists! No new nodes added.
    - **Insert `"lleb"`:**
      - $\text{root} \xrightarrow{\text{'l'}} N_5 \xrightarrow{\text{'l'}} N_6 \xrightarrow{\text{'e'}} N_7 \xrightarrow{\text{'b'}} N_8$.
  - **Phase 2: Traverse Trie to Identify Leaves and Depths:**
    - Root has two branches: `'e'` and `'l'`.
    - **Branch 1 (`'e'`):**
      - $N_1$ (`'e'`, depth 1): has child $N_2$ $\implies$ Not a leaf.
      - $N_2$ (`'m'`, depth 2, corresponds to `"me"`): has child $N_3$ (`'i'`) $\implies \mathbf{Internal\ Node\ (Absorbed!)}$
      - $N_3$ (`'i'`, depth 3): has child $N_4$ $\implies$ Not a leaf.
      - $N_4$ (`'t'`, depth 4, corresponds to `"time"`): has NO children $\implies \mathbf{Leaf\ Node!}$
      - Contribution of leaf $N_4$:
        $$
        \text{length} + 1 = 4 + 1 = \mathbf{5}
        $$
    - **Branch 2 (`'l'`):**
      - Path leads to leaf $N_8$ (`'b'`, depth 4, corresponds to `"bell"`): has NO children $\implies \mathbf{Leaf\ Node!}$
      - Contribution of leaf $N_8$:
        $$
        \text{length} + 1 = 4 + 1 = \mathbf{5}
        $$
  - **Phase 3: Aggregate Encoded Length:**
    $$
    ans = 5 + 5 = \mathbf{10}
    $$
- **Single Letter Trace ($words = [\text{"t"}]$):**
  - Reversed: `"t"`.
  - Leaf at depth 1.
  - Encoding: `"t#"` $\implies$ length $1 + 1 = \mathbf{2}$.
- **Duplicate Words Trace ($words = [\text{"time"}, \text{"time"}]$):**
  - Both map to the exact same path in the Trie $\implies$ only 1 leaf $\implies$ length **5**.
- **No Overlapping Suffixes ($words = [\text{"cat"}, \text{"dog"}]$):**
  - Both words are leaves $\implies (3 + 1) + (3 + 1) = \mathbf{8}$ (`"cat#dog#"`).

This instance demonstrates formal language suffix covering and factor monoid minimization via dual prefix tree compactification, mathematically proves why reversed Trie leaves form a minimal suffix-free code covering the input vocabulary, and derives $O(\sum |w_i|)$ runtime and $O(\Sigma \cdot \sum |w_i|)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a list of words:
Find the **minimum length** of a reference string ending in `'#'` characters where every word appears ending at a `'#'`.

```text
words = [ "time", "me", "bell" ]

Notice: "me" is a suffix of "time".
We can encode both as "time#":
  "time" starts at index 0
  "me"   starts at index 2

"bell" needs its own block: "bell#"

Reference string: "time#bell#"
Length: 5 + 5 = 10
Result: 10
```

### The Invariant of Reversed Trie Leaves
- $u$ is a suffix of $v \iff u^R$ is a prefix of $v^R$.
- When reversed words are inserted into a Trie, a word is absorbed if it is an internal ancestor of another word.
- Only **leaves** in the reversed Trie represent words that need their own `'#'` block.
- Each leaf of word length $L$ contributes $L + 1$ characters.

---

## 2. Conceptual Foundation & Invariants

### 1. Suffix Equivalence:
$$
w_i \text{ absorbed by } w_j \iff w_j.\text{endswith}(w_i) \iff w_i^R \text{ is prefix of } w_j^R
$$

### 2. Leaf Depth Summation:
$$
\text{Total Length} = \sum_{u \in \text{Leaves}(\text{Trie})} (\text{depth}(u) + 1)
$$

> **Suffix-Free Code Invariant.** The optimal reference string corresponds to the shortest concatenation of a minimal suffix-free sub-vocabulary $W^* \subseteq words$ whose suffix closure covers $words$. In the reversed Trie, $W^*$ is the set of leaf paths.

---

## 3. Step-by-Step Worked Execution

We trace $words = [\text{"time"}, \text{"me"}, \text{"bell"}]$:

---

### Step 1: Reverse Words
- `"emit"`, `"em"`, `"lleb"`.

---

### Step 2: Build Trie
- Path `"emit"` contains `"em"` as a prefix.
- Path `"lleb"` is a separate branch.

---

### Step 3: Identify Leaves
- Leaf 1: `"emit"` at depth 4 $\implies 4 + 1 = 5$.
- Node `"em"` is internal (has child `'i'`) $\implies$ absorbed! (0 cost).
- Leaf 2: `"lleb"` at depth 4 $\implies 4 + 1 = 5$.

---

### Step 4: Output
- $5 + 5 = \mathbf{10}$.

---

## 4. Complete Execution Trace

| Word $w$ | Reversed $w^R$ | Trie Node Created / Traversed | Is Leaf Node? | Cost Contributed ($L + 1$) |
|:---:|:---:|:---:|:---:|:---:|
| `"time"` | `"emit"` | Path `e -> m -> i -> t` | **Yes (End of Branch)** | **$5$** |
| `"me"` | `"em"` | Traverses `e -> m` | **No (Internal Node)** | **$0$ (Absorbed)** |
| **`"bell"`** | **`"lleb"`** | **Path `l -> l -> e -> b`** | **Yes (End of Branch)** | **`5`** |
| **Total** | — | — | — | **`10`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Word ($[\text{"t"}]$):** 1 leaf $\implies 1 + 1 = 2$.
- **All Words Identical ($[\text{"a"}, \text{"a"}, \text{"a"}]$):** Single node in Trie $\implies 1 + 1 = 2$.
- **All Words Suffixes of Longest Word ($[\text{"a"}, \text{"ba"}, \text{"cba"}]$):** Only `"cba"` is a leaf $\implies 3 + 1 = 4$.
- **Disjoint Alphabets:** No words share suffixes $\implies \sum (|w_i| + 1)$.

---

## 6. Traps & Common Anti-Patterns

- **Searching Suffixes in Forward Trie:** A standard prefix tree matches prefixes, not suffixes. Suffix matching requires either inserting reversed words or using a suffix tree.
- **Set Removal Approach Without Length Sorting:** If using a hash set `s = set(words)` and removing suffixes `w[k:]`, check that full words are not accidentally removed before their prefixes are processed.
- **Forgetting the `'#'` Delimiter Length:** Each word encoded in the reference string ends with `'#'`, so its block length is $|w| + 1$, not just $|w|$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of words, and $L$ the max word length ($L \le 7$).
  - Inserting each word into Trie takes $\mathcal{O}(L)$.
  - DFS traversal visits each Trie node at most once: $\mathcal{O}(\sum |w_i|)$.
  - Total Time: strictly linear in total characters $\mathcal{O}(\sum |w_i|)$ where $\sum |w_i| \le 1.4 \times 10^4$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\Sigma \cdot \sum |w_i|)$ where $\Sigma = 26$ for the Trie nodes.
