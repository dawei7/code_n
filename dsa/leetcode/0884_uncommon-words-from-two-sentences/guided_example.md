# Guided Example: Uncommon Words from Two Sentences

We trace the step-by-step whitespace tokenization, joint multiset union pooling, global occurrence counting, frequency unit filter ($\text{count} == 1$), and uncommon word extraction on representative sentence pairs:

- **Input:**
  $$
  s_1 = \text{"this apple is sweet"}, \quad s_2 = \text{"this apple is sour"}
  $$
- **Required output:** `["sweet", "sour"]`
  - Uncommon word definition:
    - A sentence is a string of single-space-separated words.
    - A word is **uncommon** if it appears **exactly once in one of the sentences**, and **does not appear in the other sentence**.
    - For $s_1 = \text{"this apple is sweet"}$ and $s_2 = \text{"this apple is sour"}$:
      - Words in $s_1$: `["this", "apple", "is", "sweet"]`.
      - Words in $s_2$: `["this", "apple", "is", "sour"]`.
      - `"this"` appears in both $s_1$ and $s_2$ (Common $\implies$ Excluded).
      - `"apple"` appears in both $s_1$ and $s_2$ (Common $\implies$ Excluded).
      - `"is"` appears in both $s_1$ and $s_2$ (Common $\implies$ Excluded).
      - `"sweet"` appears once in $s_1$ and $0$ times in $s_2$ (**Uncommon**).
      - `"sour"` appears once in $s_2$ and $0$ times in $s_1$ (**Uncommon**).
      - Result: **`["sweet", "sour"]`** (in any order).
- **The Joint Multiset Frequency Equivalence Invariant:**
  - **The Two Disjoint Conditions:**
    - Word appears exactly once in $s_1$ AND zero times in $s_2$.
    - OR word appears exactly once in $s_2$ AND zero times in $s_1$.
  - **The Combined Count Theorem:**
    - Consider the total frequency of a word $w$ across both sentences combined:
      $$
      \text{total\_count}(w) = \text{count}_{s_1}(w) + \text{count}_{s_2}(w)
      $$
    - If $\text{total\_count}(w) == 1$:
      - Since counts are non-negative integers, the only partition of $1$ is $1 + 0$ or $0 + 1$.
      - Thus, $w$ appears once in one sentence and zero times in the other!
    - If $\text{total\_count}(w) \ge 2$:
      - Either $w$ appears in both sentences ($1+1, 2+1, \dots$), so it is not exclusive to one sentence.
      - Or $w$ appears $\ge 2$ times within the same sentence ($2+0, 3+0, \dots$), so it does not appear "exactly once" in that sentence.
    - **Conclusion:** A word is uncommon if and only if its **total global frequency in the concatenation $s_1 + \text{" "} + s_2$ is strictly equal to $1$**!

---

## 1. Instance & Teaching Goal

Given sentences $s_1$ and $s_2$, extract words occurring with net multiplicity $1$.

```text
Sentence 1: "this apple is sweet"
Sentence 2: "this apple is sour"

Token Stream:
  ["this", "apple", "is", "sweet", "this", "apple", "is", "sour"]

Frequency Map:
  "this"  -> 2 (Duplicate)
  "apple" -> 2 (Duplicate)
  "is"    -> 2 (Duplicate)
  "sweet" -> 1 (Unique -> KEEP)
  "sour"  -> 1 (Unique -> KEEP)

Uncommon Words: ["sweet", "sour"]
```

We also contrast this with $s_1 = \text{"apple apple"}, s_2 = \text{"banana"}$: `"apple"` appears twice in $s_1$ (total 2), disqualifying it, leaving only `["banana"]`.

---

## 2. Conceptual Foundation & Invariants

### 1. Token Multiset:
Let $W = \text{tokens}(s_1) \cup \text{tokens}(s_2)$.
$$
\text{freq}(w) = \sum_{t \in W} \mathbb{I}[t == w]
$$

### 2. Selection Predicate:
$$
\text{Uncommon} = \{w \in W \mid \text{freq}(w) == 1\}
$$

---

## 3. Step-by-Step Worked Execution

We trace $s_1 = \text{"this apple is sweet"}$ and $s_2 = \text{"this apple is sour"}$:

---

### Step 1: Tokenization
- Split $s_1$ by spaces:
  $$
  W_1 = [\text{"this"}, \text{"apple"}, \text{"is"}, \text{"sweet"}]
  $$
- Split $s_2$ by spaces:
  $$
  W_2 = [\text{"this"}, \text{"apple"}, \text{"is"}, \text{"sour"}]
  $$

---

### Step 2: Build Frequency Hash Table
- Insert tokens from $W_1$:
  - `"this"`: $count \leftarrow 1$
  - `"apple"`: $count \leftarrow 1$
  - `"is"`: $count \leftarrow 1$
  - `"sweet"`: $count \leftarrow 1$
- Insert tokens from $W_2$:
  - `"this"`: $count \leftarrow 1 + 1 = 2$
  - `"apple"`: $count \leftarrow 1 + 1 = 2$
  - `"is"`: $count \leftarrow 1 + 1 = 2$
  - `"sour"`: $count \leftarrow 1$

Final Frequency Map:
$$
\{\text{"this"}: 2, \; \text{"apple"}: 2, \; \text{"is"}: 2, \; \text{"sweet"}: 1, \; \text{"sour"}: 1\}
$$

---

### Step 3: Filter for Frequency Equal to 1
- `"this"`: count $2 \ne 1$ (Discard).
- `"apple"`: count $2 \ne 1$ (Discard).
- `"is"`: count $2 \ne 1$ (Discard).
- `"sweet"`: count $1 == 1$ (**Keep!**).
- `"sour"`: count $1 == 1$ (**Keep!**).

Output List: `["sweet", "sour"]`.

---

## 4. Complete Execution Trace

| Word Token | Sentence 1 Count | Sentence 2 Count | Total Combined Count | Count $== 1$? | Reason / Classification | Output Membership |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `"this"` | $1$ | $1$ | $2$ | No | Present in both sentences | Excluded |
| `"apple"` | $1$ | $1$ | $2$ | No | Present in both sentences | Excluded |
| `"is"` | $1$ | $1$ | $2$ | No | Present in both sentences | Excluded |
| **`"sweet"`** | $1$ | $0$ | **$1$** | **Yes** | **Exclusive to $s_1$, single occurrence** | **Included** |
| **`"sour"`** | $0$ | $1$ | **$1$** | **Yes** | **Exclusive to $s_2$, single occurrence** | **Included** |

---

## 5. Boundary Cases & Failure Modes

- **Repeated Words in Single Sentence (e.g. $s_1 = \text{"apple apple"}, s_2 = \text{"banana"}$):** Total count of `"apple"` is $2$, so it is properly excluded without special duplicate tracking. Returns `["banana"]`.
- **All Words Overlap (e.g. $s_1 = \text{"a b"}, s_2 = \text{"a b"}$):** Every word has total count $2 \implies$ returns empty list `[]`.
- **Completely Disjoint Sentences:** Every word in both sentences appears once $\implies$ all words are returned.

---

## 6. Traps & Common Anti-Patterns

- **Checking $(w \in s_1 \land w \notin s_2)$ Using Set Operations Alone:** If a word appears twice in $s_1$ and zero times in $s_2$, a standard set difference `set(s1) - set(s2)` would incorrectly include it, even though the problem requires it to appear *exactly once* in $s_1$. Frequency counting handles internal duplicates correctly.
- **Nested Quadratic Scans:** Searching through strings with substring checks takes $\mathcal{O}(L_1 \cdot L_2)$ time; single-pass tokenization with hash tables takes $\mathcal{O}(L_1 + L_2)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Tokenizing strings of length $L_1$ and $L_2$: $\mathcal{O}(L_1 + L_2)$.
  - Hash map insertions and lookups for $W$ words: $\mathcal{O}(W)$.
  - Filtering entries: $\mathcal{O}(W)$.
  - Total Time: strictly $\mathcal{O}(L_1 + L_2)$, running in $< 1$ ms for sentence lengths $\le 200$.
- **Auxiliary Space Complexity:**
  - Hash map storing words and counts: $\mathcal{O}(L_1 + L_2)$ space.
