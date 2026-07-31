## General

The required correction concerns one complete column rather than individual rows. pandas can cast the `grade` Series directly with `astype(int)`, applying the same integer conversion to every grade in a vectorized operation. Assigning that converted Series back under the same column label changes its dtype while preserving the table's schema and row index.

Only `grade` is replaced. The `student_id`, `name`, and `age` columns remain untouched, and assigning a Series with the same index keeps each converted grade aligned with its original student. Returning the resulting DataFrame therefore preserves all rows and values while enforcing the requested integer representation.

## Complexity detail

Let $n$ be the number of student rows. Casting the grade Series examines and writes each of its $n$ values once, so the running time is $O(n)$. The converted Series and returned table representation require $O(n)$ space.

## Alternatives and edge cases

- **DataFrame dictionary cast:** `students.astype({"grade": int})` expresses the same targeted conversion and returns a converted DataFrame, but casting the named Series makes the single changed column explicit.
- **Row-by-row reconstruction:** Converting each grade while repeatedly concatenating one-row DataFrames is correct but may take $O(n^2)$ time because the growing table is copied repeatedly.
- **Rounding first:** Applying `round`, `floor`, or `ceil` would introduce a numerical transformation that the contract does not request; the input grades are already integer-valued floats.
- **Targeted dtype:** Only `grade` should become integer-valued; identifiers, names, ages, column order, and row order must remain unchanged.
- **Boundary grades:** Values such as `0.0` and `100.0` must become `0` and `100` without being dropped or treated as missing.
