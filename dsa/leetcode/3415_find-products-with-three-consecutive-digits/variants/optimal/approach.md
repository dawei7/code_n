## General

A qualifying substring consists of three digit characters with a non-digit or the beginning of the name immediately before it, and a non-digit or the end of the name immediately after it. Those two boundary checks are what distinguish an exact three-digit run from three characters selected out of `1234` or another longer run.

The accepted MySQL query expresses the four boundary possibilities compactly with `(^|[^0-9])[0-9]{3}([^0-9]|$)`. The app-local SQLite query adds a non-digit sentinel `x` to both ends of every name, turning beginning and end boundaries into ordinary non-digit boundaries. Its `GLOB` pattern then searches for a non-digit, three digits, and another non-digit anywhere in the padded string.

Each row is filtered independently, so a name with several qualifying runs still produces one result row. Finally, ordering by the unique `product_id` gives the required deterministic ascending result.

## Complexity detail

Let $n$ be the row count and $S$ the total number of characters in all product names. Matching scans the name text in $O(S)$ time, while ordering at most $n$ selected rows costs $O(n\log n)$. The conservative total is $O(S+n\log n)$. The result ordering can use $O(n)$ auxiliary space.

The benchmark defines `size` as $n$ and keeps every product name at a fixed length, making $S=\Theta(n)$. Its 32, 128, and 256 reverse-ordered rows span 8x and mix qualifying and nonqualifying digit runs. The accepted-class filter scales linearly before result ordering. A correct baseline that cross joins the table to itself and groups back to one row per product performs quadratic work and must fail only the scaling verdict.

## Alternatives and edge cases

- **Search for any three adjacent digits:** This incorrectly accepts a three-character slice of a four-digit or longer run.
- **Enumerate start, middle, and end patterns separately:** This can work, but sentinels reduce the boundary cases to one app-local pattern.
- **Return one row per matching substring:** The requested entity is the product, so multiple qualifying runs in one name must not duplicate its row.
- **Exactly three digits as the whole name:** Both boundaries are supplied by the sentinels or regex anchors, so the row qualifies.
- **Leading zeros:** `003` is a three-character digit run and qualifies normally.
- **Separated shorter runs:** A name such as `A12B34C` has no three-digit run and must be excluded.
- **Longer run plus a valid run:** A name such as `A1234B567C` qualifies because `567` is independently bounded.
- **Output ordering:** Sort by `product_id` even when table insertion order differs.
