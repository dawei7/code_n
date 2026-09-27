# Guided Example: Find the Width of Columns of a Grid

## 1. The grid, the question, and the measurement that matters

The input is a **0-indexed** integer matrix `grid` with $m$ rows and $n$ columns whose entries may be negative. Every entry carries a purely typographic quantity: the number of characters its decimal representation occupies. The statement fixes that measurement exactly. An integer whose magnitude needs $len$ digits measures $len$ when it is non-negative and $len + 1$ when it is negative, because the minus sign is itself a character. The width of a column is the largest such measurement among that column's $m$ entries, and the required output is an array of length $n$ holding the width of every column.

One structural observation decides the entire method: an entry in column $c$ can never influence the width of a different column $c' \ne c$. The problem therefore splits into $n$ independent one-dimensional maximizations, and each one is answered by a single sweep down its own column. Nothing needs to be sorted, and nothing needs to be remembered beyond one running best per column.

## 2. The representative input

Official Example 2 supplies a $3 \times 3$ grid that mixes signs and lets each column be won in a different row, so a single lucky guess about "the longest entry" cannot produce the whole answer.

| Row index $r$ | column 0 | column 1 | column 2 |
|---|---|---|---|
| 0 | `-15` | `1` | `3` |
| 1 | `15` | `7` | `12` |
| 2 | `5` | `6` | `-2` |

The required output is `[3, 1, 2]`. The point of the lesson is to derive that array from the measurement rule rather than to assert it, so the columns are measured one cell at a time below.

## 3. The length function that the statement defines

Two quantities compose the measurement. Let $L(x)$ be the number of digits needed by the magnitude of $x$, and let $W(x)$ be the number of characters in the printed form of $x$:

$$
L(x) =
\begin{cases}
\lfloor \log_{10} \lvert x \rvert \rfloor + 1, & \lvert x \rvert \ge 1, \\
1, & x = 0,
\end{cases}
\qquad
W(x) = L(x) + \begin{cases} 1, & x < 0, \\ 0, & x \ge 0. \end{cases}
$$

The separate case for `0` is not cosmetic: the decimal representation of zero really is the single character `0`, while $\log_{10} 0$ has no real value, so the logarithm formula simply does not apply there. With $W$ in hand the requested array is a column-wise maximum:

$$
\text{ans}[c] = \max_{0 \le r < m} W(\text{grid}[r][c]), \qquad 0 \le c < n .
$$

Written as a recurrence over the rows, with $b_r(c)$ denoting the best width seen in column $c$ after the first $r$ rows have been examined:

$$
b_0(c) = -\infty, \qquad b_{r+1}(c) = \max\bigl(b_r(c),\; W(\text{grid}[r][c])\bigr), \qquad \text{ans}[c] = b_m(c).
$$

Every one of the nine entries of the representative grid, decomposed into those two components:

| Entry | Sign class | Magnitude digits $L$ | Sign cost | Width $W$ |
|---|---|---|---|---|
| `-15` | negative | 2 | 1 | 3 |
| `1` | non-negative | 1 | 0 | 1 |
| `3` | non-negative | 1 | 0 | 1 |
| `15` | non-negative | 2 | 0 | 2 |
| `7` | non-negative | 1 | 0 | 1 |
| `12` | non-negative | 2 | 0 | 2 |
| `5` | non-negative | 1 | 0 | 1 |
| `6` | non-negative | 1 | 0 | 1 |
| `-2` | negative | 1 | 1 | 2 |

## 4. The sweep, row by row

The accumulator starts at $-\infty$ for each column, meaning "no candidate measured yet". Each row contributes one candidate per column, and a candidate is kept only when it beats the value already held.

| Stage | Entries just measured | Column 0 best | Column 1 best | Column 2 best |
|---|---|---|---|---|
| before row 0 | none | $-\infty$ | $-\infty$ | $-\infty$ |
| after row 0 | `-15`, `1`, `3` | 3, from `-15` | 1, from `1` | 1, from `3` |
| after row 1 | `15`, `7`, `12` | 3 (unchanged) | 1 (unchanged, `7` ties) | 2, from `12` |
| after row 2 | `5`, `6`, `-2` | 3 (unchanged) | 1 (unchanged, `6` ties) | 2 (unchanged, `-2` ties) |

Three details in that table are worth naming.

- Row 1 contains the numerically largest entry of column 0, namely `15`, yet column 0's best stays at 3. The width of `15` is 2, so the larger number is the *smaller* measurement. This is the decisive trap of the problem.
- Column 1 never changes after its first candidate. All three of its entries have width 1, and a maximum that has already been attained cannot be raised by later ties.
- Column 2 is won twice over: `12` establishes width 2 at row 1, and `-2` merely reproduces width 2 at row 2. The output asks for the width, not for the identity of the winner, so the tie is harmless — but it shows that the winning entry is not unique and must never be reported.

The per-column verdict, with the width of every entry listed in row order:

| Column $c$ | Entry widths, rows 0 to 2 | Largest width | Entries attaining it |
|---|---|---|---|
| 0 | 3, 2, 1 | 3 | `-15` (row 0) |
| 1 | 1, 1, 1 | 1 | `1`, `7`, `6` (all rows) |
| 2 | 1, 2, 2 | 2 | `12` (row 1), `-2` (row 2) |

Concatenating the three largest widths in column order gives `[3, 1, 2]`, which matches the expected output of the official example.

## 5. Invariant and Correctness of the single pass

The invariant maintained by the sweep is stated over row prefixes, not over whole columns, and that is exactly what makes one pass legitimate.

> **Invariant $I(r)$.** After the first $r$ rows have been consumed, the accumulator of every column $c$ satisfies $b_r(c) = \max\{\, W(\text{grid}[r'][c]) : 0 \le r' < r \,\}$, that maximum being $-\infty$ when $r = 0$.

*Base case.* $I(0)$ asserts that the accumulators equal the maximum over an empty index set. The empty maximum is $-\infty$, which is exactly the initialization, so $I(0)$ holds.

*Inductive step.* Assume $I(r)$. Row $r$ contributes the single new candidate $W(\text{grid}[r][c])$ to column $c$, and the recurrence sets $b_{r+1}(c) = \max\bigl(b_r(c), W(\text{grid}[r][c])\bigr)$. Substituting the hypothesis turns that expression into the maximum over rows $0$ through $r$, which is precisely $I(r+1)$.

*Termination.* At $r = m$ the invariant reads $b_m(c) = \max_{0 \le r' < m} W(\text{grid}[r'][c])$, and the right-hand side is the definition of $\text{ans}[c]$.

Soundness and completeness follow from the two halves of that identity. Every value ever stored is either $-\infty$ or the measurement of an entry that genuinely lies in the column, so the reported width is realized by a real entry and can never overstate the column. Conversely, the induction covers every row index $0 \le r' < m$ of every column, so no entry whose width exceeds the reported one can be skipped, and the answer can never understate the column. Exactness is therefore a consequence of the invariant rather than of any particular traversal order.

Two properties of the maximum make the traversal shape irrelevant. Maximum is commutative, so the columns may be visited in any order and even interleaved; and it is idempotent, so revisiting an entry changes nothing. The only reason to touch each entry exactly once is cost, which is the subject of the final section.

## 6. Traps this instance exposes

| Situation | Tempting shortcut | Why it fails | Correct treatment |
|---|---|---|---|
| A negative entry with fewer magnitude digits than the column's numeric maximum | Take the numeric maximum of the column, then measure it | Column 0's numeric maximum is `15`, whose width is 2, but `-15` has width 3 and is the column's true width | Compare widths themselves, never the raw numeric values |
| An entry equal to `0` | Apply $\lfloor \log_{10} \lvert x \rvert \rfloor + 1$ uniformly | $\log_{10} 0$ is undefined, and a "zero digits" result would be nonsense | Count `0` as the single character it prints as |
| An entry at the lower bound of the value range | Assume $10^{9}$ is the longest possible entry | The statement guarantees $-10^{9} \le \text{grid}[r][c] \le 10^{9}$, so `-1000000000` occupies 11 characters while `1000000000` occupies 10 | Count magnitude digits first, then add one for a negative sign |
| Several entries sharing the largest width, as in column 1 | Report "the" longest entry, or invent a tie-break | The output contains widths only, so a tie is already resolved by the value itself | Return the width; tie-breaking has no observable effect |
| A column won in a different row than its neighbour | Assume one global winning row for the whole grid | Column 0 is won at row 0, while column 2 is first won at row 1 | Track one independent running best per column |

The first two rows of that table separate a correct solution from a plausible-looking wrong one. The negative-sign rule also explains why a column's widths cannot be inferred from a sorted list of its values: within one sign class, larger magnitude means weakly more digits, but the sign class shifts the entire measurement by one, so a small negative can out-measure a large positive.

## 7. Time and auxiliary space complexity

Let $V = \max_{r,c} \lvert \text{grid}[r][c] \rvert$ be the largest magnitude appearing in the grid.

**Time.** The sweep touches each of the $m n$ entries exactly once, and the work per entry is the cost of producing its measurement $W$, which requires materializing the decimal representation of a number of magnitude at most $V$. That costs $\Theta(\log_{10} V)$ character operations, so the running time is $O(m n \log_{10} V)$. Under the stated bound $-10^{9} \le \text{grid}[r][c] \le 10^{9}$ every entry occupies at most 11 characters, which makes the bound $O(m n)$ with a small constant. The sweep is linear in the number of cells and never sorts a column, which would cost $O(n m \log m)$ for no benefit.

**Auxiliary space.** The output array holds one integer per column, so $O(n)$ is both necessary and sufficient. Beyond it, the method needs one accumulator per column — already present in that array — and one transient decimal representation of at most 11 characters, which is $O(1)$ under the value bound. The tables earlier in this lesson stored the width of every entry for clarity; a real computation never has to, because the maximum of a set can be folded while the set is streamed.
