## General

The decision for an occurrence depends on its value's frequency in the complete array, so first count every value. Because the contract restricts values to `1` through `100`, a fixed array indexed by value stores all frequencies without hashing.

After counting, inspect each possible value. A positive frequency qualifies exactly when `frequency % k == 0`. Add `value * frequency` so every copy contributes, as required by the source Note. Values with zero frequency are ignored; although zero is mathematically divisible by `k`, absent values contribute nothing and are not array elements.

The frequency array contains the exact total count for every possible value, so the divisibility test includes precisely the qualifying value classes. Multiplying each qualifying class by its count is identical to summing its individual occurrences. Their accumulated total is therefore the required answer.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Counting takes $O(n)$ time, and scanning the fixed 101-entry domain takes $O(1)$ time, so total time is $O(n)$. The frequency array has a contract-bounded size and therefore uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Hash-frequency map:** A counter keyed only by observed values also takes $O(n)$ expected time and is convenient when the value domain is not bounded; here the fixed array makes the bound explicit.
- **Count each occurrence separately:** Calling a full-array count for every element repeats work and can take $O(n^2)$ time.
- **Add each qualifying value once:** This misses multiplicity; the Note requires adding `value * frequency`.
- **No qualifying frequency:** The accumulator remains `0`, which is the required fallback.
- **`k = 1`:** Every positive frequency is divisible by one, so the result is the ordinary sum of `nums`.
- **`k` larger than the array length:** No positive frequency can be divisible by `k`, so the answer is `0`.
- **Absent values:** A stored count of zero must not cause a nonexistent value to be treated as qualifying.
