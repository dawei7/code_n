# Guided Example: Number of Substrings With Fixed Ratio

## 1. From a Ratio to a Cross-Multiplication

A substring `s[i .. j]` qualifies when the number of zeros in it, call it $z$, and the number of
ones, call it $o$, satisfy

$$
\frac{z}{o} = \frac{\text{num1}}{\text{num2}}.
$$

Division is the wrong tool for an exact count: $o = 0$ makes it undefined, and floating-point
comparison invites rounding errors. Cross-multiplying removes both problems:

$$
z \cdot \text{num2} \;=\; o \cdot \text{num1}.
$$

This is an exact integer identity, it is well defined even when one of the counts is zero, and it
is equivalent to the original ratio statement whenever $o > 0$. Since $\text{num1} \ge 1$ and
$\text{num2} \ge 1$ by the constraints, the identity also silently forbids degenerate substrings:
if $o = 0$ the identity forces $z \cdot \text{num2} = 0$, hence $z = 0$ as well, which is the empty
substring. So every matched pair of positions automatically corresponds to a **non-empty**
substring whose ratio is genuinely $\text{num1} : \text{num2}$.

Because $\text{num1}$ and $\text{num2}$ are coprime, the ratio is already in lowest terms, so a
qualifying substring must have

$$
z = t \cdot \text{num1}, \qquad o = t \cdot \text{num2}
$$

for some positive integer $t$. The possible lengths are therefore $t(\text{num1} + \text{num2})$
for $t = 1, 2, \dots$, which explains the "fixed ratio" name: the block size grows in exact
multiples rather than varying freely.

## 2. A Prefix Score That Turns Substrings into Equal Differences

Let $Z(k)$ and $O(k)$ be the numbers of zeros and ones in the prefix of length $k$, with
$Z(0) = O(0) = 0$. The counts inside `s[i .. j-1]` are the differences

$$
z = Z(j) - Z(i), \qquad o = O(j) - O(i).
$$

Substituting into the cross-multiplied identity and rearranging:

$$
\bigl(Z(j) - Z(i)\bigr)\text{num2} = \bigl(O(j) - O(i)\bigr)\text{num1}
$$

$$
\Longleftrightarrow\quad
\text{num1} \cdot O(j) - \text{num2} \cdot Z(j) \;=\; \text{num1} \cdot O(i) - \text{num2} \cdot Z(i).
$$

So define the **prefix score**

$$
P(k) \;=\; \text{num1} \cdot O(k) - \text{num2} \cdot Z(k).
$$

The derivation says exactly this: the substring `s[i .. j-1]` is a ratio substring if and only if
$P(i) = P(j)$. Counting ratio substrings is therefore the same as counting pairs of equal values in
the sequence $P(0), P(1), \dots, P(n)$ — one scan, one frequency table, no nested loops.

Note that $P$ is a signed integer: it decreases by $\text{num2}$ on each `0` and increases by
$\text{num1}$ on each `1`. The score is a rank that measures how far the prefix has drifted from
the demanded balance, and equality of rank is what a ratio substring repairs.

## 3. Worked Trace of the Official Instance

`s = "0110011"`, $\text{num1} = 1$, $\text{num2} = 2$, expected answer `4`. Here
$P(k) = O(k) - 2\,Z(k)$.

| $k$ | `s[k-1]` | $Z(k)$ | $O(k)$ | $P(k)$ | Comment |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | — | 0 | 0 | 0 | Empty prefix, the reference score. |
| 1 | `0` | 1 | 0 | $-2$ | A zero subtracts $\text{num2} = 2$. |
| 2 | `1` | 1 | 1 | $-1$ | A one adds $\text{num1} = 1$. |
| 3 | `1` | 1 | 2 | $0$ | Score returns to the reference. |
| 4 | `0` | 2 | 2 | $-2$ | Repeats the score from $k = 1$. |
| 5 | `0` | 3 | 2 | $-4$ | First occurrence of $-4$. |
| 6 | `1` | 3 | 3 | $-3$ | First occurrence of $-3$. |
| 7 | `1` | 3 | 4 | $-2$ | Third visit to $-2$. |

Because equal scores are what matter, only the frequency of each score is needed. The scan is done
left to right, and each new prefix is counted against the prefixes already seen.

| Step $k$ | $P(k)$ | Count already stored for $P(k)$ | Answer after | Table after this step |
|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | — | 0 | $\{0 \mapsto 1\}$ |
| 1 | $-2$ | 0 | 0 | $\{0 \mapsto 1,\; -2 \mapsto 1\}$ |
| 2 | $-1$ | 0 | 0 | $\{0 \mapsto 1,\; -2 \mapsto 1,\; -1 \mapsto 1\}$ |
| 3 | $0$ | 1 | 1 | $\{0 \mapsto 2,\; -2 \mapsto 1,\; -1 \mapsto 1\}$ |
| 4 | $-2$ | 1 | 2 | $\{0 \mapsto 2,\; -2 \mapsto 2,\; -1 \mapsto 1\}$ |
| 5 | $-4$ | 0 | 2 | add $-4 \mapsto 1$ |
| 6 | $-3$ | 0 | 2 | add $-3 \mapsto 1$ |
| 7 | $-2$ | 2 | 4 | $\{-2 \mapsto 3\}$ |

The final answer is `4`. Two details are worth noticing. First, the table is seeded with
`{0 -> 1}` before the scan, because the empty prefix is itself a legitimate left endpoint; without
that seed the substring starting at index 0 could never be counted. Second, the count is added
**before** the new entry is inserted, which is what prevents a prefix from being paired with
itself and producing a phantom empty substring.

## 4. Recovering the Actual Substrings

Pairing equal scores tells us how many substrings exist; expanding the pairs tells us which. A pair
$(i, j)$ with $i < j$ corresponds to `s[i .. j-1]`.

| Score $v$ | Prefix indices with $P(k) = v$ | Pairs | Substrings | Counts $(z, o)$ |
|:---:|:---|:---:|:---|:---|
| $0$ | 0, 3 | $(0, 3)$ | `s[0..2]` = `011` | $(1, 2)$ |
| $-2$ | 1, 4, 7 | $(1, 4)$ | `s[1..3]` = `110` | $(1, 2)$ |
| $-2$ | 1, 4, 7 | $(1, 7)$ | `s[1..6]` = `110011` | $(2, 4)$ |
| $-2$ | 1, 4, 7 | $(4, 7)$ | `s[4..6]` = `011` | $(1, 2)$ |
| $-1$ | 2 | none | — | — |
| $-4$ | 5 | none | — | — |
| $-3$ | 6 | none | — | — |

Three prefixes share the score $-2$, and that single group contributes $\binom{3}{2} = 3$ substrings;
the group at score $0$ contributes $\binom{2}{2} = 1$. The total is $1 + 3 = 4$, matching the
official explanation's four intervals, including the length-6 interval whose counts are
$(2, 4) = 2 \cdot (1, 2)$ — the $t = 2$ case of the lowest-terms family.

The counts column also shows why the answer cannot be obtained by counting ratio blocks of a fixed
length: lengths of $3$ and $6$ both occur here, and in general every multiple
$t(\text{num1} + \text{num2})$ is possible.

## 5. Invariant and Correctness

**Invariant.** After processing the character at index $k-1$, the frequency table satisfies
$\text{cnt}[v] = \#\{\,i \in [0, k] : P(i) = v\,\}$, and the accumulated answer equals the number of
pairs $(i, j)$ with $0 \le i < j \le k$ and $P(i) = P(j)$.

**Preservation.** Step $k$ computes $P(k)$ from $P(k-1)$ by one addition or subtraction, then adds
$\text{cnt}[P(k)]$ to the answer. Every pair ending at $k$ has the form $(i, k)$ with $i < k$, and
the table currently holds exactly the counts of $P(0), \dots, P(k-1)$; so the addition captures all
such pairs and no others. Inserting $k$ into the table after the addition keeps the invariant for
the next step.

**Soundness.** Each counted pair yields $P(i) = P(j)$, which by Section 2 is equivalent to
$z \cdot \text{num2} = o \cdot \text{num1}$ for the substring `s[i .. j-1]`. Since
$j > i$, that substring is non-empty. Because both `num1` and `num2` are at least $1$, the identity
admits no substring with only zeros or only ones, so no counted pair is degenerate.

**Completeness.** Conversely, every non-empty ratio substring `s[i .. j-1]` has $P(i) = P(j)$ with
$i < j$, so the pair $(i, j)$ is visited exactly once — at step $j$ — and is counted then. The
bijection between ratio substrings and increasing equal-score pairs is therefore exact, so the
final total is neither an over- nor an under-count.

**No divisibility check is needed.** An alternative proof route insists that $z$ be a multiple of
$\text{num1}$ and $o$ a multiple of $\text{num2}$ before testing the ratio. That is implied by the
cross-multiplication together with coprimality, but it is never necessary to verify separately:
the equality of prefix scores already encodes both conditions at once.

## 6. Boundary Analysis

Each row is an authored case; the expected counts follow from the equal-score rule.

| Instance | `s` | `num1` : `num2` | Prefix score family | Expected | Why it is a boundary |
|:---|:---|:---:|:---|:---:|:---|
| Two-fold repetition | `0110011` | `1 : 2` | scores $0$ and $-2$ repeat | 4 | Lengths 3 and 6 both qualify; a fixed-length method would miss the long one. |
| Ratio absent | `10101` | `3 : 1` | all seven scores distinct | 0 | Hits, misses, and hits again still leave only two ones in the middle. |
| Balanced, overlapping | `0101` | `1 : 1` | $0$ appears 3 times, $-1$ twice | 4 | Equal numbers of both digits, so nested and overlapping substrings all count. |
| Only the whole string | `00111` | `2 : 3` | $0$ appears at $k = 0$ and $k = 5$ | 1 | The first and last prefixes share a score and nothing in between does. |
| Unit exceeds length | `01010` | `4 : 3` | all six scores distinct | 0 | The smallest unit block needs length 7, longer than the string. |
| Repeated unit block | `001001` | `2 : 1` | $0$ three times, $-1$ twice, $-2$ twice | 5 | Requires lengths 3 and 6 to be counted together. |
| All zeros | `000000` | `1 : 2` | $0, -2, -4, \dots$ | 0 | No ones at all, so the cross-multiplied identity can never hold for a non-empty substring. |
| Long alternation | `01010101` | `1 : 1` | $0$ five times, $-1$ four times | 16 | Frequency counting dominates: $\binom{5}{2} + \binom{4}{2} = 10 + 6$. |

The all-zeros row is the sharpest trap. A method that reasons about ratios symbolically might
imagine that a substring with zero ones is a degenerate match; the exact identity rules it out
cleanly, and the prefix score handles it without a special branch, because the score simply walks
away in one direction and never returns.

## 7. Alternatives and Their Cost

| Approach | Idea | Verdict |
|:---|:---|:---|
| Enumerate all substrings | For each pair of endpoints, count zeros and ones and test the ratio. | $O(n^2)$ or worse; at $n = 10^{5}$ this is far past the limit. |
| Fixed-length sliding window | Check windows of length $\text{num1} + \text{num2}$ only. | Wrong: longer multiples such as the length-6 match in the official instance are missed. |
| Prefix counts plus per-length skip | For each left endpoint, jump ahead by the unit block repeatedly. | Correct in principle, still $O(n^2)$ in the worst case when scores repeat heavily. |
| **Prefix score with a frequency table** | Count equal values of $P(k)$ in one pass. | Chosen method: linear time, linear space, no ratio arithmetic per substring. |
| Randomised hashing of ratios | Hash the reduced $(z, o)$ pair per window. | Adds collision risk for no gain; the exact integer identity is already cheap. |

The fixed-window rejection is the instructive one. Because `num1` and `num2` are coprime, the
*smallest* qualifying block has length $\text{num1} + \text{num2}$, but any integer multiple of that
block also qualifies, and those longer substrings are not windows of the base length. Any method
that hard-codes one window size silently loses them.

## 8. Complexity Derivation

Let $n = \lvert s \rvert$ and define
$M = \max(\text{num1}, \text{num2}) \le n$.

**Time.** The string is traversed once. Each character costs one comparison to decide whether it is
a `0` or a `1`, one increment of a counter, one multiplication-free score update (adding
$\text{num1}$ or subtracting $\text{num2}$), one table lookup, and one table insertion. All of those
are constant-time operations under the constraints, so the total is $O(n)$. There is no nested
iteration: the pairing work that would normally be quadratic is delegated to the frequency table.
Arithmetic on the score is ordinary integer addition on values bounded by $n \cdot M \le 10^{10}$,
which is well within machine integer range and does not change the operation count.

**Auxiliary space.** The only growing structure is the frequency table. The score is a signed sum of
at most $n$ steps of size $\text{num1}$ or $\text{num2}$, so it lies in
$[-n \cdot \text{num2},\; n \cdot \text{num1}]$, and at most $n + 1$ distinct scores are ever
inserted — one per prefix. The table therefore holds $O(n)$ entries in the worst case, plus $O(1)$
scalars for the two counters, the running score, and the answer. No copy of the string, no suffix
array, and no per-length bookkeeping is created.

**Practical note on the table size.** In practice the number of distinct scores is usually far
smaller than $n + 1$, because the score moves in steps that are multiples of a common unit and
revisits values often; the worst case of $O(n)$ distinct entries occurs when the score drifts
monotonically, which is exactly the case where the answer is near zero.

**Total.** $O(n)$ time and $O(n)$ auxiliary space, with a single pass over the input and a single
hash table whose size is bounded by the number of prefixes.
