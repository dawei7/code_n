# Guided Example: Most Common Word

We trace the step-by-step case normalization to lowercase ($c \to \text{lower}(c)$), non-alphanumeric punctuation delimiter tokenization, banned word set filtering ($w \notin B$), frequency dictionary accumulation ($cnt[w] \mathrel{+}= 1$), and maximal frequency token extraction on representative natural language passages:

- **Input:**
  $$
  paragraph = \text{"Bob hit a ball, the hit BALL flew far after it was hit."}
  $$
  $$
  banned = [\text{"hit"}]
  $$
- **Required output:**
  $$
  \text{"ball"}
  $$
  - Word parsing & frequency rules:
    - Words in the paragraph are case-insensitive and separated by spaces or punctuation symbols (`!`, `?`, `'`, `,`, `;`, `.`).
    - The answer must be returned in lowercase.
    - Any word appearing in the $banned$ list is disqualified from selection.
    - We must return the **most frequent unbanned word**. The problem guarantees a unique answer.
    - For the sample paragraph:
      - Lowercase conversion: `"bob hit a ball, the hit ball flew far after it was hit."`
      - Extracted word tokens:
        $$
        [\text{"bob"}, \text{"hit"}, \text{"a"}, \text{"ball"}, \text{"the"}, \text{"hit"}, \text{"ball"}, \text{"flew"}, \text{"far"}, \text{"after"}, \text{"it"}, \text{"was"}, \text{"hit"}]
        $$
      - Word `"hit"` appears 3 times, but is **banned**.
      - Word `"ball"` appears 2 times, and is not banned.
      - All other unbanned words appear only 1 time.
      - Output: `"ball"`.
- **Lexical Tokenization & Hash Table Filtering Invariant:**
  - **The Tokenization Principle:**
    - Punctuation characters must act strictly as word boundaries.
    - Any contiguous sequence of alphabetic characters $[a\text{–}z]$ constitutes an independent token.
  - **Banned Set Lookup ($B$):**
    - Convert $banned$ to a hash set $B$ for $\mathcal{O}(1)$ membership testing.
  - **Frequency Accumulation ($cnt$):**
    - For each extracted lowercase token $w$:
      - If $w \notin B$:
        $$
        cnt[w] \leftarrow cnt[w] + 1
        $$
    - Track the maximum frequency encountered:
      $$
      w^* = \arg\max_{w \notin B} cnt[w]
      $$
- **Step-by-Step Worked Execution Trace on the Ball Passage:**
  - Convert $banned$ to set:
    $$
    B = \{ \text{"hit"} \}
    $$
  - Initialize frequency map: $cnt = \{\}$.
  - **Token Stream Extraction & Frequency Counting:**
    1. `"Bob"` $\to$ `"bob"`: not in $B \implies cnt[\text{"bob"}] = 1$.
    2. `"hit"` $\to$ `"hit"`: in $B \implies \mathbf{Banned\ (Ignored).}$
    3. `"a"` $\to$ `"a"`: not in $B \implies cnt[\text{"a"}] = 1$.
    4. `"ball,"` $\to$ `"ball"`: not in $B \implies cnt[\text{"ball"}] = 1$.
    5. `"the"` $\to$ `"the"`: not in $B \implies cnt[\text{"the"}] = 1$.
    6. `"hit"` $\to$ `"hit"`: in $B \implies \mathbf{Banned\ (Ignored).}$
    7. `"BALL"` $\to$ `"ball"`: not in $B \implies cnt[\text{"ball"}] \leftarrow 1 + 1 = \mathbf{2}$.
    8. `"flew"` $\to$ `"flew"`: not in $B \implies cnt[\text{"flew"}] = 1$.
    9. `"far"` $\to$ `"far"`: not in $B \implies cnt[\text{"far"}] = 1$.
    10. `"after"` $\to$ `"after"`: not in $B \implies cnt[\text{"after"}] = 1$.
    11. `"it"` $\to$ `"it"`: not in $B \implies cnt[\text{"it"}] = 1$.
    12. `"was"` $\to$ `"was"`: not in $B \implies cnt[\text{"was"}] = 1$.
    13. `"hit."` $\to$ `"hit"`: in $B \implies \mathbf{Banned\ (Ignored).}$
  - **Frequency Table of Unbanned Tokens:**
    - `"ball"`: $2$
    - `"bob"`: $1$
    - `"a"`: $1$
    - `"the"`: $1$
    - `"flew"`: $1$
    - `"far"`: $1$
    - `"after"`: $1$
    - `"it"`: $1$
    - `"was"`: $1$
  - **Maximal Element Selection:**
    - Highest count is $2$, achieved by token $\mathbf{\text{"ball"}}$.
    - Output:
      $$
      ans = \mathbf{\text{"ball"}}
      $$
- **Punctuation-Separated Stream Trace ($paragraph = \text{"a, a, a, a, b,b,b,c, c"}, banned = [\text{"a"}]$):**
  - Consecutive commas and missing spaces between words (e.g. `"b,b,b"`) are split into independent tokens `"b"`, `"b"`, `"b"`.
  - `"a"` appears 4 times, but is banned.
  - `"b"` appears 3 times, unbanned $\implies$ Winner is $\mathbf{\text{"b"}}$.
- **Single Word Paragraph ($paragraph = \text{"Bob"}, banned = []$):**
  - Only token `"bob"`, frequency 1 $\implies \text{"bob"}$.

This instance demonstrates lexical analysis tokenization via regular language filtering and multiset mode extraction, mathematically proves why partitioning text into maximal alphabetic runs correctly handles arbitrary punctuation boundaries, and derives $O(L)$ runtime and $O(L)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a paragraph and a list of banned words:
Find the **most frequent unbanned word** (case-insensitive, returned in lowercase).

```text
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned    = [ "hit" ]

Tokens found:
  "hit"  -> count = 3 (BANNED!)
  "ball" -> count = 2 (UNBANNED -> Highest!)
  "bob", "a", "the", "flew", "far", "after", "it", "was" -> count = 1

Result: "ball"
```

### The Invariant of Lexical Token Filtering
- Punctuation marks must be treated as word boundaries.
- Convert all letters to lowercase.
- Count only words not present in the banned set.

---

## 2. Conceptual Foundation & Invariants

### 1. Alphabetical Lexing:
$$
\text{Tokens}(P) = \text{RegexSplit}(P.\text{lower}(), \; [a\text{–}z]^+)
$$

### 2. Argmax Over Unbanned Complement:
$$
ans = \arg\max_{w \in \text{Tokens}(P) \setminus B} \text{Freq}(w)
$$

> **Lexical Parsing Invariant.** The language $L = [a\text{–}z]^+$ over the alphabet $\Sigma$ decomposes any passage $P \in \Sigma^*$ into an alternating sequence of words and non-alphabetic separators. The frequency functional is invariant under delimiter substitution.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Normalize & Tokenize
- Lowercase: `"bob hit a ball the hit ball flew far after it was hit"`.

---

### Step 2: Filter & Count
- `"hit"` is in banned set $\implies$ skipped.
- `"ball"` appears 2 times.
- Other words appear 1 time each.

---

### Step 3: Find Maximum
- Maximum count among unbanned words is 2 $\implies$ `"ball"`.

---

### Step 4: Output
$$
\mathbf{\text{"ball"}}
$$

---

## 4. Complete Execution Trace

| Token Encountered | In Banned Set? | Previous Count | New Count | Current Leader |
|:---:|:---:|:---:|:---:|:---:|
| `"bob"` | No | $0$ | $1$ | `"bob"` ($1$) |
| `"hit"` | **Yes** | — | — | `"bob"` ($1$) |
| `"a"` | No | $0$ | $1$ | `"bob"` ($1$) |
| `"ball"` | No | $0$ | $1$ | `"ball"` ($1$) |
| `"the"` | No | $0$ | $1$ | `"ball"` ($1$) |
| `"hit"` | **Yes** | — | — | `"ball"` ($1$) |
| **`"ball"`** | **No** | **$1$** | **$2$** | **`"ball"` ($2$)** |
| `"flew" \dots` | No | $0$ | $1$ | `"ball"` ($2$) |

---

## 5. Boundary Cases & Failure Modes

- **Single Word:** Paragraph consists of only one word $\implies$ returns that word.
- **Punctuation Chains (`"b,b,b"`):** No spaces between commas; tokens extracted cleanly as separate words.
- **Mixed Case (`"BaLL"`, `"ball"`):** Case folding maps both to identical token `"ball"`.
- **Banned Words with Different Casing:** Banned words in input are lowercase; tokens are compared in lowercase.

---

## 6. Traps & Common Anti-Patterns

- **Splitting by Space Only (`paragraph.split(" ")`):** Fails on strings with commas or punctuation directly touching words (e.g. `"ball,"` becomes `"ball,"` which won't match `"ball"`). Regex `[a-z]+` or replacing punctuation with spaces is required.
- **Checking Banned in a List ($O(B)$ per word):** Using a list for banned words causes quadratic lookup time. A hash set `set(banned)` guarantees $O(1)$ lookup.
- **Returning Uppercase or Titlecase:** The problem explicitly demands the output in lowercase.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Converting paragraph to lowercase and regex extracting words: $\mathcal{O}(L)$ where $L$ is the length of `paragraph`.
  - Hash set creation for `banned`: $\mathcal{O}(B \cdot W)$.
  - Hash map frequency counting: $\mathcal{O}(L)$.
  - Total Time: strictly linear $\mathcal{O}(L + B \cdot W)$ where $L \le 1000$. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(L)$ memory to store the extracted tokens and frequency table.
