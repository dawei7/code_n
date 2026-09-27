# Guided Example: Sentence Screen Fitting

We trace the step-by-step modular string linearization, row cursor advance, word-boundary space absorption, rollback word preservation, and total cycle quotient calculation on representative terminal screens:

- **Input:** $sentence = [\text{"a"}, \text{"bcd"}, \text{"e"}], \quad rows = 3, \quad cols = 6$
- **Required output:** `2`
  - Concatenated sentence cycle with delimiter spaces:
    $$
    s = \text{"a bcd e "} \quad (m = 8)
    $$
  - Character mapping by index modulo 8:
    - Index $0$: `'a'`, Index $1$: `' '`
    - Indices $2\dots 4$: `'b'`, `'c'`, `'d'`, Index $5$: `' '`
    - Index $6$: `'e'`, Index $7$: `' '`
  - Row-by-row cursor simulation:
    - **Row 0:** $cur \leftarrow 0 + 6 = 6$. Character at index $6$ is `'e'` (start of a new word). Preceding character at index $5$ is `' '` $\implies$ line boundary cleanly splits between words. Row 0 fits `"a bcd "` ($cur = 6$).
    - **Row 1:** $cur \leftarrow 6 + 6 = 12$. Character at $12 \pmod 8 = 4$ is `'d'` (middle of `"bcd"`). Cannot break word $\implies$ roll back $cur$ to $10$ (where index $9 \equiv 1$ was `' '`). Row 1 fits `"e a   "` ($cur = 10$).
    - **Row 2:** $cur \leftarrow 10 + 6 = 16$. Character at $16 \pmod 8 = 0$ is `'a'`. Preceding character $15 \equiv 7$ is `' '` $\implies$ clean line boundary. Row 2 fits `"bcd e "` ($cur = 16$).
  - Full sentence repetitions completed:
    $$
    \lfloor cur / m \rfloor = \lfloor 16 / 8 \rfloor = \mathbf{2}
    $$
- **Two Words Across Two Rows:** $sentence = [\text{"hello"}, \text{"world"}], rows = 2, cols = 8 \implies$ Row 0: `"hello   "`, Row 1: `"world   "` $\implies \mathbf{1}$
- **Single Letter Fit:** $sentence = [\text{"a"}], rows = 20000, cols = 20000 \implies$ each row fits $10000$ words $\implies \mathbf{200000000}$

This instance demonstrates modeling 2D screen text-justification via 1D modular pointer arithmetic, proves how word truncation rollback guarantees unbroken words without per-word scanning, and derives $O(rows + \sum |w|)$ runtime and $O(\sum |w|)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string array $sentence = [\text{"a"}, \text{"bcd"}, \text{"e"}]$ and a screen of size $rows = 3 \times cols = 6$:
Find how many times the sentence can be fitted on the screen under the formatting rules:
1. Words must appear in the exact order specified.
2. Consecutive words on the same row must be separated by a single space `' '`.
3. A word cannot be split across two lines. If a word cannot fit in the remaining columns of the current row, the entire word must move to the next row.

```text
Screen (3 rows x 6 columns):

        0   1   2   3   4   5
      +---+---+---+---+---+---+
Row 0 | a |   | b | c | d |   |   -> Fits "a bcd"
      +---+---+---+---+---+---+
Row 1 | e |   | a |   |   |   |   -> Fits "e a" (Completes Sentence #1!)
      +---+---+---+---+---+---+
Row 2 | b | c | d |   | e |   |   -> Fits "bcd e" (Completes Sentence #2!)
      +---+---+---+---+---+---+

Total Full Sentences Fitted: 2
```

### The Inefficiency of Word-by-Word Simulation
Iterating word by word and row by row takes $O(\text{total words placed})$ time. When $rows = 20000$ and $cols = 20000$, the screen can hold hundreds of millions of words, causing a naive loop to time out.
Instead, we view the text as a **repeating 1D infinite stream** and advance by an entire row ($cols$) at a time.

---

## 2. Conceptual Foundation & Invariants

### 1. The Periodic Stream String:
Concatenate all words in $sentence$ separated by spaces, with a trailing space:
$$
s = \text{"a bcd e "} \quad (m = \text{length} = 8)
$$
Every complete traversal of $m$ characters in this stream represents exactly **one full sentence**.

### 2. The Row Advance and Word Boundary Invariant:
For each row, advance the global character counter by the row's capacity:
$$
cur \leftarrow cur + cols
$$
Now inspect the character at position $cur \pmod m$:
1. **Case A (Landing on a Space):**
   If $s[cur \pmod m] == \text{' '}$, the row ended precisely at the end of a word. The trailing space can be dropped at the end of the line. The next line can start immediately at the subsequent word:
   $$
   cur \leftarrow cur + 1
   $$
2. **Case B (Landing on the Start of a Word):**
   If the character immediately before was a space ($s[(cur - 1) \pmod m] == \text{' '}$), the row packed the previous words completely, and the next line begins cleanly with the new word. No rollback needed.
3. **Case C (Landing in the Middle of a Word):**
   If the cursor lands inside a word, that word cannot be split. We must decrement $cur$ until $s[(cur - 1) \pmod m] == \text{' '}$, effectively moving the incomplete word to the start of the next row.

> **Invariant.** At the end of processing each row, $cur$ points to the start index in the cyclical stream $s$ that will be typed in column 0 of the next row.

---

## 3. Step-by-Step Worked Execution

We trace $sentence = [\text{"a"}, \text{"bcd"}, \text{"e"}]$ with $m = 8, rows = 3, cols = 6$:
Start with $cur = 0$.

---

### Row 0:
- Add row width:
  $$
  cur \leftarrow 0 + 6 = \mathbf{6}
  $$
- Inspect index $6 \pmod 8 = 6$: $s[6] = \text{'e'}$.
- Check boundary condition:
  - Character before is $s[(6 - 1) \pmod 8] = s[5] = \text{' '}$.
  - The characters typed in Row 0 are indices $0 \dots 5$:
    $$
    s[0\dots 5] = \text{"a bcd "}
    $$
  - The line fits `"a"` (col 0), space (col 1), `"bcd"` (cols 2-4), space (col 5).
  - The next word `"e"` cleanly starts at index 6 for Row 1. No rollback.
- State after Row 0: $cur = \mathbf{6}$.

---

### Row 1:
- Add row width:
  $$
  cur \leftarrow 6 + 6 = \mathbf{12}
  $$
- Inspect index $12 \pmod 8 = 4$: $s[4] = \text{'d'}$.
- Rollback evaluation:
  - $s[4]$ is `'d'`, which is the tail of `"bcd"`.
  - Is $s[(12 - 1) \pmod 8] == \text{' '}$? $s[3] = \text{'c'} \ne \text{' '}$. Decrement $cur \leftarrow 11$.
  - Is $s[(11 - 1) \pmod 8] == \text{' '}$? $s[2] = \text{'b'} \ne \text{' '}$. Decrement $cur \leftarrow 10$.
  - Is $s[(10 - 1) \pmod 8] == \text{' '}$? $s[1] = \text{' '}$ (**Match!** Stop rollback).
- $cur = \mathbf{10}$.
- Characters typed in Row 1: indices $6 \dots 9$:
  $$
  s[6] = \text{'e'}, \quad s[7] = \text{' '}, \quad s[8] \equiv s[0] = \text{'a'}, \quad s[9] \equiv s[1] = \text{' '}
  $$
- Display: `"e a   "`. Word `"bcd"` could not fit in the remaining 2 columns, so it was deferred.
- State after Row 1: $cur = \mathbf{10}$.

---

### Row 2:
- Add row width:
  $$
  cur \leftarrow 10 + 6 = \mathbf{16}
  $$
- Inspect index $16 \pmod 8 = 0$: $s[0] = \text{'a'}$.
- Check boundary condition:
  - Preceding character $s[(16 - 1) \pmod 8] = s[7] = \text{' '}$.
  - Clean word start!
- Characters typed in Row 2: indices $10 \dots 15$:
  $$
  s[10\dots 15] \equiv s[2\dots 7] = \text{"bcd e "}
  $$
- Display: `"bcd e "`.
- State after Row 2: $cur = \mathbf{16}$.

---

### Termination & Result:
All 3 rows have been processed. Total stream characters successfully placed: $cur = 16$.
$$
\text{Total Sentences} = \lfloor cur / m \rfloor = \lfloor 16 / 8 \rfloor = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| Row | Start Cursor | Add $cols = 6$ | Target Char $s[cur \pmod 8]$ | Boundary Rollback Needed? | Final $cur$ | Row Content Displayed | Cumulative Words |
|:---:|:---:|:---:|:---:|:---|:---:|:---|:---:|
| **Init** | — | — | — | — | $0$ | — | $0$ |
| **0** | $0$ | $6$ | $s[6] = \text{'e'}$ | No ($s[5] == \text{' '}$) | **$6$** | `\|a\| \|b\|c\|d\| \|` | `"a bcd"` |
| **1** | $6$ | $12$ | $s[4] = \text{'d'}$ | **Yes (rolls back $12 \to 10$)** | **$10$** | `\|e\| \|a\| \| \| \|` | `"e a"` (Sentence 1 completed!) |
| **2** | $10$ | $16$ | $s[0] = \text{'a'}$ | No ($s[7] == \text{' '}$) | **$16$** | `\|b\|c\|d\| \|e\| \|` | `"bcd e"` (Sentence 2 completed!) |
| **Done**| — | — | — | — | **$16$** | — | **Result: $16 \mathbin{//} 8 = \mathbf{2}$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Word Array ($sentence = [\text{"a"}], rows = 2, cols = 3$):** String is `"a "` ($m = 2$). Row 0 gets $cur = 3 \to 4$ (`"a a"`), Row 1 gets $4 + 3 = 7 \to 8$ (`"a a"`). Total $8 // 2 = \mathbf{4}$ times.
- **Word Length Exactly Equal to $cols$:** A word fills the entire width of a row. No spaces can follow it on that row. Handled naturally because the trailing space lands at $cur \pmod m$, incrementing $cur$ by 1 for the next row.
- **Large Rows ($rows = 2 \times 10^4$):** Because the loop executes once per row (taking at most $\max(|word|)$ rollbacks per row), total operations $\le 20000 \times 10 = 2 \times 10^5$, executing in under 10 ms.

---

## 6. Traps & Common Anti-Patterns

- **Simulating Word-by-Word:** Advancing one word at a time times out when rows and cols are large. Advancing row-by-row reduces the loop count to exactly $rows$.
- **Breaking Words Across Rows:** Forgetting the rollback loop splits words across row boundaries (e.g. putting `"bc"` on row 1 and `"d"` on row 2), which violates the fundamental problem contract.
- **Forgetting Trailing Space in Stream:** Failing to append a space after the last word in the cyclic stream causes the last word and the first word of the next repetition to merge into a single word without a separator.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Constructing string $s$ takes $O(L)$ time, where $L = \sum |word| + |sentence|$.
  - The loop runs for $rows$ iterations.
  - In each iteration, cursor rollback examines at most $\max(|word|) \le 10$ characters.
  - Total Time: $\mathcal{O}(L + rows \cdot \max(|word|))$. For $rows = 20000$ and word length $\le 10$, $\approx 2 \times 10^5$ operations (executes in $\approx 5$ ms).
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(L)$ to store the concatenated periodic stream string $s$.
