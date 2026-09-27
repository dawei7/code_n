# Guided Example: Find and Replace Pattern

We trace the step-by-step character bijection verification, bidirectional projection mapping ($s \leftrightarrow t$), last-seen position timestamp invariance, canonical signature normalization, and isomorphic string filtering on representative word dictionaries:

- **Input:**
  $$
  words = [\text{"abc"}, \text{"deq"}, \text{"mee"}, \text{"aqq"}, \text{"dkd"}, \text{"ccc"}], \quad pattern = \text{"abb"}
  $$
- **Required output:** `["mee", "aqq"]`
  - Pattern matching rules:
    - A word matches $pattern$ if there exists a **bijection** (a one-to-one and onto permutation) between the characters of $pattern$ and the characters of $word$.
    - Conditions for bijection:
      1. Every character in $pattern$ maps to exactly one character in $word$.
      2. No two distinct characters in $pattern$ map to the same character in $word$.
    - For $pattern = \text{"abb"}$:
      - Character structure: First letter is unique, followed by two identical letters ($x y y$ with $x \ne y$).
      - Testing candidates:
        - `"abc"`: letters are all distinct ($x y z$) $\implies$ Mismatch.
        - `"deq"`: letters are all distinct ($x y z$) $\implies$ Mismatch.
        - `"mee"`: $m \to a, e \to b$ ($x y y$) $\implies$ **Match!**
        - `"aqq"`: $a \to a, q \to b$ ($x y y$) $\implies$ **Match!**
        - `"dkd"`: first and third letters match ($x y x$) $\implies$ Mismatch.
        - `"ccc"`: all three letters are identical ($x x x$) $\implies$ Mismatch (violates one-to-one mapping because $a \to c$ and $b \to c$).
      - Result: **`["mee", "aqq"]`**.
- **The Bijection & Last-Seen Timestamp Invariant:**
  - **The Bi-directional Mapping Trap:**
    - Mapping in only one direction ($a \to b$) is insufficient.
    - Example: With $pattern = \text{"abb"}$ and $word = \text{"ccc"}$, a forward map $a \to c, b \to c$ is a valid function, but it fails injectivity because both $a$ and $b$ collapse to $c$.
    - A valid isomorphism requires an invertible mapping.
  - **Last-Seen Index Equivalence:**
    - Two strings $s$ and $t$ of equal length are isomorphic if and only if **for every index $i$, the last position where character $s[i]$ occurred is identical to the last position where character $t[i]$ occurred**!
    - Let $m_1[c]$ store the 1-based last seen index of character $c$ in string $s$.
    - Let $m_2[c]$ store the 1-based last seen index of character $c$ in string $t$.
    - At index $i$ (with $a = s[i]$ and $b = t[i]$):
      $$
      \text{If } m_1[a] \ne m_2[b] \implies \mathbf{Isomorphism\ Violated!}
      $$
      $$
      \text{Otherwise, update } m_1[a] \leftarrow i \quad \text{and} \quad m_2[b] \leftarrow i
      $$
    - If all characters satisfy this equality, the two strings share the exact same structural pattern.

---

## 1. Instance & Teaching Goal

Given $pattern = \text{"abb"}$, test candidate words and isolate the isomorphic matches.

```text
Pattern "abb":
  Index 1: 'a' (first appearance -> ID 0)
  Index 2: 'b' (first appearance -> ID 1)
  Index 3: 'b' (second appearance -> ID 1)
  Canonical Signature: [0, 1, 1]

Candidate "mee":
  'm' -> ID 0
  'e' -> ID 1
  'e' -> ID 1
  Signature: [0, 1, 1]  == [0, 1, 1] -> MATCH!

Candidate "ccc":
  'c' -> ID 0
  'c' -> ID 0
  'c' -> ID 0
  Signature: [0, 0, 0]  != [0, 1, 1] -> REJECT!
```

The teaching goal is to demonstrate how synchronizing last-seen history vectors checks injectivity and surjectivity in a single pass.

---

## 2. Conceptual Foundation & Invariants

### 1. Isomorphism Invariant:
For strings $s$ and $t$ of length $L$:
$$
s[i] == s[j] \iff t[i] == t[j] \quad \forall 0 \le i, j < L
$$

### 2. Timestamp State Check:
Let arrays $m_1, m_2$ of size $128$ be initialized to $0$.
For $i = 1 \dots L$:
$$
\text{match}(s, t) \iff \bigwedge_{i=1}^L \left( m_1[s[i]] == m_2[t[i]] \right)
$$
where each step sets $m_1[s[i]] = m_2[t[i]] = i$.

---

## 3. Step-by-Step Worked Execution

We test candidate words against $pattern = \text{"abb"}$:

---

### Step 1: Testing `"mee"` against `"abb"`
- Initialize $m_1, m_2$ to all zeros.
- **Index $i = 1$ ($a = \text{'m'}, b = \text{'a'}$):**
  - $m_1[\text{'m'}] = 0, \; m_2[\text{'a'}] = 0$.
  - Equal ($0 == 0$) $\implies$ assign $m_1[\text{'m'}] = 1, \; m_2[\text{'a'}] = 1$.
- **Index $i = 2$ ($a = \text{'e'}, b = \text{'b'}$):**
  - $m_1[\text{'e'}] = 0, \; m_2[\text{'b'}] = 0$.
  - Equal ($0 == 0$) $\implies$ assign $m_1[\text{'e'}] = 2, \; m_2[\text{'b'}] = 2$.
- **Index $i = 3$ ($a = \text{'e'}, b = \text{'b'}$):**
  - $m_1[\text{'e'}] = 2, \; m_2[\text{'b'}] = 2$.
  - Equal ($2 == 2$) $\implies$ assign $m_1[\text{'e'}] = 3, \; m_2[\text{'b'}] = 3$.
- All positions match! **`"mee"` is a valid match.**

---

### Step 2: Testing `"ccc"` against `"abb"`
- Initialize $m_1, m_2$ to all zeros.
- **Index $i = 1$ ($a = \text{'c'}, b = \text{'a'}$):**
  - $m_1[\text{'c'}] = 0, \; m_2[\text{'a'}] = 0 \implies m_1[\text{'c'}] = 1, \; m_2[\text{'a'}] = 1$.
- **Index $i = 2$ ($a = \text{'c'}, b = \text{'b'}$):**
  - $m_1[\text{'c'}] = 1$ (seen at index 1).
  - $m_2[\text{'b'}] = 0$ (never seen).
  - Condition $m_1[\text{'c'}] == m_2[\text{'b'}]$ **fails ($1 \ne 0$)**!
  - **`"ccc"` is rejected.**

---

### Step 3: Testing `"dkd"` against `"abb"`
- **Index $i = 3$ ($a = \text{'d'}, b = \text{'b'}$):**
  - In `"dkd"`, `'d'` was seen at index 1 $\implies m_1[\text{'d'}] = 1$.
  - In `"abb"`, `'b'` was seen at index 2 $\implies m_2[\text{'b'}] = 2$.
  - $1 \ne 2 \implies$ **`"dkd"` is rejected.**

---

### Step 4: Testing Remaining Words
- `"abc"`: index 3 sees $m_1[\text{'c'}] = 0 \ne m_2[\text{'b'}] = 2 \implies$ Rejected.
- `"deq"`: index 3 sees $m_1[\text{'q'}] = 0 \ne m_2[\text{'b'}] = 2 \implies$ Rejected.
- `"aqq"`: identically matches timestamps $[0, 0] \to [0, 0] \to [2, 2] \implies$ **Accepted!**

Matching words collected: `["mee", "aqq"]`.

---

## 4. Complete Execution Trace

| Word Tested | Target Pattern | Pos 1 ($s[1], t[1]$) | Pos 2 ($s[2], t[2]$) | Pos 3 ($s[3], t[3]$) | Structural Equivalence | Verdict |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `"abc"` | `"abb"` | `'a', 'a'` ($0=0$) | `'b', 'b'` ($0=0$) | `'c', 'b'` ($0 \ne 2$) | 3rd letter not repeated | Rejected |
| `"deq"` | `"abb"` | `'d', 'a'` ($0=0$) | `'e', 'b'` ($0=0$) | `'q', 'b'` ($0 \ne 2$) | 3rd letter not repeated | Rejected |
| **`"mee"`** | **`"abb"`** | **`'m', 'a'` ($0=0$)** | **`'e', 'b'` ($0=0$)** | **`'e', 'b'` ($2=2$)** | **$x y y$ pattern preserved** | **`Accepted`** |
| **`"aqq"`** | **`"abb"`** | **`'a', 'a'` ($0=0$)** | **`'q', 'b'` ($0=0$)** | **`'q', 'b'` ($2=2$)** | **$x y y$ pattern preserved** | **`Accepted`** |
| `"dkd"` | `"abb"` | `'d', 'a'` ($0=0$) | `'k', 'b'` ($0=0$) | `'d', 'b'` ($1 \ne 2$) | Repeats 1st letter instead of 2nd | Rejected |
| `"ccc"` | `"abb"` | `'c', 'a'` ($0=0$) | `'c', 'b'` ($1 \ne 0$) | — | Non-injective ($a, b \to c$) | Rejected |

---

## 5. Boundary Cases & Failure Modes

- **Single-Letter Words ($pattern = \text{"a"}, words = [\text{"a"}, \text{"b"}, \text{"c"}]$):** Any single letter trivially maps injectively to any other single letter $\implies$ all match.
- **Words of Different Lengths:** The problem guarantees all candidate words have the same length as $pattern$.
- **All Distinct Letters ($pattern = \text{"abcdef"}$):** A candidate matches if and only if all its letters are mutually distinct.

---

## 6. Traps & Common Anti-Patterns

- **One-Way Mapping Table:** Using a single map $pattern \to word$ accepts `"ccc"` for `"abb"` because $a \to c$ and $b \to c$ can be stored without detecting collision. Checking both directions or using a last-seen timestamp array prevents false positives.
- **String Replacement Side Effects:** Iterating through letters and performing `word.replace(x, y)` can replace already converted letters, destroying the original structure.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of words, and $L$ be the length of each word.
  - For each word, matching takes $L$ steps.
  - Each step accesses fixed arrays $m_1, m_2$ of size $128$ in $\mathcal{O}(1)$ time.
  - Total Time: $\mathcal{O}(N \cdot L)$, running in $< 2$ ms for $N \le 50, L \le 20$.
- **Auxiliary Space Complexity:**
  - Static integer tables of size $128$: strictly $\mathcal{O}(1)$ additional memory beyond output storage.
