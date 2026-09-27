# Guided Example: Decoded String at Index

We trace the step-by-step virtual tape length accumulation, reverse unwinding via modular arithmetic ($k \pmod m$), cyclic prefix reduction, and $\mathcal{O}(1)$ memory character extraction on representative run-length compressed tapes:

- **Input:**
  $$
  s = \text{"leet2code3"}, \quad k = 10
  $$
- **Required output:** `"o"`
  - Tape decoding rules:
    - We start with an empty string.
    - Read $s$ character by character:
      - If letter: append the letter to the tape.
      - If digit $d$: repeat the entire tape read so far $d$ times.
    - We must return the $k$-th letter (**1-indexed**) of the fully decoded string.
    - Forward expansion of $s = \text{"leet2code3"}$:
      - `"leet"` $\implies \text{"leet"}$ (length 4).
      - `'2'` $\implies \text{"leetleet"}$ (length 8).
      - `"code"` $\implies \text{"leetleetcode"}$ (length 12).
      - `'3'` $\implies \text{"leetleetcodeleetleetcodeleetleetcode"}$ (length 36).
    - Examining the 10th character (1-indexed):
      - 1: `'l'`, 2: `'e'`, 3: `'e'`, 4: `'t'`, 5: `'l'`, 6: `'e'`, 7: `'e'`, 8: `'t'`, 9: `'c'`, **10: `'o'`**.
      - Result: **`"o"`**.
- **The Reverse Unwinding & Modulo Folding Invariant:**
  - **The Memory Wall:**
    - An encoded string like `"a2345678999999999999999"` creates a decoded tape of length exceeding $10^{15}$, making physical string generation completely impossible.
  - **Cyclic Modulo Folding ($k \pmod m$):**
    - Suppose a tape of length $m$ is formed by repeating a base block of length $m / d$ a total of $d$ times.
    - Any index $k$ within the repeated block maps to the identical character at position:
      $$
      k' = k \pmod{\frac{m}{d}}
      $$
    - Similarly, if the tape ends with an individual letter $c$, and $k$ is not the final character, removing $c$ shrinks the length $m \leftarrow m - 1$ while keeping $k$ unchanged.
  - **The Match Condition:**
    - Whenever $k \pmod m == 0$, the target character is precisely the **final character of the current prefix**!
    - If the current character $c$ is an alphabet letter, then $c$ is that final character $\implies$ return $c$ immediately!
    - Otherwise, reverse the operation:
      - If $c$ is a digit $d$: $m \leftarrow \lfloor m / d \rfloor$.
      - If $c$ is a letter: $m \leftarrow m - 1$.

---

## 1. Instance & Teaching Goal

Given $s = \text{"leet2code3"}$ and $k = 10$, find the 10th character without constructing the 36-character string.

```text
Forward Pass:
  "leet" -> m = 4
  '2'    -> m = 8
  "code" -> m = 12
  '3'    -> m = 36

Backward Pass from end of s with k = 10:
  c = '3': digit. k % 36 = 10. m becomes 36 / 3 = 12.
  c = 'e': letter. k % 12 = 10. m becomes 12 - 1 = 11.
  c = 'd': letter. k % 11 = 10. m becomes 11 - 1 = 10.
  c = 'o': letter. k % 10 = 0 -> MATCH!

Character is 'o'!
```

The teaching goal is to demonstrate how working backwards through the construction tree folds large indices into fundamental base characters.

---

## 2. Conceptual Foundation & Invariants

### 1. Forward Length Computation:
Let $m_0 = 0$. For character $c_t$ at step $t$:
$$
m_t = \begin{cases}
m_{t-1} \times \text{int}(c_t) & \text{if } c_t \text{ is a digit} \\
m_{t-1} + 1 & \text{if } c_t \text{ is a letter}
\end{cases}
$$

### 2. Backward Unwinding Loop:
For each character $c$ in reverse order:
1. Normalize query index:
   $$
   k \leftarrow k \pmod m
   $$
2. Check terminal boundary:
   $$
   \text{If } k == 0 \land c \text{ is alphabetic} \implies \text{return } c
   $$
3. Shrink virtual tape:
   $$
   m \leftarrow \begin{cases}
   \lfloor m / \text{int}(c) \rfloor & \text{if } c \text{ is a digit} \\
   m - 1 & \text{if } c \text{ is a letter}
   \end{cases}
   $$

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"leet2code3"}, k = 10$:

---

### Phase 1: Compute Total Virtual Length $m$
- `'l'`: $m = 1$
- `'e'`: $m = 2$
- `'e'`: $m = 3$
- `'t'`: $m = 4$
- `'2'`: $m = 4 \times 2 = 8$
- `'c'`: $m = 8 + 1 = 9$
- `'o'`: $m = 9 + 1 = 10$
- `'d'`: $m = 10 + 1 = 11$
- `'e'`: $m = 11 + 1 = 12$
- `'3'`: $m = 12 \times 3 = 36$

Total length of decoded tape is $m = 36$.

---

### Phase 2: Reverse Unwinding from Right to Left

---

#### Step 1: Character `'3'` (Digit, $m = 36$)
- Fold index: $k \leftarrow 10 \pmod{36} = 10$.
- Revert operation: $m \leftarrow 36 // 3 = \mathbf{12}$.

---

#### Step 2: Character `'e'` (Letter, $m = 12$)
- Fold index: $k \leftarrow 10 \pmod{12} = 10$.
- Check match: $k = 10 \ne 0$. Not terminal.
- Revert operation: $m \leftarrow 12 - 1 = \mathbf{11}$.

---

#### Step 3: Character `'d'` (Letter, $m = 11$)
- Fold index: $k \leftarrow 10 \pmod{11} = 10$.
- Check match: $k = 10 \ne 0$. Not terminal.
- Revert operation: $m \leftarrow 11 - 1 = \mathbf{10}$.

---

#### Step 4: Character `'o'` (Letter, $m = 10$)
- Fold index:
  $$
  k \leftarrow 10 \pmod{10} = \mathbf{0}
  $$
- Check match:
  - $k == 0$ (the index aligns with the exact end of the block).
  - Current character $c = \text{'o'}$ is alphabetic.
  - **Match Found!**
- **Immediate Return: `"o"`**.

---

## 4. Complete Execution Trace

| Step (Reverse) | Character $c$ | Type | Tape Length $m$ | Normalized Index $k \pmod m$ | Match? ($k \equiv 0 \land c \text{ is alpha}$) | Next Tape Length $m'$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `'3'` | Digit | $36$ | $10 \pmod{36} = 10$ | No (Digit) | $36 / 3 = 12$ |
| $2$ | `'e'` | Letter | $12$ | $10 \pmod{12} = 10$ | No ($10 \ne 0$) | $12 - 1 = 11$ |
| $3$ | `'d'` | Letter | $11$ | $10 \pmod{11} = 10$ | No ($10 \ne 0$) | $11 - 1 = 10$ |
| **$4$** | **`'o'`** | **Letter** | **$10$** | **$10 \pmod{10} = 0$** | **`YES! Return "o"`** | — |

---

## 5. Boundary Cases & Failure Modes

- **$k = 1$:** Always returns the very first character of the string.
- **$k == m$:** $k \pmod m = 0$, so the final character of the active block is matched immediately.
- **Repeated Digits (e.g. `"ha22"`, $k = 5$):**
  - "ha" (len 2) $\to$ "haha" (len 4) $\to$ "hahahaha" (len 8).
  - Unwinds through both multiplications sequentially without error.
- **Astronomical Lengths ($10^{15}$):** Handled in $\mathcal{O}(1)$ space because arithmetic operators evaluate large integers natively without materializing strings.

---

## 6. Traps & Common Anti-Patterns

- **Materializing the Decoded String:** Creating string buffers for repetitions exceeds heap memory and causes Memory Limit Exceeded / Out Of Memory errors.
- **0-Indexing Confusion:** The problem uses 1-indexed $k$. Working with $k \pmod m$ where $k = m$ naturally yields $0$, so checking $k == 0$ directly captures the final character of the block.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Forward pass over string of length $N$: $\mathcal{O}(N)$.
  - Backward unwinding pass over at most $N$ characters: $\mathcal{O}(N)$.
  - String length $N \le 100$.
  - Total Time: strictly $\mathcal{O}(N)$, executing in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space using two 64-bit integer counters ($m, k$).
