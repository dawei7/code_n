# Guided Example: Word Abbreviation

We trace the step-by-step equivalence partitioning by length and terminal character ($(\text{len}(w), w[-1])$), prefix Trie frequency indexing ($node.cnt$), shortest unique prefix discovery ($node.cnt == 1$), abbreviation compression formatting ($prefix + count + suffix$), and brevity threshold validation ($cnt + 2 \ge \text{len}(w) \implies w$) on representative word vocabularies:

- **Input:**
  $$
  words = [\text{"like"}, \text{"god"}, \text{"internal"}, \text{"me"}, \text{"internet"}, \text{"interval"}, \text{"intension"}, \text{"face"}, \text{"intrusion"}]
  $$
- **Required output:**
  $$
  [\text{"l2e"}, \text{"god"}, \text{"internal"}, \text{"me"}, \text{"i6t"}, \text{"interval"}, \text{"inte4n"}, \text{"f2e"}, \text{"intr4n"}]
  $$
  - Abbreviation specification:
    1. Prefix of length $k \ge 1$.
    2. Followed by the number of omitted characters ($\text{len}(w) - k - 1$).
    3. Followed by the last character $w[-1]$.
    4. Each abbreviation must be **unique** among all words.
    5. If an abbreviation does not make the word strictly shorter ($\text{abbreviation length} \ge \text{word length} \iff k + 2 \ge \text{len}(w)$), keep the original word.
- **Bucket Partitioning & Trie Frequency Trace:**
  - Words can only conflict with each other if they share the **exact same length and the exact same last character**.
  - Group words into equivalence buckets by $(m, w[-1])$:
    - Bucket $(4, \text{'e'})$: `["like", "face"]`
    - Bucket $(3, \text{'d'})$: `["god"]`
    - Bucket $(2, \text{'e'})$: `["me"]`
    - Bucket $(8, \text{'t'})$: `["internet"]`
    - Bucket $(8, \text{'l'})$: `["internal", "interval"]`
    - Bucket $(9, \text{'n'})$: `["intension", "intrusion"]`
- **Bucket-by-Bucket Trie Resolution:**
  - **Case A: No Conflict in Bucket:**
    - `"like"` in bucket $(4, \text{'e'})$: Unique prefix `'l'` (length $k = 1$).
      - Abbreviation: $\text{'l'} + (4 - 1 - 1) + \text{'e'} = \mathbf{\text{"l2e"}}$. Length 3 < 4 (Shortens word!).
    - `"face"` in bucket $(4, \text{'e'})$: Unique prefix `'f'` $\implies \mathbf{\text{"f2e"}}$.
    - `"internet"` in bucket $(8, \text{'t'})$: Unique prefix `'i'` $\implies \text{'i'} + (8 - 1 - 1) + \text{'t'} = \mathbf{\text{"i6t"}}$.
  - **Case B: Length Threshold Retains Original Word:**
    - `"god"` (length 3): $k = 1 \implies \text{'g'} + 1 + \text{'d'} = \text{"g1d"}$ (length 3 == 3). Not shorter $\implies$ Retain **`"god"`**.
    - `"me"` (length 2): $k = 1 \implies 1 + 2 \ge 2 \implies$ Retain **`"me"`**.
  - **Case C: Conflict Resolution via Trie (`"internal"` vs `"interval"` in bucket $(8, \text{'l'})$):**
    - Insert both into bucket Trie:
      - Node `'i'`: $cnt = 2$ (Shared)
      - Node `'n'`: $cnt = 2$ (Shared)
      - Node `'t'`: $cnt = 2$ (Shared)
      - Node `'e'`: $cnt = 2$ (Shared)
      - Node `'r'`: $cnt = 2$ (Shared)
      - Next character diverges!
        - For `"internal"`: letter `'n'` has $cnt = 1$!
          - Shortest unique prefix: `"intern"` (length $k = 6$).
          - Candidate abbreviation: $\text{"intern"} + (8 - 6 - 1) + \text{'l'} = \text{"intern1l"}$ (length 8).
          - Length check: $6 + 2 = 8 \ge 8$ (not shorter than original 8 letters!).
          - Abbreviation does not save space $\implies$ Retain original **`"internal"`**!
        - For `"interval"`: letter `'v'` has $cnt = 1$!
          - Shortest unique prefix: `"interv"` (length $k = 6$).
          - Length check: $6 + 2 \ge 8 \implies$ Retain original **`"interval"`**!
  - **Case D: Conflict with Valid Shortening (`"intension"` vs `"intrusion"` in bucket $(9, \text{'n'})$):**
    - Insert both into bucket Trie:
      - `'i'`: $cnt = 2$, `'n'`: $cnt = 2$, `'t'`: $cnt = 2$.
      - Next letter diverges:
        - For `"intension"`: letter `'e'` has $cnt = 1$!
          - Shortest unique prefix: `"inte"` (length $k = 4$).
          - Omitted characters: $9 - 4 - 1 = \mathbf{4}$.
          - Abbreviation: $\text{"inte"} + \text{"4"} + \text{"n"} = \mathbf{\text{"inte4n"}}$ (length 6 < 9!).
        - For `"intrusion"`: letter `'r'` has $cnt = 1$!
          - Shortest unique prefix: `"intr"` (length $k = 4$).
          - Abbreviation: $\text{"intr"} + \text{"4"} + \text{"n"} = \mathbf{\text{"intr4n"}}$ (length 6 < 9!).
  - Assembled final abbreviations:
    $$
    [\text{"l2e"}, \text{"god"}, \text{"internal"}, \text{"me"}, \text{"i6t"}, \text{"interval"}, \text{"inte4n"}, \text{"f2e"}, \text{"intr4n"}]
    $$

This instance demonstrates partitioned trie-based prefix disambiguation, mathematically proves why partitioning by $(length, terminal)$ isolates all abbreviation collisions, and derives $O(\sum |w|)$ runtime and $O(\sum |w|)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of $n$ distinct strings $words$:
Abbreviate each word such that:
1. An abbreviation begins with a prefix, followed by the count of omitted letters, and ends with the last letter.
2. Every abbreviation must be **unique** across the entire dataset.
3. The prefix should be as short as possible.
4. If an abbreviation does not make the word shorter (i.e. length $\ge$ original length), keep the original word.

```text
Conflicting Pair: "intension" vs "intrusion"
  Both have length 9 and end in 'n'.
  Initial 1-letter prefix: "i7n" vs "i7n" -> CONFLICT!
  Extend prefix:
    "intension" -> prefix "inte" is unique (length 4) -> "inte4n" (length 6 < 9)
    "intrusion" -> prefix "intr" is unique (length 4) -> "intr4n" (length 6 < 9)
```

### The Invariant of Collision Partitions
- Two words $w_1$ and $w_2$ can produce identical abbreviations **if and only if**:
  $$
  \text{len}(w_1) == \text{len}(w_2) \quad \text{and} \quad w_1[-1] == w_2[-1]
  $$
- Words with different lengths or different ending characters can never conflict, even if their prefixes overlap!
- Therefore, we can partition the dictionary into independent buckets indexed by the tuple:
  $$
  \text{Key} = (\text{len}(w), \; w[-1])
  $$
- For each bucket independently, we build a **Prefix Trie** where each node tracks $node.cnt$ (how many words in this bucket share this prefix).
- The shortest unique prefix is simply the first node in the Trie with $node.cnt == 1$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Prefix Trie:
In each bucket Trie:
- `insert(w)`: Walk character by character; increment $node.cnt \leftarrow node.cnt + 1$.
- `search(w)`: Walk character by character until the first node where $node.cnt == 1$.
  Return the prefix length $k$ at that node.

### 2. The Abbreviation Formatting & Brevity Rule:
For a word $w$ with unique prefix length $k$:
- Number of omitted letters:
  $$
  \text{omitted} = \text{len}(w) - k - 1
  $$
- Abbreviated string:
  $$
  w[:k] + \text{str}(\text{omitted}) + w[-1]
  $$
- **Brevity Check:**
  If $k + 2 \ge \text{len}(w)$ (where $+2$ represents the 1-letter suffix and at least 1 digit):
  The abbreviation is not shorter than the original word.
  We must retain the original word $w$.

> **Trie Branching Invariant.** Finding the first node with $node.cnt == 1$ identifies the shortest prefix that distinguishes $w$ from all other words in its collision bucket.

---

## 3. Step-by-Step Worked Execution

We trace bucket $(9, \text{'n'})$ containing `["intension", "intrusion"]`:

---

### Step 1: Insert Words into Bucket Trie
1. Insert `"intension"`:
   Nodes: `i(1) -> n(1) -> t(1) -> e(1) -> n(1) -> s(1) -> i(1) -> o(1) -> n(1)`
2. Insert `"intrusion"`:
   Shared prefix: `i(2) -> n(2) -> t(2)`
   Divergence: `r(1) -> u(1) -> s(1) -> i(1) -> o(1) -> n(1)`

---

### Step 2: Search Shortest Unique Prefix for `"intension"`
- Step 1: `'i'` $\implies cnt = 2$ (Shared).
- Step 2: `'n'` $\implies cnt = 2$ (Shared).
- Step 3: `'t'` $\implies cnt = 2$ (Shared).
- Step 4: `'e'` $\implies cnt = \mathbf{1}$ (Unique!).
- Unique prefix length: $k = 4$.
- Prefix: `"inte"`.

---

### Step 3: Format Abbreviation for `"intension"`
- Length of word: $9$.
- Omitted count: $9 - 4 - 1 = \mathbf{4}$.
- Suffix: `'n'`.
- Abbreviation:
  $$
  \text{"inte"} + \text{"4"} + \text{"n"} = \mathbf{\text{"inte4n"}}
  $$
- Brevity check: $k + 2 = 4 + 2 = 6 < 9 \implies$ Valid!

---

### Step 4: Search Shortest Unique Prefix for `"intrusion"`
- `'i'` ($2$) $\to$ `'n'` ($2$) $\to$ `'t'` ($2$) $\to$ `'r'` ($cnt = \mathbf{1}$).
- Unique prefix length: $k = 4$. Prefix: `"intr"`.
- Omitted count: $9 - 4 - 1 = \mathbf{4}$.
- Abbreviation:
  $$
  \text{"intr"} + \text{"4"} + \text{"n"} = \mathbf{\text{"intr4n"}}
  $$
- Brevity check: $4 + 2 = 6 < 9 \implies$ Valid!

---

## 4. Complete Execution Trace

| Word $w$ | Collision Bucket | Unique Prefix $w[:k]$ | Prefix Length $k$ | Brevity Condition $k + 2 < \text{len}(w)$ | Final Output |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `"like"` | $(4, \text{'e'})$ | `"l"` | $1$ | $1 + 2 = 3 < 4$ (Yes) | **`"l2e"`** |
| `"god"` | $(3, \text{'d'})$ | `"g"` | $1$ | $1 + 2 = 3 \ge 3$ (No) | **`"god"`** |
| `"internal"` | $(8, \text{'l'})$ | `"intern"` | $6$ | $6 + 2 = 8 \ge 8$ (No) | **`"internal"`** |
| `"me"` | $(2, \text{'e'})$ | `"m"` | $1$ | $1 + 2 = 3 \ge 2$ (No) | **`"me"`** |
| `"internet"` | $(8, \text{'t'})$ | `"i"` | $1$ | $1 + 2 = 3 < 8$ (Yes) | **`"i6t"`** |
| `"interval"` | $(8, \text{'l'})$ | `"interv"` | $6$ | $6 + 2 = 8 \ge 8$ (No) | **`"interval"`** |
| `"intension"` | $(9, \text{'n'})$ | `"inte"` | $4$ | $4 + 2 = 6 < 9$ (Yes) | **`"inte4n"`** |
| `"face"` | $(4, \text{'e'})$ | `"f"` | $1$ | $1 + 2 = 3 < 4$ (Yes) | **`"f2e"`** |
| `"intrusion"` | $(9, \text{'n'})$ | `"intr"` | $4$ | $4 + 2 = 6 < 9$ (Yes) | **`"intr4n"`** |

---

## 5. Boundary Cases & Failure Modes

- **Short Words ($\text{len}(w) \le 3$):** An abbreviation of `"god"` is `"g1d"` (length 3). Since it does not save space, the original word is always retained.
- **Words That Differ Only at the Very End (`"abcdef"`, `"abcdeg"`):** Handled automatically because they end in different letters, placing them in different buckets!
- **Identical Common Prefix Up to Second-to-Last Letter (`"abcdz"`, `"abcez"`):** Requires prefix of length 4, leaving 0 omitted characters $\implies 4 + 2 \ge 5$, retaining original words.

---

## 6. Traps & Common Anti-Patterns

- **Building a Single Global Trie for All Words:** If you build a single Trie without partitioning by length and last letter, words like `"intern"` (len 6) and `"internet"` (len 8) would falsely conflict with each other in the Trie even though their abbreviations could never collide.
- **Forgetting the Brevity Rule ($k + 2 \ge \text{len}(w)$):** Generating abbreviations that have the same or greater length than the original word violates Rule 4. Retaining the original word is strictly required.
- **Iterative Conflict Extension Without Tries:** Repeatedly scanning the list to resolve conflicts takes $O(N^2 \cdot L)$ time. Trie-based prefix frequency indexing resolves all shortest unique prefixes in linear time $O(N \cdot L)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of words and $L$ be the maximum word length.
  - Inserting all words into their respective bucket Tries takes $O(N \cdot L)$ time.
  - Querying each word for its unique prefix takes $O(L)$ time.
  - Total Time: $\mathcal{O}(N \cdot L)$. For $N = 400, L = 400$, finishes in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N \cdot L)$ space to store the Trie nodes across all buckets.
