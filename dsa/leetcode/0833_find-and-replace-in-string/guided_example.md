# Guided Example: Find And Replace in String

We trace the step-by-step simultaneous string replacement simulation, prefix matching validation ($s.\text{startswith}(source, i)$), displacement collision avoidance via index tagging ($d[i] = k$), linear reconstruction cursor traversal, substring skipping ($i \mathrel{+}= |source|$), and transformed string assembly on representative edit operations:

- **Input:**
  $$
  s = \text{"abcd"}
  $$
  $$
  indices = [0, 2], \quad sources = [\text{"a"}, \text{"cd"}], \quad targets = [\text{"eee"}, \text{"ffff"}]
  $$
- **Required output:**
  $$
  \text{"eeebffff"}
  $$
  - Simultaneous replacement rules:
    - We are given original string $s$ and $K$ replacement operations.
    - The $k$-th operation specifies that at index $indices[k]$, we check if $s$ begins with substring $sources[k]$.
    - **Match:** If $s[indices[k] \dots]$ begins with $sources[k]$, that entire segment is replaced by $targets[k]$.
    - **Mismatch:** If the substring does not match, the operation is skipped with no effect.
    - **Simultaneity Guarantee:** All operations occur simultaneously based on the **original** string's character indices. Replacing text earlier in the string does NOT shift the target indices of subsequent operations!
    - For $s = \text{"abcd"}$:
      - Operation 0 at index 0: check if $s[0:]$ starts with `"a"`.
        - Matches! `"a"` $\to$ `"eee"`.
      - Index 1: no operation $\implies$ character `'b'` remains unchanged.
      - Operation 1 at index 2: check if $s[2:]$ starts with `"cd"`.
        - Matches! `"cd"` $\to$ `"ffff"`.
      - Assembled output: `"eee" + "b" + "ffff" = ` **`"eeebffff"`**.
- **Position-Indexed Dispatch & Linear Reconstruction Invariant:**
  - **The Shift Problem in Naive Replacement:**
    - If replacements are applied sequentially from left to right, inserting a longer or shorter target string mutates character indices, invalidating remaining operation indices!
  - **Index Tagging Array ($d$):**
    - Pre-validate all operations against the static original string $s$.
    - Create an array $d$ of length $n = |s|$, initialized with $-1$:
      - For each operation $k$ with index $i = indices[k]$ and string $src = sources[k]$:
        - If $s$ starts with $src$ at index $i$:
          $$
          d[i] \leftarrow k
          $$
  - **Reconstruction Cursor ($i = 0 \dots n - 1$):**
    - Walk cursor $i$ forward from $0$ to $n - 1$:
      - If $d[i] \ne -1$:
        - Operation $k = d[i]$ triggered.
        - Append $targets[k]$ to the output.
        - Jump cursor forward over the consumed original characters:
          $$
          i \leftarrow i + |sources[k]|
          $$
      - If $d[i] == -1$:
        - No replacement at this index.
        - Append original character $s[i]$.
        - Advance cursor by 1:
          $$
          i \leftarrow i + 1
          $$
- **Step-by-Step Worked Execution Trace on $s = \text{"abcd"}$:**
  - Original string length $n = 4$.
  - Initialize dispatch table:
    $$
    d = [-1, \; -1, \; -1, \; -1]
    $$
  - **Phase 0: Pre-validate Operations Against Original $s$:**
    - **Operation $k = 0$ ($idx = 0, src = \text{"a"}, tgt = \text{"eee"}$):**
      - Substring at index 0: $s[0:1] = \text{"a"}$.
      - Matches $src = \text{"a"} \implies \mathbf{Valid\ Match!}$
      - Tag table: $d[0] \leftarrow 0$.
    - **Operation $k = 1$ ($idx = 2, src = \text{"cd"}, tgt = \text{"ffff"}$):**
      - Substring at index 2: $s[2:4] = \text{"cd"}$.
      - Matches $src = \text{"cd"} \implies \mathbf{Valid\ Match!}$
      - Tag table: $d[2] \leftarrow 1$.
    - Final dispatch vector:
      $$
      d = [0, \; -1, \; 1, \; -1]
      $$
  - **Phase 1: Linear Reconstruction Cursor:**
    - Initialize: $i = 0, ans = []$.
    - **Cursor at $i = 0$:**
      - Inspect $d[0] = 0 \ne -1 \implies \mathbf{Replacement\ Triggered!}$
      - Append target: $ans.\text{append}(\text{"eee"})$.
      - Skip length of source:
        $$
        i \leftarrow 0 + |\text{"a"}| = 0 + 1 = \mathbf{1}
        $$
    - **Cursor at $i = 1$:**
      - Inspect $d[1] = -1 \implies \mathbf{Unchanged\ Character.}$
      - Append original: $ans.\text{append}(s[1]) = ans.\text{append}(\text{"b"})$.
      - Advance cursor:
        $$
        i \leftarrow 1 + 1 = \mathbf{2}
        $$
    - **Cursor at $i = 2$:**
      - Inspect $d[2] = 1 \ne -1 \implies \mathbf{Replacement\ Triggered!}$
      - Append target: $ans.\text{append}(\text{"ffff"})$.
      - Skip length of source:
        $$
        i \leftarrow 2 + |\text{"cd"}| = 2 + 2 = \mathbf{4}
        $$
    - **Cursor at $i = 4 == n$:**
      - End of original string reached!
  - **Phase 2: Join Output Strings:**
    $$
    ans = \text{"eee"} + \text{"b"} + \text{"ffff"} = \mathbf{\text{"eeebffff"}}
    $$
- **Mismatch Disqualification Trace ($s = \text{"abcd"}, sources[1] = \text{"ec"}$ at index 2):**
  - Substring at index 2 is `"cd"`.
  - Compare with $sources[1] = \text{"ec"}$: $s[2:4] \ne \text{"ec"} \implies \mathbf{Mismatch!}$
  - Dispatch tag remains $d[2] = -1$.
  - Cursor prints original characters `'c'` and `'d'` unchanged $\implies \text{"eeecd"}$.
- **Unsorted Operations Array Trace:**
  - $indices$ can appear in arbitrary order (e.g. $[2, 0]$ instead of $[0, 2]$).
  - The dispatch table $d[i]$ automatically orders operations by their position in $s$, eliminating any need to sort operations.

This instance demonstrates string rewriting systems under synchronous parallel term substitution, mathematically proves why anchoring replacement offsets to the pre-state coordinate system preserves confluence without inter-rule interference, and derives $O(N + \sum |src_k| + \sum |tgt_k|)$ runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given string $s$ and replacement operations $(index, source, target)$:
Replace $source$ with $target$ at $index$ if and only if $s$ actually matches $source$ at that index.
All replacements happen **simultaneously** on the original string.

```text
s = "abcd"
Op 0: index 0, source "a",  target "eee"  -> matches!
Op 1: index 2, source "cd", target "ffff" -> matches!

Reconstruction:
  Index 0: replace "a"  -> "eee", cursor jumps to 1
  Index 1: keep "b"     -> "b",   cursor advances to 2
  Index 2: replace "cd" -> "ffff", cursor jumps to 4 (end)

Result: "eeebffff"
```

### The Invariant of Simultaneous Rewriting
- Operations are evaluated against the **original string**, not against intermediate strings.
- Tag matching operations at their starting index $i$ in a dispatch array $d$.
- Walk a cursor $i$ from $0$ to $n - 1$:
  - If an operation is tagged at $i$, append $target$ and jump $i \mathrel{+}= |source|$.
  - Otherwise, append $s[i]$ and advance $i \mathrel{+}= 1$.

---

## 2. Conceptual Foundation & Invariants

### 1. Pre-State Compatibility Dispatch:
$$
d[i] = \begin{cases}
k & \exists k: indices[k] = i \;\land\; s[i \dots i + |sources[k]| - 1] = sources[k] \\
-1 & \text{otherwise}
\end{cases}
$$

### 2. Cursor Transduction Step:
$$
(ans, i) \leftarrow \begin{cases}
(ans \cup \{ targets[d[i]] \}, \; i + |sources[d[i]]|) & d[i] \ge 0 \\
(ans \cup \{ s[i] \}, \; i + 1) & d[i] == -1
\end{cases}
$$

> **Parallel Term Rewriting Invariant.** Let $R = \{(i_k, u_k \to v_k)\}$ be a set of non-overlapping rules on string $s$. The simultaneous rewrite relation is confluent and deterministically evaluated by a single-pass sequential transducer driven by the support indicator $d: [0, n - 1] \to R \cup \{\bot\}$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"abcd"}, indices = [0, 2], sources = [\text{"a"}, \text{"cd"}], targets = [\text{"eee"}, \text{"ffff"}]$:

---

### Step 1: Pre-Validate
- $d[0] = 0$ ($s[0:]$ starts with `"a"`).
- $d[2] = 1$ ($s[2:]$ starts with `"cd"`).
- $d = [0, -1, 1, -1]$.

---

### Step 2: Cursor at 0
- $d[0] = 0 \implies$ append `"eee"`, jump $i \leftarrow 0 + 1 = 1$.

---

### Step 3: Cursor at 1
- $d[1] = -1 \implies$ append `"b"`, advance $i \leftarrow 1 + 1 = 2$.

---

### Step 4: Cursor at 2
- $d[2] = 1 \implies$ append `"ffff"`, jump $i \leftarrow 2 + 2 = 4$.

---

### Step 5: Output
$$
\mathbf{\text{"eeebffff"}}
$$

---

## 4. Complete Execution Trace

| Cursor Index $i$ | Dispatch Tag $d[i]$ | Matched Source | Target Appended | Cursor Increment | Next Cursor Position |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $0$ | `"a"` | `"eee"` | $+1$ ($\lvert \text{"a"} \rvert$) | $1$ |
| $1$ | $-1$ | None | `"b"` (Original) | $+1$ | $2$ |
| **$2$** | **$1$** | **`"cd"`** | **`"ffff"`** | **$+2$ ($\lvert \text{"cd"} \rvert$)** | **`4` (End)** |
| **Final** | — | — | — | — | **`"eeebffff"`** |

---

## 5. Boundary Cases & Failure Modes

- **Source Mismatch:** If $s[indices[k]:]$ does not start with $sources[k]$, $d[i]$ remains $-1$; original characters are preserved untouched.
- **Unsorted Indices:** Indices can be given out of order (e.g. $[2, 0]$); dispatch table indexing inherently sorts operations by their appearance in $s$.
- **No Replacements Match:** Returns original string $s$ unmodified.
- **Replacement at End of String:** Handled without out-of-bounds error.

---

## 6. Traps & Common Anti-Patterns

- **Applying Replacements in Place Sequentially:** Modifying $s$ directly shifts all subsequent indices, causing downstream operations to target incorrect positions. Pre-validating against the static original string eliminates index drift.
- **Sorting and Tracking Offset Deltas:** Sorting indices and maintaining an `offset` variable is error-prone. The dispatch table $d$ completely avoids offset math.
- **Checking `in` Instead of `startswith`:** The condition requires $sources[k]$ to occur **exactly starting at** $indices[k]$, not anywhere in the suffix. Use `s.startswith(src, i)`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Validating $K$ operations against $s$: $\sum |sources[k]|$.
  - Single pass through string of length $N$: $\mathcal{O}(N)$.
  - Constructing output string: $\mathcal{O}(N + \sum |targets[k]|)$.
  - Total Time: strictly linear $\mathcal{O}(N + \sum |src_k| + \sum |tgt_k|)$ where $N \le 1000, K \le 100$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory for the dispatch array $d$ and output buffer.
