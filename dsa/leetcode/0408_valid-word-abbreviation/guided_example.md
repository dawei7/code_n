# Guided Example: Valid Word Abbreviation

We trace the step-by-step two-pointer parsing, multi-digit skip accumulation ($x \leftarrow x \times 10 + \text{digit}$), strict leading zero rejection (`abbr[j] == '0' and x == 0`), word index jumping ($i \leftarrow i + x$), letter equality verification ($word[i] == abbr[j]$), and terminal boundary alignment ($i + x == m \land j == n$) on representative string instances:

- **Input:** $word = \text{"internationalization"}, \quad abbr = \text{"i12iz4n"}$
- **Required output:** `true`
  - Total lengths: $m = 20, n = 7$
  - Step-by-step pointer progression:
    - Step 1 ($j = 0, c = \text{'i'}$): Match letter $word[0] == \text{'i'}$, advance $i \leftarrow 1$
    - Step 2 ($j = 1, 2, c = \text{'1'}, \text{'2'}$): Parse number $x = 12$
    - Step 3 ($j = 3, c = \text{'i'}$): Skip $x = 12 \implies i \leftarrow 1 + 12 = 13$, match $word[13] == \text{'i'}$, advance $i \leftarrow 14$
    - Step 4 ($j = 4, c = \text{'z'}$): Match letter $word[14] == \text{'z'}$, advance $i \leftarrow 15$
    - Step 5 ($j = 5, c = \text{'4'}$): Parse number $x = 4$
    - Step 6 ($j = 6, c = \text{'n'}$): Skip $x = 4 \implies i \leftarrow 15 + 4 = 19$, match $word[19] == \text{'n'}$, advance $i \leftarrow 20$
  - End of abbreviation ($j = 7$): $i + x = 20 + 0 = 20 == m \implies$ Return `true`
- **Leading Zero Rejection:** $word = \text{"internationalization"}, abbr = \text{"i012iz4n"} \implies$ rejects on `'0'` $\implies \text{false}$
- **Character Mismatch:** $word = \text{"apple"}, abbr = \text{"a2e"} \implies$ skips 2 to index 3 (`'l'`), mismatches `'e'` $\implies \text{false}$
- **Boundary Overshoot:** $word = \text{"hi"}, abbr = \text{"10"} \implies$ skip $10 > 2 \implies \text{false}$

This instance demonstrates linear string parsing with run-length jump decoding, mathematically proves why prohibiting leading zeros guarantees a unique canonical representation for any valid abbreviation, and achieves $O(|word| + |abbr|)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $word = \text{"internationalization"}$ ($m = 20$) and an abbreviation $abbr = \text{"i12iz4n"}$ ($n = 7$):
Determine whether $abbr$ is a valid abbreviation of $word$:

```text
Word:         i  n t e r n a t i o n a l  i  z  a t i o  n
Indices:      0  1                     12 13 14 15    18 19
Abbreviation: i  [------- 12 --------]   i  z  [-- 4 -]  n

Alignment:
  Index 0:      'i' == 'i'  (Match)
  Indices 1-12: 12 characters skipped
  Index 13:     'i' == 'i'  (Match)
  Index 14:     'z' == 'z'  (Match)
  Indices 15-18: 4 characters skipped
  Index 19:     'n' == 'n'  (Match)

All 20 characters accounted for -> Valid -> true
```

### The Grammar Rules of Abbreviations
1. **Replacement:** Any non-empty substring of length $k$ can be replaced by the decimal number $k$.
2. **Non-Adjacent:** Two replaced substrings cannot be adjacent (they must merge into a single combined count).
3. **No Leading Zeros:** A replacement number cannot start with `'0'` (e.g. `"01"` and `"0"` are invalid).

---

## 2. Conceptual Foundation & Invariants

### 1. State Variables:
- `i`: 0-based pointer into `word` ($0 \le i \le m$).
- `j`: 0-based pointer into `abbr` ($0 \le j \le n$).
- `x`: Integer accumulator for multi-digit numbers in `abbr`.

### 2. Transition Rules at $abbr[j]$:
1. **Digit ($abbr[j] \in \text{'0'}\dots\text{'9'}$):**
   - **Leading Zero Guard:** If $abbr[j] == \text{'0'}$ and $x == 0$: **Invalid**. Return `False`.
   - Accumulate value:
     $$
     x \leftarrow x \times 10 + \text{int}(abbr[j])
     $$
2. **Letter ($abbr[j] \in \text{'a'}\dots\text{'z'}$):**
   - Apply pending skip:
     $$
     i \leftarrow i + x, \quad x \leftarrow 0
     $$
   - Boundary & Equality Check:
     If $i \ge m$ or $word[i] \ne abbr[j]$: **Mismatch**. Return `False`.
   - Consume matching letter:
     $$
     i \leftarrow i + 1
     $$
3. Advance abbreviation pointer: $j \leftarrow j + 1$.

### 3. Terminal Condition:
When the loop exits, all characters in both strings must be exhausted:
$$
(i + x == m) \land (j == n)
$$

> **Invariant.** At every step, $i + x$ represents the exact index in `word` corresponding to the start of the next unprocessed character in `abbr`.

---

## 3. Step-by-Step Worked Execution

We trace $word = \text{"internationalization"}, abbr = \text{"i12iz4n"}$:
$m = 20, n = 7$. Initial: $i = 0, j = 0, x = 0$.

---

### Step 1: $j = 0, abbr[0] = \text{'i'}$
- Letter $\implies i \leftarrow i + x = 0 + 0 = 0, x = 0$.
- Check: $word[0] == \text{'i'}$ (**Match**).
- Advance: $i \leftarrow 0 + 1 = \mathbf{1}, \; j \leftarrow 0 + 1 = \mathbf{1}$.

---

### Step 2: $j = 1, abbr[1] = \text{'1'}$
- Digit: $x \leftarrow 0 \times 10 + 1 = \mathbf{1}$.
- Advance: $j \leftarrow 1 + 1 = \mathbf{2}$.

---

### Step 3: $j = 2, abbr[2] = \text{'2'}$
- Digit: $x \leftarrow 1 \times 10 + 2 = \mathbf{12}$.
- Advance: $j \leftarrow 2 + 1 = \mathbf{3}$.

---

### Step 4: $j = 3, abbr[3] = \text{'i'}$
- Letter $\implies$ apply pending jump:
  $$
  i \leftarrow 1 + 12 = \mathbf{13}, \quad x \leftarrow 0
  $$
- Check: $word[13] == \text{'i'}$ (**Match**).
- Advance: $i \leftarrow 13 + 1 = \mathbf{14}, \; j \leftarrow 3 + 1 = \mathbf{4}$.

---

### Step 5: $j = 4, abbr[4] = \text{'z'}$
- Letter $\implies$ apply pending jump: $i \leftarrow 14 + 0 = 14, x = 0$.
- Check: $word[14] == \text{'z'}$ (**Match**).
- Advance: $i \leftarrow 14 + 1 = \mathbf{15}, \; j \leftarrow 4 + 1 = \mathbf{5}$.

---

### Step 6: $j = 5, abbr[5] = \text{'4'}$
- Digit: $x \leftarrow 0 \times 10 + 4 = \mathbf{4}$.
- Advance: $j \leftarrow 5 + 1 = \mathbf{6}$.

---

### Step 7: $j = 6, abbr[6] = \text{'n'}$
- Letter $\implies$ apply pending jump:
  $$
  i \leftarrow 15 + 4 = \mathbf{19}, \quad x \leftarrow 0
  $$
- Check: $word[19] == \text{'n'}$ (**Match**).
- Advance: $i \leftarrow 19 + 1 = \mathbf{20}, \; j \leftarrow 6 + 1 = \mathbf{7}$.

---

### Step 8: Loop Termination & Alignment Verification
$j = 7 == n$. While loop exits.
Check final completeness:
$$
i + x == m \iff 20 + 0 == 20 \quad (\mathbf{True})
$$
$$
j == n \iff 7 == 7 \quad (\mathbf{True})
$$
Return:
$$
\mathbf{\text{True}}
$$

---

## 4. Complete Execution Trace

```text
word = "internationalization" (len 20), abbr = "i12iz4n" (len 7)

j=0: 'i' -> i=0, word[0]=='i' -> i=1, j=1
j=1: '1' -> x=1, j=2
j=2: '2' -> x=12, j=3
j=3: 'i' -> i=1+12=13, x=0, word[13]=='i' -> i=14, j=4
j=4: 'z' -> i=14, word[14]=='z' -> i=15, j=5
j=5: '4' -> x=4, j=6
j=6: 'n' -> i=15+4=19, x=0, word[19]=='n' -> i=20, j=7

Exit: i+x = 20 == 20, j == 7 -> Return True
```

| Step | Index $j$ | Token $abbr[j]$ | Type | Skip Accumulator $x$ | Word Pointer $i$ Before | Action Taken | Word Pointer $i$ After |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | 0 | `'i'` | Letter | 0 | 0 | Match $word[0] == \text{'i'}$ | 1 |
| 2 | 1 | `'1'` | Digit | 1 | 1 | Accumulate $x = 1$ | 1 |
| 3 | 2 | `'2'` | Digit | 12 | 1 | Accumulate $x = 12$ | 1 |
| 4 | 3 | `'i'` | Letter | 0 | 1 | Skip 12 $\to i = 13$, match $word[13] == \text{'i'}$ | 14 |
| 5 | 4 | `'z'` | Letter | 0 | 14 | Match $word[14] == \text{'z'}$ | 15 |
| 6 | 5 | `'4'` | Digit | 4 | 15 | Accumulate $x = 4$ | 15 |
| **7** | **6** | **'n'** | **Letter** | **0** | **15** | **Skip 4 $\to i = 19$, match $word[19] == \text{'n'}$** | **20** |
| **Exit**| 7 | - | Term | 0 | 20 | Complete ($i + x == m$) | **`true`** |

---

### Leading Zero Violation ($abbr = \text{"i012iz4n"}$)

```text
j = 0: 'i' -> match -> i = 1
j = 1: '0' -> abbr[j] == '0' and x == 0 -> LEADING ZERO DETECTED!
Immediate Return: False
```

---

## 5. Algorithmic Correctness

**Soundness.** Every character in $abbr$ is processed strictly from left to right. Digits form decimal numbers that advance pointer $i$ forward by the exact replacement count. Letters require exact character matches at $word[i]$. Rejecting leading zeros enforces the non-empty, non-redundant abbreviation specification. If any character mismatches or pointer bounds are violated, the function returns `False`.

**Completeness.** The while loop advances $j$ by 1 in every iteration, guaranteeing termination in at most $|abbr|$ steps. Checking $i + x == m$ at the end handles abbreviations that conclude with numeric skips (e.g. `"internationaliz4"`).

---

## 6. Traps This Instance Exposes

- **Leading Zeros vs Internal Zeros:** The digit `'0'` is illegal ONLY at the beginning of a numeric token ($x == 0$). A zero following a non-zero digit (e.g. `"10"`) is legal and represents the value 10.
- **Trailing Numeric Skip:** If $abbr$ ends with a number (e.g. $word = \text{"code"}, abbr = \text{"c3"}$), the while loop finishes with $x = 3$. Checking $i + x == m$ validates that the trailing skip matches the remaining word length.
- **Pointer Overflow:** If an abbreviation has a skip larger than the word (e.g. $word = \text{"hi"}, abbr = \text{"10"}$), skipping $i + x$ exceeds $m$. Checking $i \ge m$ before indexing prevents `IndexError`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M + N)$, where $M = \text{len}(word)$ and $N = \text{len}(abbr)$.
  - The while loop iterates at most $N$ times.
  - Pointer $i$ increases monotonically up to $M$.
  - Each step executes in $O(1)$ constant time.
  - Overall runtime is linear $O(M + N)$, finishing in $< 0.01$ ms.
- **Auxiliary Space Complexity:** $O(1)$ strict constant memory, maintaining only scalar pointer registers $i, j, x, m, n$.
