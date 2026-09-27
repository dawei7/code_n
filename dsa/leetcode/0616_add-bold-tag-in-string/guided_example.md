# Guided Example: Add Bold Tag in String

We trace the step-by-step dictionary prefix tree (Trie) compilation, sliding multi-pattern substring matching ($[start, end]$ intervals), adjacent and overlapping interval consolidation ($ed + 1 \ge a \implies ed = \max(ed, b)$), boundary string segmentation, and unified HTML tag wrapping (`<b>...</b>`) on representative text strings:

- **Input:** $s = \text{"aaabbb"}, \quad words = [\text{"aa"}, \text{"b"}]$
- **Required output:** `"<b>aaabbb</b>"`
  - Formatting requirements:
    1. Wrap any substring in $s$ that matches any word in $words$ with `<b>` and `</b>`.
    2. **Overlap rule:** If two matching substrings overlap (e.g. indices $0 \dots 1$ and $1 \dots 2$), they must be merged into one single pair of tags.
    3. **Adjacency rule:** If two matching substrings are directly consecutive without gaps (e.g. index $2$ and index $3$), they must also be merged into one single pair of tags.
    4. Unmatched characters remain outside the tags.
- **Trie Multi-Pattern Probing & Interval Merging Architecture:**
  - **Phase 1: Build Prefix Tree (Trie):**
    - Insert all dictionary words into a Trie.
    - Each node represents a prefix; terminal nodes are marked with `is_end = True`.
  - **Phase 2: Extract Matching Intervals:**
    - For each starting position $i \in [0, n - 1]$, traverse the Trie with characters $s[j]$ ($j \ge i$).
    - Whenever a node with `is_end == True` is encountered, record a matching interval:
      $$
      [i, \; j]
      $$
  - **Phase 3: Merge Overlapping and Consecutive Intervals:**
    - Two intervals $[s_1, e_1]$ and $[s_2, e_2]$ (with $s_1 \le s_2$) merge if:
      $$
      e_1 + 1 \ge s_2
      $$
    - If this condition holds, replace both with:
      $$
      [s_1, \; \max(e_1, e_2)]
      $$
  - **Phase 4: String Synthesis:**
    - Stream through $s$, emitting literal characters for gaps and wrapping merged intervals inside `<b>` and `</b>`.
- **Step-by-Step Worked Trace on $s = \text{"aaabbb"}, words = [\text{"aa"}, \text{"b"}]$:**
  - String length $n = 6$, indices $0 \dots 5$.
  - **Step 1: Discover All Matching Substring Intervals:**
    - Index $0$: substring $s[0 \dots 1] = \text{"aa"}$ matches `"aa"` $\implies \mathbf{[0, 1]}$.
    - Index $1$: substring $s[1 \dots 2] = \text{"aa"}$ matches `"aa"` $\implies \mathbf{[1, 2]}$.
    - Index $2$: no match for `"aa"` or `"b"`.
    - Index $3$: substring $s[3 \dots 3] = \text{"b"}$ matches `"b"` $\implies \mathbf{[3, 3]}$.
    - Index $4$: substring $s[4 \dots 4] = \text{"b"}$ matches `"b"` $\implies \mathbf{[4, 4]}$.
    - Index $5$: substring $s[5 \dots 5] = \text{"b"}$ matches `"b"` $\implies \mathbf{[5, 5]}$.
    - Raw interval list:
      $$
      pairs = [[0, 1], \; [1, 2], \; [3, 3], \; [4, 4], \; [5, 5]]
      $$
  - **Step 2: Merge Intervals:**
    - Start active interval: $[st, ed] = [0, 1]$.
    - **Inspect $[1, 2]$:**
      - Condition: $ed + 1 = 1 + 1 = 2 \ge 1 \implies \mathbf{Merge!}$
      - Update end: $ed \leftarrow \max(1, 2) = \mathbf{2}$.
      - Active interval is now $[0, 2]$.
    - **Inspect $[3, 3]$:**
      - Condition: $ed + 1 = 2 + 1 = 3 \ge 3 \implies \mathbf{Merge!}$ (Adjacent touch!).
      - Update end: $ed \leftarrow \max(2, 3) = \mathbf{3}$.
      - Active interval is now $[0, 3]$.
    - **Inspect $[4, 4]$:**
      - Condition: $3 + 1 = 4 \ge 4 \implies \mathbf{Merge!}$
      - Update end: $ed \leftarrow \max(3, 4) = \mathbf{4}$.
      - Active interval is now $[0, 4]$.
    - **Inspect $[5, 5]$:**
      - Condition: $4 + 1 = 5 \ge 5 \implies \mathbf{Merge!}$
      - Update end: $ed \leftarrow \max(4, 5) = \mathbf{5}$.
      - Active interval is now $[0, 5]$.
    - Consolidated intervals:
      $$
      t = [[0, 5]]
      $$
  - **Step 3: Wrap String in HTML Tags:**
    - The consolidated interval covers indices $0 \dots 5$, which is the entire string!
    - Assemble output:
      $$
      \text{"<b>"} + s[0 \dots 5] + \text{"</b>"} = \mathbf{\text{"<b>aaabbb</b>"}}
      $$
- **Separated Intervals Instance ($s = \text{"abcxyz123"}, words = [\text{"abc"}, \text{"123"}]$):**
  - Matches: $[0, 2]$ and $[6, 8]$.
  - Check adjacency: $2 + 1 = 3 < 6 \implies$ Gap of 3 characters (`"xyz"`).
  - Merged intervals: $[0, 2]$ and $[6, 8]$.
  - Output:
    $$
    \mathbf{\text{"<b>abc</b>xyz<b>123</b>"}}
    $$
- **No Matching Words in String:**
  - $pairs = [] \implies$ Returns original string $s$ unchanged.

This instance demonstrates multi-string dictionary matching and adjacent interval unification, mathematically proves why $ed + 1 \ge a$ guarantees minimal non-fragmented HTML tag markup, and derives $O(N \cdot L)$ runtime and $O(N + W)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s$ and a dictionary of words:
Wrap every substring in $s$ matching any word with `<b>` and `</b>`.
Merge overlapping and consecutive matches so tags are not redundant.

```text
s = "aaabbb", words = ["aa", "b"]

Matches:
  [0, 1] "aa"
  [1, 2] "aa" (overlaps with [0, 1])
  [3, 3] "b"  (adjacent to [1, 2])
  [4, 4] "b"  (adjacent to [3, 3])
  [5, 5] "b"  (adjacent to [4, 4])

Merged Interval: [0, 5] (entire string)
Result: "<b>aaabbb</b>"
```

### The Adjacent Merge Invariant
- Standard interval merging only merges overlapping intervals ($ed \ge a$).
- In HTML bold tagging, **consecutive intervals** must also merge:
  - If interval 1 ends at 2 (`"<b>abc</b>"`) and interval 2 begins at 3 (`"<b>def</b>"`), writing `"<b>abc</b><b>def</b>"` is forbidden.
  - The correct output is `"<b>abcdef</b>"`.
  - Testing $ed + 1 \ge a$ unifies both overlapping ($ed \ge a$) and adjacent ($ed + 1 = a$) intervals into one condition.

---

## 2. Conceptual Foundation & Invariants

### 1. Multi-Pattern Matching via Trie:
- Insert all dictionary words into a Trie.
- For each starting index $i$ in $s$:
  - Walk the Trie character by character.
  - If a word terminal is reached at index $j$, emit interval $[i, j]$.

### 2. Consolidated Interval Merging:
For each sorted candidate interval $[a, b]$:
- If $ed + 1 \ge a$:
  $$
  ed \leftarrow \max(ed, b)
  $$
- Else:
  - Save current $[st, ed]$ and start new interval at $[a, b]$.

> **Interval Union Invariant.** Replacing adjacent and overlapping closed intervals with their topological closure minimizes the number of tag pairs while preserving the exact subset of bolded characters.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"aaabbb"}, words = [\text{"aa"}, \text{"b"}]$:

---

### Step 1: Find Substring Matches
- Substring $s[0 \dots 1] = \text{"aa"} \implies [0, 1]$.
- Substring $s[1 \dots 2] = \text{"aa"} \implies [1, 2]$.
- Substring $s[3 \dots 3] = \text{"b"} \implies [3, 3]$.
- Substring $s[4 \dots 4] = \text{"b"} \implies [4, 4]$.
- Substring $s[5 \dots 5] = \text{"b"} \implies [5, 5]$.

---

### Step 2: Merge Consecutive/Overlapping Matches
- Init with $[0, 1]$.
- $[1, 2]$ overlaps ($1 + 1 \ge 1$) $\implies$ span $[0, 2]$.
- $[3, 3]$ touches ($2 + 1 \ge 3$) $\implies$ span $[0, 3]$.
- $[4, 4]$ touches ($3 + 1 \ge 4$) $\implies$ span $[0, 4]$.
- $[5, 5]$ touches ($4 + 1 \ge 5$) $\implies$ span $[0, 5]$.
- Merged set: $\{[0, 5]\}$.

---

### Step 3: Emit HTML
$$
\mathbf{\text{"<b>aaabbb</b>"}}
$$

---

## 4. Complete Execution Trace

| Index Range $[a, b]$ | Matched Word | Active Merged $[st, ed]$ | Merge Trigger Condition | Merged Window After |
|:---:|:---:|:---:|:---:|:---:|
| $[0, 1]$ | `"aa"` | $[0, 1]$ | Initial | $[0, 1]$ |
| $[1, 2]$ | `"aa"` | $[0, 1]$ | $1 + 1 \ge 1$ (Overlap) | $[0, 2]$ |
| $[3, 3]$ | `"b"` | $[0, 2]$ | $2 + 1 \ge 3$ (Adjacent) | $[0, 3]$ |
| $[4, 4]$ | `"b"` | $[0, 3]$ | $3 + 1 \ge 4$ (Adjacent) | $[0, 4]$ |
| $[5, 5]$ | `"b"` | $[0, 4]$ | $4 + 1 \ge 5$ (Adjacent) | **$[0, 5]$** |
| **Output** | — | — | Wrap $[0, 5]$ | **`<b>aaabbb</b>`** |

---

## 5. Boundary Cases & Failure Modes

- **No Matches:** Returns original string $s$.
- **Entire String Matched:** Wraps entire string in a single `<b>...</b>` pair.
- **Multiple Disjoint Matches:** Each group gets its own pair with plain text between them.
- **Repeated Identical Words:** Deduplicated by Trie traversal.

---

## 6. Traps & Common Anti-Patterns

- **Using Standard Interval Merge ($ed \ge a$):** Misses adjacent intervals like $[0, 1]$ and $[2, 3]$, producing ugly fragmented tags `<b>aa</b><b>b</b>`. Use $ed + 1 \ge a$.
- **Nested Tags (`<b>a<b>a</b></b>`):** Occurs if strings are replaced in place without interval consolidation.
- **Repeated String Slicing (`s.find` on every word):** Calling `s.find()` for every word repeatedly takes $O(W \cdot N^2)$. A Trie scans all prefixes in a single forward pass.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Building the Trie: $\mathcal{O}(\sum |w_i|)$.
  - Scanning $s$ with Trie: $\mathcal{O}(N \cdot L_{max})$ where $L_{max}$ is the maximum word length.
  - Merging intervals: $\mathcal{O}(K)$ where $K$ is number of matches.
  - Total Time: $\mathcal{O}(N \cdot L_{max} + \sum |w_i|)$. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\sum |w_i| \cdot |\Sigma|)$ space for the Trie data structure.
  - $\mathcal{O}(N)$ space for the output string builder.
