## General

**The denominator is the complete user population**

The requested percentage for a contest is

$$
\frac{\text{number of users registered for that contest}}
{\text{number of users in Users}}\times100.
$$

The scalar subquery `(SELECT COUNT(1) FROM Users)` computes the denominator. `COUNT(1)` counts every row because the constant 1 is never null. Since `user_id` is the primary key, each Users row represents one distinct user, so counting rows is the same as counting users.

This denominator is common to every contest. Although it is written as a scalar subquery inside the select expression, it returns exactly one number and can be reused conceptually for every group. A database optimizer will commonly evaluate or cache such an uncorrelated scalar subquery once.

**Group registrations by contest**

The outer query reads `Register` and groups by the first selected expression through `GROUP BY 1`. The first selected expression is `contest_id`, so this is positional shorthand for `GROUP BY contest_id`.

Each resulting group contains all registration rows for one contest. `COUNT(1)` counts those rows. The composite primary key `(contest_id, user_id)` guarantees that one user cannot appear twice in the same contest group. Therefore the row count is already the number of distinct registered users; `COUNT(DISTINCT user_id)` would produce the same result but is unnecessary under the schema.

Only contests represented in `Register` form groups. That matches the data model used by the query: the result reports contests with registration records, and there is no separate Contests table from which to generate empty contests.

**Calculate and round the percentage**

For each group, the source evaluates

`COUNT(1) * 100 / total_users`.

Multiplying by 100 converts the registration fraction into a percentage. In MySQL, the `/` operator performs division rather than integer `DIV`, so a count such as 2 out of 3 can retain its fractional part instead of becoming zero.

`ROUND(..., 2)` rounds the computed percentage to two digits after the decimal point. For 2 registered users among 3 total users, the unrounded percentage is approximately $66.666\ldots$, and the selected value is $66.67$.

The alias `percentage` gives the calculated column its required output name. The only other selected column is `contest_id`, so the result schema is exact.

**Apply both ordering rules**

`ORDER BY 2 DESC, 1` also uses select-list positions:

- position 2 is `percentage`, ordered descending;
- position 1 is `contest_id`, ordered ascending because no direction is specified and ascending is SQL's default.

The second key is consulted only when the rounded percentage values compare equal. This produces the requested tie order. For example, contests 208, 209, and 210 at 100 percent appear in increasing contest-ID order.

Using positional numbers makes the query concise, but understanding their mapping to the select list is important. Changing the select-column order without changing these ordinals would silently change grouping or sorting behavior.

**Why the query returns the correct rows**

For any contest group, the primary-key guarantee gives a one-to-one correspondence between its rows and its registered users. The numerator is therefore exact. The Users primary key similarly makes the scalar row count the total number of users. Division and multiplication implement the percentage definition, and `ROUND` applies the required precision.

`GROUP BY` emits one aggregate row for each represented contest. The two-level `ORDER BY` then establishes exactly the required sequence. No join is necessary because the numerator needs only Register row counts and the denominator needs only the independent total Users count; individual user attributes do not affect the calculation.

**Walk through the sample totals**

With three rows in Users, the denominator is 3. Contest 208 has three Register rows, so its percentage is $3\times100/3=100$. Contest 215 has two, giving $2\times100/3$, rounded to 66.67. Contest 207 has one, giving 33.33.

The three 100-percent contests tie on the second selected expression, so `ORDER BY 1` places IDs 208, 209, and 210 in ascending order. The lower percentages follow in descending order.

## Complexity detail

Let $u$ be the number of Users rows, $r$ the number of Register rows, and $c$ the number of distinct contests represented in Register.

Logically, counting Users is $O(u)$ and grouping Register is $O(r)$ with hash aggregation. Sorting the $c$ aggregate rows for the requested order costs $O(c\log c)$. This gives $O(u+r+c\log c)$ time, matching the manifest.

A hash-based group operation stores one aggregate counter per contest, or $O(c)$ working space. Sorting can also require $O(c)$ materialized rows. The returned result contains $c$ rows. Exact physical cost depends on MySQL's indexes, aggregation choice, temporary-table strategy, and whether it computes the scalar subquery once, but these logical bounds describe the query structure.

The schema's composite primary key means no distinct-user set is required inside each group, reducing both logical work and storage compared with a defensive `COUNT(DISTINCT user_id)`.

## Alternatives and edge cases

- **Use `COUNT(DISTINCT user_id)`:** This is robust to duplicate registration rows, but the composite primary key already forbids them. Distinct aggregation can require extra work.
- **Cross join a one-row total CTE:** Compute the Users count once in a CTE and cross join it to contest aggregates. This can make denominator reuse explicit but produces the same result.
- **Join Register to Users:** It is unnecessary when registration user IDs conform to the intended schema and no user attributes are needed. A join adds work without changing the numerator.
- **Spell out column names:** `GROUP BY contest_id ORDER BY percentage DESC, contest_id ASC` is more resilient to select-list reordering than positional ordinals. The exact source uses positions.
- **Contest with every user registered:** Its percentage is exactly 100.
- **Contest with one of three users:** The expression retains the fraction and `ROUND` returns 33.33.
- **Tied percentages:** Contest ID ascending is the deterministic secondary key.
- **Duplicate registration attempt:** The primary key prevents two rows for the same contest-user pair, which is why `COUNT(1)` is sufficient.
- **No registration rows:** The query returns no contest groups. There is no separate contest table in the contract from which to emit zero-percent rows.
- **Empty Users table:** Division by zero would be undefined. The intended problem data assumes a user population for percentages; a broader production query would need an explicit zero-denominator policy.
- **Rounding point:** The source rounds the final percentage, not the numerator or denominator separately.
- **Changing select order:** Because `GROUP BY 1` and `ORDER BY 2, 1` are positional, such a refactor must update the ordinals or replace them with names.
