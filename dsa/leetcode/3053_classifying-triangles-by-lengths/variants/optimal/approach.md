## General

**Reject invalid triples before classifying equality.** Three side lengths form a nondegenerate triangle only when all strict triangle inequalities hold:

$$
A+B>C,\qquad A+C>B,\qquad B+C>A.
$$

The first `WHEN` checks the negation:

`A + B <= C OR A + C <= B OR B + C <= A`.

If any inequality fails, the row is labeled `'Not A Triangle'`. Equality is invalid because it produces a flat, zero-area shape.

Checking validity first is essential. Values such as $(1,1,2)$ have equal sides but do not form an isosceles triangle; the first branch correctly rejects them before equality classification.

**Identify the most specific valid category next.** For a valid row, `A = B AND B = C` means all three sides are equal, so the result is `'Equilateral'`. MySQL identifiers are case-insensitive in this context, so the source's lowercase `c` refers to column `C`.

The equilateral check precedes isosceles because an equilateral row also has equal pairs. The specific category must win.

**Use Boolean arithmetic for exactly one equal pair.** In MySQL, true comparisons act like 1 and false comparisons like 0 in numeric addition. The expression

`(A = B) + (B = C) + (A = C) = 1`

is true exactly when one of the three pairwise equality comparisons holds.

For three values, exactly one equal pair means exactly two sides share a length and the third differs: an isosceles triangle. If all three were equal, all three comparisons would be true and their sum would be three, but that case has already been handled anyway.

**Everything else is scalene.** Once the row is valid, not equilateral, and not isosceles, no pair of sides is equal. All three lengths differ, so `ELSE 'Scalene'` is exhaustive.

**A branch trace.** Row $(20,20,23)$ passes all triangle inequalities. It is not equilateral. Only `A=B` is true, giving Boolean sum one, so it is isosceles.

Row $(20,20,20)$ passes validity and reaches the equilateral branch.

Row $(20,21,22)$ passes validity, all equality comparisons are false, and reaches scalene.

Row $(13,14,30)$ satisfies $13+14\le30$, so it is rejected immediately.

**Why all three inequalities are explicit.** Unlike an algorithm that first sorts the three values, SQL rows remain in their named columns. Without sorting, any side might be the largest, so the source checks all three symmetric conditions. This avoids database-specific array construction or greatest-value bookkeeping.

**One output per input row.** `CASE` evaluates in order and returns the first matching label. The query has no grouping or joins, so every `Triangles` row independently produces exactly one `triangle_type` row. The contract permits any result order, so no `ORDER BY` is required.

## Complexity detail

For $R$ table rows, the query performs a fixed number of additions, comparisons, and Boolean operations per row. Logical time is $O(R)$.

There is no grouping, sorting, or proportional intermediate state. Aside from result rows and the database scan machinery, auxiliary working state is $O(1)$ per row. Database engines may buffer output pages, but the relational algorithm needs no $O(R)$ structure.

Arithmetic must use a type wide enough for side sums. Under ordinary integer constraints this is safe in MySQL.

## Alternatives and edge cases

- **Sort side values per row:** Then only the two-smallest sum needs testing, but expressing a three-value sort in SQL is less direct than symmetric inequalities.
- **Use `GREATEST` and total sum:** Validity can be expressed as total minus largest greater than largest. The current conditions are clearer and avoid null-propagation surprises beyond normal comparisons.
- **Count distinct side lengths:** For valid rows, one, two, or three distinct lengths map to equilateral, isosceles, or scalene. Per-row distinct counting is more cumbersome than direct equality.
- **Degenerate equality:** A sum equal to the third side is `Not A Triangle` because the inequalities are strict.
- **Equilateral row:** It must be checked before isosceles to receive the requested specific label.
- **Exactly two equal sides:** Exactly one of the three pairwise comparisons is true.
- **All sides different:** Equality sum is zero, so a valid row reaches scalene.
- **Nonpositive sides:** The schema excerpt does not state positivity; the all-inequalities check rejects ordinary zero or negative configurations in many cases, but explicit positivity would be safer outside the intended dataset.
- **NULL values:** A primary-key tuple normally makes these columns non-null in MySQL. If nulls were allowed, three-valued logic would require explicit handling.
- **Any order:** No final sort is necessary because the statement permits arbitrary output order.
- **CASE short-circuit semantics:** MySQL returns the result of the first true `WHEN`. Later equality tests cannot overwrite an invalid classification, which is exactly why branch ordering forms part of correctness.
- **Why equality sum cannot be two:** For ordinary values, if $A=B$ and $B=C$, transitivity also gives $A=C$, producing three true comparisons. Otherwise at most one pair is equal. The only possible sums are therefore zero, one, or three.
- **Column-name case:** The lowercase `c` in `B = c` resolves to column `C` under MySQL's identifier rules; it is not a separate variable or string literal.
