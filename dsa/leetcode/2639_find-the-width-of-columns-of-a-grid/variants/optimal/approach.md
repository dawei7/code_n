## General

Each output position depends on exactly one matrix column. For a fixed column, convert every value to its ordinary decimal string and take the greatest resulting length. Python's conversion already includes a minus sign for negative values, counts zero as one character, and adds no sign to nonnegative values, so it matches the width definition directly.

Process column indices from left to right. For each index, scan all $m$ rows and append the maximum observed length to the answer. Every matrix cell contributes to the maximum for its own column exactly once. Consequently, when a column's scan ends, its stored maximum is the width required by the contract; collecting these maxima in column order produces the complete answer.

## Complexity detail

There are $n$ columns and $m$ entries in each column, so the scan performs $O(mn)$ conversions. Each input value is bounded by $10^9$ in magnitude, making its decimal representation at most eleven characters long; under this contract, conversion cost is constant. The returned array occupies $O(n)$ space, while the scan itself uses $O(1)$ auxiliary state.

## Alternatives and edge cases

- **Arithmetic digit counting:** Repeated division can count digits without creating strings, but it needs explicit handling for zero and a separate increment for a negative sign, making it more error-prone without changing the asymptotic cost.
- **Row-wise accumulation:** Maintaining an $n$-entry maximum array while traversing rows is equally optimal and may fit row-major processing better; the column-wise form mirrors the requested output directly.
- A minus sign contributes one character, so `-9` has width two while `9` has width one.
- Zero has width one even though it has no nonzero digits.
- The matrix is guaranteed to contain at least one row and one column, so each column maximum is taken over a nonempty set.
