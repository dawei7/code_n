## General

**Count periods by their ending day**

Let `ending_here` be the number of smooth descent periods whose final day is the current index. On the first day, its only such period is the one-day interval, so initialize `ending_here = 1` and `total = 1`.

When `prices[i - 1] - prices[i] == 1`, every valid period ending at `i - 1` can extend through day `i`, and the one-day period `[prices[i]]` is also valid. Therefore increment `ending_here`. If the difference is anything else, no multi-day period can cross that boundary, so reset `ending_here` to one.

Add `ending_here` to `total` after every day. Every smooth descent period has one unique ending index and is counted among exactly that index's valid suffixes. Conversely, the recurrence extends a suffix only across boundaries satisfying the exact-one rule, so every counted interval is valid.

## Complexity detail

The algorithm performs one constant-time update per price, for $O(n)$ time. It stores only the current suffix length and accumulated total, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every start and end:** Extend each starting day while adjacent prices differ by exactly one. This is correct but takes $O(n^2)$ time on one long smooth descent.
- **Sum run lengths arithmetically:** Split the array into maximal descent runs; a run of length $r$ contributes $r(r+1)/2$. This also takes $O(n)$ time and $O(1)$ space.
- Every individual day counts, including days adjacent to a broken boundary.
- Equal adjacent prices break a longer period.
- A drop greater than one also breaks a period because the decrease must be exactly one.
- The total can be quadratic in $n$, so fixed-width implementations need a 64-bit accumulator.
