# Guided Example: Text Justification

We trace the step-by-step greedy word packing and whitespace distribution algorithm on a representative paragraph:

- **Input:** $\text{words} = [\text{"This"}, \text{"is"}, \text{"an"}, \text{"example"}, \text{"of"}, \text{"text"}, \text{"justification."}]$, $\text{maxWidth} = 16$
- **Required output:**
  ```text
  [
    "This    is    an",
    "example  of text",
    "justification.  "
  ]
  ```

This instance demonstrates greedy word line packing, even whitespace distribution with quotient and remainder ($Q = \lfloor \text{spaces} / \text{gaps} \rfloor$, $R = \text{spaces} \pmod{\text{gaps}}$), giving extra spaces to leftmost slots, and formatting the terminal line as left-justified.

---

## 1. Instance & Teaching Goal

Given an array of strings $\text{words}$ and a maximum width $\text{maxWidth} = 16$, format the text such that each line has exactly 16 characters and is fully justified.

Key formatting rules:
1. **Greedy Line Packing:** Pack as many words as possible on each line, assuming at least one space between adjacent words.
2. **Full Justification (Intermediate Lines):** Distribute spaces between words as evenly as possible. If the number of spaces does not divide evenly among slots, assign the extra spaces to the leftmost slots.
3. **Left Justification (Last Line & Single-Word Lines):** The last line and any line containing only one word must be left-justified, separated by single spaces, with all remaining spaces appended to the right.

---

## 2. Conceptual Foundation & Invariants

### 2-Phase Line Justification Algorithm

#### Phase 1: Greedy Word Gathering
Given index $i$, find the maximum index $j$ such that:
$$
\sum_{k=i}^{j-1} |\text{words}[k]| + (j - 1 - i) \le \text{maxWidth}
$$
where $j - 1 - i$ is the minimum number of single spaces between adjacent words.

#### Phase 2: Space Calculation & Slot Distribution
Let $L = \sum_{k=i}^{j-1} |\text{words}[k]|$ be the total letter length, and let $\text{gaps} = (j - i) - 1$.
Total spaces to distribute:
$$
\text{spaces} = \text{maxWidth} - L
$$

1. **Case A: Last Line ($j == N$) or Single Word ($\text{gaps} == 0$):**
   - Join words with a single space `' '`.
   - Pad the remaining width with trailing spaces on the right:
     $$
     \text{trailing} = \text{maxWidth} - \text{len}(\text{joined\_line})
     $$
2. **Case B: Intermediate Line with Multiple Words ($\text{gaps} > 0$):**
   - Base spaces per slot:
     $$
     Q = \lfloor \text{spaces} / \text{gaps} \rfloor
     $$
   - Remainder extra spaces (distributed one by one to the first $R$ slots):
     $$
     R = \text{spaces} \pmod{\text{gaps}}
     $$
   - Slot $k \in [0, \text{gaps} - 1]$ receives $Q + 1$ spaces if $k < R$, else $Q$ spaces.

> **Invariant.** Every generated line has length strictly equal to $\text{maxWidth}$, and no word is truncated or reordered.

---

## 3. Step-by-Step Worked Execution

We format $\text{words} = [\text{"This"}, \text{"is"}, \text{"an"}, \text{"example"}, \text{"of"}, \text{"text"}, \text{"justification."}]$ with $\text{maxWidth} = 16$:

### Line 1 Processing
- Greedy packing from $i = 0$:
  - `"This"` ($4$)
  - `"is"` ($2$): $4 + 1 + 2 = 7 \le 16$.
  - `"an"` ($2$): $7 + 1 + 2 = 10 \le 16$.
  - `"example"` ($7$): $10 + 1 + 7 = 18 > 16$. Cannot fit!
- Selected words for Line 1: `["This", "is", "an"]` ($i = 0 \to j = 3$).
- Letter count: $L = 4 + 2 + 2 = 8$.
- Total spaces: $16 - 8 = 8$.
- Gaps: $3 - 1 = 2$.
- Distribution:
  - Base: $Q = \lfloor 8 / 2 \rfloor = 4$.
  - Remainder: $R = 8 \pmod 2 = 0$.
  - Both gaps receive exactly 4 spaces.
- Line 1 assembled: `"This    is    an"` (Length 16).

---

### Line 2 Processing
- Greedy packing from $i = 3$:
  - `"example"` ($7$)
  - `"of"` ($2$): $7 + 1 + 2 = 10 \le 16$.
  - `"text"` ($4$): $10 + 1 + 4 = 15 \le 16$.
  - `"justification."` ($14$): $15 + 1 + 14 = 30 > 16$. Cannot fit!
- Selected words for Line 2: `["example", "of", "text"]` ($i = 3 \to j = 6$).
- Letter count: $L = 7 + 2 + 4 = 13$.
- Total spaces: $16 - 13 = 3$.
- Gaps: $3 - 1 = 2$.
- Distribution:
  - Base: $Q = \lfloor 3 / 2 \rfloor = 1$.
  - Remainder: $R = 3 \pmod 2 = 1$.
  - Gap 0 (left): receives $Q + 1 = 2$ spaces.
  - Gap 1 (right): receives $Q = 1$ space.
- Line 2 assembled: `"example  of text"` (Length 16).

---

### Line 3 Processing (Terminal Line)
- Greedy packing from $i = 6$:
  - `"justification."` ($14 \le 16$).
  - End of words list ($j = 7 = N$).
- Selected words: `["justification."]`.
- Rule applied: **Last Line Rule (Left-Justified)**.
  - No inter-word gaps ($\text{gaps} = 0$).
  - Trailing spaces on right: $16 - 14 = 2$ spaces.
- Line 3 assembled: `"justification.  "` (Length 16).

All words formatted into 3 justified lines.

### The Greedy Accumulator in Detail

Phase 1 keeps a running width `cnt` that already includes one mandatory space per junction. A candidate word is admitted only when `cnt + 1 + |word|` still fits, and the first rejection closes the line:

| Line | Word index | Word | $\lvert \text{word} \rvert$ | Candidate width `cnt + 1 + len` | Fits in $16$? | Action | `cnt` after |
|:---:|:---:|:---|:---:|:---:|:---:|:---|:---:|
| 1 | 0 | `This` | 4 | 4 (opening word) | yes | Open line 1 | 4 |
| 1 | 1 | `is` | 2 | 7 | yes | Admit | 7 |
| 1 | 2 | `an` | 2 | 10 | yes | Admit | 10 |
| 1 | 3 | `example` | 7 | 18 | **no** | Close line 1; restart at index 3 | — |
| 2 | 3 | `example` | 7 | 7 (opening word) | yes | Open line 2 | 7 |
| 2 | 4 | `of` | 2 | 10 | yes | Admit | 10 |
| 2 | 5 | `text` | 4 | 15 | yes | Admit | 15 |
| 2 | 6 | `justification.` | 14 | 30 | **no** | Close line 2; restart at index 6 | — |
| 3 | 6 | `justification.` | 14 | 14 (opening word) | yes | Open line 3, then the list ends | 14 |

The rejected widths $18$ and $30$ are precisely why `example` and `justification.` never join the preceding line, even though each would fit alone. Because every word satisfies $\lvert \text{word} \rvert \le \text{maxWidth}$, each line admits at least one word, so the index $i$ strictly increases and the loop terminates.

---

## 4. Complete Execution Trace

| Line | Words Included | Total Word Chars $L$ | Inter-Word Gaps | Total Spaces | Space Allocation Per Gap | Produced Line Output |
|:---:|:---|:---:|:---:|:---:|:---|:---|
| 1 | `["This", "is", "an"]` | 8 | 2 | 8 | Gap 0: 4, Gap 1: 4 | `"This    is    an"` |
| 2 | `["example", "of", "text"]` | 13 | 2 | 3 | Gap 0: 2, Gap 1: 1 | `"example  of text"` |
| 3 | `["justification."]` | 14 | 0 (Last) | 2 | Left-aligned + 2 trailing | `"justification.  "` |

---

## 5. Algorithmic Correctness

**Soundness.** Intermediate lines calculate $Q = \lfloor \text{spaces}/\text{gaps} \rfloor$ and $R = \text{spaces} \pmod{\text{gaps}}$. Because $R < \text{gaps}$, awarding $Q+1$ to the first $R$ gaps and $Q$ to the rest sums to $R(Q + 1) + (\text{gaps} - R)Q = \text{gaps} \cdot Q + R = \text{spaces}$, guaranteeing the output line has length exactly $\text{maxWidth}$.

**Completeness.** Since every individual word satisfies $|\text{word}| \le \text{maxWidth}$, each line packs at least one word, monotonically advancing index $i$. All words are eventually placed in order.

---

## 6. Traps This Instance Exposes

- **Single Word on Intermediate Line:** If a line contains only one long word that fits (e.g. `"acknowledgment"` with width 16), $\text{gaps} = 0$. Attempting division by zero causes a crash. Single-word lines must be treated like the last line (left-justified with all spaces on the right).
- **Even vs Leftmost Space Bias:** When spaces don't divide evenly (e.g. 3 spaces into 2 gaps), standard typography and problem rules mandate that the extra space belongs to the left gap (`2` then `1`), not the right.
- **Spaces on Last Line:** Words on the last line must have strictly **one** space between them, with all surplus padding at the tail. Applying full justification to the last line is incorrect.

Each rule in the two-phase algorithm is exercised by a distinct instance, and the arithmetic below is what the distribution must reproduce:

| Scenario | Input | Which rule fires | Spaces arithmetic | Expected line |
|:---|:---|:---|:---|:---|
| Standard paragraph, line 1 | `["This","is","an","example","of","text","justification."]`, width $16$ | Intermediate, multiple words | $L = 8$, $\text{gaps} = 2$, $\text{spaces} = 8 \Rightarrow Q = 4, R = 0$ | `This    is    an` |
| Standard paragraph, line 2 | same input | Intermediate, uneven split | $L = 13$, $\text{gaps} = 2$, $\text{spaces} = 3 \Rightarrow Q = 1, R = 1$ | `example  of text` |
| Single-word middle line | `["What","must","be","acknowledgment","shall","be"]`, width $16$ | Single word, not the last line | $\text{gaps} = 0$; trailing $= 16 - 14 = 2$ | `acknowledgment  ` |
| One-word input | `["word"]`, width $8$ | Single word that is also the last line | $\text{gaps} = 0$; trailing $= 8 - 4 = 4$ | `word    ` |
| Leftmost bias | `["a","b","c","d"]`, width $6$ | Intermediate, remainder $R > 0$ | $L = 3$, $\text{gaps} = 2$, $\text{spaces} = 3 \Rightarrow Q = 1, R = 1$ | `a  b c` |
| Exact-width words | `["abcd","efgh","i","j"]`, width $4$ | Single word filling the width | $L = 4$, $\text{gaps} = 0$; trailing $= 4 - 4 = 0$ | `abcd` |

The last two rows separate the two biases: three spaces across two gaps gives the surplus to the *left* gap (`2` then `1`), while a word that already fills the width leaves a single-word line with zero trailing space and no gap division at all.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot W)$, where $N$ is the number of words and $W = \text{maxWidth}$. Each word is visited once to determine line membership and once to construct the string.
- **Auxiliary Space Complexity:** $O(N \cdot W)$ to store the formatted lines list.
