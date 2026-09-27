# Guided Example: Customers With Strictly Increasing Purchases

## 1. The report this query must decide

The `Orders` relation stores one row per purchase: `order_id`, `customer_id`,
`order_date`, and `price`. The requested report returns the `customer_id` of
every customer whose **total purchases** are strictly increasing yearly.

Three definitional rules turn that phrase into a checkable statement:

- The **total purchases** of a customer in one year is the sum of the prices of
  that customer's orders dated inside that year. If the customer placed no order
  in some year, the total purchases for that year is `0`.
- The first year considered for a customer is the year of that customer's
  **first order**.
- The last year considered is the year of that customer's **last order**.

So the objects being compared are not "the years that appear in the table". For
a customer with observed years $y_1 < y_2 < \dots < y_m$ and yearly totals
$T_1, \dots, T_m$, the rule demands the strictly increasing chain

$$
T_1 < T_2 < \dots < T_m
$$

evaluated across the complete integer run of calendar years from $y_1$ to $y_m$
— including any interior year in which the customer ordered nothing and whose
total is therefore `0`.

Two independent decisions hide in that sentence, and the instance below
separates them cleanly:

1. **Gaplessness** — may the observed years skip a calendar year?
2. **Strictness** — may two consecutive years carry equal totals?

The output column is only `customer_id`, and the result order is unrestricted;
the query therefore never needs to rank the surviving customers, only to decide
membership for each one.

## 2. The official instance, customer by customer

The nine authored rows below are the official example. Three customers appear,
and each one is a different kind of test.

| `order_id` | `customer_id` | `order_date` | `price` |
|:---:|:---:|:---|:---:|
| 1 | 1 | `2019-07-01` | 1100 |
| 2 | 1 | `2019-11-01` | 1200 |
| 3 | 1 | `2020-05-26` | 3000 |
| 4 | 1 | `2021-08-31` | 3100 |
| 5 | 1 | `2022-12-07` | 4700 |
| 6 | 2 | `2015-01-01` | 700 |
| 7 | 2 | `2017-11-07` | 1000 |
| 8 | 3 | `2017-01-01` | 900 |
| 9 | 3 | `2018-11-07` | 900 |

Reading the rows in storage order immediately exposes a trap: the `order_id`
sequence is interleaved across customers, and customer 1 alone has two orders
inside `2019`. Nothing about the physical row order is meaningful. The only
grouping that matters is by `(customer_id, calendar year of order_date)`.

## 3. Folding raw orders into yearly totals

The first reduction collapses every order of a customer inside one calendar year
into a single number. Until this collapse happens, no comparison between years is
even well-defined, because a year is a set of rows and not a value: customer 1's
`2019` is `1100 + 1200`, while customer 2's `2015` is a single row.

| `customer_id` | year | fold of the year's orders | yearly total $T$ |
|:---:|:---:|:---|:---:|
| 1 | 2019 | `1100 + 1200` | 2300 |
| 1 | 2020 | `3000` | 3000 |
| 1 | 2021 | `3100` | 3100 |
| 1 | 2022 | `4700` | 4700 |
| 2 | 2015 | `700` | 700 |
| 2 | 2017 | `1000` | 1000 |
| 3 | 2017 | `900` | 900 |
| 3 | 2018 | `900` | 900 |

After this step the table has one row per customer-year pair, and the question
becomes a statement about numeric sequences rather than about relation rows. Note
that customer 2 has no `2016` row at all: absence is not stored, it is inferred
from the span between the first and last order year.

## 4. Gaplessness: the calendar span must be unbroken

Because every `price` is a positive amount, a year in which a customer actually
ordered has a yearly total of at least `1`. A year inside the customer's span
with no orders has total exactly `0`. Inserting that zero into the chain forces

$$
T_{\text{previous}} \ge 1 > 0 = T_{\text{gap}},
$$

a strict decrease. A single missing interior year therefore disqualifies the
customer no matter how the real years grow. Gaplessness is not an extra policy
rule; it is what the zero-total definition does to strict increase.

The practical test is a counting identity. If the observed years of a customer
are exactly the calendar years $y_1, y_1+1, \dots, y_m$, then

$$
\max(\text{year}) - \min(\text{year}) + 1 = \text{number of observed years}.
$$

| `customer_id` | observed years | $\min$ | $\max$ | span $\max - \min + 1$ | count of years | gapless? |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| 1 | 2019, 2020, 2021, 2022 | 2019 | 2022 | 4 | 4 | yes |
| 2 | 2015, 2017 | 2015 | 2017 | 3 | 2 | no — `2016` is missing |
| 3 | 2017, 2018 | 2017 | 2018 | 2 | 2 | yes |

Customer 2 fails here for a second, independent reason that section 5 will also
detect: `700` then an implicit `0` then `1000` is not increasing.

## 5. Strict increase as a shift invariant

Strictness is where a naive formulation slips. Comparing each total with the
totals of *other* years requires knowing which year comes next, and the interior
gap of customer 2 has no row to compare against. A single window ordering solves
both problems at once: sort a customer's customer-year rows by yearly total
ascending and attach the ascending rank $\rho$ of each total. For customer 1:

| `customer_id` | year | yearly total $T$ | ascending rank $\rho$ | shift $y - \rho$ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 2019 | 2300 | 1 | 2018 |
| 1 | 2020 | 3000 | 2 | 2018 |
| 1 | 2021 | 3100 | 3 | 2018 |
| 1 | 2022 | 4700 | 4 | 2018 |

Every shift equals `2018`, so customer 1 is reported. Now the two rejected
customers:

| `customer_id` | year | yearly total $T$ | ascending rank $\rho$ | shift $y - \rho$ |
|:---:|:---:|:---:|:---:|:---:|
| 2 | 2015 | 700 | 1 | 2014 |
| 2 | 2017 | 1000 | 2 | 2015 |
| 3 | 2017 | 900 | 1 | 2016 |
| 3 | 2018 | 900 | 1 | 2017 |

Customer 2's gap reappears as two different shifts, and customer 3's tie is the
telling case: equal totals receive the *same* rank, so the two rows inherit
different shifts (`2016` versus `2017`) and the customer is rejected. The report
keeps a customer exactly when the set of shifts within the customer's partition
collapses to a single value.

## 6. Why a constant shift is exactly the right invariant

The invariant is sharper than it first looks. Claim: for a customer's observed
years $y_1 < \dots < y_m$ with totals $T_1, \dots, T_m$ and ascending ranks
$\rho_1, \dots, \rho_m$ (ties sharing the lowest rank), the condition

$$
y_i - \rho_i = c \quad \text{for one constant } c \text{ and every } i
$$

holds if and only if the observed years are consecutive *and* the totals are
strictly increasing in year order.

*Sufficiency.* If the years are consecutive and totals strictly increase, then
ascending order by total is identical to ascending order by year, so
$\rho_i = i$ and $y_i = y_1 + (i - 1)$, giving the constant
$c = y_1 - 1$ for every row.

*Necessity.* Suppose $y_i - \rho_i = c$ for all $i$. Two rows of the same
partition with equal rank would need equal years, which is impossible because
each customer-year pair is unique; hence every row has a distinct rank, ranks are
exactly $\{1, \dots, m\}$, and the years are exactly $\{c+1, \dots, c+m\}$ —
consecutive, with no interior gap. Moreover a larger year must then carry a
larger rank, and larger rank means a strictly larger total (equal totals would
share a rank), so $T_1 < \dots < T_m$.

This is why the three predicates of the canonical query are not independent
filters stacked for safety: the shift predicate already implies the gaplessness
count and the "all yearly totals distinct" count. Stating the other two makes the
intent legible — a gap and a tie each have an obvious named test — but the
decisive comparison is the single constant-shift check. Dashboarding the sample
against the authored expectations confirms the outcome: the surviving set is
just $\{1\}$.

## 7. Boundary conditions the authored trials expose

The extra authored instances isolate each semantic edge so that a wrong rule
fails loudly rather than accidentally.

| Instance | Situation | What the rules compute | Verdict |
|:---|:---|:---|:---|
| one observed year (customer 4) | 2022 holds `50 + 75` | span of one year, one shift value | qualifies vacuously |
| aggregation first (customer 5) | 2020 holds `40 + 60`, then 2021 `101`, 2022 `102` | `100 < 101 < 102`, consecutive | qualifies |
| equal yearly totals (customer 6) | `10`, `10`, `12` | the two `10`s share a rank, shifts disagree | rejected |
| later decrease (customer 7) | `10`, `20`, `15` | ordering by size reorders the years | rejected |
| interior gap (customer 8) | 2018 `5`, then 2020 `50` | span count `3` but observed years `2`; also `5`, `0`, `50` | rejected |
| independent partitions (customers 9, 10, 11) | `1, 2`; `4, 3`; a single year `7` | each partition judged alone | 9 and 11 qualify, 10 rejected |

Two traps deserve emphasis. First, customer 5 shows that a year with several
orders must be summed *before* any comparison: `40` and `60` are individually
smaller than `101`, but their year total `100` is what participates in the chain,
and comparing orders rather than years would silently mislabel the customer.
Second, customer 7 shows that the shift test does not assume monotone years; it
compares rank order with year order, so a plateau followed by a fall is caught as
two disagreements rather than one.

## 8. Alternative formulations and their trade-offs

| Formulation | How it decides | Cost shape | Where it breaks |
|:---|:---|:---|:---|
| Ascending-rank shift (used here) | one ordering per customer partition; require one distinct shift value | one sort per partition, linear scan afterwards | depends on tie semantics: a rank that assigns equal values to equal totals is what makes ties fail |
| Zero-filled calendar, then compare with the previous year | materialize every year in each customer's span, substitute `0`, compare adjacent years | needs a span expansion before the comparison | widens to the span length, so a long idle stretch creates rows that carry no information |
| Pair each year with its successor | join a year to the following year's total | quadratic in years per customer unless carefully bounded | the last year has no successor, so the terminal comparison needs a separate rule and gap years vanish from the join |
| Look for a violating pair instead of proving order | search for a year whose total is not below its successor's | correlated lookup per candidate pair | easy to mis-express the equality case, since "not increasing" includes both a tie and a decrease |

The zero-filled variant is closest in spirit and is a genuine alternative: it
makes the `0` for an unobserved year explicit instead of inferring it. The
rank-shift variant wins because it never needs to enumerate the span — the gap
and the tie both surface as disagreement inside one ordering, so the work scales
with the rows that exist rather than with the width of the calendar range.

## 9. Complexity of the method

Let $n$ be the number of rows in `Orders`, $C$ the number of distinct customers,
and $m_c$ the number of distinct order years of customer $c$. The pipeline has
three stages: group by `(customer_id, year)` and sum; order each customer's
customer-year rows by total to attach the ascending rank; then group by customer
and test the membership predicates. The prepared relation holds at most
$\min\!\left(n, \sum_c m_c\right)$ rows.

- **Time:** the grouping stage costs $\Theta(n)$ with hash aggregation or
  $O(n \log n)$ if sorted; the window ordering costs
  $O\!\left(\sum_c m_c \log m_c\right) \le O(n \log n)$; the final grouping is
  linear in the number of customer-year rows. The dominant term is the ordering,
  so the bound is $O(n \log n)$.
- **Auxiliary space:** the intermediate per-customer-year relation, at most $n$
  rows, plus one running counter per open customer group, giving $O(n)$
  auxiliary space. The input relation and the returned `customer_id` column are
  not counted.

A useful sanity reading of the bound: the query never materializes the calendar
span, so $m_c$ may be much smaller than the number of years between a customer's
first and last order without changing the cost at all. The interior gap of
customer 2 costs nothing extra; it is detected by the same comparison that
detects the tie of customer 3.