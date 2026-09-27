# Guided Example: Count Unique Characters of All Substrings of a Given String

We trace the step-by-step indicator variable linearity of expectation transformation, character occurrence indexing ($d[c] = [p_0, p_1, \dots]$), bounding interval left/right span decomposition ($(i - prev) \times (next - i)$), duplicate character suppression, and total unique character frequency contribution summation on representative strings:

- **Input:**
  $$
  s = \text{"ABA"}
  $$
- **Required output:** `8`
  - Substring unique character definitions:
    - For any substring $t$, $\text{countUniqueChars}(t)$ is the number of characters that appear **exactly once** in $t$.
    - Objective: Find the sum of $\text{countUniqueChars}(t)$ over all substrings $t$.
    - For $s = \text{"ABA"}$ ($n = 3$), all 6 substrings:
      - Length 1:
        - `"A"` (index $[0..0]$): unique char `'A'` $\implies 1$
        - `"B"` (index $[1..1]$): unique char `'B'` $\implies 1$
        - `"A"` (index $[2..2]$): unique char `'A'` $\implies 1$
      - Length 2:
        - `"AB"` (index $[0..1]$): unique chars `'A'`, `'B'` $\implies 2$
        - `"BA"` (index $[1..2]$): unique chars `'B'`, `'A'` $\implies 2$
      - Length 3:
        - `"ABA"` (index $[0..2]$): `'A'` appears twice (not unique!), only `'B'` is unique $\implies 1$
      - Total sum:
        $$
        1 + 1 + 1 + 2 + 2 + 1 = \mathbf{8}
        $$
- **Contribution Method & Interval Product Invariant:**
  - **The Principle of Double Counting:**
    - Rather than iterating over all $\mathcal{O}(N^2)$ substrings and counting unique characters in each, invert the perspective!
    - Count **in how many substrings each character instance $s[i]$ appears as a unique character**.
    - Summing this count over all character instances $i \in [0, n - 1]$ gives the exact total!
  - **Left and Right Boundary Invariant:**
    - Consider character $s[i]$. For $s[i]$ to be unique in a substring $s[L \dots R]$:
      1. The substring must include index $i$: $L \le i \le R$.
      2. The substring must NOT contain any other occurrence of the same character.
    - Let $prev$ be the previous index where character $s[i]$ appears (or $-1$ if none).
    - Let $next$ be the next index where character $s[i]$ appears (or $n$ if none).
    - The start index $L$ can be chosen from any position in $(prev, i]$:
      $$
      \text{number of choices for } L = i - prev
      $$
    - The end index $R$ can be chosen from any position in $[i, next)$:
      $$
      \text{number of choices for } R = next - i
      $$
    - By the multiplication principle, the total number of substrings where $s[i]$ is unique is:
      $$
      \text{Contribution}(i) = (i - prev) \times (next - i)
      $$
- **Step-by-Step Worked Execution Trace on $s = \text{"ABA"}$ ($n = 3$):**
  - Group indices by character:
    - Character `'A'`: indices $[0, 2]$
    - Character `'B'`: indices $[1]$
  - Initialize total sum: $ans = 0$.
  - **Evaluate Character `'A'` (Occurrences at indices $0$ and $2$):**
    - Virtual boundaries: $v = [-1, \; 0, \; 2, \; 3]$.
    - **Instance 1 (Index $0$):**
      - $prev = -1$, current $i = 0$, $next = 2$.
      - $L$ choices in $(-1, 0]$: index $0$ ($0 - (-1) = \mathbf{1}$ choice).
      - $R$ choices in $[0, 2)$: indices $0, 1$ ($2 - 0 = \mathbf{2}$ choices).
      - Valid substrings: `"A"` ($[0..0]$) and `"AB"` ($[0..1]$).
      - Contribution:
        $$
        (0 - (-1)) \times (2 - 0) = 1 \times 2 = \mathbf{2}
        $$
    - **Instance 2 (Index $2$):**
      - $prev = 0$, current $i = 2$, $next = 3$.
      - $L$ choices in $(0, 2]$: indices $1, 2$ ($2 - 0 = \mathbf{2}$ choices).
      - $R$ choices in $[2, 3)$: index $2$ ($3 - 2 = \mathbf{1}$ choice).
      - Valid substrings: `"BA"` ($[1..2]$) and `"A"` ($[2..2]$).
      - Contribution:
        $$
        (2 - 0) \times (3 - 2) = 2 \times 1 = \mathbf{2}
        $$
    - Total contribution of character `'A'`: $2 + 2 = \mathbf{4}$.
  - **Evaluate Character `'B'` (Occurrence at index $1$):**
    - Virtual boundaries: $v = [-1, \; 1, \; 3]$.
    - **Instance 1 (Index $1$):**
      - $prev = -1$, current $i = 1$, $next = 3$.
      - $L$ choices in $(-1, 1]$: indices $0, 1$ ($1 - (-1) = \mathbf{2}$ choices).
      - $R$ choices in $[1, 3)$: indices $1, 2$ ($3 - 1 = \mathbf{2}$ choices).
      - Valid substrings: `"B"` ($[1..1]$), `"AB"` ($[0..1]$), `"BA"` ($[1..2]$), and `"ABA"` ($[0..2]$).
      - Contribution:
        $$
        (1 - (-1)) \times (3 - 1) = 2 \times 2 = \mathbf{4}
        $$
    - Total contribution of character `'B'`: $\mathbf{4}$.
  - **Total Summation:**
    $$
    ans = \text{Contrib}('A') + \text{Contrib}('B') = 4 + 4 = \mathbf{8}
    $$
- **All Distinct Characters Trace ($s = \text{"ABC"}$):**
  - $n = 3$. Every character appears only once.
  - Index 0 ('A'): $(0 - (-1)) \times (3 - 0) = 1 \times 3 = 3$.
  - Index 1 ('B'): $(1 - (-1)) \times (3 - 1) = 2 \times 2 = 4$.
  - Index 2 ('C'): $(2 - (-1)) \times (3 - 2) = 3 \times 1 = 3$.
  - Total: $3 + 4 + 3 = \mathbf{10}$.
- **All Identical Characters Trace ($s = \text{"AAA"}$):**
  - Index 0: $(0 - (-1)) \times (1 - 0) = 1 \times 1 = 1$.
  - Index 1: $(1 - 0) \times (2 - 1) = 1 \times 1 = 1$.
  - Index 2: $(2 - 1) \times (3 - 2) = 1 \times 1 = 1$.
  - Total: $1 + 1 + 1 = \mathbf{3}$ (only the 3 singleton substrings have a unique 'A'!).

This instance demonstrates indicator variable decomposition on finite string topologies and combinatorics on word factor spans, mathematically proves why Fubini's summation interchange reduces quadratic substring traversal to linear interval measure products, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given string $s$:
Find the sum of unique character counts across **all substrings**.

```text
s = "ABA"

All substrings:
  "A"   -> unique = 1
  "B"   -> unique = 1
  "A"   -> unique = 1
  "AB"  -> unique = 2
  "BA"  -> unique = 2
  "ABA" -> unique = 1 ('A' repeated, only 'B' is unique)

Total sum = 1 + 1 + 1 + 2 + 2 + 1 = 8
Result: 8
```

### The Invariant of Character Contribution
- Instead of counting characters per substring, count **substrings per character**.
- Character at index $i$ is unique in all substrings $[L \dots R]$ where:
  - $L$ is between previous occurrence of $s[i]$ and $i$.
  - $R$ is between $i$ and next occurrence of $s[i]$.
- Total substrings $= (i - prev) \times (next - i)$.

---

## 2. Conceptual Foundation & Invariants

### 1. Linearity of Indicators:
$$
\sum_{t \subseteq s} \text{countUnique}(t) = \sum_{i = 0}^{n - 1} \sum_{0 \le L \le i \le R < n} \mathbb{I}[s[i] \text{ is unique in } s[L..R]]
$$

### 2. Factor Formula:
For character instance $s[i]$ with predecessor $p$ and successor $q$:
$$
\text{Contrib}(i) = (i - p) \times (q - i), \quad \text{where } p = \max(\{j < i \mid s[j] = s[i]\} \cup \{-1\})
$$
$$
q = \min(\{j > i \mid s[j] = s[i]\} \cup \{n\})
$$
$$
ans = \sum_{c \in \Sigma} \sum_{k = 1}^{|v_c| - 2} (v_c[k] - v_c[k - 1]) \times (v_c[k + 1] - v_c[k])
$$

> **Fubini Inversion Invariant.** The double summation over substrings and alphabet elements $\sum_{L \le R} \sum_{c} \mathbb{I}$ exchanges order unconditionally. For each occurrence $i$, the support of the indicator is the product interval $(p, i] \times [i, q)$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"ABA"}$:

---

### Step 1: Index Locations
- 'A': $[-1, 0, 2, 3]$.
- 'B': $[-1, 1, 3]$.

---

### Step 2: 'A' at Index 0
- $(0 - (-1)) \times (2 - 0) = 1 \times 2 = \mathbf{2}$.

---

### Step 3: 'A' at Index 2
- $(2 - 0) \times (3 - 2) = 2 \times 1 = \mathbf{2}$.

---

### Step 4: 'B' at Index 1
- $(1 - (-1)) \times (3 - 1) = 2 \times 2 = \mathbf{4}$.

---

### Step 5: Output
- $2 + 2 + 4 = \mathbf{8}$.

---

## 4. Complete Execution Trace

| Character Instance $s[i]$ | Predecessor Index $prev$ | Successor Index $next$ | Left Span ($i - prev$) | Right Span ($next - i$) | Substrings Where Unique |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $s[0] = \text{'A'}$ | $-1$ | $2$ | $1$ | $2$ | $1 \times 2 = 2$ |
| $s[1] = \text{'B'}$ | $-1$ | $3$ | $2$ | $2$ | $2 \times 2 = 4$ |
| **$s[2] = \text{'A'}$** | **$0$** | **$3$** | **$2$** | **$1$** | **$2 \times 1 = 2$** |
| **Total Sum** | — | — | — | — | **`8`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Character ($"A"$):** $(0 - (-1)) \times (1 - 0) = 1 \times 1 = 1$.
- **All Distinct ($"ABCDE"$):** Each character contributes $(i + 1) \times (n - i)$.
- **All Identical ($"AAAA"$):** Each character contributes $(1) \times (1) = 1 \implies$ total $n$.
- **Large String ($N = 10^5$):** Linear pass completes in $< 10$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Generating All Substrings ($O(N^3)$):** Checking uniqueness across all substrings creates cubic complexity and immediate TLE. Contribution counting is strictly $O(N)$.
- **Double-Counting Repeats:** If a character appears twice in a substring, NEITHER instance contributes to the sum. The condition $(next - i)$ strictly excludes substrings reaching the second occurrence.
- **Off-By-One on Sentinel Boundaries:** Always pad the index lists with $-1$ at the beginning and $n$ at the end.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass to group indices by character: $\mathcal{O}(N)$.
  - Iterating through each index list: sum of list lengths is $N + 2 \times |\Sigma|$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 10^5$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory to store the index lists for the 26 English letters.