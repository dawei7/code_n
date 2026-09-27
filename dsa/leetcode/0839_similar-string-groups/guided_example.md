# Guided Example: Similar String Groups

We trace the step-by-step single-transposition similarity predicate ($\text{diff}(s, t) \le 2$), undirected graph modeling, Disjoint Set Union (Union-Find) with path compression and union by rank, transitive connected component chaining, and independent equivalence group tallying on representative anagram vocabularies:

- **Input:**
  $$
  strs = [\text{"tars"}, \text{"rats"}, \text{"arts"}, \text{"star"}]
  $$
- **Required output:** `2`
  - String similarity and group definitions:
    - Two words are **similar** if they are identical or if swapping **at most two letters** in one word produces the other word.
    - Because all words in the input are anagrams of each other, two words are similar if and only if they differ in **at most 2 positions**:
      $$
      \text{diff}(s, t) = \sum_{k=0}^{m-1} \mathbb{I}[s[k] \ne t[k]] \le 2
      $$
    - Similarity forms an undirected graph. Two words belong to the same **group** if there is a path of similar words connecting them (transitive closure).
    - Objective: Return the total number of connected components in the graph.
    - For $strs = [\text{"tars"}, \text{"rats"}, \text{"arts"}, \text{"star"}]$:
      - `"tars"` and `"rats"`: differ at indices 0 and 2 (diff 2) $\implies$ **Similar** (connected by an edge).
      - `"rats"` and `"arts"`: differ at indices 0 and 1 (diff 2) $\implies$ **Similar** (connected by an edge).
      - `"tars"` and `"arts"`: differ at indices 0, 1, 2 (diff 3) $\implies$ Not directly similar, but connected through `"rats"`!
      - Thus, $\{\text{"tars"}, \text{"rats"}, \text{"arts"}\}$ forms a single connected component of size 3.
      - `"star"`: differs from `"tars"` by 4, from `"rats"` by 4, and from `"arts"` by 4 $\implies$ Isolated component of size 1.
      - Total connected groups: **`2`**.
- **Hamming Metric & Disjoint Set Union Invariant:**
  - **Hamming Distance Threshold:**
    - On permutation orbits of equal length $m$, a single 2-cycle transposition $(i \; j)$ alters exactly two coordinate positions:
      $$
      d_H(s, t) \in \{0, 2\} \iff \text{similar}(s, t)
      $$
    - Any pair with $d_H(s, t) > 2$ requires at least two disjoint transpositions or a 3-cycle, meaning they are not adjacent in the similarity graph.
  - **Union-Find Component Reduction:**
    - Initialize Disjoint Set Union (DSU) with $n$ singleton components (one per string).
    - For every unordered pair of strings $(i, j)$ with $j < i$:
      - Count differing positions:
        $$
        d_H = \sum_{k = 0}^{m - 1} \mathbb{I}[strs[i][k] \ne strs[j][k]]
        $$
      - If $d_H \le 2$:
        - Perform union: $\text{union}(i, j)$.
        - If $i$ and $j$ belonged to different sets, they merge into one component, decrementing the total component count:
          $$
          n_{\text{components}} \leftarrow n_{\text{components}} - 1
          $$
    - The final component count is the number of connected groups.
- **Step-by-Step Worked Execution Trace on the 4-Word Vocabulary:**
  - Strings:
    - Node 0: `"tars"`
    - Node 1: `"rats"`
    - Node 2: `"arts"`
    - Node 3: `"star"`
  - Initialize Union-Find on 4 elements:
    $$
    p = [0, 1, 2, 3], \quad size = [1, 1, 1, 1], \quad \text{groups} = 4
    $$
  - **Pair $(1, 0)$ (`"rats"`, `"tars"`):**
    - Position 0: `'r'` vs `'t'` (diff)
    - Position 1: `'a'` vs `'a'` (match)
    - Position 2: `'t'` vs `'r'` (diff)
    - Position 3: `'s'` vs `'s'` (match)
    - Differing count: $d_H = \mathbf{2} \le 2 \implies \mathbf{Similar!}$
    - Union sets: $\text{find}(1) = 1, \text{find}(0) = 0 \implies \text{Merge.}$
    - $p[1] \leftarrow 0, size[0] \leftarrow 2$.
    - Groups remaining: $4 - 1 = \mathbf{3}$.
  - **Pair $(2, 0)$ (`"arts"`, `"tars"`):**
    - Position 0: `'a'` vs `'t'` (diff)
    - Position 1: `'r'` vs `'a'` (diff)
    - Position 2: `'t'` vs `'r'` (diff)
    - Differing count: $d_H = 3 > 2 \implies \mathbf{Not\ directly\ similar.}$
  - **Pair $(2, 1)$ (`"arts"`, `"rats"`):**
    - Position 0: `'a'` vs `'r'` (diff)
    - Position 1: `'r'` vs `'a'` (diff)
    - Position 2: `'t'` vs `'t'` (match)
    - Position 3: `'s'` vs `'s'` (match)
    - Differing count: $d_H = \mathbf{2} \le 2 \implies \mathbf{Similar!}$
    - Union sets: $\text{find}(2) = 2, \text{find}(1) = \text{find}(0) = 0 \implies \text{Merge.}$
    - $p[2] \leftarrow 0, size[0] \leftarrow 3$.
    - Groups remaining: $3 - 1 = \mathbf{2}$.
  - **Pairs Involving Node 3 (`"star"`):**
    - $(3, 0)$ (`"star"`, `"tars"`): $d_H = 4 > 2$.
    - $(3, 1)$ (`"star"`, `"rats"`): $d_H = 4 > 2$.
    - $(3, 2)$ (`"star"`, `"arts"`): $d_H = 4 > 2$.
    - Node 3 has no edges.
  - **Final Component Count:**
    $$
    \text{groups} = \mathbf{2}
    $$
    - Group 1: $\{ \text{"tars"}, \text{"rats"}, \text{"arts"} \}$
    - Group 2: $\{ \text{"star"} \}$
- **Single Swap Pair Trace ($strs = [\text{"omv"}, \text{"ovm"}]$):**
  - Only two strings, differing at indices 1 and 2 ($d_H = 2$).
  - Merged into 1 component $\implies ans = \mathbf{1}$.
- **All Identical Strings Trace ($strs = [\text{"aaa"}, \text{"aaa"}]$):**
  - Differing count $d_H = 0 \le 2 \implies$ merged into 1 component.

This instance demonstrates Cayley graph connectivity over symmetric permutation groups generated by adjacent/non-adjacent transpositions, mathematically proves why equivalence group identification reduces to transitive component detection on sparse intersection graphs, and derives $O(N^2 \cdot M)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a list of anagram strings:
Two strings are **similar** if they differ in at most **2 positions** (one swap or equal).
Connected strings form **groups** (transitive closure).
Find the total number of groups.

```text
strs = [ "tars", "rats", "arts", "star" ]

"tars" <-> "rats": differ at 0, 2 (diff = 2) -> SIMILAR!
"rats" <-> "arts": differ at 0, 1 (diff = 2) -> SIMILAR!
"star": differs by 4 from all others -> ISOLATED

Groups:
  Group 1: { "tars", "rats", "arts" }
  Group 2: { "star" }

Result: 2
```

### The Invariant of the Hamming Distance $\le 2$
- Two equal-length anagrams can be transformed into each other by at most one swap if and only if their Hamming distance is $\le 2$.
- DSU maintains connected components as edges are added.

---

## 2. Conceptual Foundation & Invariants

### 1. Transposition Neighborhood:
$$
\text{Similar}(s, t) \iff \sum_{k=0}^{m-1} \mathbb{I}[s[k] \ne t[k]] \in \{0, 2\}
$$

### 2. DSU Invariant:
$$
\text{Component Count} = n - \sum_{(i, j), i < j} \mathbb{I}[\text{Similar}(s_i, s_j) \land \text{Union}(i, j) \text{ succeeded}]
$$

> **Cayley Quotient Invariant.** The similarity graph is the induced subgraph of the Cayley graph of the symmetric group $S_m$ generated by all $\binom{m}{2}$ transpositions. The connected components partition the vertex set into connected communication classes in this Cayley embedding.

---

## 3. Step-by-Step Worked Execution

We trace $strs = [\text{"tars"}, \text{"rats"}, \text{"arts"}, \text{"star"}]$:

---

### Step 1: Initialize DSU
- 4 elements, 4 groups: $\{0\}, \{1\}, \{2\}, \{3\}$.

---

### Step 2: Compare $(1, 0)$ (`"rats"`, `"tars"`)
- Diff at 0, 2 $\implies d_H = 2 \le 2$.
- Merge 0 and 1 $\implies 3$ groups remaining.

---

### Step 3: Compare $(2, 1)$ (`"arts"`, `"rats"`)
- Diff at 0, 1 $\implies d_H = 2 \le 2$.
- Merge 1 and 2 $\implies 2$ groups remaining: $\{0, 1, 2\}$ and $\{3\}$.

---

### Step 4: Compare Node 3 (`"star"`)
- Diff with all others is $4 > 2$.
- No merges.

---

### Step 5: Output
$$
\mathbf{2}
$$

---

## 4. Complete Execution Trace

| String Pair $(i, j)$ | Characters Compared | Differing Positions | Diff Count $d_H$ | Similar? ($d_H \le 2$) | DSU Merge Action | Groups Remaining |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $(1, 0)$ | `"rats"`, `"tars"` | Indices $0, 2$ | $2$ | **Yes** | Merge $1 \to 0$ | $3$ |
| $(2, 0)$ | `"arts"`, `"tars"` | Indices $0, 1, 2$ | $3$ | No | No action | $3$ |
| **$(2, 1)$** | **`"arts"`, `"rats"`** | **Indices $0, 1$** | **$2$** | **Yes** | **Merge $2 \to 0$** | **`2`** |
| $(3, 0)$ | `"star"`, `"tars"` | All indices | $4$ | No | No action | $2$ |
| $(3, 1)$ | `"star"`, `"rats"` | All indices | $4$ | No | No action | $2$ |
| **$(3, 2)$** | **`"star"`, `"arts"`** | **All indices** | **$4$** | **No** | **No action** | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **All Strings Distinct and Dissimilar:** 0 edges $\implies N$ groups.
- **All Strings Identical ($d_H = 0$):** All merge into $1$ group.
- **Single String ($N = 1$):** Returns $1$.
- **Chain of Swaps ($s_1 \sim s_2 \sim s_3$):** Transitive connectivity merges all into a single group even if $s_1$ and $s_3$ differ in 4 positions.

---

## 6. Traps & Common Anti-Patterns

- **Checking Full Transposition Instead of Counting Differences:** Because all words are guaranteed anagrams, comparing $s[k] \ne t[k]$ and counting differences $\le 2$ is sufficient, faster, and avoids string copying.
- **Early Exit in Difference Counter:** In an inner loop, if diff count exceeds 2, `break` early to save string comparison time.
- **Recomputing Groups at the End:** Decrementing $n$ whenever a successful union occurs eliminates the need for an extra pass to count unique set roots.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Testing all pairs: $\binom{N}{2} = \frac{N(N - 1)}{2}$ pairs.
  - Comparing two strings of length $M$: $\mathcal{O}(M)$ operations.
  - DSU operations with path compression and rank: $\mathcal{O}(\alpha(N)) \approx \mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(N^2 \cdot M)$ where $N \le 300, M \le 300 \implies \le 1.35 \times 10^7$ operations. Completes in $< 35$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for the DSU parent and size arrays.
