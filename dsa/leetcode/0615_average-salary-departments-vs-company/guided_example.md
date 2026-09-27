# Guided Example: Average Salary: Departments VS Company

This lesson works through one compensation ledger and answers a single question
for every department in every reporting period: is that department's average
salary above, below, or exactly level with the average salary the whole company
paid in the same period? The instance used is the canonical two-month ledger, and
it is chosen because February and March together produce all three answer
categories, so the comparison rule is exercised completely rather than only in
its "greater than" form.

The payroll relation `Salary` records one dated payment per employee, and the
`Employee` relation supplies the department that owns each employee.

| `id` | `employee_id` | `amount` | `pay_date` |
|:---:|:---:|:---:|:---:|
| $1$ | $1$ | $9000$ | `2017-03-31` |
| $2$ | $2$ | $6000$ | `2017-03-31` |
| $3$ | $3$ | $10000$ | `2017-03-31` |
| $4$ | $1$ | $7000$ | `2017-02-28` |
| $5$ | $2$ | $6000$ | `2017-02-28` |
| $6$ | $3$ | $8000$ | `2017-02-28` |

| `employee_id` | `department_id` |
|:---:|:---:|
| $1$ | $1$ |
| $2$ | $2$ |
| $3$ | $2$ |

The required relation has three attributes — the reporting month written as
`YYYY-MM`, the department, and the verdict word — and it must contain exactly one
row per pair of month and department that actually paid somebody.

| `pay_month` | `department_id` | `comparison` |
|:---:|:---:|:---:|
| `2017-02` | $1$ | `same` |
| `2017-02` | $2$ | `same` |
| `2017-03` | $1$ | `higher` |
| `2017-03` | $2$ | `lower` |

---

## 1. Normalizing the Period Attribute

The `pay_date` column is a calendar day, but the question asks about a month.
Two payments inside the same month that land on different days are the same
reporting period for this problem, so the comparison key is the month prefix,
not the day. Writing the month as `YYYY-MM` fixes the granularity once and for
all; sorting the raw `pay_date` values would instead split March into 31
separate benchmarking groups, each holding only the payments that happened to
fall on that day.

A second granularity decision is equally important. One employee can appear
several times in one month, and two different months can reuse the same
`employee_id`. The reporting unit is therefore a *pair*: the month together with
the department. Neither attribute alone identifies a row of the answer.

| Period key | Payments in the period | Departments represented |
|:---:|:---:|:---:|
| `2017-02` | `id` $4$, $5$, $6$ | $1$ and $2$ |
| `2017-03` | `id` $1$, $2$, $3$ | $1$ and $2$ |

The department of each payment is not stored in `Salary`; it is owned by
`Employee` and reached through the shared employee identity. Attaching that
attribute turns every payment row into the triple
$(\text{period}, \text{department}, \text{amount})$ and makes it possible to
aggregate the same money at two different grains.

## 2. Two Aggregates at Two Grains over One Money Stream

The decisive observation is that the company benchmark and the department
benchmark are both averages of the *same* payment amounts in the *same* period.
They differ only in how the payments are bucketed:

- the company bucket contains every payment in the period, so its county
  $n^{co}_{p}$ is the number of payments made that month;
- the department bucket contains only payments whose employee belongs to the
  department, with count $n^{dep}_{p}$.

Because both aggregates read one row of the joined ledger, they can be produced
side by side in a single pass. Partitioning the window by the period alone gives
the first value; partitioning by the period together with the department gives
the second. No pre-aggregated helper relation has to be built for either one,
and no join is needed to place the two values on the same row.

| Aggregate | Bucket definition | Symbol | March value | February value |
|:---|:---|:---:|:---:|:---:|
| Company monthly mean | every payment in the period | $\mu^{co}_{p}$ | $25000/3$ | $21000/3$ |
| Department monthly mean | payments of one department in the period | $\mu^{dep}_{p}$ | — | — |

The department values remain to be filled in per department, which is where the
one-row-per-payment structure of the joined ledger becomes visible.

## 3. Row-by-Row Evaluation on the Joined Ledger

Each payment carries the department of its employee. Two payments in March
belong to employee $2$ and employee $3$, and both of those employees sit in
department $2$; employee $1$, who is alone in department $1$, is paid once in
each month. The table below records, for every payment row, the two averages it
would carry and the verdict its comparison produces.

| Payment `id` | Period | Dept | `amount` | Company mean $\mu^{co}_{p}$ | Department mean $\mu^{dep}_{p}$ | Verdict |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `2017-03` | $1$ | $9000$ | $25000/3 \approx 8333.33$ | $9000$ | `higher` |
| $2$ | `2017-03` | $2$ | $6000$ | $25000/3 \approx 8333.33$ | $16000/2 = 8000$ | `lower` |
| $3$ | `2017-03` | $2$ | $10000$ | $25000/3 \approx 8333.33$ | $16000/2 = 8000$ | `lower` |
| $4$ | `2017-02` | $1$ | $7000$ | $21000/3 = 7000$ | $7000$ | `same` |
| $5$ | `2017-02` | $2$ | $6000$ | $21000/3 = 7000$ | $21000/3 = 7000$ | `same` |
| $6$ | `2017-02` | $2$ | $8000$ | $21000/3 = 7000$ | $21000/3 = 7000$ | `same` |

Three facts fall out of this trace.

First, the mean values are evaluated as exact rational quantities. March's
company mean is the fraction $25000/3$, not the rounded decimal $8333.33$, and
the verdict is decided on the exact fraction. No pair of values in this instance
sits close enough to a rounding boundary to change an answer, but the comparison
rule itself must be treated as exact.

Second, a value that repeats across rows carries no extra information. In
February every department happens to equal the company, and department $2$'s
value appears twice because two employees drew a paycheck that month. The answer
still needs only one row for `(2017-02, 2)`.

Third, the verdict is not a property of a payment; it is a property of the
month-department pair. Reducing the six evaluated rows to distinct pairs is
therefore part of forming the answer, not an optional cleanup.

| Evaluated rows | Distinct month-department pairs | Output rows |
|:---:|:---:|:---:|
| $6$ | $4$ | $4$ |

## 4. The Convexity Invariant Behind the Verdict

The correctness of the three-word comparison rests on one invariant of the
aggregation: inside a fixed period, the company mean is a convex combination of
the department means, weighted by the number of payments each department
contributed. A mean is a convex combination of its own parts, and the company
bucket is nothing more than the union of the department buckets, so the invariant
holds for every period regardless of how the headcounts are distributed.

Let $D$ be the set of departments that paid somebody in period $p$, let
$n_{d}$ be the number of payments department $d$ contributed, and let $N = \sum_{d \in D} n_{d}$.
Then

$$
\mu^{co}_{p}
= \frac{1}{N}\sum_{d \in D}\sum_{k=1}^{n_{d}} a_{d,k}
= \sum_{d \in D} \frac{n_{d}}{N}\,\mu^{dep}_{d},
\qquad \sum_{d \in D} \frac{n_{d}}{N} = 1 .
$$

Every weight $n_{d}/N$ is strictly positive and the weights sum to one, so the
company mean cannot lie strictly outside the range of the department means.
That immediately gives a soundness guarantee for the three-way verdict: if a
department's mean is strictly larger than the company mean it must be
`higher`, if strictly smaller it must be `lower`, and equality is the only
remaining case, reported as `same`. No fourth category is needed, and the three
words partition the possibilities with no overlap.

The convexity also bounds how many departments can sit on one side. At least one
department must reach or exceed the company mean and at least one must fall at or
below it; a period in which every department were strictly below the company
mean would require weights summing to less than one, which is impossible. In
February that bound is tight with two departments: with $n_{1} = 1$ and
$n_{2} = 2$ the weights are $1/3$ and $2/3$, and both departments equal the
company mean of $7000$, so the combination collapses to a single point.

Finally, the reduction to distinct pairs preserves every answer. Two payments of
the same department in the same period receive the same company mean, because
the company mean depends only on the period, and the same department mean,
because the department mean depends only on the pair. Identical evaluated rows
therefore reduce to one tuple without merging anything that should have stayed
separate.

## 5. The Traps This Instance Exposes

One trap is specific to this ledger and is the reason the instance is worth
tracing in full. In February, department $2$ contributes three payments that sum
to $21000$, exactly as much as the whole company, so the department verdict is
`same` rather than `lower`. Had the February payment of $8000$ by employee $3$
been left out of the ledger, the company mean would have fallen to $6500$ and
both departments would have been misreported as `higher` and `lower`. The
comparison is against every payment in the period, so the company bucket must
never be built from a partial scan.

The remaining traps are structural.

| Trap | Why it gives a wrong relation |
|:---|:---|
| Comparing against a mean of department means | The unweighted mean $(9000+8000)/2 = 8500$ for March is larger than the true company mean $25000/3$, so department $2$ would be scored `lower` against a benchmark the company never actually paid. The company benchmark must weight departments by their payment counts. |
| Partitioning by `pay_date` instead of the month | Payments on different days of one month land in different buckets, so each bucket holds only part of the month and the benchmark drifts. |
| Grouping only by department | Department $1$ is paid in both months, so a department-only key would merge `2017-02` and `2017-03` into one row and lose a required output row. |
| Emitting one row per payment | Department $2$ produced two evaluated rows in March; the required relation holds one tuple per month-department pair. |
| Building the company mean from a pre-aggregated department table | Joining two separately aggregated relations multiplies rows when a department has several employees, so the distinct reduction is needed for a different reason and the benchmark can drift from the true payment-weighted mean. |

## 6. Complexity Derivation

Let $S$ be the number of rows in `Salary` and $E$ the number of rows in
`Employee`. Attaching departments to payments is an equijoin on the shared
employee identity. With a hash table or a primary-key index on the smaller
relation each payment is matched in expected constant time, so the join
contributes $O(S + E)$ expected work; a comparison-based merge join would cost
$O\big((S+E)\log(S+E)\big)$ instead.

Partitioning the joined ledger for the two window aggregates requires the rows
to be grouped by the period, and by the period together with the department, in
one access pattern. A sort-based plan orders the $S$ joined rows and costs
$O(S \log S)$; a hash-partitioned plan costs $O(S)$ expected. Forming the verdict
is one constant-time comparison per joined row, and reducing the evaluated rows
to distinct pairs costs $O(S)$ with hashing or $O(S \log S)$ with sorting.

| Stage | Expected cost | Sort-based cost |
|:---|:---:|:---:|
| Join `Salary` to `Employee` on the employee identity | $O(S + E)$ | $O\big((S+E)\log(S+E)\big)$ |
| Partition by period, and by period plus department | $O(S)$ | $O(S \log S)$ |
| Evaluate the three-way verdict per row | $O(S)$ | $O(S)$ |
| Reduce to distinct month-department pairs | $O(S)$ | $O(S \log S)$ |

The engine-independent bound is therefore $O\big((S+E)\log(S+E)\big)$ time: the
sort-based column dominates, and $S \le S + E$ keeps the other stages inside it.

Auxiliary space is $O(S + E)$. The joined relation, the window partition state,
and the hashed or sorted set used for the distinct reduction each hold at most a
constant number of values per joined row or per employee, so the working data
stays linear in the input. The output itself contains at most one row per
represented month-department pair, which is bounded by $S$.