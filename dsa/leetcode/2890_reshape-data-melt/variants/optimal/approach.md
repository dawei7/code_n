## General

The `product` column is already the identifier that must remain attached to every measurement. The four quarter columns are the measured variables: their column names must become values in the new `quarter` column, while their cells must become values in `sales`. pandas `melt` expresses those roles directly by retaining `product` as an identifier and unpivoting the quarter columns in their listed order.

For each quarter, `melt` traverses the products in their existing row order and emits one result row per product. It repeats each product beside the selected quarter name and copies the matching integer into `sales`. Consequently, every input cell from the four quarter columns appears exactly once, attached to its original product and its original quarter, and the output contains exactly $4n$ rows.

## Complexity detail

Let $n$ be the number of products. The quarter count is fixed at four, so reading the four sales values for every product and constructing $4n$ output rows takes $O(n)$ time. The returned DataFrame contains $4n$ rows and therefore uses $O(n)$ space; this output space is unavoidable.

## Alternatives and edge cases

- **Explicit concatenation:** Building one two-column slice per quarter, adding the quarter label, and concatenating the four slices is also linear, but it repeats the same column-selection and renaming work that `melt` represents directly.
- **Row-by-row concatenation:** Appending a one-row DataFrame for each product-quarter pair preserves the required order, but repeatedly copying the growing result can take $O(n^2)$ time.
- **Product-major iteration:** Looping over products before quarters creates the same product-quarter pairs in a different order; the required result groups rows by quarter first.
- **Repeated sales values:** Equal integers in different cells remain distinct records because `product` and `quarter`, not the numeric value, identify a measurement.
- **Signed and zero values:** Sales values are copied without filtering or arithmetic, so zero and negative integers retain their exact values.
- **Column names:** The output uses the literal source labels `quarter_1` through `quarter_4` in `quarter`, not numeric quarter indices.
