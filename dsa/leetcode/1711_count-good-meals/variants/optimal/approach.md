## General
**Count only partners that appeared earlier**

Scan the array from left to right and maintain a frequency map of values already seen. For the current value `x`, a previous value `y` forms a good meal exactly when `y = power - x` for some legal power of two. Add the stored frequency of each such complement, then insert `x` into the map.

Because insertion happens after the queries, every counted partner has a smaller index. Thus no item pairs with itself and every unordered index pair is counted at the moment its later item is processed, exactly once.

**Bound the target powers**

Every value is at most $2^{20}$, so a pair sum lies from $0$ through $2^{21}$. Zero is not a power of two. Checking $2^0,2^1,\ldots,2^{21}$ therefore covers every possible good sum without testing irrelevant larger targets.

Repeated values are handled by frequencies rather than by distinct-value membership. If a complement has appeared `c` times, the current index creates `c` different meals. Reduce the final count modulo $10^9+7$.

## Complexity detail
For each of the $n$ items, exactly $B=22$ powers are tested with expected $O(1)$ hash-map lookup, for $O(nB)$ expected time. The map contains at most $n$ distinct values and uses $O(n)$ space.

## Alternatives and edge cases
- **Check every index pair:** direct nested loops are correct but take $O(n^2)$ time.
- **Sort and use two pointers per power:** repeating a two-pointer scan for all powers takes $O(n\log n+nB)$ time and complicates duplicate counting.
- **Frequency combinations after a full count:** iterating distinct complements can work, but requires careful division or ordering to avoid double-counting equal and unequal values.
- **Duplicate values:** different indices remain different items; use the full previous frequency, not a Boolean membership test.
- **Zero values:** two zeros sum to zero and do not qualify, but zero can pair with a positive power of two.
- **Two equal powers:** values such as two ones may pair because their sum is the next power of two.
- **Maximum values:** two values equal to $2^{20}$ produce the legal target $2^{21}$, so the highest target must be included.
- **Single item:** no pair exists, so the answer is zero.
- **Large pair counts:** apply the required modulus because the raw number can exceed 32-bit range.
