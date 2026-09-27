# Guided Example: Keyboard Row

We trace the step-by-step standard American QWERTY keyboard partitioning, character case normalization ($w \to \text{lower}(w)$), character set projection ($s = \text{set}(w)$), subset inclusion testing ($s \subseteq R_1 \lor s \subseteq R_2 \lor s \subseteq R_3$), and original casing preservation on representative word vocabularies:

- **Input:** $words = [\text{"Hello"}, \text{"Alaska"}, \text{"Dad"}, \text{"Peace"}]$
- **Required output:** `["Alaska", "Dad"]`
  - Keyboard row character sets:
    - Row 1: $R_1 = \{q, w, e, r, t, y, u, i, o, p\}$
    - Row 2: $R_2 = \{a, s, d, f, g, h, j, k, l\}$
    - Row 3: $R_3 = \{z, x, c, v, b, n, m\}$
  - Requirement: A word is valid if and only if all of its letters reside entirely within a single keyboard row.
- **Word-by-word set membership execution trace:**
  - **Word 1: `"Hello"`**
    - Convert to lowercase: `"hello"`
    - Unique character set: $s = \{h, e, l, o\}$
    - Test row inclusion:
      - $e, o \in R_1$, but $h, l \notin R_1 \implies s \not\subseteq R_1$
      - $h, l \in R_2$, but $e, o \notin R_2 \implies s \not\subseteq R_2$
      - $s \not\subseteq R_3$
    - Letters span multiple rows $\implies$ **Rejected**.
  - **Word 2: `"Alaska"`**
    - Convert to lowercase: `"alaska"`
    - Unique character set: $s = \{a, l, s, k\}$
    - Test row inclusion:
      - $a \in R_2$
      - $l \in R_2$
      - $s \in R_2$
      - $k \in R_2$
      - $s \subseteq R_2$ (**True!**)
    - All letters belong exclusively to Row 2 $\implies$ **Accepted**! Add original `"Alaska"` to answer.
  - **Word 3: `"Dad"`**
    - Convert to lowercase: `"dad"`
    - Unique character set: $s = \{d, a\}$
    - Test row inclusion:
      - $d \in R_2, \; a \in R_2 \implies s \subseteq R_2$ (**True!**)
    - Exclusively Row 2 $\implies$ **Accepted**! Add original `"Dad"` to answer.
  - **Word 4: `"Peace"`**
    - Convert to lowercase: `"peace"`
    - Unique character set: $s = \{p, e, a, c\}$
    - Row distribution:
      - $p, e \in R_1$
      - $a \in R_2$
      - $c \in R_3$
    - Letters span all 3 rows $\implies$ **Rejected**.
  - Final filtered list: **`["Alaska", "Dad"]`**.
- **Row 1 Instance:** $words = [\text{"Typewriter"}] \implies \{t, y, p, e, w, r, i\} \subseteq R_1 \implies \mathbf{[\text{"Typewriter"}]}$
- **Row 3 Instance:** $words = [\text{"zxcv"}] \implies \mathbf{[\text{"zxcv"}]}$
- **Empty Filter Result:** $words = [\text{"omk"}] \implies o \in R_1, m \in R_3, k \in R_2 \implies \mathbf{[]}$

This instance demonstrates set-theoretic partition verification, mathematically proves why subset inclusion guarantees row exclusivity, and derives $O(\sum |word|)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of strings $words$:
Return the words that can be typed using letters of **only one row** of an American QWERTY keyboard.
Case is ignored during comparison, but the original casing must be preserved in the output.

```text
American QWERTY Keyboard Rows:
  Row 1:  Q  W  E  R  T  Y  U  I  O  P
  Row 2:   A  S  D  F  G  H  J  K  L
  Row 3:    Z  X  C  V  B  N  M

Evaluating "Alaska":
  'A' -> Row 2
  'l' -> Row 2
  'a' -> Row 2
  's' -> Row 2
  'k' -> Row 2
  'a' -> Row 2
All characters belong to Row 2 -> Keep "Alaska"!
```

### Set-Theoretic Formulation
Let the alphabet be partitioned into three disjoint sets:
$$
\begin{aligned}
R_1 &= \{\text{'q'}, \text{'w'}, \text{'e'}, \text{'r'}, \text{'t'}, \text{'y'}, \text{'u'}, \text{'i'}, \text{'o'}, \text{'p'}\} \\
R_2 &= \{\text{'a'}, \text{'s'}, \text{'d'}, \text{'f'}, \text{'g'}, \text{'h'}, \text{'j'}, \text{'k'}, \text{'l'}\} \\
R_3 &= \{\text{'z'}, \text{'x'}, \text{'c'}, \text{'v'}, \text{'b'}, \text{'n'}, \text{'m'}\}
\end{aligned}
$$
For any word $w$:
Let $s = \text{set}(w.\text{lower}())$ be the set of unique lowercase characters in $w$.
The word $w$ is valid if and only if:
$$
s \subseteq R_1 \quad \lor \quad s \subseteq R_2 \quad \lor \quad s \subseteq R_3
$$

---

## 2. Conceptual Foundation & Invariants

### 1. Set Membership Test:
In Python or set algebra:
- $s \le R$ evaluates whether $s$ is a subset of $R$ ($s \subseteq R$).
- Since $|s| \le 26$, subset evaluation takes at most 26 hash set lookups, executing in $O(|w|)$ time.

### 2. Case Insensitivity Preservation:
Converting $w$ to lowercase $w.\text{lower}()$ normalizes character comparisons while preserving the original string $w$ for output appending.

> **Single Row Invariant.** A word $w$ belongs to a single keyboard row if and only if the intersection of its character set with two of the three keyboard rows is completely empty.

---

## 3. Step-by-Step Worked Execution

We trace $words = [\text{"Hello"}, \text{"Alaska"}, \text{"Dad"}, \text{"Peace"}]$:

---

### Step 1: Precompute Row Sets
- $R_1 = \text{set}(\text{"qwertyuiop"})$
- $R_2 = \text{set}(\text{"asdfghjkl"})$
- $R_3 = \text{set}(\text{"zxcvbnm"})$

---

### Step 2: Test Each Word

1. **Word `"Hello"`:**
   - Lowercase set: $s = \{\text{'h'}, \text{'e'}, \text{'l'}, \text{'o'}\}$.
   - Check $s \subseteq R_1$: False ($h, l \notin R_1$).
   - Check $s \subseteq R_2$: False ($e, o \notin R_2$).
   - Check $s \subseteq R_3$: False.
   - Word rejected.

2. **Word `"Alaska"`:**
   - Lowercase set: $s = \{\text{'a'}, \text{'l'}, \text{'s'}, \text{'k'}\}$.
   - Check $s \subseteq R_1$: False.
   - Check $s \subseteq R_2$:
     - $\text{'a'} \in R_2$
     - $\text{'l'} \in R_2$
     - $\text{'s'} \in R_2$
     - $\text{'k'} \in R_2$
     - $s \subseteq R_2$ is **True**!
   - Word accepted: append `"Alaska"` to answer.

3. **Word `"Dad"`:**
   - Lowercase set: $s = \{\text{'d'}, \text{'a'}\}$.
   - Check $s \subseteq R_2$: True ($d \in R_2, a \in R_2$).
   - Word accepted: append `"Dad"` to answer.

4. **Word `"Peace"`:**
   - Lowercase set: $s = \{\text{'p'}, \text{'e'}, \text{'a'}, \text{'c'}\}$.
   - $p, e \in R_1$, $a \in R_2$, $c \in R_3$.
   - Fails all subset checks. Rejected.

---

### Step 3: Final Output
$$
ans = \mathbf{[\text{"Alaska"}, \text{"Dad"}]}
$$

---

## 4. Complete Execution Trace

| Word $w$ | Lowercase Character Set $s$ | $s \subseteq R_1$? | $s \subseteq R_2$? | $s \subseteq R_3$? | Single Row? | Action Taken |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| `"Hello"` | $\{h, e, l, o\}$ | No | No | No | No | Discard |
| **`"Alaska"`** | $\{a, l, s, k\}$ | No | **Yes** | No | **Yes** | **Append `"Alaska"`** |
| **`"Dad"`** | $\{d, a\}$ | No | **Yes** | No | **Yes** | **Append `"Dad"`** |
| `"Peace"` | $\{p, e, a, c\}$ | No | No | No | No | Discard |

---

## 5. Boundary Cases & Failure Modes

- **Single Letter Words (`"a"`, `"A"`, `"z"`):** A single letter always belongs to exactly one row $\implies$ unconditionally accepted.
- **Words Spanning All 3 Rows (`"peace"`):** Fails all rows $\implies$ rejected.
- **No Qualifying Words ($[\text{"omk"}]$):** Returns empty list `[]`.
- **Duplicate Characters in Word (`"Dad"`):** Set deduplicates characters to $\{d, a\}$, correctly validating each unique letter once.

---

## 6. Traps & Common Anti-Patterns

- **Modifying the Original Word:** Converting the input word to lowercase in place (`w = w.lower()`) corrupts the original capitalization. The output must preserve the user's exact original casing.
- **Mapping Characters with Multiple If-Else Chains:** Writing individual checks for each character requires dozens of lines. Predefining three constant sets $R_1, R_2, R_3$ and checking set inclusion `s <= s2` is concise and error-free.
- **Hardcoding ASCII Values Instead of Sets:** Checking character ranges via ASCII values is error-prone because keyboard rows do not follow alphabetical ASCII order.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $L = \sum |w_i|$ be the total number of characters across all words.
  - Converting each word to lowercase and extracting its character set takes $O(|w_i|)$ time.
  - Subset comparison of a set with at most 26 elements against three fixed sets takes $O(|w_i|)$ time.
  - Total Time: $\mathcal{O}(L)$. For 1000 words of length 10, executes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space beyond storing the answer array (keyboard sets take $26$ bytes).
