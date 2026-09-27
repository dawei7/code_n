# Guided Example: Number of Lines to Write String

We trace the step-by-step proportional font pixel width mapping ($w = widths[\text{ord}(c) - 97]$), 100-pixel line capacity thresholding, greedy word-wrapping simulation, line counter incrementation ($lines \leftarrow lines + 1$), and final residual line width calculation ($[lines, last]$) on representative typesetting strings:

- **Input:**
  - Character widths: $widths = [10, 10, \dots, 10]$ (all 26 letters have width 10 pixels).
  - String to typeset: $s = \text{"abcdefghijklmnopqrstuvwxyz"}$ (26 characters).
- **Required output:**
  $$
  [3, 60]
  $$
  - Typography typesetting rules:
    - Each character $c$ occupies $widths[\text{ord}(c) - \text{ord('a')}]$ pixels.
    - Each line has a fixed maximum width of **100 pixels**.
    - Characters are placed sequentially from left to right.
    - If the next character causes the current line to exceed 100 pixels, it cannot be split; it must be pushed to start a **new line**.
    - Objective: Return $[lines, last]$, where $lines$ is the total number of lines used, and $last$ is the pixel width consumed on the final line.
    - For the uniform input:
      - Each character takes 10 pixels.
      - Line 1: Characters `'a'` through `'j'` ($10 \times 10 = 100$ pixels). Full!
      - Line 2: Characters `'k'` through `'t'` ($10 \times 10 = 100$ pixels). Full!
      - Line 3: Characters `'u'` through `'z'` ($6 \times 10 = 60$ pixels).
      - Total lines used: **3**.
      - Width on last line: **60**.
      - Output: `[3, 60]`.
- **Greedy Line Wrapping Invariant:**
  - **The 1D Capacity Packing Principle:**
    - Maintain two scalar state variables:
      - $lines$: Count of lines initiated (begins at $1$).
      - $last$: Cumulative pixel width on the current active line (begins at $0$).
  - **Sequential Token Consumption ($c \in s$):**
    - Determine pixel width:
      $$
      w = widths[\text{ord}(c) - 97]
      $$
    - **Capacity Test:**
      - If $last + w \le 100$: The character fits on the current line.
        $$
        last \leftarrow last + w
        $$
      - If $last + w > 100$: The character overflows the current line.
        - Advance to a new line:
          $$
          lines \leftarrow lines + 1
          $$
        - Start new line with this character:
          $$
          last \leftarrow w
          $$
  - **Terminal Output:**
    - After all characters are placed, $[lines, last]$ represents the exact typographical layout.
- **Step-by-Step Worked Execution Trace on the 26-Letter Alphabet:**
  - Initialize: $lines = 1, last = 0$.
  - **Characters 1 to 10 (`'a'` to `'j'`):**
    - Each character has width $w = 10$.
    - Progressively adds 10 pixels:
      - `'a'`: $0 + 10 = 10 \le 100$
      - `'b'`: $10 + 10 = 20 \le 100$
      - $\dots$
      - `'j'`: $90 + 10 = 100 \le 100$ (Line 1 is exactly full).
    - Status after `'j'`: $lines = 1, last = 100$.
  - **Character 11 (`'k'`, $w = 10$):**
    - Capacity check:
      $$
      last + w = 100 + 10 = 110 > 100 \implies \mathbf{Line\ Overflow!}
      $$
    - Line wrap triggered:
      $$
      lines \leftarrow 1 + 1 = \mathbf{2}
      $$
      $$
      last \leftarrow w = \mathbf{10}
      $$
  - **Characters 12 to 20 (`'l'` to `'t'`):**
    - Characters `'l'` through `'t'` add $9 \times 10 = 90$ pixels to Line 2.
    - Status after `'t'`: $lines = 2, last = 10 + 90 = 100$.
  - **Character 21 (`'u'`, $w = 10$):**
    - Capacity check:
      $$
      last + w = 100 + 10 = 110 > 100 \implies \mathbf{Line\ Overflow!}
      $$
    - Line wrap triggered:
      $$
      lines \leftarrow 2 + 1 = \mathbf{3}
      $$
      $$
      last \leftarrow w = \mathbf{10}
      $$
  - **Characters 22 to 26 (`'v'` to `'z'`):**
    - 5 remaining letters, each $w = 10$.
    - Progressively adds 50 pixels:
      $$
      last \leftarrow 10 + 50 = \mathbf{60}
      $$
  - **Assembly of Typesetting Metrics:**
    - Total lines: $lines = \mathbf{3}$.
    - Last line width: $last = \mathbf{60}$.
    - Result:
      $$
      ans = [\mathbf{3}, \; \mathbf{60}]
      $$
- **Variable Widths Trace ($s = \text{"bbbcccdddaaa"}$):**
  - Letter widths vary (e.g. 'a' is 4, 'b' is 10, 'c' is 10, 'd' is 10).
  - Cumulative sum increments irregularly; wrapping triggers as soon as the sum crosses 100.
- **Exact Single Line Fit ($s = \text{"a"}$, $w = 10$):**
  - $lines = 1, last = 10 \implies [1, 10]$.
- **Exact Multiple Boundary ($last = 100$ on final character):**
  - If the last character perfectly finishes a line ($last = 100$), no new empty line is opened. Returns $[lines, 100]$.

This instance demonstrates greedy offline 1D container packing and sequential stream chunking under capacity limits, mathematically proves why sequential no-break typesetting satisfies optimal partition bounds on monotonic streams, and derives $O(|s|)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given letter widths and a string $s$:
Pack characters sequentially into lines of **at most 100 pixels**.
Return `[total_lines, last_line_pixels]`.

```text
widths = all 10 pixels
s      = "abcdefghijklmnopqrstuvwxyz" (26 letters)

Line 1: 'a' through 'j' -> 10 * 10 = 100 pixels (full!)
Line 2: 'k' through 't' -> 10 * 10 = 100 pixels (full!)
Line 3: 'u' through 'z' -> 6 * 10 = 60 pixels

Total lines = 3, Last line width = 60
Result: [ 3, 60 ]
```

### The Invariant of Greedy Line Packing
- Characters cannot be split across lines.
- If current character causes $last + w > 100$, advance to a new line ($lines \mathrel{+}= 1$) and set $last = w$.
- Otherwise, add to current line ($last \mathrel{+}= w$).

---

## 2. Conceptual Foundation & Invariants

### 1. Pixel Width Lookup:
$$
w_i = widths[\text{ord}(s[i]) - 97]
$$

### 2. State Transition Function:
$$
(lines, last) \leftarrow \begin{cases}
(lines, \; last + w) & last + w \le 100 \\
(lines + 1, \; w) & last + w > 100
\end{cases}
$$

> **Greedy Bin-Packing Invariant.** The sequential word-wrap problem is an online 1D bin-packing problem with fixed order. The Next-Fit strategy is strictly optimal when item order cannot be permuted.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Characters `'a'` to `'j'`
- 10 characters $\times 10 = 100$ pixels.
- $lines = 1, last = 100$.

---

### Step 2: Character `'k'`
- $100 + 10 = 110 > 100 \implies$ wraps to Line 2!
- $lines = 2, last = 10$.

---

### Step 3: Characters `'l'` to `'t'`
- 9 characters $\times 10 = 90$ pixels.
- $last = 10 + 90 = 100$.

---

### Step 4: Character `'u'`
- $100 + 10 = 110 > 100 \implies$ wraps to Line 3!
- $lines = 3, last = 10$.

---

### Step 5: Characters `'v'` to `'z'`
- 5 characters $\times 10 = 50$ pixels.
- $last = 10 + 50 = 60$.

---

### Step 6: Output
$$
[\mathbf{3}, \; \mathbf{60}]
$$

---

## 4. Complete Execution Trace

| Segment Processed | Running Pixel Sum | Limit Check ($\le 100$) | Action | Active Line Count $lines$ | Residual Width $last$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Initial | $0$ | — | — | $1$ | $0$ |
| `'a' \dots 'j'` | $100$ | $100 \le 100$ | Fits line 1 | $1$ | $100$ |
| `'k'` | $110$ | $110 > 100$ | **Wrap to Line 2** | $2$ | $10$ |
| `'l' \dots 't'` | $100$ | $100 \le 100$ | Fits line 2 | $2$ | $100$ |
| `'u'` | $110$ | $110 > 100$ | **Wrap to Line 3** | $3$ | $10$ |
| **`'v' \dots 'z'`** | **$60$** | **$60 \le 100$** | **Fits line 3** | **`3`** | **`60`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Character ($s = \text{"a"}$):** 1 line, width of that character $\implies [1, w]$.
- **Line Perfectly Filled ($last == 100$):** Exactly 100 pixels; does not wrap until the next character arrives.
- **Each Character Fills Full Line ($w = 100$):** Every character starts a new line $\implies [|s|, 100]$.
- **Longest String ($|s| = 1000$):** Linear pass completes in $< 0.1$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Starting Line Counter at 0:** Even a single character requires 1 line; initial state must be $lines = 1$.
- **Starting a New Line at 100 when Empty:** If the last character lands exactly at 100, do NOT increment $lines$; only increment when an incoming character exceeds 100.
- **ASCII Offsets:** Letter `'a'` is ASCII 97; offset `ord(c) - ord('a')` guarantees valid indexing in range $0 \dots 25$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass over string $s$ of length $N$: $\mathcal{O}(N)$.
  - Constant-time array lookup and arithmetic per character: $\mathcal{O}(1)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 1000$. Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
