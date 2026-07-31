## General

The result depends on three consecutive transformations. First, the strict predicate `weight > 100` removes every row at or below the boundary. Second, sorting the retained rows by `weight` in descending order establishes the required output order. Finally, selecting `[["name"]]` keeps the result as a one-column DataFrame instead of reducing it to a Series.

These transformations can be chained because each produces another DataFrame. The filter preserves every column needed by the later sort, the sort permutes whole rows so each name stays attached to its weight, and the final projection discards the now-unneeded fields. Thus a name appears exactly when its original weight passes the strict threshold, and the sequence of names follows non-increasing weight.

## Complexity detail

Let $n$ be the number of input animals and $h$ the number with weight strictly greater than $100$. Filtering scans all rows in $O(n)$ time. Sorting the $h$ retained rows takes $O(h \log h)$ time, and projecting their names takes $O(h)$ time, for $O(n + h \log h)$ overall. The filtered and sorted result contains $h$ rows, so the operation uses $O(h)$ space.

## Alternatives and edge cases

- **`query` plus `sort_values`:** `animals.query("weight > 100")` can replace boolean indexing and has the same asymptotic cost, though the direct comparison keeps the threshold visible as ordinary Python syntax.
- **Repeated maximum selection:** Finding and removing the heaviest remaining animal one at a time is correct but can take $O(h^2)$ time because each selection rescans the remaining rows.
- **Sorting the full input first:** Ordering all $n$ animals before filtering is correct, but it may sort many rows that will be discarded and costs $O(n \log n)$ even when $h$ is small.
- **Strict boundary:** An animal weighing exactly $100$ kilograms must not appear; the condition is greater than, not greater than or equal to.
- **Empty result:** If no weight exceeds $100$, return an empty DataFrame that still has the `name` column.
- **DataFrame shape:** Double brackets are material: selecting `[["name"]]` returns the required DataFrame, whereas `["name"]` returns a Series.
