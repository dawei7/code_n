# Guided Example: Rising Temperature

## 1. The Calendar-Comparison Task and Its Representative Instance

A `Weather` relation records one observation per represented calendar day. Each row
carries a unique integer `id`, a `recordDate` of SQL `date` type, and an integer
`temperature`. The relation guarantees that no two rows share a `recordDate`, so a
date identifies at most one observation, but it guarantees nothing about the order
in which rows are physically stored and nothing about whether consecutive
identifiers correspond to consecutive days. The task asks for the identifier of
every day whose temperature is strictly higher than the temperature recorded on the
day immediately before it in the calendar.

| `id` | `recordDate` | `temperature` |
|:---:|:---:|:---:|
| 1 | `2015-01-01` | 10 |
| 2 | `2015-01-02` | 25 |
| 3 | `2015-01-03` | 20 |
| 4 | `2015-01-04` | 30 |

Reading the series chronologically:

- January 1 carries $10^\circ$ and has no predecessor row in the relation, so no
  rise can be established for it.
- January 2 carries $25^\circ$ against January 1's $10^\circ$; the difference
  $25 - 10 = +15$ is positive, so identifier 2 qualifies.
- January 3 carries $20^\circ$ against January 2's $25^\circ$; the difference
  $20 - 25 = -5$ is not positive, so identifier 3 is rejected.
- January 4 carries $30^\circ$ against January 3's $20^\circ$; the difference
  $30 - 20 = +10$ is positive, so identifier 4 qualifies.

The required output is therefore the one-column relation below. The contract
allows the two rows in any order, so no sorting is needed.

| `id` |
|:---:|
| `2` |
| `4` |

## 2. Calendar Adjacency and the Strict-Rise Invariant

Let the relation be a set of observations $\rho = (i, d, \tau)$ where $i$ is the
identifier, $d$ the calendar date, and $\tau$ the temperature. Two observations
stand in the *immediately-preceding-day* relation when

$$d_{\text{candidate}} - d_{\text{predecessor}} = 1 \text{ day}.$$

Writing $\Delta(d_1, d_2)$ for the signed number of days from $d_2$ to $d_1$, a
candidate $r$ qualifies when

$$\exists\, s:\; \Delta(r.d,\, s.d) = 1 \;\wedge\; r.\tau > s.\tau.$$

Three properties of this definition drive the whole solution.

**Adjacency is a relation on dates, not on positions.** The predicate compares two
date values. It never inspects `id`, never subtracts identifiers, and never relies
on physical row order. An engine is free to return rows in any order and the
predicate is unaffected.

**Adjacency is exact, not "most recent earlier".** The equality $\Delta = 1$ admits
no substitute for a missing day. If January 1 is followed directly by January 3,
then January 3 has no predecessor in the relation at all, even though January 1 is
the nearest older observation. Substituting "the previous available observation"
would silently answer a different question — temperature change between consecutive
*observations* rather than consecutive *days*.

**The comparison is strict.** Equality is not a rise. A day that repeats yesterday's
temperature, and a day that is cooler, both fail $r.\tau > s.\tau$.

> **Invariant.** An observation is emitted if and only if the relation contains an
> observation dated exactly one calendar day earlier whose temperature is strictly
> lower than its own.

Because `recordDate` is unique, a candidate can be paired with at most one
predecessor, so a qualifying day cannot produce duplicate output rows and no
de-duplication step is required.

## 3. Worked Trace: Evaluating Every Represented Day

For each candidate we ask two questions in order: does an exactly-one-day-earlier
row exist, and if so, is the candidate's temperature strictly larger?

| Candidate `id` | `recordDate` | $\tau$ | Required predecessor date | Predecessor present? | Predecessor $\tau$ | $r.\tau > s.\tau$ | Decision |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---|
| 1 | `2015-01-01` | 10 | `2014-12-31` | no row | — | not evaluable | rejected |
| 2 | `2015-01-02` | 25 | `2015-01-01` | row 1 | 10 | $25 > 10$ is true | emitted as `2` |
| 3 | `2015-01-03` | 20 | `2015-01-02` | row 2 | 25 | $20 > 25$ is false | rejected |
| 4 | `2015-01-04` | 30 | `2015-01-03` | row 3 | 20 | $30 > 20$ is true | emitted as `4` |

The trace shows why both conjuncts are necessary. Row 1 is rejected by the
adjacency conjunct, not by the temperature conjunct, because there is nothing to
compare against. Row 3 satisfies adjacency but fails the strict comparison. Only
rows 2 and 4 satisfy both.

## 4. The Adjacency Pair Grid

It is instructive to view the same computation as a grid over ordered pairs of
rows. Only pairs satisfying $\Delta = 1$ can ever contribute, and among those only
the temperature predicate selects.

| Candidate row | Partner row | $\Delta(\text{candidate}, \text{partner})$ | Calendar-adjacent? | $\tau_{\text{cand}} > \tau_{\text{partner}}$ | Contributes? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 (Jan 1, 10) | 1 (Jan 1, 10) | $0$ | no | $10 > 10$ false | no |
| 1 (Jan 1, 10) | 2 (Jan 2, 25) | $-1$ | no | $10 > 25$ false | no |
| 2 (Jan 2, 25) | 1 (Jan 1, 10) | $+1$ | yes | $25 > 10$ true | yes |
| 2 (Jan 2, 25) | 3 (Jan 3, 20) | $-1$ | no | $25 > 20$ true | no |
| 3 (Jan 3, 20) | 2 (Jan 2, 25) | $+1$ | yes | $20 > 25$ false | no |
| 3 (Jan 3, 20) | 4 (Jan 4, 30) | $-1$ | no | $20 > 30$ false | no |
| 4 (Jan 4, 30) | 3 (Jan 3, 20) | $+1$ | yes | $30 > 20$ true | yes |

The sign of the day difference is what prevents double counting. A pair of
consecutive days appears twice in the ordered grid, once with difference $+1$ and
once with difference $-1$. Only the orientation in which the candidate is the later
day satisfies the predicate, so a rise is counted once — for the warmer, later day —
and never for the earlier one. Swapping the two dates in the subtraction would
invert this: the predicate would then select days that are *cooler* than the
following day, which is the wrong question entirely.

## 5. Why the Reasoning Is Correct

**Soundness.** Let $r$ be emitted. By the adjacency conjunct, the relation contains
an observation $s$ dated exactly one day before $r$, so $s$ really is yesterday for
$r$. By the comparison conjunct, $r.\tau > s.\tau$, so $r$ really is warmer than its
yesterday. Every emitted identifier therefore satisfies the requirement, and the
uniqueness of `recordDate` ensures $r$ is emitted once rather than once per
qualifying partner.

**Completeness.** Let $r$ be a day that is warmer than its represented yesterday.
Then that yesterday observation exists in the relation, and pairing $r$ with it
satisfies both conjuncts, so $r$ is emitted. No qualifying day escapes the rule.

**Why a missing day is a correct rejection.** If the calendar day before $r$ is not
represented, the relation contains no evidence about $r$'s yesterday. Refusing to
emit $r$ is the only answer consistent with the definition. The nearest older
observation is a different row and would give a temperature *change between
observations*, which the statement does not ask for.

**Why row identifiers are irrelevant.** The instance's identifiers happen to run in
chronological order, which makes the tempting shortcut of subtracting identifiers
look correct. It is not: the contract only makes `id` unique. A relation whose rows
carry identifiers $9, 2, 1$ on consecutive May dates must obey the calendar, not the
labels — a case the authored trial inputs exercise deliberately.

## 6. Traps This Instance Exposes

| Trap | Instance that exposes it | Why it is wrong |
|:---|:---|:---|
| Comparing with the nearest earlier observation instead of the exact previous day | A relation holding only `2020-01-01` ($1^\circ$) and `2020-01-03` ($9^\circ$) | January 3 is two days after January 1, so no yesterday exists; the change is between observations, and the required output is empty |
| Assuming physical row order or identifier order encodes chronology | Rows stored as `2021-05-02`, `2021-05-01`, `2021-05-03` with identifiers `9, 2, 1` | Ordering by identifier would compare the wrong days; only date subtraction identifies the predecessor |
| Using a non-strict comparison | Two consecutive days both at $5^\circ$ | Equal temperatures are not a rise, so the output must be empty |
| Reversing the subtraction | Any adjacent pair | The predicate would then select days cooler than the following day, inverting the answer |
| Emitting the earlier day of a rising pair | January 1 and January 2 with $10^\circ$ and $25^\circ$ | The warmer day is the later one; the identifier reported is the one belonging to the higher temperature |
| Expecting one output row per represented day | January 1 in the instance | A day with no yesterday has no comparison and is omitted; the output size is at most the input size, never more |

## 7. Complexity Derivation

Let $n$ be the number of rows in `Weather`. The contract fixes one row per
represented date, so $n$ is both the row count and the number of distinct dates.

- **Pairwise adjacency cost.** Deciding the predicate directly means asking, for
  each candidate, whether the relation holds a row at the preceding calendar date,
  and then comparing the two temperatures. An evaluation that tests every ordered
  pair of rows performs $n(n-1)$ adjacency tests, so its time is $O(n^2)$. This is
  the conservative bound recorded for the pairwise formulation, and it is what
  happens when date arithmetic is applied to both sides of a comparison, because
  no ordinary index can then narrow the candidate set.
- **Reducing the cost with a date key.** Nothing in the predicate requires all
  pairs to be examined. Keying the observations by `recordDate` — a hash table, a
  sorted run, or a B-tree index — costs expected $O(n)$ for hashing and
  $O(n \log n)$ for sorting or index construction, and thereafter each candidate
  probe is $O(1)$ expected or $O(\log n)$. A constant number of comparisons per
  candidate then completes the pass in $\Theta(n)$ once the structure exists, so the
  total becomes $O(n \log n)$ with a sorted or index-driven plan and $O(n)$ expected
  with hashing.
- **Auxiliary space.** $O(n)$ for the date-keyed lookup structure in the worst case
  (every date distinct), plus $O(k)$ for the $k$ emitted identifiers, where
  $k \le n$. The pairwise formulation keeps no lookup at all and needs only the
  accumulator space for its emitted identifiers, so the faster method trades linear
  working memory for the removal of a factor of $n$.

The asymptotic lesson of the instance is that a comparison between two rows of the
same relation becomes a single keyed lookup as soon as the key is the *date* rather
than the row position, which removes a factor of $n$ from the naive pairwise
formulation.
