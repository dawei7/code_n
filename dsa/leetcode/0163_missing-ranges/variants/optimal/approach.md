## General

**Advance a frontier between present values**

The bounded numeric interval may be far wider than `nums`, so inspect only the sorted values that are present. Keep
`next_missing`, the smallest value not yet classified, starting at `lower`.

For each present `value`, emit `[next_missing, value - 1]` when `next_missing < value`. Sorted uniqueness guarantees
that the complete interval is absent and maximal. Then set `next_missing = value + 1`, classifying the current value
as present. After the scan, emit `[next_missing, upper]` when the frontier has not passed the upper bound.

Before each iteration, every bounded integer below `next_missing` has been classified exactly once as present or as
part of an emitted range, and nothing from the frontier onward has been emitted. The gap check and one-step advance
preserve that property. The final suffix check classifies everything that remains, so the output is sorted, complete,
contains no present value, and uses one maximal range for each missing run.

The implementation always returns two endpoints, including `[x, x]` for a single missing integer, matching the
source-native output contract.

## Complexity detail

Each of the $n$ present values is processed once, giving $O(n)$ time independent of `upper - lower`. Apart from the
returned ranges, the frontier and loop value use $O(1)$ auxiliary space. The output itself can contain $O(n)$ ranges.

## Alternatives and edge cases

- **Scan every bounded integer:** can take time proportional to `upper - lower`, which may approach $2 \times 10^9$.
- **Use list membership during a numeric scan:** adds an $O(n)$ search per value and can be quadratic even on a
  narrow interval.
- **Convert `nums` to a set:** adds $O(n)$ storage and still leaves work proportional to the numeric width.
- **Use `lower - 1` and `upper + 1` sentinels:** is concise in Python but may overflow fixed-width integer types.
- An empty array yields the whole bounded interval as one range.
- If every bounded value is present, the result is empty.
- Missing prefixes, suffixes, and singleton gaps all follow from the same frontier comparisons.
