## General

Tracking only each number's current count makes `add` and `deleteOne` easy, but answering `hasFrequency` would require scanning every stored number. Add a second hash map whose key is a positive frequency and whose value is the number of distinct numbers currently having that frequency.

When a number moves from frequency $f$ to $f + 1$, decrement the population of bucket $f$ when $f > 0$, update the number's own count, and increment bucket $f + 1$. Deletion performs the symmetric move from $f$ to $f - 1$; if $f = 0$, it does nothing, and frequency zero is never recorded as an occupied bucket.

After every mutation, the first map gives the exact multiplicity of each number. The second map is updated for both the departed and entered positive frequencies, so its entry for any $f$ equals the number of values whose multiplicity is exactly $f$. Therefore `hasFrequency(f)` is precisely the constant-time test that this bucket population is positive.

## Complexity detail

Each operation performs a constant number of expected $O(1)$ hash-map accesses, so `add`, `deleteOne`, and `hasFrequency` each take $O(1)$ expected time. If $n$ distinct numbers have appeared, the maps use $O(n)$ space; stale zero-valued entries created by queries are bounded by the number of operations.

## Alternatives and edge cases

- **One frequency map:** Storing only number multiplicities uses simple updates, but each query may scan all distinct numbers and take $O(n)$ time.
- **Fixed arrays:** The numeric and call bounds permit arrays instead of hash maps, trading a predictable $O(10^5)$ allocation for lower constant factors.
- Deleting an absent number must not create a negative count or alter any frequency bucket.
- Frequency zero is not queryable and must not be treated as occupied by absent numbers.
- When one number leaves a bucket that still contains another number, `hasFrequency` for that bucket remains true.
