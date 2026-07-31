## General

For any bit position, exactly one of two situations occurs. If both values have
the bit set, it contributes once to AND and once to OR. If exactly one value
has it set, it contributes only once to OR. In either case, its total
contribution equals the number of inputs containing that bit. Therefore

$$
\operatorname{popcount}(a\mathbin{\mathrm{OR}}b)
+ \operatorname{popcount}(a\mathbin{\mathrm{AND}}b)
= \operatorname{popcount}(a)+\operatorname{popcount}(b).
$$

**Count values, not array positions**

Deduplicate `nums` because pair identity depends only on values. Count how many
unique values have each possible set-bit total. Since every value is at most
$10^9$, only buckets 0 through 30 are needed.

For every ordered pair of bucket indices $(i,j)$ with $i+j\ge k$, add the
product of their frequencies. This product selects the first value from the
$i$-bucket and the second from the $j$-bucket, so reversed pairs are counted
separately. When $i=j$, the product includes every ordered combination within
that bucket, including each valid self-pair.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Deduplication and population counting take
expected $O(n)$ time. The bucket combination checks at most $31^2$ pairs, a
fixed constant under the value constraint, so total time is $O(n)$. The set of
unique values uses $O(n)$ space; the histogram uses $O(1)$ additional space.

## Alternatives and edge cases

- **Enumerate unique value pairs:** Checking the simplified popcount condition
  for every ordered pair is correct but takes $O(u^2)$ time for $u$ unique
  values.
- **Sort population counts:** Sorting the counts and using binary search also
  works in $O(n\log n)$ time, but the fixed 31-bucket domain permits linear
  counting.
- **Duplicate inputs:** Multiple occurrences of one number still represent
  only one possible value in either pair position.
- **Self-pairs:** A single occurrence permits `(value,value)`; its doubled
  popcount must meet `k`.
- **Ordered pairs:** Distinct values contribute both orientations whenever
  their population counts qualify.
- **Large threshold:** If no two bucket indices sum to `k`, the result is 0.
