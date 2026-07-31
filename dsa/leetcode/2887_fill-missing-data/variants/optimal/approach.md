## General

The requested replacement is confined to the `quantity` Series. pandas `fillna(0)` identifies every missing entry in that Series and produces the corresponding quantity values with `0` in those positions. Assigning the result back under the same column name keeps the DataFrame's existing schema and index.

Non-missing quantities pass through `fillna` unchanged. Because the replacement Series retains the original index, each value remains aligned with its product row. No operation touches `name` or `price`, so returning the updated DataFrame satisfies both the missing-value correction and the data-preservation requirements.

## Complexity detail

Let $n$ be the number of product rows. pandas examines the $n$ quantity entries once, giving $O(n)$ time. The filled Series and returned table representation require $O(n)$ space.

## Alternatives and edge cases

- **Dictionary-based DataFrame fill:** `products.fillna({"quantity": 0})` also targets only `quantity` and produces the same result, but assigning the named Series makes the changed column especially explicit.
- **Blanket DataFrame fill:** Calling `products.fillna(0)` without a column mapping can incorrectly replace missing cells in `name` or `price`, even though the task requests only quantity correction.
- **Row-by-row reconstruction:** Testing each row and repeatedly concatenating one-row DataFrames is correct but may take $O(n^2)$ time as the growing result is copied.
- **No missing quantities:** When every quantity is already present, all values and row order must remain unchanged.
- **All quantities missing:** Every missing position independently becomes `0`; no product row is removed.
- **Existing zero quantities:** A stored `0` is already valid and remains `0`; it must not be confused with a missing value.
