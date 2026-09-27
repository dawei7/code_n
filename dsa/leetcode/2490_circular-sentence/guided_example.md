# Guided Example: Circular Sentence

## 1. Isolating the Only Characters That Matter

A sentence is a list of words separated by a single space, with no leading or trailing spaces.
Circularity is defined entirely by **word joins**:

- the last character of each word equals the first character of its next word, and
- the last character of the last word equals the first character of the first word.

Notice how much of the input the definition ignores. A word of length $m$ contributes exactly two
characters to the test — its first and its last — and its $m - 2$ interior characters are never
consulted. For a sentence of $W$ words the entire decision therefore depends on at most $2W$
characters, drawn from $2W$ positions, and the structure is a **cycle** of equalities rather than a
line: the final comparison wraps from the last word back to the first.

Write the words as $w_0, w_1, \dots, w_{W-1}$ and define

$$
h_i = \text{first character of } w_i, \qquad
t_i = \text{last character of } w_i .
$$

The definition becomes the cyclic system

$$
t_i = h_{(i+1) \bmod W} \qquad \text{for every } i \in [0, W-1].
$$

For a one-word sentence the index $(0 + 1) \bmod 1$ is $0$ again, so the condition degenerates to
$t_0 = h_0$: the word must begin and end with the same character. This is why `eetcode` is
circular while `Leetcode` is not, and it falls out of the general rule rather than needing a
separate case.

## 2. A Rotation View of the Same Condition

Collect the $W$ tail characters and the $W$ head characters into sequences:

$$
T = (t_0, t_1, \dots, t_{W-1}), \qquad
H = (h_0, h_1, \dots, h_{W-1}).
$$

The system $t_i = h_{(i+1) \bmod W}$ says precisely that $T$ equals the **left rotation** of $H$
by one position:

$$
T = (h_1, h_2, \dots, h_{W-1}, h_0).
$$

So the whole test is: rotate the head sequence once and compare it character by character with the
tail sequence. This framing clarifies two things. First, circularity is a property of the boundary
algebra alone — the rest of the sentence is a carrier. Second, the "wrap" comparison is not a
special case; it is simply the last position of the rotated sequence, which is why an
implementation that indexes with $(i + 1) \bmod W$ needs no branch for it.

Character comparison here is **case-sensitive**. Uppercase and lowercase letters are declared
different, so `A` and `a` are unequal boundary characters even though they denote the same letter
of the alphabet. A case-folding comparison would wrongly accept inputs such as `Aa aA`'s mirror
image, and more importantly it would wrongly accept sentences constructed to test this exact
distinction.

## 3. Worked Trace of the Official Circular Instance

`sentence = "leetcode exercises sound delightful"`, expected `true`. Splitting on the single space
yields four words, and only their endpoints matter:

| $i$ | Word $w_i$ | Head $h_i$ | Tail $t_i$ | Interior (never inspected) |
|:---:|:---|:---:|:---:|:---|
| 0 | `leetcode` | `l` | `e` | `eetcod` |
| 1 | `exercises` | `e` | `s` | `xercise` |
| 2 | `sound` | `s` | `d` | `oun` |
| 3 | `delightful` | `d` | `l` | `elightfu` |

The head sequence is $H = (\texttt{l}, \texttt{e}, \texttt{s}, \texttt{d})$ and the tail sequence is
$T = (\texttt{e}, \texttt{s}, \texttt{d}, \texttt{l})$. The required comparison pairs each tail with
the next head, wrapping at the end:

| Step $i$ | Tail $t_i$ | Next head $h_{(i+1) \bmod 4}$ | Join described | Equal? |
|:---:|:---:|:---:|:---|:---:|
| 0 | `e` | `e` | `leetcode` ends, `exercises` begins | yes |
| 1 | `s` | `s` | `exercises` ends, `sound` begins | yes |
| 2 | `d` | `d` | `sound` ends, `delightful` begins | yes |
| 3 | `l` | `l` | `delightful` ends, `leetcode` begins (wrap) | yes |

All four joins hold, so the answer is `true`. The rotation view confirms it directly:
$(h_1, h_2, h_3, h_0) = (\texttt{e}, \texttt{s}, \texttt{d}, \texttt{l})$, which is exactly $T$.

## 4. The Trap Instances

### 4.1 Internal joins pass but the cycle does not close

`sentence = "ab ball"`, expected `false`. Here $H = (\texttt{a}, \texttt{b})$ and
$T = (\texttt{b}, \texttt{l})$.

| Step $i$ | Tail $t_i$ | Next head | Equal? | Note |
|:---:|:---:|:---:|:---:|:---|
| 0 | `b` | `b` | yes | The only internal join is satisfied. |
| 1 | `l` | `a` | no | The wrap-around join `ball` -> `ab` fails. |

A reader who checks only the spaces in the middle of the sentence sees success and stops. The wrap
join is the join that has no visible space to remind them it exists, which is exactly why it is the
most commonly missed condition.

### 4.2 A failure that appears late

`sentence = "ab bc ce da"`, expected `false`. Here
$H = (\texttt{a}, \texttt{b}, \texttt{c}, \texttt{d})$ and
$T = (\texttt{b}, \texttt{c}, \texttt{e}, \texttt{a})$.

| Step $i$ | Tail $t_i$ | Next head $h_{(i+1) \bmod 4}$ | Equal? |
|:---:|:---:|:---:|:---:|
| 0 | `b` | `b` | yes |
| 1 | `c` | `c` | yes |
| 2 | `e` | `d` | no |
| 3 | `a` | `a` | yes |

Two joins succeed, then the third fails, and the fourth succeeds again. A short-circuiting check
must therefore be applied to **every** join; a partial scan that stops after the first couple of
matches, or one that counts matching joins and compares the count loosely, would misjudge this input.

### 4.3 Case sensitivity

`sentence = "Aa aA"`, expected `true`, is the positive control for case handling:
$T = (\texttt{a}, \texttt{A})$ and the rotated heads are $(\texttt{a}, \texttt{A})$, so both joins
match as exact characters. The negative mirror — any input where a join pairs `A` with `a` — must be
rejected, and it is rejected only if comparison is done on raw characters without normalization.

## 5. Invariant and Correctness

**Invariant of the scan.** Before examining index $i$, every join
$t_k = h_{(k+1) \bmod W}$ for $k < i$ has been verified to hold.

**Preservation.** Step $i$ compares exactly $t_i$ with $h_{(i+1) \bmod W}$ and either records a
failure or leaves the invariant intact for $i + 1$. Because the comparison uses the modular index,
the final step $i = W - 1$ compares $t_{W-1}$ with $h_0$ — the wrap join — so no join escapes
verification.

**Soundness.** If the scan reports success, then $t_i = h_{(i+1) \bmod W}$ holds for all $i$, which
is literally the definition of circularity; hence the reported `true` is correct.

**Completeness.** If the sentence is circular, every one of those $W$ equalities holds, so no step
of the scan can fail and the reported result is `true`. Conversely, on a non-circular sentence at
least one equality fails, that index is visited, and the result is `false`. The scan therefore
decides the predicate exactly, and short-circuiting on the first failure preserves correctness
because a single violated join is already a counterexample to circularity.

**Why splitting on a single space is safe.** The contract guarantees exactly one space between
consecutive words and no leading or trailing spaces, so splitting on the space character produces
precisely the word list with no empty tokens. Under a weaker contract that allowed repeated or
boundary spaces, splitting would yield empty strings, and taking their first or last character would
be undefined or would fabricate spurious matches. The guarantee is what makes the simple split a
faithful reconstruction of the word list, and it is worth stating because the method silently
depends on it.

## 6. Boundary Analysis

| Instance | `sentence` | $W$ | Join pattern | Expected | Why it is a boundary |
|:---|:---|:---:|:---|:---:|:---|
| Minimum length | `a` | 1 | $t_0 = h_0$ trivially | true | A single character is both head and tail of its word. |
| Single-word chain | `eetcode` | 1 | $t_0 = h_0 = \texttt{e}$ | true | The wrap index coincides with the word itself. |
| Repeated characters | `lll` | 1 | $t_0 = h_0 = \texttt{l}$ | true | Interior repeats are irrelevant to the test. |
| Two words | `ab ba` | 2 | `b`=`b`, `a`=`a` | true | The smallest case where the wrap join is a distinct comparison. |
| Two words, wrap fails | `ab ball` | 2 | `b`=`b`, `l`!=`a` | false | Internal success with a broken cycle. |
| Case-exact match | `Aa aA` | 2 | `a`=`a`, `A`=`A` | true | Confirms comparisons are character-exact, not case-folded. |
| Late failure | `ab bc ce da` | 4 | two passes then `e`!=`d` | false | Short-circuiting must cover the whole cycle. |
| Capital first word | `Leetcode is cool` | 3 | `e`!=`i` | false | Fails on the very first join because of the leading capital. |

The `Leetcode is cool` row is the official negative example, and it fails at index $0$: the tail of
`Leetcode` is lowercase `e` while the head of `is` is lowercase `i`. Its later joins also fail, but
the predicate is already falsified, which is precisely the situation a short-circuit is designed to
exploit.

## 7. Alternatives and Their Cost

| Approach | Idea | Verdict |
|:---|:---|:---|
| Cyclic index comparison | Compare $t_i$ with $h_{(i+1) \bmod W}$ for all $i$. | Chosen method: one pass, no branching for the wrap, no string building. |
| Single-pass over the raw sentence | Compare each space's preceding and following characters, then check the two sentence endpoints separately. | Correct and avoids building a word list, but needs an explicit end-to-end comparison that is easy to forget. |
| Rotate the head sequence and compare | Materialize $H$, rotate it, compare with $T$. | Clear but allocates two extra sequences for no benefit. |
| Duplicated sentence scan | Append a space and the sentence to itself, then look for the boundary pattern. | Works, but doubles the input and obscures which join is which. |
| Case-folded or sorted comparison | Normalize case or compare multisets of boundary characters. | Wrong: order and exact case both carry meaning here. |

The raw-sentence row is the interesting alternative because it is genuinely competitive. It avoids
the word list, but it must handle the first and last characters of the entire sentence as an extra
join, and it must be certain that a character adjacent to a space exists on both sides — which the
no-leading-or-trailing-space guarantee only just provides.

## 8. Complexity Derivation

Let $L = \lvert \text{sentence} \rvert$ and let $W$ be the number of words, with $W \le L$.

**Time.** Splitting the sentence requires one pass over the $L$ characters, $O(L)$. The join scan
performs $W$ comparisons, one per word, each of which is a constant-time character equality, so it
costs $O(W) \subseteq O(L)$. Total time is $O(L)$: each input character is touched a bounded number
of times, and the decision itself costs one comparison per join. With $L \le 500$ the whole
computation is trivially fast, but the linear bound is the honest one and would hold for any input
size.

**Auxiliary space.** The word list holds $W$ substrings whose total length is $L - (W - 1)$, so the
split representation costs $O(L)$ auxiliary space. The scan itself adds only a constant number of
indices and one comparison result, $O(1)$. A variant that scans the raw sentence in place, locating
each space and comparing the characters on either side, achieves $O(1)$ auxiliary space at the cost
of the extra endpoint comparison described in Section 7. The space is not asymptotically reducible
below $O(1)$ in either case, and it never depends on the number of joins beyond the word list.

**Answer assembly.** The result is a single boolean conjunction over $W$ predicates. Under
short-circuit evaluation it may be decided before all $W$ comparisons are performed, but the worst
case remains $O(L)$ time and the space is unchanged, since the word list is built before the scan
begins.