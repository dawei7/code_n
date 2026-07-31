## Function Contract

**Inputs**

- `num`: The positive integer whose decimal prefixes and suffixes must be examined.

For every length $k$ from 1 through the number of decimal digits, take both the first $k$ digits and the last $k$ digits as integers. The complete number itself is therefore included in both families. A prime is an integer greater than 1 with no positive divisors other than 1 and itself.

**Return value**

Return `true` if every required prefix and suffix is prime. Return `false` as soon as any one of them is nonprime.
