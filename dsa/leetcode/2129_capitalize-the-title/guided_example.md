# Guided Example: Capitalize the Title

We trace the step-by-step execution of the optimal piecewise word-length normalization approach on a representative problem instance:

- **Input String (`title`):** `"First leTTeR of EACH Word"`
- **Expected Output:** `"First Letter of Each Word"`

This instance illustrates the conditional casing bifurcation based on token length, showcasing how short words (length $\le 2$) undergo total lowercasing while longer words (length $\ge 3$) receive leading title capitalization with trailing lowercase normalization.

---

## 1. Problem Overview & Representative Instance

We are given a string `title` consisting of words separated by single space characters. Each word comprises uppercase and lowercase English letters. We must capitalize the string according to length-based rules:
1. If the length of a word is $1$ or $2$ letters, convert every character to lowercase.
2. If the length of a word is $3$ or more letters, convert the first character to uppercase and all remaining characters to lowercase.

Consider our representative instance:
`"First leTTeR of EACH Word"`
- `"First"`: Length $5 \ge 3 \implies$ Capitalized to `"First"`.
- `"leTTeR"`: Length $6 \ge 3 \implies$ Capitalized to `"Letter"`.
- `"of"`: Length $2 \le 2 \implies$ Completely lowercased to `"of"`.
- `"EACH"`: Length $4 \ge 3 \implies$ Capitalized to `"Each"`.
- `"Word"`: Length $4 \ge 3 \implies$ Capitalized to `"Word"`.

Joined with spaces, the normalized sentence becomes `"First Letter of Each Word"`.

---

## 2. Mathematical & Algorithmic Principles

### Token Partitioning and Invariant Transformation
Let the string $T$ be partitioned into an ordered sequence of words $W = [w_1, w_2, \dots, w_k]$ delimited by ASCII spaces $0x20$.
Because each word $w_i$ is processed independently, the title transformation decomposes into a coordinate-wise mapping $\Phi$:

$$\Phi(w) = \begin{cases} \text{lower}(w), & |w| \le 2 \\ \text{upper}(w[0]) \cdot \text{lower}(w[1 \dots |w|-1]), & |w| \ge 3 \end{cases}$$

1. **Short Word Invariant ($|w| \in \{1, 2\}$):** Prepositions, articles, or single initials must not retain any capital letters. For example, `"OF"` and `"oF"` both map to `"of"`, and `"I"` maps to `"i"`.
2. **Standard Word Invariant ($|w| \ge 3$):** Mixed internal capitalizations (such as `"leTTeR"`) must be systematically lowered to prevent stray capitals from persisting. Only the first character is capitalized.

### Single-Pass Linear Transformation
Words can be transformed in place or accumulated via a streaming string builder, consuming $\mathcal{O}(N)$ time and maintaining the original single space delimiters between words.

| Word Length Rule | Condition | Case Rule for Character at Index $0$ | Case Rule for Characters at Indices $\ge 1$ |
|---|---|---|---|
| Short Token | $\lvert w \rvert \le 2$ | Lowercase | Lowercase |
| Standard Token | $\lvert w \rvert \ge 3$ | Uppercase | Lowercase |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Input: `title = "First leTTeR of EACH Word"`.
Word tokens extracted: `["First", "leTTeR", "of", "EACH", "Word"]`.

### Token 1: `"First"`
- Length $|w| = 5 \ge 3$.
- Standard token branch selected.
- Character $0$: `'F' \to \text{'F'}`.
- Suffix $1 \dots 4$: `"irst" \to \text{"irst"}`.
- Result: `"First"`.

### Token 2: `"leTTeR"`
- Length $|w| = 6 \ge 3$.
- Standard token branch selected.
- Character $0$: `'l' \to \text{'L'}`.
- Suffix $1 \dots 5$: `"eTTeR" \to \text{"etter"}` (internal capitals lowered).
- Result: `"Letter"`.

### Token 3: `"of"`
- Length $|w| = 2 \le 2$.
- Short token branch selected.
- Entire string lowercased: `"of" \to \text{"of"}`.
- Result: `"of"`.

### Token 4: `"EACH"`
- Length $|w| = 4 \ge 3$.
- Standard token branch selected.
- Character $0$: `'E' \to \text{'E'}`.
- Suffix $1 \dots 3$: `"ACH" \to \text{"ach"}`.
- Result: `"Each"`.

### Token 5: `"Word"`
- Length $|w| = 4 \ge 3$.
- Standard token branch selected.
- Character $0$: `'W' \to \text{'W'}`.
- Suffix $1 \dots 3$: `"ord" \to \text{"ord"}`.
- Result: `"Word"`.

### Sentence Reconstruction
Joining the transformed tokens with single spaces yields:
`"First" + " " + "Letter" + " " + "of" + " " + "Each" + " " + "Word"`
$=$ `"First Letter of Each Word"`.

---

## 4. Comprehensive State Trace

The transformation results for all tokens are detailed below:

| Token Index | Original Token Text | Measured Length | Applicable Rule | Head Transform | Tail Transform | Output Token |
|---|---|---|---|---|---|---|
| $0$ | `"First"` | $5$ | Standard ($\lvert w \rvert \ge 3$) | `'F' \to \text{'F'}` | `"irst" \to \text{"irst"}` | `"First"` |
| $1$ | `"leTTeR"` | $6$ | Standard ($\lvert w \rvert \ge 3$) | `'l' \to \text{'L'}` | `"eTTeR" \to \text{"etter"}` | `"Letter"` |
| $2$ | `"of"` | $2$ | Short ($\lvert w \rvert \le 2$) | `'o' \to \text{'o'}` | `'f' \to \text{'f'}` | `"of"` |
| $3$ | `"EACH"` | $4$ | Standard ($\lvert w \rvert \ge 3$) | `'E' \to \text{'E'}` | `"ACH" \to \text{"ach"}` | `"Each"` |
| $4$ | `"Word"` | $4$ | Standard ($\lvert w \rvert \ge 3$) | `'W' \to \text{'W'}` | `"ord" \to \text{"ord"}` | `"Word"` |

Concatenated result: `"First Letter of Each Word"`.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** The length threshold $|w| < 3$ partitions words into two mutually exclusive sets: $\{1, 2\}$ and $\{3, 4, \dots\}$. By applying full string lowercasing on words of length 1 or 2, all letters are guaranteed to be lowercase. By applying uppercase conversion to the first character and lowercase conversion to all subsequent characters on words of length $\ge 3$, both the leading capitalization and the trailing lowercase invariants are guaranteed, regardless of the input word's initial casing.

**Completeness.** Every word in `title` is isolated and processed in left-to-right sequence. Because the problem guarantees single-space delimitation with no leading or trailing whitespace, joining the transformed tokens preserves the exact word count, word order, and spacing structure of the original sentence.

---

## 6. Edge Cases & Anti-Patterns

- **Single-Letter Words:** Words like `"a"` or `"I"` have length $1 \le 2$, and are transformed to lowercase (`"a"`, `"i"`).
- **All Upper-Case Short Words:** A word like `"OF"` must not become `"Of"`; it correctly transforms to `"of"`.
- **Length Exactly Three:** Words of length $3$ (such as `"the"`) reach the threshold $\ge 3$ and must be capitalized (`"The"`).
- **Anti-Pattern — Built-in `title()` Method:** Standard language title-case functions (e.g. Python's `str.title()`) capitalize every word unconditionally, incorrectly turning `"of"` into `"Of"`. Applying explicit piecewise length branches is required.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the total number of characters in `title`. Tokenizing the string, calculating word lengths, changing letter cases, and joining the results each take linear time proportional to $N$.
- **Auxiliary Space Complexity:** $\mathcal{O}(N)$ auxiliary memory to store the list of word tokens and construct the final output string.
