## General

**Respect the compression weights.** A row with `item_count = x` and
`order_occurrences = f` contributes `x * f` items across `f` represented
orders. Summing `item_count * order_occurrences` therefore reconstructs the
total number of items without expanding the compressed rows. Separately sum
`order_occurrences` to obtain the total number of represented orders.

Divide those two totals and round the quotient to two decimal places. The
app-local SQLite query multiplies by `1.0` before division to guarantee real
rather than integer arithmetic; the native MySQL division already preserves
the required fractional value. Since both sums include every compressed row,
their quotient is exactly the mean over the uncompressed multiset.

## Complexity detail

Let $R$ be the number of rows in `Orders`. Both aggregates are accumulated in
one scan, so time is $O(R)$ and the aggregate state uses $O(1)$ auxiliary
space.

## Alternatives and edge cases

- **Expand every represented order:** This gives the same mean but can require work proportional to the sum of all occurrences rather than the compressed row count.
- **Cross join duplicated rows:** Repeating every row the same number of times leaves the ratio unchanged, but introduces quadratic intermediate work.
- **Ordinary `AVG(item_count)`:** This incorrectly weights every compressed row equally and ignores `order_occurrences`.
- **Fractional results:** Force non-integer division before applying the two-decimal rounding.
- **Highly skewed frequencies:** A row with many occurrences must influence both the numerator and denominator by the same frequency.
