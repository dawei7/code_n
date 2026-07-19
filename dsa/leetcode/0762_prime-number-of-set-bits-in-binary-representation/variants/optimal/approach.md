## General
**Count bits for every value in the interval**

Visit each integer from `left` through `right` once. A population-count operation gives the number of `1` bits in its binary representation. Increment the answer exactly when that count belongs to the fixed set of primes.

**Why the prime set is constant**

The input values have a bounded machine-word size, so their population count also has a small fixed upper bound. The only relevant prime counts are `2, 3, 5, 7, 11, 13, 17, 19`. Membership in this constant set takes constant expected time.

Each range value contributes once. The algorithm increments for a value precisely when its set-bit count is in the prime set, which is the definition of a qualifying integer. The final total therefore counts exactly the requested values.

## Complexity detail
Let `n = right - left + 1`. With a fixed-width population-count operation and constant-size prime lookup, the scan takes $O(n)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Prime bit mask:** Encode all prime bit counts in one integer and test the population count with a shift and mask; this has the same $O(n)$ time and $O(1)$ space.
- **Explicit bit loop:** Repeatedly clear the lowest set bit or shift each number to count ones, adding a logarithmic factor when integer width is treated as variable.
- **Test primality separately:** Trial division is unnecessary because the possible counts are tiny and fixed.
- **One-element range:** Return either zero or one according to that value's bit count.
- **Counts zero and one:** Neither is prime.
- **Powers of two:** They have one set bit and never qualify.
- **Inclusive upper endpoint:** The loop must examine `right` itself.
