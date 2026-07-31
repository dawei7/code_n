## General

**Classify every valid parity pattern**

Only each selected value's parity affects an adjacent sum modulo two. If the common adjacent-sum parity is zero, consecutive selected values must have equal parity. Equality then propagates through the subsequence, so every selected value is even or every selected value is odd.

If the common adjacent-sum parity is one, every adjacent pair must contain opposite parities. The selected parity sequence therefore alternates. These are the only possibilities: all even, all odd, alternating from even, or alternating from odd.

**Track the four candidates in one scan**

Count all even values and all odd values; these counts are the best lengths for the two constant-parity patterns.

For alternating patterns, maintain the longest processed subsequence ending in an even value and the longest ending in an odd value. When the current value is even, it can extend the best odd-ending subsequence, so set `alternating_end_even = alternating_end_odd + 1`. The odd-ending length is unchanged. Handle an odd value symmetrically.

The scan order preserves the subsequence constraint. The current value is later than every state it extends, and choosing it as the newest endpoint cannot reduce future options. The opposite-ending state never decreases, so each update produces the longest alternating subsequence with that endpoint among the processed prefix. Taking the maximum of the two counts and two alternating endpoints therefore covers all valid parity patterns and returns the global optimum.

## Complexity detail

The algorithm examines each of the $n$ values once and performs constant work per value, for $O(n)$ time. Four integer counters use $O(1)$ auxiliary space.

Values may be as large as $10^7$, but only `value % 2` is needed; the algorithm never depends on the numeric magnitude.

## Alternatives and edge cases

- **Quadratic subsequence DP:** Store the best valid length ending at every index for each target sum parity. This is correct but compares all ordered pairs and takes $O(n^2)$ time.
- **Build four explicit subsequences:** Greedily materializing the two alternating choices and filtering both constant parities is correct, but storing selected values uses unnecessary $O(n)$ space.
- **Assume all elements must share parity:** That covers even adjacent sums but misses alternating subsequences whose adjacent sums are all odd.
- **Two elements:** Every length-two subsequence is valid because there is only one adjacent sum to compare.
- **All one parity:** The entire array is valid with even adjacent sums.
- **Already alternating:** The entire array is valid with odd adjacent sums.
- **Repeated values:** Each occurrence is a separate selectable position and contributes to counts normally.
- **Order matters:** Equal parity totals do not determine the alternating answer; the scan must respect the original order.
- **Starting parity:** The best alternating subsequence may start with either parity, so both endpoint states are necessary.
