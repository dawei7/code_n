## General

The output position `(i, j)` corresponds exactly to the input rows `i`, `i + 1`, and `i + 2` and input columns `j`, `j + 1`, and `j + 2`. Since the output has side length `n - 2`, iterating both output coordinates enumerates every legal $3 \times 3$ window once.

**Evaluate the fixed window directly.** For each output position, inspect the nine combinations of row offset and column offset from `0` through `2`, take their maximum, and append it to the output row. Adjacent windows may share cells, but their maxima remain independent.

This writes exactly the requested value because the nine inspected coordinates are precisely the contiguous window beginning at `(i, j)`. The loop covers every possible top-left coordinate and no invalid coordinate, so the resulting dimensions and all entries match the contract.

## Complexity detail

There are $(n-2)^2$ output cells, and each examines exactly nine input cells. The time is therefore $O(9(n-2)^2) = O(n^2)$. The returned matrix contains $(n-2)^2$ values, so total output space is $O(n^2)$; excluding the required result, the auxiliary working space is $O(1)$.

## Alternatives and edge cases

- **Two-pass sliding maxima:** Horizontal width-three maxima followed by vertical width-three maxima also runs in $O(n^2)$ time, but it adds intermediate storage without improving the asymptotic bound for a fixed window.
- **Scan the entire matrix per output:** Filtering every input cell for each window is correct but takes $O(n^4)$ time.
- **Minimum dimension:** When `n = 3`, the output contains exactly one value: the maximum of the whole input.
- **Overlapping windows:** A large interior value may determine several neighboring output entries.
- **Boundary windows:** The final legal top-left coordinate is `(n - 3, n - 3)`, which reaches the last input row and column.
- **Positive values:** Initializing a running maximum to zero would be safe under this contract, but deriving it from the actual nine values avoids relying on that detail.
