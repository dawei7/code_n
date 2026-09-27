# Guided Example: Concatenated Words

We trace the step-by-step length-ascending sort ordering, prefix Trie dictionary indexing, recursive prefix decomposition (`dfs(w[i+1:])`), building block admission, and multi-segment word validation on representative word dictionaries:

- **Input:** $words = [\text{"cat"}, \text{"cats"}, \text{"catsdogcats"}, \text{"dog"}, \text{"dogcatsdog"}, \text{"hippopotamuses"}, \text{"rat"}, \text{"ratcatdogcat"}]$
- **Required output:** `["catsdogcats", "dogcatsdog", "ratcatdogcat"]`
- **Execution trace:**
  - **Step 1: Sort by length ascending:**
    $$
    [\text{"cat"}, \text{"dog"}, \text{"rat"}, \text{"cats"}, \text{"dogcatsdog"}, \text{"catsdogcats"}, \text{"ratcatdogcat"}, \text{"hippopotamuses"}]
    $$
    *Insight:* A word can only be formed by concatenating strictly shorter words. Processing by length guarantees that all potential constituent words are already in the Trie before evaluating a candidate.
  - **Step 2: Incremental Trie insertion and DFS segmentation:**
    - Initialize empty Trie: $trie = \text{Root}()$, $ans = []$
    - **Word `"cat"` (len 3):**
      - Trie is empty $\implies dfs(\text{"cat"}) = \text{False}$
      - Insert `"cat"` into Trie.
    - **Word `"dog"` (len 3):**
      - Trie contains only `{"cat"}` $\implies dfs(\text{"dog"}) = \text{False}$
      - Insert `"dog"` into Trie.
    - **Word `"rat"` (len 3):**
      - $dfs(\text{"rat"}) = \text{False}$
      - Insert `"rat"` into Trie.
    - **Word `"cats"` (len 4):**
      - Prefix `"cat"` matches, but suffix `"s"` is not in Trie $\implies dfs(\text{"cats"}) = \text{False}$
      - Insert `"cats"` into Trie.
    - **Word `"dogcatsdog"` (len 10):**
      - Prefix 1: `"dog"` in Trie (len 3), recurse on suffix `"catsdog"`
      - Prefix 2: `"cats"` in Trie (len 4), recurse on suffix `"dog"`
      - Prefix 3: `"dog"` in Trie (len 3), recurse on suffix `""` (Base case: **True!**)
      - Valid concatenation of $\ge 2$ shorter words!
      - Add `"dogcatsdog"` to $ans$.
    - **Word `"catsdogcats"` (len 11):**
      - Prefix 1: `"cats"` in Trie (len 4), recurse on suffix `"dogcats"`
      - Prefix 2: `"dog"` in Trie (len 3), recurse on suffix `"cats"`
      - Prefix 3: `"cats"` in Trie (len 4), recurse on suffix `""` (**True!**)
      - Add `"catsdogcats"` to $ans$.
    - **Word `"ratcatdogcat"` (len 12):**
      - Decomposes into `"rat"` + `"cat"` + `"dog"` + `"cat"` (**True!**)
      - Add `"ratcatdogcat"` to $ans$.
    - **Word `"hippopotamuses"` (len 14):**
      - Prefix `"hi"` not in Trie $\implies$ Fails immediately.
      - Insert into Trie.
  - Final concatenated words: `["catsdogcats", "dogcatsdog", "ratcatdogcat"]`.
- **Single Concatenation Instance:** $words = [\text{"cat"}, \text{"dog"}, \text{"catdog"}] \implies \mathbf{[\text{"catdog"}]}$
- **No Concatenated Words:** $words = [\text{"a"}, \text{"b"}, \text{"c"}] \implies \mathbf{[]}$

This instance demonstrates dynamic dictionary expansion via length sorting, mathematically proves why atomic building blocks suffice for recursive subproblem matching, and derives $O(N \log N + N \cdot L^2)$ runtime and $O(N \cdot L)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of strings $words$ (without duplicates):
A **concatenated word** is defined as a string that is comprised entirely of at least two shorter words in the given array.
Return all concatenated words in $words$.

```text
Vocabulary:
  Atomic Words:       "cat", "dog", "rat", "cats"
  Complex Words:      "catsdogcats" -> "cats" + "dog" + "cats"
                      "dogcatsdog"  -> "dog"  + "cats" + "dog"
                      "ratcatdogcat"-> "rat"  + "cat"  + "dog" + "cat"

Concatenated Words Found: ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
```

### The Length-Ordered Induction Principle
- A word $W$ can only be decomposed into words $w_1, w_2, \dots$ if each $w_i$ is **strictly shorter** than $W$ ($|w_i| < |W|$).
- If we sort all words by length in ascending order:
  - When evaluating candidate word $W$, every possible sub-word that could compose $W$ has already been encountered and processed!
  - We simply check whether $W$ can be formed by words currently in the Trie.
  - If $W$ can be formed: it is a concatenated word! We append it to the answer.
  - If $W$ cannot be formed: it is an atomic building block; we insert it into the Trie so future longer words can use it!

---

## 2. Conceptual Foundation & Invariants

### 1. The Prefix Trie Structure:
- Each node contains 26 child pointers and a boolean flag `is_end`.
- `insert(w)` traverses characters and marks the terminal node with `is_end = True`.

### 2. Recursive Decomposition DFS:
For candidate word $w$:
- Base case: If $w == \text{""}$, all characters were matched $\implies$ Return `True`.
- Walk the Trie starting from the root:
  - For each prefix character $c = w[i]$:
    - If Trie has no child for $c$, this path terminates $\implies$ Return `False`.
    - Advance Trie pointer.
    - If `node.is_end == True`:
      The prefix $w[0 \dots i]$ forms a valid dictionary word!
      Recursively test the remaining suffix:
      $$
      \text{If } dfs(w[i + 1 \dots |w| - 1]) == \text{True} \implies \text{Return True}
      $$
- If all prefix splits fail, return `False`.

> **Order Invariant.** Because words are sorted ascending by length, the Trie contains only words with length strictly less than $|W|$ (or equal length words that failed decomposition), preventing a word from trivially matching itself as a single piece.

---

## 3. Step-by-Step Worked Execution

We trace $words = [\text{"cat"}, \text{"cats"}, \text{"catsdogcats"}, \text{"dog"}, \text{"dogcatsdog"}]$:

---

### Step 1: Sort by Word Length
$$
[\text{"cat"} (3), \; \text{"dog"} (3), \; \text{"cats"} (4), \; \text{"dogcatsdog"} (10), \; \text{"catsdogcats"} (11)]
$$

---

### Step 2: Process Small Base Words
1. **Word `"cat"`:**
   - Trie is empty $\implies dfs(\text{"cat"}) = \text{False}$.
   - Action: `trie.insert("cat")`. Trie: `{"cat"}`.
2. **Word `"dog"`:**
   - Scan `"dog"` in Trie: root has no child `'d'`. $dfs(\text{"dog"}) = \text{False}$.
   - Action: `trie.insert("dog")`. Trie: `{"cat", "dog"}`.
3. **Word `"cats"`:**
   - Scan `"cats"` in Trie:
     - Prefix `"cat"` matches `is_end = True`.
     - Recurse on remaining suffix `"s"`.
     - Root has no child `'s'` $\implies dfs(\text{"s"}) = \text{False}$.
   - $dfs(\text{"cats"}) = \text{False}$.
   - Action: `trie.insert("cats")`. Trie: `{"cat", "dog", "cats"}`.

---

### Step 3: Process `"dogcatsdog"` ($|w| = 10$)
Call $dfs(\text{"dogcatsdog"})$:
- Prefix `"dog"` is matched at index 2 (`is_end = True`).
- Recurse on suffix $dfs(\text{"catsdog"})$:
  - Prefix `"cat"` is matched at index 2 (`is_end = True`):
    - Recurse on suffix $dfs(\text{"sdog"})$: fails.
  - Prefix `"cats"` is matched at index 3 (`is_end = True`):
    - Recurse on suffix $dfs(\text{"dog"})$:
      - Prefix `"dog"` matched at index 2 (`is_end = True`).
      - Recurse on suffix $dfs(\text{""})$: Base case reached $\implies$ **`True`**!
- $dfs(\text{"dogcatsdog"})$ returns `True`.
- Add `"dogcatsdog"` to output list.

---

### Step 4: Process `"catsdogcats"` ($|w| = 11$)
Call $dfs(\text{"catsdogcats"})$:
- Match `"cats"` $\implies$ recurse on `"dogcats"`.
- Match `"dog"` $\implies$ recurse on `"cats"`.
- Match `"cats"` $\implies$ recurse on `""` (**`True`**).
- Add `"catsdogcats"` to output list.

---

## 4. Complete Execution Trace

| Word $w$ | Length | Trie State Before | Suffix Decompositions Tested | Result of $dfs(w)$ | Action Taken |
|:---:|:---:|:---|:---|:---:|:---|
| `"cat"` | $3$ | `{}` | No prefixes | False | Insert `"cat"` |
| `"dog"` | $3$ | `{"cat"}` | No `'d'` | False | Insert `"dog"` |
| `"cats"`| $4$ | `{"cat", "dog"}` | `"cat"` + `"s"` (fails) | False | Insert `"cats"` |
| `"dogcatsdog"` | $10$ | `{"cat", "dog", "cats"}` | `"dog"` + `"cats"` + `"dog"` | **True** | **Append to Answer** |
| `"catsdogcats"`| $11$ | `{"cat", "dog", "cats"}` | `"cats"` + `"dog"` + `"cats"` | **True** | **Append to Answer** |

---

## 5. Boundary Cases & Failure Modes

- **Single Word Dictionary ($words = [\text{"cat"}]):$** Cannot be formed by $\ge 2$ words $\implies \mathbf{[]}$.
- **Duplicate Prefixes ($[\text{"a"}, \text{"aa"}, \text{"aaa"}, \text{"aaaa"}]$):**
  - `"a"` inserted.
  - `"aa"` decomposes into `"a" + "a"` $\implies$ added to answer.
  - `"aaa"` decomposes into `"a" + "aa"` $\implies$ added to answer.
- **Empty Strings in Input:** Handled by ignoring or length check so empty strings do not trigger infinite loops.

---

## 6. Traps & Common Anti-Patterns

- **Inserting All Words Into Trie First:** If all words are inserted before searching, a word will match itself in a single step ($w = w$) unless complex piece-counting logic is added. Sorting by length and inserting on-the-fly guarantees that only strictly shorter words exist in the Trie during evaluation.
- **Inserting Concatenated Words into Trie:** While harmless for correctness, inserting concatenated words like `"dogcatsdog"` adds redundant branches. Since any word built with `"dogcatsdog"` can also be built with `"dog"` and `"cats"`, omitting concatenated words keeps the Trie compact.
- **Unmemoized Worst-Case Suffixes:** Suffixes like `"aaaaaab"` with dictionary `{"a", "aa", ...}` can cause exponential branching. Memoizing visited failed suffixes prevents repeated tree searches.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $N$ words takes $O(N \log N \cdot L)$ time, where $L \le 30$ is maximum word length.
  - For each word, Trie descent and suffix branching takes $O(L^2)$ time with memoization.
  - Total Time: $\mathcal{O}(N \log N \cdot L + N \cdot L^2)$. For $N = 10^4$ and $L = 30$, executes in $< 120$ ms.
- **Auxiliary Space Complexity:**
  - Trie memory stores at most $\sum |w_i| = O(N \cdot L)$ character nodes.
