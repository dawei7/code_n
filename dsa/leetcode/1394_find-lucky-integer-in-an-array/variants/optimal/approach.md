## General
Count every array value in a hash table during one pass. Then examine each `(value, frequency)` pair and retain the largest value for which `value == frequency`.

The counter contains the exact multiplicity of every distinct input value, so the equality test accepts precisely the lucky integers. Taking the maximum among all accepted values implements the required tie rule. Starting from `-1` also supplies the required result when no pair qualifies.

## Complexity detail
Counting $n$ entries and scanning $u \le n$ distinct keys takes $O(n)$ expected time. The frequency table stores $u$ entries and uses $O(u)$ space.

## Alternatives and edge cases
- **Count by rescanning the array:** Calling a linear frequency operation for every distinct value is correct but can require $O(nu)$, or $O(n^2)$, time.
- **Fixed frequency array:** Because values are at most 500, an array of 501 counters also gives $O(n)$ time and $O(1)$ space relative to the fixed domain.
- **Several lucky values:** Return the numerically largest one, not the most recently encountered one.
- **Value one:** A single occurrence of `1` is lucky.
- **Near miss:** A value occurring one too many or one too few times is not lucky.
- **No lucky value:** Return `-1`, even though all input values are positive.
