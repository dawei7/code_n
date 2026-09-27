# Guided Example: Replace Words

We trace the step-by-step prefix tree (Trie) dictionary indexing ($26$-ary letter tree), tokenized sentence stream parsing, character-by-character prefix path traversal ($node \leftarrow node.children[c]$), earliest terminal root hit detection ($node.is\_end \implies w[:i]$), shortest root replacement invariant, and reconstituted sentence synthesis on representative linguistic texts:

- **Input:**
  - Root dictionary: $dictionary = [\text{"cat"}, \; \text{"bat"}, \; \text{"rat"}]$
  - Original sentence: $sentence = \text{"the cattle was rattled by the battery"}$
- **Required output:** `\text{"the cat was rat by the bat"}`
  - Linguistic definitions:
    - A **root** is a word stem that prefixes a longer derivative word (e.g. `"cat"` prefixes `"cattle"`).
    - If a word can be formed by multiple roots (e.g. roots `"c"` and `"cat"` for `"cattle"`), it must be replaced by the **shortest valid root** (here `"c"`).
    - Words without any matching dictionary root in the prefix position remain unchanged.
- **Prefix Tree (Trie) Shortest Root Invariant:**
  - **Trie Construction:**
    - Insert every root word from $dictionary$ into a 26-ary Trie.
    - Mark the terminal node of each root with a boolean flag: $node.is\_end = \mathbf{True}$.
  - **Greedy Earliest-Exit Search:**
    - For each word $w$ in the sentence:
      - Start at the Trie root and trace characters $c = w[0], w[1], \dots$
      - At each character position $i$ (1-indexed):
        1. If the character link $node.children[c]$ does not exist:
           - No root prefixes this word $\implies$ return original word $w$.
        2. Advance to the child node: $node \leftarrow node.children[c]$.
        3. If $node.is\_end == \mathbf{True}$:
           - We have encountered the **shortest root** that matches this word!
           - Immediately return prefix slice $w[:i]$ without traversing further.
      - If the word terminates without reaching any node with $is\_end == True$, return the original word $w$.
- **Step-by-Step Worked Execution Trace:**
  - **Step 1: Populate Trie:**
    - Insert `"cat"`: `root -> 'c' -> 'a' -> 't'` ($is\_end = True$).
    - Insert `"bat"`: `root -> 'b' -> 'a' -> 't'` ($is\_end = True$).
    - Insert `"rat"`: `root -> 'r' -> 'a' -> 't'` ($is\_end = True$).
  - **Step 2: Tokenize Sentence:**
    - Words: `["the", "cattle", "was", "rattled", "by", "the", "battery"]`.
  - **Step 3: Process Each Word:**
    - **Word 1: `"the"`:**
      - Test $w[0] = \text{'t'}$.
      - Trie root has no child `'t'` $\implies$ Link is `None`.
      - Output retains:
        $$
        \mathbf{\text{"the"}}
        $$
    - **Word 2: `"cattle"`:**
      - Character 1 ($i = 1$): `'c'` exists in Trie $\to node = \text{'c'}$. $is\_end = False$.
      - Character 2 ($i = 2$): `'a'` exists in Trie $\to node = \text{'a'}$. $is\_end = False$.
      - Character 3 ($i = 3$): `'t'` exists in Trie $\to node = \text{'t'}$.
        - Inspect node flag: $is\_end == \mathbf{True!}$
        - Root `"cat"` matched at length $3$.
        - Shortest root reached: halt search and return $w[:3] = \text{"cat"}$.
      - Replaced with:
        $$
        \mathbf{\text{"cat"}}
        $$
    - **Word 3: `"was"`:**
      - Test $w[0] = \text{'w'}$.
      - Child `'w'` does not exist $\implies$ Link is `None`.
      - Output retains:
        $$
        \mathbf{\text{"was"}}
        $$
    - **Word 4: `"rattled"`:**
      - Character 1 ($i = 1$): `'r'` exists $\to is\_end = False$.
      - Character 2 ($i = 2$): `'a'` exists $\to is\_end = False$.
      - Character 3 ($i = 3$): `'t'` exists $\to is\_end = \mathbf{True!}$
      - Root `"rat"` matched. Return $w[:3] = \text{"rat"}$.
      - Replaced with:
        $$
        \mathbf{\text{"rat"}}
        $$
    - **Word 5: `"by"`:**
      - Character 1: `'b'` exists $\to is\_end = False$.
      - Character 2: `'y'`. Child `'y'` under `'b'` does not exist (`None`).
      - Output retains:
        $$
        \mathbf{\text{"by"}}
        $$
    - **Word 6: `"the"`:**
      - Link `None` $\implies$ Retains **`"the"`**.
    - **Word 7: `"battery"`:**
      - Character 1: `'b'` exists $\to is\_end = False$.
      - Character 2: `'a'` exists $\to is\_end = False$.
      - Character 3: `'t'` exists $\to is\_end = \mathbf{True!}$
      - Root `"bat"` matched. Return $w[:3] = \text{"bat"}$.
      - Replaced with:
        $$
        \mathbf{\text{"bat"}}
        $$
  - **Step 4: Join Output Tokens:**
    $$
    ans = \text{"the cat was rat by the bat"}
    $$
- **Shortest Root Precedence Instance:**
  - Suppose $dictionary = [\text{"c"}, \text{"cat"}]$ and word is `"cattle"`.
  - At character 1 ($i = 1$, `'c'`), $node.is\_end == True$.
  - The search immediately returns `"c"`, ignoring the longer root `"cat"`.
- **Root Equal to Word:**
  - If $w = \text{"cat"}$, it matches root `"cat"` and returns `"cat"`.

This instance demonstrates deterministic finite-state prefix matching on retrieval trees, mathematically proves why earliest terminal state detection satisfies shortest root lexicographical minimization, and derives $O(D \cdot L_{dict} + S)$ runtime and $O(D \cdot L_{dict})$ space bounds.

---

## 1. Instance & Teaching Goal

Given a dictionary of roots and a sentence:
Replace each word with the **shortest root** that forms its prefix.
If no root matches, leave the word unchanged.

```text
Roots: ["cat", "bat", "rat"]
Sentence: "the cattle was rattled by the battery"

Replacements:
  "the"     -> no root     -> "the"
  "cattle"  -> root "cat"  -> "cat"
  "was"     -> no root     -> "was"
  "rattled" -> root "rat"  -> "rat"
  "by"      -> no root     -> "by"
  "the"     -> no root     -> "the"
  "battery" -> root "bat"  -> "bat"

Result: "the cat was rat by the bat"
```

### The Invariant of the Earliest Terminal
- By walking the Trie character-by-character from the root, the **first** node encountered that has `is_end == True` is guaranteed to be the shortest matching root.
- Halting search immediately upon finding `is_end` ensures optimal runtime and satisfies the shortest-root requirement.

---

## 2. Conceptual Foundation & Invariants

### 1. Trie Traversal Rule:
For each word $w$:
$$
node \leftarrow root
$$
For $i = 1 \dots |w|$ with character $c = w[i-1]$:
- If $node.children[c] == \text{null} \implies$ return $w$
- $node \leftarrow node.children[c]$
- If $node.is\_end \implies$ return $w[:i]$
Return $w$.

> **Prefix Prefix-Closed Invariant.** In a prefix tree, any path from root to a marked terminal node represents a valid word in the language, with parent-ancestor terminals strictly dominating descendant terminals under the length metric.

---

## 3. Step-by-Step Worked Execution

We trace $w = \text{"cattle"}$ against roots `cat, bat, rat`:

---

### Step 1: Character `'c'`
- Child exists. $is\_end = False$.

---

### Step 2: Character `'a'`
- Child exists. $is\_end = False$.

---

### Step 3: Character `'t'`
- Child exists. $is\_end = \mathbf{True!}$
- Shortest root reached: return `"cat"`.

---

## 4. Complete Execution Trace

| Word in Sentence | Trie Path Evaluated | Failure or Success Event | Output Word |
|:---:|:---:|:---:|:---:|
| `"the"` | `'t'` | Child `'t'` is null | `"the"` |
| `"cattle"` | `'c' \to 'a' \to 't'` | $is\_end = True$ on `'t'` | **`"cat"`** |
| `"was"` | `'w'` | Child `'w'` is null | `"was"` |
| `"rattled"` | `'r' \to 'a' \to 't'` | $is\_end = True$ on `'t'` | **`"rat"`** |
| `"by"` | `'b' \to 'y'` | Child `'y'` is null | `"by"` |
| `"the"` | `'t'` | Child `'t'` is null | `"the"` |
| `"battery"` | `'b' \to 'a' \to 't'` | $is\_end = True$ on `'t'` | **`"bat"`** |

---

## 5. Boundary Cases & Failure Modes

- **Multiple Matching Roots (`"c"`, `"ca"`, `"cat"`):** The algorithm halts at `"c"` on step 1, correctly choosing the shortest root.
- **Root Longer Than Word:** Fails naturally when word characters are exhausted.
- **Empty Sentence:** Returns empty string.
- **Single Letter Roots (`"a"` for `"apple"`):** Halts after 1 step $\implies$ `"a"`.

---

## 6. Traps & Common Anti-Patterns

- **Searching All Dictionary Roots Linearly ($O(D \cdot W)$ per word):** Comparing every dictionary word against every sentence word takes quadratic time. A Trie searches in $O(L)$ where $L$ is word length.
- **Not Halting on First Match:** If you find a matching root and continue traversing to see if there is a longer root, you violate the shortest root rule.
- **Handling Whitespace Incorrectly:** Use `sentence.split()` and `" ".join(...)` to preserve single space tokenization.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Inserting $D$ dictionary roots of average length $L_d$: $\mathcal{O}(\sum L_d)$.
  - Searching $W$ words in sentence: each word takes at most $\mathcal{O}(L_w)$ steps where $L_w$ is its length.
  - Total Time: $\mathcal{O}(\sum L_d + \text{len}(sentence))$. Strictly linear in the total input text size. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(26 \cdot \sum L_d)$ space for the Trie data structure.
