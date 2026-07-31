## General

Both inputs already have the same columns, so no key matching or schema alignment rule needs to be invented. A single pandas `concat` call receives the two DataFrames in the required order and uses the row axis, which is the default axis. pandas therefore copies the rows of `df1` first and appends the rows of `df2` after them.

Setting `ignore_index=True` assigns the combined rows a fresh continuous index without changing their relative order. Concatenation preserves repeated rows and repeated student identifiers because it performs no grouping, joining, sorting, or deduplication. The resulting three columns and their values are consequently exactly the vertical stack required by the contract.

## Complexity detail

Let $n$ and $m$ be the row counts of `df1` and `df2`. Constructing the combined DataFrame copies all $n + m$ rows once, so the time complexity is $O(n + m)$. The returned table stores those rows and therefore uses $O(n + m)$ space.

## Alternatives and edge cases

- **Concatenate then reset the index:** Calling `pd.concat([df1, df2]).reset_index(drop=True)` also gives a continuous index, but `ignore_index=True` expresses the same requirement within the concatenation itself.
- **Horizontal concatenation:** Using `axis=1` places columns side by side and does not satisfy the requested vertical row stacking.
- **Merge or join:** Key-based combination can match, discard, or multiply rows according to identifier values; this task requires unconditional stacking instead.
- **Repeated rows:** Equal rows from the two inputs must both remain in the result because concatenation does not deduplicate data.
- **Input order:** All rows from `df1` precede all rows from `df2`, and each table's internal row order is preserved.
- **Shared schema:** The inputs have the same ordered columns, so the result must remain `student_id`, `name`, `age` without introducing extra columns.
