# Guided Example: Reverse Words in a String III

We trace the step-by-step whitespace-delimited word tokenization, in-place character reversal within isolated token boundaries, global word order preservation, whitespace delimiter reconstruction, and linear single-pass string assembly on representative sentences:

- **Input:** $s = \text{"Let's take LeetCode contest"}$
- **Required output:** `"s'teL ekat edoCteeL tsetnoc"`
  - Problem contract:
    - Reverse the order of characters within **each individual word**.
    - Preserve the original sequence of words in the sentence.
    - Preserve single whitespace separators between adjacent words.
- **Token-by-Token Reversal Execution Trace:**
  - **Step 1: Partition into Word Tokens:**
    - Parse string by space separator:
      $$
      \text{words} = [\text{"Let's"}, \; \text{"take"}, \; \text{"LeetCode"}, \; \text{"contest"}]
      $$
  - **Step 2: Reverse Characters in Each Word Individually:**
    - **Word 0: $w_0 = \text{"Let's"}$ (Length 5):**
      - Original character sequence: `['L', 'e', 't', ''', 's']`
      - Two-pointer reflection:
        - Swap index $0$ and $4$: `'L'` $\leftrightarrow$ `'s'`
        - Swap index $1$ and $3$: `'e'` $\leftrightarrow$ `'''`
        - Index $2$ remains `'t'`
      - Inverted word:
        $$
        w_0' = \mathbf{\text{"s'teL"}}
        $$
    - **Word 1: $w_1 = \text{"take"}$ (Length 4):**
      - Characters: `['t', 'a', 'k', 'e']`
      - Swap index $0$ and $3$: `'t'` $\leftrightarrow$ `'e'`
      - Swap index $1$ and $2$: `'a'` $\leftrightarrow$ `'k'`
      - Inverted word:
        $$
        w_1' = \mathbf{\text{"ekat"}}
        $$
    - **Word 2: $w_2 = \text{"LeetCode"}$ (Length 8):**
      - Characters: `['L', 'e', 'e', 't', 'C', 'o', 'd', 'e']`
      - Invert characters:
        $$
        w_2' = \mathbf{\text{"edoCteeL"}}
        $$
    - **Word 3: $w_3 = \text{"contest"}$ (Length 7):**
      - Characters: `['c', 'o', 'n', 't', 'e', 's', 't']`
      - Invert characters:
        $$
        w_3' = \mathbf{\text{"tsetnoc"}}
        $$
  - **Step 3: Reassemble Sentence with Spaces:**
    - Join transformed tokens in original order:
      $$
      ans = w_0' + \text{" "} + w_1' + \text{" "} + w_2' + \text{" "} + w_3'
      $$
      $$
      ans = \text{"s'teL"} + \text{" "} + \text{"ekat"} + \text{" "} + \text{"edoCteeL"} + \text{" "} + \text{"tsetnoc"} = \mathbf{\text{"s'teL ekat edoCteeL tsetnoc"}}
      $$
- **Two Words Instance ($s = \text{"Mr Ding"}$):**
  - $\text{"Mr"} \to \text{"rM"}$
  - $\text{"Ding"} \to \text{"gniD"}$
  - Result: $\mathbf{\text{"rM gniD"}}$.
- **Single Character Word ($s = \text{"a"}$):**
  - Length 1 $\implies$ reversal is identical $\implies \mathbf{\text{"a"}}$.
- **Preservation of Punctuation:**
  - Punctuation attached to words (like apostrophe in `"Let's"`) reverses along with the word letters, transforming into `"s'teL"`.

This instance demonstrates partitioned string inversion across regular delimiter boundaries, mathematically proves why local word inversion leaves inter-token ordering invariant, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a sentence string $s$:
Reverse the order of characters within each word while preserving the order of the words themselves and single space separators.

```text
Input:  "Let's take LeetCode contest"
Tokens: ["Let's", "take", "LeetCode", "contest"]

Reversing each token:
  "Let's"    -> "s'teL"
  "take"     -> "ekat"
  "LeetCode" -> "edoCteeL"
  "contest"  -> "tsetnoc"

Output: "s'teL ekat edoCteeL tsetnoc"
```

### Contrast with "Reverse Words in a String I"
- In standard LeetCode 151 (*Reverse Words in a String*):
  The **order of words** is reversed, but characters inside each word are preserved (`"the sky is blue"` $\to$ `"blue is sky the"`).
- In this problem (LeetCode 557):
  The **characters inside each word** are reversed, but the **order of the words** is preserved (`"the sky"` $\to$ `"eht yks"`).

---

## 2. Conceptual Foundation & Invariants

### 1. Invariant of Independent Local Inversion:
Let a sentence be a sequence of tokens separated by spaces:
$$
S = w_0 \cdot \text{" "} \cdot w_1 \cdot \text{" "} \dots \cdot \text{" "} \cdot w_{k-1}
$$
The transformation maps each $w_i$ to its string reverse $\text{rev}(w_i)$:
$$
f(S) = \text{rev}(w_0) \cdot \text{" "} \cdot \text{rev}(w_1) \dots \cdot \text{" "} \cdot \text{rev}(w_{k-1})
$$

### 2. Two-Pointer In-Place Inversion:
For any token of length $m$:
- Initialize $l = 0, \; r = m - 1$.
- While $l < r$:
  Swap character at $l$ with character at $r$.
  $l \leftarrow l + 1, \; r \leftarrow r - 1$.

> **Positional Separator Invariant.** The index positions of the space delimiters in the final sentence are identical to their positions in the original sentence.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"Mr Ding"}$:

---

### Step 1: Tokenize
- Token 0: `"Mr"`
- Token 1: `"Ding"`

---

### Step 2: Reverse Tokens
- Token 0 (`"Mr"`):
  - Characters: `['M', 'r']`
  - Swap index 0 and 1 $\implies$ `['r', 'M']` $\implies \mathbf{\text{"rM"}}$.
- Token 1 (`"Ding"`):
  - Characters: `['D', 'i', 'n', 'g']`
  - Swap index 0 and 3: `'D'` $\leftrightarrow$ `'g'`
  - Swap index 1 and 2: `'i'` $\leftrightarrow$ `'n'`
  - Inverted $\implies \mathbf{\text{"gniD"}}$.

---

### Step 3: Join with Single Space
$$
\text{"rM"} + \text{" "} + \text{"gniD"} = \mathbf{\text{"rM gniD"}}
$$

---

## 4. Complete Execution Trace

| Original Token $w_i$ | Token Length | Left-Right Swaps | Reversed Token $\text{rev}(w_i)$ |
|:---:|:---:|:---:|:---:|
| `"Let's"` | $5$ | $0 \leftrightarrow 4, \; 1 \leftrightarrow 3$ | **`"s'teL"`** |
| `"take"` | $4$ | $0 \leftrightarrow 3, \; 1 \leftrightarrow 2$ | **`"ekat"`** |
| `"LeetCode"` | $8$ | $0 \leftrightarrow 7, \; 1 \leftrightarrow 6, \; 2 \leftrightarrow 5, \; 3 \leftrightarrow 4$ | **`"edoCteeL"`** |
| `"contest"` | $7$ | $0 \leftrightarrow 6, \; 1 \leftrightarrow 5, \; 2 \leftrightarrow 4$ | **`"tsetnoc"`** |
| **Joined Output** | — | — | **`"s'teL ekat edoCteeL tsetnoc"`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Word Without Spaces (`"Hello"`):** Reverses directly to `"olleH"`.
- **Single Letter Words (`"a b c"`):** Reverses to `"a b c"` (identity).
- **Special Characters and Punctuation:** Treated as normal characters within tokens (e.g. `"I'm"` $\to$ `"m'I"`).
- **Even vs Odd Length Words:** Two-pointer swap handles even and odd word lengths seamlessly without off-by-one errors.

---

## 6. Traps & Common Anti-Patterns

- **Reversing the Entire String First:** If you reverse the entire sentence first, you get `"tsetnoc edoCteeL ekat s'teL"`. To fix it, you would then have to reverse the list of words again. Reversing each word directly in a single pass is cleaner and requires half the operations.
- **Dropping Spaces or Trimming:** Sentences contain exact single spaces that must be preserved. Using regex split without careful re-joining can distort whitespace formatting.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Tokenizing the string: $O(N)$ where $N$ is the total length of the string.
  - Reversing each character within words visits each character exactly once: $O(N)$.
  - Joining the reversed words with spaces: $O(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 5 \times 10^4$, completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to hold the split tokens and construct the final string.
