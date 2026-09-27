# Guided Example: Bold Words in String

We trace the step-by-step multi-pattern dictionary Trie ingestion, sliding window prefix matching across text indices ($s[i \dots j]$), matching closed interval collection ($[i, j]$), overlapping and contiguous interval coalescence ($ed + 1 \ge a$), minimal HTML bold tag insertion (`<b>...</b>`), and final string reconstruction on representative character sequences:

- **Input:**
  - Dictionary: $words = [\text{"ab"}, \; \text{"bc"}]$
  - Text string: $s = \text{"aabcd"}$
- **Required output:**
  $$
  \text{"a<b>abc</b>d"}
  $$
  - Bold formatting criteria:
    - Any substring of $s$ that matches any word in $words$ must be enclosed in `<b>` and `</b>` tags.
    - **Tag Minimization (Merging Rule):**
      - If two bolded intervals overlap (e.g. $[1, 2]$ and $[2, 3]$) or are directly adjacent with zero intervening letters (e.g. $[1, 2]$ and $[3, 4]$), they **must be merged** into a single continuous pair `<b>...</b>`.
      - Redundant nested or abutting tags like `<b>ab</b><b>bc</b>` are strictly forbidden.
    - For $s = \text{"aabcd"}$:
      - Index 0: `"a"` $\to$ no match.
      - Index 1: `"ab"` matches $s[1 \dots 2]$.
      - Index 2: `"bc"` matches $s[2 \dots 3]$.
      - The two intervals $[1, 2]$ and $[2, 3]$ overlap at character index 2 (`'b'`).
      - Merged bold interval: $[1, 3]$ covering substring `"abc"`.
      - Preceding unbolded prefix: $s[0 \dots 0] = \text{"a"}$.
      - Trailing unbolded suffix: $s[4 \dots 4] = \text{"d"}$.
      - Reconstructed string: $\text{"a<b>abc</b>d"}$.
- **Trie Matching & Interval Coalescence Invariant:**
  - **Trie-Based Multi-Pattern Matching:**
    - Insert all dictionary words into a prefix tree (Trie).
    - For every starting position $i \in [0, n - 1]$:
      - Traverse the Trie following characters $s[i], s[i+1], \dots, s[j]$.
      - Whenever a node marked `is_end == true` is reached, record the closed interval $[i, j]$.
      - If a character has no outgoing Trie edge, stop advancing $j$.
  - **Interval Merging Invariant:**
    - Sort collected intervals by start index (naturally sorted by outer loop $i$).
    - Maintain active interval $[st, ed]$:
      - If the next interval $[a, b]$ satisfies:
        $$
        a \le ed + 1
        $$
        Then the intervals either overlap ($a \le ed$) or are contiguous ($a == ed + 1$).
        Coalesce them by extending the end boundary:
        $$
        ed \leftarrow \max(ed, \; b)
        $$
      - Otherwise ($a > ed + 1$):
        - Commit $[st, ed]$ to the merged list, and begin a new interval $[st, ed] \leftarrow [a, b]$.
- **Step-by-Step Worked Execution Trace on $s = \text{"aabcd"}$:**
  - Dictionary words: `"ab"`, `"bc"`. String length $n = 5$.
  - **Phase 0: Build Trie:**
    - Root $\to$ `'a'` $\to$ `'b'` (`is_end = true`).
    - Root $\to$ `'b'` $\to$ `'c'` (`is_end = true`).
  - **Phase 1: Scan Text Substrings:**
    - **Start $i = 0$ ($s[0] = \text{'a'}$):**
      - $s[0] = \text{'a'}$: node `'a'`.
      - $s[1] = \text{'a'}$: no child `'a'` under node `'a'`. Halt.
      - No matches.
    - **Start $i = 1$ ($s[1] = \text{'a'}$):**
      - $s[1] = \text{'a'}$: node `'a'`.
      - $s[2] = \text{'b'}$: node `'b'` (`is_end = true`).
        - Match found! Record interval:
          $$
          [i, j] = [\mathbf{1}, \; \mathbf{2}] \quad (\text{matches "ab"})
          $$
      - $s[3] = \text{'c'}$: no child `'c'` under node `'b'`. Halt.
    - **Start $i = 2$ ($s[2] = \text{'b'}$):**
      - $s[2] = \text{'b'}$: node `'b'`.
      - $s[3] = \text{'c'}$: node `'c'` (`is_end = true`).
        - Match found! Record interval:
          $$
          [i, j] = [\mathbf{2}, \; \mathbf{3}] \quad (\text{matches "bc"})
          $$
      - $s[4] = \text{'d'}$: no child `'d'`. Halt.
    - **Start $i = 3$ ($s[3] = \text{'c'}$):** No matching root edge `'c'`.
    - **Start $i = 4$ ($s[4] = \text{'d'}$):** No matching root edge `'d'`.
    - Raw interval list:
      $$
      pairs = [[1, 2], \; [2, 3]]
      $$
  - **Phase 2: Merge Intervals:**
    - Initialize: $st = 1, ed = 2$.
    - Inspect next pair $[a, b] = [2, 3]$:
      - Test condition: $a \le ed + 1 \iff 2 \le 2 + 1 \iff 2 \le 3 \implies \mathbf{Overlap\ Verified!}$
      - Merge:
        $$
        ed \leftarrow \max(2, 3) = \mathbf{3}
        $$
    - End of list: Append merged interval:
      $$
      t = [[\mathbf{1}, \; \mathbf{3}]]
      $$
  - **Phase 3: Assembly with HTML Tags:**
    - Current pointer $i = 0$. Merged interval $j = 0 \implies [st, ed] = [1, 3]$.
    - Slice before bold: $s[0 : 1] = \text{"a"}$.
    - Append opening tag: `"<b>"`.
    - Slice bold content: $s[1 : 4] = \text{"abc"}$.
    - Append closing tag: `"</b>"`.
    - Advance pointer: $i \leftarrow ed + 1 = 4$.
    - Remaining suffix: $s[4 : 5] = \text{"d"}$.
    - Assembled string:
      $$
      ans = \text{"a"} + \text{"<b>"} + \text{"abc"} + \text{"</b>"} + \text{"d"} = \mathbf{\text{"a<b>abc</b>d"}}
      $$
- **Adjacent Interval Coalescence Trace ($pairs = [[0, 1], [2, 3]]$):**
  - First interval $[0, 1]$, second $[2, 3]$.
  - $a = 2 \le ed + 1 = 1 + 1 = 2 \implies$ directly adjacent!
  - Merges into $[0, 3]$, producing single tag `<b>...</b>`.
- **No Matching Words ($s = \text{"xyz"}, words = [\text{"a"}]$):**
  - $pairs = [] \implies$ returns original string `"xyz"` unmodified.

This instance demonstrates multi-pattern string searching via Trie prefix automatons and 1D interval union reduction, mathematically proves why adjacency-closure coalescence yields the minimal tag factorization, and derives $O(\sum |W| + N \cdot L)$ runtime and $O(\sum |W| + N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s$ and a dictionary $words$:
Bold all occurrences of words in $s$ using `<b>` and `</b>`.
If two bold segments overlap or are adjacent, **merge them into a single `<b>...</b>`**.

```text
s = "aabcd", words = [ "ab", "bc" ]

Matches:
  "ab" at [1, 2]
  "bc" at [2, 3]

Intervals [1, 2] and [2, 3] overlap at index 2!
Merge into single interval [1, 3] covering "abc".

Result: "a<b>abc</b>d"
```

### The Invariant of the Adjacent Interval Merge
- An interval $[a, b]$ merges with $[st, ed]$ if $a \le ed + 1$ (overlaps or touches with no gap).
- Using a Trie to scan for matches at each index $i$ finds all occurrences in $O(N \cdot L)$ time.
- Emitting characters sequentially around merged intervals guarantees minimal tag placement.

---

## 2. Conceptual Foundation & Invariants

### 1. Trie Match Collection:
$$
\forall i \in [0, n - 1]: \quad \text{traverse Trie with } s[i \dots j] \implies \text{if } is\_end \implies pairs.\text{append}([i, j])
$$

### 2. Adjacency Merge Condition:
$$
\text{if } a \le ed + 1 \implies ed \leftarrow \max(ed, b) \quad \text{else commit } [st, ed], \; [st, ed] \leftarrow [a, b]
$$

> **Regular Language Union Invariant.** The bolding domain $\mathcal{B} \subset [0, n-1]$ is the union $\bigcup [a_k, b_k]$ of all matched subwords. Its topological components in the discrete metric $d(x, y) = |x - y|$ correspond to equivalence classes under the adjacency relation $|x - y| \le 1$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"aabcd"}, words = [\text{"ab"}, \text{"bc"}]$:

---

### Step 1: Find Matches
- At $i = 1$: `"ab"` matches $[1, 2]$.
- At $i = 2$: `"bc"` matches $[2, 3]$.

---

### Step 2: Merge
- $[1, 2]$ and $[2, 3]$ satisfy $2 \le 2 + 1 \implies$ merge into $[1, 3]$.

---

### Step 3: Insert Tags
- Prefix: `"a"` ($s[0:1]$).
- Tag: `<b>abc</b>` ($s[1:4]$).
- Suffix: `"d"` ($s[4:5]$).

---

### Step 4: Output
$$
\text{"a<b>abc</b>d"}
$$

---

## 4. Complete Execution Trace

| Step | Text Index $i$ | Action Taken | Substring Processed | Output Buffer Accumulator |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | $0$ | Unbolded character | `"a"` | `"a"` |
| $2$ | $1$ | Open bold tag | `<b>` | `"a<b>"` |
| $3$ | $1 \dots 3$ | Merged bold text | `"abc"` | `"a<b>abc"` |
| $4$ | $3$ | Close bold tag | `</b>` | `"a<b>abc</b>"` |
| $5$ | $4$ | Unbolded suffix | `"d"` | **`"a<b>abc</b>d"`** |

---

## 5. Boundary Cases & Failure Modes

- **No Matches:** Returns original string $s$ unmodified.
- **Entire String Bolded ($s = \text{"abc"}, words = [\text{"abc"}]$):** Wraps entire string: `<b>abc</b>`.
- **Adjacent Non-Overlapping ($[0, 1]$ and $[2, 3]$):** $a = 2 \le 1 + 1 \implies$ merges into `[0, 3]`.
- **Multiple Duplicate Matches:** Trie handles duplicate prefixes seamlessly.

---

## 6. Traps & Common Anti-Patterns

- **Not Merging Adjacent Intervals ($a == ed + 1$):** Producing `<b>ab</b><b>cd</b>` instead of `<b>abcd</b>` violates the minimum tag requirement. Merging must check $a \le ed + 1$, not just $a \le ed$.
- **Nested `<b>` Tags:** Directly replacing words with `<b>word</b>` strings causes illegal nested HTML tags (e.g. `a<b>a<b>b</b>c</b>d`). Extracting intervals and merging before formatting prevents tag duplication.
- **Quadratic String Concatenation:** Concatenating strings repeatedly inside loops incurs $O(N^2)$ overhead. Collect tokens in a list and `''.join(ans)`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Inserting dictionary into Trie: $\mathcal{O}(\sum |W|)$.
  - Scanning $s$ of length $N$ through Trie of max depth $L$: $\mathcal{O}(N \cdot L)$ where $L \le 30$.
  - Merging intervals and assembling output: $\mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(\sum |W| + N \cdot L)$. Completes in $< 5$ ms for $N = 500$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\sum |W| \cdot |\Sigma|)$ for the Trie, and $\mathcal{O}(N)$ for interval lists and output buffer.
