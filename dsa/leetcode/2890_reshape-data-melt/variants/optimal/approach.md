## General

**Melt is the inverse shape of a pivot.** The input is wide: one product row contains four separate quarter columns. The desired result is long: each product-quarter combination becomes its own row, with the former column name stored in `quarter` and the former cell value stored in `sales`.

The exact solution calls:

`pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')`.

Each argument defines one part of that reshape.

**`id_vars` identifies data that stays descriptive.** `product` is not melted. Instead, its value is repeated as needed so every generated sales row still says which product it belongs to. With four quarter columns, each original product appears four times in the result.

For example, `Umbrella` remains paired with sales from `quarter_1`, `quarter_2`, `quarter_3`, and `quarter_4`. Repetition is necessary because the original single row is becoming four rows.

**Unlisted columns become measured variables.** The source does not provide `value_vars`. pandas therefore melts every input column not listed in `id_vars`. Under the exact schema, those columns are the four quarters and nothing else. This shorter call is equivalent here to explicitly listing all four quarter labels.

In a more general DataFrame with an unexpected additional non-product column, this exact source would melt that column too. Its correctness relies on the promised five-column schema.

**`var_name` stores former headers.** The names `quarter_1` through `quarter_4` used to be column labels. After melting, those label strings become row values in a new column named `quarter`. This preserves which period each sales number came from.

**`value_name` stores former cells.** The numeric content from the quarter columns is stacked into a new column named `sales`. An input value `417` at Umbrella and `quarter_1` becomes one result row with product Umbrella, quarter `quarter_1`, and sales `417`.

**Output order follows the value-column traversal.** With normal pandas melt behavior and the input's quarter-column order, rows for `quarter_1` are emitted for all products, then rows for `quarter_2`, and so on. This matches the example: Umbrella and SleepingBag for the first quarter precede the same two products for the second quarter.

The source does not sort the output afterward. If the input quarter columns appeared in a different order, the long rows would follow that schema order.
Take any original product row $p$ and any quarter column $q$. `melt` creates exactly one output row whose `product` equals the identifier at $p$, whose `quarter` equals label $q$, and whose `sales` equals original cell $(p,q)$. Conversely, every output row comes from one such original quarter cell. Therefore no sales value is lost, duplicated beyond its one necessary long-format row, or attached to the wrong product or quarter.

**Row count changes predictably.** If input has $n$ products and four quarter columns, the output has $4n$ rows and three columns. Reshaping increases row count but reduces the number of measurement columns. The total number of sales observations remains $4n$.

**Index handling.** `pd.melt` uses `ignore_index=True` by default, so the result receives a fresh zero-based index rather than repeating each original row label four times. The task's displayed table concerns the three data columns, and this default index behavior fits it.

**The source returns a new DataFrame.** It does not modify `report` in place. The wide source remains available if the caller keeps its reference. The long result owns the reshape metadata and repeated identifier values according to pandas' allocation strategy.

**Melt preserves observation meaning while changing layout.** No quarter totals are recomputed and no products are combined. Reshaping is lossless here: given unique product rows, the long table can conceptually be pivoted back to recover the four original quarter columns.

## Complexity detail

Let $n$ be the number of products and $q$ the number of melted quarter columns. Every one of the $nq$ measurement cells becomes one output row, so time and output space are $O(nq)$. Here $q=4$ is fixed by the schema, reducing both to $O(n)$ as stated in the manifest.

The result has exactly three columns but $4n$ rows. Even though the call is one line, it necessarily allocates data proportional to that expanded output.

## Alternatives and edge cases

- **Explicit `value_vars`:** Listing the four quarter labels makes the accepted schema narrower and prevents accidental melting of extra columns.
- **`DataFrame.melt` method:** `report.melt(...)` is equivalent to the top-level `pd.melt(report, ...)` used by the source.
- **Manual row construction:** Nested loops can emit product-quarter records but are slower and more error-prone than the native reshape.
- **Unexpected extra column:** Because `value_vars` is omitted, every non-product column would be melted.
- **Missing sales value:** It remains a missing `sales` entry; melt reshapes but does not fill or drop data.
- **Empty report:** The result is empty but still has `product`, `quarter`, and `sales` columns.
- **Quarter-column order:** It controls the block order of output rows because no explicit sort follows.
- **Original index:** Default melt behavior creates a fresh result index rather than preserving repeated source labels.
