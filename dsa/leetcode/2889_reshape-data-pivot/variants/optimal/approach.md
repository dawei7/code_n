## General

The input already provides the three roles required by a pivot: `month` identifies output rows, `city` identifies output columns, and `temperature` supplies the cell values. Calling pandas `pivot` with exactly those roles reshapes the observations directly, without inventing an aggregation rule or modifying any temperature.

Each city-month pair identifies one input value, so every observation has one unambiguous output cell. pandas orders the distinct row and column labels and places the corresponding integer in each intersection. For the app-local representation, resetting the pivoted month index exposes `month` as the first ordinary column; the native LeetCode form leaves that label as the DataFrame index, which its judge renders identically.

## Complexity detail

Let $r$ be the number of observations, $c$ the number of distinct cities, and $m$ the number of distinct months. Building and ordering the pivot keys takes $O(r \log r)$ time in the general case, and materializing the wide result takes $O(cm)$ time. Together this is $O(r \log r + cm)$ time. The result contains $cm$ temperature positions, so it uses $O(cm)$ space.

## Alternatives and edge cases

- **`pivot_table` with aggregation:** A pivot table can produce the same shape when given an explicit aggregation such as `first`, but aggregation is unnecessary because each city-month pair already identifies one value.
- **Default mean aggregation:** Using `pivot_table` without an explicit aggregation may convert integer temperatures to averaged floating-point values, changing the required representation.
- **Manual nested searches:** Enumerating every month-city pair and rescanning all observations for its value is correct but can take $O(r^2)$ time on a complete grid.
- **Input order:** The long-form rows need not be grouped by city or month; the pivot keys, rather than input position, determine placement.
- **Negative temperatures:** Signed integer values must be copied unchanged into their corresponding cells.
- **Label placement:** Months form rows and cities form columns; swapping these roles produces the transpose of the required result.
