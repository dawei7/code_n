## General

**Represent a three-row window with three aliases**

The query reads the `Logs` table three times as `l1`, `l2`, and `l3`. These are
not three different tables; they are three roles for rows in one possible
consecutive window.

The first join requires:

- `l1.id = l2.id - 1`, so the second ID immediately follows the first;
- `l1.num = l2.num`, so their logged values match.

The second join applies the same conditions from `l2` to `l3`. A joined triple
therefore consists of IDs $i,i+1,i+2$ with one common `num`.

The presence of such a triple is exactly evidence that the value appears at
least three times consecutively.

**Why three rows prove “at least three”**

A run of exactly three produces one qualifying window. A longer run also
contains at least one three-row window, so it qualifies without needing to
count the entire run.

For a run of four equal values at IDs one through four, the joins produce
windows `(1,2,3)` and `(2,3,4)`. Both prove the same value qualifies.

The query does not require the run to end after `l3`; it tests a minimum length,
not an exact length.

**Deduplicate qualifying values**

`SELECT DISTINCT l2.num AS ConsecutiveNums` returns one row per qualifying
numeric value.

`DISTINCT` is necessary for two reasons. One long run can produce overlapping
three-row windows, and the same number can have separate qualifying runs later
in the log. The required result is a set of values, not one row per witnessed
window.

Any of `l1.num`, `l2.num`, or `l3.num` could be selected because the join proves
they are equal. Choosing the middle alias communicates the center of the
three-row window.

The alias `ConsecutiveNums` exactly matches the required output column.

**Trace the sample**

IDs one, two, and three all contain one. They satisfy both ID-adjacency joins
and both value-equality predicates, producing one qualifying triple.

Later ones do not form another three-ID chain. The twos at IDs six and seven
form only a pair, so no `l1,l2,l3` triple exists for two.

After projection and distinctness, the result contains only value one.

**Why pairwise equality is enough**

The query states `l1.num = l2.num` and `l2.num = l3.num`. Equality is
transitive, so all three values are equal. A separate comparison between
`l1.num` and `l3.num` would be redundant.

Similarly, the two ID equations imply a chain of adjacent integer identifiers.
No explicit `l1.id + 2 = l3.id` condition is needed.

**Soundness and completeness**

Every output value comes from a joined triple with consecutive IDs and equal
numbers, so it truly appears in at least three consecutive log positions.

Conversely, any run of length at least three has a first three-row subwindow.
Assigning those rows to `l1`, `l2`, and `l3` satisfies the joins, so its value
appears before `DISTINCT` and survives in the output.

Thus the query emits exactly the qualifying values.

**Consecutive-ID assumption**

The schema says `id` is an autoincrement primary key starting at one, and the
local function contract uses increasing IDs as the sequence. The selected
query interprets consecutive events as IDs differing by exactly one.

If rows could be deleted and gaps remained, adjacent surviving rows in
`ORDER BY id` might not differ by one. A window-function solution with
`LAG` or row numbering would be needed for that alternate interpretation. The
challenge's standard data model supports the direct ID arithmetic.

**Result ordering**

Any output order is accepted, so the query correctly omits `ORDER BY`.
`DISTINCT` may return values in any physical order, and callers should not
infer one.

No qualifying value survives twice.

## Complexity detail

Let $n$ be the number of log rows. With the primary-key index, an engine can
scan one alias and probe the next IDs through indexed joins, then deduplicate
qualifying values. A plausible plan is $O(n\log n)$ time and $O(n)$ working
space for distinct processing, matching the manifest.

Hash joins or index-specific optimizations may give different physical costs.
SQL text specifies relational semantics, while indexes, statistics, and the
optimizer determine the actual execution plan.

## Alternatives and edge cases

- **`LAG` window functions:** Compare each row with the preceding two rows in ID order; this directly expresses sequence and handles row-order adjacency with gaps.
- **Run-length grouping:** Detect value changes with window functions, assign run IDs, group, and keep counts at least three.
- **User variables:** Can track a running count in older MySQL, but evaluation order is fragile and requires explicit ordering.
- **Exactly three:** Produces one window and one output value.
- **More than three:** Overlapping windows are collapsed by `DISTINCT`.
- **Separate runs of one value:** Still produce one output row.
- **Only two consecutive rows:** No three-alias chain exists.
- **Alternating values:** Equality joins reject every window.
- **ID gaps:** Direct `id + 1` logic assumes challenge-style consecutive identifiers.
- **Any order:** No final sorting is required.
