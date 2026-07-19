## General
**Search one addend and derive the other**

Every positive decomposition of `n` has the form `a` and `n - a` for some `a` from 1 through `n - 1`. Enumerate `a` in that range and set `b = n - a`. This visits every possible positive pair exactly once up to order, so the first pair whose two decimal representations omit `0` is a valid answer.

**Test the decimal condition directly**

Convert each candidate to its decimal string and check whether it contains `"0"`. The problem guarantees that a valid decomposition exists, so the scan must return before exhausting the range. Returning immediately is important: there is no requirement to find a particular pair or to enumerate every solution.

The construction is correct because positivity follows from $1\le a<n$, the assignment `b = n - a` makes the sum exactly `n`, and the two digit tests establish the remaining No-Zero conditions. Since every eligible `a` is considered in increasing order, no valid decomposition can be skipped.

## Complexity detail
There are at most $n-1$ candidate pairs. Converting and checking an integer with at most $\lfloor\log_{10}n\rfloor+1$ digits costs $O(\log n)$ time and temporary space, giving $O(n\log n)$ worst-case time and $O(\log n)$ auxiliary space.

## Alternatives and edge cases
- **Digit-by-digit construction:** Carries can be managed while splitting each decimal digit into two nonzero digits, yielding a more intricate direct construction; the bounded search is simpler and already fits the constraints.
- **Enumerate both addends:** Trying every positive `a` and `b` independently takes $O(n^2\log n)$ time even though `b` is determined immediately by `a`.
- **Targets containing zero:** The target itself need not be No-Zero; only the two returned addends are restricted.
- **Repeated addends:** `a` and `b` may be equal, as in `[1, 1]` for `n = 2`.
- **Multiple answers:** Output order and the particular valid pair do not matter.
- **Positivity:** Zero is not a permitted addend even apart from containing the digit `0`.
