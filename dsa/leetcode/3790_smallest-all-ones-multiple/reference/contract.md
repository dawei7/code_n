## Function Contract

**Inputs**

- `k`: The positive divisor for the required all-ones integer.

“Smallest” refers to the integer's numerical value. Because each candidate extends the preceding one with another trailing `1`, this is equivalent to finding the shortest valid length. The integer itself is not returned.

**Return value**

Return the minimum positive length $L$ for which the $L$-digit repunit is divisible by `k`, or `-1` if no such length exists.
