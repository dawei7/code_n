## General
The numeric interval may be enormous, so the algorithm must move between the values that are present rather than inspect every integer. Keep `next_missing`, the smallest value in `[lower, upper]` that has not yet been classified. Initially it is `lower`.

Process the sorted values from left to right. For a current present value `value`:

- If `next_missing < value`, no array element can occur between them because the input is sorted. Therefore `[next_missing, value - 1]` is one complete maximal missing range; append it.
- The current value is present, so the next possible missing value becomes `value + 1`.

After all present values have been consumed, `[next_missing, upper]` is the remaining missing suffix if `next_missing <= upper`.

For `[0, 1, 3, 50, 75]` within `[0, 99]`, the first two values simply advance the frontier to `2`. Seeing `3` emits `[2, 2]` and moves the frontier to `4`; seeing `50` emits `[4, 49]`; seeing `75` emits `[51, 74]`. The final frontier `76` produces `[76, 99]`. Notice that a one-value gap remains a two-endpoint range, such as `[2, 2]`.

The useful invariant is that, before processing each present value, every bounded integer smaller than `next_missing` has been classified exactly once as either present or part of an emitted range, while nothing from `next_missing` onward has been emitted. Emitting the gap and stepping past the current present value preserves this frontier.

Whenever `next_missing < value`, sorted uniqueness proves that every integer from `next_missing` through `value - 1` is absent. The values immediately outside that interval are either a bound or present values, so the emitted range is maximal and cannot be merged with another missing range. Advancing to `value + 1` classifies the current present value without skipping any candidate. After the scan, the only unclassified values form the possible suffix through `upper`. Consequently the output covers every missing value exactly once, contains no present value, and uses the shortest sorted list of inclusive ranges.

## Complexity detail
Each input value is processed once, so the running time is $O(n)$ regardless of the width `upper - lower`. Apart from the returned ranges, the algorithm uses one frontier variable and therefore $O(1)$ auxiliary space.

## Alternatives and edge cases
- Iterating from `lower` to `upper` is proportional to the numeric range, which can be vastly larger than `n`.
- Converting `nums` to a set adds $O(n)$ storage and does not solve the wide-range iteration problem.
- A sentinel formulation with `lower - 1` and `upper + 1` is concise in Python, but those expressions can overflow fixed-width integer types. The `next_missing` formulation can instead use boundary checks or a wider integer type.
- An empty input yields the whole interval as one missing range. If every bounded value is present, the result is empty.
- Missing prefixes, suffixes, and a single missing integer all follow from the same frontier checks without special output formatting.
