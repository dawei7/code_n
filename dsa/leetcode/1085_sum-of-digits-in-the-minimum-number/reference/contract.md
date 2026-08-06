## Function Contract

**Input**

- `nums`: a non-empty integer array.

Let $n$ be the length of `nums`, and let $D$ be the number of decimal digits in `min(nums)`.

**Return value**

- `0` if the sum of the decimal digits of `min(nums)` is odd.
- `1` if that digit sum is even.

Repeated occurrences of the minimum do not change the answer because the contract uses the minimum value, not its frequency.
