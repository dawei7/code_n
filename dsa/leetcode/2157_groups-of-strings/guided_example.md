# Guided Example: Groups of Strings

We analyze and execute the Disjoint Set Union (DSU) graph clustering algorithm on a representative string collection, demonstrating how intermediate single-bit deletion indexing connects words across insertion, deletion, and replacement operations in linear-time factor complexity.

- **Input:** `words = ["a", "b", "ab", "cde"]`
- **Output:** `[2, 3]`

This instance illustrates 26-bit bitmask encoding, single-bit deletion lookahead, bridging replacement neighbors through common sub-masks, and computing component statistics via DSU.

---

## 1. Problem Overview & Representative Instance

We are given an array `words` of strings where each word contains no duplicate lowercase English letters. Each word is viewed purely as an unordered set of characters. Two strings $w_1$ and $w_2$ are **directly connected** if their character sets differ by at most one elementary edit operation:
1. **Addition:** Add any one letter to $w_1$ to form $w_2$.
2. **Deletion:** Delete any one letter from $w_1$ to form $w_2$.
3. **Replacement:** Replace any one letter in $w_1$ with another letter to form $w_2$.

Strings connected directly or via a chain of intermediate connections belong to the same connected component (group). Isolated strings form groups of size $1$.

The goal is to compute two values:
`[total_number_of_groups, size_of_largest_group]`

In our representative instance:
- `words = ["a", "b", "ab", "cde"]` ($n = 4$).
- `"a"` and `"ab"` differ by adding `'b'`.
- `"b"` and `"ab"` differ by adding `'a'`.
- `"a"` and `"b"` differ by replacing `'a'` with `'b'`.
- `"cde"` shares no operations with any of the other three words.

We must partition the strings into connected components and return $[2, 3]$.

---

## 2. Mathematical & Algorithmic Principles

### 26-Bit Bitmask Representation

Because each word has at most $26$ distinct lowercase letters and order does not matter:
- Every word $w$ corresponds uniquely to a 26-bit integer mask:
$$\text{mask}(w) = \sum_{c \in w} 2^{c - \text{'a'}}$$
- The number of characters in $w$ is the population count $\text{popcount}(\text{mask}(w))$.

### The Three Edit Operations in Bitmask Space

Let $M_1$ and $M_2$ be two bitmasks:
1. **Deletion / Addition:** $M_1$ and $M_2$ differ by exactly one set bit:
   $$M_1 \oplus M_2 = 2^b \iff \text{Hamming Distance} = 1$$
2. **Replacement:** $M_1$ and $M_2$ have the same popcount and differ by exactly two bits (one dropped, one added):
   $$M_1 \oplus M_2 = 2^{b_1} + 2^{b_2} \quad \text{with } b_1 \in M_1 \text{ and } b_2 \in M_2$$

### The Intermediate Sub-Mask Bridging Technique

A pairwise check of all $n \times n$ combinations takes $O(n^2)$ time, which is too slow for $n = 20000$ ($4 \times 10^8$ operations). Instead, we invert the neighborhood search:
- Notice that if $M_1$ and $M_2$ are connected by a **replacement** (dropping bit $b_1$ and adding bit $b_2$), they share a common sub-mask:
$$M_{\text{sub}} = M_1 \setminus \{b_1\} = M_2 \setminus \{b_2\}$$
- Similarly, if $M_2$ is formed by **adding** bit $b$ to $M_1$, then $M_1$ is itself the sub-mask $M_2 \setminus \{b\}$.
- Therefore, every connection (addition, deletion, or replacement) can be discovered purely by examining the sub-masks formed by **deleting a single set bit** from each word:
  - For each word with mask $M$, iterate through its set bits $b \in M$.
  - Compute candidate sub-mask $M' = M \setminus \{b\}$.
  - If $M'$ is an existing word in `words`, union $M$ and $M'$.
  - If $M'$ has already been seen as a sub-mask of some other word $M_{\text{prior}}$, union $M$ and $M_{\text{prior}}$ (capturing the replacement operation).

For each word, there are at most $26$ set bits. The number of sub-masks generated is at most $26 \times n$, reducing graph construction to $O(26 \cdot n)$.

| Concept / Data Structure | Formal Definition | Operational Role in Clustering |
|---|---|---|
| Bitmask $M(w)$ | $\sum_{c \in w} 2^{c - \text{'a'}}$ | Compact integer encoding of character presence |
| Disjoint Set Union (DSU) | Forest with rank and path compression | Merges connected word indices, tracks component sizes |
| Word Mask Map | `mask -> word_index` | Detects direct deletion/addition matches in $O(1)$ |
| Sub-Mask Map | `submask -> word_index` | Bridges replacement pairs sharing an identical deletion ancestor |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `words = ["a", "b", "ab", "cde"]` ($n = 4$).

```
Word 0: "a"   -> mask 0b00001 (1)
Word 1: "b"   -> mask 0b00010 (2)
Word 2: "ab"  -> mask 0b00011 (3)
Word 3: "cde" -> mask 0b11100 (28)

DSU initialized: 4 components of size 1.
Word map: { 1: 0, 2: 1, 3: 2, 28: 3 }
Sub-mask map: empty
```

### Step 1: Initialize Word Index Map & DSU
- Populate `word_to_id`:
  - Mask $1 \to$ Word 0 (`"a"`)
  - Mask $2 \to$ Word 1 (`"b"`)
  - Mask $3 \to$ Word 2 (`"ab"`)
  - Mask $28 \to$ Word 3 (`"cde"`)
- DSU tracking: $4$ components:
  - $\{0\}, \{1\}, \{2\}, \{3\}$, each of size $1$.

### Step 2: Process Word 0 (`"a"`, Mask $1$)
- Set bits: bit 0 (`'a'`).
- Remove bit 0: sub-mask $= 1 \setminus \{0\} = 0$.
- Checks:
  - Is $0$ a valid word in `word_to_id`? No.
  - Has sub-mask $0$ been seen before? No. Record in `sub_to_id`: `0 -> Word 0`.
- DSU components: $4$ groups.

### Step 3: Process Word 1 (`"b"`, Mask $2$)
- Set bits: bit 1 (`'b'`).
- Remove bit 1: sub-mask $= 2 \setminus \{1\} = 0$.
- Checks:
  - Is $0$ a valid word in `word_to_id`? No.
  - Has sub-mask $0$ been seen before? Yes! Associated with Word 0 (`"a"`).
  - Action: Union Word 1 (`"b"`) with Word 0 (`"a"`). (Discovers replacement `'a' \leftrightarrow 'b'`).
- DSU components:
  - Group $\{0, 1\}$ of size $2$.
  - Groups $\{2\}$ and $\{3\}$ of size $1$.
  - Total groups: $3$.

### Step 4: Process Word 2 (`"ab"`, Mask $3$)
- Set bits: bit 0 (`'a'`), bit 1 (`'b'`).
- **Iteration 1: Remove bit 0 (`'a'`):**
  - Sub-mask $= 3 \setminus \{0\} = 2$.
  - Is $2$ in `word_to_id`? Yes! Word 1 (`"b"`).
  - Action: Union Word 2 (`"ab"`) with Word 1 (`"b"`).
  - DSU merges group $\{2\}$ into $\{0, 1\}$, creating $\{0, 1, 2\}$ of size $3$.
  - Record sub-mask: `2 -> Word 2`.
- **Iteration 2: Remove bit 1 (`'b'`):**
  - Sub-mask $= 3 \setminus \{1\} = 1$.
  - Is $1$ in `word_to_id`? Yes! Word 0 (`"a"`).
  - Action: Word 2 and Word 0 are already in the same component.
  - Record sub-mask: `1 -> Word 2`.
- DSU components:
  - Group $\{0, 1, 2\}$ of size $3$.
  - Group $\{3\}$ of size $1$.
  - Total groups: $2$.

### Step 5: Process Word 3 (`"cde"`, Mask $28$)
- Set bits: bit 2 (`'c'`), bit 3 (`'d'`), bit 4 (`'e'`).
- Sub-masks:
  - Remove bit 2: mask $28 \setminus \{2\} = 24$. Not in `word_to_id` or `sub_to_id`. Record `24 -> Word 3`.
  - Remove bit 3: mask $28 \setminus \{3\} = 20$. Not in `word_to_id` or `sub_to_id`. Record `20 -> Word 3`.
  - Remove bit 4: mask $28 \setminus \{4\} = 12$. Not in `word_to_id` or `sub_to_id`. Record `12 -> Word 3`.
- No unions formed. Word 3 remains isolated.

### Step 6: Extract Group Statistics
- Component $\{0, 1, 2\}$: size $3$.
- Component $\{3\}$: size $1$.
- Number of groups: $2$.
- Largest group size: $\max(3, 1) = 3$.
- Result: `[2, 3]`.

---

## 4. Comprehensive State Trace

The table below catalogs every word, its set bits, generated sub-masks, and DSU union operations:

| Word ID | String | Mask | Set Bits | Sub-Mask | Encountered Target | Union Operation | Active Components | Largest Size |
|---|---|---|---|---|---|---|---|---|
| $0$ | `"a"` | $1$ | $\{0\}$ | $0$ | None | Record `0 -> 0` | $\{0\}, \{1\}, \{2\}, \{3\}$ | $1$ |
| $1$ | `"b"` | $2$ | $\{1\}$ | $0$ | Seen at `0 -> 0` | Union(1, 0) | $\{0, 1\}, \{2\}, \{3\}$ | $2$ |
| $2$ | `"ab"` | $3$ | $\{0, 1\}$ | $2$ | Word 1 in `word_to_id` | Union(2, 1) | $\{0, 1, 2\}, \{3\}$ | $3$ |
| $2$ | `"ab"` | $3$ | $\{0, 1\}$ | $1$ | Word 0 in `word_to_id` | Already merged | $\{0, 1, 2\}, \{3\}$ | $3$ |
| $3$ | `"cde"` | $28$ | $\{2, 3, 4\}$ | $24, 20, 12$ | None | Record sub-masks | $\{0, 1, 2\}, \{3\}$ | $3$ |

Final grouping summary:
- Total groups: $2$.
- Largest group size: $3$.

---

## 5. Algorithmic Correctness & Soundness

### Completeness of the Deletion-Only Transition Graph
Let $w_1$ and $w_2$ be two words connected by an allowed operation:
1. **$w_2$ is formed by deleting letter $b$ from $w_1$:**
   Then $M(w_2) = M(w_1) \setminus \{b\}$. When word $w_1$ deletes bit $b$, its sub-mask equals $M(w_2)$, which matches `word_to_id[M(w_2)]` and executes `union(w_1, w_2)`.
2. **$w_2$ is formed by adding letter $b$ to $w_1$:**
   Symmetric to deletion. Word $w_2$ deleting bit $b$ produces $M(w_1)$, triggering the exact same union.
3. **$w_2$ is formed by replacing letter $b_1 \in w_1$ with $b_2 \in w_2$:**
   Then $M(w_1) \setminus \{b_1\} = M(w_2) \setminus \{b_2\} = M_{\text{common}}$.
   Whichever word is processed first records $M_{\text{common}}$ in `sub_to_id`. When the second word is processed, it observes $M_{\text{common}}$ in `sub_to_id` and executes `union(w_2, w_1)`.

All three elementary operations are guaranteed to trigger a DSU union, proving that no transitive connectivity path can be missed.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Duplicate Words in Input:** If `words` contains multiple copies of the same string (e.g., `["a", "a"]`), they have identical masks. They must be merged in the DSU and both contribute to component size.
2. **Single Character Words Sharing Sub-mask 0:** Sub-mask $0$ (the empty string) connects all single-character words together if replacement is valid (e.g., `"a"` and `"b"` both reduce to empty mask $0$).
3. **All Words Isolated:** If no two words share a single-bit difference or common sub-mask, the algorithm yields $n$ groups of size $1$.
4. **Length 26 Words (Full Alphabet):** Deleting any of the $26$ characters generates $26$ distinct sub-masks, correctly linking with any word of length $25$.

### Common Anti-Patterns
- **Pairwise $O(n^2)$ Comparison:** Comparing every pair of words directly takes $4 \cdot 10^8$ operations, resulting in Time Limit Exceeded.
- **Generating All Additions ($26$ per word) and Replacements ($26 \times 26$ per word):** Generating all additions and replacements yields $26 + 26 \times 26 = 702$ branch queries per word. Generating *only deletions* ($26$ per word) and bridging replacements through a shared hash map reduces queries from $702$ to $26$ per word.
- **Forgetting Duplicates in Component Sizing:** Overwriting identical mask entries in the DSU without summing their original instance counts undercounts group sizes when duplicate words exist.

---

## 7. Complexity Analysis

### Time Complexity
- **Bitmask Conversion:** Computing bitmasks for $n$ strings of length $\le 26$ takes $O(n \cdot 26)$ time.
- **Graph Construction via Sub-Masks:**
  - For each word, there are at most $26$ set bits.
  - Generating $M \setminus \{b\}$, querying `word_to_id`, and updating `sub_to_id` takes $O(1)$ expected time.
  - Total queries: at most $26 \times n \approx 5.2 \times 10^5$.
- **DSU Operations:** Each union and find with path compression and rank operates in nearly $O(\alpha(n)) \approx O(1)$ time.
- Total time complexity is strictly $O(26 \cdot n)$, executing in approximately $50$ milliseconds for $n = 20000$.

### Auxiliary Space Complexity
- `word_to_id` stores at most $n$ distinct mask entries.
- `sub_to_id` stores at most $26 \cdot n$ sub-mask entries.
- DSU arrays store $n$ parent and size integers.
- Total auxiliary space complexity is $O(26 \cdot n)$, requiring approximately $15$ MB of working memory.
