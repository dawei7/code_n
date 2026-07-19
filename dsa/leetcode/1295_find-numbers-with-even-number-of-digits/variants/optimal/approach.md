## General
The constraint $1 \le x \le 100000$ permits only one through six decimal digits. The even-length ranges are therefore $[10,99]$ for two digits, $[1000,9999]$ for four digits, and the single six-digit value $100000$.

Scan the array once. Increment the answer whenever the current value lies in one of those three ranges. These ranges are disjoint and collectively contain every legal value with an even number of digits, so each qualifying element is counted exactly once and every nonqualifying element is excluded.

## Complexity detail
The scan performs a constant number of comparisons for each of the $n$ values, giving $O(n)$ time. The counter and current value use $O(1)$ auxiliary space; no string representation or frequency table is created.

## Alternatives and edge cases
- **String conversion:** Testing `len(str(value)) % 2` is concise, but creates a temporary representation and ignores the small fixed value domain.
- **Repeated division by ten:** Counting digits arithmetically works in $O(d)$ per value, where $d$ is its digit count, but the fixed range checks are simpler here.
- **Powers of ten:** Values 10, 1000, and 100000 begin even-digit ranges, while 100 and 10000 begin odd-digit ranges.
- **Repeated values:** Every occurrence contributes independently to the result.
- **Smallest value:** One has one decimal digit and does not qualify.
