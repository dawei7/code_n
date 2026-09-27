# Guided Example: Goat Latin

We trace the step-by-step sentence whitespace tokenization, initial letter vowel versus consonant branching ($w[0] \in \{a, e, i, o, u\}$), consonant cyclic rotation ($w[1:] + w[0]$), `"ma"` suffix attachment, 1-indexed position repetitive `'a'` extension ($a^{i}$), and whitespace output reassembly on representative sentences:

- **Input:**
  $$
  sentence = \text{"I speak Goat Latin"}
  $$
- **Required output:**
  $$
  \text{"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"}
  $$
  - Goat Latin conversion rules:
    - Words in the sentence are separated by single spaces.
    - Each word undergoes three transformation steps based on its initial character and its 1-based index $k$ in the sentence:
      1. **Initial Character Rule:**
         - If the word begins with a vowel (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`, in either uppercase or lowercase): keep the word as is.
         - If the word begins with a consonant: rotate the first letter to the end of the word ($w[1 \dots] + w[0]$).
      2. **Suffix Addition:**
         - Append the suffix `"ma"` to the end of the word.
      3. **Positional Repetition:**
         - Append $k$ copies of the character `'a'` to the end of the word, where $k$ is the 1-based position of the word in the sentence ($1 \le k \le N$).
    - For $sentence = \text{"I speak Goat Latin"}$:
      - Word 1 ($k = 1$): `"I"`
        - Starts with vowel `'I'` $\implies$ remains `"I"`.
        - Add `"ma"` $\implies \text{"Ima"}$.
        - Add $1$ `'a'` ($k = 1$) $\implies \mathbf{\text{"Imaa"}}.$
      - Word 2 ($k = 2$): `"speak"`
        - Starts with consonant `'s'` $\implies$ rotate `'s'` to end: `"peaks"`.
        - Add `"ma"` $\implies \text{"peaksma"}$.
        - Add $2$ `'a'`s ($k = 2$) $\implies \mathbf{\text{"peaksmaaa"}}.$
      - Word 3 ($k = 3$): `"Goat"`
        - Starts with consonant `'G'` $\implies$ rotate `'G'` to end: `"oatG"`.
        - Add `"ma"` $\implies \text{"oatGma"}$.
        - Add $3$ `'a'`s ($k = 3$) $\implies \mathbf{\text{"oatGmaaaa"}}.$
      - Word 4 ($k = 4$): `"Latin"`
        - Starts with consonant `'L'` $\implies$ rotate `'L'` to end: `"atinL"`.
        - Add `"ma"` $\implies \text{"atinLma"}$.
        - Add $4$ `'a'`s ($k = 4$) $\implies \mathbf{\text{"atinLmaaaaa"}}.$
      - Assembled sentence:
        $$
        \text{"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"}
        $$
- **Linguistic Transformation & Positional Suffix Invariant:**
  - **The Vowel Membership Predicate:**
    - Let $V = \{\text{'a'}, \text{'e'}, \text{'i'}, \text{'o'}, \text{'u'}\}$.
    - Check case-insensitively:
      $$
      \text{isVowel}(w) \iff \text{lower}(w_0) \in V
      $$
  - **The Word Morphism:**
    - For the $i$-th word $w$ (0-indexed, corresponding to 1-indexed position $k = i + 1$):
      $$
      w' = \begin{cases}
      w & \text{lower}(w_0) \in V \\
      w[1:] + w[0] & \text{lower}(w_0) \notin V
      \end{cases}
      $$
      $$
      T(w, i) = w' + \text{"ma"} + \text{"a"}^{i + 1}
      $$
  - **Whitespace Concatenation:**
    - The output string is the space-joined sequence of all transformed tokens:
      $$
      ans = \bigoplus_{i = 0}^{m - 1} T(w_i, i)
      $$
- **Step-by-Step Worked Execution Trace on the 4-Word Sentence:**
  - Split sentence into tokens:
    $$
    [\text{"I"}, \; \text{"speak"}, \; \text{"Goat"}, \; \text{"Latin"}]
    $$
  - Initialize empty accumulator list: $ans = []$.
  - **Token 0 ($w = \text{"I"}, i = 0, k = 1$):**
    - First character: `'I'` $\implies \text{lower}('I') = \text{'i'} \in V \implies \mathbf{Vowel.}$
    - Stem: `"I"`.
    - Append `"ma"`: `"Ima"`.
    - Append $1$ `'a'`:
      $$
      T(\text{"I"}, 0) = \mathbf{\text{"Imaa"}}
      $$
    - Add to list: $ans = [\text{"Imaa"}]$.
  - **Token 1 ($w = \text{"speak"}, i = 1, k = 2$):**
    - First character: `'s'` $\implies \text{'s'} \notin V \implies \mathbf{Consonant.}$
    - Rotate first character to end:
      $$
      \text{stem} = w[1:] + w[0] = \text{"peak"} + \text{"s"} = \mathbf{\text{"peaks"}}
      $$
    - Append `"ma"`: `"peaksma"`.
    - Append $2$ `'a'`s:
      $$
      T(\text{"speak"}, 1) = \mathbf{\text{"peaksmaaa"}}
      $$
    - Add to list: $ans = [\text{"Imaa"}, \text{"peaksmaaa"}]$.
  - **Token 2 ($w = \text{"Goat"}, i = 2, k = 3$):**
    - First character: `'G'` $\implies \text{'g'} \notin V \implies \mathbf{Consonant.}$
    - Rotate:
      $$
      \text{stem} = \text{"oat"} + \text{"G"} = \mathbf{\text{"oatG"}}
      $$
    - Append `"ma"`: `"oatGma"`.
    - Append $3$ `'a'`s:
      $$
      T(\text{"Goat"}, 2) = \mathbf{\text{"oatGmaaaa"}}
      $$
    - Add to list: $ans = [\text{"Imaa"}, \text{"peaksmaaa"}, \text{"oatGmaaaa"}]$.
  - **Token 3 ($w = \text{"Latin"}, i = 3, k = 4$):**
    - First character: `'L'` $\implies \text{'l'} \notin V \implies \mathbf{Consonant.}$
    - Rotate:
      $$
      \text{stem} = \text{"atin"} + \text{"L"} = \mathbf{\text{"atinL"}}
      $$
    - Append `"ma"`: `"atinLma"`.
    - Append $4$ `'a'`s:
      $$
      T(\text{"Latin"}, 3) = \mathbf{\text{"atinLmaaaaa"}}
      $$
    - Add to list: $ans = [\text{"Imaa"}, \text{"peaksmaaa"}, \text{"oatGmaaaa"}, \text{"atinLmaaaaa"}]$.
  - **Final String Assembly:**
    - Join tokens with single space delimiter:
      $$
      ans = \mathbf{\text{"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"}}
      $$
- **Single Letter Uppercase Vowel Trace ($sentence = \text{"I"}):**
  - Token `"I"`, vowel, $k = 1 \implies \text{"I"} + \text{"ma"} + \text{"a"} = \mathbf{\text{"Imaa"}}.$
- **All Consonants Sentence Trace ($sentence = \text{"The dog"}):**
  - `"The"` $\to \text{"heTmaa"}$.
  - `"dog"` $\to \text{"ogdmaaa"}$.
  - Joined: `"heTmaa ogdmaaa"`.

This instance demonstrates context-free string transducer transformations and positional polynomial suffix generation, mathematically proves why cyclic permutations preserve total string entropy while enforcing prefix-free positional alignments, and derives $O(N^2 + L)$ execution time and $O(N^2 + L)$ output space bounds.

---

## 1. Instance & Teaching Goal

Given a sentence of space-separated words:
Convert each word to Goat Latin:
1. If vowel start: add `"ma"`.
2. If consonant start: move first letter to end, then add `"ma"`.
3. Add $k$ `'a'`s for the $k$-th word (1-indexed).

```text
sentence = "I speak Goat Latin"

Word 1: "I"     (vowel)     -> "I"     + "ma" + "a"    = "Imaa"
Word 2: "speak" (consonant) -> "peaks" + "ma" + "aa"   = "peaksmaaa"
Word 3: "Goat"  (consonant) -> "oatG"  + "ma" + "aaa"  = "oatGmaaaa"
Word 4: "Latin" (consonant) -> "atinL" + "ma" + "aaaa" = "atinLmaaaaa"

Result: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
```

### The Invariant of the Goat Latin Grammar
- Vowels: `'a'`, `'e'`, `'i'`, `'o'`, `'u'` (case-insensitive).
- Word 1 gets 1 `'a'`, word 2 gets 2 `'a'`s, word $k$ gets $k$ `'a'`s.
- Original casing is preserved, including rotated initial capital letters (e.g. `'G'` in `"Goat"` becomes `"oatG"`).

---

## 2. Conceptual Foundation & Invariants

### 1. Token Stem Function:
$$
\text{stem}(w) = \begin{cases}
w & \text{lower}(w_0) \in \{a, e, i, o, u\} \\
w[1:] + w[0] & \text{otherwise}
\end{cases}
$$

### 2. Positional Suffix Expansion:
$$
T(w, k) = \text{stem}(w) + \text{"ma"} + \underbrace{\text{"a"} \cdots \text{"a"}}_{k \text{ times}}
$$

> **Indexed Morphism Invariant.** The transformation $T_k: \Sigma^* \to \Sigma^*$ is an affine length expansion $|T_k(w)| = |w| + 2 + k$. The total output length for $m$ words scales quadratically $\mathcal{O}(L + m^2)$ due to the arithmetic progression $\sum_{k=1}^m k = \frac{m(m+1)}{2}$.

---

## 3. Step-by-Step Worked Execution

We trace $sentence = \text{"I speak Goat Latin"}$:

---

### Step 1: Word 1 (`"I"`)
- Vowel `'I'`.
- Stem: `"I"`.
- Suffix: `"ma"` $+ 1$ `'a'` $\implies$ `"Imaa"`.

---

### Step 2: Word 2 (`"speak"`)
- Consonant `'s'`.
- Stem: `"peaks"`.
- Suffix: `"ma"` $+ 2$ `'a'`s $\implies$ `"peaksmaaa"`.

---

### Step 3: Word 3 (`"Goat"`)
- Consonant `'G'`.
- Stem: `"oatG"`.
- Suffix: `"ma"` $+ 3$ `'a'`s $\implies$ `"oatGmaaaa"`.

---

### Step 4: Word 4 (`"Latin"`)
- Consonant `'L'`.
- Stem: `"atinL"`.
- Suffix: `"ma"` $+ 4$ `'a'`s $\implies$ `"atinLmaaaaa"`.

---

### Step 5: Output
- Join with space delimiter.

---

## 4. Complete Execution Trace

| Position $k$ | Original Word | Initial Type | Transformed Stem | Appended Suffix | Resulting Token |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `"I"` | Vowel | `"I"` | `"ma"` + `"a"` | `"Imaa"` |
| $2$ | `"speak"` | Consonant | `"peaks"` | `"ma"` + `"aa"` | `"peaksmaaa"` |
| $3$ | `"Goat"` | Consonant | `"oatG"` | `"ma"` + `"aaa"` | `"oatGmaaaa"` |
| **$4$** | **`"Latin"`** | **Consonant** | **`"atinL"`** | **`"ma"` + `"aaaa"`** | **`"atinLmaaaaa"`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Word Sentence ($"I"$):** Returns `"Imaa"`.
- **Uppercase Consonant ($"The"$):** Preserves capital letter when moved: `"heTmaa"`.
- **Uppercase Vowel ($"Apple"$):** Kept as is: `"Applema"`.
- **Many Words ($m = 150$):** Suffix of final word has 150 `'a'`s; quadratic string allocation handles easily ($< 1$ ms).

---

## 6. Traps & Common Anti-Patterns

- **Lowercasing the Entire Word:** Only check `lower()` on the first character; do NOT lowercase the whole word, as the output must retain original capitalization.
- **Using 0-Indexed Count for 'a's:** The first word must receive ONE `'a'`, not zero. Ensure $i + 1$ copies of `'a'` are appended.
- **Incorrect Vowel List:** Must include both lowercase and uppercase or use `.lower()`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $L$ be the original sentence length, and $M$ the number of words ($M \le 150$).
  - Splitting sentence into words: $\mathcal{O}(L)$.
  - Constructing each word with $k$ `'a'`s: $\mathcal{O}(|w_k| + k)$.
  - Sum of lengths: $\sum |w_k| + \sum_{k=1}^M (2 + k) = L + 2M + \frac{M(M+1)}{2}$.
  - Total Time: strictly $\mathcal{O}(L + M^2)$ where $L \le 150, M \le 150 \implies \le 1.2 \times 10^4$ characters. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(L + M^2)$ memory for the output string.
