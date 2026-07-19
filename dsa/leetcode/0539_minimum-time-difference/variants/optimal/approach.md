## General
**Map every time to a minute of the day**

Convert `HH:MM` into `60 * hour + minute`, an integer from `0` through `1439`. Mark that position in a fixed Boolean array representing the entire clock.

**Detect duplicate times while marking**

If a minute is already marked, two inputs coincide and the minimum possible difference is zero, so return immediately. The pigeonhole principle gives the same conclusion whenever more than `1440` times are supplied.

**Scan occupied minutes in chronological order**

Walk the fixed minute array, comparing each occupied minute with the previous occupied minute. Record the first and last occupied positions as well as the smallest adjacent gap.

**Close the circle across midnight**

The chronological scan does not directly compare the last time of the day with the first time. Their circular separation is `first + 1440 - last`; minimize the result with this wraparound gap.

**Why adjacent clock positions are sufficient**

After sorting positions around a circle, any nonadjacent pair contains at least one adjacent arc no longer than its total separation. Therefore the minimum pair must be consecutive in chronological order or the wraparound pair. The scan checks exactly those candidates.

## Complexity detail
Parsing `n` inputs takes $O(n)$ time, and scanning all `1440` possible minutes is constant work, so total time is $O(n)$. The Boolean array always has `1440` entries, giving $O(1)$ auxiliary space relative to input size.

## Alternatives and edge cases
- **Sort converted minutes:** is concise and checks the same adjacent gaps, but costs $O(n \log n)$ time.
- **Compare every pair:** handles circular distance directly but takes $O(n^2)$ time.
- **Set plus sorted values:** detects duplicates easily but still pays sorting cost.
- **Duplicate time:** immediately makes the answer zero.
- **Midnight boundary:** `23:59` and `00:00` differ by one minute, not `1439`.
- **Exactly opposite times:** can have a difference of `720` minutes.
- **Unordered input:** has no effect because minute positions determine chronological order.
