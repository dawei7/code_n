# Guided Example: Top K Frequent Words

We trace the step-by-step token frequency accumulation ($cnt[w]$), composite order key tuple evaluation ($(-cnt[w], \; w)$), frequency-descending primary sorting, lexicographical-ascending secondary tie-breaking, and top-$k$ prefix slice extraction on representative word corpora:

- **Input:** $words = [\text{"i"}, \; \text{"love"}, \; \text{"leetcode"}, \; \text{"i"}, \; \text{"love"}, \; \text{"coding"}], \quad k = 2$
- **Required output:** `["i", "love"]`
  - Problem objective:
    - Find the $k$ most frequent words in the input array.
    - Sorting criteria:
      1. Primary criterion: **Frequency descending** (higher frequency precedes lower frequency).
      2. Secondary criterion: **Lexicographical ascending** (in case of equal frequencies, words with lower alphabetical order precede words with higher alphabetical order).
    - For the input:
      - `"i"`: count 2
      - `"love"`: count 2
      - `"coding"`: count 1
      - `"leetcode"`: count 1
      - Both `"i"` and `"love"` have frequency 2. Alphabetically, `"i"` $<$ `"love"`.
      - The top 2 words are `["i", "love"]`.
- **Composite Key Ordering & Frequency Invariant:**
  - **The Dual-Criterion Sorting Key:**
    - To satisfy both requirements simultaneously, each unique word $w$ is associated with a comparison tuple:
      $$
      \text{Key}(w) = (-cnt[w], \; w)
      $$
    - In this tuple:
      - The primary component $-cnt[w]$ sorts counts in **strictly descending** order (larger counts become more negative, sorting earlier).
      - The secondary component $w$ sorts strings in **strictly ascending lexicographical** order.
  - **Top-$k$ Extraction:**
    - Sorting the unique vocabulary by $\text{Key}(w)$ arranges all words in perfect compliance with the problem constraints.
    - Taking the prefix slice of length $k$ yields the exact requested sequence:
      $$
      ans = \text{sorted}(\text{vocab}, \; \text{key}=\text{Key})[:k]
      $$
- **Step-by-Step Worked Execution Trace on $[\text{"i"}, \text{"love"}, \text{"leetcode"}, \text{"i"}, \text{"love"}, \text{"coding"}]$ with $k = 2$:**
  - **Step 1: Aggregate Word Frequencies:**
    - Token 0: `"i"` $\implies cnt[\text{"i"}] = 1$
    - Token 1: `"love"` $\implies cnt[\text{"love"}] = 1$
    - Token 2: `"leetcode"` $\implies cnt[\text{"leetcode"}] = 1$
    - Token 3: `"i"` $\implies cnt[\text{"i"}] = 2$
    - Token 4: `"love"` $\implies cnt[\text{"love"}] = 2$
    - Token 5: `"coding"` $\implies cnt[\text{"coding"}] = 1$
    - Resulting frequency dictionary:
      $$
      cnt = \{ \text{"i"}: 2, \; \text{"love"}: 2, \; \text{"leetcode"}: 1, \; \text{"coding"}: 1 \}
      $$
  - **Step 2: Construct Composite Comparison Keys:**
    - Word `"i"`:
      $$
      \text{Key}(\text{"i"}) = (-2, \; \text{"i"})
      $$
    - Word `"love"`:
      $$
      \text{Key}(\text{"love"}) = (-2, \; \text{"love"})
      $$
    - Word `"coding"`:
      $$
      \text{Key}(\text{"coding"}) = (-1, \; \text{"coding"})
      $$
    - Word `"leetcode"`:
      $$
      \text{Key}(\text{"leetcode"}) = (-1, \; \text{"leetcode"})
      $$
  - **Step 3: Total Order Sorting:**
    - Group by primary key $-cnt$:
      - Highest frequency group ($-2$): `{"i", "love"}`
        - Compare secondary strings: $\text{"i"} < \text{"love"}$
        - Sorted order: `["i", "love"]`
      - Lower frequency group ($-1$): `{"coding", "leetcode"}`
        - Compare secondary strings: $\text{"coding"} < \text{"leetcode"}$
        - Sorted order: `["coding", "leetcode"]`
    - Global sorted sequence:
      $$
      [\text{"i"}, \; \text{"love"}, \; \text{"coding"}, \; \text{"leetcode"}]
      $$
  - **Step 4: Extract Top $k = 2$ Elements:**
    - Slice the first $k = 2$ words from the sorted sequence:
      $$
      ans = [\text{"i"}, \; \text{"love"}]
      $$
    - Return **`["i", "love"]`**.
- **Four Ranked Words Trace ($words = [\text{"the"}, \text{"day"}, \text{"is"}, \text{"sunny"}, \text{"the"}, \text{"the"}, \text{"the"}, \text{"sunny"}, \text{"is"}, \text{"is"}], k = 4$):**
  - Frequencies:
    - `"the"`: 4
    - `"is"`: 3
    - `"sunny"`: 2
    - `"day"`: 1
  - Frequencies are all strictly distinct ($4 > 3 > 2 > 1$).
  - Top 4: `["the", "is", "sunny", "day"]`.
- **Complete Tie-Break Trace ($words = [\text{"b"}, \text{"a"}, \text{"c"}], k = 2$):**
  - All have frequency 1.
  - Sorted purely alphabetically: `["a", "b", "c"]`.
  - Top 2: `["a", "b"]`.

This instance demonstrates multiset frequency distribution analysis and lexicographical composite order ranking, mathematically proves why tuple negation linearizes descending-ascending lexicographical sorting, and derives $O(N \log U)$ runtime and $O(U)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of words:
Return the **$k$ most frequent words**.
Sort by:
1. Frequency descending (highest to lowest).
2. Lexicographical ascending on ties (alphabetical order).

```text
words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2

Frequencies:
  "i": 2
  "love": 2
  "leetcode": 1
  "coding": 1

Rankings:
  1. "i"    (count 2, alphabetically before "love")
  2. "love" (count 2)
  3. "coding" (count 1, alphabetically before "leetcode")
  4. "leetcode" (count 1)

Top 2 = [ "i", "love" ]
```

### The Invariant of the Composite Comparison Key
- Pairing the negated count with the word string $(-cnt[w], \; w)$ converts a two-dimensional sort into a single standard ascending comparison.
- Larger counts sort first because $-2 < -1$. Equal counts sort alphabetically because $"i" < "love"$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Tuple Key Function:
For each unique word $w$:
$$
\text{Key}(w) = (-cnt[w], \; w)
$$

### 2. Slicing Reduction:
$$
ans = \text{sorted}(\text{vocab}, \; \text{key}=\text{Key})[:k]
$$

> **Lexicographical Product Order Invariant.** The product poset $(\mathbb{Z}, \ge) \times (\Sigma^*, \le)$ admits a total linear order under lexicographical product comparison, isomorphic to the natural standard ordering of pairs $(-cnt, str)$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Count
- `"i"`: 2
- `"love"`: 2
- `"leetcode"`: 1
- `"coding"`: 1

---

### Step 2: Form Keys
- `"i"`: $(-2, \text{"i"})$.
- `"love"`: $(-2, \text{"love"})$.
- `"coding"`: $(-1, \text{"coding"})$.
- `"leetcode"`: $(-1, \text{"leetcode"})$.

---

### Step 3: Sort
- Rank 1: `"i"`
- Rank 2: `"love"`
- Rank 3: `"coding"`
- Rank 4: `"leetcode"`

---

### Step 4: Slice First $k = 2$
- **`["i", "love"]`**.

---

## 4. Complete Execution Trace

| Unique Word | Occurrence Count | Key Tuple $(-cnt, w)$ | Global Sort Rank | In Top $k = 2$? | Selected Output |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `"i"` | $2$ | $(-2, \text{"i"})$ | **Rank 1** | **Yes** | **`"i"`** |
| `"love"` | $2$ | $(-2, \text{"love"})$ | **Rank 2** | **Yes** | **`"love"`** |
| `"coding"` | $1$ | $(-1, \text{"coding"})$ | Rank 3 | No | — |
| `"leetcode"` | $1$ | $(-1, \text{"leetcode"})$ | Rank 4 | No | — |

---

## 5. Boundary Cases & Failure Modes

- **$k$ Equals Number of Unique Words:** Returns all unique words in sorted order.
- **All Words Have Count 1:** Pure alphabetical sort of unique words.
- **Single Unique Word Repeated $N$ Times:** Returns that word in a 1-element list.
- **Long Strings ($L = 100$):** Lexicographical string comparison handles arbitrary lengths.

---

## 6. Traps & Common Anti-Patterns

- **Sorting by Count Only:** Forgetting to break ties alphabetically returns arbitrary orderings (e.g. `["love", "i"]` instead of `["i", "love"]`).
- **Inverted Tie-Breaker:** Using a max-heap where both count and string are inverted causes words with equal frequency to sort in reverse alphabetical order.
- **Sorting the Entire Input Array ($O(N \log N)$):** Counting first with a hash map and sorting only the unique vocabulary $U$ ($U \le N$) reduces sorting time to $\mathcal{O}(U \log U)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Counting word frequencies: $\mathcal{O}(N \cdot L)$ where $N$ is words and $L$ is max string length.
  - Sorting $U$ unique words: $\mathcal{O}(U \log U \cdot L)$.
  - Total Time: $\mathcal{O}(N \cdot L + U \log U \cdot L)$. Completes in $< 2$ ms for $N = 500$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(U \cdot L)$ space to store the frequency map and vocabulary list.
