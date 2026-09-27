# Guided Example: Count Ways To Build Good Strings

## 1. The construction process and the instance we trace

The instance traced here is the official second example: $low = 2$, $high = 3$,
$zero = 1$, $one = 2$, whose expected answer is $5$. A construction starts from the empty
string and then repeatedly performs one of exactly two moves:

- append the character `'0'` exactly $zero$ times, or
- append the character `'1'` exactly $one$ times.

Any number of moves is allowed. A construction is **good** when its final length lies
between $low$ and $high$ inclusive, and the required output is the number of *different*
good strings that some construction can produce, taken modulo $10^{9} + 7$.

| Move | Character appended | Block written | Block length | Available in the traced instance |
|:---:|:---:|:---:|:---:|:---|
| zero-move | `'0'` | a solid run of `'0'` | $zero$ | length $1$ |
| one-move | `'1'` | a solid run of `'1'` | $one$ | length $2$ |

Every move contributes a fixed, positive length, so a construction is just an ordered
sequence of blocks whose lengths add up to the final length. The order of the moves is
part of the construction, and the length of the result is the sum of the block lengths —
nothing else about a move can vary.

## 2. Block sequences and strings correspond one-to-one

A construction is an ordered list of moves, but the problem counts *strings*, not lists.
The two counts agree, and the reason is worth stating carefully because it is where an
over-count would otherwise creep in.

Let a **run** be a maximal block of equal characters in a string. Take any construction and
look at its result. Whenever two consecutive moves append the same character, their blocks
merge into a single run; whenever they append different characters, a run boundary appears.
Conversely, given a constructible string, split it into runs: each run consists of one
character, and its length must be a multiple of that character's block length, so the run
splits into a uniquely determined number of blocks of the corresponding type. No run can be
split in any other way, because every block of `'0'` has the same length $zero$ and every
block of `'1'` has the same length $one$.

The correspondence is therefore a bijection: distinct move sequences produce distinct
strings, and every constructible string comes from exactly one move sequence. Counting
good strings reduces to counting ordered block sequences whose total length lies in
$[low, high]$.

The traced instance has block lengths $1$ for `'0'` and $2$ for `'1'`. Its five good
strings, each with the unique construction that produces it, are listed below.

| Good string | Length | Runs in the string | Unique construction | In the range? |
|:---:|:---:|:---|:---|:---|
| `"00"` | 2 | `"00"` | zero-move, zero-move | $2 \in [2,3]$ |
| `"11"` | 2 | `"11"` | one-move | $2 \in [2,3]$ |
| `"000"` | 3 | `"000"` | zero-move, zero-move, zero-move | $3 \in [2,3]$ |
| `"011"` | 3 | `"0"` then `"11"` | zero-move, one-move | $3 \in [2,3]$ |
| `"110"` | 3 | `"11"` then `"0"` | one-move, zero-move | $3 \in [2,3]$ |

Strings such as `"101"` are not constructible: with $one = 2$, the two isolated `'1'`
characters cannot be produced by any block, and no run of length $1$ is a legal `'1'`
block. Constructibility is a whole-string property, not a count of characters.

## 3. The length recurrence

Let $f(L)$ be the number of block sequences whose lengths sum to exactly $L$, that is, the
number of constructible strings of length $L$. The last move of such a sequence is either a
zero-move, which leaves a sequence of total length $L - zero$, or a one-move, which leaves
a sequence of total length $L - one$. Those two cases are disjoint and cover every
sequence of length $L$, so

$$
f(L) = f(L - zero) + f(L - one), \qquad f(0) = 1, \qquad f(L) = 0 \ \text{for} \ L < 0 .
$$

The base value $f(0) = 1$ counts the empty sequence. Negative arguments are impossible
lengths and contribute nothing. The required answer is the range sum

$$
\sum_{L = low}^{high} f(L) \pmod{10^{9} + 7} .
$$

The recurrence depends only on smaller lengths, so the values can be filled in increasing
order of $L$. There is no circularity: removing the final block of any sequence always
reduces the total length, and both block lengths are at least $1$.

## 4. Worked trace of the official instance

With $zero = 1$ and $one = 2$, the recurrence is $f(L) = f(L - 1) + f(L - 2)$. Only
lengths $2$ and $3$ lie inside $[low, high] = [2, 3]$, and their values are accumulated
while the rest of the table is still needed as history.

| Length $L$ | $f(L - zero) = f(L-1)$ | $f(L - one) = f(L-2)$ | $f(L)$ | $L$ inside $[2,3]$? | Contribution to the answer |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | — | — | $1$ (base) | no | $0$ |
| 1 | $f(0) = 1$ | $f(-1) = 0$ | $1$ | no | $0$ |
| 2 | $f(1) = 1$ | $f(0) = 1$ | $2$ | yes | $2$ |
| 3 | $f(2) = 2$ | $f(1) = 1$ | $3$ | yes | $3$ |

The accumulated contribution is $2 + 3 = 5$, matching the expected output. The table also
shows why lengths below $low$ still have to be computed: $f(1)$ looks useless for the
answer, but $f(3)$ cannot be produced without it. In general, every length from $0$ up to
$high$ participates in the recurrence, while only lengths from $low$ to $high$ contribute
to the sum.

## 5. A second range, and what unreachable lengths look like

A different instance makes the sparsity of the table visible. For $zero = 2$, $one = 3$ the
recurrence is $f(L) = f(L - 2) + f(L - 3)$, and the target range is $[low, high] = [5, 8]$
with expected answer $11$.

| Length $L$ | $f(L - zero) = f(L-2)$ | $f(L - one) = f(L-3)$ | $f(L)$ | $L$ inside $[5,8]$? | Contribution |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | — | — | $1$ (base) | no | $0$ |
| 1 | — | — | $0$ | no | $0$ |
| 2 | $f(0) = 1$ | $f(-1) = 0$ | $1$ | no | $0$ |
| 3 | $f(1) = 0$ | $f(0) = 1$ | $1$ | no | $0$ |
| 4 | $f(2) = 1$ | $f(1) = 0$ | $1$ | no | $0$ |
| 5 | $f(3) = 1$ | $f(2) = 1$ | $2$ | yes | $2$ |
| 6 | $f(4) = 1$ | $f(3) = 1$ | $2$ | yes | $2$ |
| 7 | $f(5) = 2$ | $f(4) = 1$ | $3$ | yes | $3$ |
| 8 | $f(6) = 2$ | $f(5) = 2$ | $4$ | yes | $4$ |

The contribution $2 + 2 + 3 + 4 = 11$ matches the expected output. The value $f(1) = 0$ is
the important row: because both block lengths are $2$ and $3$, no sequence has total length
$1$, and that zero propagates forward. A length is unreachable whenever it cannot be written
as a non-negative combination of $zero$ and $one$ using ordered terms; the extreme case is
$zero = one = 2$ with $low = high = 3$, where every reachable length is even, so the only
length in range is unreachable and the answer is $0$.

## 6. Why the counting is correct

The invariant maintained while filling the table in increasing order of $L$ is:

> For every computed length $L$, $f(L)$ equals the exact number of ordered block sequences
> of total length $L$, and therefore, by the bijection of section 2, the exact number of
> constructible strings of length $L$.

Two arguments establish it. For **soundness**, each term $f(L - zero)$ and $f(L - one)$ used
in the recurrence is a count of genuine sequences, and appending one more block of the
corresponding type to such a sequence produces a genuine sequence of total length $L$. The
two appended block types differ in the character they write, so the two families are
disjoint, and every sequence counted in $f(L)$ arises from exactly one of them. Hence
$f(L)$ never exceeds the true count. For **completeness**, take any ordered block sequence
of total length $L$ with $L > 0$. It is non-empty, so it has a final block; deleting that
block leaves a sequence of total length $L - zero$ or $L - one$ that the recurrence has
already counted exactly. Every sequence is therefore accounted for, and $f(L)$ is not
smaller than the true count. Soundness and completeness together give equality.

The final sum is then exact by construction: a string is good precisely when its length
lies in the closed interval $[low, high]$, and each length is counted once, so adding the
$f(L)$ over that interval counts each good string exactly once and counts nothing else.

## 7. Boundary and trap analysis

| Situation | Instance | Trap | What actually happens | Outcome |
|:---|:---|:---|:---|:---|
| Unit blocks | $low = high = 20$, $zero = one = 1$ | expect a modest count for length $20$ | each length has two choices, so $f(20) = 2^{20}$ | `1048576` |
| Single target length | $low = high = 3$, $zero = one = 1$ | forget that length $3$ is only one term of the sum | $f(3) = 8$ is the whole answer; every binary string of length $3$ qualifies | `8` |
| Unreachable range | $low = high = 3$, $zero = one = 2$ | expect at least one construction because $3$ is a plausible length | all reachable lengths are multiples of $2$, so $f(3) = 0$ | `0` |
| Equal block lengths | $low = 2$, $high = 4$, $zero = one = 2$ | treat the two block types as the same and count compositions of $4$ with parts of size $2$, getting $1$ | the block types are distinguished by the character they write: $f(2) = 2$, $f(3) = 0$, $f(4) = 4$ | `6` |
| Range wider than one length | $low = 4$, $high = 5$, $zero = 2$, $one = 3$ | sum only $f(high)$ | both lengths in range contribute: $f(4) = 1$ and $f(5) = 2$ | `3` |
| Minimum range | $low = high = 1$, $zero = one = 1$ | assume the empty string counts | the empty string has length $0$, which is below $low$, and the two length-$1$ strings are `"0"` and `"1"` | `2` |
| Duplicate strings from different orders | $zero = one = 1$, any length | fear that `"0"` then `"1"` and `"1"` then `"0"` collide as the same string | they produce `"01"` and `"10"`, which differ; run structure always recovers the order | no over-count |
| Large answers | any instance with a large $high$ | let counts grow without reduction | counts are reduced modulo $10^{9} + 7$ at every step | bounded values |

The most common failure on this problem is the fourth row. When $zero = one$, the two moves
have equal length but write different characters, so the sequences that use them are
different constructions of different strings; collapsing them into a single "part of size
$zero$" loses most of the answer. The fifth row is the other frequent mistake: the answer is
a *sum over a closed interval* of lengths, not the count for a single length.

## 8. Alternatives and why the length recurrence is preferred

| Approach | Idea | Cost | Failure mode or tradeoff |
|:---|:---|:---|:---|
| Enumerate block sequences | generate every ordered sequence of moves and keep those whose total length lands in $[low, high]$ | $O(2^{high})$ sequences | the count grows exponentially with the length, so it collapses long before $high = 10^{5}$ |
| Enumerate strings and test them | generate candidate binary strings and check whether each run is a multiple of the corresponding block length | $O(2^{high})$ candidates | worse than enumerating sequences and equally hopeless; most candidates are not constructible |
| Backward count from each length | count completions from a partially built prefix, branching on the next block | $O(high)$ states with memoisation | correct and equal to the forward table, but it describes the same recurrence from the other end and needs an explicit stopping rule for the "finished string" case |
| Length recurrence with a full table | fill $f(0)$ up to $f(high)$ by the two-term recurrence, then sum the range | $O(high)$ time, $O(high)$ space | the method used here: simple, exact, and comfortably fast for $high \le 10^{5}$ |
| Rolling window over the last blocks | keep only the last $one$ values of $f$, since the recurrence reaches back exactly that far | $O(high)$ time, $O(\max(zero, one))$ space | same result with less memory, but it obscures the range-sum bookkeeping and the space saving is irrelevant at this input size |

## 9. Complexity: time and auxiliary space

Let $H = high$ and let $Z = \max(zero, one)$.

**Time.** The table is filled once per length from $0$ to $H$. Computing $f(L)$ performs a
constant number of operations — two lookups, one addition, and one modular reduction — and
the range condition is tested once per length. The total work is therefore $O(H)$, that is,
linear in the upper bound of the target range. With $H \le 10^{5}$ the loop is a few hundred
thousand elementary operations. The answer does not depend on the number of strings counted,
only on the number of lengths, which is why a count of $2^{20}$ or larger costs no more than
a count of $1$.

**Auxiliary space.** The straightforward fill stores one value per length, so $O(H)$
integers, and that is what bounds the method at this input size. Because the recurrence
reaches back only $Z = \max(zero, one)$ positions, the table can be reduced to a cyclic
buffer of $Z + 1$ values, giving $O(Z)$ auxiliary space; the answer's running sum needs one
extra accumulator. Either way the space is linear in a quantity that is at most $10^{5}$, and
no structure proportional to the number of good strings is ever materialised.