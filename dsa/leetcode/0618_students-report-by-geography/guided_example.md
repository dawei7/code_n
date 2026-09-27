# Guided Example: Students Report By Geography

This lesson turns a narrow roster into a wide geographic report. The input names
students and the continent they came from; the answer must present three fixed
column headers — `America`, `Asia`, and `Europe`, in that order — with each
continent's students listed alphabetically down its column, and every column
starting at the top. The chosen instance is the smallest roster on which the
three lists have *different* lengths, which is exactly the case that forces the
alignment rule to be stated and defended.

The roster is a single relation with two attributes, and duplicate rows are
permitted by the contract.

| `name` | `continent` |
|:---:|:---:|
| `Jane` | `America` |
| `Pascal` | `Europe` |
| `Xi` | `Asia` |
| `Jack` | `America` |

| `America` | `Asia` | `Europe` |
|:---:|:---:|:---:|
| `Jack` | `Xi` | `Pascal` |
| `Jane` | `null` | `null` |

The instance is asymmetric on purpose: America contributes two students while
Asia and Europe each contribute one. Two output rows are therefore needed even
though only four students exist, and the shorter continents must still occupy the
first row rather than being pushed down to make room.

---

## 1. Why the Lists Cannot Be Joined on `continent`

The obvious way to describe the target shape is "one column per continent", and
the obvious way to build it is to take three copies of the roster — one per
continent — and place them side by side. That construction fails, and seeing
exactly how it fails identifies the missing ingredient.

Pairing two restricted copies of the relation on anything other than a real key
produces a Cartesian product. America has two students and Asia has one, so
combining them without a usable predicate yields $2 \times 1 = 2$ candidate
pairs. Two of those pairs are wrong in a way the answer cannot tolerate: `Jane`
would be aligned with `Xi`, a student who has no positional relationship with her
at all. The wrong pairs are not merely extra rows, they are *mismatched* rows,
because nothing in the data says that Jane and Xi occupy the same rank.

| Candidate pairing strategy | Pairs produced | Why it is wrong |
|:---|:---:|:---|
| Combine by `continent` equality | $0$ | Every America row has an America continent value and every Asia row has an Asia value, so the equality predicate can never be satisfied across the two copies. |
| Combine with no predicate at all | $4$ | Every America row pairs with every Asia and Europe row, giving $2 \times (1 + 1) = 4$ pairs, including the mismatched pairs `(Jane, Xi)` and `(Jane, Pascal)`. |
| Combine by an explicit rank | $2$ | Only positions that genuinely correspond are joined: rank $1$ with rank $1$, rank $2$ with rank $2$. |

Only the third row of that table produces the required shape. The lesson is that
the roster as given has no attribute that identifies a *position* within a
continent, and the target shape needs one.

## 2. Constructing the Ordinal Alignment Key

The missing attribute is an ordinal position inside each continent. Assigning
rank $1$ to the alphabetically first student of a continent, rank $2$ to the
second, and so on, manufactures exactly the key the pivot needs:

$$
rk(s) = \bigl\lvert \{\, t \in \text{Student} : t.\text{continent} = s.\text{continent}
\ \wedge\ t.\text{name} \preceq s.\text{name} \,\} \bigr\rvert .
$$

Ranks are computed *within* a continent and ordered by `name`, so the key is
local to each list. The alphabetically first student of America, of Asia, and of
Europe all receive the same rank $1$, even though their names are unrelated. That
shared label is what makes horizontal stitching possible: it asserts a
correspondence that the data itself does not contain.

Applying the definition to the roster gives four ranked rows.

| `name` | `continent` | Rank $rk$ |
|:---:|:---:|:---:|
| `Jack` | `America` | $1$ |
| `Jane` | `America` | $2$ |
| `Xi` | `Asia` | $1$ |
| `Pascal` | `Europe` | $1$ |

Two properties of this key carry the rest of the argument. First, it is *dense
and consecutive* inside every continent: the ranks of the $k$-th list are
exactly $1, 2, \dots, n_{\text{continent}}$, with no gaps, because each rank
counts a prefix of the alphabetically sorted list. Second, it is
*collision-free* inside every continent, so a rank value identifies at most one
student per continent.

| Continent | Length $n_{\text{continent}}$ | Rank set | Rank $1$ | Rank $2$ |
|:---:|:---:|:---:|:---:|:---:|
| `America` | $2$ | $\{1, 2\}$ | `Jack` | `Jane` |
| `Asia` | $1$ | $\{1\}$ | `Xi` | absent |
| `Europe` | $1$ | $\{1\}$ | `Pascal` | absent |

Equal values of $rk$ across continents mean "same position in that continent's
alphabetical list". Since the list lengths differ, some rank values exist for
America but for no other continent; those are precisely the cells that must
become `null`.

## 3. Assembling the Three Columns by Rank

Grouping the ranked rows by $rk$ collects one horizontal output row per position.
Inside a group, a continent contributes a name only if it is long enough to reach
that rank; otherwise it contributes nothing. Reading the two groups gives the
answer directly.

| Rank group | `America` | `Asia` | `Europe` | Assembled row |
|:---:|:---:|:---:|:---:|:---|
| $rk = 1$ | `Jack` | `Xi` | `Pascal` | `('Jack', 'Xi', 'Pascal')` |
| $rk = 2$ | `Jane` | no Asia row at rank $2$ | no Europe row at rank $2$ | `('Jane', null, null)` |

A pivot over a ragged set of lists is usually expressed as conditional
aggregation: for each target column, keep the name when the row's continent
matches that column and discard it otherwise, then collapse the group to a single
value. The collapse is safe here for a reason worth stating explicitly. After the
rank key is attached, a group identified by $rk$ contains at most one row per
continent, because ranks are collision-free within a continent. The conditional
expression therefore produces at most one non-empty candidate per column, and any
grouping operator that selects a single surviving value returns that name
unchanged. When the continent is absent from the group, every candidate in that
column is empty and the collapsed value is `null`.

The output header order `America`, `Asia`, `Europe` is a fixed property of the
answer, not of the data. It is independent of how many students each continent
contributed and independent of the input row order, so the three columns must be
projected in that declared sequence.

| Input row order | Rank of `Jack` | Rank of `Jane` | First output row |
|:---|:---:|:---:|:---|
| `Jane`, `Pascal`, `Xi`, `Jack` (as given) | $1$ | $2$ | `('Jack', 'Xi', 'Pascal')` |
| `Jack`, `Jane`, `Xi`, `Pascal` | $1$ | $2$ | `('Jack', 'Xi', 'Pascal')` |

Because the rank is defined by alphabetical order rather than by arrival order,
the answer is invariant under permutation of the input rows. That invariance is
what makes the alphabetical requirement compatible with a pivot at all.

## 4. Why the Rank-Pivot Scheme Is Correct

The construction has to satisfy three properties, and the ordinal key supplies
all three.

*Correct ordering.* Within a continent, rank order follows alphabetical order by
definition of the key, and the output presents continents' names in increasing
rank down the column. So each column is alphabetical, which is the first
requirement.

*Complete coverage.* Every roster row receives exactly one rank, and its
continent's rank set is $\{1, \dots, n_{\text{continent}}\}$ with no gaps. Hence
every student appears in exactly one group and therefore in exactly one output
cell. No student is dropped, and no student is duplicated.

*Adequate length.* The number of output rows is the largest rank value over all
continents, which is exactly $\max_{\text{continent}} n_{\text{continent}}$. Since
the ranks are dense prefixes, America — the longest continent in this instance —
fills every group with a name, so every one of the two output rows is present and
no trailing all-`null` row is emitted. A shorter continent contributes to the
first $n_{\text{continent}}$ groups and contributes nothing to the rest, which is
exactly the `null` padding the answer demands.

Uniqueness of the reduction also matters: a rank group yields one row, not one
row per student in the group, so the output has $\max_{\text{continent}} n_{\text{continent}}$ rows rather than one row per input student.

## 5. The Traps This Instance Exposes

| Trap | Consequence on this roster |
|:---|:---|
| Ordering ranks by arrival instead of by `name` | The roster lists `Jane` before `Jack`, so America's column would read `Jane` then `Jack`. The output would be in input order, not alphabetical order. |
| Counting rows instead of numbering them | A count of America's students is $2$ for both of its rows, so the two America rows would share one group and collapse into a single cell. America would lose `Jane`. |
| Joining the continent copies with no positional key | America and Asia would pair `Jane` with `Xi`, producing a mismatched row alongside the two correct ones. |
| Taking the row count as the output height | The tallest continent determines the height. Using the total student count $4$ would emit two all-`null` rows below the real answer. |
| Collapsing the columns without first ranking | Grouping rows by `continent` alone reproduces the original narrow shape: one group per continent rather than one group per position. |
| Relying on output headers folding to lower case | The required headers are exactly `America`, `Asia`, and `Europe` with their initial capitals, so a projection that normalizes identifier case would not match the required schema. |

One further boundary deserves mention because it is invisible in this instance.
Duplicate roster rows are legal, and two rows with the same name and the same
continent are two distinct students. Because ranks are assigned per row rather
than per distinct name, the duplicates receive consecutive distinct ranks and
occupy two successive cells instead of collapsing into one. The scheme needs no
special branch for that case.

## 6. Complexity Derivation

Let $R$ be the number of rows in `Student`, and let
$H = \max_{\text{continent}} n_{\text{continent}}$ be the height of the output,
so $H \le R$.

Producing the ordinal key requires ordering the roster by the pair
`(continent, name)`, which a comparison sort performs in $O(R \log R)$ time.
Once the ranks exist, the remaining work is a single pass that evaluates a
constant number of conditional expressions per dropped row and groups the rows
by $rk$; hashing the $R$ rows into groups costs $O(R)$ expected time, while a
sort-based grouping costs $O(R \log R)$. Emitting the groups requires ordering at
most $H$ result rows, which stays inside $O(R \log R)$.

| Stage | Expected cost | Sort-based cost |
|:---|:---:|:---:|
| Order the roster by `(continent, name)` and number each continent | $O(R \log R)$ | $O(R \log R)$ |
| Evaluate the conditional candidates for the three columns | $O(R)$ | $O(R)$ |
| Group by rank and collapse each group to one row | $O(R)$ | $O(R \log R)$ |
| Order the at most $H$ result groups | $O(H \log H)$ | $O(H \log H)$ |

The engine-independent bound is $O(R \log R)$ time, dominated by the ordering
step that the alphabetical requirement makes unavoidable.

Auxiliary space is $O(R)$. The ranked intermediate relation stores one row per
roster row, the grouping structure holds at most $R$ rank groups, and the output
holds $H$ rows; the three conditional expressions need only constant working
state per row. No structure in the plan grows faster than linearly in the roster
size, and the longest continent can itself hold all $R$ students.