# Guided Example: Word Squares

We trace the step-by-step prefix tree (Trie) indexing, prefix-constrained depth-first backtracking, column-to-row symmetry extraction ($\text{pref} = [w_i[k]]_{i=0}^{k-1}$), and dead-end pruning on representative dictionary word lists:

- **Input:** $words = [\text{"area"}, \text{"lead"}, \text{"wall"}, \text{"lady"}, \text{"ball"}]$
- **Required output:** `[["ball", "area", "lead", "lady"], ["wall", "area", "lead", "lady"]]`
  - Word length: $L = 4$, Total words: $N = 5$
  - Step 1 (Index all words in a prefix Trie):
    - Root branches to `'a'` (`area`), `'l'` (`lead`, `lady`), `'w'` (`wall`), `'b'` (`ball`).
  - Step 2 (Backtracking from Row 0 = `"ball"`):
    - Row 0 placed: `b a l l`
    - Column 1 of Row 0 is `'a'` $\implies$ Row 1 must start with prefix `"a"`.
    - Trie query for `"a"`: yields `["area"]`.
    - Row 1 placed: `a r e a`.
    - Column 2 of Rows 0 and 1: Row 0 has `'l'`, Row 1 has `'e'` $\implies$ Row 2 must start with prefix `"le"`.
    - Trie query for `"le"`: yields `["lead"]`.
    - Row 2 placed: `l e a d`.
    - Column 3 of Rows 0, 1, 2: Row 0 has `'l'`, Row 1 has `'a'`, Row 2 has `'d'` $\implies$ Row 3 must start with prefix `"lad"`.
    - Trie query for `"lad"`: yields `["lady"]`.
    - Row 3 placed: `l a d y`.
    - Size 4 reached $\implies$ Word square 1 found: `["ball", "area", "lead", "lady"]`.
  - Step 3 (Backtracking from Row 0 = `"wall"`):
    - Prefix constraints identically yield: `"area"`, `"lead"`, `"lady"`.
    - Word square 2 found: `["wall", "area", "lead", "lady"]`.
  - Step 4 (Pruning invalid starters):
    - Start with Row 0 = `"area"`: Column 1 is `'r'`.
    - Trie query for `"r"`: empty! Pruned immediately after 1 step.
- **Word Reuse Instance:** $words = [\text{"abat"}, \text{"baba"}, \text{"atan"}, \text{"atal"}] \implies \text{"baba"}$ reused at rows 0 and 2.
- **Single Character Instance:** $words = [\text{"a"}] \implies [[\text{"a"}]]$

This instance demonstrates how Trie prefix indexing accelerates backtracking from exponential permutations $O(N^L)$ down to pruned branch-and-bound, mathematically proves the column-prefix constraint invariant, and derives $O(N \cdot L + K \cdot L)$ runtime bounds.

---

## 1. Instance & Teaching Goal

Given a list of unique strings $words = [\text{"area"}, \text{"lead"}, \text{"wall"}, \text{"lady"}, \text{"ball"}]$ (all of length $L = 4$):
Find all **word squares** that can be constructed using these words. The same word may be used multiple times.

```text
Word Square 1:              Word Square 2:
  b  a  l  l                  w  a  l  l
  a  r  e  a                  a  r  e  a
  l  e  a  d                  l  e  a  d
  l  a  d  y                  l  a  d  y

(Row k reads identically to Column k for all k = 0 .. 3)
```

### The Combinatorial Explosion Challenge
Brute-force selection evaluates $N^L = 5^4 = 625$ candidate grids (or $1000^4 = 10^{12}$ on large inputs).
However, in a valid word square:
**The choice of the first $k$ rows completely dictates the required prefix of row $k$!**
- For row 0: any word can be placed.
- For row 1: its first letter must equal column 1 of row 0: $w_0[1]$.
- For row 2: its first two letters must equal column 2 of rows 0 and 1: $w_0[2] + w_1[2]$.
- For row $k$: its prefix of length $k$ is determined by the $k$-th column of all preceding rows:
  $$
  \text{pref}_k = \sum_{i=0}^{k-1} w_i[k]
  $$
By maintaining a Trie, we look up all words matching $\text{pref}_k$ in $O(k)$ time, instantly pruning dead branches where no dictionary word matches the required prefix.

---

## 2. Conceptual Foundation & Invariants

### 1. The Prefix Deduction Rule:
At depth $k$ of backtracking (having successfully placed $k$ rows $w_0, \dots, w_{k-1}$):
- Construct the prefix required for row $k$:
  $$
  \text{prefix} = w_0[k] \cdot w_1[k] \cdots w_{k-1}[k]
  $$
- Query the Trie with $\text{prefix}$.
- If the result list is empty: no word can form a symmetric column $k$. Backtrack immediately!
- If the result list contains candidate indices $\{i_1, i_2, \dots\}$: explore each candidate by appending $words[i]$ to the current square and recursing to depth $k+1$.

### 2. The Trie Node Structure:
Each Trie node stores:
- `children[26]`: Pointers to next letter nodes.
- `v`: A list of word indices whose spellings pass through this node (i.e. all words that share this prefix).

> **Prefix Constraint Invariant.** A word $W$ is eligible to be placed as row $k$ if and only if $W[0 \dots k-1] == \sum_{i=0}^{k-1} w_i[k]$.

---

## 3. Step-by-Step Worked Execution

We trace $words = [\text{"area"}, \text{"lead"}, \text{"wall"}, \text{"lady"}, \text{"ball"}]$ ($L = 4$):

---

### Step 1: Populate the Prefix Trie
Each word is inserted into the Trie, appending its word index to every node along its spelling path:
- Node `"a"` stores index of `"area"`.
- Node `"l"` stores indices of `"lead"`, `"lady"`.
- Node `"le"` stores index of `"lead"`.
- Node `"lad"` stores index of `"lady"`.
- Node `"w"` stores index of `"wall"`.
- Node `"b"` stores index of `"ball"`.

---

### Step 2: Trace Search Tree for Row 0 = `"ball"`
Start with partial square: $T = [\text{"ball"}]$. Current depth $k = 1$.

#### Choosing Row 1 ($k = 1$):
- Required prefix: character at column 1 of row 0:
  $$
  \text{pref}_1 = T[0][1] = \text{'a'}
  $$
- Trie lookup for `"a"`: returns `["area"]`.
- Append `"area"`:
  $$
  T = [\text{"ball"}, \text{"area"}]
  $$

#### Choosing Row 2 ($k = 2$):
- Required prefix: column 2 of rows 0 and 1:
  $$
  \text{pref}_2 = T[0][2] + T[1][2] = \text{'l'} + \text{'e'} = \text{"le"}
  $$
- Trie lookup for `"le"`: returns `["lead"]`.
- Append `"lead"`:
  $$
  T = [\text{"ball"}, \text{"area"}, \text{"lead"}]
  $$

#### Choosing Row 3 ($k = 3$):
- Required prefix: column 3 of rows 0, 1, 2:
  $$
  \text{pref}_3 = T[0][3] + T[1][3] + T[2][3] = \text{'l'} + \text{'a'} + \text{'d'} = \text{"lad"}
  $$
- Trie lookup for `"lad"`: returns `["lady"]`.
- Append `"lady"`:
  $$
  T = [\text{"ball"}, \text{"area"}, \text{"lead"}, \text{"lady"}]
  $$

#### Depth $k = 4 == L$:
- A complete word square has been constructed!
- Save `["ball", "area", "lead", "lady"]`.
- Backtrack.

---

### Step 3: Trace Pruned Dead End (Row 0 = `"area"`)
Start with partial square: $T = [\text{"area"}]$. Current depth $k = 1$.
- Required prefix: column 1 of row 0:
  $$
  \text{pref}_1 = T[0][1] = \text{'r'}
  $$
- Trie lookup for `"r"`:
  - Root has no child `'r'` (no word starts with `'r'`).
  - Result: `[]`.
- **Pruned immediately!** Backtrack without generating any child subtrees.

---

## 4. Complete Execution Trace

| Search Path | Placed Rows | Column Vector for Next Row | Required Prefix | Trie Matches | Decision / Action | Resulting Squares |
|:---:|:---|:---|:---:|:---|:---|:---:|
| **Root** | `[]` | — | `""` | All words | Try each as Row 0 | $0$ |
| **Branch 1** | `["area"]` | `[T[0][1]] = ['r']` | `"r"` | `[]` (Empty) | **Prune dead end** | $0$ |
| **Branch 2** | `["lead"]` | `[T[0][1]] = ['e']` | `"e"` | `[]` (Empty) | **Prune dead end** | $0$ |
| **Branch 3** | `["lady"]` | `[T[0][1]] = ['a']` | `"a"` | `["area"]` | Place `"area"` | $0$ |
| $\to$ Row 2 | `["lady", "area"]`| `[T[0][2], T[1][2]]` | `"de"` | `[]` | **Prune dead end** | $0$ |
| **Branch 4** | `["ball"]` | `['a']` | `"a"` | `["area"]` | Place `"area"` | $0$ |
| $\to$ Row 2 | `["ball", "area"]`| `['l', 'e']` | `"le"` | `["lead"]` | Place `"lead"` | $0$ |
| $\to$ Row 3 | `[..., "lead"]` | `['l', 'a', 'd']` | `"lad"` | `["lady"]` | Place `"lady"` | $0$ |
| $\to$ Complete | `["ball", "area", "lead", "lady"]` | — | — | — | **Square #1 Recorded** | **$1$** |
| **Branch 5** | `["wall"]` | `['a']` | `"a"` | `["area"]` | Same cascade | — |
| $\to$ Complete | `["wall", "area", "lead", "lady"]` | — | — | — | **Square #2 Recorded** | **$2$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Letter Words ($words = [\text{"a"}]$):** $L = 1$. Immediately terminates at depth 1 with $[[\text{"a"}]]$ as a valid $1 \times 1$ word square.
- **Word Reusability ($words = [\text{"abat"}, \text{"baba"}, \text{"atan"}, \text{"atal"}]$):** `"baba"` can appear as row 0 and row 2 in the same square (`["baba", "abat", "baba", "atal"]`). The algorithm does not mark words as consumed, correctly allowing reuse.
- **No Symmetric Squares Possible ($words = [\text{"ab"}, \text{"cd"}]$):** Prefixes `"b"` and `"d"` have no matching words. Returns empty list `[]`.

---

## 6. Traps & Common Anti-Patterns

- **Linear Prefix Search Across All Words:** Scanning the entire word list with `startswith()` on every DFS step takes $O(N)$ per node. For $N = 1000$, this results in millions of string scans and Time Limit Exceeded. The Trie prefix list lookups execute in $O(L)$ time.
- **Forgetting Word Reuse:** Using a `visited` set to prevent using the same word twice produces wrong answers on inputs where diagonal or repeated words are required (e.g. palindromic squares).
- **Constructing Column Strings with Quadratic Slicing:** Repeatedly building substrings with string concatenation creates memory garbage. Extracting characters into a temporary list buffer and querying the Trie minimizes allocations.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Building the Trie with $N$ words of length $L$ takes $O(N \cdot L)$ time.
  - At each DFS level $k$, prefix lookup takes $O(k) \le O(L)$ time.
  - Because prefix constraints aggressively prune non-viable branches, the search tree visits only viable states.
  - Total Time: $\mathcal{O}(N \cdot L + K \cdot L)$, where $K$ is the number of valid partial square configurations. For typical inputs, this executes in $\approx 25$ ms.
- **Auxiliary Space Complexity:**
  - The Trie stores at most $N \cdot L$ nodes, each holding index lists.
  - Backtracking call stack depth is strictly bounded by word length $L \le 5$.
  - Total Auxiliary Space: $\mathcal{O}(N \cdot L)$ to store the Trie and output lists.
