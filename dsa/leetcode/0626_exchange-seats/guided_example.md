# Guided Example: Exchange Seats

This lesson rearranges a classroom seating chart. Every two consecutive students
trade seats, the seat labels themselves never move, and when the class has an odd
number of students the final seat has nobody to trade with. The chosen instance
has exactly five students, which is the smallest odd class that contains two
complete pairs *and* an unpaired trailing seat, so the boundary rule is exercised
inside the same trace as the ordinary swaps.

The chart is a single relation whose identifier is the primary key, and the
identifiers always begin at $1$ and increase without gaps.

| `id` | `student` |
|:---:|:---:|
| $1$ | `Abbot` |
| $2$ | `Doris` |
| $3$ | `Emerson` |
| $4$ | `Green` |
| $5$ | `Jeames` |

| `id` | `student` |
|:---:|:---:|
| $1$ | `Doris` |
| $2$ | `Abbot` |
| $3$ | `Green` |
| $4$ | `Emerson` |
| $5$ | `Jeames` |

The answer has the same shape as the input: the same number of rows, the same
identifier column, and one name per seat. What changes is which name occupies
which seat label.

---

## 1. Seat Labels Stay Fixed, Occupants Move

The contract says to trade the *seat identifiers* of every two consecutive
students, and it also says the result must be ordered by identifier ascending.
Those two statements together pin down the only sensible reading: the output is a
seating chart indexed by seat label, so the labels $1, 2, \dots, N$ remain in
place and the occupant column is permuted.

It is worth being explicit, because the alternative reading produces a lawful
relation with the wrong meaning. If the identifier column were rewritten to hold
each student's new seat number and the rows were then sorted, the output would be
a list of students annotated with where they now sit. For this class that list
would read $2, 1, 4, 3, 5$ down the first column, which is not ordered ascending
and is not a seating chart. The task is therefore not "permute the identifier
column"; it is "look up who belongs at each seat".

| Reading | First column of the output | Is it a chart by seat label? |
|:---|:---|:---|
| Permute the identifier column | $2, 1, 4, 3, 5$ | no — the labels moved with the students |
| Keep the label and permute the occupant | $1, 2, 3, 4, 5$ | yes — each row names the student at that seat |

The lesson keeps the second reading for the rest of the trace.

## 2. The Consecutive-Pairing Is a Perfect Matching

The pairing rule cuts the seat range into consecutive blocks of two:
$\{1,2\}$, $\{3,4\}$, $\{5,6\}$, and so on. Each block is swapped internally and
no seat is swapped with a seat outside its own block. Because the blocks are
disjoint, the pairing partitions the seats that take part in a swap.

Working in one-based seat labels, the partner of seat $i$ is obtained by
subtracting one to reach the zero-based slot index $i - 1$, toggling the lowest
bit of that index so that $2m$ and $2m + 1$ exchange places, and adding one back:

$$
\pi(i) = \bigl((i - 1) \oplus 1\bigr) + 1 .
$$

The toggle is the whole mechanism. In the zero-based slots the pairs are
$(0,1)$, $(2,3)$, $(4,5)$; adding or removing one from an even slot reaches its
partner, and that is exactly what flipping the low bit does for every slot,
without any test for which side of a block the slot is on.

| Seat $i$ | Slot $i - 1$ | Low bit toggled | $\pi(i)$ | Block |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | $0$ | $1$ | $2$ | $\{1,2\}$ |
| $2$ | $1$ | $0$ | $1$ | $\{1,2\}$ |
| $3$ | $2$ | $3$ | $4$ | $\{3,4\}$ |
| $4$ | $3$ | $2$ | $3$ | $\{3,4\}$ |
| $5$ | $4$ | $5$ | $6$ | $\{5,6\}$ |

Two structural properties follow immediately and both are needed later. The
mapping is an *involution*, $\pi(\pi(i)) = i$ for every seat, because toggling the
low bit twice restores it. And it has no fixed points, because toggling the low
bit always changes the slot, so no seat is ever its own partner. A mapping with
those two properties is a permutation whose cycles all have length two, which is
precisely a pairwise exchange.

## 3. The Unpaired Trailing Seat

The formula happily produces a partner for seat $5$, namely seat $6$, but seat $6$
is not in the chart. The contract's second sentence exists exactly for this case:
when the student count is odd, the last student keeps their place. Nothing needs
to be decided about *which* seat is unpaired, because the missing partner simply
is not found during the lookup.

| Seat $i$ | Partner $\pi(i)$ | Partner present in the chart? | Occupant taken from |
|:---:|:---:|:---:|:---:|
| $1$ | $2$ | yes | seat $2$ |
| $2$ | $1$ | yes | seat $1$ |
| $3$ | $4$ | yes | seat $4$ |
| $4$ | $3$ | yes | seat $3$ |
| $5$ | $6$ | no | its own row |

That last row requires care. A lookup that finds nothing must still produce a
name, because the output has five rows and seat $5$ must be occupied. The rule is
therefore a *fallback*: the occupant of seat $i$ is the student found at the
partner seat when the partner exists, and the occupant of seat $i$ itself when it
does not. This fallback is what makes the odd-length case fall out of the general
rule instead of becoming a special branch on the last identifier.

The trace for this class is therefore:

| Seat $i$ | Source seat | Source student | Seat $i$ receives |
|:---:|:---:|:---:|:---:|
| $1$ | $2$ | `Doris` | `Doris` |
| $2$ | $1$ | `Abbot` | `Abbot` |
| $3$ | $4$ | `Green` | `Green` |
| $4$ | $3$ | `Emerson` | `Emerson` |
| $5$ | $5$ (itself, no partner) | `Jeames` | `Jeames` |

## 4. Keeping the Seat Label While Taking the Partner's Student

The remaining step is a *self-comparison* of the chart against itself: the output
projects each seat's identifier together with the occupant column drawn from the
partner row rather than from the current row. Since the partner is identified by
the computed seat label, the pairing-invariant transformation is a join of the
chart to itself on the predicate that the right-hand identifier equals the
computed partner label, with the left-hand identifier projected through
unchanged.

Three details of that formulation matter.

First, the join must be an outer join that retains the left side. An inner join
would silently drop seat $5$, because no row satisfies the pairing predicate for
an absent partner label; the outer form retains the seat and supplies nothing for
the absent partner, at which point the fallback fills in the seat's own student.
This is the single most consequential choice in the plan, and it is the only place
where the odd-length rule is enforced.

Second, the join predicate is expressed purely in terms of the left seat label, so
each seat produces exactly one output row. That keeps the output cardinality equal
to the input cardinality, which is what a permutation requires.

Third, the projected identifier column comes from the left side of the join, so
the labels stay in their original positions while the occupant column travels from
the partner row.

| Plan variant | Rows produced for this class | What goes wrong |
|:---|:---:|:---|
| Pairing join retaining the left side, with a fallback | $5$ | nothing — this is the required behaviour |
| Pairing join requiring a partner on both sides | $4$ | seat $5$ disappears, because its partner label is absent |
| Join on the equality of identifiers | $5$ | every seat pairs with itself, so no occupant moves at all |

Finally, the output ordering by identifier ascending is not cosmetic. The join
that draws occupants from partner rows has no inherent order, and the chart
meaning depends on the labels being read in sequence; ordering restores the
natural reading order.

## 5. Why the Scheme Produces a Valid Rearrangement

The pairing satisfies four properties, and together they establish that the
result is exactly the required chart.

*Every seat is accounted for.* Each seat label in $1 \dots N$ produces one output
row, because the join is driven by the left side and its predicate mentions only
the left label. The output therefore has the same height as the input.

*Every occupant appears exactly once.* The pairing is a permutation of the seats,
and a permutation is a bijection from labels to labels. Pulling the occupant
through a bijection of labels therefore moves each student to exactly one seat:
no student is duplicated across two seats and no student is lost. For this class
the four paired seats exchange in two 2-cycles and seat $5$ joins the identity
cycle, giving the cycle decomposition
$(1\ 2)(3\ 4)(5)$.

*Pairs are reciprocal.* Because the mapping is an involution, seat $1$ takes the
occupant of seat $2$ while seat $2$ takes the occupant of seat $1$. The two rows
of a block exchange rather than one of them copying the other twice. The trace
above confirms the reciprocity row by row, and it is exactly the property that
fails if the toggle is replaced by a one-directional rule such as "always look at
the next seat", which would drag `Doris` into seat $1$, `Emerson` into seat $2$,
and so on, shifting the whole chart instead of exchanging pairs.

*The unpaired seat keeps its occupant.* When the class size is even, every label's
partner exists, so the fallback is never used and all $N/2$ blocks exchange
cleanly. When the class size is odd, exactly one label has no partner — the last
one — and the fallback retains that student. Neither case needs a count of the
class or a comparison against a maximum identifier.

## 6. Traps This Instance Exposes

| Trap | Failure on this chart |
|:---|:---|
| Requiring a partner for every seat | Seat $5$ has no partner and is dropped, yielding four rows instead of five and losing `Jeames`. |
| Sorting by the student name or by the swapped identifier | The labels leave ascending order, so the output stops being a seating chart read by seat number. |
| Pairing with a one-directional rule | Occupants shift along the chart instead of exchanging inside blocks: seat $1$ takes `Doris`, seat $2$ takes `Emerson`, and no pair is reciprocal. |
| Testing for the unpaired seat with an explicit class-size count | This works but introduces a second scan of the relation and a special case for one identifier, where the partner fallback already covers it. |
| Assuming the identifiers contain no gaps | The pairing arithmetic depends on the identifiers forming a consecutive run from $1$. The contract guarantees it; a plan that ignores it would mispair seats. |
| Treating duplicate names as a special case | Two students may share a name. They still occupy two distinct rows and two distinct labels, so their seats exchange like any other pair, and the output shows the same name twice — which is correct, not a duplication bug. |

Two boundary classes are worth recording. With a single student, seat $1$ computes
partner seat $2$, finds no such row, and falls back to its own occupant, so the
chart is unchanged — the general rule already handles the smallest possible class.
With a two-student class, both labels find their partners, both fallbacks go
unused, and the two occupants exchange, which is the shortest possible pair.

## 7. Complexity Derivation

Let $R$ be the number of seats, so the class size and the row count are both $R$.
Every seat is paired with at most one partner, and each of the $R$ labels produces
exactly one output row.

Determining an occupant requires locating the partner row by its primary key. A
hash table or primary-key index answers each lookup in expected $O(1)$ time,
making the pairing step $O(R)$ expected. A general tree index would cost
$O(\log R)$ per lookup and therefore $O(R \log R)$ in total, which is the
conservative engine-independent figure. The final presentation order requires
ordering $R$ output rows, which costs $O(R \log R)$ unless an index on the
identifier already supplies the order.

| Stage | Expected cost | Conservative cost |
|:---|:---:|:---:|
| Compute the partner label for each of the $R$ seats | $O(R)$ | $O(R)$ |
| Look up the partner row by primary key | $O(R)$ | $O(R \log R)$ |
| Apply the fallback for the unpaired seat | $O(R)$ | $O(R)$ |
| Order the $R$ output rows by identifier | $O(R \log R)$ | $O(R \log R)$ |

The conservative time bound is $O(R \log R)$; with hash-based lookups and an
identifier index supplying the order, the plan runs in expected $O(R)$ time. The
parity arithmetic, the low-bit toggle, and the fallback each need only constant
working state per seat, and no stage depends on the pairing structure beyond the
per-seat lookup.

Auxiliary space is $O(R)$. The result relation materializes one row per seat, and
the join's lookup structure holds at most one entry per seat, so the working data
is linear in the class size. The pairing itself stores no state at all: the
partner label is recomputed from the current seat label whenever it is needed,
which is why the transformation needs no per-seat bookkeeping beyond the lookup.