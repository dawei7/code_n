# Guided Example: Split Message Based on Limit

## 1. The packaging rules and the instance we trace

The instance traced here is the official first example:
$message = \texttt{"this is really a very awesome message"}$ with $limit = 9$, whose
expected result is an array of $14$ parts. The message has $n = 37$ characters, counted
including its six spaces.

The packaging rules are unusual enough to restate precisely, because all the difficulty
lives in them. The message is cut into $k$ consecutive pieces; piece $j$ carries the suffix
`<j/k>`, where $j$ runs from $1$ to $k$; every piece **including its suffix** must have
length exactly $limit$, except the last piece, which may be shorter; and stripping the
suffixes and concatenating the pieces in order must reproduce `message` exactly, spaces
included. Among all legal packings we must return the one with the **fewest** pieces, or an
empty array when no packing exists.

| Quantity | Meaning in this instance |
|:---|:---|
| $n$ | $37$, the number of characters that must be transported |
| $limit$ | $9$, the fixed total length of every full piece |
| $k$ | the number of pieces, unknown and to be minimised |
| $d(x)$ | the number of decimal digits of $x$, so $d(9) = 1$ and $d(14) = 2$ |
| suffix of piece $j$ | the literal text `<j/k>`, of length $3 + d(j) + d(k)$ |
| payload of piece $j$ | the message characters carried by piece $j$ |

Two features of the suffix deserve attention. It always contributes the two angle brackets
and the slash, so its length is at least $3 + 1 + 1 = 5$; and its length **depends on $k$**,
because both the part index $j$ and the total $k$ are written in decimal. The suffix grows
when the part count crosses $9 \to 10$, and that single growth event is what makes this
problem hard.

## 2. The suffix budget: where every character of a piece goes

Fix a candidate part count $k$. Piece $j$ has suffix `<j/k>`, so it can carry at most

$$
\text{cap}_j = limit - \bigl(3 + d(j) + d(k)\bigr)
$$

payload characters, and the total payload capacity of all $k$ pieces is

$$
C(k) = \sum_{j=1}^{k} \text{cap}_j
= limit \cdot k - \Bigl(3k + \sum_{j=1}^{k} d(j) + k \cdot d(k)\Bigr).
$$

The three subtracted terms have clear meanings: $3k$ pays for the brackets and slash of
every piece, $\sum_j d(j)$ pays for the digits of the part indices, and $k \cdot d(k)$ pays
for the digits of the part count repeated in every suffix. A packing into $k$ pieces exists
exactly when this capacity is enough to hold the whole message, that is, when

$$
C(k) \ge n .
$$

This is a necessary condition because the payloads must concatenate to `message`, so their
lengths must sum to exactly $n$ and cannot exceed their capacities. It is also sufficient,
and section 4 shows the filling procedure that witnesses it.

| Part count $k$ | $d(k)$ | Index digit cost $\sum_{j \le k} d(j)$ | Count digit cost $k \cdot d(k)$ | Bracket cost $3k$ | Total suffix cost | Capacity $limit \cdot k$ | Payload capacity $C(k)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 9 | 1 | 9 | 9 | 27 | 45 | 81 | 36 |
| 10 | 2 | 11 | 20 | 30 | 61 | 90 | 29 |
| 11 | 2 | 13 | 22 | 33 | 68 | 99 | 31 |
| 12 | 2 | 15 | 24 | 36 | 75 | 108 | 33 |
| 13 | 2 | 17 | 26 | 39 | 82 | 117 | 35 |
| 14 | 2 | 19 | 28 | 42 | 89 | 126 | 37 |

The last three rows contain the whole drama of this instance. With $k = 13$ the pieces can
carry only $35$ characters while the message needs $37$, so $13$ pieces are impossible. With
$k = 14$ the capacity is exactly $37$ — a perfect fit, with no slack at all. Note also that
the digit jump from $k = 9$ to $k = 10$ costs the packing $7$ payload characters: capacity
falls from $36$ to $29$ even though ten more total length was added.

## 3. Scanning part counts in increasing order

Because the answer must use the fewest pieces, the natural search tries
$k = 1, 2, 3, \dots$ and stops at the first feasible value. The table below performs that
scan on the traced instance.

| $k$ | $d(k)$ | Suffix cost | Capacity $9k$ | Payload capacity $C(k)$ | $C(k) \ge 37$? | Verdict |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 1 | 5 | 9 | 4 | no | rejected |
| 2 | 1 | 10 | 18 | 8 | no | rejected |
| 3 | 1 | 15 | 27 | 12 | no | rejected |
| 4 | 1 | 20 | 36 | 16 | no | rejected |
| 5 | 1 | 25 | 45 | 20 | no | rejected |
| 6 | 1 | 30 | 54 | 24 | no | rejected |
| 7 | 1 | 35 | 63 | 28 | no | rejected |
| 8 | 1 | 40 | 72 | 32 | no | rejected |
| 9 | 1 | 45 | 81 | 36 | no, short by $1$ | rejected |
| 10 | 2 | 61 | 90 | 29 | no | rejected |
| 11 | 2 | 68 | 99 | 31 | no | rejected |
| 12 | 2 | 75 | 108 | 33 | no | rejected |
| 13 | 2 | 82 | 117 | 35 | no, short by $2$ | rejected |
| 14 | 2 | 89 | 126 | 37 | yes, exactly | **accepted** |

The first feasible part count is $k = 14$, so $14$ is the minimum and the scan stops there.
The row for $k = 9$ is the one worth remembering: it fails by a single character, and the
temptation is to conclude that capacity grows with $k$ so the next candidates will be
closer. They are not — the very next candidate has *less* capacity than $k = 9$.

## 4. Filling the pieces once the count is fixed

With $k = 14$, every suffix `<j/14>` has length $3 + d(j) + 2$. For $j \le 9$ that is
$6$ characters and the payload capacity is $3$; for $10 \le j \le 14$ the suffix is
$7$ characters and the capacity is $2$. The fill walks the message from left to right and
gives each piece as much as it can hold, leaving the remainder for the later pieces.

| Piece $j$ | Suffix | Suffix length | Payload capacity | Payload taken | Message positions | Cumulative payload | Resulting piece |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `<1/14>` | 6 | 3 | 3 | 1–3 | 3 | `thi<1/14>` |
| 2 | `<2/14>` | 6 | 3 | 3 | 4–6 | 6 | `s i<2/14>` |
| 3 | `<3/14>` | 6 | 3 | 3 | 7–9 | 9 | `s r<3/14>` |
| 4 | `<4/14>` | 6 | 3 | 3 | 10–12 | 12 | `eal<4/14>` |
| 5 | `<5/14>` | 6 | 3 | 3 | 13–15 | 15 | `ly <5/14>` |
| 6 | `<6/14>` | 6 | 3 | 3 | 16–18 | 18 | `a v<6/14>` |
| 7 | `<7/14>` | 6 | 3 | 3 | 19–21 | 21 | `ery<7/14>` |
| 8 | `<8/14>` | 6 | 3 | 3 | 22–24 | 24 | ` aw<8/14>` |
| 9 | `<9/14>` | 6 | 3 | 3 | 25–27 | 27 | `eso<9/14>` |
| 10 | `<10/14>` | 7 | 2 | 2 | 28–29 | 29 | `me<10/14>` |
| 11 | `<11/14>` | 7 | 2 | 2 | 30–31 | 31 | ` m<11/14>` |
| 12 | `<12/14>` | 7 | 2 | 2 | 32–33 | 33 | `es<12/14>` |
| 13 | `<13/14>` | 7 | 2 | 2 | 34–35 | 35 | `sa<13/14>` |
| 14 | `<14/14>` | 7 | 2 | 2 | 36–37 | 37 | `ge<14/14>` |

All $37$ characters are consumed and every piece reaches the full length $9$, which is what
an exactly-satisfied capacity bound predicts. The spaces at positions $5$, $8$, $13$, $15$,
$22$ and $30$ are payload characters like any other: the piece `ly <5/14>` ends with the
space between `really` and `a`, and the piece ` aw<8/14>` begins with the space between
`very` and `awesome`. Suffix removal and concatenation therefore reproduce the message
exactly, as required.

A second, smaller instance shows what slack looks like. For
$message = \texttt{"short message"}$ and $limit = 15$ we have $n = 13$; the scan rejects
$k = 1$, whose payload capacity is $15 - 5 = 10$, and accepts $k = 2$, whose capacity is
$30 - 10 = 20$.

| Piece $j$ | Suffix | Payload capacity | Payload taken | Remaining message | Resulting piece | Piece length |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | `<1/2>` | 10 | 10 | `age` | `short mess<1/2>` | 15 |
| 2 | `<2/2>` | 10 | 3 | empty | `age<2/2>` | 8 |

Only the last piece is allowed to be short, and here it is: length $8 \le 15$. Every piece
before it is exactly $15$ characters.

## 5. Why the scan cannot be replaced by binary search

Capacity $C(k)$ is *not* monotone in $k$. Two forces oppose each other:
$limit \cdot k$ grows linearly, while the digit costs jump discontinuously whenever the part
count reaches a new power of ten and add $k$ extra characters to every suffix. The instance
$message = \texttt{"abbababbbaaa aabaa a"}$ with $limit = 8$ and $n = 20$ makes the effect
unmistakable.

| $k$ | Index digit cost | Count digit cost | Bracket cost | Suffix cost | Capacity $8k$ | Payload capacity | $C(k) \ge 20$? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 6 | 6 | 6 | 18 | 30 | 48 | 18 | no |
| 7 | 7 | 7 | 21 | 35 | 56 | 21 | **yes** |
| 8 | 8 | 8 | 24 | 40 | 64 | 24 | yes |
| 9 | 9 | 9 | 27 | 45 | 72 | 27 | yes |
| 10 | 11 | 20 | 30 | 61 | 80 | 19 | no |
| 11 | 13 | 22 | 33 | 68 | 88 | 20 | **yes** |
| 12 | 15 | 24 | 36 | 75 | 96 | 21 | yes |

Feasibility is true at $k = 7$, stays true through $k = 9$, becomes false at $k = 10$, and
returns to true at $k = 11$. A binary search over $k$ would sample the middle, see a
feasible or infeasible answer, and discard the wrong half. Only a strictly increasing scan
that stops at the first feasible $k$ is safe here — and it is also exactly what the
"fewest parts" requirement asks for.

## 6. Why the reasoning is correct

The invariant used by the acceptance test is a capacity identity:

> For every candidate part count $k$, the packing that fills each piece greedily and leaves
> the remainder to the later pieces succeeds **if and only if** $C(k) \ge n$, and it then
> produces pieces of length exactly $limit$ for every piece except possibly the last.

For **necessity**, suppose a legal packing into $k$ pieces exists. Each piece $j$ has the
fixed suffix `<j/k>`, so its payload is at most $\text{cap}_j$, and the payloads must
concatenate to the message, so $\sum_j \text{payload}_j = n$. Hence
$n \le \sum_j \text{cap}_j = C(k)$, and an infeasible capacity genuinely rules the packing
out.

For **sufficiency**, suppose $C(k) \ge n$ and let $R_j$ be the number of message characters
remaining before piece $j$ is filled. The claim maintained across the fill is
$R_j \le \sum_{i \ge j} \text{cap}_i$. It holds at $j = 1$ by the assumed capacity bound.
Piece $j$ takes $\min(\text{cap}_j, R_j)$ characters; if it takes all of its capacity, then
$R_{j+1} = R_j - \text{cap}_j \le \sum_{i > j} \text{cap}_i$, and if it takes the remaining
$R_j$ characters, then $R_{j+1} = 0$ and the message is finished. The claim therefore holds
at every piece, so no piece is ever asked for more characters than it can hold, and the
message is consumed exactly at or before piece $k$. In the second case the last piece used
is shorter than $limit$; in the first case it is exactly $limit$ — never longer, because the
bound forces $R_k \le \text{cap}_k$.

Finally, minimality is genuine. The scan tests $k = 1, 2, 3, \dots$ in increasing order and
returns the first $k$ with $C(k) \ge n$; by necessity no smaller $k$ admits any packing, and
by sufficiency this $k$ does. The scan stops at $k = n$, because a minimum packing cannot
leave a piece with an empty payload: such a piece contributes nothing to the message, and
its slot could be removed while the neighbouring pieces absorb its characters, giving a
packing with fewer parts. Every piece of a minimum packing therefore carries at least one of
the $n$ message characters, so $k \le n$ and no candidate beyond $n$ can ever be minimal.
When the whole scan finds nothing, the capacity condition $C(k) \ge n$ fails, and in every
such instance the failure is provable rather than incidental: for `"abc"` with $limit = 5$
every suffix is at least $5$ characters long, so $C(k) \le 0 < 3$ for all $k$; for
`"abcdefghij"` with $limit = 6$ the capacity is $k$ for $k \le 9$ and strictly negative for
every $k \ge 10$, so its maximum over all counts is $9 < 10$. Reporting the empty array is
correct in those cases, and the capacity formula is what proves it.

## 7. Boundary and trap analysis

| Situation | Instance | Trap | What actually happens | Outcome |
|:---|:---|:---|:---|:---|
| Suffix alone fills the limit | `"abc"`, $limit = 5$ | expect a one-piece answer because the message is tiny | the suffix `<1/1>` is $5$ characters, so the payload capacity is $0$ for $k = 1$ and non-positive for every $k \ge 10$ | `[]` |
| Ten characters, limit six | `"abcdefghij"`, $limit = 6$ | expect ten one-character pieces | for $k \le 9$ the capacity is exactly $k$ characters, so ten pieces are needed; at $k = 10$ the two-digit suffixes cost $6$ characters each and the capacity turns negative | `[]` |
| Single character | `"a"`, $limit = 6$ | expect the suffix to be too long to fit anything | suffix `<1/1>` is $5$ characters, leaving exactly one payload character | `["a<1/1>"]` |
| One piece, plenty of room | `"ttt"`, $limit = 9$ | split into several pieces because there is room | fewer pieces are always preferred; one piece holds all three characters plus `<1/1>` | `["ttt<1/1>"]` |
| Exact capacity | the traced instance, $k = 14$ | expect the last piece to be shorter | capacity equals $n$ exactly, so every piece is full length $9$ | all pieces length `9` |
| Slack capacity | `"short message"`, $limit = 15$ | expect every piece to be full length | capacity exceeds $n$, so the last piece is shorter | last piece length `8` |
| Repeated spaces | `"keep  two spaces"`, $limit = 9$ | normalise or split on whitespace | spaces are ordinary characters; the piece `  tw<2/4>` starts with two consecutive spaces | four pieces |
| Non-monotone capacity | `"abbababbbaaa aabaa a"`, $limit = 8$ | binary-search the part count | feasible at $k = 7, 8, 9$, infeasible at $k = 10$, feasible again at $k = 11$ | first feasible $k = 7$ |

The last row and the second row are the two traps that decide whether a solution passes.
Splitting on whitespace destroys the answer because spaces belong to the payload. Assuming
capacity grows with the part count destroys the answer at every power of ten, where the
suffixes grow by one digit for the part count **and** the part indices.

## 8. Alternatives and why the scan is preferred

| Approach | Idea | Cost | Failure mode or tradeoff |
|:---|:---|:---|:---|
| Enumerate all cut positions | choose any subset of the $n - 1$ gaps as piece boundaries and test each packing | exponential in $n$ | hopeless for $n$ up to $10^{4}$; the suffixes also depend on the count, so nothing can be precomputed per gap |
| Binary search on the part count | exploit the apparent monotonicity of "capacity grows with $k$" | $O(\log n)$ capacity tests | wrong: capacity drops at every power of ten, as the $k = 9 \to 10$ and $k = 10 \to 11$ rows show, so a bisection can discard the minimal feasible count |
| Solve a closed-form inequality for $k$ | treat $d(k)$ as a constant and invert $limit \cdot k - (3 + 2d(k))k \ge n$ analytically | constant per digit-length case | correct only if each digit-length case is solved and the smallest resulting $k$ is verified; more algebra than the linear scan, with off-by-one risk at the case boundaries |
| Increasing scan with a running digit sum | keep $\sum_{j \le k} d(j)$ incrementally and test $C(k) \ge n$ for $k = 1, 2, 3, \dots$ | $O(n \log n)$ time | the method used here: it tests exactly the counts the problem must consider, in the order that guarantees minimality |
| Scan then fill from the raw message | after finding $k$, walk the message with a cursor and cut `limit - len(tail)` characters per piece | $O(n)$ after the scan | this is the second half of the method; no extra structure is needed because the pieces are produced in order |

## 9. Complexity: time and auxiliary space

Let $n$ be the length of `message` and $limit$ the piece length.

**Time.** The scan examines candidate part counts $1, 2, \dots$ until one is feasible, and it
never needs to look beyond $k = n$, because no packing can use more pieces than the message
has characters. Each candidate costs one addition to the running digit sum
$\sum_{j \le k} d(j)$, one digit-length computation for $k$, and a constant number of
arithmetic operations. Digit lengths are $O(\log k)$, so the scan is
$O(n \log n)$ in the worst case, where every candidate up to $n$ is tested. The fill then
consumes the message once, copying $n$ payload characters and appending $k \le n$ suffixes,
which is $O(n)$ work; the pieces are produced in a single left-to-right pass. The dominated
total is $O(n \log n)$ time, and for $n \le 10^{4}$ that is a few tens of thousands of
operations. Recognising that the scan must be linear rather than logarithmic costs nothing
here: even the full linear scan is far below the limit.

**Auxiliary space.** Apart from the returned array of pieces, the scan keeps a constant
number of counters: the running digit sum, the current capacity, and the cursor used during
the fill. The auxiliary space is therefore $O(1)$. The returned array itself holds $k$
pieces whose combined length is $\sum_j (\text{payload}_j + 3 + d(j) + d(k)) = n + O(k \log k)$
characters, so the output occupies $O(n \log n)$ space in the worst case; that is the size of
the required answer rather than working memory, and it is unavoidable because every part must
carry its own suffix.