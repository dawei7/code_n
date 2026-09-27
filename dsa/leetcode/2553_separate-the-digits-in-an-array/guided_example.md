# Guided Example: Separate the Digits in an Array

## 1. The Instance and the Required Outcome

Each entry of `nums` is a positive integer, and the task is to replace that entry
by its decimal digits, written left to right, keeping every block in the same
order the values occupy in `nums`. The result is a flat list of digits whose
length depends on how many digits each value happens to have.

The instance traced here is the authored mixed-width case

```text
nums = [909, 8, 70]
```

which is deliberately unhelpful to shortcuts: it mixes a three-digit value, a
one-digit value, and a two-digit value whose units digit is $0$. Its required
output is `[9, 0, 9, 8, 7, 0]`.

| Output position | Source index $i$ | `nums[i]` | Digits of `nums[i]` | Digits contributed | Positions consumed |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | `909` | 9, 0, 9 | 3 | 0-2 |
| 1 | 1 | `8` | 8 | 1 | 3 |
| 2 | 2 | `70` | 7, 0 | 2 | 4-5 |

The width of each block is $d_i = \lfloor \log_{10} \texttt{nums[i]} \rfloor + 1$,
so the answer length is $\sum_i d_i = 3 + 1 + 2 = 6$, matching the six entries
above.

## 2. Positional Value and the Direction Digits Are Produced

A positive integer has a unique decimal expansion

$$
x = \sum_{k=0}^{d-1} a_k \, 10^{k}, \qquad a_{d-1} \neq 0, \quad 0 \le a_k \le 9,
$$

where $a_k$ is the digit standing at place $k$. Place $0$ is the units position,
the largest nonzero place is $d-1$, and the digit the reader sees first is
$a_{d-1}$.

| Value $x$ | $a_2$ (hundreds) | $a_1$ (tens) | $a_0$ (units) | Reconstruction |
|:---:|:---:|:---:|:---:|:---:|
| `909` | 9 | 0 | 9 | `9*100 + 0*10 + 9 = 909` |
| `8` | — | — | 8 | `8 = 8` |
| `70` | — | 7 | 0 | `7*10 + 0 = 70` |

Division with remainder recovers the digits from the *small* place upward.
Let $r = x \bmod 10$ and $q = \lfloor x / 10 \rfloor$. The division identity
$x = 10q + r$ with $0 \le r \le 9$ forces $r = a_0$ and $q = \sum_{k \ge 1} a_k 10^{k-1}$:
the remainder *is* the units digit, and the quotient is the same numeral with its
units digit removed. Repeating the split therefore emits
$(a_0, a_1, \dots, a_{d-1})$ — least significant first, which is the reverse of
the order the answer demands. Reversal is not cosmetic; it is the step that turns
the extraction order into reading order.

## 3. Extracting Every Block

Applying the split until the remaining value is $0$ gives one short chain per
element. The table records the value before the split, the digit the split
releases, and the value left behind.

| Source `nums[i]` | Step | Value before split | Released digit `x % 10` | Value after split `x // 10` | Buffer so far (least significant first) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `909` | 1 | `909` | 9 | `90` | 9 |
| `909` | 2 | `90` | 0 | `9` | 9, 0 |
| `909` | 3 | `9` | 9 | `0` | 9, 0, 9 |
| `8` | 1 | `8` | 8 | `0` | 8 |
| `70` | 1 | `70` | 0 | `7` | 0 |
| `70` | 2 | `7` | 7 | `0` | 0, 7 |

Two details in this trace carry most of the lesson's weight. First, `909` is a
digit palindrome, so its buffer already reads correctly and would hide an
authoring mistake; the value `70` is the honest witness, because its buffer is
`0, 7` while its block must be `7, 0`. Second, the units digit of `70` is a real
digit that must be emitted. A zero is only "leading" when it sits at the front of
a written numeral, and in the buffer a released zero is just an ordinary digit
waiting to be placed.

## 4. Restoring Reading Order

Reversing each buffer converts the extraction order $(a_0, \dots, a_{d-1})$ into
the presentation order $(a_{d-1}, \dots, a_0)$. The reversal is performed per
value, before the blocks are appended, so no block can bleed into its neighbour.

| Source `nums[i]` | Buffer, least significant first | Block after reversal | Comment |
|:---:|:---:|:---:|:---|
| `909` | 9, 0, 9 | 9, 0, 9 | Palindrome: reversal is invisible here |
| `8` | 8 | 8 | A single digit is its own reversal |
| `70` | 0, 7 | 7, 0 | The released zero is a trailing digit, not a leading one |
| `405` | 5, 0, 4 | 4, 0, 5 | Author test `[10921, 405]`: reversal genuinely reorders |

The last row is included because the authored case `nums = [10921, 405]` expects
`[1, 0, 9, 2, 1, 4, 0, 5]`; emitting `5, 0, 4` would produce a different list of
the same length, which is exactly the kind of error a length check cannot detect.

## 5. Invariant, Termination, and Why the Blocks Concatenate Correctly

**The split invariant.** Immediately after releasing digit $r$ from value $x$,
the pair satisfies $x = 10\,q + r$ with $0 \le r \le 9$ and $q = \lfloor x/10 \rfloor$.
Each released digit is therefore a true positional coefficient of the original
numeral, and the value handed to the next step is the original numeral with one
fewer place. Because $x > 0$ implies $q < x$, the sequence of remaining values is
strictly decreasing, so the chain reaches $0$ after exactly
$d = \lfloor \log_{10} x \rfloor + 1$ releases and cannot loop forever. The chain
ends only at $0$: stopping one step earlier, when the remaining value first drops
below $10$, would drop the leading digit $a_{d-1}$ — for the value `8` that would
discard the only digit and emit nothing.

**The prefix invariant.** After the first $i$ values of `nums` have been handled,
the emitted list is exactly the concatenation, in index order, of the digit blocks
of `nums[0]`, `nums[1]`, …, `nums[i-1]`. The invariant holds vacuously before any
value is handled. Each step appends precisely the block of `nums[i]` — the digits
$a_{d-1}, \dots, a_0$ produced by the chain and reversal — leaving the earlier
blocks untouched, so the invariant survives. When $i$ reaches the length of
`nums`, the emitted list is the concatenation over the whole array, which is the
required answer.

| Output position | 0 | 1 | 2 | 3 | 4 | 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Digit written | 9 | 0 | 9 | 8 | 7 | 0 |
| Owning index $i$ | 0 | 0 | 0 | 1 | 2 | 2 |
| Place $k$ inside that value | 2 | 1 | 0 | 0 | 1 | 0 |

The table also separates *value identity* from *index identity*: two positions of
the output can carry the same digit, and two positions of `nums` can carry the
same value, yet each index contributes its own block. For instance, the authored
case `nums = [13, 13]` must yield `[1, 3, 1, 3]` — four digits, because both
indices are processed independently. Values are not deduplicated and digits are
not stored as a set.

## 6. Boundary Behaviour and the Traps This Instance Exposes

| Instance | Required output | What it tests |
|:---|:---|:---|
| `[5]` | `[5]` | Minimum length and minimum value; the chain runs once |
| `[10, 20, 30]` | `[1, 0, 2, 0, 3, 0]` | Trailing zeros survive; three blocks of width 2 |
| `[100000]` | `[1, 0, 0, 0, 0, 0]` | Maximum value $10^{5}$; five zero digits after the leading 1 |
| `[10921, 405]` | `[1, 0, 9, 2, 1, 4, 0, 5]` | Internal zeros keep their slots; reversal genuinely matters |
| `[13, 13]` | `[1, 3, 1, 3]` | Duplicate values are both expanded; index order is preserved |
| `[7, 1, 3, 9]` | `[7, 1, 3, 9]` | One-digit values pass through unchanged |

The specific traps worth naming:

- **Skipping the reversal.** The buffer arrives least-significant-first. Omitting
  the reversal still yields the right *length*, so a length-only check passes while
  the values are wrong; `70` is the smallest witness.
- **Filtering out zeros.** Treating `0` as absence rather than as a digit breaks
  `[10, 20, 30]` and `[100000]`, where zeros are digits in the middle and at the
  end of the numeral.
- **Terminating too early.** Halting when the quotient first reaches $0$ instead
  of when the value reaches $0$ discards the leading digit, so `[8]` would answer
  with an empty list.
- **Fusing neighbouring values.** Concatenating several integers first and then
  splitting the fused value can borrow or invent places across the seam; block
  boundaries must be respected per index.

## 7. Alternative Formulations and Their Trade-offs

| Alternative | How it works | Trade-off |
|:---|:---|:---|
| Decimal string per value | Render `nums[i]` as text and map each character to its digit value | Short and directly produces reading order, but allocates a string per value and depends on the language's integer-to-text rules |
| Concatenate all text, then map | Join the decimal texts of every value, then walk the joined text once | One pass and no per-value reversal; the seam between blocks must be a pure concatenation, and the fused text no longer identifies which index produced each digit |
| Divide by descending powers of ten | Compute $d$, then read $\lfloor x / 10^{k} \rfloor \bmod 10$ for $k = d-1, \dots, 0$ | Emits reading order without a reversal, but needs a correct digit count first, and the leading place must not be recomputed as a zero |
| Remainder chain plus reversal | Split off $a_0$ repeatedly, then reverse the collected digits | One exact integer arithmetic pass per value and no digit-count estimate; the reversal is the only ordering step and must not be omitted |

All four produce the identical answer because every one of them realises the same
positional identity for each value; they differ only in which intermediate
representation is materialised and in how the ordering is recovered.

## 8. Time and Auxiliary Space

Let $d_i$ be the number of digits of `nums[i]` and let

$$
D = \sum_{i=0}^{n-1} d_i
$$

be the total number of digits, which is exactly the length of the answer. The
remainder chain performs one release per digit of the current value, so
extraction costs $\sum_i d_i = D$ constant-time splits, and the reversals move
exactly $D$ digits in total. Scanning the array itself costs one step per value,
which is absorbed because $d_i \ge 1$ implies $D \ge n$.

- **Time:** $O(D)$. With the stated limits $1 \le \texttt{nums[i]} \le 10^{5}$ we
  have $1 \le d_i \le 6$, hence $n \le D \le 6n$ and the bound is $O(n)$ in the
  array length as well.
- **Space:** $O(D)$ for the answer, which must be returned. Excluding that output,
  the auxiliary working space is the buffer of the value currently being split,
  whose largest size is $\max_i d_i \le 6$ — a constant under these constraints —
  so the method uses $O(1)$ auxiliary space beyond the answer.