# Guided Example: Concatenate the Name and the Profession

This is a single-relation reporting task. One table supplies every row, one
expression builds a new text value per row, and one ordering clause fixes the
sequence in which those rows appear. There is no join, no aggregation, and no
filtering, so the entire lesson is about getting three things exactly right: the
shape of the assembled string, the length and content of the result set, and the
sort direction.

## 1. The source relation

The table `Person` has three columns and, crucially, `person_id` is its primary
key, meaning the column holds unique values. That uniqueness is not decoration:
it is what makes the requested ordering a total order with no ties, so the
result is uniquely determined rather than one of several acceptable permutations.

| Column | Role | Type | Key property |
|:---|:---|:---|:---|
| `person_id` | identifies the person and drives the output order | integer | primary key: unique per row |
| `name` | the text that opens every output value | text | may itself contain spaces |
| `profession` | the source of the single letter that closes the value | enumeration | one of six fixed labels |

The output has exactly two columns, and the second one is confusingly also named
`name`: it holds the newly assembled text, not the original name. The first
column carries `person_id` through unchanged.

## 2. The representative instance

The official example supplies six people, listed here in the order the rows are
given. Note that the given order is neither ascending nor descending in
`person_id`.

| Given row position | `person_id` | `name` | `profession` |
|:---:|:---:|:---|:---|
| 1 | 1 | Alex | Singer |
| 2 | 3 | Alice | Actor |
| 3 | 2 | Bob | Player |
| 4 | 4 | Messi | Doctor |
| 5 | 6 | Tyson | Engineer |
| 6 | 5 | Meir | Lawyer |

| Required output position | `person_id` | assembled `name` |
|:---:|:---:|:---|
| 1 | 6 | Tyson(E) |
| 2 | 5 | Meir(L) |
| 3 | 4 | Messi(D) |
| 4 | 3 | Alice(A) |
| 5 | 2 | Bob(P) |
| 6 | 1 | Alex(S) |

## 3. Assembling one value from four pieces

Each output value is the concatenation of exactly four pieces, in this order:

1. the person's `name` text, unchanged;
2. one opening parenthesis, as a literal character;
3. the first character of `profession`;
4. one closing parenthesis, as a literal character.

Written as a relation between strings, the transformation is

$$
\text{out}(r) = \text{name}(r) \;\oplus\; \text{"("} \;\oplus\; \text{first}\bigl(\text{profession}(r)\bigr) \;\oplus\; \text{")"},
$$

where $\oplus$ denotes string concatenation — juxtaposition with no separator
inserted. Because no separator is added, the length of every output value obeys
the exact identity

$$
\bigl\lvert \text{out}(r) \bigr\rvert = \bigl\lvert \text{name}(r) \bigr\rvert + 3 .
$$

That identity is the cheapest self-check available: it fails immediately if a
space is left before the parenthesis or if one of the parentheses is dropped.

| `person_id` | `name` text | `profession` | First character | Assembled value | Length check |
|:---:|:---|:---|:---:|:---|:---:|
| 1 | Alex | Singer | S | Alex(S) | $4 + 3 = 7$ |
| 3 | Alice | Actor | A | Alice(A) | $5 + 3 = 8$ |
| 2 | Bob | Player | P | Bob(P) | $3 + 3 = 6$ |
| 4 | Messi | Doctor | D | Messi(D) | $5 + 3 = 8$ |
| 6 | Tyson | Engineer | E | Tyson(E) | $5 + 3 = 8$ |
| 5 | Meir | Lawyer | L | Meir(L) | $4 + 3 = 7$ |

## 4. The enumerated profession fixes every first letter

`profession` is not free text. It is an enumeration whose complete domain has
six labels, which means the mapping from profession to first character is a
fixed, finite table rather than a property that has to be discovered per row.

| Profession label | First character | Reasoning |
|:---|:---:|:---|
| Doctor | D | the label's leading character |
| Singer | S | the label's leading character |
| Actor | A | the label's leading character |
| Player | P | the label's leading character |
| Engineer | E | the label's leading character |
| Lawyer | L | the label's leading character |

Two consequences follow. First, the six first characters are pairwise distinct,
so the letter fully identifies the profession in this instance — though the
specification never relies on that, and the mapping must not be implemented by
inverting it. Second, because the domain has no empty label, the "first
character" extraction is always defined; there is no row for which the
parentheses must be empty or the value must be null. No null-handling branch is
required by the contract.

## 5. Ordering by `person_id` descending

The output is required to be ordered on `person_id` in descending order, and
descending means the largest identifier comes first. Sorting the six
identifiers $1, 3, 2, 4, 6, 5$ in decreasing order gives
$6 > 5 > 4 > 3 > 2 > 1$, so the given row order is completely discarded.

| Descending rank | `person_id` | Given row position it came from | Assembled value |
|:---:|:---:|:---:|:---|
| 1 | 6 | 5 | Tyson(E) |
| 2 | 5 | 6 | Meir(L) |
| 3 | 4 | 4 | Messi(D) |
| 4 | 3 | 2 | Alice(A) |
| 5 | 2 | 3 | Bob(P) |
| 6 | 1 | 1 | Alex(S) |

Because `person_id` is a primary key, no two rows share an identifier, so no
tie-breaking rule is needed and the descending order is total. A solution that
merely reverses the input order would produce the wrong sequence here: the input
starts with identifiers 1, 3, 2, so reversing it yields 5, 6, 4, 2, 3, 1, which
is not sorted at all.

## 6. Correctness of the three required properties

The specification asks for a result table with a particular shape, particular
content, and a particular sequence. Each property can be stated as an invariant
and checked independently.

**Cardinality invariant.** No clause removes or duplicates rows: the projection
reads one relation with a unique key, applies only row-local string operations,
and performs no join. Therefore the result has exactly as many rows as `Person`,
and the multiset of `person_id` values in the output equals the set of
`person_id` values in the input. In the traced instance, six input rows produce
six output rows — a count that would change only if the query were wrong.

**Format invariant.** For every output row there is a source row with the same
`person_id`, and its assembled text equals that row's `name` followed
immediately by an opening parenthesis, the profession's first character, and a
closing parenthesis. This is a local property: it can be verified row by row
without inspecting any other row, which is exactly why the four-piece
decomposition in Section 3 is a complete description of the transformation.

**Order invariant.** The sequence of `person_id` values in the result is
strictly decreasing. Strictness follows from uniqueness: if two rows shared an
identifier, "descending" would leave their relative order unspecified, and the
result would not be uniquely defined. The traced ordering $6,5,4,3,2,1$ is
strictly decreasing, so it satisfies the requirement, and uniqueness of the key
makes it the only sequence that does.

Taken together, the three invariants pin down the answer exactly: the right
number of rows, the right text in each, and the right sequence. A cardinality
check plus a format spot-check plus an order check is therefore a complete
verification procedure for this problem, with no need to reason about anything
global.

## 7. Boundary conditions the instance exposes

| Situation | Correct output | Why it is a trap |
|:---|:---|:---|
| A name such as `Mary Jane` that already contains a space | Mary Jane(L) | the internal space belongs to the name and must survive; only the boundary between name and parenthesis is space-free |
| A single-row table | one row, unchanged by the ordering | sorting a one-element sequence is invisible, so an ordering bug cannot be detected here |
| Identifiers 100, 55 and 1 | ordered 100, 55, 1 | ordering is numeric, not lexicographic; text ordering would put 55 before 100 |
| Identifiers that are far apart or non-consecutive | still ranked purely by value | the rank is not the identifier, and gaps must not shift anything |
| A very short name such as `X` | X(A) | the assembled value can be shorter than the parentheses plus a letter, so no fixed-width padding is allowed |
| Two people with the same `name` text | two separate output rows | rows are identified by key, never by name, so equal names must not be merged |
| A person whose profession is the last enum label, `Lawyer` | the closing letter is L | the enum's order in the domain listing has nothing to do with the letter; it is not a position or index |

The authored cases confirm these boundaries directly. A table holding only
`person_id` 42 with the name `Ava` and the profession `Doctor` yields the single
value `Ava(D)`. A table whose rows arrive as 2, 10, 5 yields 10, 5, 2 — the
input order is irrelevant. And the pair `Mary Jane` with `Lawyer` alongside `Bo`
with `Engineer` yields `Bo(E)` before `Mary Jane(L)`, with the internal space of
the longer name preserved intact.

## 8. Complexity: time and auxiliary space

Let $n$ be the number of rows in `Person` and let

$$
L = \sum_{r \in \texttt{Person}} \bigl\lvert \text{out}(r) \bigr\rvert
$$

be the total number of characters in the assembled output column. The projection
touches each row once and writes a string of length
$\lvert \text{name}(r) \rvert + 3$, so producing the text costs
$O\!\left(\sum_r \lvert \text{name}(r) \rvert\right) \subseteq O(L)$, which is
linear in the output size — no algorithm can do better, since every output
character must be written.

The ordering clause is the only superlinear part. A comparison sort over $n$
rows costs $O(n \log n)$ comparisons on the key `person_id`. That cost disappears
in the common case where the primary key has a descending index: the storage
engine can then walk the index backwards and the ordering is free, leaving
$O(L)$ total work.

Auxiliary space is $O(n)$ rows for the materialised result plus the characters of
the assembled text, i.e. $O(n + L)$ in total, and $O(\log n)$ to $O(n)$
additional working memory for the sort depending on the algorithm the engine
chooses. Nothing here is recursive and no intermediate relation is built.

| Implementation choice | Time | Auxiliary space | Trade-off |
|:---|:---:|:---:|:---|
| Assemble with a concatenation function, order on the primary key | $O(L) + O(n \log n)$ | $O(n + L)$ | direct expression of the four-piece rule; the function's null-swallowing behaviour must be kept in mind |
| Assemble with the standard two-operand text-join operator | $O(L) + O(n \log n)$ | $O(n + L)$ | identical plan; an explicit cast of the enum to text may be required by stricter engines |
| Extract the first character with a position-and-length substring | $O(L) + O(n \log n)$ | $O(n + L)$ | most portable across engines; the length argument must be 1 or the whole tail is returned |
| Extract with a left-most-characters function | $O(L) + O(n \log n)$ | $O(n + L)$ | shortest form, but not every engine exposes this exact name |
| Assemble in the application layer after selecting the raw columns | $O(L) + O(n \log n)$ | $O(n + L)$ | moves formatting out of the report and risks losing the required ordering if the client re-sorts |

Which text function is used is a portability question, not a complexity question:
all the variants above perform one pass over the rows and one ordering, and they
differ only in engine support and in how they treat a null operand. The
enumeration guarantees a non-null, non-empty profession, so that difference does
not arise here, and the substance of the problem is the four-piece format
identity, the exact row count, and the strictly descending key order.