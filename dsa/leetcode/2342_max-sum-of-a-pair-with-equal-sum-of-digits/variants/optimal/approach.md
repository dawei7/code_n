## General

An eligible pair must come from one digit-sum group. Within any such group,
the best pair consists of its two largest values. Rather than store and sort
every group, process the array once while remembering only the largest value
already seen for each digit sum.

**Complete a pair when its second value arrives**

Compute a value's decimal digit sum by repeated division by 10. If the group
already has a stored maximum, combine that maximum with the current value and
use the result to update the global answer. Then retain the larger of the
stored maximum and the current value for future pairs.

When the later index of the globally optimal pair is processed, its earlier
partner is no larger than the stored group maximum. The algorithm therefore
tests a pair at least as large as that optimum. Every tested pair shares a
digit sum and uses two different scan positions, so it cannot exceed the true
optimum. Hence the final maximum is exact.

Because legal values have at most ten decimal digits, their digit sums range
only from 1 through 81. A fixed array can represent all groups without
input-dependent storage.

## Complexity detail

Each of the $n$ values has at most ten digits under the contract, so all digit
sum computations and group updates take $O(n)$ time. The fixed 82-entry maximum
table uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Sort within digit-sum groups:** Grouping every value and sorting each group
  also identifies its largest two, but costs up to $O(n\log n)$ time and
  $O(n)$ space.
- **Check every index pair:** Comparing digit sums for all pairs is direct but
  costs $O(n^2)$ time.
- **Repeated equal values:** Two equal numbers may form a pair when they occupy
  different indices.
- **No compatible group:** Keep the answer at `-1` unless some digit sum occurs
  at least twice.
- **Largest legal value:** $10^9$ has digit sum 1 and is handled by the same
  fixed group table.
