## General

**Determine one tax bracket per company.** The tax rate is not based on an individual employee's salary. It is based on the maximum salary anywhere in that employee's company. The query therefore begins by calculating one summary row per `company_id`.

The derived table `t` groups `Salaries` by company and computes `MAX(salary) AS top`. If a company has many employees, `top` retains only its highest original salary. The primary key guarantees unique employee rows but is not needed for the maximum itself.

**Attach the company maximum back to every employee.** The outer table alias `s` still contains one row per employee. Joining `s.company_id = t.company_id` gives each employee the `top` value for their own company.

The derived table has exactly one row per company, so the join neither duplicates nor removes valid employee rows. Every employee's company appears in the derived table because that same employee contributed to its group.

This aggregate-then-join pattern is useful whenever a group-level fact must control a row-level calculation. Grouping alone would collapse employees; joining the summary back restores individual detail while sharing the correct company statistic.

**Translate tax percentages into retained salary factors.** A zero-percent tax leaves one hundred percent of salary, so the first branch returns `salary` unchanged.

A twenty-four-percent tax leaves seventy-six percent. The middle branch multiplies by `0.76`. A forty-nine-percent tax leaves fifty-one percent, so the final branch multiplies by `0.51`.

The query computes after-tax salary directly rather than first calculating tax and subtracting it. Both formulas are algebraically equivalent: `salary - 0.24 * salary` equals `0.76 * salary`.

**Respect every threshold boundary.** `top < 1000` selects zero percent. The next condition uses `top >= 1000 AND top <= 10000`, so both one thousand and ten thousand belong to the twenty-four-percent bracket. `ELSE` covers only values greater than ten thousand under the stated salary domain.

The conditions are evaluated in order by `CASE`. Although the lower test in the middle branch is logically implied after the first branch fails, writing both limits makes the inclusive range explicit.

**Round only the final after-tax amount.** `ROUND(...)` surrounds the complete `CASE` result. An employee's retained salary can contain a fractional part, and the required output is the nearest integer. Rounding the percentage or original salary earlier would distort the calculation.

For salary `7777` in a company whose maximum is in the middle bracket, the retained amount is `7777 * 0.76 = 5910.52`. `ROUND` returns `5911`.

The selected output keeps `company_id`, `employee_id`, and `employee_name` from the employee row and replaces the displayed `salary` with the rounded computed value through `AS salary`.

**Trace three company types.** If a company's maximum is seven hundred, every joined employee row uses the first branch, regardless of whether an individual's salary is much smaller. If the maximum is exactly ten thousand, every employee uses the middle branch. If one employee earns 21300, that maximum puts every employee in the company into the forty-nine-percent bracket.

This last point prevents a common mistake: applying a different rate to each employee based on their own salary would violate the company-wide rule.

**Why every output row is correct.** The derived group computes the exact maximum for each company. The equality join attaches that unique maximum to precisely the company's employees. The exhaustive, non-overlapping `CASE` thresholds choose the specified tax rate, and the multiplier gives the corresponding after-tax amount. Final rounding supplies the requested integer.

Each input employee appears once because the join is many employees to one company summary. Row ordering is unrestricted, so no `ORDER BY` is necessary.

## Complexity detail

Let `E` be the number of employee rows and `C` the number of distinct companies. A conventional hash aggregation scans `E` rows and stores one maximum per company, taking expected `O(E)` time and `O(C)` space.

Joining the `E` employee rows to the `C` summaries by company ID takes expected `O(E + C)` time with a hash table. The fixed `CASE` and rounding work is constant per employee. Total expected time is `O(E + C)` and working space is `O(C)`, matching the manifest.

The result itself contains `E` rows. If output storage is counted, it adds `O(E)`. SQL optimizers may choose indexes, sorting, temporary tables, or disk spilling, so the stated bounds describe the usual in-memory aggregate-and-join plan.

No result sort is requested, avoiding an additional ordering cost.

## Alternatives and edge cases

- **Window-function maximum:** `MAX(salary) OVER (PARTITION BY company_id)` can attach the company maximum without an explicit derived-table join. It expresses the same logic compactly where supported.
- **Correlated subquery:** Compute the maximum separately for each employee row. It is readable but may repeat work unless the optimizer decorrelates it.
- **Tax each employee independently:** This is incorrect because the company's highest salary determines the rate for every employee.
- **Maximum below 1000:** Salaries remain unchanged before rounding.
- **Maximum exactly 1000:** The inclusive middle bracket applies, producing a twenty-four-percent tax.
- **Maximum exactly 10000:** It also remains in the middle bracket.
- **Maximum above 10000:** The fifty-one-percent retained factor applies company-wide.
- **One-employee company:** That employee's own salary is also the company maximum, and the normal logic works.
- **Several employees share the maximum:** `MAX` still returns one scalar summary and the join returns each employee once.
- **Fractional retained salary:** `ROUND` is applied after multiplication to produce the nearest integer.
- **Any-order output:** Omitting `ORDER BY` is correct.
- **Output alias:** `AS salary` gives the calculated value the same required column name as the original.
- **Decimal arithmetic:** The decimal literals `0.76` and `0.51` express retained percentages directly; database numeric rules determine intermediate precision before rounding.
- **Empty table:** The derived table and final result are both empty, with no invented employees.
